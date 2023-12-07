# Import requirements
import re

# Read input
with open('input.txt') as source_file:
    items = [x.rstrip('\n') for x in source_file]

# Part 1
seeds = [int(x) for x in items[0].replace("seeds: ", "").split(" ")]
map_dict = {}
for item in items[2::]:
    print(item)
    if item.split(' ')[0] == 'seed-to-soil':
        curr_map = item.split(' ')[0]
        curr_rng = []
    elif bool(re.findall(r'\b\w+-to-\w+\b', item)):
        map_dict[curr_map] = curr_rng
        curr_map = item.split(' ')[0]
        curr_rng = []
    elif len(item) != 0:
        curr_rng.append([int(x) for x in item.split(' ')])

print(map_dict)