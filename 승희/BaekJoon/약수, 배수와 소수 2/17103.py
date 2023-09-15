import sys
N = int(sys.stdin.readline().rstrip())
num = 1000000
array = [True for _ in range(num+1)]
prime = []
for i in range(2, num+1) :
    if array[i] == True :
        prime.append(i)
        j = 2
        while i * j <= num :
            array[i*j] = False
            j += 1
for _ in range(N) :
    even = int(sys.stdin.readline().rstrip())
    cnt = 0
    for k in prime :
        if k >= even :
            break
        if array[even-k] and k <= even-k :
            cnt += 1
    print(cnt)