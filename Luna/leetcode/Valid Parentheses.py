
def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        brackets = {'}': '{', ')':'(', ']': '['}
        for i in s:
            ## { 스택에 넣기
            if i in brackets.values():
                stack.append(i)
            ## } pop 해서 확인
            elif i in brackets.keys():
                # 비교할 대상이 있는지 확인
                if len(stack) == 0:
                     return False
                top_element = stack.pop() # 마지막에 들어간 열린 괄호
                if top_element != brackets[i]: # i라면 } , brackets[i]는 } 의 쌍인 '{'
                    return False
        return len(stack) == 0

print(isValid("()"))