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

def Copy_To_Playlist(copyFromPlaylist, copyToPlaylist):
  # This makes a playlist, and adds songs from another playlist with certain features 
  print('started')
  moreNext = True 
  offset = 0
  idSongsAlreadyInPlaylist = [] 
  while moreNext == True: 
    print(offset)
    idSongsAlreadyInPlaylist, moreNext = Get_Playlist_Items(
      playlistId = copyToPlaylist,
      offset=offset
    )
    offset += 100 
  print('ended loop')
  offset = 0
  moreNext = True 
  idListToAdd = []
  while moreNext == True: 
    idListToAdd, moreNext = Get_Playlist_Items(
      playlistId = copyFromPlaylist, # This is the playlist input 
      offset = offset
    )
    offset += 100
    

    idListToAdd = Check_If_In_Playlist(idSongsAlreadyInPlaylist, idListToAdd)
    done = Add_Tracks_To_Playlist(
      playlistId = copyToPlaylist, 
      tracksToAddIdList = idListToAdd
    )
    print(done)

