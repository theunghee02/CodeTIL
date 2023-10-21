def fibonacci(n) :
    global res
    f[1] = 1
    f[2] = 1
    for i in range(3,n+1) :
        res += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]


import sys
n = int(sys.stdin.readline().rstrip())
res = 0
f = [0] * (n+1)
print(fibonacci(n), res)