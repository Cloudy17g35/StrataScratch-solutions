# Import your libraries
import pandas as pd

# Start writing code
all_energy_centes = pd.concat([fb_eu_energy, fb_asia_energy, fb_na_energy])

grouped_by_dates = all_energy_centes.groupby('date', as_index=False).sum()

maximal_energy_use = grouped_by_dates.consumption.max()

grouped_by_dates[grouped_by_dates.consumption == maximal_energy_use]
