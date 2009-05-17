#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    :copyright: (c) 2009, Samiuela Loni Vea Taufa
    :license: ISCL, see LICENSE.txt for more details
"""
import optparse, sys

class WSoptions:
    def __init__(self):      
        self.rows = 20
        self.cols = 20
        self.usage = ""
        self.parser = optparse.OptionParser()
        self.version = "0.00.01"
        self.directions = 1
        self.args = None
        self.format = 'unicode'
        self.outputpath = ''
        self.article = False
        self.minimumwordlength = 0
        self.set_options()
        self.lingua = "en"
        
    def read_options_default(self):
        pass # Get it from a file?
    
    def set_options(self):
        self.usage = """
        usage: %prog [options] filename

        %prog generages wordsearch puzzles from text in filename
        
        filename is the file containing words for generating 
        wordsearch puzzle(s). The file contains lines of words 
        (whether one word per line or a paragraph of text.)
        
        --article used with output format 'html' (-f html)
        retains the structure of the text in the file with output
        highlighting words hidden in the puzzle.
        """
        self.version = "%prog " + self.version
        self.parser = optparse.OptionParser(usage=self.usage, version=self.version)
        self.parser.add_option('','--article',action='store_true', dest='article',
                               help='Retain input file format for highlighted article output.',
                               default=False)
        self.parser.add_option('-d', '--directions', action='store', type='int', dest='directions',
                                help='''Set the Directions words can traverse puzzle; one or 
            a combination of the numbers  [1|2|4|8|16|32|64|128]. 
            ( Left to Right = 1, Right to Left = 2, 
            Up = 4, Down = 8, 
            Diag Up to Left = 16, Diag Up to Right = 32, 
            Diag Down to Left = 64, Diag Down to Right = 128)
            
            Combine directions such as:
            9 = Right[1] + Down[8] (default);
            11 = Right[1] + Left[2] + Down[8];
            143 = Right[1] + Left[2] + Down[8] + Up[4] + DiagDwnRight[128];
            255 = All Directions
            '''
         )
        self.parser.add_option('-f','--format', action='store', type='string', nargs=1,
                               dest='format', help='Output format: [html|unicode|xml]')
        self.parser.add_option('-g', '--gridsize', action='store', type='int', nargs=2,
                               dest='grid_size', help='Two paramaters, the x and y size of ' + 
                                    'the puzzle grid to be created. The default is 20 by 20')
        self.parser.add_option('-l', '--level', action='store', type='int', dest='level',
                              help='''Set the Level of Difficulty [1-5]. A simplified amalgamation of directions.
            Level 1 (Basic [9]- default) Left to Right and Down,
            Level 2 (Sweet [137]) Right, Down, DiagDwnRight
            Level 3 (Challenger [143]) Right, Left, Down, Up, DiagDwnRight
            Level 4 (Try Me [175]) Right, Left, Down, Up, DiagDwnRight, DiagUpRight
            Level 5 (All Out [255]) All Directions
            ''')
        self.parser.add_option('-m','--minimumwordlength',action='store', type='int', nargs=1,
                               dest='minimumwordlength', help='Minimum length of word for puzzle',
                               default=2)
        self.parser.add_option('-o','--outputpath', action='store', type='string', nargs=1,
                               dest='outputpath', help='Where to create the puzzle, must be '+
                               'a directory if the pathname is a directory')
        self.parser.add_option('-t','--text', action='store',type='string', nargs=1,
                               dest='lingua',help="""Specify the input text character set rules:
                               Currently "en" (default) and "to" are supported.
                               """,
                               default='en')
        
    
    def read_cmdline(self):
        options, self.args = self.parser.parse_args()

        if options.grid_size is not None:
            self.rows = options.grid_size[0]
            self.cols = options.grid_size[1]
            
        if options.format is not None:
            self.format = options.format
            
        if options.level is not None:
            if options.level > 5:
                level = 5
            else:
                level = options.level
            if level == 5:
                self.directions = 255
            elif level == 1:
                self.directions = 9
            elif level == 2:
                self.directions = 137
            elif level == 3:
                self.directions = 143
            elif level == 4:
                self.directions = 175
                
        if options.directions is not None:
            self.directions = options.directions
            
        self.minimumwordlength = options.minimumwordlength
        self.article = options.article
        self.outputpath = options.outputpath
        self.lingua = options.lingua
        
    def get_cmdline(self):
        self.read_cmdline()
        if len(self.args) < 1: # Did I get a filename?
            self.parser.print_help()
            sys.exit(2)

        return self.args[0], self.rows, self.cols, self.directions

if __name__ == '__main__':
    pass