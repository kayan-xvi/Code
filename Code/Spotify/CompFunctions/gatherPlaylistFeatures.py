import requests 
import statistics
import matplotlib.pyplot as plt

from CompFunctions.Functions.getPlaylistItems import *
from CompFunctions.Functions.getTracksFeatures import *

def Get_Playlists_Features(playlistId): 
    playlistItems, moreNext = Get_Playlist_Items(playlistId) 
    resp = Get_Many_Tracks_Features(playlistItems)

    playlistFeatures = {}
    featureTypes = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
    for type in featureTypes: 
        playlistFeatures[type] = []

    for trackFeatures in resp['audio_features']:
        for feature in trackFeatures: 
            playlistFeatures[feature].append(trackFeatures[feature])

    print(playlistFeatures.keys())

    danceability = playlistFeatures['danceability']
    energy = playlistFeatures['energy']
    # key refers to the pitch - C == 0 all the way up to 11, no key detected == -1 
    key = playlistFeatures['key']
    # loudness is between -60 and 0 db, more negative is quieter 
    loudness = playlistFeatures['loudness']
    # mode refers to major or minor - major == 1 and minor == 0 
    mode = playlistFeatures['mode']
    # speechiness is how much is spoken in a track 
    speechiness = playlistFeatures['speechiness']
    acousticness = playlistFeatures['acousticness']
    instrumentalness = playlistFeatures['instrumentalness']
    # liveness is to what extent it sounds like it was performed live 
    liveness = playlistFeatures['liveness']
    # valance is positiveness 
    valence = playlistFeatures['valence']
    tempo = playlistFeatures['tempo']
    timeSignature = playlistFeatures['time_signature']
    

    print(f'danceability: \nMean = {statistics.mean(danceability)} \nStdDev = {statistics.stdev(danceability)}')
    print(f'energy: \nMean = {statistics.mean(energy)} \nStdDev = {statistics.stdev(energy)}')
    print(f'key: \nMean = {statistics.mean(key)} \nStdDev = {statistics.stdev(key)}')
    print(f'loudness: \nMean = {statistics.mean(loudness)} \nStdDev = {statistics.stdev(loudness)}')
    #print(f'mode: \nMode = {statistics.mode(mode)}')
    print(f'speechiness: \nMean = {statistics.mean(speechiness)} \nStdDev = {statistics.stdev(speechiness)}')
    print(f'acousticness: \nMean = {statistics.mean(acousticness)} \nStdDev = {statistics.stdev(acousticness)}')
    print(f'instrumentalness: \nMean = {statistics.mean(instrumentalness)} \nStdDev = {statistics.stdev(instrumentalness)}')
    #print(f'liveness: \nMean = {statistics.mean(liveness)} \nStdDev = {statistics.stdev(liveness)}')
    print(f'valence: \nMean = {statistics.mean(valence)} \nStdDev = {statistics.stdev(valence)}')
    print(f'tempo: \nMean = {statistics.mean(tempo)} \nStdDev = {statistics.stdev(tempo)}')
    #print(f'timeSignature: \nMean = {statistics.mean(timeSignature)} \nStdDev = {statistics.stdev(timeSignature)}')

    playlistInfo = {
        'danceabilityMean': statistics.mean(danceability), 'danceabilityStd' : statistics.stdev(danceability),
        'energyMean' : statistics.mean(energy), 'energyStd': statistics.stdev(energy), 
        'keyMean' : statistics.mean(key), 'keyStd' :statistics.stdev(key),
        'loudnessMean' : statistics.mean(loudness), 'loudnessStd' : statistics.stdev(loudness), 
        'modeMean' : statistics.mean(mode), 'modeStd' : statistics.stdev(mode),
        'speechinessMean' : statistics.mean(speechiness), 'speechniessStd' : statistics.stdev(speechiness),
        'acousticnessMean' : statistics.mean(acousticness), 'acousticnessStd' : statistics.stdev(acousticness), 
        'instrumentalnessMean' : statistics.mean(instrumentalness), 'instrumentalness' : statistics.stdev(instrumentalness),
        'livenessMean' : statistics.mean(liveness), 'liveness' : statistics.stdev(liveness),
        'valenceMean' : statistics.mean(valence), 'valenceStd' : statistics.stdev(valence), 
        'tempoMean' : statistics.mean(tempo), 'tempoStd' : statistics.stdev(tempo), 
        'timeSignatureMean' : statistics.mean(timeSignature), 'timeSignatureMean' : statistics.stdev(timeSignature)
        }

    return playlistInfo

    