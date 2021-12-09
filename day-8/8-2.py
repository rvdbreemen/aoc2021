#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-8/8-1.txt", "r")
#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-8/test.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-8/8-1.txt", "r")
f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-8/test.txt", "r")
m=[]

specs=[]
numbers=[] 

for x in f:
    #process a single line
    m = x.strip().split("|")
    a = m[0].split()        #split strings into list
    a.sort(key=len)         #sort list by length
    b={}
    for i in a:
        b[len(i)] = set(i)
        specs.append(b)
    numbers=m[1].split()
    
    known_digits = {2: "1", 4: "4", 3: "7", 7: "8"}
    for digit in b:
        match len(digit):
            case 6:
                if len(set(digit).union(cache[4])) == 6:
                    return "9"
                elif len(set(digit).intersection(cache[1])) == 2:
                    return "0"
                else:
                    return "6"
            case 5:
                if len(set(digit).union(cache[1])) == len(set(digit)):
                    return "3"
                elif len(set(digit).union(cache[4])) == 7:
                    return "2"
                else:
                    return "5"
            case other:
                return known[other]    


print("aantal: %d" % len(numbers))

import numpy as np

a = np.zeros((8),  dtype = int)
print(a)

digit_array = np.zeros((7),  dtype = int)
d=[]
for x in astr:
    c=[]
    print(x) 
    for y in x:
        digit=[]
        if len(y) == 2:
            digit = [y,1]
        elif len(y) == 3:
            digit = [y,7]
        elif len(y) == 4:
            digit = [y,4]
        elif len(y) == 7:
            digit = [y,8]
        
        # if len(y) == 5:
        #     # 2 - 3 - 5
            
        # if len(y) == 6:
        #     # 0 - 6 - 9     

        if len(digit)>0:
           c.append(digit)
    d.append(c)
    
for x in bstr:
    for i in range(0, len(x)):
        s = x[i]
        c = len(s)-1
        a[c] += 1
        print(s, c)
    print (x, a)

s = a[1] + a[2] + a[3] + a[6]
print ("Anwser: %d" % (s))
    
    
