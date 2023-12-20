import sys
from collections import OrderedDict

def hash(s, acc=0):
    if not s:
        return acc
    c = s[0]
    newAcc = acc
    newAcc += ord(c)
    newAcc *= 17
    newAcc %= 256
    return hash(s[1:], newAcc)

def solve1(input):
    lines = open(input).read().splitlines()
    commands = lines[0].split(",")
    SUM = 0
    for command in commands:
        h = hash(command, 0)
        # print('command '+command)
        # print('HASH '+str(h))
        SUM += h
    return SUM

print(solve1(sys.argv[1]))


def solve2(input):
    lines = open(input).read().splitlines()
    commands = lines[0].split(",")
    ALL_BOXES = [OrderedDict() for _ in range(256)]
    for command in commands:
        if command[-1] == '-':
            label = command[:-1]
            boxNr = hash(label)
            if label in ALL_BOXES[boxNr].keys():
                del ALL_BOXES[boxNr][label]
        else:
            label, focalValue = command.split("=")
            boxNr = hash(label)
            ALL_BOXES[boxNr][label] = int(focalValue)

    SUM = 0
    for boxNr, box in enumerate(ALL_BOXES):
        i = 1
        for k, v in box.items():
            SUM += (boxNr+1)*i*v
            i += 1

    # print (ALL_BOXES)                    
    return SUM

print(solve2(sys.argv[1]))
