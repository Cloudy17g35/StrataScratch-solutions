facebook_web_log['year'] = facebook_web_log.timestamp.dt.year
facebook_web_log['month'] = facebook_web_log.timestamp.dt.year
facebook_web_log['day'] = facebook_web_log.timestamp.dt.day
page_loads = facebook_web_log[facebook_web_log.action == 'page_load']
page_exits = facebook_web_log[facebook_web_log.action == 'page_exit']
page_loads = page_loads.sort_values(by=['user_id', 'timestamp']).drop_duplicates(subset =['user_id', 'year', 'month', 'day'] , keep='last')
page_exits = page_exits.sort_values(by=['user_id', 'timestamp']).drop_duplicates(subset =['user_id', 'year', 'month', 'day'] , keep='first')
df = page_exits.merge(page_loads, left_on=['user_id', 'year', 'month', 'day'], right_on=['user_id', 'year', 'month', 'day'], how='left', suffixes=['_exits', '_loads'])

df['session_time'] = df['timestamp_exits'] - df['timestamp_loads']
df['session_time'] = df['session_time'].dt.total_seconds()

df.groupby('user_id', as_index=False).mean()[['user_id', 'session_time']]
