import sys



def solve1(input):
    lines = open(input).read().splitlines()
    commands = lines[0].split(",")
    SUM = 0
    for command in commands:
        h = 0
        for c in command:
            h += ord(c)
            h *= 17
            h %= 256
        # print('command '+command)
        # print('HASH '+str(h))
        SUM += h
    return SUM


print(solve1(sys.argv[1]))

