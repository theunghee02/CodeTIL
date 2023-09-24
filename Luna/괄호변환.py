## 균형잡힌 괄호 문자열 u,v로 분리
def divide(p):
    open_bracket = 0
    end_bracket = 0
    for i in range(len(p)):
        if p[i] =='(': open_bracket +=1
        elif p[i] == ')' : end_bracket +=1
        if open_bracket == end_bracket : 
            u = p[:i+1]
            v = p[i+1:]
            break
    return u,v
            
    
## 올바른 괄호 문자열인지 확인
def check(u):
    stack = []
    for bracket in u:
        if bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

def solution(p):
    if len(p)== 0: return ""
    ## "균형잡힌 괄호 문자열" u, v로 분리
    u,v = divide(p)
    ## 올바른 괄호 문자열이라면
    if check(u):
        return u + solution(v)
    ##올바른 괄호 문자열이 아니라면
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        u = u[1:-1]
        print(u)
        for i in range(1,len(u)-1):
            if u[i] == '(':
                answer+=')'
            else:
                answer+='('
     
        return answer
                
print(solution("()))((()"))