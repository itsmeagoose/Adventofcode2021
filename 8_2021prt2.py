puzzel = open('2021day8.txt','r').read().splitlines()
epic = open('2021day8.txt','r').read().splitlines()
c = 0
n = 0
total = 0
one = 0
onelet = ""
four = 0
fourlet = ""
seven = 0
eight = 0
current = []
for i in puzzel:
    puzzel[c] = puzzel[c].split("|")
    epic[c] = (puzzel[c])[0]
    puzzel[c] = (puzzel[c])[1]
    puzzel[c] = puzzel[c].split()
    epic[c] = epic[c].split()
    c += 1
c = 0
n = 0
h = 0
g = 0
for l in puzzel:
    current = []
    

    for z in epic[h]:
        if len(z) == 2:
            onelet = z
            onelet.split()
            onelet = list(onelet)


    for y in epic[g]:
        if len(y) == 4:
            fourlet = y
            fourlet.split()
            fourlet = list(fourlet)
        if onelet[0] in fourlet:
            fourlet.remove(onelet[0])
        if onelet[1] in fourlet:
            fourlet.remove(onelet[1])
            

    for m in puzzel[n]:
        if len(m) == 2:
            current.append(1)
        elif len(m) == 3:
            current.append(7)
        elif len(m) == 4:
            current.append(4)
        elif len(m) == 5:
            if onelet[0] in list(m) and onelet[1] in list(m):
                current.append(3)
            elif fourlet[0] in list(m) and fourlet[1] in list(m):
                current.append(5)
            else:
                current.append(2) 
        elif len(m) == 6:
            if onelet[0] not in list(m) or onelet[1] not in list(m):
                current.append(6)
            elif fourlet[0] in list(m) and fourlet[1] in list(m):
                current.append(9)
            else:
                current.append(0)
        elif len(m) == 7:
            current.append(8)
    strings = [str(integer) for integer in current]
    a_string = "".join(strings)
    intgr = int(a_string)
    total += int(intgr)
    print(total)

    n += 1
    h += 1
    c += 1
    g += 1
print(total)
    
