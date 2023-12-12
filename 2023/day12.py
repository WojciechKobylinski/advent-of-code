import sys, itertools

def possible(springs, nums):
    cnt = 0
    tmpNums = list(nums)
    matched = 0
    for c in springs:
        if c == '.':
            if cnt > 0:
                if tmpNums and cnt == tmpNums[0]:
                    tmpNums = tmpNums[1:]
                    cnt = 0
                    matched += 1
                else:
                    return False
        elif c == '#':
            cnt += 1
    if cnt > 0:
        if tmpNums and cnt == tmpNums[0]:
            matched += 1
        else:
            return False
    
    return matched == len(nums)

def processLine(springs, nums):
    options = [springs]
    for i, c in enumerate(options[0]):
        if c == '?':
            newOptions = []
            for opt in options:
                withSub = list(opt)
                withSub[i] = '.'
                newOptions.append(withSub)
                withoutSub = list(opt)
                withoutSub[i] = '#'
                newOptions.append(withoutSub)
            options = newOptions
    result = 0
    for opt in options:
        if possible(opt, nums):
            # print("OPT "+str(opt)+" NUMS "+str(nums))
            result += 1
    return result

def solve1(input):
    lines = open(input).read().splitlines()
    SUM = 0
    for line in lines:
        springs, nums = line.split(" ")
        springs = list(springs)
        nums = list(map(int, nums.split(",")))

        # print(" LINE "+"".join(springs))
        SUM += processLine(springs, nums)
    return SUM

print(solve1(sys.argv[1]))

def solve2(input):
    lines = open(input).read().splitlines()
    SUM = 0
    for line in lines:
        springs, nums = line.split(" ")
        springs = springs+"?"+springs+"?"+springs+"?"+springs+"?"+springs
        springs = list(springs)
        nums = list(map(int, nums.split(",")))
        nums = nums * 5

        # print(" LINE "+"".join(springs))
        SUM += processLine(springs, nums)
    return SUM

# print(solve2(sys.argv[1]))
