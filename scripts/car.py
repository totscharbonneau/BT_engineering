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


wheel_radius = 6.35/2
wheel_width = 2.8
picar_length = 23.5
picar_height = 4.75    
picar_width = 8

bpy.ops.mesh.primitive_cube_add(
    size=1,
    location=(0, 0, picar_height),
    scale=(picar_width, picar_length, 0.3)
)

main_body = bpy.context.active_object
main_body.name = "main_body"

for i in range(0, 4):
    if (i < 2): back_wheel_distance = -picar_length/2 + 4.12
    else: back_wheel_distance = picar_length/2 - 4.7625
    bpy.ops.mesh.primitive_cylinder_add(
        radius=wheel_radius,
        depth=2.8,
        location=((-1)**i*(picar_width/2 + wheel_width/2 + 0.1), back_wheel_distance, wheel_radius-picar_height),
        scale=(1, 1, 1),
        rotation=(0, 90*np.pi/180, 0)
    )

    wheel_object = bpy.context.active_object
    wheel_object.name = f"wheel_{i}"
    wheel_object.parent = main_body

line_sensor_height = 0.3
line_sensor_length = 3
line_sensor_width = 12.3825
line_sensor_elevation = 1.9
sensors_distances = 1.9
sensor_height = 2.3

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
        radius=0.2,
        depth= sensor_height,
        location=((i-2)*sensors_distances, 1/4*line_sensor_length, -sensor_height/2-line_sensor_height),
        rotation=(0, 0, 0)
    )
    sensor_object = bpy.context.active_object
    sensor_object.name = f"Sensor_{i}"
    sensor_object.parent = line_sensor_object

bpy.ops.mesh.primitive_cube_add(
    size=1,
    location=(0, picar_length/2, 2),
    scale=(2, 0.5, 1)
)

other_object = bpy.context.active_object
other_object.parent = main_body