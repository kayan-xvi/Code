from CompFunctions.gatherPlaylistFeatures import *
from CompFunctions.createAndAddToSpecifiedPlaylist import *


def Make_Similar_Playlist(songSourcePlaylist, featureSourcePlaylist, newPlaylistName): 
    playlistFeatures = Get_Playlists_Features(featureSourcePlaylist)
    Create_And_Add_To_Specified_Playlist(songSourcePlaylist, newPlaylistName, playlistFeatures)


