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
        self.format = 'html'
        self.outputpath = ''
        self.minimumwordlength = 0
        
    def load(self, filename):
        fh = self.wsstreamio.open(filename)
        self.wsstreamio.load(fh)
        self.lines = self.wsstreamio.lines
        
    def process(self):
        
        self.wstext.setLanguage('to')
        self.wstext.minimumwordlength = self.minimumwordlength
        self.wstext.setWordlist(self.lines)
        
        self.wstext.wordlist.sort
        
        self.wsmatrix = wsmatrix.WSmatrix((self.rows, self.cols),self.directions,self.wstext.wordlist)
        
        self.pMatrix, self.wlaccepted, self.wlrejected = self.wsmatrix.populate()
        
    def output(self):
        
        self.wsformat.matrix = self.pMatrix
        self.wsformat.accepted = self.wlaccepted
        self.wsformat.rejected = self.wlrejected
        self.wsformat.solution = self.wsmatrix.wordsplaced
        
        if self.format == 'html':
            myaccepted, mymatrix, mysolution = self.wsformat.html()
            print """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Wordsearch Puzzle Generation</title>
</head>
<body>
<table class=''>
            <tr><th>Word Search Puzzle</th><th>Word List</th></tr>
            <tr><td valign='top'>%s</td><td valign='top'>%s</td></tr>
            </table>
            <hr />
            <h2>Solution</h2>
            %s
            </body>
            </html>
            """ % (mymatrix, myaccepted, mysolution)
        elif self.format == 'xml':
            myaccepted, mymatrix, mysolution = self.wsformat.xml()
        else:
            myaccepted, mymatrix, mysolution = self.wsformat.unicode()
            myline = ""
            for line in myaccepted:
                myline += line.strip() +", "
            myaccepted = myline[0:len(myline)-2]
        
            print mymatrix
            print myaccepted
            print "(%s of %s)" %(self.wsmatrix.cells_available, self.wsmatrix.maxrow * self.wsmatrix.maxcol)
            #print "-------------"
            #print mysolution
        
    def main(self):
        options = wsoptions.WSoptions()
        pathname, self.rows, self.cols, self.directions = options.get_cmdline()
        self.format = options.format
        self.outpath = options.outputpath
        self.minimumwordlength = options.minimumwordlength
        
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