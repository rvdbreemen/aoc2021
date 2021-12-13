#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-9/9-1.txt", "r")
#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-9/test.txt", "r")
f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-10/puzzleinput.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-10/test.txt", "r")
#f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-10/test2.txt", "r")

input=[]
for line in f:
    input.append(line.strip())



def puzzel1():
    switcher={
        ")":3,
        "]":57,
        "}":1197,
        ">":25137
    }
        
    result = 0
    for line in input:
        stack=[]
        for i in range(0,len(line)):
            char = line[i]
            left_chars = "([{<"
            right_chars= ")]}>"
            if char in left_chars:
                stack.append(char)
            elif char in right_chars != -1:
                
                if len(stack) == 0:
                    print("does not compute")
                else: 
                    expect_char = stack.pop()
                    if left_chars.index(expect_char) != right_chars.index(char):
                        #error in chunck
                        print ("Syntax error: %s - %d"%(char, switcher.get(char,"fout!")))
                        result += switcher.get(char,"fout!")
                        break
    return result
                        
def puzzel2():
    switcher={
        ")":3,
        "]":57,
        "}":1197,
        ">":25137
    }
    
    result=0
    autocomplete_results = []
    for line in input:
        stack=[]
        for i in range(0,len(line)):
            char = line[i]
            left_chars = "([{<"
            right_chars= ")]}>"
            
            if char in left_chars:
                stack.append(char)
            elif char in right_chars != -1:
                if len(stack) == 0:
                    print("does not compute")
                else: 
                    expect_char = stack.pop()
                    if left_chars.index(expect_char) != right_chars.index(char):
                        #error in chunck, drop the stack
                        print ("Syntax error: %s - %d"%(char, switcher.get(char,"fout!")))
                        stack.clear()
                        break
        if (len(stack) != 0):
            #no chunck error, but there is stuff left on stack, then autocomplete line
            autocomplete_result = 0
            autocomplete_str = "" 
            for i in range(0, len(stack)):
                expect_char = stack.pop()
                autocomplete_result *= 5
                autocomplete_result += left_chars.index(expect_char)+1
                autocomplete_str += right_chars[left_chars.index(expect_char)]
            autocomplete_results.append(autocomplete_result)
            print("Autocomplete result: %s - %d"%(autocomplete_str, autocomplete_result))	
    autocomplete_results.sort()
    center = len(autocomplete_results)//2
    result = autocomplete_results[center]
            
    return result

            
    return result

print("Anwser puzzel 1:", puzzel1())
print("Anwser puzzel 2:", puzzel2())