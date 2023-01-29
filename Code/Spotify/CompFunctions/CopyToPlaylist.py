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
from CompFunctions.Functions.getTracksFeatures import * 
from CompFunctions.Functions.checkIfInPlaylist import * 

def Copy_To_Playlist(copyFromPlaylist, copyToPlaylist):
  '''
  This adds songs from another playlist to an existing playlist 
  Checks for duplicates 
  '''
  #print('started')

  # Gets songs already in target playlist 
  idSongsAlreadyInPlaylist = Get_Playlist_Items(
    playlistId = copyToPlaylist
  )

  # gets songs in playlist from which to add 
  idListToAdd = Get_Playlist_Items(
    playlistId = copyFromPlaylist
  )
    
  # Checks for duplication 
  idListToAdd = Check_If_In_Playlist(idSongsAlreadyInPlaylist, idListToAdd)

  # Adds any new tracks
  Add_Tracks_To_Playlist(
    playlistId = copyToPlaylist, 
    tracksToAddIdList = idListToAdd
  )

