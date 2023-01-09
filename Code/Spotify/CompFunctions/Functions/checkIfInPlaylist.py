def Check_If_In_Playlist(existingSongs, newSongs): 
    for newSong in newSongs: 
        if newSong in existingSongs: 
            newSongs.remove(newSong)
    return newSongs

