import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
pocket = dict()
reverseP = dict()

for i in range(N) :
    inp = sys.stdin.readline().rstrip()
    pocket[str(i+1)] = inp
    reverseP[inp] = str(i+1)

for j in range(M) :
    question = sys.stdin.readline().rstrip()
    if question.isdigit() :
        print(pocket[question])
    else :
        print(reverseP[question])