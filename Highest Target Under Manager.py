# Import your libraries
import pandas as pd

# Start writing code
df = salesforce_employees[salesforce_employees.manager_id == 13]

max_target = df.target.max()

df[df.target == max_target][['first_name', 'target']]
