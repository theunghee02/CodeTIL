def make_one(n):
    # n이 1이라면 연산을 아예 하지 않은거임 -> 0출력
    if n==1:
        return 0
    if n%3 == 0:
        result = make_one(n//3)
    if n%2 == 0:
        result =make_one(n//2)
    
    result = make_one(n-1)
n = int(input())
result = make_one(N)
print(result)