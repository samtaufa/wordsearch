import libpry
from src.wsmatrix import WSmatrix, WSdirections, WSwords
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
        matrix, available, minleftover = test.cells_init(maxx,maxy)
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
        test = WSmatrix()
        
        
    def test_insertWord(self):
        test = WSmatrix()
        
    def test_populate(self):
        test = WSmatrix((0,0))
        directions = WSdirections()
        assert len(test.startGrid(directions.Right,11)) == 0
        
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

class u_WSwords(libpry.AutoTree):
    def setUpAll(self):
        self.Twords = ["sam","is","not","in","the","house"]

    def setUp(self):
        pass
        
    def tearDown(self):
        self.test = None

    def test_sanitize_length(self):
        wordlist = ["short", "notshorter", "longing", "verylongword"]
        expect   = ["short", "notshorter", "longing" ]
        expectlong= ["verylongword"]
        test = WSwords(wordlist, 11)
        assert test.wordlist == expect
        assert test.wordlist_rejected == expectlong
        
    def test_sanitize_content(self):
        wordlist =["short", "not6shorter", "longing","verylongword"]
        expect =  ["short", "not", "longing","verylongword"]
        test = WSwords(wordlist)
        assert test.wordlist == expect
        assert test.wordlist_rejected == []

    
tests = [
    u_WSmatrix(),
    u_WSdirections(),
    u_WSwords()
]
