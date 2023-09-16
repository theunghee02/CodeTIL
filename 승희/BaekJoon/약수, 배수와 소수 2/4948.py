import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
num = 123456*2
array = [False] + [True for _ in range(num)]
for i in range(2, int(num**0.5)+1) :
    if array[i] == True :
        j = 2
        while i * j <= num :
            array[i*j] = False
            j += 1
while n != 0 :
    for k in range(n+1, n*2+1) :
        if array[k] :
            cnt += 1
    print(cnt)
    n = int(sys.stdin.readline().rstrip())
    cnt = 0