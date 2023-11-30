import bpy

class SimUltrasonicAvoidance:
    def __init__(self, parent):
        self._parent = parent

    def distance(self):
        scene = bpy.context.scene
        deps = bpy.context.view_layer.depsgraph
        sensorLocation = self._parent._objects["distanceSensor"].matrix_world.translation
        sensorRotation = self._parent._objects["picar"].rotation_euler
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