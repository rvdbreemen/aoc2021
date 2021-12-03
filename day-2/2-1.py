f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-2/2-1.txt", "r")
m=[]
for x in f:
    m.append(x.split())
print ("Aantal metingen: %d" % len(m))

i = 0
incr = 0
decr = 0
depth = 0
position = 0
for x in m:
    if x[0] == "down":
        depth += int(x[1])
    elif x[0] == "up":
        depth -= int(x[1])
    elif x[0] == "forward":
        position += int(x[1])
    i+=1

print ("depth: %d  position: %d  result: %d"% (depth, position, depth * position))
f.close()