x, y, a = map(int, input().split())
z=  x **y
print(f"내가 계산한 {x}의 {y}의 지수 결과값은 {z}이며 실제 {a}와 비교 시 동일 여부는 {a == z}이다.")