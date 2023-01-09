from collections import Counter

boardWidth = 3 
possibleAll = ['','|','-','+']
possibleTaken = ['|','-','+']
#This class is for setting up each game - all attributes are common to all games 
class Game: 
    def __init__(self):
        self.board = [['','',''],['','',''],['','','']]

class Player: 
    def __init__(self): 
        self.turn = None
        self.symbol = None

class Hero(Player): 
    def __init__ (self, turn, symbol): 
        super().__init__()
        self.turn = True
        self.symbol = '-'

class Villain(Player): 
    def __init__ (self, turn, symbol): 
        super().__init__()
        self.turn = False
        self.symbol = '|'
#print(hero1.turn)
#print(villain1.turn)

#This function checks the condition of winning 
def isOver(game): 
    column0 = []
    column1 = [] 
    column2 = []
    columns = [column0, column1, column2]
    diagonalf = []
    diagonalb = [] 
    diagonals = [diagonalf, diagonalb]
    for row in game.board: 
        column0.append(row[0])
        column1.append(row[1])
        column2.append(row[2])
        for possible in possibleTaken: 
            #print(Counter(row)[possible])
            #This part checks for rows 
            if Counter(row)[possible] == 3: 
                return True 
    for column in columns: 
        for possible in possibleTaken:
            #This part checks for columns 
            if Counter(column)[possible] == 3: 
                return True
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
                return True

#This function is for checking whose turn it is 
def checkTurn(hero, villain): 
    if hero.turn == True: 
        return hero 
    if villain.turn == True:
        return villain 
    #else: 
        #return None

#This function is for having one turn 
def haveTurn(player): 
    pass


#This function is for having one full game 
def haveGame(hero,villain):
    pass

game1 = Game()
#print(game1.board)
for i in range(boardWidth): 
    print(game1.board[i])

hero1 = Hero(None) 
villain1 = Villain(None) 

if isOver: 
    pass 
else: 
    turn = checkTurn(hero, villain)
    #if turn == None: 
        #break 
    haveTurn(turn) 


while not isOver: 
    checkTurn(hero1)
    haveTurn(villain1)

#This function is for having a new game 



global hero10
hero10 = 123
