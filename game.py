import pygame
#initialize all imported pygame modules
pygame.init()

#initialize a screen for display
dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption("Welcome to Snake game!")
game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)
pygame.quit()
quit()