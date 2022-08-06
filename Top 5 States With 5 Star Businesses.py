# Import your libraries
import pandas as pd

# Start writing code
five_stars_business = yelp_business[yelp_business.stars == 5]

df = five_stars_business.groupby('state', as_index=False).count()[['state', 'business_id']].sort_values(by=['business_id'], ascending=[False])

df.nlargest(5,'business_id', keep='all')
