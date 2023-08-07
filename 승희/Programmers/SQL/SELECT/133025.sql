-- https://school.programmers.co.kr/learn/courses/30/lessons/133025
SELECT f.FLAVOR
FROM FIRST_HALF as f
JOIN ICECREAM_INFO as i ON f.FLAVOR = i.FLAVOR
WHERE f.TOTAL_ORDER > 3000 and i.INGREDIENT_TYPE = 'fruit_based'
ORDER BY f.TOTAL_ORDER DESC;