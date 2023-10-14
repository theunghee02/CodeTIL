n = int(input())
time = [0] * n
pay = [0] * n

for i in range(n):
    time[i], pay[i] = map(int, input().split())

max_profit = 0

def backtrack(day, current_profit):
    global max_profit
    if day == n:
        max_profit = max(max_profit, current_profit)
        return

    # If we don't take the job on the current day
    backtrack(day + 1, current_profit)

    # If we take the job on the current day, check if it fits within the time frame
    if day + time[day] <= n:
        backtrack(day + time[day], current_profit + pay[day])

backtrack(0, 0)
print(max_profit)