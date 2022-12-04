-- Task
-- https://leetcode.com/problems/duplicate-emails/

-- Solution
/* Write your T-SQL query statement below */
select email
from person
group by email
having count(id) > 1