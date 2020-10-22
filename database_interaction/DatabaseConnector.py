from typing import List

class DatabaseConnector:
    def __init__(self, dbname, host, port, login, password):
        self.dbname_ = dbname
        self.host_ = host
        self.port_ = port
        self.login_ = login
        self.password_ = password

    def executeRequest(self, request: str, parameters: List[str] = None):
        pass

    def createDatabase(self):
        pass

    def dropDatabase(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

# PRIVATE FUNCTIONS:

# FIELDS:

    dbname_ = None
    host_ = None
    port_ = None
    login_ = None
    password_ = None
