import sys

def sameRows(lines, i1, i2):
    for row, _ in enumerate(lines):
        if lines[row][i1] != lines[row][i2]:
            return False
    return True

def processLines(lines):
    for i in range(len(lines)-1):
        rowsUp = i+1
        rowsDown = len(lines)-i-1
        # print((rowsUp, rowsDown))
        allFine = True
        for j in range(min(rowsUp, rowsDown)):
            # print("comparing "+str(i-j)+ " and "+ str(i+j+1))
            # print("comparing "+str(lines[i-j])+ " and "+ str(lines[i+j+1]))
            if lines[i-j] != lines[i+j+1]:
                allFine = False
                # print("not same")
                break
            # print("same")
        if allFine:
            return 100 * (i+1)
    
    lineLength = len(lines[0])
    for i in range(lineLength-1):
        colsLeft = i+1
        colsRight = lineLength-i-1
        allFine = True
        for j in range(min(colsLeft, colsRight)):
            if not sameRows(lines, i-j, i+j+1):
                allFine = False
                break
        if allFine:
            return i+1
    return 1000000

def solve1(input):
    lines = open(input).read().splitlines()
    currentLines = []
    SUM = 0
    for line in lines:
        if line:
            currentLines.append(line)
        else:
            SUM += processLines(currentLines)
            currentLines = []
    SUM += processLines(currentLines)
    return SUM

# print(solve1(sys.argv[1]))


def countDifferences(line1, line2):
    differences = 0
    for i, c in enumerate(line1):
        if line1[i] != line2[i]:
            differences += 1
    return differences

def countDifferencesInRows(lines, i1, i2):
    differences = 0
    for row, _ in enumerate(lines):
        if lines[row][i1] != lines[row][i2]:
            differences += 1
    return differences

def processLines2(lines):
    for i in range(len(lines)-1):
        rowsUp = i+1
        rowsDown = len(lines)-i-1
        # print((rowsUp, rowsDown))
        differences = 0
        for j in range(min(rowsUp, rowsDown)):
            # print("comparing "+str(i-j)+ " and "+ str(i+j+1))
            # print("comparing "+str(lines[i-j])+ " and "+ str(lines[i+j+1]))
            differences += countDifferences(lines[i-j], lines[i+j+1])
            if differences > 1:
                # print("not same")
                break
            # print("same")
        if differences == 1:
            return 100 * (i+1)
    
    lineLength = len(lines[0])
    for i in range(lineLength-1):
        colsLeft = i+1
        colsRight = lineLength-i-1
        differences = 0
        for j in range(min(colsLeft, colsRight)):
            differences += countDifferencesInRows(lines, i-j, i+j+1)
            if differences > 1:
                break
        if differences == 1:
            return i+1
    return 1000000

def solve2(input):
    lines = open(input).read().splitlines()
    currentLines = []
    SUM = 0
    for line in lines:
        if line:
            currentLines.append(line)
        else:
            SUM += processLines2(currentLines)
            currentLines = []
    SUM += processLines2(currentLines)
    return SUM

print(solve2(sys.argv[1]))
