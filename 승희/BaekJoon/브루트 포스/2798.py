import sys
from itertools import combinations
N,M = map(int, sys.stdin.readline().rstrip().split())
black = list(map(int, sys.stdin.readline().rstrip().split()))
result = list(combinations(black,3))

for i in range(len(result)) :
    result[i] = result[i][0] + result[i][1] + result[i][2]

result.sort()
for i in range(len(result)-1,-1,-1) :
    if result[i] > M :
        continue
    else :
        print(result[i])
        break