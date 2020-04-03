from CrawlerInterface import *

class CrawlerController:

    def selectAttributes(self, attributeList):
        self.local = LocalCrawler(attributeList)
        self.http = HttpCrawler(attributeList)
        pass

    def crawlDocuments(self, documentList, attributeList):
        self.selectAttributes(attributeList)
        fullData = {}
        for doc in documentList:
            protocol = doc[1]
            url = doc[0].splitlines()[0]
            if protocol == "local":
                self.local.crawl(url)
            else:
                self.http.crawl(url)
        try:
            d = self.local.getData()
            fullData.update(d)
        except TypeError:
            print("No local files to crawl, continuing...")
        try:
            for d in self.http.getData():
                fullData.update(d)
        except TypeError:
            print("No remote files to crawl, continuing...")
        return fullData
