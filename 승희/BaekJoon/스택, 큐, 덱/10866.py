import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
deq = deque()
for _ in range(n) :
    string = list(map(str, sys.stdin.readline().rstrip().split()))
    if string[0] == 'pop_back' :
        if len(deq) != 0 :
            print(deq.pop())
        else :
            print(-1)
    elif string[0] == 'pop_front' :
        if len(deq) != 0 :
            print(deq.popleft())
        else :
            print(-1)
    elif string[0] == 'push_front' :
        deq.appendleft(string[1])
    elif string[0] == 'push_back' :
        deq.append(string[1])
    elif string[0] == 'size' :
        print(len(deq))
    elif string[0] == 'empty' :
        if len(deq) == 0 :
            print(1)
        else :
            print(0)
    elif string[0] == 'front' :
        if len(deq) != 0 :
            print(deq[0])
        else :
            print(-1)
    elif string[0] == 'back' :
        if len(deq) != 0 :
            print(deq[-1])
        else :
            print(-1)