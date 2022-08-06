# Import your libraries
import pandas as pd

# Start writing code


processed_tickets = facebook_complaints[facebook_complaints.processed == True].groupby('type', as_index=False).count()
all_tickets = facebook_complaints[(facebook_complaints.processed == True) ^ (facebook_complaints.processed == False)].groupby('type', as_index=False).count()
df = all_tickets.merge(processed_tickets, left_on='type', right_on='type', suffixes=['_all', '_done'])[['type', 'processed_all', 'processed_done']]

df['ratio'] = df['processed_done'] / df['processed_all']

df[['type', 'ratio']]
