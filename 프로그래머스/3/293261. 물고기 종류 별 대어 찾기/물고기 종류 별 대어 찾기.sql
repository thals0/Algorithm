-- 코드를 작성해주세요
select id, fish_name, length
from (select *
from fish_info 
where (fish_type, length) in 
(select fish_type, max(length) from fish_info group by fish_type)) i 
join fish_name_info n on i.fish_type = n.fish_type 
order by id