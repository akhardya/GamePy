#!/usr/bin/python

import pygame
import sys

# Variable globales
playerSprite=None
playerRect=None
explosionSprite=None
explosionPos=[]

# Fonctions
def loadData():
    global playerSprite
    global playerRect
    global explosionPos
    global explosionSprite
   
    playerSprite = pygame.image.load("./Data/player.png")
    playerRect = playerSprite.get_rect()
    explosionSprite = pygame.image.load("./Data/bullet_player.png")

pygame.display.set_caption('Shoot me up')

def display():
    screen.fill((30,30,50))
    screen.blit(playerSprite,playerRect)
    pygame.display.flip()

def explosionUpdate(deltaTime):
	explosionTimeCounter += deltaTime
	explosionStep = explosionTimeCounter/100
	imageX = explosionStep % 5
	imageY = explosionStep / 5
	screen.blit(explosionSprite,explosionPos,[64*imageX,64*imageY,64,64])

def update(deltaTime):
    global explosionPos

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keysState = pygame.key.get_pressed()
    if keysState[pygame.K_ESCAPE]:
        sys.exit()
    if keysState[pygame.K_RIGHT]:
        playerRect.x+=1 * deltaTime
    if keysState[pygame.K_LEFT]:
        playerRect.x-=1 * deltaTime
    if keysState[pygame.K_DOWN]:
    	playerRect.y+=1 * deltaTime
    if keysState[pygame.K_UP]:
    	playerRect.y-=1 * deltaTime
    if keysState[pygame.K_SPACE]:
        print explosionPos
        explosionPos.append(pygame.Rect(playerRect.x,playerRect.y,explosionSprite.get_width(),explosionSprite.get_height()))


pygame.init()

screen = pygame.display.set_mode((800,640))

loadData()

fpsLimiter = pygame.time.Clock()
nbFrames = 0
deltaTime = 0
oldTime = 0

while 1:
    display()
    update(deltaTime)
    fpsLimiter.tick(60)
    curTime = pygame.time.get_ticks()
    deltaTime = curTime - oldTime
    oldTime = curTime
    if pygame.time.get_ticks() - oldTime > 1000:
            print "FPS : " + str(nbFrames)
            oldTime = pygame.time.get_ticks()
            nbFrames = 0


