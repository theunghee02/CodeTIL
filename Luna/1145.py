numbers = list(map(int, input().split()))
i = 1

while True:
    cnt = 0  
    for num in numbers:
        if i%num == 0:
            cnt += 1
    if cnt >= 3:
        break
    i += 1

print(i)
