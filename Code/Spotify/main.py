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

# def possible(): 

#   done = ''
#   #action = input('What would you like to do?')
#   action = ''

#   if action == 'add': 
#     done = Add_Tracks_To_Playlist(
#       playlistId = playlistIds.Test2,
#       tracksToAdd = trackIds.uris
#     )
#   if action == 'get': 
#     done = Get_Playlist_Items(
#       playlistId = playlistIds.Test2
#       )
#     trackIds.tempIds = done
#   if action == 'create': 
#     done = Create_Playlist(
#       userId = userIds.KVI,
#       newPlaylistName = 'Test1',
#       wantToBePublic = False,
#     )
#   if action == 'feat': 
#     done = Get_Track_Features( 
#       trackId = trackIds.idsOnly[1]
#     )
  

# def Main(): 
#   # newPlaylistId= Create_Playlist(
#   #   userId = userIds.KVI,
#   #   newPlaylistName = 'Test5',
#   #   wantToBePublic = False 
#   # )

#   idListing = Get_Playlist_Items(
#     playlistId = playlistIds.Test1
#   )
#   print(idListing)
#   #print(len(uriListing))
#   #print(uriListing)
#   # for uri in uriListing: 
#   #   energy = Get_Track_Features(
#   #     trackId = uri[14:]
#   #   )['energy'] # A certain feature key should be added here to get that feature so you can filter the songs
#   #   print(energy)
#   #   if 1==1: # Can change this to only add tracks of certain features 
#   #     #energy < 0.6: 
#   #     done = Add_Tracks_To_Playlist(
#   #       playlistId = newPlaylistId,
#   #       tracksToAdd = [uri]
#   #     )
#   #     print(done)

# # This imports all of the data of any tracks stored
# # And any playlists and the user information
# from Data.tracks import *
# from Data.playlists import * 
# from Data.users import * 

# # This imports all the functions to actually do stuff 
# # The convention is them requiring userId, then other parameters
# from CompFunctions.Functions.createPlaylist import *
# from CompFunctions.Functions.addTracksToPlaylist import *
# from CompFunctions.Functions.getPlaylistItems import *
# from CompFunctions.Functions.getTrackFeatures import *
# from CompFunctions.Functions.getManyTracksFeatures import * 

# def Create_And_Add_To_Playlist():
#   # This makes a playlist, and adds songs from another playlist with certain features 

#   newPlaylistId= Create_Playlist(
#     userId = userIds.KVI,
#     newPlaylistName = 'Test6',
#     wantToBePublic = False
#   )

#   moreNext = True 
#   offset = 0
#   while moreNext == True: 
#     idListing, moreNext = Get_Playlist_Items(
#       playlistId = playlistIds.KI, # This is the playlist input 
#       offset = offset
#     )
#     offset += 100
#     idListToAdd = []

#     trackFeatures = Get_Many_Tracks_Features(
#       trackIds=idListing
#     )
#     for i in range(len(idListing)): 
#       if trackFeatures['audio_features'][i]['energy'] < 0.6 and trackFeatures['audio_features'][i]['tempo'] < 100: # Change this line to filter
#         idListToAdd.append(idListing[i])
#     #print(idListToAdd)
#     done = Add_Tracks_To_Playlist(
#       playlistId = newPlaylistId,
#       tracksToAddIdList = idListToAdd
#     )
#     print(done)



#Create_And_Add_To_Playlist(playlistIds.StarWarsSoundtracks, 'ChilledSW') 
Copy_To_Playlist(playlistIds.ChillStarWars, '4cgxa3Jd6VA1m8UJfnkQxO')
