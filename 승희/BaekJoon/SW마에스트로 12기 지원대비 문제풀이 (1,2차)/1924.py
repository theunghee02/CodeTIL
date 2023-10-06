import sys
x,y = map(int, sys.stdin.readline().split())
day = 0
monList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dayList = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(x-1) :
    day = day + monList[i]
day = (day + y) % 7

print(dayList[day])