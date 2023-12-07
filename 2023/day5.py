import sys

def translateSeeds(seeds, translations):
    result = []
    for seed in seeds:
        newSeed = seed
        for t in translations:
            if seed >= t["from"] and seed < t["to"]:
                newSeed = seed - t["from"] + t["moveTo"]
                break
        result.append(newSeed)
    return result

def solve1(input):
    lines = open(input).read().splitlines()
    _, seedsString = lines[0].split(": ")
    seeds = list(map(int, seedsString.split(" ")))
    translations = []
    for line in lines[1:]:
        if not line or line[0].isalpha():
            seeds = translateSeeds(seeds, translations)
            #cleared each time the numbers are stopping.
            #can be applied multiple times because after use translations are cleared
            translations = []
        else:
            rangeStart, sourceRangeStart, rangeLength = list(map(int, line.split(" ")))
            translations.append({
                "from": sourceRangeStart,
                "to": sourceRangeStart + rangeLength,
                "moveTo": rangeStart
            })
    seeds = translateSeeds(seeds, translations)
    return min(seeds)

print(solve1(sys.argv[1]))

def move(seed, start, moveTo):
    return (seed-start) + moveTo

def translateSeedRange(seedRanges, translations):
    result = []

    notTranslated = seedRanges

    while seedRanges:
        sr = notTranslated.pop()
        noMatch = True
        for t in translations:
            a, b = sr
            ta, tb, moveTo = t["from"], t["to"], t["moveTo"]

            #do they cut
            if ta<b and tb>a:
                noMatch = False
                if ta>a and tb<b:
                    notTranslated.append([a, ta])
                    result.append([moveTo, move(tb, ta, moveTo)])
                    notTranslated.append([tb, b])
                    break
                elif ta<=a and tb>=b:
                    result.append([move(a,ta,moveTo), move(b,ta,moveTo)])
                    break
                elif ta>a:
                    notTranslated.append([a,ta])
                    result.append([moveTo, move(b,ta,moveTo)])
                    break
                else: #tb<b
                    result.append([move(a,ta,moveTo), move(tb,ta,moveTo)])
                    notTranslated.append([tb, b])
                    break
        if noMatch:
            result.append(sr)
            
    return result

def solve2(input):
    lines = open(input).read().splitlines()
    _, seedsString = lines[0].split(": ")
    seedsRanges = list(map(int, seedsString.split(" ")))
    seeds = []
    for i in range(0, len(seedsRanges), 2):
        seeds.append([seedsRanges[i], seedsRanges[i]+seedsRanges[i+1]])
    translations = []
    for line in lines[1:]:
        if not line or line[0].isalpha():
            seeds = translateSeedRange(seeds, translations)
            #cleared each time the numbers are stopping.
            #can be applied multiple times because after use translations are cleared
            translations = []
        else:
            rangeStart, sourceRangeStart, rangeLength = list(map(int, line.split(" ")))
            translations.append({
                "from": sourceRangeStart,
                "to": sourceRangeStart + rangeLength,
                "moveTo": rangeStart
            })
    seeds = translateSeedRange(seeds, translations)
    return min(list(map(lambda x: x[0],seeds)))

print(solve2(sys.argv[1]))