# Import required packages
import re

# Read input
with open('input.txt') as source_file:
    items = [x.rstrip('\n') for x in source_file]


# Check wins function
def check_wins(gi=0):
    win_nums = items[gi].split(": ")[1].split(' | ')[0].replace("  ", " ").split(" ")
    our_nums = items[gi].split(": ")[1].split(' | ')[1].replace("  ", " ").split(" ")
    return (len([x for x in our_nums if x in win_nums and x]))


# Part 1
win_sum = 0
for item in items:
    game_idx = int(re.findall(r'Card\s+(\d+):', item)[0])-1
    if check_wins(game_idx) > 0:
        win_sum += (2 ** (check_wins(game_idx)-1))
print(f"Answer to question 1: {win_sum}")

# Part 2
for item in items:
    game_idx = int(re.findall(r'Card\s+(\d+):', item)[0])-1
    for i in range(check_wins(game_idx)):
        items.append(items[game_idx+i+1])
print(f"Answer to question 2: {len(items)}")