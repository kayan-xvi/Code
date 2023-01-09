# Class for storing different track ids 
class trackClass:
  def __init__(self): 
    self.links = [
      'https://open.spotify.com/track/23OXdR7YuUBVWh5hSnYJau?si=98474a5bdfb74c46', 
      'https://open.spotify.com/track/2KVMuEgVOyOkxxx0xEFNMS?si=78751e05d9964983',
      'https://open.spotify.com/track/454I78HEySdcHE8fcVabTb?si=56e3905753e840f3'
      ]
    self.idsOnly = [
      '454I78HEySdcHE8fcVabTb'
    ]
    self.uris = [
      'spotify:track:23OXdR7YuUBVWh5hSnYJau'
      ]
    self.tempUris = []
    self.tempIds = []

trackIds = trackClass()

# This reformats the song links into the 'spotify:tracks:xxx' form, and moves them into trackId.tracks
for trackLink in trackIds.links: 
  if (f'{trackLink[31:53]}' not in trackIds.idsOnly):
    trackIds.idsOnly.append(f'{trackLink[31:53]}')
  if (f'spotify:track:{trackLink[31:53]}' not in trackIds.uris):
    trackIds.uris.append(f'spotify:track:{trackLink[31:53]}')  
    

#print(trackIds.uris)
#print(trackIds.tracks)