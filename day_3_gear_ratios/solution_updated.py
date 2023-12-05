# Import required packages
import re
import numpy

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

# Part 2 - functions
def symbol_search(num, row, col):
    if len(num) > 0:
        for y in [-1, 0, 1]:
            for x in range(len(num)+2):
                cr, cc = row+y, col-x
                if (len(items) > cr >= 0 and len(items[0]) > cc >= 0) and bool(re.search(r'\*', items[cr][cc])):
                    matrix[cr][cc] = matrix[cr][cc] + [int(num)]
    return 0

# Part 1
matrix = []
for i in range(len(items)):
    row = [[1]]*len(items[0])
    matrix.append(row)
gear_sum = 0
num_str = ''
for row in range(len(items)):
    for col in range(len(items[row])):
        if items[row][col].isdigit() and col < len(items[row])-1:
            num_str += items[row][col]
        elif items[row][col].isdigit() and col == len(items[row])-1:
            num_str += items[row][col]
            gear_sum += symbol_search(num_str, row, col)
            num_str = ''
        else:
            gear_sum += symbol_search(num_str, row, col)
            num_str = ''
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        if len(matrix[row][col])==3:
            gear_sum += numpy.prod(matrix[row][col])




print(f"Answer to question 2: {gear_sum}")

# 527446 is right