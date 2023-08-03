-- https://school.programmers.co.kr/learn/courses/30/lessons/144853
SELECT BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문' and date_format(PUBLISHED_DATE, '%Y') = '2021'
ORDER BY PUBLISHED_DATE;