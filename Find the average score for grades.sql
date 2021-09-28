-- Find the average score for grades A, B, and C.
-- Output the results along with the corresponding grade (ex: 'A', avg(score)).

SELECT grade, avg(score) average_score

  FROM los_angeles_restaurant_health_inspections
  
 GROUP BY grade;
 
 
