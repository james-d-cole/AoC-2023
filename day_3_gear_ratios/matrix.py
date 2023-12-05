with open('input.txt') as source_file:
    items = [[y for y in x.rstrip('\n')] for x in source_file]



matrix = []
for i in range(len(items)):
    row = [[0]]*len(items[0])
    matrix.append(row)
matrix[0][0] = matrix[0][0] + [1]

print(matrix)