SELECT first_name, last_name, city, order_details 
  FROM customers 
  LEFT JOIN orders on customers.id = orders.cust_id
  ORDER BY first_name;
