puzzel = open('2021day2.txt','r').read().splitlines()
x = 0
y = 0
for i in puzzel:
    i = i.split(" ")
    if i[0] == "up":
        y -= int(i[1])
    elif i[0] == "down":
        y += int(i[1])
    elif i[0] == "forward":
        x += int(i[1])
print(x * y)
