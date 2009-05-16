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
    
    def __str__(self):
        vd = [] # valid directions
        if self.Right in self.Directions:
            vd.append("Left to Right")
        if self.Left in self.Directions:
            vd.append("Right to Left")
        if self.Up in self.Directions:
            vd.append("Up")
        if self.Down in self.Directions:
            vd.append("Left to Down")
        if self.DiagUpLeft in self.Directions:
            vd.append("Diagonal Up Right to Left")
        if self.DiagUpRight in self.Directions:
            vd.append("Diagonal Up Left to Right")
        if self.DiagDwnLeft in self.Directions:
            vd.append("Diagonal Down Right to Left")
        if self.DiagDwnRight in self.Directions:
            vd.append("Diagonal Down Left to Right")
        
        vdirections = ""
        for dir in vd:
            vdirections += "%s, " % dir
        
        return vdirections[:-2]
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