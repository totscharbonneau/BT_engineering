import bpy
import math
lineWidth = 0.018
general_scale = 0.001 # MODIFIER LA TAILLE DE RÉFÉRENCE
largeur = 18


class TrackFactory:
    # LES TAILLES SONT CODER EN mm ET MODIFIABLE VIA LE general_scale

    def track1(name, nameObstacle, location=(0, 0, 0), locationObstacle=(0, 0, 0)):
        # CREATION DES OBJETS
        bpy.ops.mesh.primitive_plane_add(location=location, size=1)
        track = bpy.context.active_object
        track.scale = (lineWidth, 1.15, 0)
        track.name = name

        bpy.ops.mesh.primitive_cube_add(location=locationObstacle, size=1, scale=(0.1,0.05,0.2))
        obstacle = bpy.context.active_object
        obstacle.name = nameObstacle


    def track2(name, nameObstacle, location=(0, 0, 0), locationObstacle=(0, 0, 0)):
        # CREATION DES OBJETS
        # COURBE 1
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
        sphere_outer1 = bpy.context.object
        bpy.context.active_object.name = 'courbe1'

        # COURBE 2
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
        sphere_outer2 = bpy.context.object
        bpy.context.active_object.name = 'courbe2'

        # COURBE 3
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
        sphere_outer3 = bpy.context.object
        bpy.context.active_object.name = 'courbe3'

        # COURBE 4
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
        sphere_outer4 = bpy.context.object
        bpy.context.active_object.name = 'courbe4'

        # BOOLEAN 1
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
        sphere_bool1 = bpy.context.object
        bpy.context.active_object.name = 'sphere_bool1'

        # BOOLEAN 2
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
        sphere_bool2 = bpy.context.object
        bpy.context.active_object.name = 'sphere_bool2'

        # BOOLEAN 3
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
        sphere_bool3 = bpy.context.object
        bpy.context.active_object.name = 'sphere_bool3'

        # BOOLEAN 4
        bpy.ops.mesh.primitive_uv_sphere_add(location=(0,0,0))
        sphere_bool4 = bpy.context.object
        bpy.context.active_object.name = 'sphere_bool4'

        # BOOLEAN 5
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
        cube_bool1 = bpy.context.object
        bpy.context.active_object.name = 'cube_bool1'

        # BOOLEAN 6
        bpy.ops.mesh.primitive_cube_add(location=(0,0,0))
        cube_bool2 = bpy.context.object
        bpy.context.active_object.name = 'cube_bool2'


        # CREATION DES OBJETS FINI

        # MODIFICATION DES OBJETS
        # COURBE 1
        obj_location(sphere_outer1,0,200,0)
        obj_scale(sphere_outer1,200,200,2)

        # COURBE 2
        obj_location(sphere_outer2,0,700-largeur,0)
        obj_scale(sphere_outer2,300,300,2)

        # COURBE 3
        obj_location(sphere_outer3,0,-250+largeur,0)
        obj_scale(sphere_outer3,250,250,2)

        # COURBE 4
        obj_location(sphere_outer4,0,1250-largeur*2,0)
        obj_scale(sphere_outer4,250,250,2)


        # BOOLEAN 1
        obj_location(sphere_bool1,0,200,0)
        obj_scale(sphere_bool1,200-largeur,200-largeur,20)

        # BOOLEAN 2
        obj_location(sphere_bool2,0,700-largeur,0)
        obj_scale(sphere_bool2,300-largeur,300-largeur,20)

        # BOOLEAN 3
        obj_location(sphere_bool3,0,-250+largeur,0)
        obj_scale(sphere_bool3,250-largeur,250-largeur,20)

        # BOOLEAN 4
        obj_location(sphere_bool4,0,1250-largeur*2,0)
        obj_scale(sphere_bool4,250-largeur,250-largeur,20)

        # CUBE BOOLEAN 1
        obj_location(cube_bool1,-500,0,0)
        obj_scale(cube_bool1,500,2000,20)

        # CUBE BOOLEAN 2
        obj_location(cube_bool2,500,0,0)
        obj_scale(cube_bool2,500,2000,20)

        # MODIFICATION DES OBJETS FINI


        ##### MODIFICATION BOOLEAN #####

        # COURBE 1
        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects["courbe1"].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects["courbe1"]

        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'

        bool_modifier.object = bpy.data.objects["sphere_bool1"]
        bpy.ops.object.modifier_apply({"object": bpy.context.active_object}, modifier=bool_modifier.name)

        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'

        bool_modifier.object = bpy.data.objects["cube_bool2"]
        bpy.ops.object.modifier_apply({"object": bpy.context.active_object}, modifier=bool_modifier.name)

        # Changez l'échelle en Z à 0
        bpy.context.active_object.scale.z = 0.0

        # COURBE 2
        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects["courbe2"].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects["courbe2"]

        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'

        bool_modifier.object = bpy.data.objects["sphere_bool2"]
        bpy.ops.object.modifier_apply({"object": bpy.context.active_object}, modifier=bool_modifier.name)

        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'

        bool_modifier.object = bpy.data.objects["cube_bool1"]
        bpy.ops.object.modifier_apply({"object": bpy.context.active_object}, modifier=bool_modifier.name)

        # Changez l'échelle en Z à 0
        bpy.context.active_object.scale.z = 0.0

        # COURBE 3
        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects["courbe3"].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects["courbe3"]

        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'

        bool_modifier.object = bpy.data.objects["sphere_bool3"]
        bpy.ops.object.modifier_apply({"object": bpy.context.active_object}, modifier=bool_modifier.name)

        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'

        bool_modifier.object = bpy.data.objects["cube_bool1"]
        bpy.ops.object.modifier_apply({"object": bpy.context.active_object}, modifier=bool_modifier.name)

        # COURBE 4
        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects["courbe4"].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects["courbe4"]

        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'

        bool_modifier.object = bpy.data.objects["sphere_bool4"]
        bpy.ops.object.modifier_apply({"object": bpy.context.active_object}, modifier=bool_modifier.name)

        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'

        bool_modifier.object = bpy.data.objects["cube_bool2"]
        bpy.ops.object.modifier_apply({"object": bpy.context.active_object}, modifier=bool_modifier.name)


        # MOUVEMENT CUBE 2

        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects["cube_bool2"].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects["cube_bool2"]
        bpy.ops.transform.rotate(value=0.52, orient_axis='Z') 
        bpy.ops.transform.translate(value=(0, -0.53, 0))

        # COURBE 3
        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects["courbe3"].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects["courbe3"]

        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'

        bool_modifier.object = bpy.data.objects["cube_bool2"]
        bpy.ops.object.modifier_apply({"object": bpy.context.active_object}, modifier=bool_modifier.name)

        # Changez l'échelle en Z à 0
        bpy.context.active_object.scale.z = 0.0

        # MOUVEMENT CUBE 2

        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects["cube_bool2"].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects["cube_bool2"]
        bpy.ops.transform.translate(value=(-0.16, 3.53, 0))

        # COURBE 4
        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects["courbe4"].select_set(True)
        bpy.context.view_layer.objects.active = bpy.data.objects["courbe4"]

        bpy.ops.object.modifier_add(type='BOOLEAN')
        bool_modifier = bpy.context.object.modifiers[-1]
        bool_modifier.name = "Boolean"
        bool_modifier.operation = 'DIFFERENCE'

        bool_modifier.object = bpy.data.objects["cube_bool2"]
        bpy.ops.object.modifier_apply({"object": bpy.context.active_object}, modifier=bool_modifier.name)

        # Changez l'échelle en Z à 0
        bpy.context.active_object.scale.z = 0.0

        ##### MODIFICATION BOOLEAN #####


        # SUPPRIMER LES OBJETS DE MODIFICATION BOOLEAN
        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects.remove(bpy.data.objects.get("sphere_bool1"), do_unlink=True)
        bpy.data.objects.remove(bpy.data.objects.get("sphere_bool2"), do_unlink=True)
        bpy.data.objects.remove(bpy.data.objects.get("sphere_bool3"), do_unlink=True)
        bpy.data.objects.remove(bpy.data.objects.get("sphere_bool4"), do_unlink=True)
        bpy.data.objects.remove(bpy.data.objects.get("cube_bool1"), do_unlink=True)
        bpy.data.objects.remove(bpy.data.objects.get("cube_bool2"), do_unlink=True)
        # FIN SUPPRIMER LES OBJETS DE MODIFICATION BOOLEAN


        # FUSIONNER LES LIGNES POUR DÉPLACEMENT 
        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects["courbe1"].select_set(True)
        bpy.data.objects["courbe2"].select_set(True)
        bpy.data.objects["courbe3"].select_set(True)
        bpy.data.objects["courbe4"].select_set(True)

        bpy.context.view_layer.objects.active = bpy.data.objects["courbe1"]
        bpy.ops.object.join()
        bpy.data.objects["courbe1"].name = name


        bpy.ops.transform.rotate(value=0.95, orient_axis='Z') 
        bpy.ops.transform.translate(value=(0.12, 0.1, 0))
        bpy.ops.object.select_all(action='DESELECT')

        bpy.ops.mesh.primitive_cube_add(location=locationObstacle, size=1, scale=(0.1,0.05,0.2))
        obstacle = bpy.context.active_object
        obstacle.name = nameObstacle
        # FIN FUSIONNER LES LIGNES POUR DÉPLACEMENT

    def track3(name, nameObstacle, location=(0, 0, 0), locationObstacle=(0, 0, 0)):
        bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
        plane_obj1 = bpy.context.active_object
        bpy.context.active_object.name = 'plane_obj1'

        bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
        plane_obj2 = bpy.context.active_object
        bpy.context.active_object.name = 'plane_obj2'
        # CREATION DES OBJETS FINI
        
        # MODIFICATION DES OBJETS
        # LIGNE 1
        obj_location(plane_obj1,0,250,0)
        obj_scale(plane_obj1,largeur,500,0)

        # LIGNE 2
        obj_location(plane_obj2,0,500,0)
        obj_scale(plane_obj2,largeur,150,0)
        obj_rotation(plane_obj2,90)
        # MODIFICATION DES OBJETS FINI

        bpy.ops.object.select_all(action='DESELECT')

        bpy.data.objects["plane_obj1"].select_set(True)
        bpy.data.objects["plane_obj2"].select_set(True)

        bpy.context.view_layer.objects.active = bpy.data.objects["plane_obj1"]
        bpy.ops.object.join()

        bpy.data.objects["plane_obj1"].name = name

        bpy.ops.mesh.primitive_cube_add(location=locationObstacle, size=1, scale=(0.1,0.05,0.2))
        obstacle = bpy.context.active_object
        obstacle.name = nameObstacle
        # FIN FUSIONNER LES LIGNES POUR DÉPLACEMENT


def obj_location(object,x,y,z):
    object.location.x = x*general_scale
    object.location.y = y*general_scale
    object.location.z = z*general_scale

def obj_scale(object,x,y,z):
    object.scale.x = x*general_scale
    object.scale.y = y*general_scale
    object.scale.z = z*general_scale

def obj_rotation(object,angle):
    angle_degrees = angle 
    angle_radians = math.radians(angle_degrees)
    object.rotation_euler.z += angle_radians
