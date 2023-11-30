import bpy

class SimContext:
    def setBlenderEnv(numberOfCycles):
        for obj in bpy.data.objects:
            obj.select_set(True)
        bpy.ops.object.delete()
        bpy.context.scene.unit_settings.system = 'METRIC'
        bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
        bpy.context.scene.unit_settings.mass_unit = 'GRAMS'
        if bpy.context.scene.rigidbody_world == None:
            bpy.ops.rigidbody.world_add()
        bpy.context.scene.rigidbody_world.time_scale = 1
        bpy.context.scene.rigidbody_world.substeps_per_frame = 70
        bpy.context.scene.frame_end = numberOfCycles
        bpy.context.scene.rigidbody_world.point_cache.frame_end = numberOfCycles