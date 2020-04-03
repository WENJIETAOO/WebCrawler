from AttributeGenerator import *
import pandas as pd


class AttributeFileParser:

    def __init__(self, fin):
        if fin:
            self.filename = fin
        else:
            raise AttributeError(message="Must provide filename to AttributeFileParser")
        self.regexParser = RegexExtractor()  # initialize regex processor
        self.attributeParser = AttributeExtractor()  # initialize attribute processor
        self.fileEntity = open(self.filename, 'r')  # create readable file object

    def read_single_attribute(self, attributeline):
        attribute = attributeline.split(sep="|")[0]
        ruletype = attributeline.split(sep="|")[1]
        # only first 2 pipes are treated as delimiter, others are treated as part of regex/XPATH
        regex = '|'.join(attributeline.split(sep="|")[2:])
        parsedattribute = self.attributeParser.parse(attribute)
        parsedregex = self.regexParser.parse(regex, ruletype=ruletype)
        return parsedattribute, ruletype, parsedregex  # returns tuple (attributename, regex)

    def read_all_attributes(self):
        attributelist = []
        if self.filename.split('.')[1] not in ('txt','psv'):  # if not txt or psv, read excel
            attributelist = pd.read_excel(self.filename).to_records(index=False).tolist()
        for line in self.fileEntity.readlines():
            attributelist.append(self.read_single_attribute(line))
        return attributelist  # returns list of tuples [(attr1, regex1), (attr2, regex2)]

    def destroy(self):
        # close file reader
        self.fileEntity.close()
        # TODO deal with created extractor objects as needed
