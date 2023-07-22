-- https://school.programmers.co.kr/learn/courses/30/lessons/59034
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') as TLNO
FROM PATIENT
WHERE AGE <= 12 and GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME;