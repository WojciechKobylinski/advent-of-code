import sys

def prettyPrint2d(array2d):
    print('\n'.join(['\t'.join(str(cell) for cell in row) for row in array2d]))

def getDimensions(lines):
    rows = len(lines)
    cols = len(lines[0])
    return (rows, cols)

def isSymbol(x):
    return not x.isdigit() and not x == "."

def mark(tab, r, c, ROWS, COLS, val):
    rless = max(r-1,0)
    cless = max(c-1,0)
    rmore = min(r+1, ROWS-1)
    cmore = min(c+1, COLS-1)
    tab[rless][cless] = val
    tab[rless][c] = val
    tab[rless][cmore] = val
    tab[r][cless] = val
    tab[r][c] = val
    tab[r][cmore] = val
    tab[rmore][cless] = val
    tab[rmore][c] = val
    tab[rmore][cmore] = val
    

def markSymbols(lines, tab):
    ROWS, COLS = getDimensions(lines)
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if isSymbol(col):
                mark(tab, r, c, ROWS, COLS, True)

def solve1(input):
    lines = open(input).read().splitlines()
    ROWS, COLS = getDimensions(lines)
    adjacent = [[False] * COLS for i in range(ROWS)]
    markSymbols(lines, adjacent)
    #prettyPrint2d(adjacent)
    sum = 0
    for r, row in enumerate(lines):
        currentNumber = 0
        tainted = False
        for c, col in enumerate(row):
            if col.isdigit():
                if currentNumber > 0:
                    currentNumber = currentNumber*10 + int(col)
                    tainted |= adjacent[r][c]
                else:
                    currentNumber = int(col)
                    tainted = adjacent[r][c]
            else:
                if currentNumber > 0 and tainted:
                    sum += currentNumber
                currentNumber = 0
                tainted = False
        if currentNumber > 0 and tainted:
            sum += currentNumber
    return sum

print(solve1(sys.argv[1]))

def collectNumbers(lines):
    ROWS, COLS = getDimensions(lines)
    numbers = [[0] * COLS for i in range(ROWS)]
    values = {}
    whichNr = 1
    for r, row in enumerate(lines):
        currentNumber = 0
        startingIndex = 0
        for c, col in enumerate(row):
            if col.isdigit():
                if currentNumber > 0:
                    currentNumber = currentNumber*10 + int(col)
                else:
                    startingIndex = c
                    currentNumber = int(col)
            else:
                if currentNumber > 0:
                    for i in range (startingIndex, c):
                        numbers[r][i] = whichNr
                    values[whichNr] = currentNumber
                    whichNr += 1
                currentNumber = 0
        if currentNumber > 0:
            for i in range (startingIndex, c):
                numbers[r][i] = whichNr
            values[whichNr] = currentNumber
            whichNr += 1
    return numbers, values

def checkAStar(r, c, ROWS, COLS, numbers, values):
    numbersAround = set()
    rless = max(r-1,0)
    cless = max(c-1,0)
    rmore = min(r+1, ROWS-1)
    cmore = min(c+1, COLS-1)
    numbersAround.add(numbers[rless][cless])
    numbersAround.add(numbers[rless][c])
    numbersAround.add(numbers[rless][cmore])
    numbersAround.add(numbers[r][cless])
    numbersAround.add(numbers[r][c])
    numbersAround.add(numbers[r][cmore])
    numbersAround.add(numbers[rmore][cless])
    numbersAround.add(numbers[rmore][c])
    numbersAround.add(numbers[rmore][cmore])
    numbersAround.remove(0)
    #print("it has "+str(len(numbersAround))+" "+str(numbersAround))
    if len(numbersAround) == 2:
        l = list(numbersAround)
        first = values[l[0]]
        second = values[l[1]]
        #print("A star in "+str(r)+";"+str(c)+" first:"+str(first)+" second:"+str(second))
        return first * second
    return 0
    
def solve2(input):
    lines = open(input).read().splitlines()
    ROWS, COLS = getDimensions(lines)
    numbers, values = collectNumbers(lines)
    #prettyPrint2d(numbers)

    SUM = 0
    for r, row in enumerate(lines):
        for c, col in enumerate(row): 
            if col == '*':
                #print("A star in "+str(r)+";"+str(c))
                SUM += checkAStar(r, c, ROWS, COLS, numbers, values)
    return SUM

print(solve2(sys.argv[1]))