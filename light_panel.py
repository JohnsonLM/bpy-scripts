bl_info = {
    "name": "Light Panel",
    "author": "Johnson Martin",
    "version": (0, 1),
    "blender": (2, 92, 0),
    "location": "View3D > Sidebar > Tool Panel",
    "description": "Adds panel for quickly adjusting lights in viewport",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

import bpy

class LightPanel(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Tool"
    bl_label = "Lights"
    bl_idname = "OBJECT_PT_LightPanel"

    def draw(self, context):
        layout = self.layout

        box = layout
        row = box.row()
        row.label(text="Color Palette (drag/drop)",icon='COLOR')
        row = box.row()
        row.template_palette(context.tool_settings.image_paint, "palette", color=False)


        world = bpy.data.worlds['World']
        box = layout.box()
        row = box.row()
        row.label(icon='WORLD')
        row.label(text=str(world.name) + " (See world properties for color)")

        #row.label(text="See world panel for color.")
        row = box.row()
        row.prop(world.node_tree.nodes["Background"].inputs[1], "default_value", text="Strength")


        #list data for lights
        for object in bpy.data.objects:
            if object.type == "LIGHT":
                box = layout.box()
                row = box.row()

                light = object.data

                if light.type == "SUN":
                    row.label(text=str(object.name),icon='LIGHT_SUN')
                    row = box.row()
                    row = box.row()
                    row.prop(light, "color",text="")
                    row = box.row()
                    row.prop(light, "energy")
                    row.prop(light, "angle")
                if light.type == "POINT":
                    row.label(text=str(object.name),icon='LIGHT_POINT')
                    row = box.row()
                    row = box.row()
                    row.prop(light, "color",text="")
                    row = box.row()
                    row.prop(light, "energy")
                    row.prop(light, "shadow_soft_size",text="Radius")
                if light.type == "SPOT":
                    row.label(text=str(object.name),icon='LIGHT_SPOT')
                    row = box.row()
                    row = box.row()
                    row.prop(light, "color",text="")
                    row = box.row()
                    row.prop(light, "energy")
                    row.prop(light, "shadow_soft_size",text="Radius")
                if light.type == "AREA":
                    row.label(text=str(object.name),icon='LIGHT_AREA')
                    row = box.row()
                    row = box.row()
                    row.prop(light, "color",text="")
                    row = box.row()
                    row.prop(light, "energy")
                    row.prop(light, "size",text="Size X")
                    row = box.row()
                    row.prop(light, "shape",text="")
                    row.prop(light, "size_y",text="Size Y")
                  

    
                else:
                    pass
        for material in bpy.data.materials:
            if "light" in material.name:
                box = layout.box()
                row = box.row()
                row.label(icon='META_PLANE')
                row.label(text=str(material.name))
                row = box.row()
                row.prop(material.node_tree.nodes["Principled BSDF"].inputs[17], "default_value", text="Color")
                row = box.row()
                row.prop(material.node_tree.nodes["Principled BSDF"].inputs[18], "default_value", text="Strength")
            else:
                pass
            
        layout.label(text="Only materials with 'light' suffix included as lights.",icon="PROP_OFF")
        

def register():
    bpy.utils.register_class(LightPanel)


def unregister():
    bpy.utils.unregister_class(LightPanel)


if __name__ == "__main__":
    register()

    
palette = bpy.data.palettes.get("LightPalette")
if palette is None:
    palette = bpy.data.palettes.new("LightPalette")
    
    # add colors to that palette
    col1 = palette.colors.new()
    col1.color = (0.931030, 1.000000, 0.505225)
    col2 = palette.colors.new()
    col2.color = (0.297170, 0.609276, 1.000000)
    col3 = palette.colors.new()
    col3.color = (1, 1, 1)
    col4 = palette.colors.new()
    col4.color = (1.000000, 0.905059, 0.222366)
    
    # make color active
    palette.colors.active = col1

bpy.context.tool_settings.image_paint.palette = palette
