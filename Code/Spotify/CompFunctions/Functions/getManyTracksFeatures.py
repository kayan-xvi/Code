import requests 
from accessToken import accessToken

def Get_Many_Tracks_Features (trackIds):
  '''
  Requires a list of track ids 
  
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
  '''
  print(trackIds)
  response = requests.get(
    'https://api.spotify.com/v1/audio-features?ids=' + ','.join(trackIds),
    headers = { 
      'Authorization': f'Bearer {accessToken}'
    # },
    # json = { 
    #   'ids' : trackIds
    }
  )
  response.status_code
  resp = response.json()
  return resp
  
#   # This section fetches the track uris from the track info
#   listing = []
#   for item in resp['items']: 
#     listing.append(item['track']['uri'])
#   return listing
