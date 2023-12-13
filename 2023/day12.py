import sys
from functools import lru_cache

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

def matchingNum(springs, num):
    if len(springs) < num:
        return False
    if len(springs) == num:
        return all(c in {'#', '?'} for c in springs[:num])
    return all(c in {'#', '?'} for c in springs[:num]) and springs[num] in ('.', '?')

@lru_cache
def sumRecurrent(springs, nums):
    if not nums:
        return 1
    if not springs:
        return 0
    allNums = nums.split(",")
    firstNum = int(nums[0])
    restNums = ",".join(allNums[1:])
    if springs[0] == '.':
        return sumRecurrent(springs[1:], nums)
    if springs[0] == '?':
        without = sumRecurrent(springs[1:], nums)
        if matchingNum(springs, firstNum):
            return without + sumRecurrent(springs[firstNum+1:], restNums)
        else:
            return without
    if springs[0] == "#":
        if matchingNum(springs, firstNum):
            return sumRecurrent(springs[firstNum+1:], restNums)
        else:
            return 0
    print("ERRRORRR")
    return -1



def solve2(input):
    lines = open(input).read().splitlines()
    SUM = 0
    for line in lines:
        springs, nums = line.split(" ")
        springs = springs+"?"+springs+"?"+springs+"?"+springs+"?"+springs
        nums = nums+','+nums+','+nums+','+nums+','+nums

        # print(" LINE "+"".join(springs))
        SUM += sumRecurrent(springs, nums)
    return SUM

print(solve2(sys.argv[1]))
