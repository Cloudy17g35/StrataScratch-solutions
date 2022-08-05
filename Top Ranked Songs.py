# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking = spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking.position == 1]
spotify_worldwide_daily_song_ranking.groupby(['position', 'trackname'], as_index=False).count()[['trackname', 'artist']].sort_values(by='artist', ascending=False)
