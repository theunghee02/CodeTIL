def solution(a, b):
    answer = 0
    result1 = str(a) + str(b)
    result2 = str(b) + str(a)
    if int(result1) > int(result2): return result1
    else: return result2
print(solution(9,91))