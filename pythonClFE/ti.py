import curses
 
# get the curses screen window
screen = curses.initscr()
 
# turn off input echoing
curses.noecho()
 
# respond to keys immediately (don't wait for enter)
curses.cbreak()
 
# map arrow keys to special values
screen.keypad(True)
 
try:
    while True:
        char = screen.getch()
        print(char)
        if char == ord('q'):
            break
        else:
            screen.move(0, 0)
            screen.clrtoeol()
            screen.addch(0, 0, char)
            print(char)
finally:
    # shut down cleanly
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()