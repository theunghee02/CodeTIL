import sys
N = int(sys.stdin.readline().rstrip())
array = []
sum = 0
array = list(map(int, sys.stdin.readline().rstrip().split()))
minority = []
for i in range(N) :
    for j in range(1, array[i]):
        if array[i] % j == 0:
            minority.append(j)
    if len(minority) == 1 :
        sum += 1
    minority = []
print(sum)