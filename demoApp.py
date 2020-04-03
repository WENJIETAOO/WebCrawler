# For demonstrating functionality on a limited use case
from AttributeGenerator import *
from DocumentGenerator import *
from DataExportInterface import *
from CrawlerInterface import *
from config import *

conf = config
attfilename = 'Attributes/wikipediaLocations.txt'
attributeparser = AttributeFileParser(attfilename)
urlfilename = 'Webpages/wikipediaLocations.txt'
urlparser = URLFileParser(urlfilename)
crawler = CrawlerController()
exporter = InformationManager(conf.local_db)

atts = attributeparser.read_all_attributes()
attid = exporter.addAttributeData(atts, attfilename, "wikipediaatts")
#print(attid)

urls = urlparser.read_all_urls()
docid = exporter.addDocumentData(urls, urlfilename, "wikipediadocs")
#print(docid)

crawlresults = crawler.crawlDocuments(urls, atts)

print(crawlresults)
#exporter.createDataframe(crawlresults)
exporter.exportDataframeToDB(crawlresults, docid, attid)
