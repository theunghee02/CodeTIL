N = int(input())
answer = []
for i in range(N):
    num = int(input())
    answer.append(num)

answer.sort()
for x in answer:
    print (x)
