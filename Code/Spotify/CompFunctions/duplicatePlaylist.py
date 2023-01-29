from CompFunctions.Functions.createPlaylist import * 
from CompFunctions.Functions.getPlaylistItems import *
from CompFunctions.Functions.addTracksToPlaylist import *

def Duplicate_Playlist(userId, playlistId, newPlaylistName): 
    
    newPlaylistId = Create_Playlist(userId, newPlaylistName)

    itemsInPlaylist = Get_Playlist_Items(playlistId)

    Add_Tracks_To_Playlist(newPlaylistId, itemsInPlaylist)



