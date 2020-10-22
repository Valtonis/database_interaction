from typing import List

from .TableStructure import TableStructure

class DatabaseRequestBuilder:
    def __init__(self, tableStructures: List[TableStructure]):
        self.tableStructures_ = tableStructures

    def getCreateTablesRequest(self) -> str:
        pass

    def getRemoveTablesRequest(self) -> str:
        pass

    def getCleanTablesRequest(self) -> str:
        pass

    def getRemoveTableRecordsRequest(self, tableName: str, ids: List[int]) -> str:
        pass

    @staticmethod
    def compileInsertRequestTemplate(table: str, fields: List[str], numberOfRecords: int = 1) -> str:
        pass

    @staticmethod
    def compileUpdateRequestTemplate(table: str, fields: List[str], ids: List[int] = None) -> str:
        pass

    @staticmethod
    def getCurrentValueOfAutoincrementedFieldRequest(tableName, fieldName) -> str:
        pass

# PRIVATE FUNCTIONS:

# FIELDS:

    tableStructures_: List[TableStructure] = None
