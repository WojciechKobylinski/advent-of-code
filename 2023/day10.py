import sys

def edgeCandidate(fromPoint, toPoint, maybeEdges, edges):
    newEdge = (fromPoint, toPoint)
    if newEdge in maybeEdges:
        maybeEdges.remove(newEdge)
        edges.add(newEdge)
    else:
        maybeEdges.add(newEdge)

def prepareEdgesAndStart(lines):
    maybeEdges = set()
    edges = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'F':
                edgeCandidate((x,y), (x+1, y), maybeEdges, edges)
                edgeCandidate((x,y), (x, y+1), maybeEdges, edges)
            if char == '7':
                edgeCandidate((x-1,y), (x, y), maybeEdges, edges)
                edgeCandidate((x,y), (x, y+1), maybeEdges, edges)
            if char == 'J':
                edgeCandidate((x-1,y), (x, y), maybeEdges, edges)
                edgeCandidate((x,y-1), (x, y), maybeEdges, edges)
            if char == 'L':
                edgeCandidate((x,y), (x+1, y), maybeEdges, edges)
                edgeCandidate((x,y-1), (x, y), maybeEdges, edges)
            if char == '|':
                edgeCandidate((x,y-1), (x, y), maybeEdges, edges)
                edgeCandidate((x,y), (x, y+1), maybeEdges, edges)
            if char == '-':
                edgeCandidate((x-1,y), (x, y), maybeEdges, edges)
                edgeCandidate((x,y), (x+1, y), maybeEdges, edges)
            if char == 'S':
                edgeCandidate((x-1,y), (x, y), maybeEdges, edges)
                edgeCandidate((x,y-1), (x, y), maybeEdges, edges)
                edgeCandidate((x,y), (x+1, y), maybeEdges, edges)
                edgeCandidate((x,y), (x, y+1), maybeEdges, edges)
                start = (x,y)
    return (edges, start, (len(lines[0]), len(lines)))

def solve1(input):
    lines = open(input).read().splitlines()
    edges, START = prepareEdgesAndStart(lines)
    where = START
    STEPS = 0
    while STEPS == 0 or where != START:
        STEPS += 1
        for e in edges:
            fromPoint, toPoint = e
            if fromPoint == where or toPoint == where:
                edges.remove(e)
                if fromPoint == where:
                    where = toPoint
                else:
                    where = fromPoint
                break  
    return int(STEPS/2)

print(solve1(sys.argv[1]))

def solve2(input):
    lines = open(input).read().splitlines()
    edges, START, (DIM_X, DIM_Y) = prepareEdgesAndStart(lines)
    where = START
    isEdge = [[False]*DIM_Y for _ in range(DIM_X)]
    countAbove = [[0]*DIM_Y for _ in range(DIM_X)]
    countToLeft = [[0]*DIM_Y for _ in range(DIM_X)]

    STEPS = 0
    traverseEdges = set(edges)
    while STEPS == 0 or where != START:
        whereX, whereY = where
        isEdge[whereX][whereY] = True
        STEPS += 1
        for e in traverseEdges:
            fromPoint, toPoint = e
            if fromPoint == where or toPoint == where:
                traverseEdges.remove(e)
                if fromPoint == where:
                    where = toPoint
                else:
                    where = fromPoint
                break  

    for x in range(1, DIM_X):
        for y in range(DIM_Y):
            countToLeft[x][y] = countToLeft[x-1][y]
            charToLeft = lines[y][x-1]
            if isEdge[x-1][y] and charToLeft in {'J', '7', '|'}:
                countToLeft[x][y] += 1

    for y in range(1,DIM_Y):
        for x in range(DIM_X):
            countAbove[x][y] = countAbove[x][y-1]
            charAbove = lines[y-1][x]
            if isEdge[x][y-1] and charAbove in {'J', 'L', '-'}:
                countAbove[x][y] += 1

    SUM = 0
    
    # for y in range(DIM_Y):
    #     for x in range(DIM_X):
    #         if not isEdge[x][y] and (
    #             countAbove[x][y] % 2 == 1 and 
    #             countToLeft[x][y] % 2 == 1 ):
    #             SUM += 1
    #         if isEdge[x][y]:
    #             print("X", end='')
    #         elif (countAbove[x][y] % 2 == 1 and
    #             countToLeft[x][y] % 2 == 1):
    #             print("I", end='')
    #         else:
    #             print(".", end='')
    #     print()
    # print()
    return SUM

print(solve2(sys.argv[1]))