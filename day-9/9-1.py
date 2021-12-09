#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-9/9-1.txt", "r")
#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-9/test.txt", "r")
f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-9/puzzleinput.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-9/test.txt", "r")

grid = dict()
for y, line in enumerate(f.readlines()):
    values = line.strip()
    for x, value in enumerate(values):
        grid[(x, y)] = int(value)

def GetLowPoints():
    low_point = []
    for (x,y) in grid:
        lowest_value = True
        lava_height = grid[(x,y)]
        for i in range(-1, 2):
            if (i != 0
                and (lava_height >= grid.get((x + i, y), float('inf'))
                or lava_height >= grid.get((x, y + i), float('inf')))):
                lowest_value = False
        if (lowest_value):
            low_point.append((x,y))
    return low_point

def GetBasinSize(point, count, visited):
    # Only count points that have not been visited before
    if(visited.get(point, False)):
        return 0
    # Don't cound the edge
    if(grid.get(point, 9) == 9):
        return 0

    # mark point as counted
    visited[point] = True
    count_result = 0
    # rescursively call the function for each adjacent point.
    count_result += GetBasinSize((point[0] - 1, point[1]), count, visited)
    count_result += GetBasinSize((point[0] + 1, point[1]), count, visited)
    count_result += GetBasinSize((point[0], point[1] - 1), count, visited)
    count_result += GetBasinSize((point[0], point[1] + 1), count, visited)
    return count_result + 1


def puzzel2():
    low_points = GetLowPoints()
    basin_sizes = []
    for i in low_points:
        basin_sizes.append(GetBasinSize(i, 0, dict()))
        
    basin_sizes.sort()
    r = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
    return r

def puzzel1():
    risk = 0
    for i in GetLowPoints():
        risk += grid[i] + 1
    return risk

print("Anwser puzzel 1:", puzzel1())
print("Anwser puzzel 2:", puzzel2())