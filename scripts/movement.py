import bpy
import mathutils
from math import degrees , radians
import numpy as np

def get_contexteoverwrite():
    for i, area in enumerate(bpy.context.screen.areas):
        if area.type == 'VIEW_3D':
            view3d = bpy.context.screen.areas[i]
            context_override = {'window': bpy.context.window, 
                    'screen': bpy.context.screen, 
                    'area' : view3d}
            return context_override
    return None

class picar:
    def __init__(self):
        self.back_wheels = back_wheels()
        self.front_wheels = front_wheels()
        self.blendercar = bpy.data.objects["back_car"]
        self.wheel_base = np.abs(self.front_wheels.wheel2.location[1] - self.back_wheels.wheel0.location[1])
        self.wheel_depth = self.front_wheels.wheel2.dimensions[2]
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

    
    def test(self):
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

    def turningradius(self):
        return self.wheel_base/np.tan(np.deg2rad(np.abs(self.front_wheels.real_angle)))


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

    def get_realanglefromblender(self):
        self.real_angle = degrees(self.wheel2.rotation_euler[0])
    def update(self):
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
bpy.context.scene.frame_set(0)
# bpy.data.objects["main_body"].select_set(True)
# bpy.data.objects["wheel_2"].select_set(True)
# bpy.data.objects["wheel_3"].select_set(True)
car1.back_wheels.speed(20)
# car1.front_wheels.wanted_angle = -15
# car1.front_wheels.update()
# car1.front_wheels.update()
# car1.test()
# car1.move()


for i in range(0,250):
    if i == 40:
        car1.front_wheels.wanted_angle = -15
    bpy.context.scene.frame_set(i)
    car1.move()