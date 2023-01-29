from CompFunctions.gatherPlaylistFeatures import *
from CompFunctions.CreateAndAddToSpecifiedPlaylist import *


def make_similar_playlist(songSourcePlaylist, featureSourcePlaylist, newPlaylistName): 
    playlistFeatures = Get_Playlists_Features(featureSourcePlaylist)
    Create_And_Add_To_Specified_Playlist(songSourcePlaylist, newPlaylistName, playlistFeatures)


