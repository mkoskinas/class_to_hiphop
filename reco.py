import pandas as pd
import numpy as np
from helpers import load_from_gcs

# Candidate model returns most popular hip hop tracks amongst sophisticated users in sample who have the input classical track in a playlist
def reco_v2(input_track_id, reco_dat, popularity_threshold=1, playlist_len=10):
  # Calculate total_popularity score (only needed for app)
  reco_dat['total_popularity'] = reco_dat.track_popularity + reco_dat.artist_popularity
  # Filter for users who have the input track in a playlist
  relevant_users = reco_dat.user_id[reco_dat.track_id == input_track_id]
  relevant_data = reco_dat[reco_dat.user_id.isin(relevant_users)]
  # Filter for hip hop tracks
  hiphop_tracks = relevant_data[relevant_data.artist_genre.str.contains('hip hop')]
  # Compute # of users who listened to each hip hop track
  hiphop_tracks = hiphop_tracks.groupby(['track_id', 'track_name', 'track_popularity', 'artist_id', 'artist_name', 'artist_genre', 'artist_popularity', 'total_popularity']).user_id.nunique()
  hiphop_tracks = hiphop_tracks.to_frame()
  hiphop_tracks.reset_index(level=['track_id', 'track_name', 'track_popularity', 'artist_id', 'artist_name', 'artist_genre', 'artist_popularity', 'total_popularity'], inplace=True)
  # Apply popularity threshold
  hiphop_tracks = hiphop_tracks[hiphop_tracks.total_popularity < np.quantile(reco_dat.total_popularity, popularity_threshold)]
  # Limit to columns of interest
  hiphop_tracks = hiphop_tracks.sort_values(by=['user_id'], ascending=False)
  hiphop_tracks.reset_index(inplace=True)
  hiphop_tracks = hiphop_tracks[['track_id', 'track_name', 'artist_name', 'user_id', 'total_popularity']]
  return hiphop_tracks.head(playlist_len)

if __name__ == '__main__':
  #reco_data = pd.read_csv('reco_data.csv')
  reco_data = load_from_gcs('hiphopclass', 'data/reco_data_sampo.csv', 'reco_data.csv')
  print(reco_v2(input_track_id='3DNRdudZ2SstnDCVKFdXxG', reco_dat=reco_data))
  reco_v2(input_track_id='3DNRdudZ2SstnDCVKFdXxG', reco_dat=reco_data, popularity_threshold=.9, playlist_len=3)