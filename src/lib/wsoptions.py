#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2008, Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
import optparse, sys, os, os.path

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
        self.minimumwordlength = 0
        self.set_options()
    def read_options_default(self):
        pass # Get it from a file?
    
    def set_options(self):
        self.usage = """
        usage: %prog [options] pathname

        where pathname is the file or directory
        containing words for generating wordsearch
        puzzle(s)
        """
        self.version = "%prog " + self.version
        self.parser = optparse.OptionParser(usage=self.usage, version=self.version)
        self.parser.add_option('-g', '--gridsize', action='store', type='int', nargs=2,
                               dest='grid_size', help='Two paramaters, the x and y size of ' + 
                                    'the puzzle grid to be created. The default is 20 by 20')
        self.parser.add_option('-o','--outputpath', action='store', type='string', nargs=1,
                               dest='outputpath', help='Where to create the puzzle, must be '+
                               'a directory if the pathname is a directory')
        self.parser.add_option('-f','--format', action='store', type='string', nargs=1,
                               dest='format', help='Output format: [html|unicode|xml]')
        self.parser.add_option('-l','--minimumwordlength',action='store', type='int', nargs=1,
                               dest='minimumwordlength', help='Minimum length of word for puzzle',
                               default=2)
        self.parser.add_option('-d', '--directions',action='store', type='int', dest='directions',
                                help='''Directions words can traverse puzzle.
[1|2|4|8|16|32|64|128].
( Left to Right = 1, Right to Left = 2, Up = 4, Down = 8, Diag Up to Left = 16,
Diag Up to Right = 32, Diag Down to Left = 64, Diag Down to Right = 128)

Combine directions such as:
9 = Right[1] + Down[8] (default);
11 = Right[1] + Left[2] + Down[8];
143 = Right[1] + Left[2] + Down[8] + Up[4] + DiagDwnRight[128];
256 = All Directions
'''
         )
    
    def read_cmdline(self):
        options, self.args = self.parser.parse_args()

        if options.grid_size is not None:
            self.rows = options.grid_size[0]
            self.cols = options.grid_size[1]
        
        if options.directions is not None:
            self.directions = options.directions
            
        if options.format is not None:
            self.format = options.format
            
        self.minimumwordlength = options.minimumwordlength
            
    def get_cmdline(self):
        self.read_cmdline()
        if len(self.args) < 1: # Did I get a filename?
            self.parser.print_help()
            sys.exit(2)

        return self.args[0], self.rows, self.cols, self.directions

if __name__ == '__main__':
    pass