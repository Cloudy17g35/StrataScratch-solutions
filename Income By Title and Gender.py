# Import your libraries
import pandas as pd

# Start writing code
merged = sf_employee.merge(sf_bonus, how='left', left_on='id', right_on='worker_ref_id').dropna(subset=['bonus'])

emps_with_bonuses = merged.groupby(['id', 'salary', 'sex', 'employee_title'], as_index=False).sum()
emps_with_bonuses['total_comp'] = emps_with_bonuses['salary'] + emps_with_bonuses['bonus']
emps_with_bonuses.groupby(['employee_title', 'sex'], as_index=False).mean()[['employee_title', 'sex', 'total_comp']]

