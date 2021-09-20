--Find order details made by Jill and Eva.
--Consider the Jill and Eva as first names of customers.
--Output the order date, details and cost along with the first name.
--Order records based on the customer id in ascending order.

SELECT *
  FROM customers
  LEFT JOIN orders ON customers.id = orders.cust_id
 WHERE (first_name LIKE 'Jill') 
    OR (first_name LIKE 'Eva')
ORDER BY cust_id
;
