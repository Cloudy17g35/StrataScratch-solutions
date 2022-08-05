# Import your libraries
import pandas as pd

# Start writing code
#employees = employee[employee]

employees = employee[employee['id'] != employee['manager_id']]
managers = employee[employee['id'] == employee['manager_id']]
merged_df = employees.merge(managers, left_on='manager_id', right_on='manager_id', suffixes=['_employee', '_managers'])

merged_df[merged_df.salary_employee > merged_df.salary_managers]
