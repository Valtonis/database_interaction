import sys
import psycopg2
import time
import linecache

from ..DatabaseConnector import DatabaseConnector

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print('EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj))


class PostgresqlDatabaseConnector(DatabaseConnector):
    def __del__(self):
        self.disconnect()

    def executeRequest(self, request, parameters=None):
        self.executeRequest_(request, parameters, connectToDatabase=True)

        return self.cursor_

    def createDatabase(self):
        request = "CREATE DATABASE " + self.dbname_ + ";"
        self.disconnect()
        self.connect_(connectToDatabase=False)
        self.executeRequest_(request, parameters=None, connectToDatabase=False)
        self.disconnect()

        grantRequest = "GRANT ALL ON SCHEMA public TO " + self.login_ + ";" \
                       "GRANT ALL ON SCHEMA public TO public;"

        self.connect()
        self.executeRequest_(grantRequest)
        self.disconnect()

    def dropDatabase(self):
        request = "DROP DATABASE " + self.dbname_ + ";"
        self.disconnect()
        self.connect_(connectToDatabase=False)
        self.executeRequest_(request, parameters=None, connectToDatabase=False)
        self.disconnect()

    def connect(self):
        self.connect_(connectToDatabase=True)

    def disconnect(self):
        if self.connection_ is None:
            return
        try:
            self.cursor_.close()
            del self.cursor_
            self.connection_.close()
            del self.connection_
        except:
            PrintException()

# PRIVATE FUNCTIONS:

    def executeRequest_(self, request, parameters=None, connectToDatabase=True):
        while True:
            try:
                self.cursor_.execute(request, parameters)
                return
            except psycopg2.Warning as err:
                PrintException()
            except psycopg2.InterfaceError as err:
                PrintException()
                raise err
            except psycopg2.DataError as err:
                PrintException()
                raise err

            except psycopg2.OperationalError as err:
                PrintException()
                self.disconnect()
                self.connect_(connectToDatabase)
            except psycopg2.IntegrityError as err:
                PrintException()
            except psycopg2.InternalError as err:
                PrintException()
                self.disconnect()
                self.connect_(connectToDatabase)
            except psycopg2.ProgrammingError as err:
                PrintException()
                raise err
            except psycopg2.NotSupportedError as err:
                PrintException()
                raise err

            time.sleep(5)

    def connect_(self, connectToDatabase=True):
        while True:
            try:
                if connectToDatabase == True:
                    self.connection_ = psycopg2.connect(dbname=self.dbname_,
                                                        user=self.login_,
                                                        password=self.password_,
                                                        host=self.host_,
                                                        port=self.port_)
                else:
                    self.connection_ = psycopg2.connect(user=self.login_,
                                                        password=self.password_,
                                                        host=self.host_,
                                                        port=self.port_)
                self.connection_.autocommit = True

                self.cursor_ = self.connection_.cursor()
                return
            except psycopg2.Warning as err:
                PrintException()
            except psycopg2.InterfaceError as err:
                PrintException()
                raise err
            except psycopg2.DataError as err:
                PrintException()
                raise err

            except psycopg2.OperationalError as err:
                PrintException()
                self.disconnect()
            except psycopg2.IntegrityError as err:
                PrintException()
            except psycopg2.InternalError as err:
                PrintException()
                self.disconnect()
            except psycopg2.ProgrammingError as err:
                PrintException()
                raise err
            except psycopg2.NotSupportedError as err:
                PrintException()
                raise err

            time.sleep(5)

# FIELDS:

    connection_ = None
    cursor_ = None
