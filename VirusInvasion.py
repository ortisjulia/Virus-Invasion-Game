# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 12:29:44 2020

@author: ortis
"""

#!/usr/bin/python3
'''
    Title: VirusInvasion.py
    Date: 2020-10-30
    Author: Julia Ortis Sunyer
    Description:
        This code creates the game Virus Invasion, which consists on shooting vaccines at
        viruses that keep coming to infect a scientist. In order to run it, you need to have
        all the files that this code uses (images, music, etc.) in the same folder so that
        the code can recognize it and use it. Then by just running the code the game will
        work.
    List of functions:
        - player(), to load the scientist
        - enemy(), to load the viruses
        - show_score(), to show the score in the upper left corner
        - fire_bullet(), to fire the vaccine at the virus
        - isCollision(), for when the vaccine collides with the virus
        - game_intro(), for the title page of the game that is shown before the game starts
        - game_over_text(), to show GAME OVER and stop the game when the virus infect the scientist
    List of non-standard modules:
        - Pygame, to create the game
        - Mixer, from pygame, for the music
    Procedure:
        First I imported all the modules necessary for the game, pygame, mixer, random and math.
        Then, I initialized the game and created the different variables that I am going to use
        throughout the code. After creating all the necessary variables, I create the functions
        that I will call during the game loop. The functions I used are all explained in the 
        list of functions section. After doing all this, I can create the game loop and call
        the functions and use the variables when necessary. At the end of the loop, I update
        the display so that the game works properly.
    Usage:
        VirusInvasion.py
    Acknowledgements:
    The images used were obtained from:
        - Icons made by <a href="https://www.flaticon.com/authors/smashicons" title="Smashicons">Smashicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
        - <a href='https://www.freepik.com/vectors/school'>School vector created by upklyak - www.freepik.com</a>
    The music is from:
        - zapsplat.com
'''

'''First, I import all the modules I need to develop the game. Pygame is the module
that allows me to create the full game. Mixer from pygame allows me to add music and
sounds to the game. Radom creates random numbers so that the viruses appear at random
spots in the screen and math allows me to use math functions'''
import pygame
from pygame import mixer
import random
import math

'''Initialize the game, very imporant. The game does not work if you do not do that'''
pygame.init()

'''Create the screen, background, background sound, tile and icon, scientist, 
virus, vaccine and score'''
#Screen
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load('lab2.png')

#Title and icon
pygame.display.set_caption("Virus Invasion")
icon = pygame.image.load('virusicon.png')
pygame.display.set_icon(icon)

#Scientist
playerImg = pygame.image.load('scientist3.png')
playerX = 340 #X coordinate of the scientist
playerY = 450 #Y coordinate of the scientist
playerX_change = 0

#Virus
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 30
for i in range(num_of_enemies):   #I use a for loop and lists to create more than one enemy
    enemyImg.append(pygame.image.load('virus.png'))
    enemyX.append(random.randint(0, 735)) #Coordinates of where the virus can be
    enemyY.append(random.randint(50, 150)) #Coordinates of where the virus can be
    enemyX_change.append(4)
    enemyY_change.append(40)

#Vaccine
bulletImg = pygame.image.load('syringe.png')
bulletX = 0 #X coordinate of the vaccine
bulletY = 480 #Y coordinate of the vaccine
bulletX_change = 0
bulletY_change = 5
bullet_state = 'ready'

#Score (it increases when the vaccine hits the virus)
score_value = 0
font = pygame.font.Font('University.otf', 20)
textX = 10
textY = 10

#Intro text:
intro_font = pygame.font.Font('ARCADE.otf', 64)
intro_font2 = pygame.font.Font('ARCADE.otf', 30)
intro_font3 = pygame.font.Font('ARCADE.otf', 30)
intro_font4 = pygame.font.Font('ARCADE.otf', 30)

#Intro background:
intro_background = pygame.image.load('virusintro.png')

#Game Over text:
over_font = pygame.font.Font('ARCADE.otf', 64)
over_font2 = pygame.font.Font('ARCADE.otf', 30)
    
'''Functions used in the game'''
#Function player with the image and the coordinates we want to place the scientist image in the screen
def player(x, y):
    screen.blit(playerImg, (x, y))

#Function enemy with the image and the coordinates we want to place the virus image in the screen
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

#Function show score so that the score is shown in white at the top left corner of the screen
def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (0,0,0))
    screen.blit(score, (x, y))

#In fire the vaccine is currently moving. That's why I create the function fire
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10)) #So the bullet appears at the right spot in the screen

#Function for when the virus is hit
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#Function for game intro
def game_intro():
    #Background music for the game intro
    mixer.music.load('intro2.wav')
    mixer.music.play(-1) 
    
    intro = True
    
    while intro:
        #Values for RGB to implement colors on the screen. Max value 255
        screen.fill((255, 255, 255))
    
        #Background image
        screen.blit(intro_background, (0,0))
        
        #Intro title (the name of the game)
        intro_text = intro_font.render('VIRUS INVASION!', True, (0,0,0))
        screen.blit(intro_text, (130, 250))
    
        #Intro title (the instructions to play)
        intro_text2 = intro_font2.render('Help the scientist destroy all the viruses!', True, (0,0,0))
        screen.blit(intro_text2, (50, 300))
    
        #Intro title (instructions to start the game)
        intro_text3 = intro_font3.render('Press space to start the game', True, (0,0,0))
        screen.blit(intro_text3, (150, 500))
        
        #Intro title (instructions to stop running the game)
        intro_text4 = intro_font4.render('Press e to exit', True, (0,0,0))
        screen.blit(intro_text4, (270, 550))
        
        #For loop to control the start of the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global running
                intro = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #to get into the game loop
                    pygame.mixer.music.stop() #To stop the intro music
                    intro = False
                    running = True
                if event.key == pygame.K_e: #the game stops running
                    pygame.mixer.music.stop()
                    intro = False
                    running = False
        pygame.display.update()

#Function to show the game over text in the middle of the screen when the virus gets to the scientist
def game_over_text():
    over_text = over_font.render('GAME OVER', True, (0,0,0))
    screen.blit(over_text, (200, 250))
    over_text2 = over_font2.render('THE SCIENTIST HAS BEEN INFECTED!', True, (0,0,0))
    screen.blit(over_text2, (100, 200))
    
'''Game loop'''
#First the game intro
game_intro()

#Background music for the game play
mixer.music.load('background.mp3')
mixer.music.play(-1) #The minus one is so that the music plays on a loop

#To run the game
while running:
    #Values for RGB to implement colors on the screen. Max value 255
    screen.fill((0, 0, 0))
    
    #Background image
    screen.blit(background, (0, 0))
    
    #For loop to control the movement of the scientist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    pygame.mixer.Sound.set_volume(bullet_sound, 0.2)
                    bulletX = playerX #to get the current x coordinate of the spaceship
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    #Checking for boundries of scientist so it doesn't go out of bounds
    playerX += playerX_change
    ##To avoid the scientist to leave the screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 672:
        playerX = 672
    
    #Checking for boundries of the virus so it doesn't go out of bounds
    for i in range(num_of_enemies):
        #Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        #To avoid that the virus leaves the screen
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i] #to change the Y coordinate when it hits the wall
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]
        #Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            pygame.mixer.Sound.set_volume(explosion_sound, 0.1)
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        #Call the virus after the screen so it is drawn after the screen in drawn
        enemy(enemyX[i], enemyY[i], i)
    
    #Vaccine movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    #Call the scientist after the screen so it is drawn after the screen in drawn
    player(playerX, playerY)
    show_score(textX, textY)
    
    #To update the screen:
    pygame.display.update()