N = int(input())
for i in range(N):
    line = input()
    sum = 0
    cnt = 0
    for j in line:
        if j == 'O':
            cnt += 1
            sum += cnt
        else : cnt = 0
    print(sum)
    sum = 0
    cnt = 0
    