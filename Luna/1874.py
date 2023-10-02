n = int(input())
now = 1 # 오름차순으로 push해줘야 하기 때문에 필요
stack = []
oper = [] # 연산자들 출력
answer = True
for i in range(n):
    num = int(input())
    while now <= num:
        stack.append(now)
        oper.append("+")
        now+=1
    ## 스택 꺼내기
    if stack[-1] == num:
        stack.pop()
        oper.append("-")
    ## 스택을 꺼냈을때 num과 같지 않은 경우
    else :
        print("NO") 
        answer = False
        break
if answer == True:
    for i in oper:
        print(i)