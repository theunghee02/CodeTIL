import sys
import math
N = int(sys.stdin.readline().rstrip())
arr = []
before = int(sys.stdin.readline().rstrip())
for i in range(N-1) :
    now = int(sys.stdin.readline().rstrip())
    arr.append(now - before)
    before = now

allG = arr[0]
for j in range(1, len(arr)) :
    allG = math.gcd(allG, arr[j])

result = 0
for k in arr :
    result += k // allG - 1
print(result)