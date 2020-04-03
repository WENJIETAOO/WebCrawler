import re
import xml.etree.ElementTree as et
from bs4 import BeautifulSoup


class LocalCrawler:

    def __init__(self, attributes):  # attributes is a list of tuples (attributename, ruletype, regex/xpath)
        self.attributes = attributes
        self.fulldata = {}
        pass

    def crawl(self, url):  # URL must be an absolute path
        urldata = {}
        print(url)
        try:
            with open(url, mode='r', encoding="utf-8") as fin:
                filetext = fin.read()
                for a in self.attributes:
                    name, rtype, patt = a
                    print(a)
                    if rtype == 'regex':
                        try:
                            patt = patt.rstrip()
                            pattcomp = re.compile(patt)
                            regexdata = self.soupify(filetext)
                            matches = pattcomp.findall(regexdata)
                            urldata[name]=matches[0][0]
                        except Exception as e:
                            urldata[name] = ''
                            pass  # TODO handle exception from re.find here if needed
                    elif rtype == 'xpath':
                        try:
                            tree = et.parse(url)  # This can also be read from string using et.fromstring(urldata)
                            urldata[name] = tree.find(patt).text
                        except et.ParseError:
                            pass  # TODO handle parse error
                    else:
                        # invalid attribute data
                        raise Exception(message="Attribute Data Malformed : " + name+ ' ' + rtype + ' ' + patt)
        except FileNotFoundError as e:
            pass  # TODO decide how to handle FNF exception
        print("urldata: ")
        print(urldata)
        self.fulldata[url] = urldata

    def getData(self):
        return self.fulldata  # returns dict of {url:dict of attribute:data} -> {url: {att1: data1, att2: data2}}

    def soupify(self, filetext):
        dataout = ''
        VALID_TAGS = ['div', 'p']
        soup = BeautifulSoup(filetext, features="html.parser")
        for tag in soup.find_all('p'):
            if tag.name not in VALID_TAGS:
                tag.replaceWith(tag.renderContents())
        for t in soup.find_all('p'):
            if t.string:
                dataout = dataout+'\n'+t.string
            else:
                dataout = dataout + '\n' + t.text
        return dataout