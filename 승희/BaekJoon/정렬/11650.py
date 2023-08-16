import sys
N = int(sys.stdin.readline().rstrip())
array = []
for _ in range(N) :
    array.append(tuple(map(int,sys.stdin.readline().rstrip().split())))
array.sort()
for i in array :
    print(i[0], i[1])