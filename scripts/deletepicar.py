import bpy

collection_name = "picar_coll"

if collection_name in bpy.data.collections:
    picar_collection = bpy.data.collections[collection_name]

    # Iterate through the objects in the collection and remove them
    for obj in picar_collection.objects:
        bpy.data.objects.remove(obj)

    # Remove the collection itself
    bpy.data.collections.remove(picar_collection)