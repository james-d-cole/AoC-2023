# Import required packages
import re

# Read input
with open('input.txt') as source_file:
    items = [x.rstrip('\n') for x in source_file]

# Part 1
races = list(zip(re.findall(r'(\d+)', items[0]), re.findall(r'(\d+)', items[1])))
win_sum = 1
for race in races:
    time, dist = int(race[0]), int(race[1])
    wins = 0
    for i in range(time+1):
        if (i * (time - i)) > dist:
            wins += 1
    win_sum = win_sum * wins
print(f"Answer to question 1: {win_sum}")

# Part 2
time = int("".join(re.findall(r'(\d+)', items[0])))
dist = int("".join(re.findall(r'(\d+)', items[1])))
wins = 0
for i in range(time+1):
    if (i * (time - i)) > dist:
        wins += 1
print(f"Answer to question 1: {wins}")
