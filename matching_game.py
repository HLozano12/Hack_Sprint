#!/usr/bin/python3
""" This is the matching game module """

import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.set_caption('Matching Game')

    pygame.display.flip()
