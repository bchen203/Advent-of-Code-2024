
def find_start(map: list[list[str]]):
    for i in range(len(map[0]) - 1):
        for j in range(len(map)):
            if map[i][j] == "^":
                return j, i


def move_guard(map: list[list[str]]):
    direction = "up"
    width = len(map[0])
    height = len(map)
    on_map = True
    x, y = find_start(map)
    visited = [[0 for i in range(width)] for j in range(height)]
    while on_map:
        match direction:
            case "up":
                if y - 1 < 0:
                    on_map = False
                    visited[y][x] = 1
                    map[y][x] = "X"
                elif map[y - 1][x] == "." or map[y - 1][x] == "X":
                    visited[y][x] = 1
                    map[y][x] = "X"
                    y -= 1
                    map[y][x] = "^"
                elif map[y - 1][x] == "#":
                    map[y][x] = ">"
                    direction = "right"
            case "down":
                if y + 1 > height - 1:
                    on_map = False
                    visited[y][x] = 1
                    map[y][x] = "X"
                elif map[y + 1][x] == "." or map[y + 1][x] == "X":
                    visited[y][x] = 1
                    map[y][x] = "X"
                    y += 1
                    map[y][x] = "V"
                elif map[y + 1][x] == "#":
                    map[y][x] = "<"
                    direction = "left"
            case "left":
                if x - 1 < 0:
                    on_map = False
                    visited[y][x] = 1
                    map[y][x] = "X"
                elif map[y][x - 1] == "." or map[y][x - 1] == "X":
                    visited[y][x] = 1
                    map[y][x] = "X"
                    x -= 1
                    map[y][x] = "<"
                elif map[y][x - 1] == "#":
                    map[y][x] = "^"
                    direction = "up"
            case "right":
                if x + 1 > width - 1:
                    on_map = False
                    visited[y][x] = 1
                    map[y][x] = "X"
                elif map[y][x + 1] == "."  or map[y][x + 1] == "X":
                    visited[y][x] = 1
                    map[y][x] = "X"
                    x += 1
                    map[y][x] = ">"
                elif map[y][x + 1] == "#":
                    map[y][x] = "V"
                    direction = "down"

    total_spaces = 0
    for line in visited:
        print(line)
        total_spaces += sum(line)

    print("Curr Map")
    for line in map:
        print(line)
    # with open("final_path.txt", "w") as file:
    #     for i in range(width):
    #         line = ""
    #         for j in range(height):
    #             line += map[i][j]
    #         file.write(line)
    #         if i != width - 1:
    #             file.write("\n")
    print(f"Spaces Traveled: {total_spaces}")





with open("../Input/Day_6.txt", "r") as file:
    lines = file.readlines()

lines = [list(line.strip()) for line in lines]
move_guard(lines)


