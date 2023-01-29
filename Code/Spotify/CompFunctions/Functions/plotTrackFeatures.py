import statistics
import matplotlib.pyplot as plt

def Plot_Playlist_Features(playlistFeatures): 
    
    features = [] 

    for feature in playlistFeatures: 
        features.append(playlistFeatures[feature])
    print (features)
    plt.boxplot(features)
    plt.show()

    # data = [energy, danceability, key, loudness, speechiness, acousticness, instrumentalness, valence]
    # plt.boxplot(data)
    # #plt.scatter(energy,tempo)
    # plt.show()

