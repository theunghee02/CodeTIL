-- https://school.programmers.co.kr/learn/courses/30/lessons/59412
SELECT HOUR(DATETIME) as HOUR, COUNT(ANIMAL_ID) as COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR between '9' and '19'
ORDER BY HOUR;