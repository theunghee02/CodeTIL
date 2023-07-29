import sys
M = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())
sum = 0
min = []
minority = []
for i in range(M, N+1) :
    for j in range(1,i) :
        if i % j == 0 :
            minority.append(j)
    if len(minority) == 1 :
        sum += i
        min.append(i)
    minority = []
if len(min) == 0 :
    print(-1)
else :
    print(sum)
    print(min[0])