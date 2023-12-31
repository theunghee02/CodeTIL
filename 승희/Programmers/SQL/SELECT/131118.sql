-- https://school.programmers.co.kr/learn/courses/30/lessons/131118
SELECT i.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(r.REVIEW_SCORE),2) as SCORE
FROM REST_INFO i
JOIN REST_REVIEW r ON i.REST_ID = r.REST_ID
GROUP BY r.REST_ID
HAVING ADDRESS LIKE '%서울시%' or ADDRESS LIKE '%서울특별시%'
ORDER BY SCORE DESC, FAVORITES DESC;