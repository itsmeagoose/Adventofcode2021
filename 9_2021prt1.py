#itsmeagoose
#2021

puzzel = open('2021day9.txt','r').read().splitlines()
grid = []

c = 0
count = 0
ans = 0
x = 0
y = 0
s = len(puzzel) - 1
g = len(puzzel[c]) - 1
current = 0
smaller = 0
answers = []

for i in puzzel:
    puzzel[c] = list(puzzel[c])
    c += 1
    
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
            answers.append([x,y])
            ans += 1
        x += 1
    x = 0
    y += 1
print(ans, answers)
    
            
    
            
            



        
