def calc_card(card):
    result = 0
    for y in range(0, 5):
        for x in range(0, 5):
            if card[y,x] != -1:
                result += card[y,x]           
    return result
        

def check_bingo(card):
    for x in range(0, 5):
        if card[0,x] == -1 and card[1,x] == -1 and card[2,x] == -1 and card[3,x] == -1 and card[4,x] == -1:
            return True
    for y in range(0, 5):
        if card[y,0] == -1 and card[y,1] == -1 and card[y,2] == -1 and card[y,3] == -1 and card[y,4] == -1:
            return True
    return False


#f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-4/1-1.txt", "r")
# f = open("/Users/Breee02/Documents/GitHub/aoc2021/day-3/test1.txt", "r")
f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-4/4-1.txt", "r")
m=[]
for x in f:
    m = x.split (",")
bingo_numbers=[]
for i in m:
    bingo_numbers.append(int(i))

print ("Aantal bingo nummers: %d" % len(bingo_numbers))

import numpy as np

k = np.zeros((5, 5), dtype=np.int16)

f = open("d:/Users/Robert/Documents/GitHub/Rvdb/AoC2021/aoc2021/day-4/4-2.txt", "r")
m=[]
bingo_cards=[]
ki = 0
y = 0 
for datain in f:
    str = datain.rstrip("\n")
    n = 3
    m = [str[i:i+n] for i in range(0, len(str), n)]
    
    t=[]
    if len(m)==5:
        for i in m:
            t.append(int(i))
    
    if len(t) == 5:
        for x in range(0, 5):
            k[y,x] = t[x]
        y += 1
    else:
        #next card
        bingo_cards.append(k.copy())
        ki += 1
        y = 0

for number in bingo_numbers:
    bingo = False
    b = 0
    for card in bingo_cards:
        #check number off card
        for x in range(0, 5):
            for y in range(0, 5):
                if card[y,x] == number:
                    card[y,x] = -1
    
    for card in bingo_cards:      
        #check bingo on card
        if check_bingo(card):
            bingo = True
            print ("Bingo! on card")
            print (card)
            print ("Bingo number %d" % number)
            print ("Sum of board: %d" % calc_card(card))
            print ("Anwser: %d" % (number * calc_card(card)))
            #remove bingo card from list
            del bingo_cards[b]
            print ("Number of bingo cards left: %d" % len(bingo_cards))
        b += 1
    
    if len(bingo_cards) == 0:
        print("No more bingo cards")
        
    if bingo == False:
        print ("Geen bingo! %d" % number)
            
            

        
