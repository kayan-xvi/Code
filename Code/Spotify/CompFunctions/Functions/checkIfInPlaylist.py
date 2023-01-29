def Check_If_In_Playlist(existingSongs, newSongs): 
    '''
    This function compares 2 lists of songs 
    Returns a list of all song in newSongs which aren't in existingSong
    '''
    notDuplicated = []

    for newSong in newSongs: 
        if newSong not in existingSongs: 
            notDuplicated.append(newSong)
    return notDuplicated

