-- Find the total cost of each customer's orders. Output customer's id, first name, and the total order cost. 
-- Order records by customer's first name alphabetically.


SELECT  c.id, first_name ,SUM(total_order_cost)
  FROM customers c INNER JOIN orders o
  on c.id = o.cust_id
 GROUP BY c.id, first_name
 ORDER BY first_name
;
