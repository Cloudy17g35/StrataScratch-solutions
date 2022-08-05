# Import your libraries
import pandas as pd

# Start writing code
playbook_events[playbook_events.device == 'macbook pro'].groupby('event_name', as_index=False).count()[['event_name', 'user_id']].sort_values(by='user_id', ascending=False)
