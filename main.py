#Week 1:
#Week 2:
#make comments for all code



#imports of all of the 
import pygame 
import time
import random
#imports the librarys so I can use them in this file

pygame.init()
#initiates pygame and all the modlues in it 
display_width = 800
display_height = 600
# did this so that when i want to refrence screen width or height later, its easier  

#####player_width= 
#create a player and input image upthere here

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
#defines what the colors are RGB


gameDisplay = pygame.display.set_mode((display_width,display_height))
# this makes the windows width and height 
pygame.display.set_caption('Soccer Run')
#sets the title of the window to "soccer run"
clock = pygame.time.Clock()
#times the FPS of the game


playerZIMG = pygame.image.load('zlatan1animated.png')
#changed the name, for my game; loads up the image, gets it ready
def defenders(defenderx, defendery):
    #put the defenders at a x,y location


def player(x,y):
    #defines the player function 
    gameDisplay.blit((playerZIMG), (x,y)) 
    #puts the image at x,y


def text_objects(text, font)
    #defines the object text_objects
    textSurface = font.render(Text, True, black)
    #makes the text surface able to be used and makes it black
    return textSurface, textSurface.get_rect()
    #uses the surface and the rectangle to center the text 

def message_display(text):
    #defnies the function for when we want to display a message
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    #sets the font type and size 
    TextSurf, TextRect = text_objects(text, largeText)
    #returns the text surface and the text rectangle 
    TextRect.center = ((display_width/2),(display_height/2))
    #put the text in half the width and height, so it is in the middle of the screen
    gameDisplay.blit(TextSurf, TextRect)
    #puts the text on the surface, which is contained within the rectangle 
    pygame.display.update()
    #updates the new display 

    time.sleep(2)
    #puts the message up for 2 secconds 

    game_loop()
    #after the message is gone, then the game starts over agian 



def collision():
    #function for when the player collides with one of the defenders
    message_display("The defence got you")
    #then display "the defence got you"

def game_loop():
    #defines the function of the game looping 
    x = (display_width * 0.45)
    #moves the image twoards the center, because images are refrenced by the top left
    y = (display_height * 0.8)
    #moves the image twoards the center, because images are refrenced by the top left

    x_change = 0
    #varibale to change the location of the car

defenders_startx = random.randrange(0 display_width)
#makes the defenders start anywhere between the far left and far right of the screen
defenders_starty = random.range-600
#makes the defenders appear off screen 600 pixles before they go on the real screen so they dont just randomly pop up
defender_speed = 7
#makes the defenders move 7 pixles per seccond

    gameExit = False
    #the game is not exited

    while not gameExit:
        #while the game is not exited do the following, it will loop:
        for event in pygame.event.get():
            #gets any event that happens, where is mouse?, what keys are being pressed?, etc.; 
            if event.type == pygame.QUIT:
                #asks is the user wants to quit/ exit the window
                quit()
                #if they click to quit then close the window

            if event.type == pygame.KEYDOWN:
                #asks is there was any key pressed down at all
                if event.key == pygame.K_LEFT:
                    #if the left arrow key was pressed them move x 10 pixles left
                    x_change = -10
                    #subtracts 10 pixles from the x value
                if event.key == pygame.K_RIGHT:
                    #if the right arrow key was pressed then moved x 10 pixles right
                    x_change = 10
                    #adds 10 pixlesthe x values

            if event.type == pygame.KEYUP:
                #when ANY key is released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    #if the key was left or right arrow
                    x_change = 0
                    #then there is no change to x, 

        x += x_change
        #chagnes how much x changes and saves the previous change 
        gameDisplay.fill(white)
        #fill the background with white

        defenders(defenders_startx, defenders_starty)
        #uses the random starting value of the defenders 
        defenders_starty += defenders_speed
        # the defenders will be 7 pixles lower eachtime a defender appears in the game 

        player(x,y)
        #puts the player/image at x,y

        if x > 600 - player_width or x > 300
            #if this happens, need to fingure out how to make the car stop moveing 

        if defenders_starty > display_height
            #if the defender is off the screen then:
            defenders_starty = 0 - defenders_height
            #after a block goes off the screen, the next one imediatly shows up 
            defenders_startx = random.randrange(0,display_width)
            #makes it so the x value will always be random, the blocks will always be in a different spot 

        pygame.display.update()
        #updates the entire window 
        clock.tick(60)
        #how many FPS the game will run 

game_loop()
#actualy runs the function "game_loop"
pygame.quit()
#uninits pygame/ stops it fromm running
quit()



#https://www.youtube.com/user/sentdex/videos