-- 코드를 작성해주세요
select id, email, first_name, last_name
from DEVELOPER_INFOS
where SKILL_1 = 'Python' or SKILL_2 = 'Python' or SKILL_3 = 'Python'
order by 1