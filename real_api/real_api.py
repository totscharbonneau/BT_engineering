import time
from real_api.back_wheels import *
from real_api.front_wheels import *
from real_api.Line_Follower import *
from real_api.Ultrasonic_Avoidance import *
from real_api.picar import *

class RealAPI:
    __lastTime = None

    ultrasonicAvoidance = None
    lineFollower = None
    backWheels = None
    frontWheels = None

    def __init__(self):
        self.ultrasonicAvoidance = Ultrasonic_Avoidance(20)
        self.lineFollower = Line_Follower()
        self.backWheels = Back_Wheels(db='helper_files/config')
        self.frontWheels = Front_Wheels(db='helper_files/config')
        picar.setup()
        calibrationReference = [100,100,100,100,90]#[50, 50, 50, 50, 40]
        self.lineFollower.references = calibrationReference
        self.frontWheels.ready()
        self.backWheels.ready()
        self.__lastTime = time.perf_counter_ns()

    def cycleAction(self, cycle):
        currentTime = time.perf_counter_ns()
        cycleTime = currentTime-self.__lastTime
        self.__lastTime = currentTime
        if(cycleTime < 41000000):
            time.sleep((41000000-cycleTime)/1000000000)