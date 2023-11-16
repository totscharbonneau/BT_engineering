import bpy, time

with open("sim_api/shape_factory.py") as f:
    code = f.read()
    exec(code)

with open("sim_api/sim_context.py") as f:
    code = f.read()
    exec(code)

objNames = {
  "marble": "Marble",
  "picar": "back_car",
  "distanceSensor": "distance_sensor"
}

class SimAPI:
    __objects = dict()

    def __init__(self, isResetNeeded):
        if(isResetNeeded):
            SimContext.setBlenderEnv()
            ShapeFactory.picarGen(objNames["picar"], [0, -picar_length/2 + 4.12/100, 0])
            ShapeFactory.marbleGen(objNames["marble"], [0, picar_length/2 - 4.7625/100, picar_height+0.015])
        for key, value in objNames.items():
            self.__objects[key] = bpy.data.objects[value]

    def distance(self):
        timeout = 0.05
        time.sleep(timeout)
        scene = bpy.context.scene
        deps = bpy.context.view_layer.depsgraph
        sensorLocation = self.__objects["distanceSensor"].matrix_world.translation
        sensorRotation = self.__objects["picar"].rotation_euler
        rayResult = scene.ray_cast(deps, sensorLocation, mathutils.Euler([sensorRotation[0], sensorRotation[1]+90, sensorRotation[2]]))
        if rayResult[0] == False:
            return -1
        return int(100*((rayResult[1][0]-sensorLocation[0])**(2)+(rayResult[1][1]-sensorLocation[1])**(2)+(rayResult[1][2]-sensorLocation[2])**(2))**(1/2))

    def get_distance(self, mount = 5):
        sum = 0
        for i in range(mount):
            distanceAttempt = self.distance()
            sum += distanceAttempt
        return int(sum/mount)

    def less_than(self, alarmGate):
        distance = self.get_distance()
        status = 0
        if distance >=0 and distance <= alarmGate:
            status = 1
        elif distance > alarmGate:
            status = 0
        else:
            status = -1
        return status
