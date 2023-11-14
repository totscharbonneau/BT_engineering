import bpy, mathutils

bpy.context.scene.unit_settings.system = 'METRIC'
bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
bpy.context.scene.unit_settings.mass_unit = 'GRAMS'
bpy.ops.rigidbody.world_add()
bpy.context.scene.rigidbody_world.time_scale = 1
bpy.context.scene.rigidbody_world.substeps_per_frame = 70
bpy.context.object.scale[0] = 0.025
bpy.context.object.scale[1] = 0.025
bpy.context.object.scale[2] = 0.0015
bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0, 0.14), scale=(0.14, 0.14, 0.14))
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
bpy.data.objects["Cube"].select_set(True)
bpy.data.objects["Sphere"].select_set(False)
bpy.context.view_layer.objects.active = bpy.data.objects["Cube"]
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Sphere"]
bpy.context.object.modifiers["Boolean"].solver = 'EXACT'
bpy.ops.object.modifier_set_active(modifier="Boolean")
bpy.ops.object.convert(target='MESH')
bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
for obj in bpy.context.selected_objects:
    obj.name = "Coupole"
bpy.ops.rigidbody.object_add()  
bpy.context.object.rigid_body.type = 'PASSIVE'
bpy.context.object.rigid_body.collision_shape = 'MESH'
bpy.context.object.rigid_body.mesh_source = 'BASE'
bpy.context.object.rigid_body.friction = 1
bpy.context.object.rigid_body.restitution = 0
bpy.data.objects["Cube"].select_set(True)
bpy.data.objects["Coupole"].select_set(False)
bpy.context.view_layer.objects.active = bpy.data.objects["Cube"]
bpy.ops.object.delete() 
bpy.data.objects["Sphere"].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects["Sphere"]
bpy.ops.object.delete() 
bpy.ops.mesh.primitive_uv_sphere_add(enter_editmode=False, align='WORLD', location=(0, 0.015, 0.0223344), scale=(0.003995, 0.003995, 0.003995))
bpy.ops.rigidbody.object_add()
bpy.context.object.rigid_body.mass = 0.00517
bpy.context.object.rigid_body.collision_shape = 'SPHERE'
bpy.context.object.rigid_body.friction = 1
bpy.context.object.rigid_body.restitution = 0
bpy.context.object.rigid_body.linear_damping = 0.7
bpy.data.objects["Coupole"].select_set(True)
bpy.data.objects["Sphere"].select_set(False)
test = mathutils.bvhtree.BVHTree.find_nearest(bpy.data.objects["Coupole"].data.vertices,mathutils.Vector((-1, -1, 1)), 0.1)
bpy.data.objects["Coupole"].__getattribute__


def distance():
    vehicule = bpy.data.objects["Coupole"]
    verts = [vert.co for vert in vehicule.data.vertices]
    test = verts.index(mathutils.Vector((1, -1, -1)))