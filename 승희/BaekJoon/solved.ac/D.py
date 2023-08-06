import sys
N = int(sys.stdin.readline().rstrip())
arrayA = list(map(int, sys.stdin.readline().rstrip().split()))
arrayB = list(map(int, sys.stdin.readline().rstrip().split()))

cnt = 0
for i in range(N) :
    for j in range(i+1,N) :
        if min(arrayA[i:j+1]) == min(arrayB[i:j+1]) and max(arrayA[i:j+1]) == max(arrayB[i:j+1]) :
            cnt += 1
print(cnt)