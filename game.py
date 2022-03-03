import math
import random
import pygame

# Initialize pygame
pygame.init()

# screen/window size
screen = pygame.display.set_mode((800,600))

# game name
pygame.display.set_caption('Save the Plane')

planeImg = pygame.image.load('plane.png')
planeX = 100
planeY = 300-32
planeY_change = 0
plane_speed = 0.2
def plane(x,y):
    screen.blit(planeImg,(x,y))

coinImg_1 = pygame.image.load('dollar.png')
coinImg_2,coinImg_3,coinImg_4,coinImg_5,coinImg_6,coinImg_7 = coinImg_1.copy(),coinImg_1.copy(),coinImg_1.copy(),coinImg_1.copy(),coinImg_1.copy(),coinImg_1.copy()
#print(id(coinImg_1),id(coinImg_2),id(coinImg_3))
coinX_change = -0.05
cycle_count = 0
coinX_1 = random.randint(200+cycle_count,400+cycle_count)
coinY_1 = random.randint(64,600-64)
coinX_2 = random.randint(400+cycle_count,600+cycle_count)
coinY_2 = random.randint(64,600-64)
coinX_3 = random.randint(600+cycle_count,800+cycle_count)
coinY_3 = random.randint(64,600-64)
coinX_4 = random.randint(800+cycle_count,1000+cycle_count)
coinY_4 = random.randint(64,600-64)
coinX_5 = random.randint(1000+cycle_count,1200+cycle_count)
coinY_5 = random.randint(64,600-64)
coinX_6 = random.randint(1200+cycle_count,1400+cycle_count)
coinY_6 = random.randint(64,600-64)
coinX_7 = random.randint(1400+cycle_count,1600+cycle_count)
coinY_7 = random.randint(64,600-64)

visible_1,visible_2,visible_3,visible_4,visible_5,visible_6 = True,True,True,True,True,True
def coin(img,x,y):
    screen.blit(img,(x,y))

def collision(coinx,coiny,planex,planey):
    return True if math.dist([coinx,coiny],[planex,planey])<60 else False

score_value = 0
score_speed = 10**4
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render('Coins: '+str(score_value),True,(0,0,0))
    screen.blit(score, (x,y))
running = True
while running:
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                planeY_change = plane_speed
            elif event.key==pygame.K_UP:
                planeY_change = -plane_speed
        else:
            planeY_change = 0
    
    if coinX_change<-0.85:
        coinX_change = -0.05

    coinX_1 += coinX_change
    if collision(coinX_1,coinY_1,planeX,planeY) and visible_1:
        visible_1 = False
        score_value += 1
        coinX_change -= score_value/score_speed
        coinImg_1.set_alpha(0)
    if coinX_1<-64:
        #print('came 1')
        visible_1 = True
        coinImg_1.set_alpha(255)
        cycle_count = 600
        coinX_1 = random.randint(200+cycle_count,400+cycle_count)
        coinY_1 = random.randint(64,600-64)
        #print(coinX_1)
    coin(coinImg_1,coinX_1,coinY_1)

    coinX_2 += coinX_change
    if collision(coinX_2,coinY_2,planeX,planeY) and visible_2:
        visible_2 = False
        score_value += 1
        coinX_change -= score_value/score_speed
        coinImg_2.set_alpha(0)
    if coinX_2<-64:
        #print('came 2')
        visible_2 = True
        coinImg_2.set_alpha(255)
        coinX_2 = random.randint(400+cycle_count,600+cycle_count)
        coinY_2 = random.randint(64,600-64)
        #print(coinX_2)
    coin(coinImg_2,coinX_2,coinY_2)

    coinX_3 += coinX_change
    if collision(coinX_3,coinY_3,planeX,planeY) and visible_3:
        visible_3 = False
        score_value += 1
        coinX_change -= score_value/score_speed
        coinImg_3.set_alpha(0)
    if coinX_3<-64:
        #print('came 3')
        visible_3 = True
        coinImg_3.set_alpha(255)
        coinX_3 = random.randint(600+cycle_count,800+cycle_count)
        coinY_3 = random.randint(64,600-64)
        #print(coinX_3)
    coin(coinImg_3,coinX_3,coinY_3)

    coinX_4 += coinX_change
    if collision(coinX_4,coinY_4,planeX,planeY) and visible_4:
        visible_4 = False
        score_value += 1
        coinX_change -= score_value/score_speed
        coinImg_4.set_alpha(0)
    if coinX_4<-64:
        #print('came 4')
        visible_4 = True
        coinImg_4.set_alpha(255)
        coinX_4 = random.randint(800+cycle_count,1000+cycle_count)
        coinY_4 = random.randint(64,600-64)
        #print(coinX_4)
    coin(coinImg_4,coinX_4,coinY_4)

    coinX_5 += coinX_change
    if collision(coinX_5,coinY_5,planeX,planeY) and visible_5:
        visible_5 = False
        score_value += 1
        coinX_change -= score_value/score_speed
        coinImg_5.set_alpha(0)
    if coinX_5<-64:
        #print('came 5')
        visible_5 = True
        coinImg_5.set_alpha(255)
        coinX_5 = random.randint(1000+cycle_count,1200+cycle_count)
        coinY_5 = random.randint(64,600-64)
        #print(coinX_5)
    coin(coinImg_5,coinX_5,coinY_5)

    coinX_6 += coinX_change
    if collision(coinX_6,coinY_6,planeX,planeY) and visible_6:
        visible_6 = False
        score_value += 1
        coinX_change -= score_value/score_speed
        coinImg_6.set_alpha(0)
    if coinX_6<-64:
        #print('came 6')
        visible_6 = True
        coinImg_6.set_alpha(255)
        coinX_6 =  random.randint(1200+cycle_count,1400+cycle_count)
        coinY_6 = random.randint(64,600-64)
        #print(coinX_6)
    coin(coinImg_6,coinX_6,coinY_6)

    planeY += planeY_change
    planeY = 0 if planeY<0 else planeY
    planeY = 600-64 if planeY>600-64 else planeY
    plane(planeX,planeY)
    
    show_score(textX,textY)
    pygame.display.update()
