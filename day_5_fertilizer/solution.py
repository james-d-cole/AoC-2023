# Import required packages
import re

# Read input
with open('input.txt') as source_file:
    items = [x.rstrip('\n') for x in source_file]

# Part 1
seeds = [int(x) for x in items[0].replace("seeds: ", "").split(" ")]
mp = [[x]*8 for x in seeds]
x = 0
for item in items[2::]:
    if bool(re.findall(r'\b\w+-to-\w+\b', item)):
        x += 1
        for y in range(len(mp)):
            mp[y][x] = mp[y][x-1]
    elif len(item) > 0:
        cr = [int(x) for x in item.split(' ')]
        for y in range(len(mp)):
            if cr[1] <= mp[y][x-1] < cr[1]+cr[2]:
                mp[y][x] = cr[0]+mp[y][x-1]-cr[1]
print(f"Answer to question 1: {min([x[-1] for x in mp if x[0] in seeds])}")
