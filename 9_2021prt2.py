#itsmeagoose
#2021

puzzel = open('2021day9.txt','r').read().splitlines()
grid = []
basins = []
more = []
c = 0
count = 0
ans = 0
x = 0
y = 0
s = len(puzzel) - 1
g = len(puzzel[c]) - 1
current = 0
smaller = 0

for i in puzzel:
    puzzel[c] = list(puzzel[c])
    c += 1

def basin(x, y, listing):
    global basins
    if int(puzzel[y][x]) != int(9):
        if (x,y) not in listing:
            if x < g:
                listing.add((x,y))
                basin(x + 1, y, listing)
            if x > 0:
                listing.add((x,y))
                basin(x - 1, y, listing)
            if y < s:
                listing.add((x,y))
                basin(x, y + 1, listing)
            if y > 0:
                listing.add((x,y))
                basin(x, y - 1, listing)
    else:
        basins = listing
for k in puzzel:
    for l in k:
        current = puzzel[y][x]
        grid = []
        if x > 0:
            grid.append(puzzel[y][x - 1])
        if y > 0:
            grid.append(puzzel[y - 1][x])
        if x < g:
            grid.append(puzzel[y][x + 1])
        if y < s:
            grid.append(puzzel[y + 1][x])
        smaller = 0
        count = 0
        for m in grid:
            if int(current) < int(grid[count]):
                pass
            else:
                smaller += 1
            count += 1
        if smaller == 0:
            ans += int(current)
            basinsize = 0
            a = True
            b = True
            c = True
            d = True
            basins = set()
            basin(x, y, basins)
            more.append(len(basins))
            ans += 1
        x += 1
    x = 0
    y += 1
more.sort()
print(more)
hello = (more[-3:])
print(more[-3:])
print(hello[0] * hello[1] * hello[2])
    
            
    
            
            



        
