from DocumentGenerator import *
import pandas as pd


class URLFileParser:

    def __init__(self, fin):
        if fin:
            self.filename = fin
        else:
            raise AttributeError(message="Must provide filename to URLFileParser")
        self.urlParser = URLExtractor()
        if self.filename.split('.')[1] in ['xls','xlsx']:
            self.isexcel = True
            self.fileEntity = pd.read_excel(fin, names = ['hint','url'])
        else:
            self.isexcel = False
            self.fileEntity = open(self.filename, 'r')  # create readable file object

    def read_single_url(self, urlline):
        protocol = urlline.split(sep=":")[0]
        url = urlline
        parsedProtocol, parsedUrl = self.urlParser.parse(url)
        return parsedProtocol, parsedUrl

    def read_all_urls(self):
        urllist = []
        if self.isexcel:
            for i, row in self.fileEntity.iterrows():
                hint = row['hint']
                url = row['url']
                protocol, parsedUrl = self.read_single_url(url)
                urllist.append((hint, protocol, parsedUrl))
        else:
            for line in self.fileEntity.readlines():
                hint = line.split('|')[0]
                protocol, parsedUrl = self.read_single_url(''.join(line.split('|')[1:]))
                urllist.append((hint, protocol, parsedUrl))
        return urllist

    def destroy(self):
        # close file reader
        self.fileEntity.close()
        # TODO deal with created extractor objects as needed