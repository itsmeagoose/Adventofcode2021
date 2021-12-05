#itsmeagoose
#2021

puzzel = open('2021day4.txt','r').read().splitlines()

instructions = puzzel[0]
instructions = instructions.split(",")
del puzzel[0]

j = 1
c = 0
count = 0
runs = 0

for i in puzzel:
    i = str(i)
    puzzel[c] = i.split()
    c += 1

for draws in instructions:
    while j <= len(puzzel):
        board = [puzzel[j], puzzel[j+1], puzzel[j+2], puzzel[j+3], puzzel[j+4]]
        for lines in board:
            for nbrs in lines:
                if draws == nbrs:
                    lines[count] = "X"
                if lines.count("X") == 5:
                    print(nbrs, board)
                count += 1
            count = 0
            while runs < 5:
                #print((board[0])[runs])
                if (board[0])[runs] == "X":
                    if (board[1])[runs] == "X" and (board[2])[runs] == "X" and (board[3])[runs] == "X" and (board[4])[runs] == "X":
                        print(board)
                runs += 1
            runs = 0
            #print(board, lines, nbrs)
        j += 6
    j = 1
print("oh no")


