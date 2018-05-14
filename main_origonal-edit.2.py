"""I took most of this code from  https://www.youtube.com/user/sentdex. I used his code to create an avoidance 
game focused around soccer.
"""
#imports the libraries I will use 
import pygame
import random
import time
import class_MainWindow

pygame.init()

#dimensions of the screen
display_width = 600
display_height = 826

#colors that i will use later
black = (0,0,0)
white= (255,255,255)

#the dimensions of the player
player_width = 60 
player_height = 131

#sets variables for things I will use later
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

#images for the game including: player, background, defender1&2
player_Image = pygame.image.load('C:/Users/Gianluca.Mavica19/OneDrive - Bellarmine College Preparatory/Desktop/2018 S2/Intro_to_CS/Mavica_Gianluca/final project/resources/zlatan_psg_running.png')
background_Image = pygame.image.load('C:/Users/Gianluca.Mavica19/OneDrive - Bellarmine College Preparatory/Desktop/2018 S2/Intro_to_CS/Mavica_Gianluca/final project/resources/soccer_field.1.png')
thing = pygame.image.load('C:/Users/Gianluca.Mavica19/OneDrive - Bellarmine College Preparatory/Desktop/2018 S2/Intro_to_CS/Mavica_Gianluca/final project/resources/sergio_ramos.png')
thing2 = pygame.image.load('C:/Users/Gianluca.Mavica19/OneDrive - Bellarmine College Preparatory/Desktop/2018 S2/Intro_to_CS/Mavica_Gianluca/final project/resources/sergio_ramos.png')

#function that counts how many defenders the user has dodged
def things_dodged(count):
    font = pygame.font.SysFont(None, 50)
    text= font.render("Dodged: " + str(count), True , black)
    gameDisplay.blit(text, (0,0))

#function that brings up the image of the player and sets its location in the game
def player(x,y):
    gameDisplay.blit(player_Image,(x,y))

#function that brings up the image of the defeder1 and sets its location on the screen
def things(thingx, thingy):
    gameDisplay.blit(thing, (thingx, thingy))

#function that brings up the image of the defender2 and sets its location on the screen
def things2(thing2x, thing2y):
    gameDisplay.blit(thing2, (thing2x, thing2y))

#function that puts of the text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#function that creates the formating for the text 
def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf", 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

    time.sleep(2)

    game_loop()

#function that displays a message when the user hits the defender
def crash():
    message_display("Foul!")

#funstion that displays a message when the user goes out of bounds
def out_of_bounds():
    message_display("Stay in bounds")


#function that loops the game
def game_loop():
    #puts the plaeyr on the screen in a certain location
    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0 

#sets defender2's location and speed
    thing2_startx = random.randrange(0, display_width)
    thing2_starty = -200
    thing2_speed = 20

#sets defender1's location and speed
    thing_startx = random.randrange(0, display_width)
    thing_starty = -200
    thing_speed = 15
#sets the dimensions of defender2
    thing2_width = 85
    thing2_height = 214 

#sets the dimenstions for defender1
    thing_width = 85
    thing_height = 214

#sets the original amount of defenders dodged to - 
    dodged = 0  
    
    #boolean that says, when the game is exit dont run
    gameExit = False

#while loop that does stuff when the game is not exited
    while not gameExit:
        #when you click the "x" button the game will exit 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
#when there is a key down do this:
            if event.type == pygame.KEYDOWN:
                #is the key pressed is the left arrow key move the image -15 pixles right
                if event.key == pygame.K_LEFT:
                    x_change = -15
                #if the key pressed is the right arrow key move the image 15 pixles right 
                if event.key == pygame.K_RIGHT:
                    x_change = 15

#makes it so you can hold down the key 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

#keeps changing the x value of the player 
        x += x_change
        #makes the game display all white
        gameDisplay.fill(white)
        #puts the background image on the screen
        gameDisplay.blit(background_Image, [0,0])
        #puts defender 1 on the screen 
        things(thing_startx, thing_starty)
        #moves  defender1 at is given speed
        thing_starty += thing_speed
        #moves defender 2 at its given speed
        thing2_starty += thing2_speed
        #puts the player on the screen
        player(x,y)
        #starts the function that counts how many defenders have been dodged
        things_dodged(dodged)

#it the player goes our of bounds that he is it runs the out of bounds function 
        if x > display_width - player_width or x < 0:
            out_of_bounds()

#if the player dedges the defender then mae the defender faster, up to a certain point 
        if thing_starty > display_height:
            thing_starty = 0- thing_height
            thing_startx = random.randrange(0,display_width)
            dodged +=1
            thing_speed += 2 <25

# controls the collisions for defender1 
        if y < thing_starty + thing_height:
            print("y crossover")

            if x > thing_startx and x < thing_startx + thing_width or x+ player_width > thing_startx and x + player_width < thing_startx + thing_width:
                print("x crossover")
                crash()

#if the player has dodged 2 or more defender then add defender2
        if dodged > 2:
            things2(thing2_startx, thing2_starty)

            if thing2_starty > display_height:
                thing2_starty = 0- thing2_height
                thing2_startx = random.randrange(0,display_width)
                dodged +=1
                thing2_speed +=5 <30 

#controls colisions for defender2
            if y < thing2_starty + thing2_height:
                print("y crossover")

                if x > thing2_startx and x < thing2_startx + thing2_width or x+ player_width > thing2_startx and x + player_width < thing2_startx + thing2_width:
                    print("x crossover")
                    crash()

#updates the screen 
        pygame.display.update()
        
        #FPS
        clock.tick(60)

#starts the game_loop function
game_loop()
pygame.quit()
quit()