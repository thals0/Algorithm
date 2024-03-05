-- 코드를 작성해주세요
SELECT year(ym) as year, 
round(sum(pm_val1)/count(*),2) as 'pm10', 
round(sum(pm_val2)/count(*),2) as 'pm2.5'
from AIR_POLLUTION
where LOCATION2 = '수원'
group by year(ym)
order by 1