import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
queue = deque()
for _ in range(N) :
    inList = list(map(str, sys.stdin.readline().rstrip().split()))
    if inList[0] == 'push' :
        queue.append(inList[1])
    elif inList[0] == 'pop' :
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue.popleft())
    elif inList[0] == 'size' :
        print(len(queue))
    elif inList[0] == 'empty':
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    elif inList[0] == 'front':
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[0])
    elif inList[0] == 'back':
        if len(queue) == 0 :
            print(-1)
        else :
            print(queue[-1])