import pandas as pd

# Start writing code
joined_df = airbnb_hosts.merge(airbnb_units, left_on='host_id', right_on='host_id')

filtered = joined_df[(joined_df['age'] < 30) & (joined_df['unit_type'] == 'Apartment')]

filtered.drop_duplicates().groupby('nationality').size().reset_index()
