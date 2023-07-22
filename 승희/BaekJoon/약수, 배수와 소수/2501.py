import sys
N,K = map(int, sys.stdin.readline().rstrip().split())
nli = []
for i in range(1,N+1) :
    if N % i == 0 :
        nli.append(i)
if len(nli) >= K :
    print(nli[K-1])
else :
    print(0)