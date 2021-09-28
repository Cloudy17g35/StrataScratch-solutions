-- Find whether hosts or guests give higher review scores based on their average review scores. Output the higher of the average review score rounded to the 2nd decimal spot (e.g., 5.11)

SELECT from_type, ROUND(avg(review_score), 2)
  FROM airbnb_reviews
 GROUP BY from_type
 ORDER BY avg(review_score) DESC
 LIMIT 1;
