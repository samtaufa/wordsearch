import libpry
from lib.wsoptions import WSoptions
from lib.wsmatrix import WSdirections
import sys

class u_WSoptions(libpry.AutoTree):
    def setUpAll(self):
        self.test = WSoptions()
        sys.argv = ['app.py', '-g','21','21', '-d', '1','test_options.py']        
        
    def tearDownAll(self):
        self.test = None

    def test_init(self):
        self.test = WSoptions()
        assert self.test.rows == 20
        assert self.test.cols == 20
    
    def test_read_cmdline(self):      
        self.test.set_options()
        sys.argv = ['app.py', '-g','18','18', '-d', '1','test_options.py']        
        self.test.read_cmdline()
        assert self.test.rows == 18
        assert self.test.cols == 18
        
    def test_get_gridsize(self):
        self.test.set_options()
        sys.argv = ['app.py', '-g','11','11', '-d', '1','test_options.py']        
        self.test.read_cmdline()
        assert self.test.rows == 11
        assert self.test.cols == 11 
        assert self.test.directions == 1
        
    def test_get_cmdline(self):
        directions = WSdirections()
        self.test.set_options()
        self.test.read_cmdline()        
        filename, x, y, dir = self.test.get_cmdline()
        assert filename == 'test_options.py'
        assert x == 21
        assert y == 21
        assert dir == 1

tests = [
    u_WSoptions()
]
