import requests 
#
# This imports all of the data of any tracks stored
# And any playlists and the user information
from Data.tracks import *
from Data.playlists import * 
from Data.users import * 

# This imports all the functions to actually do stuff 
# The convention is them requiring userId, then other parameters
#from CompFunctions.createAndAddToPlaylist import * 
from CompFunctions.copyToPlaylist import *
from CompFunctions.gatherPlaylistFeatures import * 
from CompFunctions.createAndAddToSpecifiedPlaylist import *
from CompFunctions.makeSimilarPlaylist import *
from CompFunctions.duplicatePlaylist import *

# This imports all single functionos 
from CompFunctions.Functions.plotTrackFeatures import * 
from CompFunctions.Functions.getTracksFeatures import * 
from CompFunctions.Functions.getPlaylistItems import * 
from CompFunctions.Functions.splitToHundreds import * 

def main(): 
    #Get_Playlists_Features(playlistIds.Lonely4am)
    #Create_And_Add_To_Playlist(playlistIds.KI, 'sameaslonely', 0.5)
    #playlistInfo = Get_Playlists_Features(playlistIds.Lonely4am)
    #Create_And_Add_To_Specified_Playlist(playlistIds.KI, 'sameaslonely', Get_Playlists_Features(playlistIds.Lonely4am))
    #make_similar_playlist(playlistIds.KI, playlistIds.Lonely4am, 'name')
    #Plot_Playlist_Features(playlistInfo)
    #Duplicate_Playlist(userIds.KVI, playlistIds.KI, 'newname')
    #Copy_To_Playlist(playlistIds.Lonely4am, playlistIds.KI)
    print(len(Get_Tracks_Features(Get_Playlist_Items(playlistIds.KI))))
    #lists = Split_To_Hundreds(Get_Playlist_Items(playlistIds.KI))
    #for item in lists: 
    #    print(len(item))


main()