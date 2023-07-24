import sys
li = []
row = 0
col = 0
high = 0
for i in range(9) :
    li.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(9) :
        if li[i][j] > high :
            high = li[i][j]
            row = i
            col = j
print(high)
print(row+1, col+1)
