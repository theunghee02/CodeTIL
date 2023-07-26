import sys
xli = []
yli = []
for i in range(3) :
    x,y = map(int, sys.stdin.readline().rstrip().split())
    if x in xli:
        xli.remove(x)
    else:
        xli.append(x)
    if y in yli:
        yli.remove(y)
    else:
        yli.append(y)

print(xli[0], yli[0])