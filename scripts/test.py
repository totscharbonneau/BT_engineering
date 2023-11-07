import bpy
import numpy as np

def recurLayerCollection(layer_collection, collection_name):
    found = None
    if (layer_collection.name == collection_name):
        return layer_collection
    for layer in layer_collection.children:
        found = recurLayerCollection(layer, collection_name)
        if found:
            return found

base_cude = bpy.data.objects.get("Cube")
if base_cude:
    bpy.data.objects.remove(base_cude, do_unlink=True)

picar = bpy.data.collections.new('picar_coll')
bpy.context.scene.collection.children.link(picar)
layer_collection = bpy.context.view_layer.layer_collection
sub_layer_collection = recurLayerCollection(layer_collection, 'picar_coll')
bpy.context.view_layer.active_layer_collection = sub_layer_collection


wheel_radius = 2
wheel_width = 0.5
picar_length = 20
picar_height = 2
picar_width = 10

bpy.ops.mesh.primitive_cube_add(
    size=1,
    location=(0, 0, wheel_radius+0.3),
    scale=(picar_width, picar_length, picar_height)
)

for i in range(0, 4):
    if (i < 2): back_wheel_distance = -picar_length/4
    else: back_wheel_distance = picar_length/4
    bpy.ops.mesh.primitive_cylinder_add(
        radius=wheel_radius,
        location=((-1)**i*(picar_width/2), back_wheel_distance, wheel_radius),
        scale=(1, 1, wheel_width),
        rotation=(0, 90*np.pi/180, 0)
    )

for i in range (0,2):
    if i == 0:
        position = picar_length/4
    elif i == 1:
        position = -picar_length/4
    bpy.ops.mesh.primitive_cylinder_add(
        radius=1,
        location=(0, position, wheel_radius),
        scale=(0.3, 0.3, 6),
        rotation=(0, 90*np.pi/180, 0)
    )
