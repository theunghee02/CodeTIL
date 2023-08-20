n = int(input())
string = []

for i in range(n):
    string.append(input())

# set으로 변환 (중복 제거) -> 리스트로 
set_string = list(set(string))
print(set_string)

#길이 짧은 순 -> 사전순
set_string.sort()
set_string.sort(key=len)


for i in set_string:
    print(i)