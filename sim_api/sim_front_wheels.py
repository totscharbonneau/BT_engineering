import numpy, math

def get_contexteoverwrite():
    for i, area in enumerate(bpy.context.screen.areas):
        if area.type == 'VIEW_3D':
            view3d = bpy.context.screen.areas[i]
            context_override = {'window': bpy.context.window, 
                    'screen': bpy.context.screen, 
                    'area' : view3d}
            return context_override
    return None


class SimFrontWheels:
    __real_angle = 0
    wanted_angle = 0
    __maxangle = 45
    __wheel0 = None
    __wheel2 = None
    __wheel3 = None
    __picar = None
    __simBackWheels = None
    # __wheel_base = None


    def __init__(self, parent, simBackWheels):
        self.__wheel0 = parent._objects["wheel0"]
        self.__wheel2 = parent._objects["wheel2"]
        self.__wheel3 = parent._objects["wheel3"]
        self.__picar = parent._objects["picar"]
        # self.__wheel_base = numpy.abs(self.__wheel2.location[1] - self.__wheel0.location[1])
        self.__simBackWheels = simBackWheels
        self.__real_angle = self.__wheel2.rotation_euler[0]

    def getRealAngle(self):
        return self.__real_angle

    def getRealAngleFromBlender(self):
        self.__real_angle = math.degrees(self.__wheel2.rotation_euler[0])
        return self.__real_angle
    
    def update(self):
        if numpy.abs(self.wanted_angle) > self.__maxangle:
            self.wanted_angle = numpy.sign(self.wanted_angle)*self.__maxangle
        self.getRealAngleFromBlender()
        self.__wheel2.rotation_euler = [math.radians(self.wanted_angle), self.__wheel2.rotation_euler[1], self.__wheel2.rotation_euler[2]] 
        self.__wheel3.rotation_euler = self.__wheel2.rotation_euler

    def turningradius(self):
        wheel_base = numpy.abs(self.__wheel2.location[1] - self.__wheel0.location[1])
        return wheel_base/numpy.tan(numpy.deg2rad(numpy.abs(self.__real_angle)))

    def turning(self):
        if self.__real_angle == 0:
            return None
        bpy.ops.object.select_all(action='DESELECT')
        self.__picar.select_set(True)
        radius = self.turningradius()
        bpy.ops.object.empty_add(
        location=(numpy.sign(self.__real_angle)*radius, 0, 0),
        scale=(1,1,1)
        )
        turningpoint = bpy.context.active_object
        turningpoint.name = "turningpoint"
        turningpoint.parent = self.__picar
        bpy.context.scene.tool_settings.transform_pivot_point = 'ACTIVE_ELEMENT'
        self.__picar.select_set(True)

        rotationrad = -numpy.sign(self.__real_angle)*self.__simBackWheels.getDirection()*(self.__simBackWheels.getCurrentSpeed()*1/100/24)/radius

        bpy.ops.transform.rotate(value=rotationrad, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)

        #clean up
        bpy.context.scene.tool_settings.transform_pivot_point = 'BOUNDING_BOX_CENTER'
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['turningpoint'].select_set(True)
        bpy.ops.object.delete()

    def get_contexteoverwrite(self):
        for i, area in enumerate(bpy.context.screen.areas):
            if area.type == 'VIEW_3D':
                view3d = bpy.context.screen.areas[i]
                context_override = {'window': bpy.context.window, 
                        'screen': bpy.context.screen, 
                        'area' : view3d}
                return context_override
        return None