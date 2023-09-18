from enum import Enum
import random

class Difficulty(Enum):
    '''
    tuples representing the difficult of a game
    in the format (x, y, n) when x is the number of rows, y
    is the number of columns and n is the number of mine on the map
    '''
    easy = (9, 9, 10)
    medium = (16, 16, 40)
    hard = (16, 30, 99)


class Board():
    MAX_Flags = 99
    EMPTY = 0
    MINE = 1
    def __init__(self, diff: Difficulty):
        self.numMines = diff.value[2]
        self.rows = diff.value[0]
        self.cols = diff.value[1]
        self.board = [[Board.EMPTY for _ in range(diff.value[1])] for _ in range(diff.value[0])] # index might need to be fixed later can't think of it right now
        self.visibleBoard = {} # list of tuples for coordinates and their values
        self.flagLocations = []

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


    def checkCell(self, x, y):
        # 
        if not(0 <= x < self.rows and 0 <= y < self.cols):
            raise Exception("invalid")
        if not self.visibleBoard: # might not work with dictionary
            self.generateMines(x, y)
        if self.board[x][y] == Board.MINE:
            print("you lost")
            return
        self.revealCells(x, y)


    def revealCells(self, x, y):  # island is a patch of tiles with no mine
        if (x,y) in self.visibleBoard:
            return
    
        mines = self.checkSurroundings(x, y)
        self.visibleBoard[(x, y)] = mines

        if mines != 0:
            self.visibleBoard[(x, y)] =  mines
            return
        for col in range(max(x-1, 0), min(x+2, self.cols), 2):
            self.revealCells(col, y)
        for row in range(max(y-1, 0), min(y+2, self.cols), 2):
            self.revealCells(x, row)
 
    '''
        1. pass in a "seed point"
        2. check the value at that point
        3. reveal that point
        4. if mines is non-zero (has bombs around) reveal the cell with the value and exit out (since it's not an island)
        5. otherwise call the function on all other squares NOT in visible board
    '''

    def checkSurroundings(self, x, y):
        s = 0
        for x in range(max(x-1, 0), min(x+2, self.cols)):
            for y in range(max(y-1, 0), min(y+2, self.rows)):
                s += self.board[x][y]
        return s

    def generateMines(self, x, y):
        '''
        generates the mine based off the first x,y
        '''
        locations = [(x, y) for x in range(self.cols) for y in range(self.rows)]
        locations.remove((x,y))
        locations = random.sample(locations, k=self.numMines)
        for xCord, yCord in locations:
            self.board[xCord][yCord] = Board.MINE

    def printBoard(self):
        for x in range(self.rows):
            for y in range(self.cols):
                # check if the square is visible
                if (x, y) in self.visibleBoard:
                    print(self.visibleBoard[(x,y)], end = ' ')
                elif (x, y) in self.flagLocations:
                    print('F', end=' ')
                else:
                    print('*', end=' ')
            print()
    
    
board = Board(Difficulty.hard)
board.printBoard()
print()
print()
print()
board.checkCell(1, 5)
board.printBoard()