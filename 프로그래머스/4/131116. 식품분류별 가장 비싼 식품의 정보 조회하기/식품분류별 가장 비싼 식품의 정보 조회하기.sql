select m.category, price as max_price, p.product_name 
from food_product p
join (select category, max(price) as max_price from food_product
    group by category 
    having category in ('과자', '국', '김치', '식용유')) m
on p.category = m.category and p.price = m.max_price
order by 2 desc
