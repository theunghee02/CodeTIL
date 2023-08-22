n = int(input())
## 후위표기식
word = input()
## 피연산자값 저장 리스트
numbers = [0] * n
for i in range(n):
    numbers[i] = int(input())

## 피연산자 스택
stack = []
for ch in word:
    if 'A'<= ch<='Z':
        stack.append(numbers[ord(ch) - ord('A')])
    else:
        top_element = stack.pop()
        result = stack.pop()
        if ch=='+':
            result += top_element
        elif ch== '-':
            result -= top_element
        elif ch == '*':
            result *= top_element
        elif ch =='/':
            result/=top_element
        
        stack.append(result)

print(("{:.2f}".format(result)))