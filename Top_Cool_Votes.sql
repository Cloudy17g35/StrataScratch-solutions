-- Find the business and the review_text that received the highest number of  'cool' votes.
-- Output the business name along with the review te

SELECT business_name, review_text
  FROM yelp_reviews
 WHERE cool = (SELECT MAX(cool) 
                FROM yelp_reviews);
