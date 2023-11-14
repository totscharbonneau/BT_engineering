import bpy
import numpy as np
import math

# LES TAILLES SONT CODER EN mm ET MODIFIABLE VIA LE general_scale

# FONCTION GENERAL POUR MODIFIER UN OBJET: LA POSITION / LA TAILLE / LA ROTATION
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

general_scale = 0.001 # MODIFIER LA TAILLE DE RÉFÉRENCE
largeur = 18

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