import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
num = list(map(int, sys.stdin.readline().rstrip().split()))
prefix_sum = [0]
temp = 0

for i in num :
    temp += i
    prefix_sum.append(temp)

for _ in range(m) :
    a,b = map(int, sys.stdin.readline().rstrip().split())
    print(prefix_sum[b] - prefix_sum[a-1])