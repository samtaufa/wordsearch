#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    lang.Language
    
    Language

    :copyright: (c) 2009, Samiuela Loni Vea Taufa
    :license: MIT, see LICENSE.txt for more details

    Unicode Text: "ÁÂÃÄÉÊËÍÎÏÓÔÕÖÚÛÜáâãäéêëíîïóôõöúûüĀāĒēĨĩĪīŌōŨũŪūẼẽ"

"""
import string, unicodedata

class Language:
    """
        Base Language Class
        
        Defines basic methods for managing character sets in a Language
        
        'c_' denote 'character' methods
        'w_' denote 'word' methods
    """
    def __init__(self):
        self.charSet = ""
        self.charSetExt = ""
        self.wordConstructs = ""
        self.initGlottals()
        self.initCharSet()
        self.initCharSetExt()
        self.wordConstructs = self.charSet + self.charSetExt

    def initGlottals(self):
        self.apostrophe  = unicodedata.lookup('APOSTROPHE')
        self.glottals_all = self.apostrophe
    def initCharSet(self):
        self.charSet = unicode(string.letters)
    def initCharSetExt(self):
        self.charSetExt = self.apostrophe
    def c_allowNumerics( self, numerics = "" ):
        """
            Allow Numerics as part of the extended character set
        """
        if numerics == "":
            numerics = string.digits
            
        for i in numerics:
            if not (i in self.charSet or i in self.charSetExt):
                self.charSetExt += i
                
    def c_addCharacters( self, allowThese = ""):
        """
            add 'allowThese' characters to the Extended Character set.
        """
        for c in allowThese:
            if not ( c in self.charSetExt ):
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
              
        for iCurr in range(0, iMax):
            letter = line[iCurr]
            if letter in self.wordConstructs:
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