from os import X_OK, makedirs


def load_input(coordinates, folds):
    #f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-9/9-1.txt", "r")
    #f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-9/test.txt", "r")
    f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-13/puzzleinput.txt", "r")
    #f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-13/test.txt", "r")
    #f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-13/test2.txt", "r")
    for line in f: 
        line = line.strip().strip('\n')
        if "fold along " in line:
            line = line.replace("fold along ", "")
            fold = tuple(line.split("="))
            folds.append([fold[0], int(fold[1])])
        elif len(line) > 0:
            coordinates.append(tuple(map(int, line.split(','))))

def print_grid(grid):
    for line in grid:
        print(''.join(map(str, line)))       


def puzzel1(coords, folds, stop_after):
    #find max values
    max_x = 0
    max_y = 0
    for coord in coords:
        max_x = max(max_x, coord[0])
        max_y = max(max_y, coord[1])
    print(f"max_x: {max_x} max_y: {max_y}")
    #define transparent grid
    grid=[["." for x in range(max_x+1)] for y in range(max_y+1)]
    print_grid(grid)
    #mark coordinates
    for count, coord in enumerate(coords):
        grid[coord[1]][coord[0]] = "#"
        print(f"coord[{count}]: {coord}")
        #print_grid(grid)
    #fold grid
    for i,fold in enumerate(folds):
        if i >= stop_after: continue
        if (fold[0] == "y"):
            _grid=[["." for x in range(max_x+1)] for y in range(fold[1])]
            for y in range(fold[1]):
                for x in range(0, max_x+1):
                    if grid[y][x] == "#" or grid[max_y-y][x] == "#":
                        _grid[y][x] = "#"
                    else:
                        _grid[y][x] = "."
                print(f"folded y line: {y}")
                #print_grid(grid)
            #copy _grid to grid
            grid = _grid
            print("folded y line")
            print_grid(grid)
            max_y=fold[1]-1
        if (fold[0] == "x"):
            _grid=[["." for x in range(fold[1])] for y in range(max_y+1)]
            for x in range(fold[1]):
                for y in range(0, max_y+1):
                    if grid[y][x] == "#" or grid[y][max_x-x] == "#":
                        _grid[y][x] = "#"
                    else:
                        _grid[y][x] = "."
                print(f"folded x line: {x}")
                #print_grid(_grid)
            #copy _grid to grid
            grid = _grid
            max_x=fold[1]-1
            print("folded x line")
            print_grid(grid)
            
    #count number of #
    count = 0
    for y in range(0, len(grid)):
        for x in range(0, max_x+1):
            if grid[y][x] == "#":
                print(f"# at {x},{y}")
                count += 1
    return count
            

coords=[]
folds=[]
load_input(coords, folds)                    
print("Anwser puzzel 1:", puzzel1(coords, folds,1))
print("Anwser puzzel 2:", puzzel1(coords, folds,len(folds)))
