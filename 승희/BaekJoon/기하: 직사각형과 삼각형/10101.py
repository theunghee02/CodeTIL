import sys
sum = 0
triangle = []
for i in range(3) :
    gak = int(sys.stdin.readline().rstrip())
    sum += gak
    triangle.append(gak)

if sum != 180 :
    print("Error")
else :
    if triangle[0] == triangle[1] or triangle[1] == triangle[2] or triangle[2] == triangle[0] :
        if triangle[0] == 60 and triangle[1] == 60 :
            stat = print("Equilateral")
        else :
            print("Isosceles")
    else :
        print("Scalene")