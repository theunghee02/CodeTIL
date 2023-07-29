import sys
S = sys.stdin.readline().rstrip()
result = int(S[0])
for i in range(1,len(S)) :
    result = result*int(S[int(i)]) if result*int(S[int(i)]) > result+int(S[int(i)]) else result+int(S[int(i)])
print(result)