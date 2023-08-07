import sys
N = int(sys.stdin.readline().rstrip())
Sarray = []
Aarray = []
index = 0
for i in range(N) :
    Si = input()
    if Si == '?' :
        index = i
    Sarray.append(Si)

M = int(sys.stdin.readline().rstrip())
for j in range(M) :
    Ai = input()
    Aarray.append(Ai)

if N == 1 :
    print(Aarray[0])
elif index == 0 :
    e = Sarray[index + 1][0]
    for l in Aarray :
        if l[-1] == e and l not in Sarray:
            print(l)
elif index == N-1 :
    s = Sarray[index - 1][-1]
    for l in Aarray :
        if l[0] == s and l not in Sarray:
            print(l)
else :
    s = Sarray[index-1][-1]
    e = Sarray[index+1][0]
    for l in Aarray :
        if l[0] == s and l[-1] == e and l not in Sarray :
            print(l)