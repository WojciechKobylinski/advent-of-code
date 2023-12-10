import sys

def edgeCandidate(fromPoint, toPoint, maybeEdges, edges):
    newEdge = (fromPoint, toPoint)
    if newEdge in maybeEdges:
        maybeEdges.remove(newEdge)
        edges.add(newEdge)
    else:
        maybeEdges.add(newEdge)

def solve1(input):
    lines = open(input).read().splitlines()
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
                START = (x,y)
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
    # no time for it yet...
    SUM = 0
    return SUM

print(solve2(sys.argv[1]))