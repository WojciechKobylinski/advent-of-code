import sys

def allZeroes(nums):
    return all(num == 0 for num in nums)

def prepareNextLevel(nums):
    # print("preparing next level "+str(nums))
    return [nums[i] - nums[i-1] for i in range(1, len(nums))]

def predict(nums):
    levels = [nums]
    currentLevel = 0
    while not allZeroes(levels[currentLevel]):
        newLevel = prepareNextLevel(levels[currentLevel])
        # print(" new level "+ str(newLevel))
        levels.append(newLevel)
        currentLevel += 1
    levels[currentLevel].append(0)
    for lvl in range(currentLevel-1, 0, -1):
        newVal = levels[lvl][-1] + levels[lvl-1][-1]
        levels[lvl-1].append(newVal)
    return levels[0][-1]

def solve1(input):
    lines = open(input).read().splitlines()
    SUM = 0
    for line in lines:
        nums = list(map(int, line.split(" ")))
        SUM += predict(nums)
    return SUM


print(solve1(sys.argv[1]))