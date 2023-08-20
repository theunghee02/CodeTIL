def solution(numbers, hand):
    num = { 1 : [0,0], 2 : [0,1], 3 : [0,2],
            4 : [1,0], 5 : [1,1], 6 : [1,2],
            7 : [2,0], 8 : [2,1], 9 : [2,2],
            '*' : [3,0], 0 : [3,1], '#' : [3,2] }
    answer = ''
    right = num['#']
    left = num['*']
    for i in numbers:
        if i in [1,4,7]:
            left = i
            answer += 'L'

        elif i in [3,6,9]:
            right = i
            answer += 'R'

        ### 2,5,8,0 일때
        else:
            ## 거리계산 : x값 + y값
            # 이전 Left와 목표지점의 거리
            newLeft = abs(num[left][0] - num[i][0]) + abs(num[left][1] - num[i][1])
            # 이전 right와 목표지점 거리
            newRight = abs(num[right][0] - num[i][0]) + abs(num[right][1] - num[i][1])

            ## 이전 Left와 목표지점의 거리 - 이전 right와 목표지점 거리 비교
            if newRight < newLeft:
                right = i
                answer += 'R'
            elif newLeft < newRight:
                left = i
                answer += 'L'
            else:
                if hand == 'left':
                    answer +='L'
                    left = i
                else:
                    answer +='R'
                    right = i
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))