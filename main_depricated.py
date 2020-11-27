import pygame
from Utils.RGBcolors import AllColors as Color
import time

WIDTH = 600
HEIGHT = 600

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TicTacToe")


class Grid():
    def __init__(self,win,width,height,xOffset,yOffset):
        self.win = win
        self.default = Color.LIGHT_GREY
        self.player1 = Color.PINK
        self.player2 = Color.TURQUOISE
        self.grid = [[self.default,self.default,self.default]
                    ,[self.default,self.default,self.default]
                    ,[self.default,self.default,self.default]]

        self.width = width
        self.height = height
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.xNodeSize = width / 3
        self.yNodeSize = height / 3
        self.turns = 0


    def getPlayer(self,row,col):
        color = self.grid[row][col]
        player = 0
        if color == self.player1: player = 1
        elif color == self.player2: player = 2

        return player

    def changeState(self,row,col,player):
        color = self.default
        if player == 1: color = self.player1
        elif player == 2: color = self.player2
        self.grid[row][col] = color

    def reset(self):
        self.grid = [[self.default,self.default,self.default]
                    ,[self.default,self.default,self.default]
                    ,[self.default,self.default,self.default]]
        self.turns = 0

    def findPos(self,pos):
        x,y = pos

        row = (x // self.xNodeSize) - self.xOffset
        col = (y // self.yNodeSize) - self.yOffset

        return (row,col)

    def draw(self):
        for row in range(len(self.grid)):
            xPos = self.xOffset + (self.xNodeSize * row)
            for col in range(len(self.grid[row])):
                color = self.grid[row][col]
                yPos = self.yOffset + (self.yNodeSize * col)
                pygame.draw.rect(self.win, color, (xPos,yPos,self.xNodeSize,self.yNodeSize))

        for row in range(len(self.grid) + 1):
            xPos = self.xOffset + (self.xNodeSize * row)
            pygame.draw.line(self.win,Color.BLACK,(xPos, self.yOffset),(xPos, self.yOffset + self.height))
        for col in range(len(self.grid[1]) + 1):
            yPos = self.yOffset + (self.yNodeSize * col)
            pygame.draw.line(self.win,Color.BLACK,(self.xOffset, yPos),(self.xOffset + self.width, yPos))


    def winLogic(self,winFunc):
        players = [self.player1,self.player2]
        for color in players:
            if self.grid[0][0] == color and self.grid[0][1] == color and self.grid[0][2] == color: return winFunc(self.win,color)
            elif self.grid[1][0] == color and self.grid[1][1] == color and self.grid[1][2] == color: return winFunc(self.win,color)
            elif self.grid[2][0] == color and self.grid[2][1] == color and self.grid[2][2] == color: return winFunc(self.win,color)
            elif self.grid[0][0] == color and self.grid[1][0] == color and self.grid[2][0] == color: return winFunc(self.win,color)
            elif self.grid[0][1] == color and self.grid[1][1] == color and self.grid[2][1] == color: return winFunc(self.win,color)
            elif self.grid[0][2] == color and self.grid[1][2] == color and self.grid[2][2] == color: return winFunc(self.win,color)
            elif self.grid[0][0] == color and self.grid[1][1] == color and self.grid[2][2] == color: return winFunc(self.win,color)
            elif self.grid[2][0] == color and self.grid[1][1] == color and self.grid[0][2] == color: return winFunc(self.win,color)

            elif self.grid[0][0] != self.default and self.grid[0][1] != self.default and self.grid[0][2] != self.default and self.grid[1][0] != self.default and self.grid[1][1] != self.default and self.grid[1][2] != self.default and self.grid[2][0] != self.default and self.grid[2][1] != self.default and self.grid[2][2] != self.default: win(self.win,self.default) 
            




grid = Grid(win,600,600,0,0)
win.fill(Color.WHITE)
pygame.display.update()




def win(win,color):
    global grid
    win.fill(color)
    pygame.display.update()
    time.sleep(0.3)
    grid = Grid(win,600,600,0,0)
    return



player1 = True


running = True
while running:   
    grid.draw()
    pygame.display.update()
    grid.winLogic(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        
        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            row,col = grid.findPos(pos)
            if grid.getPlayer(int(row),int(col)) == 0:
                if player1:
                    grid.changeState(int(row),int(col),1)
                else:
                    grid.changeState(int(row),int(col),2)
                
                player1 = not player1

        
pygame.quit()