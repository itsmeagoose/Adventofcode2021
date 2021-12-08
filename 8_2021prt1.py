puzzel = open('2021day8.txt','r').read().splitlines()
c = 0
n = 0
one = 0
four = 0
seven = 0
eight = 0
for i in puzzel:
    puzzel[c] = puzzel[c].split("|")
    puzzel[c] = (puzzel[c])[1]
    puzzel[c] = puzzel[c].split()
    c += 1
c = 0
for l in puzzel:
    n = 0
    for m in puzzel[c]:
        if len(m) == 2:
            print(m)
            one += 1
        elif len(m) == 4:
            four += 1
        elif len(m) == 3:
            seven += 1
        elif len(m) == 7:
            eight += 1
    c += 1
print(one + four + seven + eight)
    
