#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2008, Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
#
# 
import random, string, copy, time, os, os.path, fnmatch
from lib import wsmatrix, wsoptions, wsstreamio

class wordsearch:
    def __init__(self):
        self.lines = []
        self.rows = 0
        self.cols = 0
        self.directions = 1
        self.wsstreamio = wsstreamio.WSstreamIO()
        self.wsmatrix = wsmatrix.WSmatrix()
        self.wstext = wsmatrix.WStext()
        self.pMatrix = []
        self.wlaccepted = []
        self.wlrejected = []
        self.wsformat = wsmatrix.WSformats()
        
    def load(self, filename):
        fh = self.wsstreamio.open(filename)
        self.wsstreamio.load(fh)
        self.lines = self.wsstreamio.lines
        
    def process(self):
        
        self.wstext.setLanguage('to')
        self.wstext.setWordlist(self.lines)
        
        self.wstext.wordlist.sort
        
        self.wsmatrix = wsmatrix.WSmatrix((self.rows, self.cols),self.directions,self.wstext.wordlist)
        
        self.pMatrix, self.wlaccepted, self.wlrejected = self.wsmatrix.populate()
        
    def output(self):
        
        self.wsformat.matrix = self.pMatrix
        self.wsformat.accepted = self.wlaccepted
        self.wsformat.rejected = self.wlrejected
        self.wsformat.solution = self.wsmatrix.wordsplaced
        
        myaccpeted, mymatrix, mysolution = self.wsformat.html()
        
        print mymatrix
        print "-------------"
        print mysolution
        
        
    def main(self):
        options = wsoptions.WSoptions()
        pathname, self.rows, self.cols, self.directions = options.get_cmdline()
        
        if os.path.isfile(pathname):
            self.load(pathname)
            self.process()
            self.output()
        elif os.path.isdir(pathname):
            for root, dirs, files in os.walk(pathname):
                filelist = fnmatch.filter(files, '*.txt')
                for file in filelist:
                    self.load(os.path.join(root, file))
                    self.process()
                    self.output()        

def main():
    app = wordsearch()
    app.main()
    
if __name__ == "__main__":
    main()