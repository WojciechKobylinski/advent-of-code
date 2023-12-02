import sys

# only 12 red cubes, 13 green cubes, and 14 blue cubes are allowed
MAX_VALS = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

def goodDraw(draw, maxVals):
    for oneColor in draw.split(", "):
        [count, color] = oneColor.strip().split(" ")
        count = int(count)
        if maxVals[color] < count:
            return False
    return True

def idIfGoodGameElseZero(line):
    [gamePart, allDraws] = line.split(": ")
    [_, id] = gamePart.split(" ")
    for aDraw in allDraws.split("; "):
        if not goodDraw(aDraw, MAX_VALS):
            return 0
    return int(id)


def solve1(input):
    lines = open(input).read().splitlines()
    goodIdsOrZeroes = list(map(idIfGoodGameElseZero, lines))
    return sum(goodIdsOrZeroes)

print(solve1(sys.argv[1]))


def cubeValue(line):
    SUM = {"red": 0, "green": 0, "blue": 0}
    [_, allDraws] = line.split(": ")
    for aDraw in allDraws.split("; "):
        for oneColor in aDraw.split(", "):
            [count, color] = oneColor.strip().split(" ")
            count = int(count)
            if SUM[color] < count:
                SUM[color] = count
    return SUM["red"] * SUM["green"] * SUM["blue"]

def solve2(input):
    lines = open(input).read().splitlines()
    goodIdsOrZeroes = list(map(cubeValue, lines))
    return sum(goodIdsOrZeroes)

print(solve2(sys.argv[1]))