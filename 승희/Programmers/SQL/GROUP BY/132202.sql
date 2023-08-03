-- https://school.programmers.co.kr/learn/courses/30/lessons/132202
SELECT MCDP_CD as '진료과코드', COUNT(MCDP_CD) as '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '%2022-05%'
GROUP BY MCDP_CD
ORDER BY COUNT(MCDP_CD), MCDP_CD;