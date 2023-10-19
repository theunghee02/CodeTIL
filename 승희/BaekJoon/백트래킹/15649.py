import sys
from itertools import permutations
n,m = map(int, sys.stdin.readline().rstrip().split())
arr = [i for i in range(1,n+1)]
result = sorted(list(permutations(arr,m)))
for i in result :
    print(*i)