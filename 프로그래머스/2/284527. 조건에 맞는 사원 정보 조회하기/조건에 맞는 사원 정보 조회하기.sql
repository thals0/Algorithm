-- 코드를 작성해주세요
select j.score , e.emp_no, emp_name, position, email
                            from hr_employees e 
                            join (select emp_no, sum(score) as score from hr_grade
                                    group by emp_no
                                    order by 2 desc limit 1) 
                            j on e.emp_no = j.emp_no
