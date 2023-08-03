import sys
N, K = map(int, sys.stdin.readline().rstrip().split())

count = 0
for i in range(N+1) :
    for j in range(60) :
        for k in range(60) :
            if i < 10 or j < 10 or k < 10:
                com = str(i) + str(j) + str(k) + '0'
            else :
                com = str(i) + str(j) + str(k)
            if str(K) in com :
                count += 1
print(count)