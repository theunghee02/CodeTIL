import sys
minList = list(map(int, sys.stdin.readline().rstrip().split()))
minList[2] -= minList[0]
minList[3] -= minList[1]
min = sorted(minList)
print(min[0])