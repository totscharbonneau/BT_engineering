import bpy

class SimContext:
    def setBlenderEnv():
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