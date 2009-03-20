#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2008, Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
#
# 
import random, string, copy, time

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
        self.wordsplaced = {}
        self.wordsrejected = {}
        self.rejectMax = 100
        self.maxrow = 0
        self.maxcol = 0
        self.maxruntime = 60.0
        
        self.maxrow, self.maxcol = size
        self.wsDir = WSdirections()
        self.wsDir.set_directions(directions)
        self.directions = self.wsDir.Chosen
        self.wordlist = wordlist
        
        self.matrix, self.cells_available, self.cells_minleftover = \
            self.init_cells(self.maxrow, self.maxcol)
        self.startCells = []
        
        self.language = "to"
        self.WStext = WStext()
        self.debug = False
        
    def set_directions(self, directions = 1):
        """
            :directions - integer concatenation of wsDirections.Directions
        """
        self.directions = self.wsDir.set_directions(directions)
        
    def init_cells(self, rows=0, cols=0):
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
            if self.debug: print 'word is too long'
            return [] # word is too long
        
        if length > x_max  and (direction in [dir.Up,
                                                  dir.Down]):
            if self.debug: print 'word is too long X'
            return [] # word is too long
        
        if length > y_max and (direction in [dir.Right,
                                                 dir.Left]):
            if self.debug: print 'word is too long Y'
            return [] # word is too long
        

        # Columns
        if direction in [dir.Right, dir.DiagUpRight, dir.DiagDwnRight]:
            y_max = self.maxcol - (length - 1)
            
        if direction in [dir.Left, dir.DiagUpLeft, dir.DiagDwnLeft]:
            y_min = (length - 1)
            y_max = self.maxcol

        # Rows
        if direction in [dir.Down, dir.DiagDwnRight, dir.DiagDwnLeft]:
            x_max = self.maxcol - (length - 1)
            
        if direction in [dir.Up, dir.DiagUpRight, dir.DiagUpLeft]:
            x_min = (length - 1)
            x_max = self.maxrow
            
        if x_min < 0 or y_min < 0 or x_max < x_min or y_max < y_min:
            if self.debug: print 'maths went wrong'
            return [] # shouldn't get here, but worth checking
            
        if self.debug: print "X(%s -> %s) to Y(%s -> %s)" % (x_min, x_max, y_min, y_max)
        tempGrid =[]
        if x_min == x_max:
            if self.debug: print "(%s, %s) X equal" % (x_min, x_max)
            for yc in range (y_min, y_max):
                tempGrid.append ([x_min, yc])
        else:
            for xc in range ( x_min, x_max ):
                if y_min == y_max:
                    if self.debug: print "(%s, %s) Y equal" % (y_min, y_max)
                    tempGrid.append([xc, y_min])
                else:
                    for yc in range (y_min, y_max):
                        tempGrid.append ([xc, yc])
        
        return tempGrid[:]

    def populate_matrix(self, matrix, wordlist):
        """
            Outer Looop:
        """
        if len(wordlist) == 0: # special case, recursion completed
            return True, matrix, [], []
        success = False
        accepted = []
        rejected = []
        startPoint = (0,0)
        dirGo = 0
        
        while 1: # Loop through all available words
            if success or len(wordlist) == 0:
                break
            alldirections = self.directions[:]
            if self.debug: print
            if self.debug: print "%s " % wordlist[0],
            while 1: # Loop through all available directions
                if success or len(alldirections) == 0:
                    break
                dirGo =  alldirections.pop(random.randint(0, len(alldirections) -1 ))
                #dirGo =  alldirections.pop(0)
                subGrid = self.startGrid(dirGo, len(wordlist[0]))
                if self.debug: print " -> ", dirGo, "@ ", 
                while 1: # Loop through all available Grid positions
                    if success or len(subGrid) == 0:
                        break
                    startPoint = subGrid.pop( random.randint(0, len(subGrid)-1) )
                    #startPoint = subGrid.pop(0)
                    if self.debug: print " (%s,%s)" % (startPoint[0], startPoint[1]),
                    if self.canInsertWord(wordlist[0], startPoint, dirGo, matrix):
                        # note it can be done for this word and do it
                        success, matrix, accepted, rejected, cellValues = self.insertWord(wordlist, startPoint, dirGo, matrix)
                        if not success:
                            self.revertWord(wordlist[0], startPoint, dirGo, matrix, cellValues)

            word = wordlist.pop(0)
            if success: #
                accepted.append( word )
                if not word in self.wordsplaced:
                    self.wordsplaced[ word ] = [0, startPoint, dirGo]
                self.wordsplaced[ word ] = [self.wordsplaced[word][0] + 1, startPoint, dirGo ]
            else:
                rejected.append( word ) # word needs to be rejected
                if not word in self.wordsrejected:
                    self.wordsrejected[ word ] = 0
                self.wordsrejected[ word ] += 1
                #wordlist.append(wordlist[0])
                if self.wordsrejected[ word ] > self.rejectMax:
                    success = True
        return success, matrix, accepted, rejected

    def populate(self):
        """
            Main Loop to insert document into Matrix Grid
        """
        maxruntime = time.time() + self.maxruntime
        
        
        workingList = self.wordlist[:]
        workingMatrix = self.matrix[:]
        
        longest = max (self.maxcol, self.maxrow)
        workingList, rejected = self.WStext.sanitize_words(workingList, longest)
        success = False
        rejected2 = []
        while 1:  # Loop until timed out or success 'conditions' reached
            if success or time.time() >= maxruntime or len(workingList) == 0:
                break
            success, workingMatrix, accepted, rejected2 = self.populate_matrix(workingMatrix, workingList)
            
            #if self.cells_available <= self.cells_minleftover:
            #    success = True 
            if not success:
                tmp_word = ''
                tmp_cnt = 0
                for word in rejected2:
                    if rejected2[word] > tmp_cnt:
                        tmp_word = word
                if tmp_cnt > 0:
                    rejected += [tmp_word]
                    workingList.pop(workingList.index(tmp_word))

        if rejected2 != []:
            rejected += rejected2
        return workingMatrix, accepted, rejected
            
    def insertWord(self,wordList, startPos, direction, matrix):
        """
            Recursively insert a word into the Matrix and
            return success state
            
            return: True/False
            curr:   (x, y) current grid cell
            word:   word to insert
            direction: WSdirections.Direction to insert word
        """
        row, col = startPos
        storeCellContent = ''
        word = wordList[0]
        for i in range(len(word)):
            storeCellContent += matrix[row][col] 
            matrix[row][col] = word[i]
            row, col = self.cellNext((row,col), direction)
        success, matrix, accepted, rejected = self.populate_matrix(matrix, wordList[1:])
        return success, matrix, accepted, rejected, storeCellContent
    
    def revertWord(self, word, startPos, direction, matrix, storeCellContent):
        row, col = startPos
        for i in range(len(storeCellContent)):
            matrix[row][col] = storeCellContent[i]
            row, col = self.cellNext((row, col), direction)
        
    def canInsertWord(self, word, startPos, direction, matrix):
        if not self.lengthOK(len(word), startPos, direction):
            if self.debug: print "Error: Word length too long"
            return False
        success = True
        pos = startPos
        for i in range(len(word)):
            if not (matrix[pos[0]][pos[1]] == self.INPUT_MASK or
                    matrix[pos[0]][pos[1]] == word[i]):
                success = False
                break
            pos = self.cellNext(pos, direction)
        return success
    def lengthOK(self, length, startPos, direction):
        row, col = startPos
        if direction in [self.wsDir.Right, self.wsDir.DiagUpRight, self.wsDir.DiagDwnRight]:
            col += (length - 1)
        if direction in [self.wsDir.Left, self.wsDir.DiagDwnLeft, self.wsDir.DiagDwnRight]:
            col -= (length - 1)
            
        # Movements in the Y plane (Note: Left and Right do not move)
        if direction in [self.wsDir.DiagUpLeft, self.wsDir.Up, self.wsDir.DiagUpRight]:
            row -= (length - 1)
        elif direction in [self.wsDir.Down, self.wsDir.DiagDwnLeft, self.wsDir.DiagDwnRight]:
            row += (length - 1)
        
        success = False
        if 0 <= row <= (self.maxrow - 1) and 0 <= col <= ( self.maxcol - 1 ):
            success = True
        return success
    def cellNext(self, currPos, direction):
        """
            return: (x, y) Next cell in a given direction
            curr:   (x, y) Current cell location
            direction: WSdirections.Direction to move
        """
        row, col = currPos
        # Movements in the X plane (Note: UP AND Down do not move)
        if direction in [self.wsDir.Right, self.wsDir.DiagUpRight, self.wsDir.DiagDwnRight]:
            col += 1
        if direction in [self.wsDir.Left, self.wsDir.DiagDwnLeft, self.wsDir.DiagDwnRight]:
            col -= 1
            
        # Movements in the Y plane (Note: Left and Right do not move)
        if direction in [self.wsDir.DiagUpLeft, self.wsDir.Up, self.wsDir.DiagUpRight]:
            row -= 1
        elif direction in [self.wsDir.Down, self.wsDir.DiagDwnLeft, self.wsDir.DiagDwnRight]:
            row += 1
        
        #if not (0 <= row <= self.maxrow and 0 <= col <= self.maxcol):
        #    raise 'Matrix Size Overflow (x,y) Max(%d,%d) Given (%d,%d) Calc(%d,%d) Direction:%d' \
        #    %( self.maxrow, self.maxcol, currPos[0], currPos[1],
        #      row, col, direction
        #    )
        return row, col
class WSdirections():
    """
        Utilities for management of WS directions
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
        self.Chosen = self.add(combined)
        return self.Chosen
    
    def add(self, combined = 0):
        """
            Verify and add combined to the Chosen directions list
            :combined an integer concatination of directions
        """
        directions = self.Chosen
        for i in range(0, len(self.Directions)):
            if combined & self.Directions[i]:
                directions.append(self.Directions[i])
        return directions

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
        

class WStext():
    """
        Utilities for managing WS wordlists
    """
    def __init__(self, wordlist = [], maxlength = 1000, lingua = "to"):
        self.maxlength = maxlength
        self.wordlist = []
        self.wordlist_rejected = []
        self.language = self.setLanguage( lingua )
        self.wordlist, self.wordlist_rejected = self.sanitize_words(wordlist, maxlength)
        
    def setLanguage(self, lingua):
        
        if lingua == "eng" or lingua[0:1] == "en":
            from lang import en as language
        elif lingua == "local":
            from lang import Language as language
        else:
            from lang import to as language
            
        lang = language()
        return lang
    
    def sanitize_words(self, wordlist = [], maxlength = 0):
        """
            Sanitise the Wordlist by building a list of
            acceptable characters for a word
            
            return: goodwords, rejectedwords
        """
        
        if wordlist == []:
            wordlist = self.wordlist        

        if maxlength == 0:
            maxlength = self.maxlength
        
        goodwords = []
        rejects   = []
        
        for word in wordlist:
            if len(word) == 0:
                continue
            word = self.language.w_Tokens(word)[0]            
            if len(word) > maxlength:
                rejects.append(word)
            else:
                goodwords.append(word)
                
        return goodwords, rejects

    def pop(self):
        """
            Return a random item from WStext.wordlist
        """
        item = random.randint(0, len(self.wordlist) -1)
        return self.wordlist.pop(item)
    def append(self, wordlist):
        """
            Append a word to WStext.wordlist
        """
        if type(wordlist) == type(''):
            wordlist = [wordlist]
        goodwords, rejectedwords = self.sanitize_words(wordlist)
        
        for word in goodwords:
            self.wordlist.append(word)
        for word in rejectedwords:
            self.wordlist_rejected.append(word)
            
class WSformats():
    def __init__(self, accepted =[], matrix=[], solution={}, rejected = []):
        self.accepted = accepted
        self.matrix = matrix
        self.rejected = rejected
        self.solution = solution
        self.letterBin = ""
        
        if accepted != []:
            self.fillLetterBin()

        wsmatrix = WSmatrix()
        self.INPUT_MASK = wsmatrix.INPUT_MASK
        self.INPUT_BLOCK = wsmatrix.INPUT_BLOCK
        
    def textDirection(self, direction):
        if direction == 1:
            return "Right"
        elif direction == 2:
            return "Left"
        elif direction == 4:
            return "Up"
        elif direction == 8:
            return "Down"
        elif direction == 16:
            return "Diagonal Up Left"
        elif direction == 32:
            return "Diagonal Up Right"
        elif direction == 64:
            return "Diagonal Down Left"
        elif direction == 128:
            return "Diagonal Down Right"
        
        return "ERROR"
    
    def fillLetterBin(self, accepted = []):
        if accepted == []:
            accepted = self.accepted        
        
        all_letters = ""
        for line in accepted:
            all_letters += line
        
        self.letterBin = all_letters
        
    def getLetter(self):
        x = len (self.letterBin)
        if x > 0:
            return self.letterBin[random.randint(0, x - 1)]
        return INPUT_MASK
 
    def html(self, accepted=[], matrix=[], solution={}):
        if accepted == []:
            accepted = self.accepted        
        if matrix == []:
            matrix = self.matrix
        if solution == {}:
            solution = self.solution
        
        accepted.sort()
        self.fillLetterBin()
        myaccepted = self.html_accepted(accepted)
        mymatrix = self.html_matrix(matrix)
        mysolution = self.html_solution(matrix, accepted, solution)

        return myaccepted, mymatrix, mysolution
    
    def html_solution(self, matrix, accepted, solution):
        
        keys = solution.keys()
        keys.sort()
        mysolution ="<table class='wssolution'>"
        mysolution += "\n  <tr><th>Word</th><th>Start @</th><th>Direction</th></tr>"
        for word in keys:
            if word in accepted:
                mysolution += "\n  <tr><td>%s</td><td>(%s,%s)</td><td>%s</td></tr>" % (
                    word,
                    solution[word][1][0] + 1, solution[word][1][1] + 1,
                    self.textDirection(solution[word][2]))
        mysolution += "\n</table>"
        mysolution += "\n\n"
        mysolution += self.html_matrix(matrix,False)
        
        return mysolution
    
    def html_accepted(self, accepted = []):        
        myaccepted = "<table class='WStext'>"
        for word in accepted:
            myaccepted += "\n  <tr><td>" + str(word) + "</td></tr>"
        myaccepted += "\n</table>"
        return myaccepted
        
    def html_matrix(self, matrix = [], obfuscate = True):        
        rows = len(matrix)
        cols = len(matrix[0])
        mymatrix = "<table class='wsmatrix'>"
        
        for row in range(rows):
            mymatrix += "\n    <tr>"
            for col in range(cols):
                cellvalue = matrix[row][col]
                if cellvalue[0] == self.INPUT_MASK and obfuscate:
                    cellvalue = self.getLetter()
                    
                mymatrix += "<td>" + cellvalue + "</td>"
            mymatrix += "</tr>"
        mymatrix += "\n</table>"
        return mymatrix
    
    def xml(self, accepted=[], matrix=[], solution=[]):
        pass
    def unicode(self, accepted=[], matrix=[], solution={}):
        if accepted == []:
            accepted = self.accepted        
        if matrix == []:
            matrix = self.matrix
        if solution == {}:
            solution = self.solution
        
        accepted.sort()
        self.fillLetterBin()
        myaccepted = self.unicode_accepted(accepted)
        mymatrix = self.unicode_matrix(matrix)
        mysolution = self.unicode_solution(matrix, accepted, solution)

        return myaccepted, mymatrix, mysolution
    
    def unicode_solution(self, matrix, accepted, solution):
        
        keys = solution.keys()
        keys.sort()
        mysolution =""
        mysolution += "\nWord\tStart @\tDirection"
        for word in keys:
            if word in accepted:
                mysolution += "\n  %s\t(%s,%s)\t%s" % (
                    word,
                    solution[word][1][0] + 1, solution[word][1][1] + 1,
                    self.textDirection(solution[word][2]))
        mysolution += "\n"
        mysolution += "\n\n"
        mysolution += self.unicode_matrix(matrix,False)
        
        return mysolution
    
    def unicode_accepted(self, accepted = []):        
        myaccepted = ""
        for word in accepted:
            myaccepted += "\n  %s" % str(word)
        myaccepted += "\n"
        return myaccepted
        
    def unicode_matrix(self, matrix = [], obfuscate = True):        
        rows = len(matrix)
        cols = len(matrix[0])
        mymatrix = ""
        
        for row in range(rows):
            mymatrix += "\n    "
            for col in range(cols):
                cellvalue = matrix[row][col]
                if cellvalue[0] == self.INPUT_MASK and obfuscate:
                    cellvalue = self.getLetter()
                    
                mymatrix += "%s " % cellvalue
            mymatrix += ""
        mymatrix += "\n"
        return mymatrix
    
    
if __name__ == '__main__':
    pass