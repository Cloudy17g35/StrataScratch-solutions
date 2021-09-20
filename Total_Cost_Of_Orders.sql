-- Find the total cost of each customer's orders. Output customer's id, first name, a
nd the total order cost. Order records by customer's first name alphabetically.

SELECT  cust_id, first_name, total_order_cost
  FROM customers
 INNER JOIN orders ON customers.id = orders.cust_id
 ORDER BY first_name
 ;
