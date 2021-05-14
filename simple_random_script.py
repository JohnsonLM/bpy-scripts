import bpy
import random 

data = bpy.data
ops = bpy.ops
object = data.objects



def randomizeLocRot():
    object["Cube"].rotation_euler[0] = random.randint(1,9)
  
  
    
def randomizeCamera():
    #Add Camera if none exists
    if data.scenes["Scene"].camera == None:
        ops.object.camera_add()
        data.scenes["Scene"].camera = object["Camera"]
    else:
        print("else")
    
    
    
def export():
    ops.render.render()
    
    
render_num = range(10)

for render in render_num:
    randomizeLocRot()
    randomizeCamera()
    export()