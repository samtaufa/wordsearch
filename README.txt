README

1. What is this
2. What use is it
3. Quick Start: How do I use it
4. What are the requirements
5. What are the features
6. Why bother ?

1. What is this

wordsearch.py generates 'wordsearch' or 'word find' printable paper puzzles,
containing words in a grid.

Word search puzzles are pen and paper puzzles containing a grid of letters. 
The player's task is to locate words hidden within this grid. Each word is 
in a straight line, but can be placed in any direction, horizontally (left to 
right, or right to left), vertically (upwards or downwards), or diagonally. 
Just to make the puzzle that little bit more difficult, words may overlap or
intersect, and of course not every letter in the grid is actually part of a
word. 
[ref: http://ezinearticles.com/?Printable-Word-Search-Puzzles-for-Kids&id=1133957]

2. What use is it.

I use it to generate word puzzles that my family
and friends play on their 'offline-time' and to
help reaffirm sight word skills for the children.

3. How do I use it.

  a) wordsearch.py runs from the command-line, and provides
  a list of options.
  
     Type: wordsearch.py to see a list of command-line options.
     
   b) create a text file (e.g. wordlist.txt) to contain a list
   of words you want to use in a wordsearch puzzle.
   
   c) Run the wordsearch.py program with your text file as a
   comand-line option.
   
   e.g. wordsearch.py wordlist.txt
   
   There are sample wordlists in the ./docs/examples directory.
   
   ./src/wordsearch.py ./docs/examples/wordlist.1.txt --grid 5 5
   
        a w i l l
        s a i d o
        g o o d d
        l c o m e
        a t b i g

        at, big, come, do, good, said, will
        7 words (3 of 25 cells spot filled [12%])

4. What are the running requirements.

   General Use:
      (aka. this is what I've got)
       * Python 2.6.1 http://www.python.org
       * BeautifulSoup 
       
    Coding:
       * pry http://dev.nullcube.com for unit testing
       
5. Why bother ?

   I find that family and friends enjoy the distraction offered
   by a wordsearch puzzle, and wanted the ability to create 
   customised puzzles using words in the context of what we
   are doing, pursuing (e.g. have names of our local 'club'
   members etc.)
   
   I bought a shareware application for Windows 3.x at some time
   in the past, which supported grids of various shapes, but
   eventually the program no longer ran on newer OSs, machines
   and the other shareware apps out there didn't have the
   features I desperately wanted (support for accented characters.)
   
   During a school vacation break, I wrote a Turbo C version of 
   the puzzle generator to review software algorithm techniques
   such as backtracking, C++ and bitwise mathematics(?)
   
   Once again, Windows 95 transitioned onwards and I lost the
   subsequent .exe's and at some point no longer had a functional
   
   Recently? I was re-educating myself on programming techniques
   and pointers, backtracking etc. came back like an unwanted
   itch. But, I wanted to use this problem to learn a new
   language, so this version of the program is written in
   poor man's Python.