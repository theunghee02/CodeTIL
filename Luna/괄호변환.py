p = "(()())()"
# def divide(p):
## 올바른 괄호 문자열인지 확인
def check(u):
    stack = []
    for bracket in u:
        if bracket == '(':
            stack.append(u)
        else:
            if len(stack) == 0:
                return False
            stack.pop()

def sol(p):
    if len(p)== 0: return ""
    ## "균형잡힌 괄호 문자열" u, v로 분리
    u,v = divide(p)
    ## 올바른 괄호 문자열이라면
    if u == "올바른 괄호 문자열":
        return sol(v) + u
    ##올바른 괄호 문자열이 아니라면
    else:
        answer = '('
        answer += sol(v)
        answer += ')'
        # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 