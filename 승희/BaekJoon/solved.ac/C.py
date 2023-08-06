import sys
T = int(sys.stdin.readline().rstrip())
sum = 0
cnt = 0
for i in range(T) :
    N = int(sys.stdin.readline().rstrip())
    array = map(int, sys.stdin.readline().rstrip().split())
    for k in array :
        if k >= 0 : # 양수
            sum += k
        else :
            cnt += 1
    print(i, sum, cnt)
    if sum > cnt :
        print("YES")
    else :
        print("NO")
    sum = 0
    cnt = 0