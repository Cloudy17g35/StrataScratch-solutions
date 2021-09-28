--Find the average number of beds in each neighborhood that has at least 3 beds in total.

--Output results along with the neighborhood name and sort the results based on the number of average beds in descending order.

SELECT neighbourhood, AVG(beds) AS average_beds
  FROM airbnb_search_details
 GROUP BY neighbourhood
HAVING AVG(beds) >= 3;
