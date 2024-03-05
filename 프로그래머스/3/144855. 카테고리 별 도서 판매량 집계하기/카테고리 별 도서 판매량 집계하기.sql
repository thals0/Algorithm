-- 코드를 입력하세요

select category, sum(sales) as total_sales
from book b join book_sales s
on b.book_id= s.book_id
WHERE to_char(SALES_DATE, 'yyyy-mm-dd') like '2022-01%'
group by category
order by 1