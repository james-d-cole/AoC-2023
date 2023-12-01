 # Read input
with open('input.txt') as source_file:
    items = [x.rstrip('\n') for x in source_file]
 
 # Part 1
calibration_sum = 0
for item in items:
    digits = [x for x in item if x in ('1', '2', '3', '4', '5', '6', '7', '8', '9')]
    calibration_sum += int(digits[0] + digits[-1])
print(f"Answer to question 1: {calibration_sum}")

# Part 2
calibration_sum = 0
replace_dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9',
                '1':'1', '2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9'}
for item in items:
    search_results = []
    for search_string in replace_dict.keys():
        if item.find(search_string) > -1:
            search_results += [[replace_dict[search_string], item.find(search_string)]]
        if item.rfind(search_string) > -1:
            search_results += [[replace_dict[search_string], item.rfind(search_string)]]
    search_results.sort(key = lambda x: x[1])
    calibration_sum += int(search_results[0][0] + search_results[-1][0])
print(f"Answer to question 2: {calibration_sum}")