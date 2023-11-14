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


wheel_radius = 6.35/2/100
wheel_width = 2.8/100
picar_length = 23.5/100
picar_height = 4.75/100    
picar_width = 8/100

bpy.ops.object.empty_add(
    location=(0, -picar_length/2 + 4.12/100, 0),
    radius=0.01,
    scale=(1,1,1)
    )
back_car = bpy.context.active_object
back_car.name = "back_car"

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
        rotation=(0, 90*np.pi/180, 0)
    )

    wheel_object = bpy.context.active_object
    wheel_object.name = f"wheel_{i}"
    wheel_object.parent = main_body

line_sensor_height = 0.3/100
line_sensor_length = 3/100
line_sensor_width = 12.3825/100
line_sensor_elevation = 1.9/100
sensors_distances = 1.9/100
sensor_height = 2.3/100

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

bpy.ops.mesh.primitive_cube_add(
    size=1,
    location=(0, picar_length/2, 2/100),
    scale=(2/100, 0.5/100, 1/100)
)

other_object = bpy.context.active_object
other_object.parent = main_body