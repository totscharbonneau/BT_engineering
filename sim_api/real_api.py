from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from SunFounder_Line_Follower import Line_Follower
from picar import front_wheels
from picar import back_wheels
import picar


class RealAPI:

    ultrasonicAvoidance = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
    lineFollower = Line_Follower.Line_Follower()
    backWheels = back_wheels.Back_Wheels(db='config')
    frontWheels = front_wheels.Front_Wheels(db='config')
    REFERENCES = [200, 200, 200, 200, 200]
    def __init__(self):
        picar.setup()
        self.lineFollower.references = self.REFERENCES
        self.frontWheels.ready()
        self.backWheels.ready()  