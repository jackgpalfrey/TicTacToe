# Imports
import pygame
from Utils.RGBcolors import AllColors as Color
import time

# Window Settings
WIDTH = 750
HEIGHT = 775

# Window Setup
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TicTacToe")
programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)


class Grid():
    def __init__(self,win,width,height,xOffset,yOffset):
        """ Creates Grid Object

        Args:
            win (Surface): The Game WIndow
            width (int): Width of Grid
            height (int): Height of Grid
            xOffset (int): Offset From LEft
            yOffset (int): Offset from top
        """
        self.win = win
        self.default = Color.LIGHT_GREY
        self.player1 = Color.PINK
        self.player2 = Color.TURQUOISE
        self.width = width
        self.height = height
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.turns = 0
        self.gridSize = 3 # Number of Squares in grid on an axis  - Full number of squares is n**2


        self.reset() # Creates grid data structure

    def createGrid(self,size):
        """ Creates Grid Data Structure id 2d Array

        Args:
            size (int): Number of Squares in grid on an axis

        Returns:
            array: Array data structure of grid
        """
        grid = [] # Creates empyty array

        # Creates Nodes in array
        for i in range(size):
            grid.append([])
            for y in range(size):
                grid[i].append(self.default)
        
        # Gets node sizes
        self.size = size
        self.xNodeSize = self.width / size
        self.yNodeSize = self.height / size
        self.grid = grid # Sets class-wide grid varaible to the grid
        return self.grid # Returns the grid


    def getPlayer(self,row,col):
        """ Gets The Player in a specific node

        Args:
            row (int): Row position
            col (int): Collumn postion

        Returns:
            int: 0 = Default (No Player), 1 = Player 1, 2 = Player 2
        """
        try:
            color = self.grid[row][col]
        except:
            return False
        player = 0
        if color == self.player1: player = 1
        elif color == self.player2: player = 2

        return player

    def changeState(self,row,col,player):
        """ Changest color of squares

        Args:
            row (int): Row Posiiton
            col (int): Collumn Position
            player (int): 0 = Default (No Player), 1 = Player 1, 2 = Player 2
        """
        # Sets color to player color
        color = self.default
        if player == 1: color = self.player1
        elif player == 2: color = self.player2
        self.grid[row][col] = color # Pushes color to actual Grid Array

    def reset(self):
        """ Resets back to empty grid
        """
        self.win.fill(Color.WHITE)
        self.grid = self.createGrid(self.gridSize)

    def findPos(self,pos):
        """ Get Row, Col posiiton in grid

        Args:
            pos (tuple): (x,y) pygame position

        Returns:
            tuple: (row,col) position in array
        """
        x,y = pos # Gets seperate x and y vars from pygame tuple

        # Finds Postion in Grid
        row = (x // self.xNodeSize) - self.xOffset
        col = (y // self.yNodeSize) - self.yOffset

        return (row,col) # Returns row and col
        
    def draw(self):
        """ Draws Grid
        """
        for row in range(len(self.grid)):
            xPos = self.xOffset + (self.xNodeSize * row)
            for col in range(len(self.grid[row])):
                color = self.grid[row][col]
                yPos = self.yOffset + (self.yNodeSize * col)
                pygame.draw.rect(self.win, color, (xPos,yPos,self.xNodeSize,self.yNodeSize))

        for row in range(1,len(self.grid)):
            xPos = self.xOffset + (self.xNodeSize * row)
            pygame.draw.line(self.win,Color.BLACK,(xPos, self.yOffset),(xPos, self.yOffset + self.height))
        for col in range(1,len(self.grid[1])):
            yPos = self.yOffset + (self.yNodeSize * col)
            pygame.draw.line(self.win,Color.BLACK,(self.xOffset, yPos),(self.xOffset + self.width, yPos))


    def winLogic(self,winFunc):
        """ Checks if anyone has won OR grid is fyll

        Args:
            winFunc (function): Runs if someone has won
        """
        playerColors = [self.player1,self.player2] # All Possible Players

        for playerColor in playerColors: # Cycles through for each player  
            # Creates  row and col points vars to store the number of claimed nodes in each row and col
            rowPoints = []
            colPoints = []
            for x in range(self.size):
                rowPoints.append(0)
                colPoints.append(0)
            
            # Creates diagonal points vars
            diagPointsL = 0
            diagPointsR = 0

            # Checks nodes and increments row and col points 
            for row in range(self.size):
                for col in range(self.size):
                    node = self.grid[row][col]
                    if node == playerColor:
                        colPoints[row] += 1
                        rowPoints[col] += 1

                        # Checks diagonals
                        if row == self.size - 1 - col:
                            diagPointsR += 1
                        if row == col:
                            diagPointsL += 1
                    



            # Checks if any rows, col or diagonals have suficient points
            for points in rowPoints:
                if points == self.size: win(self.win,playerColor)
            for points in colPoints:
                if points == self.size: win(self.win,playerColor)
            if diagPointsL == self.size: win(self.win,playerColor)
            if diagPointsR == self.size: win(self.win,playerColor)

        # Checks if grid is full
        full = 0         
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                node = self.grid[row][col]
                if node != self.default:
                    full += 1

        if full == (self.size ** 2):
            win(self.win,self.default)
         
# Creates Grid Object and prepares surface
grid = Grid(window,750,750,0,0,)
pygame.display.update()


def win(win,color):
    """ Turns whole Window the color of the winner and then  resets the grid

    Args:
        win (Surface): The Game Window
        color (tuple): RGB Color Value of Winner
    """
    global grid
    # Fulls window winners color
    win.fill(color) 
    pygame.display.update()

    time.sleep(0.3) # Waits .3 seconds
    grid.reset() # Resets Grid
    return


player1 = True # Sets whos turn it is to player 1

running = True
while running:   
    if player1:
        playerColor = grid.player1
    else:
        playerColor = grid.player2
    grid.draw() # Draws Grid
    pygame.draw.rect(window, playerColor, (0,WIDTH,WIDTH,25))
    pygame.draw.line(window,Color.BLACK,(0, grid.height),(WIDTH, grid.height))
    pygame.display.update()
    grid.winLogic(win) # Checks if any player has won
    for event in pygame.event.get():
        # Manages Quit Event
        if event.type == pygame.QUIT:
            running = False
            break
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                grid.reset()
                
            
        
        # Manages Click Event 
        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos() # Gets tuple mouse position
            row,col = grid.findPos(pos) # Gets row col position of click
            try:
                if grid.getPlayer(int(row),int(col)) == 0: # Checks if grid position is empty
                    if player1: # Checks if its player 1 turn
                        grid.changeState(int(row),int(col),1) # Sets node to Player 1 color
                        player1 = not player1 # Toggles player 1
                    else: # If not its player 2's turn
                        grid.changeState(int(row),int(col),2) # Sets node to player 2 color
                        player1 = not player1 # Toggles player 1
            except:
                pass
                
             

        
pygame.quit()
