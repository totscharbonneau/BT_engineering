import bpy

def recurLayerCollection(layer_collection, collection_name):
    found = None
    if (layer_collection.name == collection_name):
        return layer_collection
    for layer in layer_collection.children:
        found = recurLayerCollection(layer, collection_name)
        if found:
            return found

environement = bpy.data.collections.new('env_coll')
bpy.context.scene.collection.children.link(environement)
layer_collection = bpy.context.view_layer.layer_collection
sub_layer_collection = recurLayerCollection(layer_collection, 'env_coll')
bpy.context.view_layer.active_layer_collection = sub_layer_collection


bpy.ops.mesh.primitive_plane_add(
    size=500,
    enter_editmode=False,
    align='WORLD',
    location=(0, 0, 0),
    scale=(1, 1, 1)
    )
