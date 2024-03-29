x = input("입력값 1:")
y = input("입력값 2:")
a = input("입력값 3:")
try:
    x = float(x)
    y = float(y)
    a = float(a)
    z = pow(pow(x, y), 1 / a)
except ValueError:
    print("유효하지 않은 숫자 입니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다. 0 이 아닌 다른 값을 입력하시오.")
else : print("x의 y 제곱한 값에 1/a를 제곱한 결과값은", z,"이다.")
