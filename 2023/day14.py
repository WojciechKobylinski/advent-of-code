import sys



def solve1(input):
    lines = open(input).read().splitlines()
    SUM = 0
    columnCount = len(lines[0])
    rowCount = len(lines)
    for column in range(columnCount):
        value = rowCount
        for line in range(rowCount):
            if lines[line][column] == 'O':
                SUM += value
                value -= 1
            elif lines[line][column] == '#':
                value = rowCount-line-1
    return SUM


print(solve1(sys.argv[1]))

