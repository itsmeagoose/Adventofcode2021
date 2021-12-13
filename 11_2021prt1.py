#itsmeagoose
#2021
import math
puzzel = open('2021day11.txt','r').read().splitlines()
epic = open('2021day11.txt','r').read().splitlines()
c = 0
r = 0
grid = []
flashes = 0

for lines in puzzel:
    puzzel[c] = list(puzzel[c])
    for charicters in puzzel[c]:
        puzzel[c][r] = int(puzzel[c][r])
        r += 1
    r = 0
    c += 1
          
runs = 0
while runs != 100:
    c = 0
    r = 0
    for lines in puzzel:
        for charicters in puzzel[c]:
            if puzzel[c][r] < 10:
                puzzel[c][r] += 1
            r += 1
        r = 0
        c += 1
    while any(10 in line for line in puzzel) or any(11 in line for line in puzzel) or any(12 in line for line in puzzel) or any(13 in line for line in puzzel):
        r = 0
        c = 0
    
        for lines in puzzel:
            for charicters in puzzel[c]:
                if puzzel[c][r] > 9:
                    if r + 1 != 10:
                        puzzel[c][r + 1] += 1
                    if c + 1 != 10:
                        puzzel[c + 1][r] += 1
                        
                    if r +1 != 10 and c + 1 != 10:
                        puzzel[c + 1][r + 1] += 1
                        
                    if r - 1 != -1:
                        puzzel[c][r - 1] += 1
                    if c - 1 != -1:
                        puzzel[c - 1][r] += 1
                        
                    if r - 1 != -1 and c - 1 != -1:
                        puzzel[c - 1][r - 1] += 1
                    if r - 1 != -1 and c + 1 != 10:
                        puzzel[c + 1][r - 1] += 1
                    if r + 1 != 10 and c - 1 != -1:
                        puzzel[c - 1][r + 1] += 1
                    puzzel[c][r] = -100
                    flashes += 1
                r += 1
            r = 0
            c += 1
            
    r = 0
    c = 0
    m = 0
    for lines in puzzel:
        for charicters in puzzel[c]:
            if puzzel[c][r] < 0:
                m += 1
                puzzel[c][r] = 0
            r += 1
        r = 0
        c += 1
    
    if m >= 100:
        print(runs)
    runs += 1
print(flashes)
