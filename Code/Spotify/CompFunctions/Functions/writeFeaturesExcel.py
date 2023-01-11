import pandas as pd 

excelFile = 'Code\Spotify\playlistFeatures.xlsx' 
playlistData = pd.read_excel(excelFile, index_col=1)

print(playlistData)