with open("./Input/Day_1.txt", "r") as file:
    lines = file.readlines()


left = []
right = []
freqRight = {} # for part 2
for line in lines:
    temp = line.split("   ")
    valLeft = int(temp[0])
    valRight = int(temp[1].strip())
    left.append(valLeft)
    right.append(valRight)
    if valRight in freqRight:
        freqRight.update({valRight: freqRight.get(valRight) + 1})
    else:
        freqRight.update({valRight: 1})

print(freqRight)
left.sort()
right.sort()

difference = []

# Part 1 Solution
for i in range(len(left)):
    difference.append(abs(right[i] - left[i]))
print(difference)
print(sum(difference))


#Part 2 Solution
similarity = 0
for num in left:
    if num in freqRight:
        similarity += num * freqRight.get(num)

print(similarity)
