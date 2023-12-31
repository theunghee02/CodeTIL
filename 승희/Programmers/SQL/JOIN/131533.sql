-- https://school.programmers.co.kr/learn/courses/30/lessons/131533
SELECT PRODUCT_CODE, SUM(p.PRICE * SALES_AMOUNT) as SALES
FROM PRODUCT as p
JOIN OFFLINE_SALE as o ON p.PRODUCT_ID = o.PRODUCT_ID
GROUP BY PRODUCT_CODE
ORDER BY SALES DESC, PRODUCT_CODE;