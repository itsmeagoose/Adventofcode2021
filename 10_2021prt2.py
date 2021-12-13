#itsmeagoose
#2021
import math
puzzel = open('2021day10.txt','r').read().splitlines()
epic = open('2021day10.txt','r').read().splitlines()
opened = []
closed = []
no = []
c = 0
m = 0
ded = []
prev_no = 0
p = None

for l in puzzel:
    puzzel[c] = list(puzzel[c])
    c += 1
    
for i in puzzel:
    for k in i:
        if k == "<":
            opened.append("<")
        elif k == "[":
            opened.append("[")
        elif k == "{":
            opened.append("{")
        elif k == "(":
            opened.append("(")

        elif k == ">":
            closed.append("<")
            if closed[len(closed)-1] == opened[len(opened)-1]:
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
            else:
                no.append(closed[len(closed)-1])
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)

        elif k == "]":
            closed.append("[")
            if closed[len(closed)-1] == opened[len(opened)-1]:
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
            else:
                no.append(closed[len(closed)-1])
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
                
        elif k == "}":
            closed.append("{")
            if closed[len(closed)-1] == opened[len(opened)-1]:
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
            else:
                no.append(closed[len(closed)-1])
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
                
        elif k == ")":
            closed.append("(")
            if closed[len(closed)-1] == opened[len(opened)-1]:
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
            else:
                no.append(closed[len(closed)-1])
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
    if int(len(no)) > prev_no:
        epic.pop(m)
        prev_no = int(len(no))
        m -= 1
    m += 1
m = 0                        
ans = 0
for h in no:
    if h == "<":
        ans += 25137  
    elif h == "[":
        ans += 57
    elif h == "{":
        ans += 1197
    elif h == "(":
        ans += 3

t = []
for q in epic:
    closed = []
    opened = []
    for w in q:
        if w == "<":
            opened.append("<")
        elif w == "[":
            opened.append("[")
        elif w == "{":
            opened.append("{")
        elif w == "(":
            opened.append("(")

        elif w == ">":
            closed.append("<")
            if closed[len(closed)-1] == opened[len(opened)-1]:
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)


        elif w == "]":
            closed.append("[")
            if closed[len(closed)-1] == opened[len(opened)-1]:
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)

                
        elif w == "}":
            closed.append("{")
            if closed[len(closed)-1] == opened[len(opened)-1]:
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)

                
        elif w == ")":
            closed.append("(")
            if closed[len(closed)-1] == opened[len(opened)-1]:
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)

    score = 0
    opened.reverse()
    for g in opened:
        score = score * 5
        if g == "<":
            score += 4  
        elif g == "[":
            score += 2   
        elif g == "{":
            score += 3
        elif g == "(":
            score += 1
        print(score)
    t.append(score)
print(t)
n = math.ceil(len(t) / 2)
print(n)
print(sorted(t)[-n])
               

        
    

    
    
