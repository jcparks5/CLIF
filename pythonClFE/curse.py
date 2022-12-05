# Draw text to center of screen
import curses
import sys
from insert import *
from save import *
from sharedFunctions import *
from variables import *

# Make a function to print a line in the center of screen
def Start():
    
    n = sys.argv[1]
    f = open(n, "r")

    while True:
        line = f.readline()
        if not line:
            break
        tempFile.append(line)    
    
    message = prepareDrawBox()

    # Draw the text
    screen.addstr(0, 0, message)

    # enter Command mode
    CommandReady()

    # loop until we are going to quit
    while True:

        # take input and reset screen
        mystr = screen.getstr().decode()
        CommandReady()

        # check command
        if(mystr == 'insert'):
            insertMode()
        elif(mystr == 'save'):
            saveFile()
        elif(mystr == 's and q'):
            saveFile()
            break
        elif(mystr == 'quit'):
            break
    curses.nocbreak(); screen.keypad(0)
    curses.endwin()

if (__name__ == "__main__"):
    Start();