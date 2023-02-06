import requests 
import statistics
import matplotlib.pyplot as plt

from CompFunctions.Functions.getPlaylistItems import *
from CompFunctions.Functions.getTracksFeatures import *

def Get_Top_Songs(playlistId, featureName, numberOfSongs=50, Top=True): 
    '''
    This function finds the top (or bottom) songs of a playlist by a certain feature
    Returns a list of songids 
    '''
    playlistItems = Get_Playlist_Items(playlistId) 
    #print(len(playlistItems))
    playlistInfo, playlistItems = Get_Tracks_Features(playlistItems)
    #print(len(playlistItems))

    featureTypes = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
    playlistDictionary = {}
    #print(playlistInfo)
    #print(playlistInfo)
    # print(playlistInfo[380])
    # print(playlistInfo[381])
    # print(playlistInfo[382])
    # print(playlistInfo[383])
    i=0
    for song in playlistInfo:
        
        i+=1
        #print(song)
        number = song[featureName]
        #print(type(song[featureName]))
        while number in playlistDictionary: 
            #print(i)
            #print(number)
            number += 0.0001
        playlistDictionary[number] = song['id']
    
    orderedPlaylistList = sorted(playlistDictionary)
    print(orderedPlaylistList)
    print(orderedPlaylistList.count(1))

    selectedSongs = []

    if Top == True: 
        for songNumber in range(numberOfSongs): 
            selectedSongs.append(playlistDictionary[orderedPlaylistList[len(orderedPlaylistList)-songNumber-1]])
    else: 
        for songNumber in range(numberOfSongs): 
            selectedSongs.append(playlistDictionary[orderedPlaylistList[songNumber]])


    return selectedSongs

    #print(playlistFeatures.keys())

    

    