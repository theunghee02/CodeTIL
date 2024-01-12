import sys
n = int(sys.stdin.readline().rstrip())

A = list(map(int, sys.stdin.readline().rstrip().split())) # 수열 A - 증가하는 부분 수열
reversedA = A[::-1] # 감소하는 부분 수열

increase = [1] * n
decrease = [1] * n

for i in range(n) :
    for j in range(i) :
        if A[i] > A[j] :
            increase[i] = max(increase[i], increase[j]+1)
        if reversedA[i] > reversedA[j] :
            decrease[i] = max(decrease[i], decrease[j]+1)

# 가장 큰 값들을 더해서 빼는 것이 아니라,
# increase, decrease 모두 loop를 다 돌았기 때문에
# 이론상 같은 위치를 더하고 두 번씩 계산했기에 1 빼기
result = [0] * n
for i in range(n) :
    result[i] = increase[i] + decrease[n-i-1] - 1
print(max(result))