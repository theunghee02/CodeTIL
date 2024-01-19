n = 2
arr = [1] * (n+1)
res = []
for i in range(len(arr)):
    arr[i] = bin(i)
for i in range(len(arr)):
    res.append(arr[i].count('1'))
print(res)