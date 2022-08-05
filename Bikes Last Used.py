dc_bikeshare_q1_2012.sort_values(by=['end_time', 'bike_number'], ascending=False).drop_duplicates(subset='bike_number')[['bike_number', 'end_time']]
