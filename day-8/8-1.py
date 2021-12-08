#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-8/8-1.txt", "r")
f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-8/test.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-8/8-1.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-8/test.txt", "r")
m=[]
a=[]
b=[]
for x in f:
    m = x.strip().split("|")
    a.append(m[0].split())
    b.append(m[1].split())
    
print("aantal: %d" % len(a))


    
print(min(o))
