# Import your libraries
import pandas as pd

# Start writing code
customers.merge(orders, left_on='id' ,right_on='cust_id', how='left').sort_values(by=['first_name', 'order_details'])[['first_name', 'last_name', 'city', 'order_details']]
