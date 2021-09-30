-- Find employees whose bonus is less than $150.
-- Output the first name along with the corresponding bonus.

SELECT first_name, bonus
  FROM employee
 WHERE bonus < 150;
