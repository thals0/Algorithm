select car_id, cr.car_type, round(daily_fee * (1-discount_rate/100) * 30) as fee
from (select car_id, car_type, daily_fee
        from CAR_RENTAL_COMPANY_CAR 
        where CAR_TYPE in ('SUV', '세단') and 
        car_id not in (select car_id FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY where date_format(end_date, '%Y-%m-%d') > '2022-11-01')) cr 
join (select * from CAR_RENTAL_COMPANY_DISCOUNT_PLAN 
            where DURATION_TYPE = '30일 이상') p
on cr.CAR_TYPE = p.CAR_TYPE
group by car_id
having fee between 500000 and 2000000
order by 3 desc, 2, 1 desc