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
    playlistInfo = Get_Tracks_Features(playlistItems)

    playlistFeatures = {}
    featureTypes = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
    for type in featureTypes: 
        playlistFeatures[type] = []

    #print(playlistInfo)
    for song in playlistInfo:
        for feature in song: 
            #print(feature)
            playlistFeatures[feature].append(song[feature])
            
    return playlistFeatures

    #print(playlistFeatures.keys())

    

    