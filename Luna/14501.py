n = int(input())
time = [0] * n
pay = [0] * n
result = []
cache = [0] * n
def func(time, pay, start):
    # 7일을 넘어버리는 경우가 있으니, 인덱스 검사 
    if start >=len(time):
        return 0
    # 캐시를 먼저 확인해서 계산된 적이 있다면
    if cache[start] != 0:
        ## cache hit
        return cache[start]
    ## chache miss
    ret = 0
    for i in range(start, len(time)):
        # 일정이 가능한지 확인
        if i + time[i] -1 <len(time) :
            result = pay[i] + func(time, pay, i + time[i])
            ret = max(ret, result)
    ## 현재 ret을 캐시에 넣기
    cache[start] = ret
    return ret

for i in range(n):
    time[i], pay[i] = map(int, input().split())
print(func(time,pay,0))

# max_profit = 0

# def backtrack(day, current_profit):
#     global max_profit
#     # Base case : 마지막 날짜가 되었을때, Max 값 출력
#     if day == n:
#         max_profit = current_profit
#         return

#     # 선택하지 않는 경우 => 수익은 이동하지 않고, 다음날로 넘어감
#     backtrack(day + 1, current_profit)
#     # 선택하는 경우 
#     if day + time[day] <= n:
#         backtrack(day + time[day], current_profit + pay[day])

# backtrack(0, 0)
# print(max_profit)