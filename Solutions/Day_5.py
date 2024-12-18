

with open("../Input/Day_5.txt", "r") as file:
    lines = file.readlines()

rules = [line[:-1] for line in lines if "|" in line]

rules_dict = {}
for rule in rules:
    before = int(rule[0:2])
    after = int(rule[-2:])
    if before not in rules_dict:
        rules_dict.update({before:[after]})
    else:
        values = rules_dict.get(before)
        values.append(after)
        rules_dict.update({before: values})
updates = lines[len(rules) + 1:]
# convert updates to list[list[int]]
updates = [[int(num) for num in update.strip().split(",")] for update in updates]

# Part 1 Solution
results = []
for update in updates:
    valid_update = True
    for i in range(len(update)):
        if not valid_update:
            break
        for j in range(i, len(update)):
            if update[j] in rules_dict:
                if update[i] in rules_dict.get(update[j]):
                    valid_update = False
                    break
    if valid_update:
        results.append(update[len(update)//2])
print(f"total: {sum(results)}")

# Part 2 Solution
invalid_updates = []
for update in updates:
    valid_update = True
    for i in range(len(update)):
        if not valid_update:
            invalid_updates.append(update)
            break
        for j in range(i, len(update)):
            if update[j] in rules_dict:
                if update[i] in rules_dict.get(update[j]):
                    valid_update = False
                    break

for update in invalid_updates:
    for i in range(len(update)):
        for j in range(i, len(update)):
            if update[j] in rules_dict:
                if update[i] in rules_dict.get(update[j]):
                    temp = update[j]
                    update[j] = update[i]
                    update[i] = temp
total = 0
for update in invalid_updates:
    total += update[len(update)//2]
print(f"total: {total}")

