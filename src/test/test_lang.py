#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

    Test classes for language libraries lang.lang.Language and
    lang.to.to
    
    :copyright: (c) 2009, Samiuela Loni Vea Taufa
    :license: MIT, see LICENSE.txt for more details
    
    Unicode Text: "ÁÂÃÄÉÊËÍÎÏÓÔÕÖÚÛÜáâãäéêëíîïóôõöúûüĀāĒēĨĩĪīŌōŨũŪūẼẽ"

"""

import sys, string, unicodedata
from BeautifulSoup import BeautifulSoup
import libpry
from lang.lang import Language
from lang.to import to
class u_Language(libpry.AutoTree):
    def test_Tokens1(self):
        """Word Tokenize a string"""
        line1 = "This is a line of text'ed words"
        line_expect = ["This","is","a","line","of",u"text'ed", "words"]
        test1 = Language()
        Tokens = test1.w_Tokens(line1)
        assert Tokens == line_expect

    def test_Tokens2(self):    
        """Word Tokenize a string with non-word characters"""
        line2 = "This$ is# a 6 line43 of text'ed words"
        line_expect = ["This","is","a","line","of",u"text'ed","words"]
        test2 = Language()
        Tokens = test2.w_Tokens(line2)
        assert Tokens == line_expect

    def test_Tokens3(self):    
        """Word Tokenize a string with an apostrophe leading a word"""
        line3 = "This is a line of 'text'ed' words"
        line_expect = ["This","is","a","line","of",u"text'ed","words"]
        test3 = Language()
        Tokens = test3.w_Tokens(line3)
        assert Tokens == line_expect
        
    def test_Tokens4(self):    
        """Word Tokenize a string with apostrophe pre-pending words 
        (including the last word in a string)"""
        line4 = "This is a line of 'text'ed' words'"
        line_expect = ["This","is","a","line","of",u"text'ed","words"]
        test4 = Language()
        Tokens = test4.w_Tokens(line4)
        assert Tokens == line_expect
        
    def test_Tokens5(self):    
        """Word Tokenize a string with apostrophne pre-pending words
        beginning with a vowel"""
        line5 = "This 'is 'a 'line of text'ed' words"
        line_expect = ["This","is","a","line","of",u"text'ed","words"]
        test5 = Language()
        Tokens = test5.w_Tokens(line5)
        assert Tokens == line_expect
        
class u_To(libpry.AutoTree):
    def test_Tokens1(self):    
        """Word Tokenize a string with a glottal"""
        line1 = "This is a line of text'ed words"
        line_expect = ["This","is","a","line","of",u"text\u02bbed","words"]
        test1 = to()
        Tokens = test1.w_Tokens(line1)
        assert Tokens == line_expect

    def test_Tokens2(self):    
        """Word Tokenize a string with non-word characters"""
        line2 = "This$ is# a 6 line43 of text'ed words"
        line_expect = ["This","is","a","line","of",u"text\u02bbed","words"]
        test2 = to()
        Tokens = test2.w_Tokens(line2)
        assert Tokens == line_expect

    def test_Tokens3(self):    
        """Word Tokenize a string with apostrophe pre-pending words 
        and ending words"""
        line3 = "This is a line of 'text'ed' words'"
        line_expect = ["This","is","a","line","of",u"text\u02bbed","words"]
        test3 = to()
        Tokens = test3.w_Tokens(line3)
        assert Tokens == line_expect        
        
    def test_Tokens4(self):    
        """Word Tokenize a string with apostrophe [pre|post]-pending words 
        (including the last word in a string)"""
        line4 = "This is a line of 'text'ed' words'"
        line_expect = ["This","is","a","line","of",u"text\u02bbed","words"]
        test4 = to()
        Tokens = test4.w_Tokens(line4)
        assert Tokens == line_expect
    
    def test_Tokens5(self):
        """Word Tokenize a string with apostropne pre-pending words
        beginning with a vowel (different meaning in Tongan Language than English)"""
        line5 = "This 'is 'a 'line of text'ed' words"
        line_expect = ["This",u"\u02bbis",u"\u02bba","line","of",u"text\u02bbed","words"]
        test5 = to()
        Tokens = test5.w_Tokens(line5)
        assert Tokens == line_expect

    def test_Tokens7(self):
        """Word contains a dierisis and leading glottal"""
        line7="""�Otua Taumai� �al�,"""
        line_expect = [u"\u02bbOtua",u"Taumai\u0101",u"\u02bbal\u0101"]
        test = to()
        Tokens = test.w_Tokens(line7.decode('cp1252'))
        assert Tokens == line_expect
    def test_Tokens8(self):
        """Words contain intermingled msword smart single quotes ` and ' 
        They all become glottals in Tongan Language"""
        line8="""�Iteita tamasi�i �i mu�a fa�iteliha;"""
        line_expect = [u"\u02bbIteita", u"tamasi\u02bbi", u"\u02bbi", u"mu\u02bba", u"fa\u02bbiteliha"]
        test = to()
        Tokens = test.w_Tokens(line8.decode('cp1252'))
        assert Tokens == line_expect
    def test_transform1(self):
        test = to()
        answer = test.c_transform("o","o",unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'))
        assert answer == unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON')
    def test_transform3(self):
        test = to()
        answer = test.c_transform(test.diacritics_all, test.diacritics_all, test.diacritics_to)
        assert answer == test.diacritics_to
        
tests = [
    u_Language(),
    u_To()
]