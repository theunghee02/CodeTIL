import sys
str = sys.stdin.readline().rstrip()
result = []
for i in range(len(str)) :
    for j in range(1,len(str)+1) :
        result.append(str[i:i+j])
result = set(result)
print(len(result))