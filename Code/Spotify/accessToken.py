# Turns access token from accessToken.txt into a string which can actually be used elsewhere

with open(r'Code\Spotify\accessToken.txt') as token: 
  #print(token)
  accessToken = token.read()
#print(accessToken)