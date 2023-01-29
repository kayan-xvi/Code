import requests 
#
# This imports all of the data of any tracks stored
# And any playlists and the user information
from Data.tracks import *
from Data.playlists import * 
from Data.users import * 

# This imports all the functions to actually do stuff 
# The convention is them requiring userId, then other parameters
from CompFunctions.CreateAndAddToPlaylist import * 
from CompFunctions.CopyToPlaylist import *
from CompFunctions.gatherPlaylistFeatures import * 
from CompFunctions.CreateAndAddToSpecifiedPlaylist import *
from CompFunctions.makeSimilarPlaylist import *

def main(): 
    #Get_Playlists_Features(playlistIds.Lonely4am)
    #Create_And_Add_To_Playlist(playlistIds.KI, 'sameaslonely', 0.5)
    #Get_Playlists_Features(playlistIds.Lonely4am)
    #Create_And_Add_To_Specified_Playlist(playlistIds.KI, 'sameaslonely', Get_Playlists_Features(playlistIds.Lonely4am))
    make_similar_playlist(playlistIds.KI, playlistIds.Lonely4am, 'name')
main()