import requests 

# This imports all of the data of any tracks stored
# And any playlists and the user information
from Data.tracks import *
from Data.playlists import * 
from Data.users import * 

# This imports all the functions to actually do stuff 
# The convention is them requiring userId, then other parameters
from Functions.createPlaylist import *
from Functions.addTracksToPlaylist import *
from Functions.getPlaylistItems import *
from Functions.getTrackFeatures import *


done = Create_Playlist(
    userId=userIds.KVI,
    newPlaylistName='Access Token Works',
    wantToBePublic=False
) 