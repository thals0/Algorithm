-- 코드를 입력하세요
SELECT MEMBER_ID, member_name, gender, DATE_FORMAT(date_of_birth, '%Y-%m-%d') as date_of_birth
from MEMBER_PROFILE
where GENDER = 'W' and DATE_OF_BIRTH like '%-03-%' and tlno is not null
order by member_id 