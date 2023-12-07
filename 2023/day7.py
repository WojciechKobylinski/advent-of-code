import sys, itertools

CARD_VALUE = {
    "A":12,
    "K":11,
    "Q":10,
    "J":9,
    "T":8,
    "9":7,
    "8":6,
    "7":5,
    "6":4,
    "5":3,
    "4":2,
    "3":1,
    "2":0,
}

CARD_VALUE_WITH_JOKER = {
    "A":12,
    "K":11,
    "Q":10,
    "T":9,
    "9":8,
    "8":7,
    "7":6,
    "6":5,
    "5":4,
    "4":3,
    "3":2,
    "2":1,
    "J":0,
}


def getTupleCount(cards):
    frequencyOfCards = {card: cards.count(card) for card in set(cards)}
    frequencies = list(frequencyOfCards.values())
    tuples = {val: frequencies.count(val) for val in set(frequencies)}
    return tuples

def gradeTuples(tuples):
    if 5 in tuples.keys():
        return 6
    elif 4 in tuples.keys():
        return 5
    elif 3 in tuples.keys() and 2 in tuples.keys():
        return 4
    elif 3 in tuples.keys():
        return 3
    elif 2 in tuples.keys() and tuples[2] == 2:
        return 2
    elif 2 in tuples.keys():
        return 1
    else:
        return 0
    
def grade(cards):
    tuples = getTupleCount(cards)
    return gradeTuples(tuples)


def calculateOrder(valueMap, cards):
    N = len(valueMap)
    cardValues = list(map(lambda x: valueMap[x], cards))
    cardValues = [
        cardValues[0] * N**4,
        cardValues[1] * N**3,
        cardValues[2] * N**2,
        cardValues[3] * N**1,
        cardValues[4],
    ]
    return sum(cardValues)

def solve1(input):
    lines = open(input).read().splitlines()
    hands = []
    for line in lines:
        cards, bet = line.split(" ")
        graded = grade(cards)
        order = calculateOrder(CARD_VALUE, cards)
        hands.append({"cards": cards, "bet": int(bet), "order" : order, "graded": graded})
    # sorted from worst to best
    sortedHands = sorted(hands, key = lambda x: (x["graded"], x["order"]))
    SUM = 0
    for multiplier, hand in enumerate(sortedHands):
        SUM += (multiplier+1) * hand["bet"]
    return SUM


print(solve1(sys.argv[1]))

def gradeWithJoker(cards):
    jokerCount = cards.count("J")
    cards = cards.replace("J", "")
    max = grade(cards)
    for drawCards in itertools.product('23456789TQKA', repeat=jokerCount):
        aGrade = grade(cards+"".join(drawCards))
        if aGrade > max:
            max = aGrade
    return max

def solve2(input):
    lines = open(input).read().splitlines()
    hands = []
    for line in lines:
        cards, bet = line.split(" ")
        graded = gradeWithJoker(cards)
        order = calculateOrder(CARD_VALUE_WITH_JOKER, cards)
        hands.append({"cards": cards, "bet": int(bet), "order" : order, "graded": graded})
    # sorted from worst to best
    sortedHands = sorted(hands, key = lambda x: (x["graded"], x["order"]))
    SUM = 0
    for multiplier, hand in enumerate(sortedHands):
        SUM += (multiplier+1) * hand["bet"]
    return SUM

print(solve2(sys.argv[1]))