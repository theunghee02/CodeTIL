import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(str, sys.stdin.readline().rstrip().split()))
x,y = 0, 0
for a in A :
    if a == 'R' :
        if y+1 <= N-1 and y+1 > 0 :
            y += 1
    elif a == 'L' :
        if y - 1 <= N-1 and y - 1 > 0:
            y -= 1
    elif a == 'U' :
        if x - 1 <= N-1 and x - 1 > 0:
            x -= 1
    elif a == 'D' :
        if x + 1 <= N-1 and x + 1 > 0:
            x += 1
print(x+1, y+1)