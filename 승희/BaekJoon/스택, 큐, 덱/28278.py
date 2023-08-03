import sys
N = int(sys.stdin.readline().rstrip())
line = []
stack = []
for i in range(N) :
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    if line[0] == 1 :
        stack.append(line[1])
    elif line[0] == 2 :
        print(stack.pop() if len(stack) > 0 else -1)
    elif line[0] == 3 :
        print(len(stack))
    elif line[0] == 4:
        print(0 if len(stack) > 0 else 1)
    elif line[0] == 5:
        print(stack[-1] if len(stack) > 0 else -1)