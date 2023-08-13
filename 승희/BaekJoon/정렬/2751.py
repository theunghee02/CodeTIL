import sys
N = int(sys.stdin.readline().rstrip())
array = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
array.sort()
for i in array :
    print(i)