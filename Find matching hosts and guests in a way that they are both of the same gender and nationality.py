# Import your libraries
import pandas as pd

# Start writing code
dup_free= airbnb_hosts.merge(airbnb_guests, left_on=['nationality', 'gender'], right_on=['nationality', 'gender']).drop_duplicates(subset=['host_id', 'guest_id'])

dup_free[['host_id', 'guest_id']]
