import requests 
from accessToken import accessToken

# This can get all of the items in a playlist, even past the 100 limit of the api
def Get_Playlist_Items (playlistId, offset=0):
  response = requests.get(
    f'https://api.spotify.com/v1/playlists/{playlistId}/tracks?offset={offset}',
    headers = { 
      'Authorization': f'Bearer {accessToken}'
    }
    # json = {
    #   'offset' : 10,
    #   'limit' : 50
    # }
  )
  resp = response.json()
  # resp = resp['items']
  # resp = resp['uri']
  # print(resp)
  # print(type(resp))
  # This section fetches the track uris from the track info
  #uriListing = []
  idListing = []
  # print(resp)
  # print(resp['items'])
  
  # resp['items'] is a list of all the different songs and must be iterated through 
  for item in resp['items']: 
    #print(item)
    #uriListing.append(item['track']['uri'])
    idListing.append(item['track']['id'])
    print(item['track']['name'])
  #print(resp)
  moreNext = False
  # print(resp['next'])
  if resp['next'] != None: 
    moreNext = True 
    #print('more to come')
    # for id in Get_Playlist_Items(playlistId, offset+100):
    #   idListing.append(id)
  
  return idListing, moreNext
  # uriListing = []
  # idListing = []
  # for item in resp['items']: 
  #   uriListing.append(item['track']['uri'])
  #   idListing.append(item['track']['id'])
  # #print(resp)
  # if resp['next'] != None: 
  #   print('more to come')
  #   for uri in Get_Playlist_Items(playlistId, offset+100):
  #     uriListing.append(uri)
  
  # return uriListing
