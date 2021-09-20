--Write a query that calculates the difference between the highest salaries 
--found in the marketing and engineering departments. Output just the difference in salaries.
--Tables: db_employee, db_dept

SELECT

(SELECT MAX(salary)
   FROM db_employee
  INNER JOIN db_dept
     ON db_employee.department_id = db_dept.id
   WHERE department = 'marketing')

-

(SELECT MAX(salary)
  FROM db_employee
 INNER JOIN db_dept
    ON db_employee.department_id = db_dept.id
WHERE department = 'engineering') AS diff;
