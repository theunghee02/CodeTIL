from collections import deque
N = int(input())
deq = deque(enumerate(map(int, input().split())))
res = []

while deq :
    idx, paper = deq.popleft()
    res.append(idx+1)

    if paper > 0 :
        deq.rotate(-(paper - 1))
    elif paper < 0 :
        deq.rotate(-paper) #paper 자체가 음수이기 때문에 오른쪽으로 돌려면 양수로 만들어야 함

print(*res)