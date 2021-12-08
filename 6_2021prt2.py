puzzel = open('2021day6.txt','r').read().splitlines()
fishes = puzzel[0]
fishes = fishes.split(",")
m = 0
l = 0
days = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
zero = 0
middel0 = 0
middel1 = 0
middel2 = 0
middel3 = 0
middel4 = 0
middel5 = 0
middel6 = 0
middel7 = 0
middel8 = 0
for d in fishes:
    fishes[l] = int(fishes[l])
    if fishes[l] == 1:
        one += 1
    elif fishes[l] == 0:
        zero += 1
    elif fishes[l] == 2:
        two += 1
    elif fishes[l] == 3:
        three += 1
    elif fishes[l] == 4:
        four += 1
    elif fishes[l] == 5:
        five += 1
    elif fishes[l] == 6:
        six += 1
    elif fishes[l] == 7:
        seven += 1
    elif fishes[l] == 8:
        eight += 1
    l += 1
while days < 256:
    middel8 += eight
    middel7 += seven
    middel6 += six
    middel5 += five
    middel4 += four
    middel3 += three
    middel2 += two
    middel1 += one
    middel0 += zero
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    zero = 0
    one += middel2
    two += middel3
    three += middel4
    four += middel5
    five += middel6
    six += middel7
    seven += middel8
    zero += middel1
    six += middel0
    eight += middel0
    middel0 = 0
    middel1 = 0
    middel2 = 0
    middel3 = 0
    middel4 = 0
    middel5 = 0
    middel6 = 0
    middel7 = 0
    middel8 = 0
    days += 1
    print(days)
print(one + two + three + four + five + six + seven + eight + zero)
