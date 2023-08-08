def solution(array, n):
    answer = 0
    for i in array:
        if n == array[i] : answer +=1
    return answer

solution([0,2,3,4], 1)