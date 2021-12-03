#itsmeagoose
#2021
puzzel = open('2021day3.txt','r').read().splitlines()


def check_oxygen(nbrs, j):
    common = []
    commen = 1
    for i in nbrs:
        common.append(int(i[j]))
    if common.count(0) > common.count(1):
        commen = 0
        #print(j, nbrs)
    else:
        commen = 1
    new_nbrs = []
    for i in nbrs:
        #print(i[j], j, commen)
        if int(i[j]) == int(commen):
            new_nbrs.append(i)
            #print(len(new_nbrs))
    if len(new_nbrs) == 1:
       print(new_nbrs, "boink")
    else:
        check_oxygen(new_nbrs, j+1)
    common = []
        



def check_co2(nbrs, j):
    common = []
    commen = 1
    for i in nbrs:
        common.append(int(i[j]))
    if common.count(0) > common.count(1):
        commen = 1
        #print(j, nbrs)
    else:
        commen = 0
    new_nbrs = []
    for i in nbrs:
        #print(i[j], j, commen)
        if int(i[j]) == int(commen):
            new_nbrs.append(i)
            #print(len(new_nbrs))
    if len(new_nbrs) == 1:
       print(new_nbrs, "boink")
    else:
        check_co2(new_nbrs, j+1)
    common = []


print(check_oxygen(puzzel, 0))
print(check_co2(puzzel, 0), "boink")


    
