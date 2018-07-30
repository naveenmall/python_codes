import pygame

#  lets define some colors
white = (255, 255, 255)  # mixture of all color lights (red , Green, Blue) RGB
black = (0, 0, 0)
red = (255, 0, 0)

pygame.init()
gameDisplay = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake Game")


exitGame = False

while not exitGame:
    gameDisplay.fill(white)
    for event in pygame.event.get():
        #  print(event)
        if event.type == pygame.QUIT:
            exitGame = True

    pygame.draw.rect(gameDisplay, red, [200, 200, 100, 40])
    #  alternate method
    gameDisplay.fill(black, rect=[205, 205, 40, 100])

    pygame.display.update()


pygame.quit()
quit()
