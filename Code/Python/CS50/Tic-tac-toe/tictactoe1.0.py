from collections import Counter

#Program-long variable which can be used to store anything for the whole running of the program
class ProgramLong: 
    def __init__(self): 
        self.gameNumber = 0

programLong = ProgramLong()

boardWidth = 3 
possibleAll = ['','x','o']
possibleTaken = ['x','o']

#This class is for setting up each game - all attributes are common to all games 
class Game: 
    def __init__(self):
        self.board = [['','',''],['','',''],['','','']]
        self.isOver = False

class Player: 
    def __init__(self): 
        self.turn = None
        self.symbol = None

class Hero(Player): 
    def __init__ (self, turn, symbol): 
        super().__init__()
        self.turn = True
        self.symbol = 'x'

class Villain(Player): 
    def __init__ (self, turn, symbol): 
        super().__init__()
        self.turn = False
        self.symbol = 'o'
    
#print(hero1.turn)
#print(villain1.turn)

#This function checks the condition of winning, and if it is over changes (game.over)
def checkIfOver(game): 
    column0 = []
    column1 = [] 
    column2 = []
    columns = [column0, column1, column2]
    diagonalf = []
    diagonalb = [] 
    diagonals = [diagonalf, diagonalb]
    allSpaces = []
    for row in game.board: 
        column0.append(row[0])
        column1.append(row[1])
        column2.append(row[2])
        for space in row: 
            #print(space)
            allSpaces.append(space)
        for possible in possibleTaken: 
            #print(Counter(row)[possible])
            #This part checks for rows 
            if Counter(row)[possible] == 3: 
                print('row')
                game.isOver = True
    for column in columns: 
        for possible in possibleTaken:
            #This part checks for columns 
            if Counter(column)[possible] == 3: 
                print('column')
                game.isOver = True
    diagonalf.append(game.board[0][0])
    diagonalf.append(game.board[1][1])
    diagonalf.append(game.board[2][2])
    diagonalb.append(game.board[0][2])
    diagonalb.append(game.board[1][1])
    diagonalb.append(game.board[2][0])
    for diagonal in diagonals: 
        for possible in possibleTaken:
            #This part checks for diagonals
            if Counter(diagonal)[possible] == 3:
                print('diagonal')
                game.isOver = True
    if Counter(allSpaces)[''] == 0: 
        game.isOver = True

#This function is for checking whose turn it is 
def checkTurn(hero, villain): 
    if hero.turn == True: 
        return hero, villain
    if villain.turn == True:
        return villain, hero
    #else: 
        #return None

#This function is for having one turn - playing a single move 
#It requires the objects of whose turn it is and isn't 
def playMove(player, notPlayer): 
    player.turn = False 
    notPlayer.turn = True

#This function sets up the game 
def setupGame(): 
    exec(f'game{programLong.gameNumber} = Game()')
    exec(f'hero{programLong.gameNumber} = Hero(None,None)')
    exec(f'villain{programLong.gameNumber} = Villain(None,None)')
    
    print(game0)
    

#This function is for having one full game 
def haveGame():
    setupGame()
    while not game1.isOver:
        #ONE TURN
        checkIfOver(game1)
        print(f'The game is over: {game1.isOver}')
        if not game1.isOver: 
            #This should trigger if the game is not over yet 
            #Returns the object of whose turn it is 
            turn, notTurn = checkTurn(hero1, villain1)
            #if turn == None: 
                #break 
            print(turn)
            playMove(turn, notTurn) 
            #game1.over = True
        else: 
            #This should trigger if the game is over
            print('over')
            print(game1.isOver)

        programLong.gameNumber += 1 




haveGame()


#GAME SETUP
#Need to use exec to create game, hero, villain 
#In each game when using haveGame
game1 = Game()
#print(game1.board)
for i in range(boardWidth): 
    print(game1.board[i])
hero1 = Hero(None, None) 
villain1 = Villain(None, None) 




#This function is for having a new game 





#Test case for over game 
overGame = Game()
overGame.board[1] = ['x','x','x']
#print(overGame.board)
#isOver(overGame)
print(overGame.isOver)