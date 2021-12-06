#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-4/1-1.txt", "r")
# f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-3/test1.txt", "r")
f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-5/5-1.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-5/test.txt", "r")
m=[]
van=[]
naar=[]
for n in f:
    van.append(list(map(int, n.split()[0].split(","))))
    naar.append(list(map(int, n.split()[2].split(","))))

#setup result matrix
import numpy as np
size = 1000
r = np.zeros((size,size))

for i in range(len(van)):
    cx1=van[i][0]
    cy1=van[i][1]
    cx2=naar[i][0]
    cy2=naar[i][1]
    a=abs(cx1-cx2)
    b=abs(cy1-cy2)
    print(van[i], naar[i])
    print (a,b)
    
    if a==b:
        #diagonal
        dx=int((cx2-cx1)/a)
        dy=int((cy2-cy1)/b)
        for i in range(0, a+1):
            x = cx1+dx*i
            y = cy1+dy*i
            r[x,y]+=1    
    if b==0:
        #horizontal
        if cx1<cx2:
            for x in range(cx1,cx2+1):
                r[x,cy1] += 1
        else:
            for x in range(cx2,cx1+1):
                r[x,cy1] += 1
                
    if a==0:
        #vertical
        if cy1<cy2:
            for y in range(cy1,cy2+1):
                r[cx1,y] += 1
        else:
            for y in range(cy2,cy1+1):
                r[cx1,y] += 1
                

result = 0            
for x in range(size):
    for y in range(size):
        if r[x,y]>=2:
            result += 1
print ("Result: %d" % result)       
