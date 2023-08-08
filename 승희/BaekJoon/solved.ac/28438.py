import sys
N,M,Q = map(int, sys.stdin.readline().rstrip().split())
R = [0] * N
C = [0] * M
for _ in range(Q) :
    num, rc, v = map(int, sys.stdin.readline().rstrip().split())
    if num == 1 :
        R[rc-1] += v
    elif num == 2 :
        C[rc-1] += v

for i in range(N) :
    for j in range(M) :
        print(R[i] + C[j], end=" ")
    print()