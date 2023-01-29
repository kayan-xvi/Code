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

def Create_And_Add_To_Specified_Playlist(inputPlaylist, newPlaylistName, features):
  # This makes a playlist, and adds songs from another playlist with certain features 


  # Createds the playlist 
  newPlaylistId= Create_Playlist(
    userId = userIds.KVI,
    newPlaylistName = newPlaylistName,
    wantToBePublic = True
  )


  moreNext = True 
  offset = 0
  idSongsAlreadyInPlaylist = [] 
  # Loop gets items already in playlist 
  # Only actually gets the last <100 tracks 
  while moreNext == True: 
    alreadyIn, moreNext = Get_Playlist_Items(
      playlistId = newPlaylistId,
      offset=offset
    )
    idSongsAlreadyInPlaylist.append(alreadyIn)
  offset = 0
  moreNext = True 
  # Loop gets items in from source playlist 
  while moreNext == True: 
    idListing, moreNext = Get_Playlist_Items(
      playlistId = inputPlaylist, # This is the playlist input 
      offset = offset
    )
    offset += 100
    idListToAdd = []

    # Gets individual track features from collection of 100 tracks from source playlist
    trackFeatures = Get_Many_Tracks_Features(
      trackIds=idListing
    )

    minDanceability = features[0] - features[1]
    maxDanceability = features[0] + features[1]
    minEnergy = features[2] - features[3]
    maxEnergy = features[2] + features[3]
    minKey = features[4] - features[5]
    maxKey = features[4] + features[5]
    minLoudness = features[6] - features[7]
    maxLoudness = features[6] + features[7]
    minSpeechiness = features[8] - features[9]
    maxSpeechiness = features[8] + features[9]
    minAcousticness = features[10] - features[11]
    maxAcousticness = features[10] + features[11]
    minInstrumentalness = features[12] - features[13]
    maxInstrumentalness = features[12] + features[13]
    minValence = features[14] - features[15]
    maxValance = features[14] + features[15]
    minTempo = features[16] - features[17]
    maxTempo = features[16] + features[17]

    # Checks track features in comparison to mean of input +- 1 std 
    # If within, it adds the track id to a list 

    #print(len(idListing))
    for i in range(len(idListing)): 
      #print(trackFeatures['audio_features'][i]['energy'])
      if minEnergy < trackFeatures['audio_features'][i]['energy'] < maxEnergy: 
        if minDanceability < trackFeatures['audio_features'][i]['danceability'] < maxDanceability: 
          # if minKey < trackFeatures['audio_features'][i]['key'] < maxKey: 
            if minLoudness < trackFeatures['audio_features'][i]['loudness'] < maxLoudness: 
               if minSpeechiness < trackFeatures['audio_features'][i]['speechiness'] < maxSpeechiness: 
              #   if minAcousticness < trackFeatures['audio_features'][i]['acousticness'] < maxAcousticness: 
                  if minInstrumentalness < trackFeatures['audio_features'][i]['instrumentalness'] < maxInstrumentalness:
                    if minValence < trackFeatures['audio_features'][i]['valence'] < maxValance:  
                      if minTempo < trackFeatures['audio_features'][i]['tempo'] < maxTempo:  
                        idListToAdd.append(idListing[i])
        
    # This checks if the songs in 
    idListToAdd = Check_If_In_Playlist(idSongsAlreadyInPlaylist, idListToAdd)
    done = Add_Tracks_To_Playlist(
      playlistId = newPlaylistId, 
      tracksToAddIdList = idListToAdd
    )
    print(done)

