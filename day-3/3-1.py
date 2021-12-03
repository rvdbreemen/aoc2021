f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-3/3-1.txt", "r")
# f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-3/test1.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-3/3-1.txt", "r")
m=[]
for x in f:
    m.append(x)
print ("Aantal metingen: %d" % len(m))
powerof2 = len(m[0])-1
print ("Power of 2: %d" % powerof2)

i = 0
gamma = 0
epsilon = 0
espilon_s = ""
gamma_s = ""
for i in range(0, len(x)):
    one = 0
    zero = 0
    for x in m:
        if x[i] == '0':
            zero += 1
        elif x[i] == '1':
            one += 1
        else:
            print ("geen 0 of 1")

    if one < zero:
        epsilon += pow(2, powerof2 -1- i)
        espilon_s += "1"
        gamma_s += "0"
    elif one > zero:
        espilon_s += "0"
        gamma_s += "1"
        gamma +=  pow(2, powerof2-1- i )
    else:
        print("Hmmm, that should not happen!")

print ("epsilon: %d"% epsilon)
print ("epsilon string")
print (espilon_s)
print ("gamma  : %d"% gamma)
print ("gamma string")
print (gamma_s)
print ("power consumption: %d"% (gamma * epsilon))
f.close()