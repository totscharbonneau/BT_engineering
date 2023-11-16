with open("sim_api/shape_factory.py") as f:
    code = f.read()
    exec(code)

with open("sim_api/track_factory.py") as f:
    code = f.read()
    exec(code)

with open("sim_api/sim_context.py") as f:
    code = f.read()
    exec(code)

with open("sim_api/sim_ultrasonic_avoidance.py") as f:
    code = f.read()
    exec(code)

with open("sim_api/sim_line_follower.py") as f:
    code = f.read()
    exec(code)

objNames = {
  "marble": "Marble",
  "picar": "back_car",
  "distanceSensor": "distance_sensor",
  "lineSensor0": "Sensor_0",
  "lineSensor1": "Sensor_1",
  "lineSensor2": "Sensor_2",
  "lineSensor3": "Sensor_3",
  "lineSensor4": "Sensor_4",
  "line": "plane_obj1",
  "obstacle": "obstacle_obj1"
}

class SimAPI:
    __objects = dict()

    simUltrasonicAvoidance = SimUltrasonicAvoidance()
    simLineFollower = None

    def __init__(self, isResetNeeded):
        if(isResetNeeded):
            SimContext.setBlenderEnv()
            ShapeFactory.picarGen(objNames["picar"], [0, -picar_length/2 + 4.12/100, 0])
            ShapeFactory.marbleGen(objNames["marble"], [0, picar_length/2 - 4.7625/100, picar_height+0.015])
            TrackFactory.track1(objNames["line"], objNames["obstacle"], (0,0.575,0), (0,0.625,0))
        for key, value in objNames.items():
            self.__objects[key] = bpy.data.objects[value]
        self.simLineFollower = SimLineFollower(parent=self)

