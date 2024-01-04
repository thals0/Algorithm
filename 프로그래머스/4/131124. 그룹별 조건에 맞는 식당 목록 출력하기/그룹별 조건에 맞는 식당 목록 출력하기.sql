-- 코드를 입력하세요
select member_name, review_text, date_format(review_date, '%Y-%m-%d') as review_date
from MEMBER_PROFILE m join
(select * from rest_review where member_id = (select member_id from REST_REVIEW group by MEMBER_ID order by count(*) desc limit 1)) r
on m.member_id = r.member_id
order by review_date, review_text