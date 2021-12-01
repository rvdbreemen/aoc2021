f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/dag-1/1-2.txt", "r")
m=[]
for x in f:
    m.append(int(x))
print ("aantal metingen: %d"%len(m))

i = 0
incr = 0
decr = 0
for x in m:
    w1 = m[i]+m[i+1]+m[i+2]
    w2 = m[i+1]+m[i+2]+m[i+3]
    if(w2>w1):
        incr+=1
        print("%d: %d (increment)" % (i,int(x)))
    elif (w2==w1):
        print("%d: %d (equal)" % (i,int(x)))
    else:
        decr+=1
        print("%d: %d (decrement)"% (i,int(x)))

    i+=1
    if (i+3>len(m)-1):
        break

print ("result: %d"% incr)
f.close()