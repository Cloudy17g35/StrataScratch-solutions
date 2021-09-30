--Find the price of the cheapest property for every city

SELECT city, MIN(price) minimal_price 
  FROM airbnb_search_details
 GROUP BY city;
