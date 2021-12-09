#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-8/8-1.txt", "r")
#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-8/test.txt", "r")
f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-8/8-1.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-8/test.txt", "r")
m=[]
a=[]
b=[]
for x in f:
    m = x.strip().split("|")
    a.append(m[0].split())
    b.append(m[1].split())
    
print("aantal: %d" % len(a))

import numpy as np

a = np.zeros((8),  dtype = int)
print(a)

for x in b:
    for i in range(0, len(x)):
        s = x[i]
        c = len(s)-1
        a[c] += 1
        print(s, c)
    print (x, a)

s = a[1] + a[2] + a[3] + a[6]
print ("Anwser: %d" % (s))
    
    
