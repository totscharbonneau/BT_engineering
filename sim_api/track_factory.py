import bpy
import math
import bpy
import math
lineWidth = 0.018
general_scale = 0.001 # MODIFIER LA TAILLE DE RÉFÉRENCE
largeur = 18

general_scale = 0.001 # MODIFIER LA TAILLE DE RÉFÉRENCE

class TrackFactory:

    def track1(name, nameObstacle, location=(0, 0, 0), locationObstacle=(0, 0, 0)):
        bpy.ops.mesh.primitive_plane_add(location=location, size=1)
        track = bpy.context.active_object
        track.scale = (lineWidth, 1.15, 0)
        track.name = name
        bpy.ops.mesh.primitive_cube_add(location=locationObstacle, size=1, scale=(0.1,0.05,0.2))
        obstacle = bpy.context.active_object
        obstacle.name = nameObstacle


    def track2(name, location=(0, 0, 0)):
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0.2,0), scale=(0.2,0.2,0.002))
        sphere_outer1 = bpy.context.object
        bpy.context.active_object.name = 'courbe1'
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0.7-lineWidth,0), scale=(0.3,0.3,0.002))
        sphere_outer2 = bpy.context.object
        bpy.context.active_object.name = 'courbe2'
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,-0.25+lineWidth,0), scale=(0.25,0.25,0.002))
        sphere_outer3 = bpy.context.object
        bpy.context.active_object.name = 'courbe3'
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,1.25-lineWidth*2,0), scale=(0.25,0.25,0.002))
        sphere_outer4 = bpy.context.object
        bpy.context.active_object.name = 'courbe4'
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0.2,0), scale=(0.2-lineWidth,0.2-lineWidth,0.02))
        sphere_bool1 = bpy.context.object
        bpy.context.active_object.name = 'sphere_bool1'
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0.7-lineWidth,0), scale=(0.3-lineWidth,0.3-lineWidth,0.02))
        sphere_bool2 = bpy.context.object
        bpy.context.active_object.name = 'sphere_bool2'
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,-0.25+lineWidth,0), scale=(0.25-lineWidth,0.25-lineWidth,0.02))
        sphere_bool3 = bpy.context.object
        bpy.context.active_object.name = 'sphere_bool3'
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,1.25-lineWidth*2,0), scale=(0.25-lineWidth,0.25-lineWidth,0.02))
        sphere_bool4 = bpy.context.object
        bpy.context.active_object.name = 'sphere_bool4'
        bpy.ops.mesh.primitive_cube_add(location=(-0.5,0,0), scale=(0.5,2,0.02))
        cube_bool1 = bpy.context.object
        bpy.context.active_object.name = 'cube_bool1'
        bpy.ops.mesh.primitive_cube_add(location=(0.5,0,0), scale=(0.5,2,0.02))
        cube_bool2 = bpy.context.object
        bpy.context.active_object.name = 'cube_bool2'

        bpy.ops.object.select_all(action='DESELECT')
        sphere_outer1.select_set(True)
        bpy.context.view_layer.objects.active = sphere_outer1
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'
        bool_modifier.object = sphere_bool1
        bpy.ops.object.modifier_apply({"object": sphere_outer1}, modifier=bool_modifier.name)
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'
        bool_modifier.object = cube_bool2
        bpy.ops.object.modifier_apply({"object": sphere_outer1}, modifier=bool_modifier.name)
        sphere_outer1.scale.z = 0.0

        bpy.ops.object.select_all(action='DESELECT')
        sphere_outer2.select_set(True)
        bpy.context.view_layer.objects.active = sphere_outer2
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'
        bool_modifier.object = sphere_bool2
        bpy.ops.object.modifier_apply({"object": sphere_outer2}, modifier=bool_modifier.name)
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'
        bool_modifier.object = cube_bool1
        bpy.ops.object.modifier_apply({"object": sphere_outer2}, modifier=bool_modifier.name)
        sphere_outer2.scale.z = 0.0

        bpy.ops.object.select_all(action='DESELECT')
        sphere_outer3.select_set(True)
        bpy.context.view_layer.objects.active = sphere_outer3
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'
        bool_modifier.object = sphere_bool3
        bpy.ops.object.modifier_apply({"object": sphere_outer3}, modifier=bool_modifier.name)
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'
        bool_modifier.object = cube_bool1
        bpy.ops.object.modifier_apply({"object": sphere_outer3}, modifier=bool_modifier.name)

        bpy.ops.object.select_all(action='DESELECT')
        sphere_outer4.select_set(True)
        bpy.context.view_layer.objects.active = sphere_outer4
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'
        bool_modifier.object = sphere_bool4
        bpy.ops.object.modifier_apply({"object": sphere_outer4}, modifier=bool_modifier.name)
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'
        bool_modifier.object = cube_bool2
        bpy.ops.object.modifier_apply({"object": sphere_outer4}, modifier=bool_modifier.name)

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects["cube_bool2"].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects["cube_bool2"]
        bpy.ops.transform.rotate(value=0.52, orient_axis='Z') 
        bpy.ops.transform.translate(value=(0, -0.53, 0))

        bpy.ops.object.select_all(action='DESELECT')
        sphere_outer3.select_set(True)
        bpy.context.view_layer.objects.active = sphere_outer3
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'
        bool_modifier.object = cube_bool2
        bpy.ops.object.modifier_apply({"object": sphere_outer3}, modifier=bool_modifier.name)
        sphere_outer3.scale.z = 0.0

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects["cube_bool2"].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects["cube_bool2"]
        bpy.ops.transform.translate(value=(-0.16, 3.53, 0))

        bpy.ops.object.select_all(action='DESELECT')
        sphere_outer4.select_set(True)
        bpy.context.view_layer.objects.active = sphere_outer4
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'
        bool_modifier.object = cube_bool2
        bpy.ops.object.modifier_apply({"object": sphere_outer4}, modifier=bool_modifier.name)
        sphere_outer4.scale.z = 0.0

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects.remove(sphere_bool1, do_unlink=True)
        bpy.data.objects.remove(sphere_bool2, do_unlink=True)
        bpy.data.objects.remove(sphere_bool3, do_unlink=True)
        bpy.data.objects.remove(sphere_bool4, do_unlink=True)
        bpy.data.objects.remove(cube_bool1, do_unlink=True)
        bpy.data.objects.remove(cube_bool2, do_unlink=True)

        bpy.ops.object.select_all(action='DESELECT')
        sphere_outer1.select_set(True)
        sphere_outer2.select_set(True)
        sphere_outer3.select_set(True)
        sphere_outer4.select_set(True)
        bpy.context.view_layer.objects.active = sphere_outer1
        bpy.ops.object.join()
        sphere_outer1.name = name
        bpy.ops.transform.rotate(value=0.95, orient_axis='Z') 
        bpy.ops.transform.translate(value=(0.12, 0.1, 0))
        bpy.ops.object.select_all(action='DESELECT')

    def track3(name,  location=(0, 0, 0)):
        bpy.ops.mesh.primitive_plane_add(location=(0,0.25,0), size=1)
        track = bpy.context.active_object
        track.scale = (lineWidth,0.5,0)
        bpy.ops.mesh.primitive_plane_add(location=(0,0.5,0), size=1)
        track2 = bpy.context.active_object
        track2.scale = (lineWidth,0.5,0)
        track2.rotation_euler.z += math.radians(90)
        track.select_set(True)
        track2.select_set(True)
        bpy.context.view_layer.objects.active = track
        bpy.ops.object.join()
        track.name = name