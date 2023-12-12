# Read input
with open('input.txt') as source_file:
    lines = [[int(y) for y in x.rstrip('\n').split(' ')] for x in source_file]

# Part 1
total_score_n = 0
for line in lines:
    next_item, new_item = line[-1], line[-1]
    curr_list = line
    while len([x for x in curr_list if x != 0]) > 0:
        new_list = []
        for i in range(len(curr_list)-1):
            new_list += [curr_list[i+1] - curr_list[i]]
        next_item += new_list[-1]
        curr_list = new_list
    total_score_n += next_item
print(f"The answer to question 1 is {total_score_n}")

# Part 2
total_score_p = 0
for line in lines:
    curr_list = line
    new_line = [curr_list[::-1]]
    while len([x for x in curr_list if x != 0]) > 0:
        new_list = []
        for i in range(len(curr_list)-1):
            new_list += [curr_list[i+1] - curr_list[i]]
        new_line.append(new_list[::-1])
        curr_list = new_list
    new_line = new_line[::-1]
    for i in range(1,len(new_line)):
        new_line[i].append(new_line[i][-1] - new_line[i-1][-1])
    total_score_p += new_line[-1][-1]
print(f"The answer to question 2 is {total_score_p}")