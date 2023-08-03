import sys
a1, a0 = map(int,sys.stdin.readline().rstrip().split())
c = int(sys.stdin.readline().rstrip())
n0 = int(sys.stdin.readline().rstrip())

n = n0
fn = a1*n + a0
gn = n
if fn <= c*gn and a1 <= c:
    print(1)
else :
    print(0)