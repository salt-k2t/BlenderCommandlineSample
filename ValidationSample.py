import bpy
import glob
import os
import json

if __name__ == "__main__":    
    files = glob.glob("./Samples/*.blend")    
    results = {}
    for file in files:
        file_name = os.path.splitext(os.path.basename(file))[0]
        scn_file = "./Samples/" + file_name + ".blend"
        png_file = "./Images/" + file_name+ ".png"

        # Open scene
        bpy.ops.wm.open_mainfile(filepath=scn_file)

        # Export rendered image to png file
        bpy.ops.render.render()
        bpy.data.images['Render Result'].save_render(filepath = png_file)
        
        # Validate
        if  "Cube" in bpy.context.scene.objects:
            print("Valid")
            results[file_name] = "Valid"
        else:
            print("Invalid")            
            results[file_name] = "Invalid"

    # Export result
    with open("./result.json", 'w') as outfile:
        json.dump(results, outfile, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    
    # Quit Blender
    bpy.ops.wm.quit_blender()
