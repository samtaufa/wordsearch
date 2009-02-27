#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2008, Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
#
# 
import random, string, copy
from lang import to as language
class WSmatrix():
    """
       
        WS Matrix and management utilities
    """  
    def __init__(self, size=(20,20), directions = 1, wordlist = []):
        """
            size: integer values for (maximum rows, maximum cols)
            directions: integer concatenation of directions
            wordlist: list of words
        """
        self.matrix   = []        
        self.INPUT_MASK = '*'
        self.INPUT_BLOCK = '#'
        self.cells_available = 0
        self.cells_minleftover = 0
        self.wordsplaced = []
        self.wordsrejected = []
        
        self.maxrow, self.maxcol = size
        self.wsDir = WSdirections()
        self.wsDir.set_directions(directions)
        self.directions = self.wsDir.Chosen
        self.wordlist = wordlist
        
        self.matrix, self.cells_available, self.cells_minleftover = \
            self.cells_init(self.maxrow, self.maxcol)
        self.startCells = []
        
    def set_directions(self, directions = 1):
        """
            :directions - integer concatenation of wsDirections.Directions
        """
        self.wsDir.set_directions(directions)
        self.directions = self.wsDir.Chosen
        
    def cells_init(self, rows=0, cols=0):
        """
            Initialise matrix with INPUT_MASK
            :rows - # rows of matrix
            :cols - # cols of matrix
        """
        if rows ==  0: rows = self.maxrow
        if cols == 0: cols = self.maxcol
            
        matrix = []

        available = rows * cols
        minleftover = int(0.01 * available)
        
        matrix = [[self.INPUT_MASK for col in range(cols)] for row in range(rows)]
        
        self.matrix = matrix
        self.cells_available = available
        self.cells_minleftover = minleftover
        
        return matrix, available, minleftover
        
    def display(self, matrix = []):
        if matrix == []:
            matrix = self.matrix
            
        for xcell in range (0, self.maxrow):
            for ycell in range (0, self.maxcol):
                print matrix[xcell][ycell],
            print
            
    def startGrid(self, direction, length):
        """
            For a WSword of length and set with the direction
            return a list of vertices that can accommodate
            the length of the WSword
            
            return:     list of vertices (Matrix Cells)
            direction:  integer direction
            length:     maximum length of words
            returns:    list of vertices
        """
        dir = self.wsDir
        x_min, y_min = 0, 0
        x_max, y_max = self.maxrow, self.maxcol
        
        #length -= 1
        if length > x_max and length > y_max:
            return [] # word is too long
        
        if length > x_max  and not (direction in [dir.Up,
                                                  dir.Down]):
            return [] # word is too long
        
        if length > y_max and not (direction in [dir.Right,
                                                 dir.Left]):
            return [] # word is too long
        
        if direction in [dir.Right, dir.DiagUpRight, dir.DiagDwnRight]:
            x_min = 0
            x_max = self.maxrow - length
            
        if direction in [dir.Up, dir.Down]:
            x_min = 0
            x_max = self.maxrow
        
        if direction in [dir.Left, dir.DiagUpLeft, dir.DiagDwnLeft]:
            x_min = length
            x_max = self.maxrow
            
        if direction in [dir.Right, dir.Left]:
            y_min = 0
            y_max = self.maxcol
            
        if direction in [dir.Down, dir.DiagDwnRight, dir.DiagDwnLeft]:
            y_min = 0
            y_max = self.maxcol - length
            
        if direction in [dir.Up, dir.DiagUpRight, dir.DiagUpLeft]:
            y_min = length
            y_max = self.maxcol
            
        if x_min < 0 or y_min < 0 or x_max < 0 or y_max < 0:
            return [] # shouldn't get here, but worth checking
            
        tempGrid =[]
        for xc in range ( x_min, x_max ):
            for yc in range (y_min, y_max):
                tempGrid.append ([xc, yc])
        
        self.startCells = tempGrid
    def popStartCells(self):
        """
            Return a random start cell
            
        """
        item = random.randint(0, len(self.startCells) -1)
        return self.startCells.pop(item)
    def insertWord(self, wordStr, start, direction ):
        pass
    
    def insertWordPart(self, wordstr, start, direction):
        pass
    
    def populate(self):
        """
            Main Loop to insert document into Matrix Grid
        """
        success = False
        workinglist = self.wordlist
        directions  = copy.deepcopy(self.direction)
        
        while 1:
            if success or len(workinglist) == 0:
                break
            dirGo = directions.pop()
            item = random.randint(0, len(workinglist)-1)
            word = workinglist.pop(item)
            subGrid = self.startGrid(dirGo, len(word))
            
            while 1:
                if success or len(subGrid) == 0:
                    break
                
                startPoint = subGrid.pop( random.randint(0, len(subGrid)-1) )
                success = insertWord(word, startPoint, dirGo, )
            
            if self.cells_available <= self.cells_minleftover:
                return True
            
            if success:
                self.wordsplaced.append( word )
            elif len(directions) == 0:
                self.wordsrejected.append( word )
        
        return success    
    
class WSdirections():
    """
        Utilities for managing WS directions
    """
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
    def set_directions(self, combined=0):
        """
            Verify and initialise directions to combined
            :combined an integer concatination of directions
        """
        self.Chosen = []
        self.add(combined)
        
    def add(self, combined = 0):
        """
            Verify and add combined to the Chosen directions list
            :combined an integer concatination of directions
        """
        for i in range(0, len(self.Directions)):
            if combined & self.Directions[i]:
                self.Chosen.append(self.Directions[i])

    def pop(self):
        """
            Pop a random direction from the Chosen list
        """
        item = random.randint(0, len(self.Chosen) -1)
        return self.Chosen.pop(item)
        
    def append(self, item = 0):
        """
            Verify and append item onto the direction list
            :item an integer concatination of directions
        """
        self.add(item)
        

class WSwords():
    def __init__(self, wordlist = [], maxlength = 15):
        self.maxlength = maxlength
        self.wordlist = []
        self.wordlist_rejected = []
        self.wordlist, self.wordlist_rejected = self.sanitize(wordlist, maxlength)
        
    def sanitize(self, wordlist = [], maxlength = 0):
        """
            Sanitise the Wordlist by building a list of acceptable characters for a word
            rejecting 
        """
        lang = language()
        
        if wordlist == []:
            wordlist = self.wordlist        

        if maxlength == 0:
            maxlength = self.maxlength
        
        goodwords = []
        rejects   = []
        
        for word in wordlist:
            if len(word) == 0:
                continue
            word = lang.w_Tokens(word)[0]            
            if len(word) > maxlength:
                rejects.append(word)
            else:
                goodwords.append(word)
                
        return goodwords, rejects

    def pop(self):
        """
            Return a random item from WSwords.wordlist
        """
        item = random.randint(0, len(self.wordlist) -1)
        return self.wordlist.pop(item)
    def append(self, wordlist):
        """
            Append a word to WSwords.wordlist
        """
        if type(wordlist) == type(''):
            wordlist = [wordlist]
        goodwords, rejectedwords = self.sanitize(wordlist)
        
        for word in goodwords:
            self.wordlist.append(word)
        for word in rejectedwords:
            self.wordlist_rejected.append(word)
            
if __name__ == '__main__':
    pass