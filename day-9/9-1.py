#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-9/9-1.txt", "r")
f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-9/test.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-8/8-1.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-8/test.txt", "r")
m=[]
for x in f:
    m.append(set(x.strip()))
    
