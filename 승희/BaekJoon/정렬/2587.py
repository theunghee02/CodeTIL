def quick_sort(array) :
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_array = [x for x in tail if x <= pivot]
    right_array = [x for x in tail if x > pivot]

    return quick_sort(left_array) + [pivot] + quick_sort(right_array)

import sys
array = []
avg = 0
for _ in range(5) :
    i = int(sys.stdin.readline().rstrip())
    array.append(i)
    avg += i
# 평균
print(avg//5)

array = quick_sort(array)
print(array[2])