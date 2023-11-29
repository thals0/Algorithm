-- 코드를 입력하세요
select a.FOOD_TYPE, a.REST_ID, a.REST_NAME, a.FAVORITES
from REST_INFO a
inner join (select FOOD_TYPE, MAX(FAVORITES) as FAVORITES from REST_INFO group by FOOD_TYPE) b
on a.FOOD_TYPE = b.FOOD_TYPE and a.FAVORITES = b.FAVORITES
order by FOOD_TYPE desc