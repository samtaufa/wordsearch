README

Unicode Support:    "ÁÂÃÄÉÊËÍÎÏÓÔÕÖÚÛÜáâãäéêëíîïóôõöúûüĀāĒēĨĩĪīŌōŨũŪūẼẽ"

1. What is this
2. What use is it
3. Quick Start: How do I use it
4. What are the requirements
5. What are the features
6. Why bother ?
   . Self Education / Fun
   . Unicode
7. I don't like this

1. What is this

        $ ./src/wordsearch.py ./docs/examples/wordlist.1.txt --gridsize 8 15
        
        Find words hidden: Left to Right
        
                u p h e r e a l l o o k t o h
                t a n d o h a v e f o r c a r
                b o y n d a d o g e t y o u a
                r g i r l i n o i s l i k e m
                w i l l m o t h e r s s e e o
                e w c a n h a d b i g g o o d
                r a t w e n t c o m e a m a o
                i g o t b h o m e i t s a i d

        all, am, and, at, big, boy, can, car, come, dad, do, for, get, girl, good, got,
        had, have, here, home, in, is, it, like, look, mother, no, said, see, to, up, we
        nt, will, you
        34 words (16 of 120 cells spot filled [13%])

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
       
5. What are the features

    Other than the standard fare for wordsearch puzzle generators,
    an interesting functional feature of this rendition is 
    
    --article
    
    when combined with html output.
    
    If you generate a puzzle from paragraphs of text, then using
    --article and --format html will display the original text
    paragraph, with the hidden words 'highlighted'
    
    
    $ ./src/wordsearch.py ./docs/examples/paragraphs.1.txt --gridsize 8 15 --article --format html

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=        UTF-8" />
        <title>Wordsearch Puzzle Generation</title>
    </head>
    <body>
        <p class='title'>Title: Word Search Puzzle</p>
        <p class='subtitle'>Sub-Title</p>
        <p class='directions'>Find words hidden: Left to Right</p>
        <div class='ws-puzzle'>
            <p class='ws-puzzle'>p e n p r i n t a b l e a c h </p>
            <p class='ws-puzzle'>a v e r t i c a l l y g r i d </p>
            <p class='ws-puzzle'>r i g h t g e n e r a t e s r </p>
            <p class='ws-puzzle'>o f i n d i r e c t i o n o t </p>
            <p class='ws-puzzle'>p y c o n t a i n i n g a r e </p>
            <p class='ws-puzzle'>d w o r d s e a r c h t a s k </p>
            <p class='ws-puzzle'>d i a g o n a l l y p a p e r </p>
            <p class='ws-puzzle'>i h o r i z o n t a l l y b e </p>

        </div>
        <div class='ws-wordlist'>
            <p class='ws-wordlist'>
             are, be, containing, diagonally, direction, each, find, generates, grid, horizo
            ntally, not, of, paper, pen, printable, py, right, task, vertically, wordsearch
            </p>
        </div>
        <div class='ws-article'>
            <p class='ws-article'><span class='highlight'>´╗┐wordsearch.py</span> <span clas
            s='highlight'>generates</span> 'wordsearch' or 'word <span class='highlight'>fin
            d'</span> <span class='highlight'>printable</span> <span class='highlight'>paper
            </span> puzzles, <br />
            <p class='ws-article'><span class='highlight'>containing</span> words in a <span
             class='highlight'>grid.</span> <br />
            <p class='ws-article'><br />
            <p class='ws-article'>Word search puzzles <span class='highlight'>are</span> <sp
            an class='highlight'>pen</span> and paper puzzles containing a grid <span class=
            'highlight'>of</span> letters. <br />
            <p class='ws-article'>The player's <span class='highlight'>task</span> is to loc
            ate words hidden within this grid. <span class='highlight'>Each</span> word is <
            br />
            <p class='ws-article'>in a straight line, but can <span class='highlight'>be</sp
            an> placed in any <span class='highlight'>direction,</span> <span class='highlig
            ht'>horizontally</span> (left to <br />
            <p class='ws-article'><span class='highlight'>right,</span> or right to left), <
            span class='highlight'>vertically</span> (upwards or downwards), or <span class=
            'highlight'>diagonally.</span> <br />
            <p class='ws-article'>Just to make the puzzle that little bit more difficult, wo
            rds may overlap or <br />
            <p class='ws-article'>intersect, and of course <span class='highlight'>not</span
            > every letter in the grid is actually part of a <br />
            <p class='ws-article'>word. <br />
        </div>
        <p class='ws-stats'>20 words (4 of 120 cells spot filled [3%])</p>
    </body>
</html>

    
6. Why bother ?

  - Self Education / Fun

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
   
   During a school vacation break, I wrote a Turbo C++ version of 
   the puzzle generator to review software algorithm techniques
   such as backtracking, C++ and bitwise mathematics(?)
   
   Once again, Windows 95 transitioned onwards and I lost the
   subsequent .exe's and at some point no longer had a functional
   
   Sometime passed and I had a functioning Python version of the
   program, but when I looked at it again, it didn't run on
   the 'current' version of Python for some reason. (Now that the
   re-write is complete, I discover the original Python version
   of the code actually works)
   
   Recently? I was re-educating myself on programming techniques
   and pointers, backtracking etc. came back like an unwanted
   itch. At the same time I was presented with the problem of
   trying to collect Tongan Language text (with the challenge of
   maintaining/correcting syntactic errors.)
   
   Woo hoo, let's do this in a new 'framework' language ('cause
   it would be waay to simple to use something you were already
   confident and familiar with.)
   
   Justify things by saying that we'll add a few more interesting
   challenges to redefine our problem and the wordsearch programming
   challenge came to light.

  - Unicode
  
  Text: "ÁÂÃÄÉÊËÍÎÏÓÔÕÖÚÛÜáâãäéêëíîïóôõöúûüĀāĒēĨĩĪīŌōŨũŪūẼẽ"
  
  If your text editor can display the full text above (within quotes)
  without having substituted a "?" mark or square block instead of the
  letter/character, then you might like this tool.
  
7. I don't like this

IF you're still interested in wordsearch puzzles, but hate my code,
you might find more traction in other projects, possibly:

  http://puzzlemaker.discoveryeducation.com/WordSearchSetupForm.asp
  http://puzzlemaker.discoveryeducation.com/WordSearchWithMessageSetupForm.asp
  http://sourceforge.net/projects/findthatword/
  http://wordsearchcreator.org/

Other educational (?) puzzles, or puzzles that ...

http://puzzlemaker.discoveryeducation.com/AdvMazeSetupForm.asp