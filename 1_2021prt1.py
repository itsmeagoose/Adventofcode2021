puzzel = open('2021day1.txt','r').read().splitlines()
m = 0
a = 0
for i in puzzel:
    i = int(i)
    if i > m:
        a += 1
    m = i
# we need -1 because we dont count the first increse
print(a - 1)
