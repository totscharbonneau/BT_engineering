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
bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj1 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj1'

bpy.ops.mesh.primitive_cube_add(location=(0,0,0),size=1)
obstacle_obj1 = bpy.context.active_object
bpy.context.active_object.name = 'obstacle_obj1'
# CREATION DES OBJETS FINI

# MODIFICATION DES OBJETS
# LIGNE 1
obj_location(plane_obj1,0,575,0)
obj_scale(plane_obj1,largeur,1150,0)

# OBSTACLE 1
obj_location(obstacle_obj1,0,625,0)
obj_scale(obstacle_obj1,100,50,200)
# MODIFICATION DES OBJETS FINI