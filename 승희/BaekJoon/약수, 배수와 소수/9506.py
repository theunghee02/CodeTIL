import sys
n = int(sys.stdin.readline().rstrip())
aliquot = []
sum = 0
while n != -1 :
    for i in range(1,n+1) :
        if n % i == 0 :
            aliquot.append(i)
            if i != n :
                sum += i
    if sum == n :
        print(f"{n} = ", end="")
        for i in aliquot :
            if i == aliquot[-1] :
                break
            if i == aliquot[0] :
                print(f"{i} ", end="")
            else :
                print(f"+ {i} ", end="")
        print()
    else :
        print(f"{n} is NOT perfect.")
    n = int(sys.stdin.readline().rstrip())
    aliquot = []
    sum = 0
