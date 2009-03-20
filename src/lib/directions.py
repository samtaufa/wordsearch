#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2008, Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
import random
class Directions:
    def __init__(self):
        self.Right = 1
        self.Left  = 2
        self.Up    = 4
        self.Down  = 8
        self.DiagUpLeft   = 16
        self.DiagUpRight  = 32
        self.DiagDwnLeft  = 64
        self.DiagDwnRight = 128
        self.Directions = [ self.Right, self.Left, self.Up,
                           self.Down, self.DiagUpLeft, self.DiagUpRight,
                           self.DiagDwnLeft, self.DiagDwnRight]
        self.Chosen = []
    
    def set_directions(self, combined):
        for i in range(0, len(self.Directions)):
            if combined & self.Directions[i]:
                self.Chosen.append(self.Directions[i])

    def pop(self):
        item = random.randint(0, len(self.DirChosen)-1)
        return self.Chosen.pop(item)
        
    def push(self, item):
        self.Chosen.append(item)
        
if __name__ == '__main__':
    pass