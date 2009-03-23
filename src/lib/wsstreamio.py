#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2008, Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
# Unicode Text: "ÁÂÃÄÉÊËÍÎÏÓÔÕÖÚÛÜáâãäéêëíîïóôõöúûüĀāĒēĨĩĪīŌōŨũŪūẼẽ"

import os.path

class WSstreamIO:
    def __init__(self, filename = ""):
        self.words = []
        self.lines = []
        if filename != "":
            fh = self.open(filename)
            if fh:
                self.load(fh)
                fh.close()

    def open(self, filename):
        if not os.path.isfile(filename):
            return False
        try:
            fh = open( filename, 'rUb')
        except IOError:
            fh = None # File may not be readable
            
        return fh
        
    def load(self, fh = None):
        for line in fh:
            self.lines.append( line.strip( "\r\n" ) )
            
        return self.lines
        
if __name__ == '__main__':
    pass