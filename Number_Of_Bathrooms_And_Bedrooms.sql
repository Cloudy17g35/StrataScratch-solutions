-- Find the average number of bathrooms and bedrooms for each city’s property types. Output the result along with the city name and the property type.

SELECT property_type,city, 
       AVG(bathrooms) AS average_bathrooms , 
       AVG(bedrooms) AS average_bedrooms
  FROM airbnb_search_details
  GROUP BY property_type, city; 
