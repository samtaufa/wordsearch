import sys, string, unicodedata
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
    def test_Tokens6(self):
        """Word Tokenize a string"""
        line1 = "This is a line of text.ed wor.ds"
        line_expect = ["This","is","a","line","of","text","ed", "wor","ds"]
        test1 = Language()
        Tokens = test1.w_Tokens(line1)
        assert Tokens == line_expect
        
class u_To(libpry.AutoTree):
    def test_Tokens1(self):    
        """Word Tokenize a string"""
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
        """Word Tokenize a string with apostrophne pre-pending words
        beginning with a vowel"""
        line5 = "This 'is 'a 'line of text'ed' words"
        line_expect = ["This",u"\u02bbis",u"\u02bba","line","of",u"text\u02bbed","words"]
        test5 = to()
        Tokens = test5.w_Tokens(line5)
        assert Tokens == line_expect
    def test_Tokens6(self):
        """Word Tokenize a string"""
        line1 = "break.this.up"
        line_expect = ["break","this","up"]
        test1 = to()
        Tokens = test1.w_Tokens(line1)
        assert Tokens == line_expect

    def test_transform1(self):
        test = to()
        answer = test.c_transform("o","o",unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON'))
        assert answer == unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON')
    #~ def test_transform2(self):
        #~ test = to()
        #~ answer = test.transform(test.transformFrom)
        #~ assert answer == test.transformTo
    def test_transform3(self):
        test = to()
        answer = test.c_transform(test.diacritics_all, test.diacritics_all, test.diacritics_to)
        assert answer == test.diacritics_to
        
    #~ def test_inituVowels(self):
        #~ test = to()

        
tests = [
    u_Language(),
    u_To()
]