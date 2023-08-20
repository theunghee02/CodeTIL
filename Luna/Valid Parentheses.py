
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
        print(stack)
        for i in stack:
            top_element = stack.pop()
            if top_element != brackets[i]:
                return False
        return True

print(isValid("()"))