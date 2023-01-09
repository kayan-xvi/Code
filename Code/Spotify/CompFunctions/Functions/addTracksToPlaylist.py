import requests 
from accessToken import accessToken

def Add_Tracks_To_Playlist (playlistId, tracksToAddIdList):
  tracksToAddUriList = [] 
  for id in tracksToAddIdList: 
    tracksToAddUriList.append('spotify:track:' + id)
  response = requests.post(
    f'https://api.spotify.com/v1/playlists/{playlistId}/tracks', 
    headers = { 
      'Authorization': f'Bearer {accessToken}'
    },
    json = {
      'uris' : tracksToAddUriList
    }
  )
  return response.json()