import sys
N = int(sys.stdin.readline().rstrip())
Sarray = []
Aarray = []
index = 0
for i in range(N) :
    Si = sys.stdin.readline().rstrip()
    if Si == '?' :
        index = i
    Sarray.append(Si)

M = int(sys.stdin.readline().rstrip())
for j in range(M) :
    Ai = sys.stdin.readline().rstrip()
    Aarray.append(Ai)

if index == 0 :
    e = Sarray[index + 1][0]
    for l in range(len(Aarray)):
        if Aarray[l][-1] == e and Aarray[l] not in Sarray:
            print(Aarray[l])
elif index == len(Sarray)-1 :
    s = Sarray[index - 1][-1]
    for l in range(len(Aarray)):
        if Aarray[l][0] == s and Aarray[l] not in Sarray:
            print(Aarray[l])
else :
    s = Sarray[index-1][-1]
    e = Sarray[index+1][0]
    for l in range(len(Aarray)) :
        if Aarray[l][0] == s and Aarray[l][-1] == e and Aarray[l] not in Sarray :
            print(Aarray[l])