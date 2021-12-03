f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-3/3-2.txt", "r")
#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-3/test1.txt", "r")

# f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-3/test1.txt", "r")
# f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-3/3-1.txt", "r")
m=[]
for x in f:
    m.append(x)
print ("Aantal metingen: %d" % len(m))
powerof2 = len(m[0])-1
print ("Power of 2: %d" % powerof2)

i = 0
s = m
for i in range(0, len(x)):
    one = 0
    zero = 0
    oneset = []
    zeroset=[]
    for x in s:
        if x[i] == '0':
            zero += 1
            zeroset.append(x)
        else:
            one += 1
            oneset.append(x)
        
    if (one > zero):
        s = oneset
    if (one < zero):
        s = zeroset
    if (one == zero):
        s = oneset
    if len(s) == 1:
        break

o2 = int(s[0],2)
print("O2: %d" % o2)

i = 0
s = m
for i in range(0, len(x)):
    one = 0
    zero = 0
    oneset = []
    zeroset=[]
    for x in s:
        if x[i] == '0':
            zero += 1
            zeroset.append(x)
        else:
            one += 1
            oneset.append(x)
        
    if (zero < one):
        s = zeroset
    if (zero > one):
        s = oneset
    if (one == zero):
        s = zeroset
    if len(s) == 1:
        break

co2 = int(s[0],2)
print("CO2: %d" % co2)
print("Answer: %d" % (o2 * co2))

# print ("power consumption: %d"% (gamma * epsilon))
f.close()