import sys
n = int(sys.stdin.readline().rstrip())
initial = 1
addition = 6
i = 1

while True :
    if n == 1 :
        break
    elif n > initial and n <= initial + addition :
        i += 1
        break
    else :
        initial += addition
        i += 1
        addition = i * 6
print(i)