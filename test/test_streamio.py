# -*- coding: utf-8 -*-
# Copyright (c) 2008, Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
# Unicode Text: "ÁÂÃÄÉÊËÍÎÏÓÔÕÖÚÛÜáâãäéêëíîïóôõöúûüAaEeIiIiOoUuUu??"

import libpry
import sys
from src.streamio import StreamIO
from src.directions import Directions

class u_StreamIO(libpry.AutoTree):
    def setUpAll(self):
        import os
        self.filename = "test_streamio.py"
        
    def tearDownAll(self):
        pass
        
    def test_init1(self):
        test = StreamIO()
        assert test.words == []
        assert test.lines == []
        
    def test_init2(self):
        test = StreamIO('test_streamio.py')
        assert test.words == []
        assert test.lines != []
        
    def test_open(self):
        test = StreamIO()
        fh = test.open(self.filename)
        assert file == type(fh)
        assert self.filename == fh.name
        
    def test_load(self):
        test = StreamIO(self.filename)
        assert test.lines > 0

    def test_open(self):
        test = StreamIO()
        fh = test.open(self.filename)
        assert fh
        
    def test_load(self):
        test = StreamIO()
        fh = test.open(self.filename)
        lines = test.load(fh)
        assert lines

    def test_lines(self):
        test = StreamIO(self.filename)
        assert test.lines
        
    
        




tests = [
    u_StreamIO()
]

