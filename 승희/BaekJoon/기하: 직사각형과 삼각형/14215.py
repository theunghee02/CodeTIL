import sys
a,b,c = map(int, sys.stdin.readline().rstrip().split())
x = max(a,b,c)
other = a+b+c-x
if x < other :
    print(a+b+c)
else :
    print(other*2-1)