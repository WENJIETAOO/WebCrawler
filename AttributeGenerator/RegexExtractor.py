import re
import lxml.etree

#  The class name is actually a misnomer since we decided to allow XPATH ruletypes
#  Also this is really more like a validator, since the string/ruletype pair is what gets thrown to the crawler anyway
class RegexExtractor:

    def __init__(self):
        pass

    def parse(self, regex, ruletype=''):
        if ruletype.lower()=="regex":
            return self.parseRegex(regex)
        elif ruletype.lower()=="xpath":
            return self.parseXpath(regex)
        else:
            return self.parseRegex(regex)  # for now, we assume default behavior to be regex

    def parseRegex(self, regex):
        try:
            re.compile(regex)
            return regex
        except re.error:
            raise Exception(message="Rule: "+regex+" is not a valid regex")

    def parseXpath(self, xpath):
        try:
            lxml.etree.XPath(xpath)
            return xpath.rstrip()
        except lxml.etree.XPathSyntaxError:
            raise Exception(message="Rule: "+xpath+" is not a valid XPath (did you mean to use regex?)")
