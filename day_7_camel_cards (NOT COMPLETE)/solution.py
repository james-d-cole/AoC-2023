# Import required packages
import re
from collections import Counter

# Read input
with open('input.txt') as source_file:
    items = [x.rstrip('\n') for x in source_file]


# Functions
def convert(card):
    if card == 'T':
        return 10
    elif card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 14
    else:
        return int(card)


# Part 1
hands = [re.findall(r'([A-Z0-9][^\s]+)', x) for x in items]
fives, fours, house, three, tpair, opair, highc = [], [], [], [], [], [], []
for i in range(len(hands)):
    hands[i][0] = [convert(x) for x in hands[i][0]]
    len_set = len(set(hands[i][0]))
    if len_set == 1:
        fives.append(hands[i])
    elif len_set == 2 and Counter(hands[i][0]).most_common(1)[0][1] == 4:
        fours.append(hands[i])
    elif len_set == 2 and Counter(hands[i][0]).most_common(1)[0][1] == 3:
        house.append(hands[i])
    elif len_set == 3 and Counter(hands[i][0]).most_common(1)[0][1] == 3:
        three.append(hands[i])
    elif len_set == 3 and Counter(hands[i][0]).most_common(1)[0][1] == 2:
        tpair.append(hands[i])
    elif len_set == 4:
        opair.append(hands[i])
    elif len_set == 5:
        highc.append(hands[i])

print(fives)
print(fours)
print(house)
print(three)
print(tpair)
print(opair)
print(highc)