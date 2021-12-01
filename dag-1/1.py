f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/dag-1/1.txt", "r")
i = 0
incr = 0
decr = 0
for x in f:
    if (i>0):
        if (int(x)>y):
            incr+=1
            print("%d (increment)" % int(x))
        else:
            decr+=1
            print("%d (decrement)"% int(x))
    y = int(x)
    i+=1
print ("result: %d"% incr)
f.close()