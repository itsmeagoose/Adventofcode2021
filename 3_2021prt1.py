#itsmeagoose
#2021
puzzel = open('2021day3.txt','r').read().splitlines()
m = []
gamma = []
e = []
o = 0
n = 0
while o <= 11:
    for i in puzzel:
        m.append(int(i[n]))
    if m.count(0) > m.count(1):
        gamma.append(0)
        e.append(1)
    else:
        gamma.append(1)
        e.append(0)
    n += 1
    m = []
    print(e)
    print(gamma)
    o += 1
    
#put through binary calc
gammanum = 2981
enum = 1114
print(enum * gammanum)
