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

# Part 2
cube_power_sum = 0
pattern = r'(\d+)\s*([a-zA-Z]+)'
for item in items:
    min_cube = {'red':0, 'green':0, 'blue':0}
    matches = re.findall(pattern, item)
    for match in matches:
        if int(match[0]) > min_cube[match[1]]:
            min_cube[match[1]] = int(match[0])
    cube_power_sum += min_cube['red'] * min_cube['green'] * min_cube['blue']

print(cube_power_sum)
