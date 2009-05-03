#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Test classes for lib.wsmatrix and lib.wsstreamio

    :copyright: (c) 2009, Samiuela Loni Vea Taufa
    :license: MIT, see LICENSE.txt for more details
"""

import libpry
from lib.wsmatrix import WSmatrix, WSdirections, WStext, WSformats
from lib.wsstreamio import WSstreamIO
import sys

class u_WSmatrix(libpry.AutoTree):
    def setUpAll(self):
        self.words = ['this','is','my','matrix','test','collection','not','very','large','but','hoping']
        
    def test_init(self):
        directions = WSdirections()
        test = WSmatrix((11,11),directions.Right | directions.Left,self.words)
        assert test.maxrow == 11
        assert test.maxcol == 11
        assert test.directions == [directions.Right, directions.Left]
        assert test.wordlist == self.words
        
        
    def test_size(self):
        test = WSmatrix((15,15))
        assert test.maxrow == 15
        assert test.maxcol == 15
    
    def test_directions(self):
        test = WSmatrix()
        directions = WSdirections()
        assert test.directions == [directions.Right]
        
        test.set_directions(directions.Right | directions.Left)
        assert test.directions == [directions.Right, directions.Left]

        test.set_directions(directions.Right | directions.Left | directions.Up | directions.Down)
        assert test.directions == [directions.Right, directions.Left, directions.Up, directions.Down]

    def test_cell_init(self):
        test = WSmatrix()
        maxx=30
        maxy=25
        matrix, available, minleftover = test.init_cells(maxx,maxy)
        assert len(matrix) == maxx
        assert len(matrix[0]) == maxy
        assert available == (maxx * maxy)
        assert minleftover == int(0.01 * available)
        
    #~ def test_display(self):
        #~ test = WSmatrix()
        #~ print "\ntest_display"
        #~ for i in range(3,10):
            #~ test.maxrow = i
            #~ test.maxcol = i-2 
            #~ print "%s x %s" %( i, i-2)
            #~ print"- "* (i-2)
            #~ test.display()
            #~ print"- "* (i-2)
        
    def test_startGrid(self):
        directions = WSdirections()
        test = WSmatrix((10,10),directions.Right | directions.Left,self.words)
        matrix = test.startGrid(directions.Right, 10)
        assert len(matrix) == 10
        matrix = test.startGrid(directions.Down, 10)
        assert len(matrix) == 10
        matrix = test.startGrid(directions.Right,9)
        assert len(matrix) == 20
        matrix = test.startGrid(directions.DiagDwnRight,10)
        assert len(matrix) == 1
    def test_insertWord(self):
        test = WSmatrix()
    def test_canInsertWord(self):
        words =['this','one','will','do']
        directions = WSdirections()
        test = WSmatrix((11,11),directions.Right | directions.Left,words)
        for word in words:
            answer = test.canInsertWord(word, (0,0), directions.Right, test.matrix)
            assert answer == True
        assert test.canInsertWord('this is a very long word not to fit in grid', (0,0), directions.Right, test.matrix) == False

    def test_insertWord(self):
        words =['this','one','will','do','nicely', 'fine', 'thankyou','seriouslybroken']
        directions = WSdirections()
        test = WSmatrix((5,9),directions.Right | directions.Left,words)
        matrix = test.matrix
        assert test.canInsertWord(words[0], (0,0), directions.Right,matrix) == True
        
        test.debug = False
        assert test.canInsertWord(words[1:][0], (0,0), directions.Right,matrix) == True
        assert test.canInsertWord(words[1:][0], (1,0), directions.Right,matrix) == True
        assert test.canInsertWord(words[2], (2,0), directions.Right,matrix) == True
        assert test.canInsertWord(words[3], (3,0), directions.Right,matrix) == True
        assert test.canInsertWord(words[4], (4,0), directions.Right,matrix) == True

        #~ print 
        #~ print "InsertWord"
        #~ x = len(matrix)
        #~ for i in range(x):
            #~ print matrix[i]
                
        #~ print
        
    def test_populate(self):
        words =['where','is','world','taking','us','spontaneously','this','one','will','do', 'just', 'fine', 'thankyou']
        directions = WSdirections()
        test = WSmatrix((11,11),directions.Right | directions.Left,words)
        matrix, accepted, rejected = test.populate()
        assert rejected == ['spontaneously', 'is', 'us']
        #~ print
        #~ test.display(matrix)
        #~ print accepted
        #~ print rejected
        #~ print
    
    def test_populate_matrix(self):
        words =['bitspaceX', 'this','one','will','do', 'just', 'fine', 'thankyou']
        directions = WSdirections()
        test = WSmatrix((10,10),directions.DiagDwnRight | directions.Right,words)
        success, matrix, accepted, rejected = test.populate_matrix(test.matrix, words)
        assert rejected == []
        #~ print
        #~ test.display(matrix)
        #~ print
        #~ print "words   : ", words
        #~ print "accepted: ", test.wordsplaced
        #~ print "rejected: ", rejected, test.wordsrejected
        
    def test_populate_matrix1(self):
        words =['bitspace','extras']
        directions = WSdirections()
        test = WSmatrix((7,9),directions.DiagDwnLeft,words)
        success, matrix, accepted, rejected = test.populate_matrix(test.matrix, words)
        assert rejected == []
        #~ print
        #~ test.display(matrix)
        #~ print "words   : ", words
        #~ print "accepted: ", accepted, test.wordsplaced
        #~ print "rejected: ", rejected, test.wordsrejected
        
    def test_longlist(self):
        words =['bitspace','extras','officious', 'as','it','may','seem','to','some','considering',
        'the','significance','wonderous','proposals','obstinate','peter','paul','mary','children','christmas',
        'trees','foundations','thrillseeking','frivolous']
        directions = WSdirections()
        test = WSmatrix((7,9),directions.Right|directions.Left|directions.Up|directions.Down,words)
        success, matrix, accepted, rejected = test.populate_matrix(test.matrix, words)
        #~ #assert rejected == []
        #~ print
        #~ test.display(matrix)
        
    def test_cellNext(self):
        pass
        
        
class u_WSdirections(libpry.AutoTree):
    def setUpAll(self):
        pass
    def test_set_directions(self):
        test = WSdirections()
        test.set_directions(5)
        assert test.Chosen == [1, 4]
        test.set_directions(127)
        assert test.Chosen == [1, 2, 4, 8, 16, 32, 64]
        test.set_directions(255)
        assert test.Chosen == [ 1, 2, 4, 8, 16, 32, 64, 128]
        
    def test_pop(self):
        test = WSdirections()
        test.set_directions(255)
        assert len(test.Chosen) == 8
        local_dir = []
        for i in range(0, len(test.Chosen)):
            local_dir.append(test.pop())
        assert len(test.Chosen) == 0
        for i in range(0, 100):
            test.set_directions(255)
            local_dir = []
            for i in range(0, len(test.Chosen)):
                local_dir.append(test.pop())
            test.set_directions(255)
            assert test.Chosen != local_dir
    def test_push(self):
        test = WSdirections()
        local_dir = []
        test.append(1)
        assert test.Chosen == [1]
        test.append(2)
        assert test.Chosen == [1, 2]
        test.append(4)
        assert test.Chosen == [1, 2, 4]
        test.append(128)
        assert test.Chosen == [1, 2, 4, 128]

class u_WStext(libpry.AutoTree):
    def setUpAll(self):
        self.Twords = ["sam","is","not","in","the","house"]

    def setUp(self):
        pass
        
    def tearDown(self):
        self.test = None

    def test_sanitize_length(self):
        wordlist = ["short", "notshorter", "longing", "verylongword"]
        expect   = ["notshorter", "longing" ]
        expectreject= ["verylongword", "short"]
        test = WStext(wordlist, 11)
        assert test.wordlist == expect
        assert test.wordlist_rejected == expectreject
        
    def test_sanitize_content(self):
        wordlist =["short", "not6shorter", "longing","verylongword"]
        expect =  ["longing", "short", "not"]
        test = WStext(wordlist, 11)
        assert test.wordlist == expect
        assert test.wordlist_rejected == ["verylongword"]
    
    def test_sanitize_words(self):
        wordlist = ["word", "is", "his", "short"]
        expect = ["short", "word", "his"]
        reject = []
        test = WStext(wordlist, 11)
        good, bad = test.sanitize_words(wordlist, 11)
        assert good == expect
        assert bad == ["is"]
    def test_sanitize_nosubwords(self):
        wordlist = ["short", "word", "is", "his"]
        expect = ["short", "word", "his"]
        reject = []
        test = WStext(wordlist, 11)
        good, bad = test.sanitize_nosubwords(wordlist, reject)
        assert good == expect
        assert bad == ["is"]
        wordlist = ["short", "notshorter", "longing", "long", "verylongword"]
        expect = ["notshorter", "longing", "verylongword"]
        reject = []
        test = WStext(wordlist)
        good, bad = test.sanitize_nosubwords(wordlist, reject)
        assert good == expect
        assert bad == ["short", "long"]
        
    def test_sanitize_sortbysize(self):
        wordlist = ["word", "is", "his", "short"]
        expect = ["short", "word", "his", "is"]
        test = WStext(wordlist, 11)
        answer = test.sanitize_sortbysize(wordlist)
        assert answer == expect
        wordlist = ["longing", "notshorter"]
        expect = ["notshorter","longing"]
        test = WStext(wordlist, 11)
        answer = test.sanitize_sortbysize(wordlist)
        assert answer == expect
        
class u_WSformats(libpry.AutoTree):
    def setUpAll(self):
        words =['bitspaceX', 'this','one','will','do', 'just', 'fine', 'thankyou']
        directions = WSdirections()
        test = WSmatrix((5,9),directions.DiagDwnRight,words)
        success, matrix, accepted, rejected = test.populate_matrix(test.matrix, words)
        self.format = WSformats()
        self.format.matrix = matrix
        self.format.accepted = accepted
        self.format.rejected = rejected
        self.format.solution = test.wordsplaced
        
    def tearDownAll(self):
        pass
    def test_html(self):
        self.format.html()
        #~ print self.format.acceptedFormatted
        #~ print self.format.matrixFormatted
        #~ print self.format.solutionFormatted
    def test_unicode(self):
        self.format.unicode()
        #~ print self.format.acceptedFormatted
        #~ print self.format.matrixFormatted
        #~ print self.format.solutionFormatted
    def test_xml(self):
        pass
    def test_getLetter(self):
        self.format.fillLetterBin()
        #~ for i in range(0,10):
            #~ print self.format.getLetter()," ",
        #~ print
class u_WSlang(libpry.AutoTree):
    def setUpAll(self):
        self.wsstreamio = WSstreamIO()
        self.wstext = WStext()
        self.wstext.setLanguage('to')
        fh = self.wsstreamio.open('unicode.txt')
        self.wsstreamio.load(fh)
        self.lines = self.wsstreamio.lines
        self.originalEncoding = self.wsstreamio.originalEncoding        
        
    def test_loadfile(self):
        self.wstext.setWordlist(self.lines)
        lineswordcount = 0
        for line in self.lines:
            for word in line:
                lineswordcount += 1
        assert lineswordcount > len(self.wstext.wordlist)
        #~ for i in range(len(self.wstext.wordlist)):
            #~ print "[%s]" % str(self.wstext.wordlist[i]),
tests = [
    u_WSmatrix(),
    u_WSdirections(),
    u_WStext(),
    u_WSformats(),
    u_WSlang()
]
