# Import your libraries
import pandas as pd

# Start writing code
df = ms_download_facts.merge(ms_user_dimension, left_on='user_id', right_on='user_id').merge(ms_acc_dimension, left_on='acc_id', right_on='acc_id')

df = df.groupby(['date', 'paying_customer'], as_index=False).sum()

paied = df[df.paying_customer == 'yes'][['date', 'downloads']]
not_paied = df[df.paying_customer == 'no'][['date', 'downloads']]
compared = paied.rename(columns={'downloads': 'yes'}).merge(not_paied.rename(columns={'downloads':'no'}))

compared[compared.no > compared.yes]

