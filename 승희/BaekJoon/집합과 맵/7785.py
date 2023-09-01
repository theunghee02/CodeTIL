import sys
n = int(sys.stdin.readline().rstrip())
arr = set()
for _ in range(n) :
  name, el = map(str, sys.stdin.readline().rstrip().split())
  if el == 'enter' :
    arr.add(name)
  elif el == 'leave' :
    arr.remove(name)
arr = sorted(arr, reverse=True)
for i in arr :
  print(i)