# this is ONLY part 2 of day 1
puzzel = open('2021day1.txt','r').read().splitlines()
m = 0
n = 0
a = 0
b = 1
c = 2
d = 3
count = 0
run = False
increses = 0
while d < len(puzzel):
    # this defines the variable and the previous variable
    m = (int(puzzel[a]) + int(puzzel[b]) + int(puzzel[c]))
    n = (int(puzzel[b]) + int(puzzel[c]) + int(puzzel[d]))
    if n > m:
        increses += 1
        #print(m, n)
    else:
        print(m, n)
    a += 1
    b += 1
    c += 1
    d += 1
print(increses)
