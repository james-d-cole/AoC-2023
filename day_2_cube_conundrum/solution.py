# Import packages
import re

# Read input
with open('input.txt') as source_file:
    items = [x.rstrip('\n') for x in source_file]

# Part 1
game_id_sum = 0
limits = {'red':12, 'green':13, 'blue':14}
pattern = r'(\d+)\s*([a-zA-Z]+)'
for item in items:
    game_id = int(item.split(': ')[0].replace("Game ", ""))
    matches = re.findall(pattern, item)
    within_limit = True
    for match in matches:
        if int(match[0]) > limits[match[1]]:
            within_limit = False
    if within_limit:
        game_id_sum += game_id
print(f"Answer to question 1: {game_id_sum}")
