# The crawler interface can work with a user-defined crawler (which we will implement)
# It can also be used to pass various arguments (URLS, Regex, etc) to a 3rd party crawler
# It also returns the output of the crawler, depending on format, to the system to be loaded to a DB

from CrawlerInterface.HttpCrawler import *
from CrawlerInterface.LocalCrawler import *
from CrawlerInterface.CrawlerController import *
#import CrawlerInterface.detectorists as detectorists
