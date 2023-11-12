-- 코드를 입력하세요
SELECT B.TITLE, B.BOARD_ID, R.REPLY_ID, R.WRITER_ID, R.CONTENTS, DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d')
FROM USED_GOODS_BOARD B LEFT JOIN USED_GOODS_REPLY R
ON B.BOARD_ID = R.BOARD_ID
WHERE B.CREATED_DATE LIKE ('2022-10%') AND REPLY_ID IS NOT NULL
ORDER BY R.CREATED_DATE, B.TITLE