import libpry
from src.options import Options
from src.wsmatrix import WSdirections
import sys

class u_Options(libpry.AutoTree):
    def setUpAll(self):
        self.test = Options()
        sys.argv = ['app.py', '-g','21','21', '-d', '1','test_options.py']        
        
    def tearDownAll(self):
        self.test = None

    def test_init(self):
        self.test = Options()
        assert self.test.x == 20
        assert self.test.y == 20
    
    def test_read_cmdline_options(self):      
        self.test.set_cmdline_defaults()
        sys.argv = ['app.py', '-g','18','18', '-d', '1','test_options.py']        
        self.test.read_cmdline_options()
        assert self.test.options.grid_size[0] == 18
        assert self.test.options.grid_size[1] == 18
        
    def test_get_gridsize(self):
        self.test.set_cmdline_defaults()
        sys.argv = ['app.py', '-g','11','11', '-d', '1','test_options.py']        
        self.test.read_cmdline_options()
        self.test.get_gridsize()
        assert self.test.options.grid_size[0] == 11
        assert self.test.options.grid_size[1] == 11 
        assert self.test.options.directions == 1
        
    def test_get_cmdline(self):
        directions = WSdirections()
        self.test.set_cmdline_defaults()
        self.test.read_cmdline_options()        
        filename, x, y, dir = self.test.get_cmdline()
        assert filename == 'test_options.py'
        assert x == 21
        assert y == 21
        assert dir == 1

tests = [
    u_Options()
]
