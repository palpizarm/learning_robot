import random


# app layout
width, height =  1000,700
# ground size
grd_w = 650
grd_h = 650
# sprite size
sprite_size = 32
# information layout
VIEW_W = 300
VIEW_H = 325



# length of the grid
GRD_LENGTH = 20;
#Ground cost type
NORMAL_GRD_COST = 1;
MODERATE_GRD_COST = 2;
HARD_GRD_COST = 3;
LOCKED_GRD_COST = 1000;
COST = [NORMAL_GRD_COST,MODERATE_GRD_COST,HARD_GRD_COST,LOCKED_GRD_COST]
# Ground type
NORMAL_GROUND = 1;
MODERATE_GROUND = 2;
HARD_GROUND = 3;
LOCKED_GROUND = 4;
GRD_TYPES = [NORMAL_GROUND,MODERATE_GROUND,HARD_GROUND,LOCKED_GROUND]
# Battery sizes
BATTERY_T1 = 80
BATTERY_T2 = 95
BATTERY_T3 = 107
BATTERIES = [0,BATTERY_T1,BATTERY_T2,BATTERY_T3]

# cameras = (square view count, cost)
CAMERAS = [(),(1,2),(2,3),(3,4)]
# motors = (,)
MOTORS = [(),(NORMAL_GROUND,), (NORMAL_GROUND,MODERATE_GROUND),(NORMAL_GROUND,MODERATE_GROUND,HARD_GROUND)]

# objetive position
OBJ_X = 20 
OBJ_Y = 1

# Adaptability values
MAX_DIST = 19


# COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,128)


# calculate the distance of the robot and objetive point
# use the chebyshov distance method
def distance(x1,y1,x2,y2):
    return max(abs(x2-x1),abs(y2-y1))

# create a grid
# grid generate = 2
def generateGrid():
    file = open('data/grid.txt', 'w+')
    for row in range(GRD_LENGTH):
        elements = []
        for column in range(GRD_LENGTH):
            file.write(str(random.randint(NORMAL_GROUND, LOCKED_GROUND)))
            if column != 19:
                file.write(',')
        if row != 19:
            file.write('\n')