#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    Stream IO class for opening, loading, and writing raw documents.

    :copyright: (c) 2009, Samiuela Loni Vea Taufa
    :license: ISCL, see LICENSE.txt for more details

    Unicode Text: "ÁÂÃÄÉÊËÍÎÏÓÔÕÖÚÛÜáâãäéêëíîïóôõöúûüĀāĒēĨĩĪīŌōŨũŪūẼẽ"

"""

import os.path, sys, codecs
from BeautifulSoup import BeautifulSoup

class WSstreamIO:
    def __init__(self, filename = ""):
        self.words = []
        self.lines = []
        self.originalEncoding = 'utf-8'
        if filename != "":
            fh = self.open(filename)
            if fh:
                self.load(fh)
                fh.close()

    def open(self, filename):
        if not os.path.isfile(filename):
            return False
        
        self.originalEncoding = BeautifulSoup(open(filename).read()).originalEncoding
        fh = open( filename, 'rb')
        text = fh.read()
        fh.close()
        if text.find('\x91') > -1 and self.originalEncoding == "ISO-8859-2": # msword smartquote in Latin-1
            self.originalEncoding = "cp1252" # was this an MS Word converted doc ?        
        try:
            fh = codecs.open( filename, encoding=self.originalEncoding)
        except IOError:
            fh = open( filename, 'rb')
        return fh
        
    def load(self, fh = None):
        for line in fh:
            self.lines.append( (line.strip("\r\n")).decode(self.originalEncoding) )
        return self.lines
    def write(self, filename, data):
        fh = codecs.open( filename, encoding='utf-8', mode = 'w+')
        fh.write(data)
if __name__ == '__main__':
    pass