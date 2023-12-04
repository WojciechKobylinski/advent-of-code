import sys

def solve1(input):
    lines = open(input).read().splitlines()
    SUM = 0
    for line in lines:
        [_, nums] = line.split(": ")
        [winners, choices] = nums.split(" | ")
        winSet = set()
        for winner in winners.split(" "):
            if not winner == "":
                winSet.add(winner)
        count = 0
        for choice in choices.split(" "):
            if choice in winSet:
                count += 1
        if count > 0:
            SUM += 2 ** (count-1)
    return SUM

print(solve1(sys.argv[1]))

def solve2(input):
    lines = open(input).read().splitlines()
    SUM = 0
    multiplier = [1]  * len(lines)
    for nr, line in enumerate(lines):
        currentMultiplier = multiplier[nr]
        SUM += currentMultiplier
        [_, nums] = line.split(": ")
        [winners, choices] = nums.split(" | ")
        winSet = set()
        for winner in winners.split(" "):
            if not winner == "":
                winSet.add(winner)
        count = 0
        for choice in choices.split(" "):
            if choice in winSet:
                count += 1
        for i in range(count):
            if (nr + 1 + i < len(lines)):
                multiplier[nr + 1 + i] += currentMultiplier
    return SUM

print(solve2(sys.argv[1]))