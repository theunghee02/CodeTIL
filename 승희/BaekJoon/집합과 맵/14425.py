# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end) :
  while start <= end :
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target :
      return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target :
      end = mid - 1
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else :
      start = mid + 1
  return None

import sys
N,M = map(int, sys.stdin.readline().rstrip().split())
arr1 = sorted([sys.stdin.readline().rstrip() for _ in range(N)])
arr2 = [sys.stdin.readline().rstrip() for _ in range(M)]
cnt = 0
for i in arr2 :
  result = binary_search(arr1, i, 0, N-1)
  if result != None :
    cnt += 1
print(cnt)