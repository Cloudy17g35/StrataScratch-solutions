# Import your libraries
import pandas as pd

# Start writing code
grouped = airbnb_contacts.groupby('id_guest', as_index=False).sum().sort_values(['n_messages', 'id_guest'], ascending=False)[['id_guest', 'n_messages']]

grouped['ranking'] = grouped['n_messages'].rank(method='dense', ascending = False).astype(int)
grouped
