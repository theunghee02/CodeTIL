-- https://school.programmers.co.kr/learn/courses/30/lessons/132204
SELECT a.APNT_NO, p.PT_NAME, p.PT_NO, a.MCDP_CD, d.DR_NAME, a.APNT_YMD
FROM APPOINTMENT a
JOIN PATIENT p ON p.PT_NO = a.PT_NO
JOIN DOCTOR d ON d.DR_ID = a.MDDR_ID
WHERE a.APNT_CNCL_YN = 'N' and a.APNT_YMD LIKE '2022-04-13%' and a.MCDP_CD = 'CS'
ORDER BY a.APNT_YMD;