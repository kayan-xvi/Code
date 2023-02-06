# This imports all of the data of any tracks stored
# And any playlists and the user information
from Data.tracks import *
from Data.playlists import * 
from Data.users import * 

# This imports all the functions to actually do stuff 
# The convention is them requiring userId, then other parameters
from CompFunctions.Functions.createPlaylist import * 
from CompFunctions.Functions.addTracksToPlaylist import *

def Create_Add_Tracks(newPlaylistName, tracksToAddIdList): 
    '''
    This function adds a list of song ids to the playlist created 
    '''

    newPlaylistId = Create_Playlist(
    userId = userIds.KVI,
    newPlaylistName = newPlaylistName,
    )

    Add_Tracks_To_Playlist(newPlaylistId, tracksToAddIdList)