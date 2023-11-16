lineWidth = 0.018

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
