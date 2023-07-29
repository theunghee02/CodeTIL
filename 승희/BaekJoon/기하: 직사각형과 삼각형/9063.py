import sys
N = int(sys.stdin.readline().rstrip())
xli = []
yli = []
for i in range(N) :
    x,y = map(int, sys.stdin.readline().rstrip().split())
    xli.append(x)
    yli.append(y)
width = max(xli) - min(xli)
length = max(yli) - min(yli)
print(width * length)