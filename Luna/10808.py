## 문자열
string = input()
## A-Z까지의 리스트
arr = [0] * 26

for i in string:
    arr[ord(i)-97]+=1

for i in arr:
    print(i, end=" ")