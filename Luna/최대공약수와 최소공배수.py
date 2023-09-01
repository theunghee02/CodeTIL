##최대공약수
def GCD(x,y):
    while(y):
        ##나누어떨어지지 않을 경우 - 최대 공약수 못찾음
        if y>x:
            x,y = y,x
        if x%y == 0:
            return y
        else : return GCD(y, x%y)
def LCM(x,y):
    result = (x*y) // GCD(x,y)
    return result

def solution(x,y):
    answer = []
    answer.append(GCD(x,y))
    answer.append(LCM(x,y))
    return answer