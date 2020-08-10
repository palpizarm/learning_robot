# Robot class

class Robot:
    
    def __init__(self, p_motor, p_camera, p_battery, parents):
        self.motor = p_motor
        self.camera = p_camera
        self.battery = p_battery
        self.x = 1
        self.y = 20
        self.time = 0
        self.parents = parents
        self.travel = []

    def get_posoition(self):
        return (self.x,self.y)