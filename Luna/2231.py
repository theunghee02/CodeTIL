def d(n):
    total = n
    while(n>0):
        total += n%10
        n=n//10
    return total

N = int(input())
for i in range(1, N+1):
    result = d(i)
    if(result == N):
        print(i)
        break
    elif(i == N): print(0)

