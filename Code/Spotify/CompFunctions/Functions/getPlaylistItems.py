import requests 
from accessToken import accessToken

# This can get all of the items in a playlist, even past the 100 limit of the api
def Get_Playlist_Items (playlistId):
  '''
  This function takes in the playlistId and gets all of the tracks in the playlist 
  Returns a list of all trackIds
  '''
  offset = 0
  idListing = []
  moreNext = True 
  
  while moreNext == True: 
    response = requests.get(
      f'https://api.spotify.com/v1/playlists/{playlistId}/tracks?offset={offset}',
      headers = { 
        'Authorization': f'Bearer {accessToken}'
      }
    )

    resp = response.json()
    for item in resp['items']: 
      idListing.append(item['track']['id'])

    if resp['next'] == None: 
      moreNext = False
    offset += 100 
  #print(idListing)
  return idListing

