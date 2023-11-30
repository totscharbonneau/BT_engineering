import real_api.back_wheels
import real_api.front_wheels
import real_api.Line_Follower
import real_api.Ultrasonic_Avoidance
import real_api.picar

class RealAPI:
    ultrasonicAvoidance = None
    lineFollower = None
    backWheels = None
    frontWheels = None

    def __init__(self):
        self.ultrasonicAvoidance = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
        self.lineFollower = Line_Follower.Line_Follower()
        self.backWheels = back_wheels.Back_Wheels(db='helper_files.config')
        self.frontWheels = front_wheels.Front_Wheels(db='helper_files.config')
        picar.setup()
        calibrationReference = [200, 200, 200, 200, 200]
        self.lineFollower.references = calibrationReference
        self.frontWheels.ready()
        self.backWheels.ready()  