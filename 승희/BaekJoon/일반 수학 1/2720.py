import sys
t = int(sys.stdin.readline().rstrip())
li = [25, 10, 5, 1]
res = []
j = 0
for i in range(t) :
    c = int(sys.stdin.readline().rstrip())
    for k in li :
        res.append(c // k)
        c = c % k
        j += 1
    for i in res :
        print(i, end=" ")
    print()
    j = 0
    res = []