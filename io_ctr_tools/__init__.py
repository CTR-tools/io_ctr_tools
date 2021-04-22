bl_info = {
    "name": "Crash Team Racing level (LEV)",
    "author": "dcxdemo",
    "version": (1, 0, 0),
    "blender": (2, 90, 0),
    "location": "File > Import/Export",
    "description": "Import Crash Team Racing level mesh with vertex colors",
    "doc_url": "https://github.com/CTR-tools/CTR-tools",
    "support": 'COMMUNITY',
    "category": "Import-Export",
}

import bpy
from bpy.props import (
    CollectionProperty,
    StringProperty,
    BoolProperty,
    FloatProperty,
)
from bpy_extras.io_utils import (
    ImportHelper,
    ExportHelper,
    axis_conversion,
    orientation_helper,
)

from kaitaistruct import *
from .ctr_lev import *
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator

def add_mesh(collection, ob_name, coords, edges=[], faces=[], colors=[]):

    mesh = bpy.data.meshes.new(ob_name + "_Mesh")
    ob = bpy.data.objects.new(ob_name, mesh)

    mesh.from_pydata(coords, edges, faces)
    
    vcol_lay = mesh.vertex_colors.new()

    for i, col in enumerate(vcol_lay.data):
        col.color[0] = colors[i][0]
        col.color[1] = colors[i][1]
        col.color[2] = colors[i][2]
        col.color[3] = colors[i][3]

    ob.show_name = False

    mesh.update()    
    mesh.validate()
    collection.objects.link(ob)
    return ob

def push_coord(vertex, verts):
    p = vertex.coord
    verts.append((p.x / float(100), -p.z / float(100), p.y / float(100)))
    return

def push_color(vertex, colors):
    c = vertex.vcolor
    colors.append((c.r / float(255), c.g / float(255), c.b / float(255), c.a / float(255)))
    return

class ImportLEV(bpy.types.Operator, ImportHelper):
    bl_idname = "import_mesh.lev"
    bl_label = "Import LEV"
    bl_options = {'UNDO'}

    files: CollectionProperty(
        name="File Path",
        description="File path used for importing the LEV file",
        type=bpy.types.OperatorFileListElement,
    )

    lod_level: EnumProperty(
        name="LOD Level",
        description="Choose LOD level to import",
        items=(
            ('Low', "Low", "Description one"),
            ('Med', "Medium", "Description two"),
            ('Both', "Both", "Description three"),
        ),
        default='Med',
    )
    
    directory: StringProperty()

    filename_ext = ".lev"
    filter_glob: StringProperty(default="*.lev", options={'HIDDEN'})


    def execute(self, context):
        import os

        context.window.cursor_set('WAIT')

        paths = [
            os.path.join(self.directory, name.name)
            for name in self.files
        ]

        if not paths:
            paths.append(self.filepath)
        
        scenes = []
        
        for path in paths:
            scenes.append(CtrLev.from_file(path))


        if self.lod_level == 'Low' or self.lod_level == 'Both':
            lowCol = bpy.data.collections.new(os.path.splitext(os.path.basename(path))[0] + "_low");
            bpy.context.scene.collection.children.link(lowCol)
        
        if self.lod_level == 'Med' or self.lod_level == 'Both':
            medCol = bpy.data.collections.new(os.path.splitext(os.path.basename(path))[0] + "_med");
            bpy.context.scene.collection.children.link(medCol)
            
        if paths:
            for q in scenes[0].scene.quad_block_array:

                if self.lod_level == 'Low' or self.lod_level == 'Both':
                    verts = []
                    colors = []
                    faces = []
            
                    faces.append((len(verts)+1, len(verts)+0, len(verts)+2, len(verts)+3))
                    
                    for i in range(0, 4):
                        push_coord(scenes[0].scene.vertex_array[q.indices[i]], verts)

                    push_color(scenes[0].scene.vertex_array[q.indices[1]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[0]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[2]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[3]], colors)

                    add_mesh(lowCol, "piece_" + str(q.block_id), verts, [], faces, colors)

                if self.lod_level == 'Med' or self.lod_level == 'Both':
                    verts = []
                    colors = []
                    faces = []
            
                    faces.append((len(verts)+4, len(verts)+0, len(verts)+5, len(verts)+6))
                    faces.append((len(verts)+1, len(verts)+4, len(verts)+6, len(verts)+7))
                    faces.append((len(verts)+6, len(verts)+5, len(verts)+2, len(verts)+8))
                    faces.append((len(verts)+7, len(verts)+6, len(verts)+8, len(verts)+3))
                   
                    for i in range(0, 9):
                        push_coord(scenes[0].scene.vertex_array[q.indices[i]], verts)
                   
                    push_color(scenes[0].scene.vertex_array[q.indices[4]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[0]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[5]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[6]], colors)
                    
                    push_color(scenes[0].scene.vertex_array[q.indices[1]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[4]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[6]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[7]], colors)
                    
                    push_color(scenes[0].scene.vertex_array[q.indices[6]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[5]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[2]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[8]], colors)  
                    
                    push_color(scenes[0].scene.vertex_array[q.indices[7]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[6]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[8]], colors)
                    push_color(scenes[0].scene.vertex_array[q.indices[3]], colors)
                   
                    add_mesh(medCol, "piece_" + str(q.block_id), verts, [], faces, colors)

        context.window.cursor_set('DEFAULT')

        return {'FINISHED'}


def menu_func_import(self, context):
    self.layout.operator(ImportLEV.bl_idname, text="Crash Team Racing level (.lev)")


classes = (
    ImportLEV,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()