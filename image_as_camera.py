bl_info = {
    "name": "Add Image as Camera",
    "author": "Johnson Martin",
    "version": (0, 1),
    "blender": (2, 92, 0),
    "location": "View3D > Add menu > Camera",
    "description": "Allows user to add a camera with a background image quickly from the viewport",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

import bpy
import os
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator

class OT_to_camera(Operator, ImportHelper):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    bl_idname = "image_ref.to_camera"
    bl_label = "Image as Camera"

    def execute(self, context):
        # load image to blenddata
        img_path = self.filepath
        img = bpy.data.images.load(img_path, check_existing=False)

        # create camera
        camera = bpy.data.cameras.new("Camera")
        cam_obj1 = bpy.data.objects.new(img.name, camera)
        bpy.context.scene.collection.objects.link(cam_obj1)

        # add image background
        camera.show_background_images = True
        bg_img = camera.background_images.new()
        bg_img.image = img
        bg_img.frame_method = 'FIT'

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator("image_ref.to_camera",icon="IMAGE_DATA")

def register():
   bpy.utils.register_class(OT_to_camera)
   bpy.types.VIEW3D_MT_camera_add.prepend(menu_func)

def unregister():
    bpy.utils.unregister_class(OT_to_camera)
    bpy.types.VIEW3D_MT_camera_add.remove(menu_func)

if __name__ == "__main__":
    register()