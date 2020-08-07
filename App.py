# main windows
import pygame
from Util import *





# pygame setting
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Robot learning')
screen.fill([255,255,255])
run = True

# load components

ground_image = pygame.image.load(r'data/ground.png')
ground_image = pygame.transform.scale(ground_image, (grd_w, grd_h))
robot_image =  pygame.image.load(r'data/robot.png')
robot_image = pygame.transform.scale(robot_image,(rbt_size,rbt_size))
ground_image.blit(robot_image, (0,0))
screen.blit(ground_image,(width-grd_w,25))

# main window
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()