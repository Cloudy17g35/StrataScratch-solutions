# Import your libraries
import pandas as pd

# Start writing code
amazon_transactions["created_at"] = pd.to_datetime(amazon_transactions["created_at"]).dt.strftime('%m-%d-%Y')
df = amazon_transactions.sort_values(by=['user_id', 'created_at'])

df['prev_value'] = df.groupby('user_id')['created_at'].shift()

df['time_dif'] = (pd.to_datetime(df['created_at']) - pd.to_datetime(df['prev_value'])).dt.days

df[df.time_dif <= 7].user_id.unique()

