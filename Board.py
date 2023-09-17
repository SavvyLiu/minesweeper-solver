from enum import Enum

class Difficulty(Enum):
    '''
    tuples representing the difficult of a game
    in the format (x, y, n) when x is the number of rows, y
    is the number of columns and n is the number of bombs on the map
    '''
    easy = (9, 9, 10)
    medium = (16, 16, 40)
    hard = (16, 30, 99)


class Board():
    MAX_Flags = 99
    EMPTY = 0
    BOMB = 1
    def __init__(self, diff: Difficulty):
        numBombs = Difficulty[2]
        rows = diff[0]
        cols = diff[1]
        board = [[board.BOMB for _ in range(diff[1])] for _ in range(diff[0])] # index might need to be fixed later can't think of it right now
        visibleBoard = [] # list of tuples for coordinates and their values
        flagLocations = []

    def placeFlag(self, x, y):
        if not(0 <= x < self.cols and 0 <= y < self.rows):
            raise Exception("invalid coordinate for square")
        if len(self.flagLocations) > Board.MAX_Flags: # maybe print something here if it can't place anything
            return
        if (x, y) in self.flagLocations:
            return
        if (x, y) in self.visibleBoard: # shouldn't be able to flag known locations
            return
        self.flagLocations += (x, y)


    def Check(self, x, y):
        # 
        if not(0 <= x < self.rows and 0 <= y < self.cols):
            raise Exception("invalid")
        if not self.visibleBoard: 
            # do special first click  fdasfasdfasfasdfsdfas
            pass
        if self.board[x][y] == Board.BOMB: # check for bomb first
            # player die
            pass
        
        else: 
            if 
            #self.visibleBoard.append(x,y, BombCheck())
            self.visibleBoard.append(findIsland(x, y))


    def findIsland(self, x, y, points = []):  # island is a patch of tiles with no bombs
        bombs = self.BombCheck(self, x,y)
        # if the tuple (x, y, bombs) is already in visibile baord
        if bombs != 0 and :
            points.append((x, y, bombs))
        self.findIsland(x,y, points)
        
        return points


    def BombCheck(self, x, y):
        s = 0
        for y in range(min(y-1, 0), max(y+2, self.rows)):
            s += sum(self.board[min(x-1, 0): max(x+2, self.cols)])
        return s


