#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2008, Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
import optparse, sys

class WSoptions:
    def __init__(self):      
        self.rows = 20
        self.cols = 20
        self.usage = ""
        self.parser = optparse.OptionParser()
        self.version = "0.00.01"
        self.options = None
        self.args = None
    def read_options_default(self):
        pass # Get it from a file?
    
    def set_cmdline_defaults(self):
        self.usage = """
        usage: %prog [options] filename

        where filename is the text file containing words for the puzzle
        """
        self.version = "%prog " + self.version
        self.parser = optparse.OptionParser(usage=self.usage, version=self.version)
        self.parser.add_option('-g', '--gridsize', action='store', type='int', nargs=2, dest='grid_size',
                                help='Two paramaters, the x and y size of the puzzle grid to be created. The default is 20 by 20')
        self.parser.add_option('-d', '--directions',action='store', type='int', dest='directions',
                                help='''specifies the directions in which the puzzle can be drawn
        Directions are as listed: 
        
        ( Left to Right = 1, Right to Left = 2, 
        Up = 4, Down = 8, Diag Up to Left = 16, Diag Up to Right = 32,
        Diag Down to Left = 64, Diag Down to Right = 128)

        Combining the directions gives us:
        
           Very BASIC:\t  9 = Right + Down (default)\n
           BASIC:\t\t 11 = Right + Left + Down\n
           InterMediate:\t143 = Right + Left + Down + Up + DiagDwnRight\n
           WINNER:\t\t256 = All Directions
         '''
         )
    
    def read_cmdline_options(self):
        (self.options, self.args) = self.parser.parse_args()

    def get_gridsize(self):
        if len(self.options.grid_size) == 2:
            self.rows = self.options.grid_size[0]
            self.cols = self.options.grid_size[1]
        else:
            self.parser.print_help()
            sys.exit(2)
        
    def get_cmdline(self):
        
        if self.args is None or self.options is None:
            return
        
        if len(self.args) < 1: # Did I get a filename?
            self.parser.print_help()
            sys.exit(2)

        self.get_gridsize()    
        
        return self.args[0], self.rows, self.cols, self.options.directions

if __name__ == '__main__':
    pass