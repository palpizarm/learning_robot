# Grid class
from Square import *
from Util import *

class Grid:

    def __init__(self):
        grid = []

    def createGrid(self, file_name):
        types = [0,NORMAL_GRD_COST,MODERATE_GRD_COST,HARD_GRD_COST,LOCKED_GRD_COST]
        data = open(r'data/' + file_name +  '.txt')
        data = [line.split(',') for line in data.readlines()]
        for row in range(GRD_LENGTH):
            elements = []
            for column in range(GRD_LENGTH):
                value = int(data[row][column])
                elements.append(Square(value,types[value]))
            grid.append(elements)
        