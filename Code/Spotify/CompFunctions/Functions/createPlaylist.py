import requests
from accessToken import accessToken

def Create_Playlist (userId, newPlaylistName, wantToBePublic = True):
  '''
  This function creates a playlist under the specified user, with the given name
  Returns the new playlist id 
  '''
  response = requests.post(
    f'https://api.spotify.com/v1/users/{userId}/playlists',
    headers = { 
      'Authorization': f'Bearer {accessToken}'
    },
    json = {
      'name' : newPlaylistName,
      'public' : wantToBePublic
    }
  )
  return response.json()['id']