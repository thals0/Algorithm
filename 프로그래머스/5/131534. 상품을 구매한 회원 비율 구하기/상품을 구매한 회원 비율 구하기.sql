-- 코드를 입력하세요
# YEAR,MONTH, PUCHASED_USERS, PUCHASED_RATIO
# count(*), count(*)/(SELECT count(*) from USER_INFO where JOINED like '2021%')
select year(SALES_DATE), month(SALES_DATE), count(*), round(count(*)/(SELECT count(*) from USER_INFO where JOINED like '2021%'),1)
from(
select *
from ONLINE_SALE
where user_id in (SELECT user_id from USER_INFO where JOINED like '2021%')
group by user_id, year(SALES_DATE), month(SALES_DATE)) s
group by year(SALES_DATE), month(SALES_DATE)
order by 1,2

