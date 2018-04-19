#Week 1:
#Week 2:
#make comments for all code



#imports of all of the 
import pygame 
import time
import random

pygame.init()
display_width = 800
display_height = 600

#player_width= 
#create a player and input image upthere here

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Soccer Run')
clock = pygame.time.Clock()


playerZIMG = pygame.image.load('zlatan1animated.png')

def defenders(defenderx, defendery):


def player(x,y):
    gameDisplay.blit((player1IMG), (x,y)) 


def text_objects(text, font)
    textSurface = font.render(Text, True, blue)
    return textSurface, textSurface/get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()



def collision():
    message_display("The defence got you")

def game_loop():
    x = (display_width * 0.45)
    y = (display_hight * 0.8)

    x_change = 0

defenders_startx = random.randrange(0 display_width)
defenders_starty = random.range-600
defender_speed = 7

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)


        defenders(defenders_startx, defenders_starty)
        defenders_starty += defenders_speed
        player(x,y)

        if x > 600 - player_width or x > 300
            #if this happens how can i stop movement?

        if defenders_starty > display_height
            defenders_starty = 0 - defenders_height
            defenders_startx = random.randrange(0,display_width)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()



#https://www.youtube.com/user/sentdex/videos