import sys
li = []
for i in range(5) :
    s = sys.stdin.readline().rstrip()
    sli = []
    for j in s :
        sli.append(j)
    li.append(sli)

high = 0
n = 0
for i in range(len(li)) :
    if len(li[i]) > high :
        high = len(li[i])
        n = len(li[i])
        
row = 0
while row < n :
    for i in range(5) :
        if row < len(li[i]) :
            print(li[i][row], end = "")
    row += 1
