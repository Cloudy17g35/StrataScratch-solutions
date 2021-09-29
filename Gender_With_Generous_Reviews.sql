-- Write a query to find which gender gives a higher average review score when writing reviews as guests.
-- Use the `from_type` column to identify guest reviews. Output the gender and their average review score.


SELECT gender, avg(review_score) average_score
  FROM airbnb_reviews reviews
 INNER JOIN airbnb_guests guests
    ON reviews.from_user = guests.guest_id
 WHERE from_type = 'guest'
 GROUP BY gender
 ORDER BY average_score DESC
 LIMIT 1;
