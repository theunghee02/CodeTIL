import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
deq = deque()
for _ in range(N) :
    inp = list(map(int, sys.stdin.readline().rstrip().split()))
    if inp[0] == 1 :
        deq.appendleft(inp[1])
    elif inp[0] == 2 :
        deq.append(inp[1])
    elif inp[0] == 3 :
        if len(deq) != 0 :
            print(deq.popleft())
        else :
            print(-1)
    elif inp[0] == 4 :
        if len(deq) != 0 :
            print(deq.pop())
        else :
            print(-1)
    elif inp[0] == 5 :
        print(len(deq))
    elif inp[0] == 6 :
        if len(deq) == 0 :
            print(1)
        else :
            print(0)
    elif inp[0] == 7 :
        if len(deq) != 0 :
            print(deq[0])
        else :
            print(-1)
    elif inp[0] == 8 :
        if len(deq) != 0 :
            print(deq[-1])
        else :
            print(-1)