def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] !=0:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                break
                
            ##stack의 길이는 최소 2개여야됨
            if(len(stack)>1):
                if(stack[-1] == stack[-2]):
                    stack.pop()
                    stack.pop()
                    answer +=2
    return answer


##def solution(board, moves):
    n = len(board)
    stack = []
    answer = 0
    for i in moves:
        for j in range(n):
            value = board[j][i-1]
            if value != 0:
                stack.append(value)
                board[j][i-1] = 0
                break
        if len(stack) >= 2:
            if stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()
                answer += 2         
    return answer