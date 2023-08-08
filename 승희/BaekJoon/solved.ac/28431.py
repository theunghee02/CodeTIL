import sys
array = []
for i in range(5) :
    n = sys.stdin.readline().rstrip()
    if n not in array :
        array.append(n)
    else :
        array.remove(n)
print(*array)