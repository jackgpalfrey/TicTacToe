import pygame
from Utils.RGBcolors import AllColors as Color

WIDTH = 600
HEIGHT = 600

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TicTacToe")


class Grid():
    def __init__(self,win,width,height,xOffset,yOffset):
        self.win = win
        self.grid = [[Color.LIGHT_GREY,Color.LIGHT_GREY,Color.LIGHT_GREY]
                    ,[Color.LIGHT_GREY,Color.LIGHT_GREY,Color.LIGHT_GREY]
                    ,[Color.LIGHT_GREY,Color.LIGHT_GREY,Color.LIGHT_GREY]]

        self.width = width
        self.height = height
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.xNodeSize = width / 3
        self.yNodeSize = height / 3


    def getColor(self,row,col):
        return self.grid[row][col]

    def changeState(self,row,col,val):
        self.grid[row][col] = val

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
        players = [Color.RED,Color.BLUE]
        for color in players:
            if self.grid[0][0] == color and self.grid[0][1] == color and self.grid[0][2] == color: return winFunc(self.win,color)
            elif self.grid[1][0] == color and self.grid[1][1] == color and self.grid[1][2] == color: return winFunc(self.win,color)
            elif self.grid[2][0] == color and self.grid[2][1] == color and self.grid[2][2] == color: return winFunc(self.win,color)
            elif self.grid[0][0] == color and self.grid[1][0] == color and self.grid[2][0] == color: return winFunc(self.win,color)
            elif self.grid[0][1] == color and self.grid[1][1] == color and self.grid[2][1] == color: return winFunc(self.win,color)
            elif self.grid[0][2] == color and self.grid[1][2] == color and self.grid[2][2] == color: return winFunc(self.win,color)
            elif self.grid[0][0] == color and self.grid[1][1] == color and self.grid[2][2] == color: return winFunc(self.win,color)
            elif self.grid[2][0] == color and self.grid[1][1] == color and self.grid[0][2] == color: return winFunc(self.win,color)
            




grid = Grid(win,600,600,0,0)
win.fill(Color.WHITE)
pygame.display.update()




def win(win,color):
    win.fill(color)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

playerR = True


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
            if grid.getColor(int(row),int(col)) == Color.LIGHT_GREY:
                if playerR:
                    grid.changeState(int(row),int(col),Color.RED)
                else:
                    grid.changeState(int(row),int(col),Color.BLUE)
                
                playerR = not playerR

        
pygame.quit()