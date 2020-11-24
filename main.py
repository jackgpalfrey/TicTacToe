import pygame
from Utils.RGBcolors import AllColors as Color

WIDTH = 600
HEIGHT = 600

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Testing123")


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




grid = Grid(win,600,600,0,0)
win.fill(Color.WHITE)
pygame.display.update()

while True:
    grid.draw()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        elif pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            row,col = grid.findPos(pos)
            grid.changeState(int(row),int(col),Color.RED)
        