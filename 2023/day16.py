import sys

RIGHT = 1
DOWN = 2
LEFT = 4
UP = 8

MAPPINGS = {
    RIGHT: {
        "/": [UP],
        "\\": [DOWN],
        "|": [UP, DOWN],
        "-": [RIGHT],
    },
    LEFT: {
        "/": [DOWN],
        "\\": [UP],
        "|": [UP, DOWN],
        "-": [LEFT],
    },
    UP: {
        "/": [RIGHT],
        "\\": [LEFT],
        "|": [UP],
        "-": [RIGHT, LEFT],
    },
    DOWN: {
        "/": [LEFT],
        "\\": [RIGHT],
        "|": [DOWN],
        "-": [RIGHT, LEFT],
    }
}

def nextDirections(symbol, direction):
    if symbol == ".":
        return [direction]
    return MAPPINGS[direction][symbol]

def doSolve(input, initialBeam):
    MAX_X, MAX_Y = len(input[0]), len(input)
    touched = {(initialBeam[0], initialBeam[1])}
    visited = set()
    activeBeams = {initialBeam}
    while activeBeams:
        newBeams = set()
        for beam in activeBeams:
            if beam not in visited:
                x, y, beamDirection = beam
                touched.add((x,y))
                visited.add(beam)
                dirs = nextDirections(input[y][x], beamDirection)
                for dir in dirs:
                    if dir == LEFT and x > 0:
                        newBeams.add((x-1, y, LEFT))
                    if dir == RIGHT and x < MAX_X-1:
                        newBeams.add((x+1, y, RIGHT))
                    if dir == UP and y > 0:
                        newBeams.add((x, y-1, UP))
                    if dir == DOWN and y < MAX_Y-1:
                        newBeams.add((x, y+1, DOWN))
        activeBeams = newBeams
    return len(touched)

def solve1(input):
    input = open(input).read().splitlines()
    return doSolve(input, (0,0,RIGHT))

# print(solve1(sys.argv[1]))

def solve2(input):
    input = open(input).read().splitlines()
    MAX_X, MAX_Y = len(input[0]), len(input)
    MAX_RESULT = 0
    for y in range(MAX_Y):
        MAX_RESULT = max(MAX_RESULT, doSolve(input, (0, y, RIGHT)))
        MAX_RESULT = max(MAX_RESULT, doSolve(input, (MAX_X-1, y, LEFT)))
    for x in range(MAX_X):
        MAX_RESULT = max(MAX_RESULT, doSolve(input, (x, 0, DOWN)))
        MAX_RESULT = max(MAX_RESULT, doSolve(input, (x, MAX_Y-1, UP)))
    return MAX_RESULT

print(solve2(sys.argv[1]))