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

with open("sim_api/sim_back_wheels.py") as f:
    code = f.read()
    exec(code)

with open("sim_api/sim_front_wheels.py") as f:
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
    "wheel0": "wheel_0",
    "wheel1": "wheel_1",
    "wheel2": "wheel_2",
    "wheel3": "wheel_3"
}


class SimAPI:
    _objects = None

    ultrasonicAvoidance = None
    lineFollower = None
    backWheels = None
    frontWheels = None

    def __init__(self, isResetNeeded, numberOfCycles):
        if(isResetNeeded):
            SimContext.setBlenderEnv(numberOfCycles)
            ShapeFactory.picarGen(objNames["picar"], (0, -picar_length/2 + 4.12/100, 0))
            ShapeFactory.marbleGen(objNames["marble"], (0, picar_length/2 - 4.7625/100, picar_height+0.015))
            #TrackFactory.track1(objNames["line"], "obstacle", (0,0.575,0), (0,0.625,0))
            TrackFactory.track2(objNames["line"], (0,0.575,0))
            #TrackFactory.track3(objNames["line"], (0,0.575,0))
            self._objects = dict()
            for key, value in objNames.items():
                self._objects[key] = bpy.data.objects[value]
            self.backWheels = SimBackWheels(parent=self)
            self.frontWheels = SimFrontWheels(parent=self, simBackWheels=self.backWheels)
        else:
            self._objects = dict()
            for key, value in objNames.items():
                self._objects[key] = bpy.data.objects[value]
            self._objects["picar"].location = (0, -picar_length/2 + 4.12/100, 0)
            self._objects["marble"].location = (0, picar_length/2 - 4.7625/100, picar_height+0.015)
            self.backWheels = SimBackWheels(parent=self)
            self.frontWheels = SimFrontWheels(parent=self, simBackWheels=self.backWheels)
            self.frontWheels.__real_angle = 0
            self.frontWheels.update()
        self.ultrasonicAvoidance = SimUltrasonicAvoidance(parent=self)
        self.lineFollower = SimLineFollower(parent=self)


    def move(self):
        self.frontWheels.update()
        if self.frontWheels.getRealAngle() == 0:
            direction = self.backWheels.direction()
            move_distance = self.backWheels.getDirection()*self.backWheels.getCurrentSpeed()*1/100/24
            translation_vector = move_distance * direction
            self.backWheels.setLocation(self.backWheels.getLocation() + translation_vector)
        else:
            self.frontWheels.turning()
        self._objects["picar"].select_set(True)
        self._objects["wheel2"].select_set(True)
        self._objects["wheel3"].select_set(True)
        bpy.ops.anim.keyframe_insert(type='LocRotScale')
        for obj in bpy.data.objects:
            obj.select_set(False)

    def cycleAction(self, cycle):
        bpy.context.scene.frame_set(cycle)