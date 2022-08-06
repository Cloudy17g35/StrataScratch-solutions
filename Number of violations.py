# Import your libraries
import pandas as pd

# Start writing code
df = sf_restaurant_health_violations[sf_restaurant_health_violations.business_name == 'Roxanne Cafe']

df['year'] = df.inspection_date.dt.year

df.groupby('year', as_index=False).count()[['year', 'violation_id']]
