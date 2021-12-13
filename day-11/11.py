def load_grid(grid):
    #f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-9/9-1.txt", "r")
    #f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-9/test.txt", "r")
    f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-11/puzzleinput.txt", "r")
    #f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-11/test.txt", "r")
    #f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-11/test2.txt", "r")
    for line in f:
        grid.append(list(map(int,list(line.strip()))))

def print_grid(grid):
    for line in grid:
        print(''.join(map(str, line)))

def get_neighbour_cells(grid, org_x, org_y):
    neighbour_cells = []
    for y_delta in (-1,0,1):
        y = org_y + y_delta
        if 0 <= y and y < len(grid):
            for x_delta in (-1,0,1):
                x = org_x + x_delta
                if 0 <= x and x < len(grid[y]):
                    #if not itself, then append to neighbour cells
                    if (x, y) != (org_x, org_y):
                        neighbour_cells.append((x, y))
    return neighbour_cells

def get_next_grid(grid,flash_count):
    from queue import Queue
    flashed = Queue()
    #every cell by +1
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1
            if grid[y][x] > 9:
                flashed.put((x, y))
    
    #when anyone flashed, then find neighbours and add 1      
    while flashed.qsize() > 0:
        x, y = flashed.get()
        if grid[y][x] >9:
            flash_count += 1
            grid[y][x] = 0  #reset cell to 0
            
            for x_buren, y_buren in get_neighbour_cells(grid, x, y):
                if grid[ y_buren][x_buren] != 0:
                    grid[ y_buren][x_buren] += 1
                if grid[ y_buren][x_buren] > 9:
                   flashed.put((x_buren,  y_buren))
                 
    return (grid, flash_count)
                  


def puzzel1(input):
    flash_count = 0
    for i in range(0, 100):
        input,flash_count = get_next_grid(input, flash_count)
        print("Itteration: %d - #flashes: %d"% (i+1, flash_count))
        #print_grid(input)
    return flash_count

def puzzel2(input):
    for i in range(0, 800):
        flash_count=0
        input,flash_count = get_next_grid(input, flash_count)
        
        print("Itteration: ", i+1)
        #print_grid(input)
        
        if sum(sum(flashes) for flashes in input) == 0:
            print(f"Synchronized: {i+1}")
            break
    return i + 1

input=[]
load_grid(input)                    
print_grid(input)
print("Anwser puzzel 1:", puzzel1(input))
input=[]
load_grid(input)                    
print_grid(input)
print("Anwser puzzel 2:", puzzel2(input))