import curses
from sharedFunctions import *
from variables import *

def saveFile():
    for i in range(0, num_rows):
        print(screen.instr(i, 0, num_cols).decode())

    CommandReady(screen, num_rows)
