import bpy
from bpy.props import IntProperty

#class RemoveData(bpy.types.Operator):
    #bl_description = ""
    #bl_idname = "lights.remove_data"
    #bl_label = "Simple Object Operator"

    #for light in bpy.data.lights:
        #if light.users == 0:
             #bpy.data.lights.remove(light)

    #@classmethod
    #def poll(cls, context):
        #return context.active_object is not None

    #def execute(self, context):
        #return {'FINISHED'}


class View3DPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    bl_label = "Lights"

    def draw(self, context):
        layout = self.layout

        layout.scale_y = 1.1
        #layout.operator("lights.remove_data")
        
        for light in bpy.data.lights:
            #layout.label(text="----")
            layout.label(text=str(light.name),icon='LIGHT')
            layout.prop(light, "color",slider=True)
            layout.prop(light, "energy",slider=True)
            layout.prop(light, "angle",slider=True) 
        
        
def register():
    bpy.utils.register_class(View3DPanel)
    #bpy.utils.register_class(RemoveData)


def unregister():
    bpy.utils.unregister_class(View3DPanel)
    #bpy.utils.unregister_class(RemoveData)

if __name__ == "__main__":
    register()
