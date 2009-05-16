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
from lang.en import en

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
class u_En(libpry.AutoTree):
    def test_Tokens1(self):
        """Word Tokenize a string"""
        line1 = "This is a line of text'ed words"
        line_expect = ["This","is","a","line","of","text","ed", "words"]
        test1 = en()
        Tokens = test1.w_Tokens(line1)
        assert Tokens == line_expect

    def test_Tokens2(self):    
        """Word Tokenize a string with non-word characters"""
        line2 = "This$ is# a 6 line43 of text'ed words"
        line_expect = ["This","is","a","line","of","text","ed","words"]
        test2 = en()
        Tokens = test2.w_Tokens(line2)
        assert Tokens == line_expect

    def test_Tokens3(self):    
        """Word Tokenize a string with an apostrophe leading a word"""
        line3 = "This is a line of 'text'ed' words"
        line_expect = ["This","is","a","line","of","text", "ed","words"]
        test3 = en()
        Tokens = test3.w_Tokens(line3)
        assert Tokens == line_expect
        
    def test_Tokens4(self):    
        """Word Tokenize a string with apostrophe pre-pending words 
        (including the last word in a string)"""
        line4 = "This is a line of 'text'ed' words'"
        line_expect = ["This","is","a","line","of","text", "ed","words"]
        test4 = en()
        Tokens = test4.w_Tokens(line4)
        assert Tokens == line_expect
        
    def test_Tokens5(self):    
        """Word Tokenize a string with apostrophne pre-pending words
        beginning with a vowel"""
        line5 = "This 'is 'a 'line of text'ed' words"
        line_expect = ["This","is","a","line","of","text", "ed","words"]
        test5 = en()
        Tokens = test5.w_Tokens(line5)
        assert Tokens == line_expect        
class u_To(libpry.AutoTree):
    def test_Tokens1(self):    
        """Word Tokenize a string with a glottal"""
        line1 = "This is a line of text'ed words"
        line_expect = [u"This",u"is",u"a",u"line",u"of",u"text\u02bbed",u"words"]
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

    def test_Tokens6(self):
        """Word contains a dierisis and leading glottal"""
        line6='\x91Otua Taumai\xe4 \x91al\xe4,'
        #~ line6="""\x91Otua Taumai\xe4 \x91al\xe4"""
        line_expect = [u"\u02bbOtua",u"Taumai\u0101",u"\u02bbal\u0101"]
        test = to()
        line6=test.c_transpose(line6.decode('cp1252'))
        Tokens = test.w_Tokens(line6)
        assert Tokens[0] == line_expect[0]
        assert Tokens[1] == line_expect[1]
        assert Tokens[2] == line_expect[2]
    def test_Tokens7(self):
        """Word contains a dierisis and leading glottal"""
        line7="Breakdance \x91Otua Taumai\xe4 \x91al\xe4,"
        line_expect = [u"Breakdance", u"\u02bbOtua",u"Taumai\u0101",u"\u02bbal\u0101"]
        test = to()
        line7=test.c_transpose(line7.decode('cp1252'))
        Tokens = test.w_Tokens(line7)
        assert Tokens[0] == line_expect[0]
        assert Tokens[1] == line_expect[1]
        assert Tokens[2] == line_expect[2]
        assert Tokens[3] == line_expect[3]
    def test_Tokens8(self):
        """Words contain intermingled msword smart single quotes ` and ' 
        They all become glottals in Tongan Language"""
        line8="\x91Iteita tamasi\x92i \x91i mu\x92a fa\x92iteliha;"
        line_expect = [u"\u02bbIteita", u"tamasi\u02bbi", u"\u02bbi", u"mu\u02bba", u"fa\u02bbiteliha"]
        test = to()
        line8=test.c_transpose(line8.decode('cp1252'))
        Tokens = test.w_Tokens(line8)
        assert Tokens[0] == line_expect[0]
        assert Tokens[1] == line_expect[1]
        assert Tokens[2] == line_expect[2]
        assert Tokens[3] == line_expect[3]
    def test_transform1(self):
        test = to()
        answer = test.c_transform("o","o",unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'))
        assert answer == unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON')
    def test_ctranspose(self):
        """Words contain intermingled msword smart single quotes ` and ' 
        They all become glottals in Tongan Language"""
        line="""\x91Iteita tamasi\x92i \x91i mu\x92a fa\x92iteliha;"""
        line_expect=u"""\u02bbIteita tamasi\u02bbi \u02bbi mu\u02bba fa\u02bbiteliha;"""
        test = to()
        transpose = test.c_transpose([line.decode('cp1252')])[0]
        assert transpose == line_expect
        
    #~ def test_transform3(self):
        #~ test = to()
        #~ answer = test.c_transform(test.diacritics_all, test.diacritics_all, test.diacritics_to)
        #~ assert answer == test.diacritics_to
        
tests = [
    u_Language(),
    u_En(),
    u_To()
]