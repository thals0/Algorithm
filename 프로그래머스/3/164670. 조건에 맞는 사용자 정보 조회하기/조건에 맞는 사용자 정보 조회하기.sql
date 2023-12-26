-- 코드를 입력하세요
SELECT USER_ID, nickname
, CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS 전체주소
, CONCAT(SUBSTRING(TLNO, 1, 3), '-', SUBSTRING(TLNO, 4, 4), '-', SUBSTRING(TLNO, 8)) AS 전화번호
from USED_GOODS_USER
where USER_ID in (select WRITER_ID from USED_GOODS_BOARD group by WRITER_ID having count(*) >= 3)
order by USER_ID desc