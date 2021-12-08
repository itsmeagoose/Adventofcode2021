puzzel = open('2021day6.txt','r').read().splitlines()
fishes = puzzel[0]
fishes = fishes.split(",")
m = 0
days = 0
while days < 256:
    for i in fishes:
        fishes[m] = int(fishes[m])
        fishes[m] -= 1
        if int(fishes[m]) == -1:
            fishes.append(int(9))
            fishes[m] = int(6)
        m += 1
    m = 0
    days += 1
print(len(fishes))
