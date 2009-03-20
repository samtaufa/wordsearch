# -*- coding: utf-8 -*-
# Copyright (c) 2008, Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
# Unicode Text: "����������������������������������AaEeIiIiOoUuUu??"

import libpry
import sys
from src.lib.wsstreamio import WSstreamIO
from src.lib.directions import Directions

class u_WSstreamIO(libpry.AutoTree):
    def setUpAll(self):
        import os
        self.filename = "test_wsstreamio.py"
        
    def tearDownAll(self):
        pass
        
    def test_init1(self):
        test = WSstreamIO()
        assert test.words == []
        assert test.lines == []
        
    def test_init2(self):
        test = WSstreamIO('test_wsstreamio.py')
        assert test.words == []
        assert test.lines != []
        
    def test_open(self):
        test = WSstreamIO()
        fh = test.open(self.filename)
        assert file == type(fh)
        assert self.filename == fh.name
        
    def test_load(self):
        test = WSstreamIO(self.filename)
        assert test.lines > 0

    def test_open(self):
        test = WSstreamIO()
        fh = test.open(self.filename)
        assert fh
        
    def test_load(self):
        test = WSstreamIO()
        fh = test.open(self.filename)
        lines = test.load(fh)
        assert lines

    def test_lines(self):
        test = WSstreamIO(self.filename)
        assert test.lines
        
    
        




tests = [
    u_WSstreamIO()
]

