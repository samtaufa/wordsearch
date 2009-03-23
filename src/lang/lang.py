#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2008, Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
import string, unicodedata

class Language:
    def __init__(self):
        self.charSet = ""
        self.charSetExt = ""
        self.initGlottals()
        self.initCharSet()
        self.initCharSetExt()
    def initCharSet(self):
        self.charSet = unicode(string.letters)
    def initCharSetExt(self):
        self.charSetExt = self.apostrophe
    def initGlottals(self):
        self.glottals_all = (unicodedata.lookup('APOSTROPHE') +
                             unicodedata.lookup('GRAVE ACCENT') +
                             unicodedata.lookup('ACUTE ACCENT') +
                             unicodedata.lookup('MODIFIER LETTER TURNED COMMA') +
                             unicodedata.lookup('MODIFIER LETTER APOSTROPHE') +
                             unicodedata.lookup('MODIFIER LETTER REVERSED COMMA') +
                             unicodedata.lookup('MODIFIER LETTER ACUTE ACCENT') +
                             unicodedata.lookup('MODIFIER LETTER GRAVE ACCENT') +
                             unicodedata.lookup('COMBINING TURNED COMMA ABOVE') +
                             unicodedata.lookup('COMBINING REVERSED COMMA ABOVE') +
                             unicodedata.lookup('COMBINING COMMA ABOVE') +
                             unicodedata.lookup('COMBINING COMMA ABOVE RIGHT') +
                             unicodedata.lookup('COMBINING GRAVE TONE MARK') +
                             unicodedata.lookup('COMBINING ACUTE TONE MARK') +
                             unicodedata.lookup('LATIN LETTER GLOTTAL STOP') +
                             unicodedata.lookup('LATIN CAPITAL LETTER GLOTTAL STOP')
                             )
        self.apostrophe  = unicodedata.lookup('APOSTROPHE')
    def c_allowNumerics( self, numerics = "" ):
        if numerics == "":
            numerics = string.digits
            
        for i in numerics:
            if not (i in self.charSet or i in self.charSetExt):
                self.charSetExt += i
                
    def c_addCharacters( self, allowThese = ""):
        for c in allowThese:
            if not ( c in self.charSet or c in self.charSetExt):
                self.charSetExt += c
                
    def c_delCharacters( self, blockThese = u""):
        for letter in blockThese:
            if letter in self.charSet:
                self.charSet = self.charSet.replace(letter,'')
            if letter in self.charSetExt:
                self.charSetExt = self.charSetExt.replace(letter,'')
    def c_transform( self, letters_in = u"", transFrom = u"", transTo = u""):
        """Transform a string where characters exist in Table "transFrom"
        to their indexed counterpart in transTo
        """
        myletters = letters_in
        for letter in letters_in:
            if letter in transFrom:
                index = transFrom.index(letter)
                newletter = transTo[index]
                myletters = myletters.replace(letter, newletter)
        return myletters
    
    def w_validFirst( self, letter):
        return True # Any unique rules for first characters in a word?
    def w_Tokens(self, line = None):
        if line is None:
            line = self.list_words
        
        iTokenStart = 0
        iPrev = 0
        iCurr = 0
        iMax  = len(line)
        Tokens = []
        
        wordConstructs = self.charSet + self.charSetExt
        
        for iCurr in range(0, iMax):
            letter = line[iCurr]
            if letter in wordConstructs:
                if iCurr == iMax-1: # last letter special exception
                    if letter not in self.glottals_all:
                        Tokens.append(line[iTokenStart:iMax])
                    else:
                        Tokens.append(line[iTokenStart:iMax-1])
                elif letter in self.glottals_all:
                    # transform glottal if inside a word and next letter is a valid letter
                    if iCurr > iTokenStart:
                        if line[iCurr+1] in self.charSet:
                            line = line[0:iCurr] + self.apostrophe + line[iCurr+1:]
                        else:
                            Tokens.append(line[iTokenStart:iCurr])
                            iTokenStart = iCurr + 1
                    else:
                        iTokenStart = iCurr + 1
            else:                
                if iCurr == iTokenStart: # We're still at the start
                    iTokenStart += 1     # Ignore the error and start with the next letter
                else:
                    Tokens.append(line[iTokenStart:iCurr])
                    iTokenStart = iCurr + 1
            iPrev = iCurr
        return Tokens
    

if __name__ == "__main__":
    pass