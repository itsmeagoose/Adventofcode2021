#itsmeagoose
#2021

puzzel = open('2021day10t.txt','r').read().splitlines()

opened = []
closed = []
no = []
c = 0
m = 0
ded = []

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
                print(opened[len(opened)-1], closed[len(closed)-1])
                no.append(closed[len(closed)-1])
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
                ded.append(i[m])
                
        elif k == "]":
            closed.append("[")
            if closed[len(closed)-1] == opened[len(opened)-1]:
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
            else:
                print(opened[len(opened)-1], closed[len(closed)-1])
                no.append(closed[len(closed)-1])
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
                ded.append(i[m])
                
        elif k == "}":
            closed.append("{")
            if closed[len(closed)-1] == opened[len(opened)-1]:
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
            else:
                print(opened[len(opened)-1], closed[len(closed)-1])
                no.append(closed[len(closed)-1])
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
                ded.append(i[m])
                
        elif k == ")":
            closed.append("(")
            if closed[len(closed)-1] == opened[len(opened)-1]:
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
            else:
                print(opened[len(opened)-1], closed[len(closed)-1])
                no.append(closed[len(closed)-1])
                closed.pop(len(closed)-1)
                opened.pop(len(opened)-1)
                ded.append(i[m])
        m += 1
print(no)
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
print(ans)

    
    
