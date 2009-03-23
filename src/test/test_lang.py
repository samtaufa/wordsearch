import sys, string, unicodedata
import libpry
from src.lang.lang import Language, to
class u_Language(libpry.AutoTree):
    def setUp(self):
        pass
    def test_Tokens1(self):    
        line1 = "This is a line of text'ed words"
        line_expect = ["This","is","a","line","of",u"text'ed", "words"]
        test1 = Language()
        Tokens = test1.w_Tokens(line1)
        assert Tokens == line_expect

    def test_Tokens3(self):    
        line3 = "This is a line of 'text'ed' words"
        line_expect = ["This","is","a","line","of",u"text'ed","words"]
        test3 = Language()
        Tokens = test3.w_Tokens(line3)
        assert Tokens == line_expect
        
    def test_Tokens4(self):    
        line4 = "This is a line of 'text'ed' words"
        line_expect = ["This","is","a","line","of",u"text'ed","words"]
        test4 = Language()
        Tokens = test4.w_Tokens(line4)
        assert Tokens == line_expect
        
    def test_Tokens5(self):    
        line5 = "This 'is 'a 'line of text'ed' words"
        line_expect = ["This","is","a","line","of",u"text'ed","words"]
        test5 = Language()
        Tokens = test5.w_Tokens(line5)
        assert Tokens == line_expect
        
class u_To(libpry.AutoTree):
    def setUpAll(self):
        pass

    def setUp(self):
        pass
        
    def tearDown(self):
        pass

    def test_Tokens1(self):    
        line1 = "This is a line of text'ed words"
        line_expect = ["This","is","a","line","of",u"text\u02bbed","words"]
        test1 = to()
        Tokens = test1.w_Tokens(line1)
        assert Tokens == line_expect

    def test_Tokens2(self):    
        line2 = "This$ is# a 6 line43 of text'ed words"
        line_expect = ["This","is","a","line","of",u"text\u02bbed","words"]
        test2 = to()
        Tokens = test2.w_Tokens(line2)
        assert Tokens == line_expect


    def test_Tokens3_To(self):    
        line3 = "This is a line of 'text'ed' words"
        line_expect = ["This","is","a","line","of",u"text\u02bbed","words"]
        test3 = to()
        Tokens = test3.w_Tokens(line3)
        assert Tokens == line_expect        
        
    def test_Tokens4(self):    
        line4 = "This is a line of 'text'ed' words"
        line_expect = ["This","is","a","line","of",u"text\u02bbed","words"]
        test4 = to()
        Tokens = test4.w_Tokens(line4)
        assert Tokens == line_expect
    
    def test_Tokens5_To(self):
        line5 = "This 'is 'a 'line of text'ed' words"
        line_expect = ["This",u"\u02bbis",u"\u02bba","line","of",u"text\u02bbed","words"]
        test5 = to()
        Tokens = test5.w_Tokens(line5)
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