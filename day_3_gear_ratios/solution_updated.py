# Import required packages
import re

# Read input
with open('input.txt') as source_file:
    items = [[y for y in x.rstrip('\n')] for x in source_file]


# Part 1 - functions
def symbol_search(num, row, col):
    if len(num) > 0:
        for y in [-1, 0, 1]:
            for x in range(len(num)+2):
                cr, cc = row+y, col-x
                if (len(items) > cr >= 0 and len(items[0]) > cc >= 0) and not bool(re.search(r'\d|\.', items[cr][cc])):
                    return int(num)
    return 0


# Part 1
part_sum = 0
num_str = ''
for row in range(len(items)):
    for col in range(len(items[row])):
        if items[row][col].isdigit() and col < len(items[row])-1:
            num_str += items[row][col]
        elif items[row][col].isdigit() and col == len(items[row])-1:
            num_str += items[row][col]
            part_sum += symbol_search(num_str, row, col)
            num_str = ''
        else:
            part_sum += symbol_search(num_str, row, col)
            num_str = ''
print(f"Answer to question 1: {part_sum}")

# Part 2


# 527446 is right