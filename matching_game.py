# #!/usr/bin/python3
""" This is the matching game module """


import pygame


if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1280, 1024))

    framerate = 60

    done = False

    while not done:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        pygame.display.set_caption('Matching Game')
        icon=pygame.image.load(r‘images/holbie_logo.png’)
        pygame.display.set_icon(icon)
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(x, y, 90, 90))
        pygame.display.flip()
