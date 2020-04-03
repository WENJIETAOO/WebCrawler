import unittest
import os
from DocumentGenerator import *


class TestURLExtractor(unittest.TestCase):
    def test_urls(self):
        localpath = os.getcwd()+"\localurlfile.html\n"
        testurls = [
            localpath,
            "http://cs.unb.ca/~wsong/lab1.html\n"
            "http://www.google.com\n"
        ]
        expectedresults = [
            ('local', 'C:\\Users\\ividito\\Desktop\\SeniorDesign\\Testing\\localurlfile.html'),
            ('http', 'http://cs.unb.ca/~wsong/lab1.html'),
            ('http', 'http://www.google.com')
        ]
        with open('testurls.txt', 'w') as urlfile:
           urlfile.writelines(testurls)
        self.urlreader = URLFileParser('testurls.txt')
        self.assertTrue(self.urlreader.read_all_urls() == expectedresults)

    def tearDown(self):
        self.urlreader.destroy()


if __name__ == "__main__":
    unittest.main()
