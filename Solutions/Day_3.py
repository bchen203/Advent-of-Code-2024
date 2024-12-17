import re
# from Solutions.Day_2 import is_monotonically_increasing

with open("../Input/Day_3.txt", "r") as file:
    contents = file.read()



matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", contents)

total = 0
# Part 1 Solution
for match in matches:
    nums = re.findall(r"\d{1,3}", match)
    total += (int(nums[0]) * int(nums[1]))

print(f"total: {total}")


# Part 2 Solution

total = 0

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", contents)

is_enabled = True
for match in matches:
    if match == "do()":
        is_enabled = True
    elif match == "don't()":
        is_enabled = False
    else:
        if is_enabled:
            num_string = re.findall(r"\d{1,3}", match)
            total += (int(num_string[0]) * int(num_string[1]))
print(f"total: {total}")
