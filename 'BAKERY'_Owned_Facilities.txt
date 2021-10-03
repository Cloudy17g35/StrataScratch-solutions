--   Find the owner_name and the pe_description of facilities owned by 'BAKERY' where low-risk cases have been reported.

SELECT owner_name, pe_description 
  FROM los_angeles_restaurant_health_inspections
 WHERE pe_description like '%LOW RISK%' 
   AND owner_name like '%BAKERY%';
