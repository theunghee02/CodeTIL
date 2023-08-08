import sys
N = int(sys.stdin.readline().rstrip())
array = []
for _ in range(N) :
    array.append(int(sys.stdin.readline().rstrip()))
array.sort()
for i in array :
    print(i)