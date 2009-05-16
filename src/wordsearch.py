#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    wordsearch.py
    
    Main application for generating 'wordsearch' or 'word find'
    puzzles from a provided file(s) containing 'words'

    :copyright: (c) 2009, Samiuela Loni Vea Taufa
    :license: MIT, see LICENSE.txt for more details
"""
import os.path, fnmatch
from lib import wsmatrix, wsoptions, wsstreamio

class wordsearch:
    def __init__(self):
        self.article = False
        self.directions = 1
        self.wsstreamio = wsstreamio.WSstreamIO()
        self.matrixPlaced = []
        self.wlplaced = []
        self.wlrejected = []
        
    def load(self, filename):
        fh = self.wsstreamio.open(filename)
        self.wsstreamio.load(fh)
        self.lines = self.wsstreamio.lines
        
    def process(self):
        
        self.lines = self.wstext.language.c_transpose(self.lines)
        self.wstext.setWordlist(self.lines)
        #self.wstext.wordlist.sort()
        #workingList, rejected = wstext.sanitize_words(workingList, longest)
        self.wsmatrix = wsmatrix.WSmatrix((self.rows, self.cols),
                        self.directions, self.wstext.wordlist,
                        self.wstext) 
        self.matrixPlaced, self.wlplaced, self.wlrejected = self.wsmatrix.populate()        
    def output(self):
        wsformat = wsmatrix.WSformats()
        wsformat.matrix = self.matrixPlaced
        wsformat.accepted = self.wlplaced
        wsformat.rejected = self.wlrejected
        wsformat.solution = self.wsmatrix.wordsplaced
        wordcount = len(self.wlplaced)
        spotfilled = self.wsmatrix.cells_available
        matrixsize = self.wsmatrix.maxrow * self.wsmatrix.maxcol
        matrixratio = int(spotfilled / float(matrixsize) * 100)
        puzzlestats = "%s words (%s of %s cells spot filled [%s%%])"%(wordcount, spotfilled, matrixsize, matrixratio)
        puzzledirections = "Find words hidden: %s" % self.wsmatrix.wsDir
        
        myarticle = ""
        puzzlepage = ""
        if self.format == 'html':
            wsformat.html()
            myarticle = ""
            template = """
                    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
                        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
                    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
                    <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                        <title>Wordsearch Puzzle Generation</title>
                    </head>
                    <body>
                    <p class='title'>Title: Word Search Puzzle</p>
                    <p class='subtitle'>Sub-Title</p>
                    <p class='directions'>%s</p>
                    <div class='ws-puzzle'>
                    %s
                    </div>
                    <div class='ws-wordlist'>
                    %s
                    </div>
                """
            puzzlepage = template % (puzzledirections,
                                     wsformat.matrixFormatted,
                                     wsformat.acceptedFormatted)
            if self.article:
                myarticle = wsformat.html_article(self.lines, wsformat.accepted, self.wstext)
                myarticle = "<div class='ws-article'>\n%s\n</div>\n" % myarticle
                puzzlepage += myarticle
            puzzlepage += "<p class='ws-stats'>%s</p>" % puzzlestats
            puzzlepage += """
            </body>
            </html>
            """
        elif self.format == 'xml':
            pass
        else:
            wsformat.unicode()
            puzzlepage += puzzledirections + "\n"
            puzzlepage += wsformat.matrixFormatted + "\n"
            puzzlepage += wsformat.acceptedFormatted + "\n"
            puzzlepage += puzzlestats
        
        if self.outputpath:
            self.wsstreamio.write(self.outputpath, puzzlepage)
        else:
            print str(puzzlepage)
    def cmdline(self):
        options = wsoptions.WSoptions()
        pathname, self.rows, self.cols, self.directions = options.get_cmdline()
        self.format = options.format
        self.outpath = options.outputpath
        self.article = options.article
        self.minimumwordlength = options.minimumwordlength
        self.outputpath = options.outputpath
        
        self.wstext = wsmatrix.WStext(lingua = options.lingua,
                                      minlength = options.minimumwordlength,
                                      maxlength = max(options.rows, options.cols)
                                      )
        return pathname
    
    def main(self):
        pathname = self.cmdline()
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