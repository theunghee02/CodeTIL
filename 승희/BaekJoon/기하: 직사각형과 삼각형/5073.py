import sys
s1, s2, s3 = map(int, sys.stdin.readline().rstrip().split())
while s1 != 0 and s2 != 0 and s3 != 0 :
    if s1 == s2 and s2 == s3 :
        print("Equilateral")
    elif max(s1, s2, s3) >= s1+s2+s3-max(s1, s2, s3) :
        print("Invalid")
    elif (s1 == s2 and s2 != s3) or (s2 == s3 and s1 != s2) or (s1 == s3 and s2 != s3) :
        print("Isosceles")
    else :
        print("Scalene")
    s1, s2, s3 = map(int, sys.stdin.readline().rstrip().split())