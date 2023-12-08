import sys, re

def solve1(input):
    lines = open(input).read().splitlines()
    directions = list(lines[0])
    L, R = {}, {}

    for line in lines[2:]:
        point, left, right = re.compile(r'(\w+) = \((\w+), (\w+)\)').search(line).groups()
        L[point] = left
        R[point] = right
    STEPS = 0
    where = 'AAA'

    while where != 'ZZZ':
        STEPS += 1
        if directions[0] == 'L':
            where = L[where]
        else:
            where = R[where]
        directions.append(directions[0])
        directions = directions[1:]
    return STEPS

# print(solve1(sys.argv[1]))

def solve2(input):
    lines = open(input).read().splitlines()
    directions = list(lines[0])
    L, R = {}, {}

    WHERE = []
    for line in lines[2:]:
        point, left, right = re.compile(r'(\w+) = \((\w+), (\w+)\)').search(line).groups()
        L[point] = left
        R[point] = right
        if point[2] == 'A':
            WHERE.append(point)
    STEPS = 0

    # moze policzyc cykle tego i zobaczyc jak sie ktory cykl zachowuje. pomnożyć i voila

    while any(point[2] != 'Z' for point in WHERE):
        STEPS += 1
        if directions[0] == 'L':
            WHERE = [L[point] for point in WHERE] 
        else:
            WHERE = [R[point] for point in WHERE] 
        directions.append(directions[0])
        directions = directions[1:]
    return STEPS

print(solve2(sys.argv[1]))