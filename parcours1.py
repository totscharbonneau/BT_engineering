import bpy
import numpy as np
import math

def obj_location(object,x,y,z):
    object.location.x = x
    object.location.y = y
    object.location.z = z

def obj_scale(object,x,y,z):
    object.scale.x = x
    object.scale.y = y
    object.scale.z = z

def obj_rotation(object,angle):
    angle_degrees = angle 
    angle_radians = math.radians(angle_degrees)
    object.rotation_euler.z += angle_radians

general_scale = 0.1
largeur = 18*general_scale
longueur = 1052*general_scale

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj1 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj1'

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj2 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj2'

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj3 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj3'

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj4 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj4'

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj5 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj5'

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj6 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj6'

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj7 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj7'

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj8 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj8'

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj9 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj9'

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj10 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj10'

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj11 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj11'

bpy.ops.mesh.primitive_plane_add(location=(0,0,0),size=1)
plane_obj12 = bpy.context.active_object
bpy.context.active_object.name = 'plane_obj12'


# LIGNE 1
obj_location(plane_obj1,0,0,0)
obj_scale(plane_obj1,largeur,1052*general_scale,0)

# LIGNE 2
obj_location(plane_obj2,-240*general_scale,276*general_scale,0)
obj_scale(plane_obj2,largeur,500*general_scale,0)

# LIGNE 3
obj_location(plane_obj3,-516*general_scale,276*general_scale,0)
obj_scale(plane_obj3,largeur,500*general_scale,0)

# LIGNE 4
obj_location(plane_obj4,-756*general_scale,0*general_scale,0)
obj_scale(plane_obj4,largeur,1052*general_scale,0)

# LIGNE 5
obj_location(plane_obj5,-1094*general_scale,-664*general_scale,0)
obj_scale(plane_obj5,largeur,400*general_scale,0)
obj_rotation(plane_obj5,90)

# LIGNE 6
obj_location(plane_obj6,-1432*general_scale,-426*general_scale,0)
obj_scale(plane_obj6,largeur,200*general_scale,0)

# LIGNE 7
obj_location(plane_obj7,-1194*general_scale,-188*general_scale,0)
obj_scale(plane_obj7,largeur,200*general_scale,0)
obj_rotation(plane_obj7,90)

# LIGNE 8
obj_location(plane_obj8,-954*general_scale,150*general_scale,0)
obj_scale(plane_obj8,largeur,400*general_scale,0)




# LIGNE 12
obj_location(plane_obj12,276*general_scale,174*general_scale,0)
obj_scale(plane_obj12,largeur,1400*general_scale,0)



# COURBE 1
bpy.ops.mesh.primitive_uv_sphere_add(location=(-120*general_scale, 526*general_scale, 0), scale=((120*general_scale + largeur/2),(120*general_scale+ largeur/2),0))
sphere_outer1 = bpy.context.object
bpy.context.active_object.name = 'courbe1'

# COURBE 2
bpy.ops.mesh.primitive_uv_sphere_add(location=(-378*general_scale, 26*general_scale, 0), scale=((138*general_scale + largeur/2),(138*general_scale+ largeur/2),0))
sphere_outer2 = bpy.context.object
bpy.context.active_object.name = 'courbe2'

# COURBE 3
bpy.ops.mesh.primitive_uv_sphere_add(location=(-636*general_scale, 526*general_scale, 0), scale=((120*general_scale + largeur/2),(120*general_scale+ largeur/2),0))
sphere_outer3 = bpy.context.object
bpy.context.active_object.name = 'courbe3'

# COURBE 4
bpy.ops.mesh.primitive_uv_sphere_add(location=(-894*general_scale, -526*general_scale, 0), scale=((138*general_scale + largeur/2),(138*general_scale+ largeur/2),0))
sphere_outer4 = bpy.context.object
bpy.context.active_object.name = 'courbe4'

# COURBE 5
bpy.ops.mesh.primitive_uv_sphere_add(location=(-1294*general_scale, -526*general_scale, 0), scale=((138*general_scale + largeur/2),(138*general_scale+ largeur/2),0))
sphere_outer5 = bpy.context.object
bpy.context.active_object.name = 'courbe5'

# COURBE 6
bpy.ops.mesh.primitive_uv_sphere_add(location=(-1294*general_scale, -326*general_scale, 0), scale=((138*general_scale + largeur/2),(138*general_scale+ largeur/2),0))
sphere_outer6 = bpy.context.object
bpy.context.active_object.name = 'courbe6'

# COURBE 7
bpy.ops.mesh.primitive_uv_sphere_add(location=(-1094*general_scale, -50*general_scale, 0), scale=((138*general_scale + largeur/2),(138*general_scale+ largeur/2),0))
sphere_outer7 = bpy.context.object
bpy.context.active_object.name = 'courbe7'

# COURBE 8
bpy.ops.mesh.primitive_uv_sphere_add(location=(-1094*general_scale, 350*general_scale, 0), scale=((138*general_scale + largeur/2),(138*general_scale+ largeur/2),0))
sphere_outer8 = bpy.context.object
bpy.context.active_object.name = 'courbe8'



# COURBE 12
bpy.ops.mesh.primitive_uv_sphere_add(location=(138*general_scale, -526*general_scale, 0), scale=((138*general_scale + largeur/2),(138*general_scale+ largeur/2),0))
sphere_outer12 = bpy.context.object
bpy.context.active_object.name = 'courbe12'