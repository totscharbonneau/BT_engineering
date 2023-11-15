import bpy
import mathutils
from math import degrees , radians
import numpy as np
import bmesh
from mathutils.bvhtree import BVHTree
from enum import Enum

mainState = [
    "FOLLOWLINE"
    "OBSTACLE"
    "INIT"
    "STOP"
]

DistanceAlerte = 30 # Distance a laquelle on commence a arreter
DistanceArret = 10 # Distance ou on arrete
Distance30cm = 30 #Distance avnt de repartir sur la ligne
DeltaSlow = 0.1 # Variation de l'angle lors de la phase de turn slow
DeltaSlow = 0.5 # Variation de l'angle lors de la phase de turn fast
MaxwaitingTimeTurnSlowly = 10 # Temps avant que turn slow devienne turn fast
MaxwaitingTimePause = 3 # temps de repos en ligne droite avant de recommencer a tourner


def get_contexteoverwrite():
    for i, area in enumerate(bpy.context.screen.areas):
        if area.type == 'VIEW_3D':
            view3d = bpy.context.screen.areas[i]
            context_override = {'window': bpy.context.window, 
                    'screen': bpy.context.screen, 
                    'area' : view3d}
            return context_override
    return None


class picar():

    def __init__(self):
        self.back_wheels = back_wheels()
        self.front_wheels = front_wheels()
        self.blendercar = bpy.data.objects["back_car"]
        self.wheel_base = np.abs(self.front_wheels.wheel2.location[1] - self.back_wheels.wheel0.location[1])
        self.wheel_depth = self.front_wheels.wheel2.dimensions[2]
        self.track = bpy.data.objects["plane_obj1"]
        self.currentState = "INIT"
        self.line_sensorData = None

    def control(self):
            for i in range(0,250):
                self.line_sensorData = self.line_sensor()
                capteurSonore = 50
                waitingTime = 50
                self.runState()
                self.currentState = self.switchState()
                bpy.context.scene.frame_set(i)
                car1.move()

    def move(self):
        self.front_wheels.update()
        if self.front_wheels.real_angle == 0:
            direction = self.blendercar.matrix_world.to_quaternion() @ mathutils.Vector((0, 1, 0))
            move_distance = self.back_wheels.direction*self.back_wheels.currentspeed*1/100/24
            translation_vector = move_distance * direction
            self.blendercar.location += translation_vector
        else:
            self.turning()
        bpy.data.objects["back_car"].select_set(True)
        bpy.data.objects["wheel_2"].select_set(True)
        bpy.data.objects["wheel_3"].select_set(True)
        bpy.ops.anim.keyframe_insert(type='LocRotScale')

    def turning(self):
        if self.front_wheels.real_angle == 0:
            print("Abort")
            return None
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects["back_car"].select_set(True)
        radius = self.turningradius()
        bpy.ops.object.empty_add(
        location=(np.sign(self.front_wheels.real_angle)*radius, 0, 0),
        scale=(1,1,1)
        )
        turningpoint = bpy.context.active_object
        turningpoint.name = "turningpoint"
        turningpoint.parent = self.blendercar
        # bpy.context.scene.cursor.location = turningpoint.location
        bpy.ops.view3d.snap_cursor_to_active(get_contexteoverwrite())
        bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
        bpy.data.objects["back_car"].select_set(True)

        rotationrad = -np.sign(self.front_wheels.real_angle)*self.back_wheels.direction*(self.back_wheels.currentspeed*1/100/24)/radius

        bpy.ops.transform.rotate(value=rotationrad, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

        #clean up
        bpy.context.scene.tool_settings.transform_pivot_point = 'BOUNDING_BOX_CENTER'
        bpy.context.scene.cursor.location = [0,0,0]
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['turningpoint'].select_set(True)
        bpy.ops.object.delete()
        # bpy.data.objects["main_body"].select_set(True)
        # bpy.data.objects["wheel_3"].select_set(True)
        # bpy.data.objects["wheel_2"].select_set(True)
    
    def runState(self):
        match self.currentState:
            case "FOLLOWLINE":
                self.back_wheels.speed(10)
                match self.line_sensorData:
                    case [0,0,0,0,0]:
                        None
                    case [1,0,0,0,0]:
                        self.front_wheels.wanted_angle += -5
                    case [1,1,0,0,0]:
                        self.front_wheels.wanted_angle += -3
                    case [0,1,0,0,0]:
                        self.front_wheels.wanted_angle += -2
                    case [0, 1, 1, 0, 0]:
                        self.front_wheels.wanted_angle += -1
                    case [0, 0, 1, 0, 0]:
                        None
                    case [0, 0, 1, 1, 0]:
                        self.front_wheels.wanted_angle += 1
                    case [0, 0, 0, 1, 0]:
                        self.front_wheels.wanted_angle += 2
                    case [0, 0, 0, 1, 1]:
                        self.front_wheels.wanted_angle += 3
                    case [0, 0, 0, 0, 1]:
                        self.front_wheels.wanted_angle += 5
                    case _:
                        print("unexpected line sensor reading")
            case "OBSTACLE":
                print("State = OBSTACLE")
                # Add code for the OBSTACLE state
            case "INIT":
                None
                # Add code for the INIT state
            case "STOP":
                print("State = STOP")
                # Add code for the STOP state
            case _:
                print("Invalid state")

    def switchState(self):
        match self.currentState:
            case "FOLLOWLINE":
                return self.currentState
            case "OBSTACLE":
                print("State = OBSTACLE")
                # Add code for the OBSTACLE state
            case "INIT":
                if bpy.context.scene.frame_current == 10:
                    return "FOLLOWLINE"
                else:
                    return self.currentState
            case "STOP":
                None
                # Add code for the STOP state
            case _:
                print(self.currentState)
                print("Invalid state")

    def test(self):
        print(self.line_sensor())

    def turningradius(self):
        return self.wheel_base/np.tan(np.deg2rad(np.abs(self.front_wheels.real_angle)))

    def line_sensor(self):
        track = self.track
        sensor0 = bpy.data.objects["Sensor_0"]
        sensor1 = bpy.data.objects["Sensor_1"]
        sensor2 = bpy.data.objects["Sensor_2"]
        sensor3 = bpy.data.objects["Sensor_3"]
        sensor4 = bpy.data.objects["Sensor_4"]
        output = []
        sensorlist = [sensor0,sensor1,sensor2,sensor3,sensor4]
        bm_track = bmesh.new()
        bm_track.from_mesh(track.data)
        bm_track.transform(track.matrix_world) 
        obj_track_BVHtree = BVHTree.FromBMesh(bm_track) 

        for sensor in sensorlist:

            bm1 = bmesh.new()
            bm1.from_mesh(sensor.data)
            bm1.transform(sensor.matrix_world)
            obj1_BVHtree = BVHTree.FromBMesh(bm1)
            overlap = obj1_BVHtree.overlap(obj_track_BVHtree)

            output.append(int(bool(overlap)))
        
        return output
    
class back_wheels:
    direction = 1
    currentspeed = 0
    wheel0 = bpy.data.objects["wheel_0"]
    wheel1 = bpy.data.objects["wheel_1"]
    def forward(self):
        self.direction = 1
    def backward(self):
        self.direction = -1
    def print(self):
        print(self.direction)
        print(self.currentspeed)
    def speed(self, speedint):
        self.currentspeed = speedint
    def stop(self):
        self.currentspeed = 0


class front_wheels:
    def __init__(self):
        self.wheel2 = bpy.data.objects["wheel_2"]
        self.wheel3 = bpy.data.objects["wheel_3"]
        self.real_angle = self.wheel2.rotation_euler[0]
        self.wanted_angle = 0
        self.maxangle = 15

    def get_realanglefromblender(self):
        self.real_angle = degrees(self.wheel2.rotation_euler[0])
    def update(self):
        if np.abs(self.wanted_angle) > self.maxangle:
            self.wanted_angle = np.sign(self.wanted_angle)*self.maxangle
        self.get_realanglefromblender()
        # self.wheel2.rotation_euler = [radians(self.wanted_angle), self.wheel2.rotation_euler[1], self.wheel2.rotation_euler[2]] 
        if np.abs(self.wanted_angle - self.real_angle) < 1  and np.abs(self.wanted_angle - self.real_angle) != 0:
                self.wheel2.rotation_euler = [radians(self.wanted_angle), self.wheel2.rotation_euler[1], self.wheel2.rotation_euler[2]] 
        elif self.wanted_angle < self.real_angle:
               self.wheel2.rotation_euler = [self.wheel2.rotation_euler[0] - radians(1), self.wheel2.rotation_euler[1], self.wheel2.rotation_euler[2]] 
        elif self.wanted_angle > self.real_angle:
               self.wheel2.rotation_euler = [self.wheel2.rotation_euler[0] + radians(1), self.wheel2.rotation_euler[1], self.wheel2.rotation_euler[2]] 
        self.wheel3.rotation_euler = self.wheel2.rotation_euler

car1 = picar()

car1.control()

# bpy.context.scene.frame_set(0)
# # bpy.data.objects["main_body"].select_set(True)
# # bpy.data.objects["wheel_2"].select_set(True)
# # bpy.data.objects["wheel_3"].select_set(True)
# car1.back_wheels.speed(20)
# # car1.front_wheels.wanted_angle = -15
# # car1.front_wheels.update()
# # car1.front_wheels.update()
# # car1.test()
# # car1.move()


# for i in range(0,250):
#     if i == 40:
#         car1.front_wheels.wanted_angle = -15
#     bpy.context.scene.frame_set(i)
#     car1.move()