
def count_horizontal(strings: list[str]):
    total = 0
    width = len(strings[0]) - 1 # account for newline char
    for string in strings:
        for x in range(width - 3):
            horizontal_string = string[x:x+4]
            # print(horizontal_string)
            if horizontal_string == "XMAS" or horizontal_string == "SAMX":
                total += 1

    return total

def count_vertical(strings: list[str]):
    width = len(strings[0]) - 1 # account for newline char
    height = len(strings)

    total = 0
    for y in range(height - 3):
        for x in range(width):
            vert_string = strings[y][x] + strings[y+1][x] + strings[y+2][x] + strings[y+3][x]
            # print(vert_string)
            if vert_string == "XMAS" or vert_string == "SAMX":
                total += 1



            # print(strings[y][x] + strings[y+1][x] + strings[y+2][x] + strings[y+3][x])
    return total

def count_diagonal(strings: list[str]):
    width = len(strings[0]) - 1  # account for newline char
    height = len(strings)

    right = 0
    for y in range(height - 3):
        for x in range(width - 3):
            right_diagonal_string = strings[y][x] + strings[y + 1][x + 1] + strings[y + 2][x + 2] + strings[y + 3][x + 3]
            # print(right_diagonal_string)
            if right_diagonal_string == "XMAS" or right_diagonal_string == "SAMX":
                right += 1

    left = 0
    for y in range(height - 3):
        # print("Current Block")
        # print(strings[y] + strings[y+1] + strings[y+2] + strings[y+3])
        # print(strings[y+1])
        # print(strings[y+2])
        # print(strings[y+3])
        for x in range(width - 1, 2, -1):
            # print(y, x)
            # print(strings[y])
            # print(strings[y][x])
            left_diagonal_string = strings[y][x] + strings[y + 1][x - 1] + strings[y + 2][x - 2] + strings[y + 3][x - 3]
            # print(left_diagonal_string)
            # print()
            if left_diagonal_string == "XMAS" or left_diagonal_string == "SAMX":
                left += 1
    # print(left, right)
    return left + right

def count_XMAS(strings: list[str]):
    width = len(strings[0]) - 1
    height = len(strings)
    total = 0
    for y in range(height - 2):
        for x in range(width - 2):
            right_diagonal = strings[y][x] + strings[y + 1][x + 1] + strings[y + 2][x + 2]
            print(right_diagonal)
            left_diagonal = strings[y][x + 2] + strings[y + 1][x + 1] + strings[y + 2][x]
            print(left_diagonal)
            if (right_diagonal == "MAS" or right_diagonal == "SAM") and (left_diagonal == "MAS" or left_diagonal == "SAM"):
                total += 1
    return total

with open("../Input/Day_4.txt", "r") as file:
    # contents = file.read()

    lines = file.readlines()
    print(lines)

# Part 1 Solution
total = sum([count_horizontal(lines), count_vertical(lines), count_diagonal(lines)])
print(f"total: {total}")

# Part 2 Solution
total = count_XMAS(lines)
print(f"total: {total}")

# print(count_horizontal(lines))
# print(count_vertical(lines))
# print(count_diagonal(lines))
