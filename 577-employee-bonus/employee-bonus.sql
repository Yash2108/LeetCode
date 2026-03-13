# Write your MySQL query statement below
SELECT name, bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empId = b.empId 
WHERE bonus IS NULL or bonus < 1000