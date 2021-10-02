-- Find the most common grade earned by bakeries.
-- Order the result based on the number bakeries which earned each grade in descending order.


SELECT COUNT(facility_name) number_of_bakeries, grade
  FROM los_angeles_restaurant_health_inspections
 WHERE facility_name LIKE '%BAKERY%'
 GROUP BY grade
 ORDER BY number_of_bakeries DESC
 LIMIT 1;
