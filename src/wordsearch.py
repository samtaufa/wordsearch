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
        puzzledirections = "<div class='ws-directions'>Find words hidden: %s</div>" % self.wsmatrix.wsDir
        
        myarticle = ""
        puzzlepage = ""
        if self.format == 'html':
            wsformat.html()
            myarticle = ""
            template_stylesheet="""
        <style>
        <!--
         /* Font Definitions */
            @font-face
                   {font-family:Cambria;
                   panose-1:2 4 5 3 5 4 6 3 2 4;}
            @font-face
                   {font-family:Calibri;
                   panose-1:2 15 5 2 2 2 4 3 2 4;}
            @font-face
                   {font-family:Consolas;
                   panose-1:2 11 6 9 2 2 4 3 2 4;}
         /* Style Definitions */
            p {
                margin-right:0cm;
                margin-left:0cm;
                font-size:12.0pt;
                font-family:"Times New Roman","serif";
            }
            p.ws-puzzle, li.ws-puzzle, div.ws-puzzle {
                margin:0cm;
                margin-bottom:.0001pt;
                text-align:center;
                font-size:20.0pt;
                font-family:"Courier New";
            }
            p.ws-wordlist, li.ws-wordlist, div.ws-wordlist {
                margin-top:24.0pt;
                margin-right:0cm;
                margin-bottom:0cm;
                margin-left:0cm;
                margin-bottom:.0001pt;
                text-align:justify;
                font-size:14.0pt;
                font-family:"Calibri","sans-serif";
            }
            p.ws-solution, li.ws-solution, div.ws-solution {
                margin:0cm;
                margin-bottom:.0001pt;
                text-align:right;
                font-size:8.0pt;
                font-family:"Courier New";
            }
            p.ws-article, li.ws-article, div.ws-article {
                margin:0cm;
                margin-bottom:.0001pt;
                font-size:14.0pt;
                font-family:"Times New Roman","serif";
            }
            div.ws-article {
                margin-top: 12pt;
            }
            p.title, li.title, div.title {
                margin-top:0cm;
                margin-right:0cm;
                margin-bottom:15.0pt;
                margin-left:0cm;
                page-break-after:avoid;
                border:none;
                padding:0cm;
                font-size:26.0pt;
                font-family:"Cambria","serif";
                color:#17365D;
                letter-spacing:.25pt;
            }
            p.subtitle, li.subtitle, div.subtitle {
                margin:0cm;
                margin-bottom:.0001pt;
                page-break-after:avoid;
                font-size:12.0pt;
                font-family:"Cambria","serif";
                color:#4F81BD;
                letter-spacing:.75pt;
                font-style:italic;
            }
            .highlight {
                font-style: italic;
                font-weight: bold;
            }
            p.ws-directions, li.ws-directions, div.ws-directions {
                margin:0cm;
                margin-bottom:.0001pt;
                page-break-after:avoid;
                font-size:12.0pt;
                font-family:"Cambria","serif";
                #color:#4F81BD;
                letter-spacing:.75pt;
                font-style:italic;
            }
            
        -->
        </style>            
            """
            template_body="""
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
            
            template_head = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        <title>Wordsearch Puzzle Generation</title>
        %s
    </head>
                """ % template_stylesheet
            template = """
%s
%s""" % (template_head, template_body)
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