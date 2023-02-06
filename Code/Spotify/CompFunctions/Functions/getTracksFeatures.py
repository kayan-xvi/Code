import requests 
from accessToken import accessToken

from CompFunctions.Functions.splitToHundreds import *

def Get_Tracks_Features (trackIds):
  '''
  This gets the features of a list of max 100 songs 
  Requires a list of track ids and the track list with nulls removed
  
  Possible keys: 
  acousticness
  analysis_url
  danceability
  durations_ms
  energy
  id
  instrumentalness 
  key 
  liveness 
  loudness 
  mode 
  speechiness 
  tempo
  time_signature
  track_href
  typeuri
  valence

  Returns [{song1info}, {song2info}, ...]
  '''
  #print(trackIds)
  features = []

  smallerTrackIds = Split_To_Hundreds(trackIds)

  for list in smallerTrackIds:
    response = requests.get(
      'https://api.spotify.com/v1/audio-features?ids=' + ','.join(list),
      headers = { 
        'Authorization': f'Bearer {accessToken}'
      # },
      # json = { 
      #   'ids' : trackIds
      }
    )
    response.status_code
    resp = response.json()
    #print(resp['audio_features'])
    features.extend(resp['audio_features'])
    #print(features)
    #for song in features:
      #print(song['speechiness']+song['instrumentalness'])
    
    nullSongs = []
    counter = 0
    for song in reversed(features): 
      if song == None: 
        nullSongs.append(trackIds[counter])
        features.remove(song)
      counter += 1 
    for null in nullSongs: 
      trackIds.remove(null)
      #print('removed')

  return features, trackIds
