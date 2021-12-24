import pygame
import random
import math
from pygame import mixer
import os
from Menu import main_menu

# We need to put this to initialize pygame and use pygame functions
#Initialize the Game

pygame.init()

#Background image
background = pygame.image.load(f"images/4161657.jpg")

#background sound
mixer.music.load(f"images/Music/Pop_Smoke_-_Tsunami_Audio_ft_Dav_(getmp3.pro).mp3")
mixer.music.play(-1) #to play on loop -1

#we need this to set the screen for the user also the first input is the size of the screen
screen = pygame.display.set_mode((800,600)) #800 is the widhth and 600 the height

#Title and icon
pygame.display.set_caption("Crazy octopus vs Poseidon") #how to find a title to your game
icon = pygame.image.load(f"images/trident.png") #how to access an image
pygame.display.set_icon(icon)  #Icon of the app

#player
playerImg = pygame.image.load(f"images/poseidon-2.png")
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change =[]
number_of_enemies = 10

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load(f"images/octopus.png"))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.4)
    enemyY_change.append(40)

#bullet
# ready - you can't see the bullet on the screen
# fire _ the bullet is currently moving
bulletImg = pygame.image.load(f"images/storm.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"

#Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX, textY = 10,10

#Game Over Text
over_font = pygame.font.Font("freesansbold.ttf", 128)

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = font.render("GAME OVER LOOSER", True, (255, 255, 255))
    screen.blit(over_text, (200,250))

def player(x,y):
    screen.blit(playerImg, (x,y)) #draw our character on the screen with blit

def enemy(x,y, i):
    screen.blit(enemyImg[i], (x,y)) #draw our enemy on the screen with blit

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

def isCollission(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    if distance < 27 :
        return True
    else:
        return False

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Game Framerate
clock = pygame.time.Clock()
FPS=30

#this allow the programm to not close the window until the game end or you quit
running = True
show_menu = True
while running:
    if show_menu:
        main_menu()
        pygame.time.delay(1500)
        show_menu = False
        clock.tick(5)
    # RGB - red, green, blue (the value 255 is the color so you can mix the value to do all the colours)
    screen.fill((0, 255, 255))
    #add the background for the entierity of the game
    screen.blit(background, (0,0))

    #event is anything happening on the game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if the keystroke for movement are pressed the player can start to move
        if event.type == pygame.KEYDOWN:  #Keydown is pressend the button if it's key up it'S release the button
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound(f"images/Music/thunder_sound_effect_-6204590353607357141.mp3")
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            else :
                continue

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change
    #this allow us to create boundaries for our game
    if 0 >= playerX:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    #enemy movement
    for i in range(number_of_enemies):

        #Game Over
        if enemyY[i] > 440:
            for j in range(number_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if 0 >= enemyX[i]:
            enemyX_change[i] = 0.4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.4
            enemyY[i] += enemyY_change[i]

            # Collision
        collision = isCollission(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound(f"images/Music/big_explosion_effect_video_mp4_hd_sound_-6447227997374597740.mp3")
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)


    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state ==  "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY) #to make the character appear on the screen
    # for one enemy : enemy(enemyX, enemyY) #make the enemy appear on the display
    show_score(textX, textY)
    pygame.display.update() #update the screen with the game when it'S change