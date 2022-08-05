# Import your libraries
import pandas as pd

# Start writing code
orders = orders[(orders.order_date.dt.month == 3) & (orders.order_date.dt.year == 2019)]

orders.groupby('cust_id', as_index=False).sum()[['cust_id', 'total_order_cost']].sort_values(by='total_order_cost', ascending=False)
