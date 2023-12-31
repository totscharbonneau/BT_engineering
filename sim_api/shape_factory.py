import bpy
from numpy import pi

wheel_radius = 0.0635/2
wheel_width = 0.028
picar_length = 0.235
picar_height = 0.0475  
picar_width = 0.08
line_sensor_height = 0.003
line_sensor_length = 0.03
line_sensor_width = 0.123825
line_sensor_elevation = 0.019
sensors_distances = 0.019
sensor_height = 0.023

class ShapeFactory:
    def receptacleGen(name, location=[0, 0, 0], parent=None):
        bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(0.025, 0.025, 0.0015))
        for obj in bpy.context.selected_objects:
            obj.name = "CubeReceptacleGen"
            cubeReceptacleGen = obj
        bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0.14), scale=(0.14, 0.14, 0.14))
        for obj in bpy.context.selected_objects:
            obj.name = "SphereReceptacleGen"
            sphereReceptacleGen = obj
        bpy.ops.sculpt.sculptmode_toggle()
        bpy.ops.sculpt.dynamic_topology_toggle()
        bpy.context.scene.tool_settings.sculpt.detail_type_method = 'MANUAL'
        bpy.context.scene.tool_settings.sculpt.constant_detail_resolution = 700
        bpy.ops.sculpt.detail_flood_fill()
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.transform.tosphere(value=1, mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False)
        bpy.ops.object.editmode_toggle()
        bpy.context.object.scale[0] = 1.00352
        bpy.context.object.scale[1] = 1.00352
        bpy.context.object.scale[2] = 1.00352
        for obj in bpy.data.objects:
            obj.select_set(False)
        cubeReceptacleGen.select_set(True)
        bpy.context.view_layer.objects.active = cubeReceptacleGen
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = sphereReceptacleGen
        bpy.context.object.modifiers["Boolean"].solver = 'EXACT'
        bpy.ops.object.modifier_set_active(modifier="Boolean")
        bpy.ops.object.convert(target='MESH')
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        for obj in bpy.context.selected_objects:
            obj.name = name
            obj.location = location
            if(parent != None):
                obj.parent = parent
        bpy.ops.rigidbody.object_add()  
        bpy.context.object.rigid_body.type = 'PASSIVE'
        bpy.context.object.rigid_body.collision_shape = 'MESH'
        bpy.context.object.rigid_body.mesh_source = 'BASE'
        bpy.context.object.rigid_body.friction = 1
        bpy.context.object.rigid_body.restitution = 0
        bpy.context.object.rigid_body.kinematic = True
        for obj in bpy.data.objects:
            obj.select_set(False)
        cubeReceptacleGen.select_set(True)
        bpy.context.view_layer.objects.active = cubeReceptacleGen
        bpy.ops.object.delete()
        sphereReceptacleGen.select_set(True)
        bpy.context.view_layer.objects.active = sphereReceptacleGen
        bpy.ops.object.delete()

    def marbleGen(name, location=[0, 0, 0], parent=None):
        bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=location, scale=(0.003995, 0.003995, 0.003995))
        for obj in bpy.context.selected_objects:
            obj.name = name
            if(parent != None):
                obj.parent = parent
        bpy.ops.rigidbody.object_add()
        bpy.context.object.rigid_body.mass = 0.00517
        bpy.context.object.rigid_body.collision_shape = 'SPHERE'
        bpy.context.object.rigid_body.friction = 1
        bpy.context.object.rigid_body.restitution = 0
        bpy.context.object.rigid_body.linear_damping = 0.7


    def picarGen(name, location=[0, 0, 0], parent=None):
        bpy.ops.object.empty_add(
            location=(0, -picar_length/2 + 4.12/100, 0),
            radius=0.01,
            scale=(1,1,1)
            )
        back_car = bpy.context.active_object
        back_car.name = name
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(0, 0, picar_height),
            scale=(picar_width, picar_length, 0.3/100)
        )
        main_body = bpy.context.active_object
        main_body.name = "main_body"
        child_matrix_world = main_body.matrix_world.copy()
        # Set the parent while keeping the transformation
        main_body.parent = back_car
        # Restore the child's world matrix
        main_body.matrix_world = child_matrix_world
        for i in range(0, 4):
            if (i < 2): back_wheel_distance = -picar_length/2 + 4.12/100
            else: back_wheel_distance = picar_length/2 - 4.7625/100
            bpy.ops.mesh.primitive_cylinder_add(
                radius=wheel_radius,
                depth=2.8/100,
                location=((-1)**i*(picar_width/2 + wheel_width/2 + 0.1/100), back_wheel_distance, wheel_radius-picar_height),
                scale=(1, 1, 1),
                rotation=(0, 90*pi/180, 0)
            )
            wheel_object = bpy.context.active_object
            wheel_object.name = f"wheel_{i}"
            wheel_object.parent = main_body
        bpy.ops.mesh.primitive_cube_add(
            size=1,
            location=(0, picar_length/2+line_sensor_length/2, line_sensor_elevation-picar_height),
            scale=(line_sensor_width, line_sensor_length, line_sensor_height),
        )
        line_sensor_object = bpy.context.active_object
        line_sensor_object.name = "line_sensor"
        line_sensor_object.parent = main_body
        for i in range(0, 5):
            bpy.ops.mesh.primitive_cylinder_add(
                radius=0.2/100,
                depth= sensor_height,
                location=((i-2)*sensors_distances, 1/4*line_sensor_length, -sensor_height/2-line_sensor_height),
                rotation=(0, 0, 0)
            )
            sensor_object = bpy.context.active_object
            sensor_object.name = f"Sensor_{i}"
            sensor_object.parent = line_sensor_object
        bpy.ops.object.empty_add(
            location=(0, picar_length/2, 2/100),
            radius=0.01
        )
        distance_sensor = bpy.context.active_object
        distance_sensor.name = "distance_sensor"
        distance_sensor.parent = main_body
        ShapeFactory.receptacleGen("Receptacle", [0, picar_length/2 - 4.7625/100, 0.003], main_body)
        back_car.location = location
        if(parent != None):
            back_car.parent = parent