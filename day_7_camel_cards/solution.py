# Import required packages
import re
from collections import Counter

# Read input
with open('input.txt') as source_file:
    items = [x.rstrip('\n') for x in source_file]


# Parse hands
def parse_cards(items, part_2=False):
    hands = [re.findall(r'([A-Z0-9][^\s]+)', x) for x in items]
    for i in range(len(hands)):
        if part_2:
            hands[i][0] = ['J23456789TQKA'.index(x) + 1 for x in hands[i][0]]
        else:
            hands[i][0] = ['23456789TJQKA'.index(x) + 1 for x in hands[i][0]]
    return hands


# Score hand
def score_hand(h1, part_2=False):
    c1 = Counter(h1).most_common()
    if part_2:
        if c1[0][0] == 1 and len(c1) > 1:
            j1_sub = c1[1][0]
        else:
            j1_sub = c1[0][0]
        h1 = [x if x != 1 else j1_sub for x in h1]
        c1 = Counter(h1).most_common()
    if c1[0][1] == 5:
        return 7
    elif c1[0][1] == 4:
        return 6
    elif c1[0][1] == 3 and c1[1][1] == 2:
        return 5
    elif c1[0][1] == 3:
        return 4
    elif c1[0][1] == 2 and c1[1][1] == 2:
        return 3
    elif c1[0][1] == 2:
        return 2
    else:
        return 1


# Part 1 
total_sum = 0
hands = parse_cards(items, False)
for i in range(len(hands)):
    hands[i].append(score_hand(hands[i][0], False))
hands = sorted(hands, key=lambda x: (x[2], x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))
hands = [[rank + 1] + sublist for rank, sublist in enumerate(hands)]
for hand in hands:
    total_sum += (hand[0] * int(hand[2]))
print(f"Answer to question 1: {total_sum}")

# Part 2
total_sum = 0
hands = parse_cards(items, True)
for i in range(len(hands)):
    hands[i].append(score_hand(hands[i][0], True))
hands = sorted(hands, key=lambda x: (x[2], x[0][0], x[0][1], x[0][2], x[0][3], x[0][4]))
hands = [[rank + 1] + sublist for rank, sublist in enumerate(hands)]
for hand in hands:
    total_sum += (hand[0] * int(hand[2]))
print(f"Answer to question 2: {total_sum}")
