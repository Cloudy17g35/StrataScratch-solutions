# Import your libraries
import pandas as pd

# Start writing code
#yelp_business.groupby('categories', as_index=False).sum()[['categories', 'review_count']].sort_values(by='review_count', ascending=False)

yelp_business.categories = yelp_business.categories.str.split(';')
yelp_business.explode('categories').groupby('categories', as_index=False).sum()[['categories', 'review_count']].sort_values(by='review_count', ascending=False)
