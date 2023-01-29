

def Split_To_Hundreds(bigList): 
    '''
    This takes a list of trackIds
    Returns [[100],[16]]
    '''
    smallerLists = [[]]
    hundredCounter = 0
    tracksInList = 0

    for item in bigList: 
      if tracksInList == 100: 
        tracksInList = 0
        hundredCounter += 1 
        smallerLists.append([])
      smallerLists[hundredCounter].append(item)
      tracksInList += 1 

    return smallerLists