import curses
from sharedFunctions import *
from variables import *
import keyboard

def insertMode():
    currentY = 0
    currentX = 0
    screen.move(num_rows - 1, 0)
    screen.clrtoeol()
    screen.move(currentY, currentX)
    curses.noecho()
    screen.keypad(True)
    drawBoxShift()
    
    while True:

        #Update the cursor to its new location
        screen.move(currentY, currentX)

        #Get new character
        mychar = screen.getch()

        #Check command
        #Fuck me
        if(mychar == 0x00):
            if keyboard.is_pressed(']+shift'):
                screen.insstr('}')
            elif keyboard.is_pressed(']'):
                screen.insstr(']')
            if(currentX < num_cols - 1):
                currentX += 1
            else:
                drawBoxShift(0,1)

        #Up key
        elif(mychar == curses.KEY_UP):
            if(currentY > 0):
                currentY -= 1
            elif(drawBox[0][0] != 0):
                drawBoxShift(-1, 0)

        #Down key
        elif(mychar == curses.KEY_DOWN):
            if(currentY < num_rows - 1):
                currentY += 1
            elif(drawBox[1][0] < len(tempFile) - 1):
                drawBoxShift(1, 0)

        #Left key
        elif(mychar == curses.KEY_LEFT):
            if(currentX > 0):
                currentX -= 1
            elif(drawBox[0][1] != 0):
                drawBoxShift(0, -1)

        #Right key
        elif(mychar == curses.KEY_RIGHT):
            if(currentX < num_cols - 1):
                currentX += 1
            elif(drawBox[1][1] != getLongestLine()-1):
                drawBoxShift(0, 1)
        
        #Enter character
        elif(mychar == 0x0A):
            if (currentY < num_rows - 1):
                keep = screen.instr(currentY, 0, currentX).decode()
                move = screen.instr(currentY, currentX).decode()

                currentY += 1
                currentX = 0
                screen.insertln()
                screen.clrtoeol()
                screen.addstr(currentY - 1, 0, keep)
                screen.addstr(currentY, 0, move)
        
        #Backspace character
        elif(mychar == 0x08):
            if (currentX > 0):
                currentX -= 1
                screen.delch(currentY,currentX)
            else:
                screen.instr(currentY, 0).decode()

        #Delete character
        elif(mychar == 0x14A):
            screen.delch(currentY,currentX)

        # Ctrl Q to quit
        elif(mychar == 0x11):
            curses.echo()
            CommandReady()
            return()     
        
        else:
            screen.insstr(chr(mychar))
            if(currentX < num_cols - 1):
                currentX += 1
            else:
                drawBoxShift(0,1)