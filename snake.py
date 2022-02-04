import pygame
from pygame.locals import *
import random
import time
                
def snake(snakelist):
    snakeImg = pygame.image.load('cylinder1.png')
    for z in snakelist:
        # pygame.draw.rect(screen, black, [z[0], z[1], 10,10])
        snakeRect = snakeImg.get_rect(topleft = (z[0],z[1]))
        screen.blit(snakeImg,snakeRect)

def messege(msg,color):
    font_style = pygame.font.SysFont(None,50)
    msg = font_style.render(msg,True,color)
    screen.blit(msg, [screenwidth/2-100,screenHeight/2-10])

def score(score):
    score_font = pygame.font.SysFont("comicsansms", 25)
    value = score_font.render("Your Score: " + str(score), True, black)
    screen.blit(value, [10, 10])

pygame.init()

screenwidth = 500
screenHeight = 500
black = (0,0,0); brown = (100,50,25)

screen = pygame.display.set_mode((screenwidth,screenHeight))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

def gameLoop():
    x = 250
    y = 250
    x_change = y_change =0
    
    foodx = (random.randint(10,screenwidth-20)//10)*10
    foody = (random.randint(10,screenHeight-20)//10)*10
    frogImg = pygame.image.load('frog1.png')

    snakeList = []
    snakeLength = 1

    ask = False
    running = True
    while running:
        screen.fill((200,55,55))
        while ask:
            font_style = pygame.font.SysFont(None,30)
            msg = font_style.render('You lost! c:Continue, q:Quit',True,brown)
            screen.blit(msg, [130,screenHeight/4])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        ask = False
                        running = False
                    elif event.key == K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_LEFT:
                    x_change = -10; y_change = 0
                elif event.key == K_RIGHT:
                    x_change = 10; y_change = 0
                elif event.key == K_UP:
                    y_change = -10; x_change = 0
                elif event.key == K_DOWN:
                    y_change = 10; x_change = 0

        x = x + x_change
        y = y + y_change

        if x < 10: ask = True
        elif x > screenwidth-10: ask = True
        if y < 10: ask = True
        elif y > screenHeight-10: ask = True
        
        #food
        # pygame.draw.rect(screen,(10,255,50),(foodx,foody,10,10))
        frogRect = frogImg.get_rect(topleft = (foodx,foody))
        screen.blit(frogImg,frogRect)

        snakePosition = []
        snakePosition.append(x)
        snakePosition.append(y)
        snakeList.append(snakePosition)
        
        if len(snakeList) > snakeLength:
            # print(snakeList,    snakeLength)
            del snakeList[0]
 
        for z in snakeList[:-1]:
            if z == snakePosition:
                ask = True
 
        snake(snakeList)
        score(snakeLength-1)

        if x == foodx and y==foody:
            foodx = (random.randint(10,screenwidth-20)//10)*10
            foody = (random.randint(10,screenHeight-20)//10)*10
            snakeLength += 1

        # border 
        border1 = pygame.draw.rect(screen,(0,255,255),(0,0,10,500))
        border2 = pygame.draw.rect(screen,(0,255,255),(0,0,500,10))
        border3 = pygame.draw.rect(screen,(0,255,255),(490,0,10,500))
        border4 = pygame.draw.rect(screen,(0,255,255),(0,490,500,10))
               
        pygame.display.flip()
        clock.tick(5)
        
gameLoop()
messege('Game Over',brown)
pygame.display.update()
time.sleep(1)
pygame.quit()
quit()


