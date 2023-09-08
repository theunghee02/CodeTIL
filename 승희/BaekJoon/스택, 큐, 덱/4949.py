import sys
string = list(sys.stdin.readline().rstrip())
while string[0] != '.' :
    stack = []
    for i in string :
        if len(stack) > 0 and stack[-1] == '(' and i == ')' :
            stack.pop()
        elif len(stack) > 0 and stack[-1] == '[' and i == ']' :
            stack.pop()
        elif i == '(' or i == '[' or i == ']' or i == ')' :
            stack.append(i)
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')
    string = list(sys.stdin.readline().rstrip())
    stack = []