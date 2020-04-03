import pandas as pd
from DataExportInterface.DatabaseInterface import *


class InformationManager:

    def __init__(self, conf):
        self.data_df = pd.DataFrame()
        self.conf = conf
        self.db = DatabaseInterface(conf)

    def createDataframe(self, data):
        # data is url: data dict as defined in crawler interface
        self.data_df = pd.DataFrame(data).transpose()
        self.data_df.index.name = "URL"
        self.data_df.reset_index(level=0, inplace=True)


    def exportDataframeAsExcel(self, documentname = 'crawleroutput.xls'):  # export to DB will come later
        self.data_df.to_excel(documentname, index_label=True)

    def exportDataframeToDB(self, data, docid=1, attid=1):
        self.createDataframe(data)
        table = self.db.createNewDataTable(self.data_df, docid, attid)
        return table

    def getDocumentListById(self, docid):
        doclist = self.db.runStoredProcedure("getDocumentListById", (docid))
        return doclist

    def getAttributeListById(self, attid):
        attlist = self.db.runStoredProcedure("getAttributeListById", (attid))
        return attlist

    def addAttributeData(self, attdata, filename, attname):
        attid = self.db.runStoredProcedure("addAttributeIndex", (filename, attname))[0][0]
        print(attid)
        for record in attdata:
            name, atttype, patt = record
            self.db.runStoredProcedure("addAttributeData", (attid, name, atttype, patt))
        return attid

    def addDocumentData(self, docdata, filename, docname):
        docid = self.db.runStoredProcedure("addUrlIndex", (filename, docname))[0][0]
        print(docid)
        for record in docdata:
            hint, protocol, url = record
            self.db.runStoredProcedure("addURLData", (docid, hint, protocol, url))
        return docid

    def getCrawlData(self, docid, attid):
        tablename = "table_" + str(docid) + '_' + str(attid)
        data = self.db.runStoredProcedure('getCrawlTableData', (tablename))
        return data
