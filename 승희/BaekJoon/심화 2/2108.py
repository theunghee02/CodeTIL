import sys
N = int(sys.stdin.readline().rstrip())
arr = []
dict = {}
total = 0

for _ in range(N) :
    a = int(sys.stdin.readline().rstrip())
    arr.append(a)
    if a in dict :
        dict[a] += 1
    else :
        dict[a] = 1
    total += a

# 산술평균
print(round(total / N))

# 중앙값
arr.sort()
print(arr[(N-1)//2])

# 최빈값
if N == 1 :
    print(arr[0])
else :
    sorDic = sorted(dict.items(), key=lambda x: (-x[1],x[0]))
    if sorDic[0][1] == sorDic[1][1] :
        print(sorDic[1][0])
    else :
        print(sorDic[0][0])

# 범위
print(max(arr) - min(arr))