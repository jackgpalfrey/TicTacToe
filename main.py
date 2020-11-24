import pygame

WIDTH = 800
HEIGHT = 800

win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Testing123")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()