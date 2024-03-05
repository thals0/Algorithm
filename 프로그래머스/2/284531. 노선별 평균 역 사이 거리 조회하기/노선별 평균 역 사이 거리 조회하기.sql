-- 코드를 작성해주세요
select route, 
concat(round(sum(d_between_dist),1),'km') as total_distance, 
concat(round(sum(d_between_dist) / count(*),2),'km') as AVERAGE_DISTANCE
from SUBWAY_DISTANCE
group by route 
order by round(sum(d_between_dist),1) desc