#itsmeagoose
#2021

puzzel = open('2021day5.txt','r').read().splitlines()
grid = [[0]*1000 for i in range(1000)]

same = 0

for i in puzzel:
    end = i.split("->")[1]
    start = i.split("->")[0]
    endX = int(end.split(",")[0])
    endY = int(end.split(",")[1])
    startX = int(start.split(",")[0])
    startY = int(start.split(",")[1])
    smallerX = 0
    smallerY = 0
    largeX = 0
    largeY = 0
    if endX == startX or endY == startY:
        if endX == startX and endY != startY:
            if endY > startY:
                while startY <= endY:
                    if grid[endX][startY] == 0:
                        grid[endX][startY] = 1
                    elif grid[endX][startY] == 1:
                        grid[endX][startY] = 2
                        same += 1
                    startY += 1
            else:
                while endY <= startY:
                    if grid[endX][endY] == 0:
                        grid[endX][endY] = 1
                    elif grid[endX][endY] == 1:
                        grid[endX][endY] = 2
                        same += 1
                    endY += 1
        else:
            if endX > startX:
                while startX <= endX:
                    if grid[startX][startY] == 0:
                        grid[startX][startY] = 1
                    elif grid[startX][startY] == 1:
                        grid[startX][startY] = 2
                        same += 1
                    startX += 1
            else:
                while endX <= startX:
                    if grid[endX][endY] == 0:
                        grid[endX][endY] = 1
                    elif grid[endX][endY] == 1:
                        grid[endX][endY] = 2
                        same += 1
                    endX += 1
    else:
        while startX != endX:
            if grid[startX][startY] == 0:
                grid[startX][startY] = 1
            elif grid[startX][startY] == 1:
                grid[startX][startY] = 2
                same += 1
            if startX < endX:
                startX += 1
            elif startX > endX:
                startX -= 1
            if startY < endY:
                startY += 1
            elif startY > endY:
                startY -= 1
        if startX == endX:
            if grid[startX][startY] == 0:
                grid[startX][startY] = 1
            elif grid[startX][startY] == 1:
                grid[startX][startY] = 2
                same += 1
            
print(same)
