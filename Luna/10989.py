N = int(input())
arr = [0 for _ in range(1000)]
for _ in range(N):
    inputs = int(input())
    arr[inputs] +=1
    
for i in range(N):
    if(arr[i]!=0):
        for j in range(arr[i]):
            print(i)
