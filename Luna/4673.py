## 셀프넘버가 아닌수
def d(n):
    total = n
    while(n>0):
        total += n%10
        n = n//10
    return total

## 메인
arr = [0] * 10001
result = 0
for i in range(1, 10001):
    result = d(i)
    ## result = 생성할 수 있는 값
    if(result <10001):
        arr[result] = 1
for i in range(1, 10001):
    if(arr[i]!= 1) : print(i)