import bpy
import mathutils
import bmesh
from mathutils.bvhtree import BVHTree


sensor0 = bpy.data.objects["Sensor_0"]
sensor1 = bpy.data.objects["Sensor_1"]
sensor2 = bpy.data.objects["Sensor_2"]
sensor3 = bpy.data.objects["Sensor_3"]
sensor4 = bpy.data.objects["Sensor_4"]

route = bpy.data.objects["plane_obj1"]

def line_sensor(track):
    
    sensor0 = bpy.data.objects["Sensor_0"]
    sensor1 = bpy.data.objects["Sensor_1"]
    sensor2 = bpy.data.objects["Sensor_2"]
    sensor3 = bpy.data.objects["Sensor_3"]
    sensor4 = bpy.data.objects["Sensor_4"]
    output = []
    sensorlist = [sensor0,sensor1,sensor2,sensor3,sensor4]
    bm_track = bmesh.new()
    bm_track.from_mesh(track.data)
    bm_track.transform(track.matrix_world) 
    obj_track_BVHtree = BVHTree.FromBMesh(bm_track) 

    for sensor in sensorlist:

        bm1 = bmesh.new()
        bm1.from_mesh(sensor.data)
        bm1.transform(sensor.matrix_world)
        obj1_BVHtree = BVHTree.FromBMesh(bm1)
        overlap = obj1_BVHtree.overlap(obj_track_BVHtree)

        output.append(int(bool(overlap)))
    # Check for collisions
    
    
    return output

print(line_sensor(route))
