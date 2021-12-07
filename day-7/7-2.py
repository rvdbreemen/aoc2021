f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-7/7-1.txt", "r")
#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-7/test.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-7/7-1.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-6/test.txt", "r")
m=[]
for x in f:
    m=list(map(int, x.split(",")))
   
print("aantal: %d" % len(m))

max_value = max(m)
o=[]
t=0
for x in range(0, max_value):
    d=0
    dl=[]
    for y in m:
        e = 0
        if x>y:
            for i in range(y, x):
                e += 1
                d += e
        else:
            for i in range(x, y):
                e += 1
                d += e
    o.append(d)
    t+=1
    print(x)

print ("Zoek minimale waarde")
print(min(o))
print ("Klaar!")
