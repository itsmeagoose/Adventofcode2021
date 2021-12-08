puzzel = open('2021day7.txt','r').read().splitlines()
crabs = puzzel[0].split(",")
fuelreq = 13242357675866
fuel = 0
go_to = 0
n = 0
while go_to < 1000:
    fuel = 0
    for i in crabs:
        i = int(i)
        n = 0
        if go_to < i:
            while go_to != i:
                n += 1
                i -= 1
                fuel += n
        else:
            while go_to != i:
                n += 1
                i += 1
                fuel += n
    if fuel < fuelreq:
        fuelreq = fuel
    go_to += 1
    print(go_to)
    n = 0
print(fuelreq)
            
