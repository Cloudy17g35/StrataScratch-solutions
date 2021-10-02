-- Find the total number of inspections with low risk in 2017.


SELECT EXTRACT(YEAR FROM activity_date) as year, 
                COUNT(serial_number) frequency
  FROM los_angeles_restaurant_health_inspections
 WHERE  EXTRACT (YEAR FROM activity_date) = 2017 
        AND (pe_description LIKE '%LOW RISK%')
 GROUP BY year
;
