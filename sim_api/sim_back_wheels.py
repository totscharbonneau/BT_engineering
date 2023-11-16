class SimBackWheels:
    __direction = 1
    __currentspeed = 0
    __wheel0 = None
    __wheel1 = None
    __picar = None

    def __init__(self, parent):
        self.__wheel0 = parent._objects["wheel0"]
        self.__wheel1 = parent._objects["wheel1"]
        self.__picar = parent._objects["picar"]

    def forward(self):
        self.__direction = 1

    def backward(self):
        self.__direction = -1

    def speed(self, speedint):
        self.__currentspeed = speedint

    def getCurrentSpeed(self):
        return self.__currentspeed

    def stop(self):
        self.__currentspeed = 0

    def direction(self):
        return self.__picar.matrix_world.to_quaternion() @ mathutils.Vector((0, 1, 0))
    
    def getDirection(self):
        return self.__direction

    def getLocation(self):
        return self.__picar.location
    
    def setLocation(self, location):
        self.__picar.location = location