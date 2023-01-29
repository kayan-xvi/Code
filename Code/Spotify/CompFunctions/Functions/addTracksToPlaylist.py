import requests 
from accessToken import accessToken

from CompFunctions.Functions.splitToHundreds import * 

def Add_Tracks_To_Playlist (playlistId, tracksToAddIdList):
  '''
  This function adds the [list] of track uris to the specified playlist id 
  Returns a snapshot of it having completed 
  '''
  # print('adding')
  # tracksToAddUriList = ['']
  #tracksInList = 0
  #hundredCounter = 0

  # for id in tracksToAddIdList: 
  #   if tracksInList == 100: 
      # tracksInList = 0
      # tracksToAddUriList[hundredCounter].removesuffix(',')
      # hundredCounter += 1 
      # tracksToAddUriList.append('')
  #   if tracksInList == 99: 
  #     tracksToAddUriList[hundredCounter] += f'spotify:track:{id}'
  #     tracksInList += 1 
  #   else: 
  #     tracksToAddUriList[hundredCounter] += f'spotify:track:{id},'
  #     tracksInList += 1 

  # print(tracksToAddUriList)

  # if tracksToAddIdList == tracksToAddUriList: 
  #   print(True)    

  hundredList = Split_To_Hundreds(tracksToAddIdList)

  # tracksToAddUriList = [[]] 
  # for id in tracksToAddIdList: 
  #   if tracksInList == 100: 
  #     tracksInList = 0
  #     hundredCounter += 1 
  #     tracksToAddUriList.append([])
  #   tracksToAddUriList[hundredCounter].append('spotify:track:' + id)
  #   tracksInList += 1 
  #print(tracksToAddUriList)
  #print(len(tracksToAddUriList))

  # Max 100 songs per request 
  for list in hundredList: 
    tracksToAddUriList = []
    for id in list: 
      tracksToAddUriList.append('spotify:track:' + id)

    #print(len(uriList))
    response = requests.post(
      f'https://api.spotify.com/v1/playlists/{playlistId}/tracks', 
      headers = { 
        'Authorization': f'Bearer {accessToken}'
      },
      json = {
        'uris' : tracksToAddUriList
      }
    )
    print(response.json())