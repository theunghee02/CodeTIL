import sys
N, k = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort(reverse=True)
print(array[k-1])