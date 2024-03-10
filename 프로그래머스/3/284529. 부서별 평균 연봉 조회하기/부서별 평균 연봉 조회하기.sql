-- 코드를 작성해주세요
select j.DEPT_ID, DEPT_NAME_EN, j.AVG_SAL
from HR_DEPARTMENT d
join (select DEPT_ID, round(sum(sal)/count(*)) as AVG_SAL
from HR_EMPLOYEES
group by DEPT_ID) j on d.DEPT_ID = j.DEPT_ID
order by 3 desc