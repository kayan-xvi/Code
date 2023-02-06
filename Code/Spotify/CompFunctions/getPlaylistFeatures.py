import requests 
import statistics
import matplotlib.pyplot as plt

from CompFunctions.Functions.getPlaylistItems import *
from CompFunctions.Functions.getTracksFeatures import *

def Get_Playlist_Features(playlistId): 
    '''
    This function gets the playlist features of a song into a dictionary of form {key: [all, songs]}
    Uses the keys: ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
    '''
    playlistItems = Get_Playlist_Items(playlistId) 
    #print(len(playlistItems))
    playlistInfo, playlistItems = Get_Tracks_Features(playlistItems)
    #print(len(playlistItems))

    playlistFeatures = {}
    featureTypes = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
    for type in featureTypes: 
        playlistFeatures[type] = []
    #print(playlistInfo)
    #print(playlistInfo)
    # print(playlistInfo[380])
    # print(playlistInfo[381])
    # print(playlistInfo[382])
    # print(playlistInfo[383])
    #i=0
    for song in playlistInfo:
        #print(i)
        #i+=1
        #print(song)
        for feature in song: 
            #print(feature)
            #print(feature)
            playlistFeatures[feature].append(song[feature])
            
    return playlistFeatures

    #print(playlistFeatures.keys())

    

    