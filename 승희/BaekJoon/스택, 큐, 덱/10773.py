import sys
k = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(k) :
    i = int(sys.stdin.readline().rstrip())
    if i != 0 :
        stack.append(i)
    else :
        stack.pop()
print(sum(stack))