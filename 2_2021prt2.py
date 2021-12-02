puzzel = open('2021day2.txt','r').read().splitlines()
x = 0
y = 0
m = 0
aim = 0
for i in puzzel:
    i = i.split(" ")
    if i[0] == "up":
        #y -= int(i[1])
        aim -= int(i[1])
    elif i[0] == "down":
        #y += int(i[1])
        aim += int(i[1])
    elif i[0] == "forward":
        x += int(i[1])
        m = aim * int(i[1])
        print(aim, i[1], m)
        y += m
    m = 0
print(x * y)
