import sys
li = [[0 for _ in range(100)] for _ in range(100)]
res = 0

n = int(sys.stdin.readline().rstrip())
for _ in range(n) :
    x, y = list(map(int, sys.stdin.readline().rstrip().split()))
    for row in range(x,x+10) :
        for col in range(y,y+10) :
            li[row][col] = 1


for i in li :
    res += i.count(1)
print(res)