# main windows
import pygame
import random
from Util import *
from Robot import *
from Grid import *


# start algorithm
def init():
    pass

# select the best robots, probabilitic way
def selection(robots):
    grades = testing(robots)
    best_robots = []
    for count in range(len(robots)):
        # generate random number
        r = random.uniform(0,1)
        robot = 0
        # pick the robot  
        for index in range(len(grades)):
            if robot < r < robot + grades[index]:
                best_robots.append(robots[index])    
                break
            robot += grades[index]
    return best_robots

# takes the selection robots and do the crossing
def crossing(robots):
    new_robots = []
    for count in range(0,len(robots),2):
        # take two robot
        r1 = robots[count]
        r2 = robots[count + 1]
        # bits of each robot
        bits_r1 = get_binary_setting(r1)
        bits_r2 = get_binary_setting(r2)
        # pick the point of the crossing
        index = random.randint(2,12)
        # doing crossing
        aux = bits_r1[0:index]
        bits_r1[0:index] = bits_r2[0:index]
        bits_r2[0:index] = aux
        r1 = build_robot(bits_r1)
        r2 = build_robot(bits_r2)
        new_robots.append([r1,r2])
    return new_robots


def get_binary_setting(robot):
    setting = []
    # get camera type
    value = '{0:02b}'.format(robot.camera.type)
    setting.append([int(n) for n in value])
    # get motor type
    value = '{0:02b}'.format(robot.motor.type)
    setting.append([int(n) for n in value])
    # get battery type
    value = '{0:02b}'.format(robot.battery.type)
    setting.append([int(n) for n in value])
    # get behavior

def build_robot(binary_setting):
    setting_type = []
    # set camera type
    value = [str(x) for x in binary_setting[0:4]]
    value = ''.join(value)
    setting_type.append(int(value))
    # set motor type
    value = [str(x) for x in binary_setting[4:8]]
    value = ''.join(value)
    setting_type.append(int(value))
    # set battery type
    value = [str(x) for x in binary_setting[8:12]]
    value = ''.join(value)
    setting_type.append(int(value))
    # set behavior

    # select motor, battery and camera and set behavior

    # build robot
    robot = Robot(1,1,1)
    return robot

# calculate grade for each robot
def testing(robots):
    grades = []
    normalize_grade = []
    # evalute each robot 
    for robot in robots:
    # distance of the objetive, cost and time
        x1, y1 = robot.get_position()
        dist = distance(x1, y1, OBJ_X, OBJ_Y)
        # hacer un forma para calcular en costo con la configuracion del robot
        cost = 0
        grades.append(adaptability(dist,cost,robot.time))
    average = sum(grades)
    for grade in grades:
        normalize_grade.append(grade/average)
    return normalize_grade

# adaptability function
def adaptability(distance, cost, time):
    return distance + cost + time



# General setting
robots = []

grid = Grid()
grid.createGrid('grid_1')



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
robot_image = pygame.transform.scale(robot_image,(sprite_size,sprite_size))
rock_image = pygame.image.load(r'data/rock.png')
rock_image = pygame.transform.scale(rock_image,(sprite_size,sprite_size))
# load rock in map
for r_count in range(GRD_LENGTH):
    for c_count in range(GRD_LENGTH):
        if grid.grid[r_count][c_count].type == LOCKED_GROUND:
            ground_image.blit(rock_image, (r_count*sprite_size,c_count*sprite_size))
screen.blit(ground_image,(width-grd_w,25))

# main window
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()