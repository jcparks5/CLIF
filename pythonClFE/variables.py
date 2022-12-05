import curses

screen = curses.initscr()
num_rows, num_cols = screen.getmaxyx()
drawBox = [[0,0],[num_rows - 1, num_cols - 1]]
tempFile = []