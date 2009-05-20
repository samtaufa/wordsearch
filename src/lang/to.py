#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    Tongan Language extensions to the Language class

    :copyright: (c) 2009, Samiuela Loni Vea Taufa
    :license: MIT, see LICENSE.txt for more details

    Unicode Text: "ÁÂÃÄÉÊËÍÎÏÓÔÕÖÚÛÜáâãäéêëíîïóôõöúûüĀāĒēĨĩĪīŌōŨũŪūẼẽ"

"""
import string, unicodedata
from lang import Language

class to(Language):
    def __init__(self, wordlist=[]):
        Language.__init__(self)
        self.initCharSet()
        self.initCharSetExt()
        self.initGlottals()
        # Compromise for mis-typed documents
        self.c_addCharacters(self.diacritics_all) 
        # Compromise for mis-typed documents
        self.c_addCharacters(self.glottals_all) 
        # Compromise for non-Tongan words, valid in Tongan context
        self.c_addCharacters(string.ascii_lowercase + string.ascii_uppercase)
        self.wordConstructs = self.charSet + self.charSetExt + self.apostrophe
        self.initTranslators()
        self.wordlist = []
        if wordlist:
            self.wordlist = self.c_transpose(wordlist)
        
    def initCharSet(self):
        self.vowel_with_diacritics = (
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH ACUTE')
            )
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
            unicodedata.lookup('LATIN CAPITAL LETTER U') +
            self.vowel_with_diacritics
        )
        self.consonants = (
            unicodedata.lookup('LATIN SMALL LETTER F') +
            unicodedata.lookup('LATIN SMALL LETTER H') +
            unicodedata.lookup('LATIN SMALL LETTER K') +
            unicodedata.lookup('LATIN SMALL LETTER L') +
            unicodedata.lookup('LATIN SMALL LETTER M') +
            unicodedata.lookup('LATIN SMALL LETTER N') +
            unicodedata.lookup('LATIN SMALL LETTER G') +
            unicodedata.lookup('LATIN SMALL LETTER P') +
            unicodedata.lookup('LATIN SMALL LETTER S') +
            unicodedata.lookup('LATIN SMALL LETTER T') +
            unicodedata.lookup('LATIN SMALL LETTER V') +
            unicodedata.lookup('LATIN CAPITAL LETTER F') +
            unicodedata.lookup('LATIN CAPITAL LETTER H') +
            unicodedata.lookup('LATIN CAPITAL LETTER K') +
            unicodedata.lookup('LATIN CAPITAL LETTER L') +
            unicodedata.lookup('LATIN CAPITAL LETTER M') +
            unicodedata.lookup('LATIN CAPITAL LETTER N') +
            unicodedata.lookup('LATIN CAPITAL LETTER G') +
            unicodedata.lookup('LATIN CAPITAL LETTER P') +
            unicodedata.lookup('LATIN CAPITAL LETTER S') +
            unicodedata.lookup('LATIN CAPITAL LETTER T') +
            unicodedata.lookup('LATIN CAPITAL LETTER V') 
        )
        self.glottal  = unicodedata.lookup('MODIFIER LETTER TURNED COMMA')
            # unicodedata.lookup('LEFTER SINGLE QUOTATION MARK') # when character not available

        self.charSet = (
            self.consonants + self.vowels + self.glottal
#           + unicodedata.lookup('FULL STOP')
        )
    def initGlottals(self):
        self.apostrophe  = unicodedata.lookup('APOSTROPHE')
        self.glottals_all = (self.apostrophe +
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
                             unicodedata.lookup('LATIN CAPITAL LETTER GLOTTAL STOP') +
                             unicodedata.lookup('LEFT SINGLE QUOTATION MARK') +
                             unicodedata.lookup('RIGHT SINGLE QUOTATION MARK') 
                             )
    
    def initCharSetExt(self):
        """Diacritical mark: a mark placed over, under, alongside or
        attached to a letter to indicate pronunciation, stress, or other value.
        """
        self.diacritics_all = (
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH DIAERESIS') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH DIAERESIS') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH DIAERESIS') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH DIAERESIS') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH DIAERESIS') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH DIAERESIS') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH DIAERESIS') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH DIAERESIS') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH DIAERESIS') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH DIAERESIS') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH TILDE') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH TILDE') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH TILDE') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH TILDE') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH TILDE') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH TILDE') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH TILDE') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH TILDE') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH TILDE') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH TILDE') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH GRAVE') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH GRAVE') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH GRAVE') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH GRAVE') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH GRAVE') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH GRAVE') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH GRAVE') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH GRAVE') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH GRAVE') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH GRAVE') 
            )    
        #self.charSetExt = self.diacritics_all
    def initTranslators(self):
        self.toLowerDict = {
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH GRAVE') : unicodedata.lookup('LATIN SMALL LETTER A WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH GRAVE') : unicodedata.lookup('LATIN SMALL LETTER E WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH GRAVE') : unicodedata.lookup('LATIN SMALL LETTER I WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH GRAVE') : unicodedata.lookup('LATIN SMALL LETTER O WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH GRAVE') : unicodedata.lookup('LATIN SMALL LETTER U WITH GRAVE') 
        }
        for k, v in zip(string.ascii_uppercase, string.ascii_lowercase):
            self.toLowerDict[k] = v

        self.toUpperDict = {
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH GRAVE'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH GRAVE'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH GRAVE'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH GRAVE'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH GRAVE'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH GRAVE')
        }
        for k, v in zip(string.ascii_lowercase, string.ascii_uppercase):
            self.toUpperDict[k] = v
            
        self.transposeDict = {
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH ACUTE') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH ACUTE') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH CIRCUMFLEX') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH CIRCUMFLEX') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH DIAERESIS') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH DIAERESIS') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH TILDE') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH TILDE') : unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON'), 
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER A WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER E WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER I WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER O WITH GRAVE'), 
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH GRAVE') : unicodedata.lookup('LATIN CAPITAL LETTER U WITH GRAVE'), 
            unicodedata.lookup('LATIN SMALL LETTER A WITH GRAVE') : unicodedata.lookup('LATIN SMALL LETTER A WITH GRAVE'), 
            unicodedata.lookup('LATIN SMALL LETTER E WITH GRAVE') : unicodedata.lookup('LATIN SMALL LETTER E WITH GRAVE'), 
            unicodedata.lookup('LATIN SMALL LETTER I WITH GRAVE') : unicodedata.lookup('LATIN SMALL LETTER I WITH GRAVE'), 
            unicodedata.lookup('LATIN SMALL LETTER O WITH GRAVE') : unicodedata.lookup('LATIN SMALL LETTER O WITH GRAVE'), 
            unicodedata.lookup('LATIN SMALL LETTER U WITH GRAVE') : unicodedata.lookup('LATIN SMALL LETTER U WITH GRAVE'),
            unicodedata.lookup('APOSTROPHE') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('GRAVE ACCENT') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('ACUTE ACCENT') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('MODIFIER LETTER TURNED COMMA') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('MODIFIER LETTER APOSTROPHE') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('MODIFIER LETTER REVERSED COMMA') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('MODIFIER LETTER ACUTE ACCENT') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('MODIFIER LETTER GRAVE ACCENT') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('COMBINING TURNED COMMA ABOVE') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('COMBINING REVERSED COMMA ABOVE') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('COMBINING COMMA ABOVE') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('COMBINING COMMA ABOVE RIGHT') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('COMBINING GRAVE TONE MARK') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('COMBINING ACUTE TONE MARK') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('LATIN LETTER GLOTTAL STOP') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('LATIN CAPITAL LETTER GLOTTAL STOP') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('LEFT SINGLE QUOTATION MARK') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA'),
            unicodedata.lookup('RIGHT SINGLE QUOTATION MARK') : unicodedata.lookup('MODIFIER LETTER TURNED COMMA')
        }
    def c_transpose(self, text = []):
        """
            Transpose text in the list using the rules set up
            in transposeDict
        """
        isString = False
        if type(text) == type(u""):
            isString = True
            text = [text]
        elif type(text) == type(""):
            isString = True
            text = [unicode(text)]
            
        newtext = []
        for i in range(len(text)):
            line = text[i]
            for k, v in self.transposeDict.iteritems():
                line = line.replace(k,v)
            newtext.append(line)
        
        if isString: return newtext[0]
        
        return newtext
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
            if letter in self.glottals_all:
                if iCurr == iMax - 1:
                    Tokens.append(line[iTokenStart:iMax -1])
                elif line[iCurr+1] in self.vowels:
                    line = line[:iCurr] + \
                        self.glottal + \
                        line[iCurr+1:]
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