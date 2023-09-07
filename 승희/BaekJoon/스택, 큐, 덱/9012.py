import sys
T = int(sys.stdin.readline().rstrip())
for _ in range(T) :
    bracket = sys.stdin.readline().rstrip()
    stack = []
    for i in bracket :
        if len(stack) > 0 and stack[-1] == '(' and i == ')' :
            stack.pop()
        else :
            stack.append(i)
    if len(stack) == 0 :
        print('YES')
    else :
        print('NO')