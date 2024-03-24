-- 코드를 작성해주세요
select fish_count, fish_name
from fish_name_info n right join 
(select fish_type, count(*) as fish_count from fish_info group by fish_type) i
on n.fish_type = i.fish_type
order by fish_count desc
