#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-4/1-1.txt", "r")
# f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-3/test1.txt", "r")
f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-6/6-1.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-6/test.txt", "r")
m=[]
for x in f:
    m=list(map(int, x.split(",")))
   
print("aantal: %d" % len(m))

s=[]
for i in range(0,9):
    s.append(m.count(i))
    
    
for g in range(0,257):
    print ("day: %d" % g)
    sum=0
    for x in s:
        sum += x
    print ("Number of fish: %d" % sum)
    
    r = s.copy()
    r.pop(0)

    x = s[0]
    r[6]=r[6]+x
    r.append(x)
    s = r.copy()
    
    
        
    # for x in range(0, len(m)):
    #     m[x] -= 1
    
    # for x in range(0,len(m)):
    #     if m[x]<0:
    #         m[x]=6
    #         m.append(8)
            

    
    
        