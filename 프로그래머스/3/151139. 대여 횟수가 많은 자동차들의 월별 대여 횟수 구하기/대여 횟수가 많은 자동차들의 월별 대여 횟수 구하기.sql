-- 코드를 입력하세요
select month(start_date) as month, car_id, count(*) as records
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
where month(start_date) between '8' and '10' and car_id in (select car_id
                from CAR_RENTAL_COMPANY_RENTAL_HISTORY
                where month(start_date) between '8' and '10'
                group by car_id
                having count(car_id) >= 5)
group by month(start_date), car_id
having records > 0
order by 1,2 desc