-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, date_format(OUT_DATE, '%Y-%m-%d'), 
case when date_format(OUT_DATE, '%m') < 5 then '출고완료'
    when OUT_DATE like '2022-05-01%' then '출고완료'
    when OUT_DATE is null then '출고미정'
    else '출고대기'
end as 출고여부
FROM FOOD_ORDER
order by ORDER_ID
