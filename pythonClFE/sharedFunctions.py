from variables import *

def CommandReady():
    screen.move(num_rows - 1, 0)
    screen.clrtoeol()
    screen.addstr(num_rows - 1, 0, ":")

def prepareDrawBox():
    message = ''
    for i in range (drawBox[0][0], drawBox[1][0] + 1):
        if(i < len(tempFile)):
            add = (tempFile[i][drawBox[0][1]:drawBox[1][1]+1])
            if tempFile[i] == '\n':
                add = '\n'
            if (i == drawBox[1][0]):
                message += add.replace("\n", "")
            else:
                message += add
        else:
            break

    return message

def replace(message):
    screen.erase()
    screen.addstr(0, 0, message)

def drawBoxShift(y = 0, x = 0):
    flashTempFile()
    drawBox[0][0] = drawBox[0][0] + y
    drawBox[0][1] = drawBox[0][1] + x
    drawBox[1][0] = drawBox[1][0] + y
    drawBox[1][1] = drawBox[1][1] + x
    replace(prepareDrawBox())

def getLongestLine():
    longest = 0
    for i in tempFile:
        if len(i) > longest:
            longest = len(i)
    return longest

def flashTempFile():
    for i in range(0, len(tempFile)):
        rowID = i + drawBox[0][0]
        if (tempFile[rowID] != '\n'):
            sub1 = tempFile[rowID][0:drawBox[0][1]]
            sub2 = tempFile[rowID][drawBox[1][1]+1:]
            newStingSection = screen.instr(i, 0, num_cols).decode()
            updateRow = sub1 + newStingSection + sub2
            tempFile[rowID] = updateRow
