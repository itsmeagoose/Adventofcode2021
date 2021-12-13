#itsmeagoose
#2021
import math

numpaths = 0
puzzel = open('2021day12.txt','r').read().splitlines()
caves = {}
for lines in puzzel:
    gofrom , goto = lines.split("-")
    if gofrom not in caves:
        caves.update({gofrom : [goto]})
    else:
        caves[gofrom].append(goto)
        #print(caves)
    if goto not in caves:
        caves.update({goto : [gofrom]})    
    else:
        caves[goto].append(gofrom)
        #print(caves)

"""while len(travelled) < 11:
    finished = False
    n = 0
    while not finished:
        if caves[path][n].isupper() or caves[path][n] not in travelled:
            travelled.append(path)
            prevpath = path
            path = caves[path][n]
            print(caves[path])
            if "end" in travelled:
                    travelled.remove("end")
            if path == "end" and travelled not in completed:
                print(path, travelled, completed)
                numpaths += 1
                completed.append(travelled)
                print(travelled)
                path = prevpath
            if travelled in completed:
                pass
            travelled = list(dict.fromkeys(travelled))
            finished = True
        else:
            n += 1
            travelled = list(dict.fromkeys(travelled))
print(numpaths, completed)"""

def findpaths(caves, path, travelled, extra):
    if path == "end":
        return 1
    result = 0
    for options in caves[path]:
        if options.isupper() or options not in travelled:
            visit = travelled + [options]
            #visit.extend([options])
            #i dont know why extend doesnt work
            result += findpaths(caves, options, visit, extra)
        elif extra == 1 and options != "start" and options != "end":
            visit = travelled + [options]
            result += findpaths(caves, options, visit, 0)
    return result 
result = findpaths(caves, "start", ["start"], 1)
print(result)


