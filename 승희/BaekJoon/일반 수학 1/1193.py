import sys
n = int(sys.stdin.readline().rstrip())
line = 0
end = 0
while n > end :
    line += 1
    end += line

diff = end - n
if line % 2 == 0 : #짝수 라인
    numerator = line - diff
    denominator = diff + 1
else :
    numerator = diff + 1
    denominator = line - diff

print(f"{numerator}/{denominator}" )
