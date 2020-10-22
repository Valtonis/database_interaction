from typing import List, Tuple

class ForeignKeyRecord:
    def __init__(self, tableFieldNames: List[str], referenceTableName: str, referenceTableFieldNames: List[str]):
        self.tableFieldNames_ = tableFieldNames
        self.referenceTableName_ = referenceTableName
        self.referenceTableFieldNames_ = referenceTableFieldNames

# FIELDS:

    tableFieldNames_: List[str] = None
    referenceTableName_: str = None
    referenceTableFieldNames_: List[str] = None

class IndexRecord:
    def __init__(self, indexName: str, indexingMethod: str, indexingFieldNames: List[str]):
        self.indexName_ = indexName
        self.indexingMethod_ = indexingMethod
        self.indexingFieldNames_ = indexingFieldNames

# FIELDS:

    indexName_: str = None
    indexingMethod_: str = None
    indexingFieldNames_: List[str] = None


class TableStructure:
    def __init__(self,
                 tableName: str,
                 tableFieldNamesAndTypes: List[Tuple[str, str]],
                 primaryKeyFields: List[str],
                 foreignKeyRecords: List[ForeignKeyRecord] = [],
                 indexRecords: List[IndexRecord] = []):

        self.tableName_ = tableName
        self.tableFieldNamesAndTypes_ = tableFieldNamesAndTypes
        self.primaryKeyFields_ = primaryKeyFields
        self.foreignKeyRecords_ = foreignKeyRecords

        self.indexRecords_ = indexRecords

# FIELDS:

    tableName_: str = None
    tableFieldNamesAndTypes_: List[Tuple[str, str]] = None
    primaryKeyFields_: List[str] = None
    foreignKeyRecords_: List[ForeignKeyRecord] = None

    indexRecords_: List[IndexRecord] = None
