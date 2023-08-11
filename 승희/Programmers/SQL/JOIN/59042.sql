-- https://school.programmers.co.kr/learn/courses/30/lessons/59042
SELECT o.ANIMAL_ID, o.NAME
FROM ANIMAL_OUTS o
LEFT OUTER JOIN ANIMAL_INS i ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE i.DATETIME IS NULL;