-- 코드를 작성해주세요
select count(*) as fish_count
from fish_info i
join (select * from fish_name_info where fish_name = 'BASS' or fish_name = 'SNAPPER') n on i.fish_type = n.fish_type