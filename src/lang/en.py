#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    English Language extensions to the Language class

    :copyright: (c) 2009, Samiuela Loni Vea Taufa
    :license: MIT, see LICENSE.txt for more details

    Unicode Text: "ÁÂÃÄÉÊËÍÎÏÓÔÕÖÚÛÜáâãäéêëíîïóôõöúûüĀāĒēĨĩĪīŌōŨũŪūẼẽ"

"""
import string, unicodedata
from lang import Language

class en(Language):
    def __init__(self, wordlist=[]):
        Language.__init__(self)
        self.initCharSet()
        self.initCharSetExt()
        self.initGlottals()
        self.wordConstructs = self.charSet + self.charSetExt + self.apostrophe
        self.initTranslators()
        self.wordlist = []
        if wordlist:
            self.wordlist = self.c_transpose(wordlist)
        
    def initCharSet(self):
        self.vowels = (
            unicodedata.lookup('LATIN SMALL LETTER A') +
            unicodedata.lookup('LATIN SMALL LETTER E') +
            unicodedata.lookup('LATIN SMALL LETTER I') +
            unicodedata.lookup('LATIN SMALL LETTER O') +
            unicodedata.lookup('LATIN SMALL LETTER U') +
            unicodedata.lookup('LATIN CAPITAL LETTER A') +
            unicodedata.lookup('LATIN CAPITAL LETTER E') +
            unicodedata.lookup('LATIN CAPITAL LETTER I') +
            unicodedata.lookup('LATIN CAPITAL LETTER O') +
            unicodedata.lookup('LATIN CAPITAL LETTER U')
        )
        self.consonants = (
            unicodedata.lookup('LATIN SMALL LETTER B') +
            unicodedata.lookup('LATIN SMALL LETTER C') +
            unicodedata.lookup('LATIN SMALL LETTER D') +
            unicodedata.lookup('LATIN SMALL LETTER F') +
            unicodedata.lookup('LATIN SMALL LETTER G') +
            unicodedata.lookup('LATIN SMALL LETTER H') +
            unicodedata.lookup('LATIN SMALL LETTER J') +
            unicodedata.lookup('LATIN SMALL LETTER K') +
            unicodedata.lookup('LATIN SMALL LETTER L') +
            unicodedata.lookup('LATIN SMALL LETTER M') +
            unicodedata.lookup('LATIN SMALL LETTER N') +
            unicodedata.lookup('LATIN SMALL LETTER O') +
            unicodedata.lookup('LATIN SMALL LETTER P') +
            unicodedata.lookup('LATIN SMALL LETTER Q') +
            unicodedata.lookup('LATIN SMALL LETTER R') +
            unicodedata.lookup('LATIN SMALL LETTER S') +
            unicodedata.lookup('LATIN SMALL LETTER T') +
            unicodedata.lookup('LATIN SMALL LETTER V') +
            unicodedata.lookup('LATIN SMALL LETTER W') +
            unicodedata.lookup('LATIN SMALL LETTER X') +
            unicodedata.lookup('LATIN SMALL LETTER Y') +
            unicodedata.lookup('LATIN SMALL LETTER Z') +
            unicodedata.lookup('LATIN CAPITAL LETTER B') +
            unicodedata.lookup('LATIN CAPITAL LETTER C') +
            unicodedata.lookup('LATIN CAPITAL LETTER D') +
            unicodedata.lookup('LATIN CAPITAL LETTER F') +
            unicodedata.lookup('LATIN CAPITAL LETTER G') +
            unicodedata.lookup('LATIN CAPITAL LETTER H') +
            unicodedata.lookup('LATIN CAPITAL LETTER J') +
            unicodedata.lookup('LATIN CAPITAL LETTER K') +
            unicodedata.lookup('LATIN CAPITAL LETTER L') +
            unicodedata.lookup('LATIN CAPITAL LETTER M') +
            unicodedata.lookup('LATIN CAPITAL LETTER N') +
            unicodedata.lookup('LATIN CAPITAL LETTER O') +
            unicodedata.lookup('LATIN CAPITAL LETTER P') +
            unicodedata.lookup('LATIN CAPITAL LETTER Q') +
            unicodedata.lookup('LATIN CAPITAL LETTER R') +
            unicodedata.lookup('LATIN CAPITAL LETTER S') +
            unicodedata.lookup('LATIN CAPITAL LETTER T') +
            unicodedata.lookup('LATIN CAPITAL LETTER V') +
            unicodedata.lookup('LATIN CAPITAL LETTER W') +
            unicodedata.lookup('LATIN CAPITAL LETTER X') +
            unicodedata.lookup('LATIN CAPITAL LETTER Y') +
            unicodedata.lookup('LATIN CAPITAL LETTER Z') 
        )
        self.charSet = (
            self.consonants + self.vowels + self.apostrophe
        )
    def initGlottals(self):
        self.apostrophe  = unicodedata.lookup('APOSTROPHE')
    
    def initTranslators(self):
        self.toLowerDict = {
            unicodedata.lookup('LATIN CAPITAL LETTER A') : unicodedata.lookup('LATIN SMALL LETTER A') ,
            unicodedata.lookup('LATIN CAPITAL LETTER E') : unicodedata.lookup('LATIN SMALL LETTER E') ,
            unicodedata.lookup('LATIN CAPITAL LETTER I') : unicodedata.lookup('LATIN SMALL LETTER I') ,
            unicodedata.lookup('LATIN CAPITAL LETTER O') : unicodedata.lookup('LATIN SMALL LETTER O') ,
            unicodedata.lookup('LATIN CAPITAL LETTER U') : unicodedata.lookup('LATIN SMALL LETTER U') ,
            unicodedata.lookup('LATIN CAPITAL LETTER B') : unicodedata.lookup('LATIN SMALL LETTER B') ,
            unicodedata.lookup('LATIN CAPITAL LETTER C') : unicodedata.lookup('LATIN SMALL LETTER C') ,
            unicodedata.lookup('LATIN CAPITAL LETTER D') : unicodedata.lookup('LATIN SMALL LETTER D') ,
            unicodedata.lookup('LATIN CAPITAL LETTER F') : unicodedata.lookup('LATIN SMALL LETTER F') ,
            unicodedata.lookup('LATIN CAPITAL LETTER G') : unicodedata.lookup('LATIN SMALL LETTER G') ,
            unicodedata.lookup('LATIN CAPITAL LETTER H') : unicodedata.lookup('LATIN SMALL LETTER H') ,
            unicodedata.lookup('LATIN CAPITAL LETTER J') : unicodedata.lookup('LATIN SMALL LETTER J') ,
            unicodedata.lookup('LATIN CAPITAL LETTER K') : unicodedata.lookup('LATIN SMALL LETTER K') ,
            unicodedata.lookup('LATIN CAPITAL LETTER L') : unicodedata.lookup('LATIN SMALL LETTER L') ,
            unicodedata.lookup('LATIN CAPITAL LETTER M') : unicodedata.lookup('LATIN SMALL LETTER M') ,
            unicodedata.lookup('LATIN CAPITAL LETTER N') : unicodedata.lookup('LATIN SMALL LETTER N') ,
            unicodedata.lookup('LATIN CAPITAL LETTER P') : unicodedata.lookup('LATIN SMALL LETTER P') ,
            unicodedata.lookup('LATIN CAPITAL LETTER Q') : unicodedata.lookup('LATIN SMALL LETTER Q') ,
            unicodedata.lookup('LATIN CAPITAL LETTER R') : unicodedata.lookup('LATIN SMALL LETTER R') ,
            unicodedata.lookup('LATIN CAPITAL LETTER S') : unicodedata.lookup('LATIN SMALL LETTER S') ,
            unicodedata.lookup('LATIN CAPITAL LETTER T') : unicodedata.lookup('LATIN SMALL LETTER T') ,
            unicodedata.lookup('LATIN CAPITAL LETTER V') : unicodedata.lookup('LATIN SMALL LETTER V') ,
            unicodedata.lookup('LATIN CAPITAL LETTER W') : unicodedata.lookup('LATIN SMALL LETTER W') ,
            unicodedata.lookup('LATIN CAPITAL LETTER X') : unicodedata.lookup('LATIN SMALL LETTER X') ,
            unicodedata.lookup('LATIN CAPITAL LETTER Y') : unicodedata.lookup('LATIN SMALL LETTER Y') ,
            unicodedata.lookup('LATIN CAPITAL LETTER Z') : unicodedata.lookup('LATIN SMALL LETTER Z') 
        }
        for k, v in zip(string.ascii_uppercase, string.ascii_lowercase):
            self.toLowerDict[k] = v

        self.toUpperDict = {
            unicodedata.lookup('LATIN SMALL LETTER A') : unicodedata.lookup('LATIN CAPITAL LETTER A') ,
            unicodedata.lookup('LATIN SMALL LETTER E') : unicodedata.lookup('LATIN CAPITAL LETTER E') ,
            unicodedata.lookup('LATIN SMALL LETTER I') : unicodedata.lookup('LATIN CAPITAL LETTER I') ,
            unicodedata.lookup('LATIN SMALL LETTER O') : unicodedata.lookup('LATIN CAPITAL LETTER O') ,
            unicodedata.lookup('LATIN SMALL LETTER U') : unicodedata.lookup('LATIN CAPITAL LETTER U') ,
            unicodedata.lookup('LATIN SMALL LETTER B') : unicodedata.lookup('LATIN CAPITAL LETTER B') ,
            unicodedata.lookup('LATIN SMALL LETTER C') : unicodedata.lookup('LATIN CAPITAL LETTER C') ,
            unicodedata.lookup('LATIN SMALL LETTER D') : unicodedata.lookup('LATIN CAPITAL LETTER D') ,
            unicodedata.lookup('LATIN SMALL LETTER F') : unicodedata.lookup('LATIN CAPITAL LETTER F') ,
            unicodedata.lookup('LATIN SMALL LETTER G') : unicodedata.lookup('LATIN CAPITAL LETTER G') ,
            unicodedata.lookup('LATIN SMALL LETTER H') : unicodedata.lookup('LATIN CAPITAL LETTER H') ,
            unicodedata.lookup('LATIN SMALL LETTER J') : unicodedata.lookup('LATIN CAPITAL LETTER J') ,
            unicodedata.lookup('LATIN SMALL LETTER K') : unicodedata.lookup('LATIN CAPITAL LETTER K') ,
            unicodedata.lookup('LATIN SMALL LETTER L') : unicodedata.lookup('LATIN CAPITAL LETTER L') ,
            unicodedata.lookup('LATIN SMALL LETTER M') : unicodedata.lookup('LATIN CAPITAL LETTER M') ,
            unicodedata.lookup('LATIN SMALL LETTER N') : unicodedata.lookup('LATIN CAPITAL LETTER N') ,
            unicodedata.lookup('LATIN SMALL LETTER P') : unicodedata.lookup('LATIN CAPITAL LETTER P') ,
            unicodedata.lookup('LATIN SMALL LETTER Q') : unicodedata.lookup('LATIN CAPITAL LETTER Q') ,
            unicodedata.lookup('LATIN SMALL LETTER R') : unicodedata.lookup('LATIN CAPITAL LETTER R') ,
            unicodedata.lookup('LATIN SMALL LETTER S') : unicodedata.lookup('LATIN CAPITAL LETTER S') ,
            unicodedata.lookup('LATIN SMALL LETTER T') : unicodedata.lookup('LATIN CAPITAL LETTER T') ,
            unicodedata.lookup('LATIN SMALL LETTER V') : unicodedata.lookup('LATIN CAPITAL LETTER V') ,
            unicodedata.lookup('LATIN SMALL LETTER W') : unicodedata.lookup('LATIN CAPITAL LETTER W') ,
            unicodedata.lookup('LATIN SMALL LETTER X') : unicodedata.lookup('LATIN CAPITAL LETTER X') ,
            unicodedata.lookup('LATIN SMALL LETTER Y') : unicodedata.lookup('LATIN CAPITAL LETTER Y') ,
            unicodedata.lookup('LATIN SMALL LETTER Z') : unicodedata.lookup('LATIN CAPITAL LETTER Z') 
        }
        for k, v in zip(string.ascii_lowercase, string.ascii_uppercase):
            self.toUpperDict[k] = v
        
    def c_transpose(self, text = []):
        """
            Transpose text in the list using the rules set up
            in transposeDict
        """
        return text
    def lowercase(self, text=""):
        """
            Convert text to lowercase
        """
        for k, v in self.toLowerDict.iteritems():
            text = text.replace(k,v)
        return text                
    def w_validFirst( self, letter):
        if letter in self.charSet or letter in self.charSetExt:
            return True
        return False
    def w_Tokens(self, line = u""):
        """
        From a line of text, return tokens for each validated word construct
        """
        #if line == "":
        #    line = self.list_words
        
        iTokenStart = 0
        iPrev = 0
        iCurr = 0
        iMax  = len(line)
        Tokens = []
        wordboundary = False
        for iCurr in range(0, iMax):
            letter = line[iCurr]
            if letter == self.apostrophe:
                if iCurr == iTokenStart:
                    wordboundary = True
                elif iCurr == iMax - 1:
                    Tokens.append(line[iTokenStart:iMax -1])
                elif line[iCurr+1] in self.consonants: # contraction
                    pass
                else: # Word boundary ?
                    wordboundary = True
            elif letter in self.wordConstructs:
                if iCurr == iMax - 1:
                    Tokens.append(line[iTokenStart:iMax])
            else: # Word Boundary ?
                wordboundary = True
            if wordboundary:
                if iTokenStart == iCurr:
                    iTokenStart = iCurr + 1 #i.e. we're inside a non-token
                else:
                    Tokens.append(line[iTokenStart:iCurr])
                    iTokenStart = iCurr + 1
                wordboundary = False
        return Tokens

if __name__ == "__main__":
    pass