import sys

def filterDigits(s):
    return ''.join(filter(str.isdigit, s))

def firstDigit(s):
    return int(s[0])

def lastDigit(s):
    return int(s[-1])

def pickFirstAndLast(s):
    return firstDigit(s)*10 + lastDigit(s)

def solve(input):
    lines = open(input).read().splitlines()
    justNumbers = list(map(filterDigits, lines))
    picked = list(map(pickFirstAndLast, justNumbers))
    return sum(picked)

print(solve(sys.argv[1]))

INTERESTING = {
    "1": 1, "one": 1,
    "2": 2, "two": 2,
    "3": 3, "three": 3,
    "4": 4, "four": 4,
    "5": 5, "five": 5,
    "6": 6, "six": 6,
    "7": 7, "seven": 7,
    "8": 8, "eight": 8,
    "9": 9, "nine": 9,
}

def firstDigitOrWord(s):
    for i, c in enumerate(s):
        for k, v in INTERESTING.items():
            if (s[i:i+len(k)]) == k:
                return v

def lastDigitOrWord(s):
    for i in range (len(s), -1, -1):
        for k, v in INTERESTING.items():
            if (s[i-len(k):i]) == k:
                return v


def pickFirstAndLastWithWords(s):
    return firstDigitOrWord(s)*10 + lastDigitOrWord(s)

def solve2(input):
    lines = open(input).read().splitlines()
    picked = list(map(pickFirstAndLastWithWords, lines))
    return sum(picked)
    
print(solve2(sys.argv[1]))