#!/usr/bin/python3
""" This is the memory test module """

import pygame
import time
import random
 
pygame.init()

display_width = 800
display_height = 600

# colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)

#music
# pygame.mixer.music.load('Bionic Commando (2009) - 18 - Piano Theme.mp3')
# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play(-1)
######
 
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Holbie Memory Test")
clock = pygame.time.Clock()
# background pics
background = pygame.image.load("prism.jpg")
backgroundGameLoop = pygame.image.load('holbie_background.jpg')
# base pics
holbieBlue = pygame.image.load('holbie_logo_blue.png')
holbieYellow = pygame.image.load('holbie_logo_yellow.png')
holbieGreen = pygame.image.load('holbie_logo_green.png')
holbieOrange = pygame.image.load('holbie_logo_orange.png')

gameIcon = pygame.image.load('holbie_logo.png')
pygame.display.set_icon(gameIcon)

def quitgame():
    pygame.quit()
    quit()

def button(msg,x,y,w,h,ib_c,ab_c,it_c,at_c,action=None):
    pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > pos[0] > x and y+h > pos[1] > y:
        pygame.draw.rect(gameDisplay, ab_c,(x,y,w,h))
        text(msg,x+(w/2),y+(h/2),50,at_c,'coolvetica rg.ttf')
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ib_c,(x,y,w,h))
        text(msg,x+(w/2),y+(h/2),50,it_c,'coolvetica rg.ttf')
  


def text(msg, x, y, size, color, font, sysfont = False):
    if sysfont:
        font = pygame.font.SysFont(font,size)
    else: font = pygame.font.Font(font,size) 
    TextSurf = font.render(msg, True, color)
    TextRect = TextSurf.get_rect()
    TextRect.center = ((x),(y))
    gameDisplay.blit(TextSurf, TextRect)


def about():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(background, (00,00))
        # References to authors
        text('References:',display_width/2,display_height/1.25,15,white,'coolvetica rg.ttf')
        text(' - Authored by Marwan Mohamed - ',display_width/2,display_height/1.2,15,white,'coolvetica rg.ttf')
        text(' - Adapted by Nikki E - Hector L - Jay C - ',display_width/2,display_height/1.15,15,white,'coolvetica rg.ttf')

        button("Back",(display_width/2)-100,(display_height/2)-50,200,100,white,red,red,white,game_intro)

        pygame.display.update()
        clock.tick(15)
        
def game_intro():
    # pygame.mixer.music.pause()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(background, (00,00))
        text('Holbie Memory Test',display_width/2,display_height/7,50,red,'crackman.ttf')

        button("Start",(display_width/2)-100,200,200,100,white,red,red,white,game_loop)
        button("About",(display_width/2)-100,325,200,100,white,red,red,white,about)
        button("Quit",(display_width/2)-100,450,200,100,white,red,red,white,quitgame)

        pygame.display.update()
        clock.tick(15)

def check_same(tile, choosen):
    l = []
    for i in range(len(tile)):
            if tile[i] == True:
                l.append(choosen[i])
    if len(l) == 2:
        return len(list(set(l))) != len(l)
    if len(l) == 4:
        return len(list(set(l))) != len(l) - 1
    elif len(l) == 6:
        return len(list(set(l))) != len(l) - 2
    else:
        return len(list(set(l))) != len(l) - 3
            
def l_random():
    # 3 x 2
    # 4 x 2
    l=[[holbieBlue,holbieYellow,holbieGreen],[holbieBlue,holbieYellow,holbieGreen,holbieOrange]]
    l_final =[]
    while len(l_final) != len(l[1])*2:
        choice = l[1][random.randint(0,len(l[1])-1)]
        if l_final.count(choice) <= 1 : l_final.append(choice)
    return l_final

def game_loop(oldchoosen = None, oldtile = None, old_x = None):
    # pygame.mixer.music.unpause()
    choosen = None
    time.sleep(0.1)
    if old_x != None:
        x = old_x
    else:
        x = 1
    Won = None
    gameExit = False
    if oldtile != None:
        tile = oldtile[:]
    else:
        tile = [False, False, False, False, False, False, False, False]
    tile1 = tile[0]
    tile2 = tile[1]
    tile3 = tile[2]
    tile4 = tile[3]
    tile5 = tile[4]
    tile6 = tile[5]
    tile7 = tile[6]
    tile8 = tile[7]
    if oldchoosen != None:
        choosen = oldchoosen[:]
    else:
        choosen = l_random()
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(backgroundGameLoop,(0,0))
        gameDisplay.blit(pygame.transform.scale(choosen[0], (150, 150)),(175,100))
        gameDisplay.blit(pygame.transform.scale(choosen[1], (150, 150)),(325,100))
        gameDisplay.blit(pygame.transform.scale(choosen[2], (150, 150)),(475,100))
        gameDisplay.blit(pygame.transform.scale(choosen[3], (150, 150)),(175,250))
        gameDisplay.blit(pygame.transform.scale(choosen[4], (150, 150)),(325,250))
        gameDisplay.blit(pygame.transform.scale(choosen[5], (150, 150)),(475,250))
        gameDisplay.blit(pygame.transform.scale(choosen[6], (150, 150)),(250,400))
        gameDisplay.blit(pygame.transform.scale(choosen[7], (150, 150)),(400,400))

        if (Won == True):
            time.sleep(0.3)
            if tile.count(True) == 8:
                time.sleep(5)
                game_intro()
            
            game_loop(choosen, tile, x)
            Won = None
        if (Won == False):
            time.sleep(0.3)
            game_loop(choosen)

        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 325 > pos[0] > 175 and 250 > pos[1] > 100 and click[0] == 1:
            tile1 = True
        if 475 > pos[0] > 325 and 250 > pos[1] > 100 and click[0] == 1:
            tile2 = True
        if 625 > pos[0] > 475 and 250 > pos[1] > 100 and click[0] == 1:
            tile3 = True
        #row 2
        if 325 > pos[0] > 175 and 400 > pos[1] > 250 and click[0] == 1:
            tile4 = True
        if 475 > pos[0] > 325 and 400 > pos[1] > 250 and click[0] == 1:
            tile5 = True
        if 625 > pos[0] > 475 and 400 > pos[1] > 250 and click[0] == 1:
            tile6 = True
        #row3
        if 400 > pos[0] > 250 and 550 > pos[1] > 400 and click[0] == 1:
            tile7 = True
        if 550 > pos[0] > 400 and 550 > pos[1] > 400 and click[0] == 1:
            tile8 = True

        tile = [tile1, tile2, tile3, tile4, tile5, tile6, tile7, tile8]
        #print tile
        if tile.count(True) > x:
            if check_same(tile, choosen) == True:        
                text('Nice !!!',display_width/2,display_height/1.05,30,green,'coolvetica rg.ttf')
                Won = True
                x += 2         
            else:
                text('Nope !!!',display_width/2,display_height/1.05,30,red,'coolvetica rg.ttf')
                Won = False

        if not tile1: pygame.draw.rect(gameDisplay, white, (175,100,150,150))
        if not tile2: pygame.draw.rect(gameDisplay, white, (325,100,150,150))
        if not tile3: pygame.draw.rect(gameDisplay, white, (475,100,150,150))
        if not tile4: pygame.draw.rect(gameDisplay, white, (175,250,150,150))
        if not tile5: pygame.draw.rect(gameDisplay, white, (325,250,150,150))
        if not tile6: pygame.draw.rect(gameDisplay, white, (475,250,150,150))
        if not tile7: pygame.draw.rect(gameDisplay, white, (250,400,150,150))
        if not tile8: pygame.draw.rect(gameDisplay, white, (400,400,150,150))

        # horizontal
        pygame.draw.line(gameDisplay, black, (175,100),(625,100),5)
        pygame.draw.line(gameDisplay, black, (175,250),(625,250),5)
        pygame.draw.line(gameDisplay, black, (175,400),(625,400),5)
        pygame.draw.line(gameDisplay, black, (250,550),(550,550),5)
        # vertical
        pygame.draw.line(gameDisplay, black, (175,100),(175,400),5)
        pygame.draw.line(gameDisplay, black, (325,100),(325,400),5)
        pygame.draw.line(gameDisplay, black, (475,100),(475,400),5)
        pygame.draw.line(gameDisplay, black, (625,100),(625,400),5)
        pygame.draw.line(gameDisplay, black, (250,400),(250,550),5)
        pygame.draw.line(gameDisplay, black, (400,400),(400,550),5)
        pygame.draw.line(gameDisplay, black, (550,400),(550,550),5)
        
        pygame.display.update()
        clock.tick(60)

game_intro()
pygame.quit()
quit()
