# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking.groupby('artist', as_index=False).count()[['artist', 'id']].sort_values('id', ascending=False)
