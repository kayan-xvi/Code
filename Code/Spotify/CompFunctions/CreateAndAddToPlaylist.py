# This imports all of the data of any tracks stored
# And any playlists and the user information
from Data.tracks import *
from Data.playlists import * 
from Data.users import * 

# This imports all the functions to actually do stuff 
# The convention is them requiring userId, then other parameters
from CompFunctions.Functions.createPlaylist import *
from CompFunctions.Functions.addTracksToPlaylist import *
from CompFunctions.Functions.getPlaylistItems import *
from CompFunctions.Functions.getTrackFeatures import *
from CompFunctions.Functions.getManyTracksFeatures import * 
from CompFunctions.Functions.checkIfInPlaylist import * 

def Create_And_Add_To_Playlist(inputPlaylist, newPlaylistName):
  # This makes a playlist, and adds songs from another playlist with certain features 

  newPlaylistId= Create_Playlist(
    userId = userIds.KVI,
    newPlaylistName = newPlaylistName,
    wantToBePublic = True
  )

  moreNext = True 
  offset = 0
  idSongsAlreadyInPlaylist = [] 
  while moreNext == True: 
    idSongsAlreadyInPlaylist, moreNext = Get_Playlist_Items(
      playlistId = newPlaylistId,
      offset=offset
    )
  offset = 0
  moreNext = True 
  while moreNext == True: 
    idListing, moreNext = Get_Playlist_Items(
      playlistId = inputPlaylist, # This is the playlist input 
      offset = offset
    )
    offset += 100
    idListToAdd = []

    trackFeatures = Get_Many_Tracks_Features(
      trackIds=idListing
    )

    #print(len(idListing))
    for i in range(len(idListing)): 
      #print(trackFeatures['audio_features'][i]['energy'])
      if trackFeatures['audio_features'][i]['instrumentalness'] < 0.2 and trackFeatures['audio_features'][i]['speechiness'] > 0.7 and 0.4 < trackFeatures['audio_features'][i]['danceability'] < 0.75 and trackFeatures['audio_features'][i]['energy'] > 0.5 and trackFeatures['audio_features'][i]['loudness'] > -20 : # Change this line to filter
      #if trackFeatures['audio_features'][i]['energy'] < energy: 
        idListToAdd.append(idListing[i])
    #print(idListToAdd)
    idListToAdd = Check_If_In_Playlist(idSongsAlreadyInPlaylist, idListToAdd)
    done = Add_Tracks_To_Playlist(
      playlistId = newPlaylistId, 
      tracksToAddIdList = idListToAdd
    )
    print(done)

