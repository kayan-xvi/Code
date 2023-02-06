from CompFunctions.Functions.getTracksFeatures import *

def Filter_Track_List(
    trackIdList, 
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
    maxDuration=1000000000
    ): 
    '''
    Takes in a list of tracks and specified features
    ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
    Takes a list of numbers for the keys it must fit 

    Either change the min and max of a feature to select a range 
    Or select a central point and stdev for central+-stdev

    Returns songs which match the input parameters
    '''


    keys = ['danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'type', 'id', 'uri', 'track_href', 'analysis_url', 'duration_ms', 'time_signature']
    filteredSongs = []
    #i = 0
    #j = 0

    trackFeatures = Get_Tracks_Features(trackIdList)
    #print(maxEnergy)

    # Song must go through all criteria without passing in order to be selected 
    for song in trackFeatures: 
        print(song)
        #print(danceability)
        if not minDanceability < song['danceability'] < maxDanceability: 
            continue 
        if danceability != None: 
            if song['danceability'] < danceability - danceabilityStd or song['danceability'] > danceability + danceabilityStd:
                continue

        if not minEnergy < song['energy'] < maxEnergy:
            continue 
        #i += 1
        #print(i)
        if energy != None: 
            if song['energy'] < energy - energyStd or song['energy'] > energy + energyStd:
                continue

        if key != None: 
            if song['key'] not in key: 
                continue

        if mode != None: 
            if song['mode'] != mode: 
                continue

        if not minLoudness < song['loudness'] < maxLoudness: 
            continue
        if loudness != None: 
            if song['loudness'] < loudness - loudnessStd or song['loudness'] > loudness + loudnessStd:
                continue

        if not minSpeechiness < song['speechiness'] < maxSpeechiness: 
            continue
        if speechiness != None: 
            if song['speechiness'] < speechiness - speechinessStd or song['speechiness'] > speechiness + speechinessStd:
                continue

        if not minAcousticness < song['acousticness'] < maxAcousticness: #
            continue
        if acousticness != None: 
            if song['acousticness'] < acousticness - acousticnessStd or song['acousticness'] > acousticness + acousticnessStd:
                continue

        if not minInstrumentalness < song['instrumentalness'] < maxInstrumentalness: 
            continue
        if instrumentalness != None: 
            if song['instrumentalness'] < instrumentalness - instrumentalnessStd or song['instrumentalness'] > instrumentalness + instrumentalnessStd:
                continue

        if not minLiveness < song['liveness'] < maxLiveness: 
            continue
        #j += 1
        #print(f'j{j}')
        if liveness != None: 
            if song['liveness'] < liveness - livenessStd or song['liveness'] > liveness + livenessStd:
                continue

        if not minValence < song['valence'] < maxValence: 
            continue
        if valence != None: 
            if song['valence'] < valence - valenceStd or song['valence'] > valence + valenceStd:
                continue

        if not minTempo < song['tempo'] < maxTempo: 
            continue
        if tempo != None: 
           if song['tempo'] < tempo - tempoStd or song['tempo'] > tempo + tempoStd:
                continue

        if type != None: 
            if song['type'] != type: 
                continue

        if timeSignature != None: 
            if song['time_signature'] not in timeSignature: 
                continue
        
        if not minDuration < song['duration_ms'] < maxDuration: 
            continue
        if duration != None: 
           if song['duration_ms'] < duration - durationStd or song['duration_ms'] > duration + durationStd:
                continue

        filteredSongs.append(song['id'])
        

    return filteredSongs


   