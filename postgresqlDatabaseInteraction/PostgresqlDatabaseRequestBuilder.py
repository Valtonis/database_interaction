from typing import List

from ..DatabaseRequestBuilder import DatabaseRequestBuilder

class PostgresqlDatabaseRequestBuilder(DatabaseRequestBuilder):
    def getCreateTablesRequest(self) -> str:
        request = ""
        for tableStructure in self.tableStructures_:
            tableCreationRequest = "CREATE TABLE " + tableStructure.tableName_ + " ("
            for fieldName, type in tableStructure.tableFieldNamesAndTypes_:
                tableCreationRequest += fieldName + " " + type + ","
            tableCreationRequest += "PRIMARY KEY  (" + ",".join(tableStructure.primaryKeyFields_) + "),"
            for foreignKeyRecord in tableStructure.foreignKeyRecords_:
                tableCreationRequest += "FOREIGN KEY "
                tableCreationRequest += "(" + ",".join(foreignKeyRecord.tableFieldNames_) + ") "
                tableCreationRequest += "REFERENCES " + foreignKeyRecord.referenceTableName_
                tableCreationRequest += " (" + ",".join(foreignKeyRecord.referenceTableFieldNames_) + "),"
            tableCreationRequest = tableCreationRequest[:-1]
            tableCreationRequest += ");"

            request += tableCreationRequest

            for indexRecord in tableStructure.indexRecords_:
                indexesCreationRequest = "CREATE INDEX " + indexRecord.indexName_ + " "
                indexesCreationRequest += "ON " + tableStructure.tableName_ + " "
                indexesCreationRequest += "USING " + indexRecord.indexingMethod_ + " "
                indexesCreationRequest += "(" + ",".join(indexRecord.indexingFieldNames_) + ");"
                request += indexesCreationRequest

        return request

    def getRemoveTablesRequest(self) -> str:
        request = ""
        for tableStructure in reversed(self.tableStructures_):
            for indexRecord in tableStructure.indexRecords_:
                request += "DROP INDEX " + indexRecord.indexName_ + ";"
            request += "DROP TABLE " + tableStructure.tableName_ + ";"

        return request

    def getCleanTablesRequest(self) -> str:
        request = ""
        for tableStructure in reversed(self.tableStructures_):
            request += "DELETE FROM " + tableStructure.tableName_ + ";"

        return request

    def getRemoveTableRecordsRequest(self, tableName: str, ids: List[int]) -> str:
        request = "DELETE FROM " + tableName + " WHERE id IN " + "(" + ",".join(ids) + ");"

        return request

    @staticmethod
    def compileInsertRequestTemplate(table: str, fields: List[str], numberOfRecords: int = 1) -> str:
        request = "INSERT INTO " + table + " (" + ",".join(fields) + ") VALUES "
        values = "(" + ",".join(["%s" for i in range(len(fields))]) + ")"
        request += ",".join([values for i in range(numberOfRecords)]) + ";"
        return request

    @staticmethod
    def compileUpdateRequestTemplate(table: str, fields: List[str], ids: List[int] = None) -> str:
        request = "UPDATE " + table + " SET " + ",".join([f + "=%s" for f in fields])
        if ids is None:
            request += ";"
        elif len(ids) == 1:
            request += " WHERE id=" + str(ids[0]) + ";"
        else:
            request += " WHERE id IN (" + ",".join(ids) + ");"
        return request

    @staticmethod
    def getCurrentValueOfAutoincrementedFieldRequest(tableName, fieldName) -> str:
        request = "SELECT currval(pg_get_serial_sequence('{}','{}'));".format(tableName, fieldName)
        return request

# FIELDS:

