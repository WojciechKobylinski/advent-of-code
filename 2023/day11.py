import sys, itertools

def solve1(input):
    lines = open(input).read().splitlines()
    DIM_X = len(lines[0])
    DIM_Y = len(lines)
    ANY_X = [False for _ in range(DIM_X)]
    ANY_Y = [False for _ in range(DIM_Y)]
    
    points = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                ANY_X[x] = True
                ANY_Y[y] = True
                points.append((x,y))
    sumEmptyXs =  list(itertools.accumulate([0 if x else 1 for x in ANY_X]))
    sumEmptyYs =  list(itertools.accumulate([0 if y else 1 for y in ANY_Y]))

    SUM = 0
    for i, p1 in enumerate(points):
        x1, y1 = p1
        for p2 in points[i+1:]:
            x2, y2 = p2
            addX = abs(sumEmptyXs[x1]-sumEmptyXs[x2])
            addY = abs(sumEmptyYs[y1]-sumEmptyYs[y2])
            distance = abs(x1-x2)+abs(y1-y2)+addX+addY
            SUM += distance
    return SUM

print(solve1(sys.argv[1]))

def solve2(input):
    lines = open(input).read().splitlines()
    DIM_X = len(lines[0])
    DIM_Y = len(lines)
    ANY_X = [False for _ in range(DIM_X)]
    ANY_Y = [False for _ in range(DIM_Y)]
    
    points = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '#':
                ANY_X[x] = True
                ANY_Y[y] = True
                points.append((x,y))
    sumEmptyXs =  list(itertools.accumulate([0 if x else 1 for x in ANY_X]))
    sumEmptyYs =  list(itertools.accumulate([0 if y else 1 for y in ANY_Y]))

    SUM = 0
    for i, p1 in enumerate(points):
        x1, y1 = p1
        for p2 in points[i+1:]:
            x2, y2 = p2
            addX = abs(sumEmptyXs[x1]-sumEmptyXs[x2])
            addY = abs(sumEmptyYs[y1]-sumEmptyYs[y2])
            distance = abs(x1-x2)+abs(y1-y2)+(addX+addY)*(1_000_000-1)
            SUM += distance
    return SUM

print(solve2(sys.argv[1]))
