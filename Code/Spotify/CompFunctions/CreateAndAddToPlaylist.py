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
from CompFunctions.Functions.getTracksFeatures import * 
from CompFunctions.Functions.checkIfInPlaylist import * 
from CompFunctions.Functions.filterTrackList import *

def Create_And_Add_To_Playlist(
    inputPlaylist, 
    newPlaylistName,
    danceability=None, 
    danceabilityStd=0.15,
    minDanceability=0, 
    maxDanceability=1,
    energy=None,
    energyStd = 0.15,
    minEnergy = 0,
    maxEnergy = 1,
    key=None, 
    loudness=None, 
    loudnessStd=10,
    minLoudness=-60,
    maxLoudness=0,
    mode=None, 
    speechiness=None,
    speechinessStd = 0.15,
    minSpeechiness = 0,
    maxSpeechiness = 1,
    acousticness=None,
    acousticnessStd = 0.15,
    minAcousticness = 0,
    maxAcousticness = 1,
    instrumentalness=None,
    instrumentalnessStd=0.15,
    minInstrumentalness=0,
    maxInstrumentalness=1,
    liveness=None,
    livenessStd=0.15,
    minLiveness=0,
    maxLiveness=1,
    valence=None,
    valenceStd=0.15,
    minValence=0,
    maxValence=1,
    tempo=None,
    tempoStd=10,
    minTempo=0,
    maxTempo=500,
    type=None,
    timeSignature=None,
    duration=None,
    durationStd=30000,
    minDuration=0,
    maxDuration=1000000000,
    featureDict=None,
    featureSpecifier=None
  ):
  '''
  This makes a playlist, and adds songs from another playlist with certain features
  ''' 
  if featureDict != None: 
    if featureSpecifier == None: 
      acousticness = featureDict['acousticnessMean']
      danceability = featureDict['danceabilityMean']
      duration = featureDict ['durationMean']
      energy = featureDict ['energyMean']
      instrumentalness = featureDict ['instrumentalnessMean']
      key = featureDict ['keyMean']
      liveness = featureDict ['livenessMean']
      loudness = featureDict ['loudnessMean']
      mode = featureDict ['modeMode']
      speechiness = featureDict['speechinessMean']
      tempo = featureDict ['tempoMean']
      timeSignature = featureDict['timeSignatureMean']
      valence = featureDict['valenceMean']
    else: 
      if 'acousticness' in featureSpecifier: 
        acousticness = featureDict['acousticnessMean']
      if 'danceability' in featureSpecifier: 
        danceability = featureDict['danceabilityMean']
      # if 'duration' in featureSpecifier: 
      #   duration = featureDict ['durationMean']
      if 'energy' in featureSpecifier: 
        energy = featureDict ['energyMean']
      if 'instrumentalness' in featureSpecifier: 
        instrumentalness = featureDict ['instrumentalnessMean']
      # if 'key' in featureSpecifier: 
      #   key = featureDict ['keyMean']
      if 'liveness' in featureSpecifier: 
        liveness = featureDict ['livenessMean']
      if 'loudness' in featureSpecifier: 
        loudness = featureDict ['loudnessMean']
      # if 'mode' in featureSpecifier: 
      #   mode = featureDict ['modeMean']
      if 'speechiness' in featureSpecifier: 
        speechiness = featureDict['speechinessMean']
      if 'tempo' in featureSpecifier: 
        tempo = featureDict ['tempoMean']
      # if 'timeSignature' in featureSpecifier: 
      #   timeSignature = featureDict['timeSignatureMean']
      if 'valence' in featureSpecifier: 
        valence = featureDict['valenceMean']

  newPlaylistId = Create_Playlist(
    userId = userIds.KVI,
    newPlaylistName = newPlaylistName,
  )

  trackIdList = Get_Playlist_Items(inputPlaylist)

  filteredTracks = Filter_Track_List(
    trackIdList,
    danceability=danceability, 
    danceabilityStd=danceabilityStd,
    minDanceability=minDanceability, 
    maxDanceability=maxDanceability,
    energy=energy,
    energyStd = energyStd,
    minEnergy = minEnergy,
    maxEnergy = maxEnergy,
    key=key, 
    loudness=loudness, 
    loudnessStd=loudnessStd,
    minLoudness=minLoudness,
    maxLoudness=maxLoudness,
    mode=mode, 
    speechiness=speechiness,
    speechinessStd = speechinessStd,
    minSpeechiness = minSpeechiness,
    maxSpeechiness = maxSpeechiness,
    acousticness=acousticness,
    acousticnessStd = acousticnessStd,
    minAcousticness = minAcousticness,
    maxAcousticness = maxAcousticness,
    instrumentalness=instrumentalness,
    instrumentalnessStd=instrumentalnessStd,
    minInstrumentalness=minInstrumentalness,
    maxInstrumentalness=maxInstrumentalness,
    liveness=liveness,
    livenessStd=livenessStd,
    minLiveness=minLiveness,
    maxLiveness=maxLiveness,
    valence=valence,
    valenceStd=valenceStd,
    minValence=minValence,
    maxValence=maxValence,
    tempo=tempo,
    tempoStd=tempoStd,
    minTempo=minTempo,
    maxTempo=maxTempo,
    type=type,
    timeSignature=timeSignature,
    duration=duration,
    durationStd=durationStd,
    minDuration=minDuration,
    maxDuration=maxDuration
    )

  #print(len(filteredTracks))
  Add_Tracks_To_Playlist(newPlaylistId, filteredTracks)

