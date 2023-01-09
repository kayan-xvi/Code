import requests 
from accessToken import accessToken

def Get_Track_Features (trackId):
  '''
  Possible keys: 
  acousticness 0-1 ###
  analysis_url
  danceability 0-1 ###
  durations_ms int(ms)
  energy 0-1 ###
  id str
  instrumentalness 0-1 ###
  key int(-1-11) ###
  liveness 0-1 
  loudness -60-0
  mode major=1 minor=0 ###
  speechiness 0-1 ###
  tempo BPM
  time_signature int(3-7)/4
  track_href
  typeuri
  valence 0-1 positiveness ###
  '''
  response = requests.get(
    f'https://api.spotify.com/v1/audio-features/{trackId}',
    headers = { 
      'Authorization': f'Bearer {accessToken}'
    }
  )
  resp = response.json()
  return resp
  
#   # This section fetches the track uris from the track info
#   listing = []
#   for item in resp['items']: 
#     listing.append(item['track']['uri'])
#   return listing
