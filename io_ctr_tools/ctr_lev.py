# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class CtrLev(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.data_size = self._io.read_u4le()
        self._raw_data = self._io.read_bytes(self.data_size)
        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
        self.data = self._root.Lev(_io__raw_data, self, self._root)
        self.ptr_map_size = self._io.read_u4le()
        self.ptr_map = [None] * (self.ptr_map_size // 4)
        for i in range(self.ptr_map_size // 4):
            self.ptr_map[i] = self._io.read_u4le()


    class VisDataBranch(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.axis_x = self._io.read_u2le()
            self.axis_y = self._io.read_u2le()
            self.axis_z = self._io.read_u2le()
            self.unk = self._io.read_u2le()
            self.left_child_id = self._io.read_u2le()
            self.right_child_id = self._io.read_u2le()
            self.unk0 = self._io.read_u4le()


    class BuildInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ptr_build_start = self._io.read_u4le()
            self.ptr_build_end = self._io.read_u4le()
            self.ptr_build_type = self._io.read_u4le()

        @property
        def build_start(self):
            if hasattr(self, '_m_build_start'):
                return self._m_build_start if hasattr(self, '_m_build_start') else None

            _pos = self._io.pos()
            self._io.seek(self.ptr_build_start)
            self._m_build_start = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self._io.seek(_pos)
            return self._m_build_start if hasattr(self, '_m_build_start') else None

        @property
        def build_end(self):
            if hasattr(self, '_m_build_end'):
                return self._m_build_end if hasattr(self, '_m_build_end') else None

            _pos = self._io.pos()
            self._io.seek(self.ptr_build_end)
            self._m_build_end = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self._io.seek(_pos)
            return self._m_build_end if hasattr(self, '_m_build_end') else None

        @property
        def build_type(self):
            if hasattr(self, '_m_build_type'):
                return self._m_build_type if hasattr(self, '_m_build_type') else None

            _pos = self._io.pos()
            self._io.seek(self.ptr_build_type)
            self._m_build_type = (self._io.read_bytes_term(0, False, True, True)).decode(u"ascii")
            self._io.seek(_pos)
            return self._m_build_type if hasattr(self, '_m_build_type') else None


    class Vertex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.coord = self._root.Vector3s(self._io, self, self._root)
            self.nil = self._io.read_u2le()
            self.colorz = self._root.Color(self._io, self, self._root)
            self.color_morph = self._root.Color(self._io, self, self._root)


    class Vector3s(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s2le()
            self.y = self._io.read_s2le()
            self.z = self._io.read_s2le()


    class SceneHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ptr_mesh_info = self._io.read_u4le()
            self.ptr_skybox = self._io.read_u4le()
            self.ptr_tex_array = self._io.read_u4le()
            self.num_instances = self._io.read_u4le()
            self.ptr_instances = self._io.read_u4le()
            self.num_models = self._io.read_u4le()
            self.ptr_models_ptr = self._io.read_u4le()
            self.unk_ptr3 = self._io.read_u4le()
            self.unk_ptr4 = self._io.read_u4le()
            self.ptr_instances_ptr_array = self._io.read_u4le()
            self.unk_ptr5 = self._io.read_u4le()
            self.null1 = self._io.read_u4le()
            self.null2 = self._io.read_u4le()
            self.cnt_water = self._io.read_u4le()
            self.ptr_water = self._io.read_u4le()
            self.ptr_named_tex = self._io.read_u4le()
            self.ptr_named_tex_array = self._io.read_u4le()
            self.ptr_restart_main = self._io.read_u4le()
            self.some_data = [None] * (3)
            for i in range(3):
                self.some_data[i] = self._root.Somedata(self._io, self, self._root)

            self.start_grid = [None] * (8)
            for i in range(8):
                self.start_grid[i] = self._root.Posang(self._io, self, self._root)

            self.unkptr1 = self._io.read_u4le()
            self.unkptr2 = self._io.read_u4le()
            self.ptr_low_tex_array = self._io.read_u4le()
            self.back_color = self._root.Color(self._io, self, self._root)
            self.bg_mode = self._io.read_u4le()
            self.build = self._root.BuildInfo(self._io, self, self._root)
            self.skip = self._io.read_bytes(68)
            self.cnt_trial_data = self._io.read_u4le()
            self.ptr_trial_data = self._io.read_u4le()
            self.cnt_spawn_arrays2 = self._io.read_u4le()
            self.ptr_spawn_arrays2 = self._io.read_u4le()
            self.cnt_spawn_arrays = self._io.read_u4le()
            self.ptr_spawn_arrays = self._io.read_u4le()
            self.cnt_restart_pts = self._io.read_u4le()
            self.ptr_restart_pts = self._io.read_u4le()
            self.skip2 = self._io.read_bytes(16)
            self.bg_color = [None] * (4)
            for i in range(4):
                self.bg_color[i] = self._root.Color(self._io, self, self._root)

            self.skip2_unkptr = self._io.read_u4le()
            self.cnt_vcanim = self._io.read_u4le()
            self.ptr_vcanim = self._io.read_u4le()
            self.skip2_3 = self._io.read_bytes(12)
            self.ptr_ai_nav = self._io.read_u4le()
            self.skip3 = self._io.read_bytes(36)


    class NavFrame(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.point = self._root.Posang(self._io, self, self._root)
            self.data = self._io.read_bytes(8)


    class Posang(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.position = self._root.Vector3s(self._io, self, self._root)
            self.angle = self._root.Vector3s(self._io, self, self._root)


    class Vector4s(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_s2le()
            self.y = self._io.read_s2le()
            self.z = self._io.read_s2le()
            self.w = self._io.read_s2le()


    class AiFrameHeader(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk1 = self._io.read_u2le()
            self.num_frames = self._io.read_u2le()
            self.skip = self._io.read_bytes(72)


    class QuadBlock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.indices = [None] * (9)
            for i in range(9):
                self.indices[i] = self._io.read_u2le()

            self.quad_flags = self._io.read_u2le()
            self.draw_order_low = self._io.read_u1()
            self.f1 = self._io.read_u1()
            self.f2 = self._io.read_u1()
            self.f3 = self._io.read_u1()
            self.draw_order_high = self._io.read_bytes(4)
            self.ptr_texture_mid = [None] * (4)
            for i in range(4):
                self.ptr_texture_mid[i] = self._io.read_u4le()

            self.bbox = self._root.BoundingBox(self._io, self, self._root)
            self.terrain_type = self._io.read_u1()
            self.weather_intensity = self._io.read_u1()
            self.weather_type = self._io.read_u1()
            self.terrain_flag_unknown = self._io.read_u1()
            self.block_id = self._io.read_u2le()
            self.progress_tracker = self._io.read_u1()
            self.midflag_unk = self._io.read_u1()
            self.ptr_texture_low = self._io.read_u4le()
            self.ptr_texture_high = self._io.read_u4le()
            self.unk_col_array = [None] * (10)
            for i in range(10):
                self.unk_col_array[i] = self._io.read_u2le()


        @property
        def midtex1(self):
            if hasattr(self, '_m_midtex1'):
                return self._m_midtex1 if hasattr(self, '_m_midtex1') else None

            _pos = self._io.pos()
            self._io.seek(self.ptr_texture_mid[0])
            self._m_midtex1 = self._root.CtrTex(self._io, self, self._root)
            self._io.seek(_pos)
            return self._m_midtex1 if hasattr(self, '_m_midtex1') else None

        @property
        def midtex2(self):
            if hasattr(self, '_m_midtex2'):
                return self._m_midtex2 if hasattr(self, '_m_midtex2') else None

            _pos = self._io.pos()
            self._io.seek(self.ptr_texture_mid[1])
            self._m_midtex2 = self._root.CtrTex(self._io, self, self._root)
            self._io.seek(_pos)
            return self._m_midtex2 if hasattr(self, '_m_midtex2') else None

        @property
        def midtex3(self):
            if hasattr(self, '_m_midtex3'):
                return self._m_midtex3 if hasattr(self, '_m_midtex3') else None

            _pos = self._io.pos()
            self._io.seek(self.ptr_texture_mid[2])
            self._m_midtex3 = self._root.CtrTex(self._io, self, self._root)
            self._io.seek(_pos)
            return self._m_midtex3 if hasattr(self, '_m_midtex3') else None

        @property
        def midtex4(self):
            if hasattr(self, '_m_midtex4'):
                return self._m_midtex4 if hasattr(self, '_m_midtex4') else None

            _pos = self._io.pos()
            self._io.seek(self.ptr_texture_mid[3])
            self._m_midtex4 = self._root.CtrTex(self._io, self, self._root)
            self._io.seek(_pos)
            return self._m_midtex4 if hasattr(self, '_m_midtex4') else None


    class Vector3u(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_u2le()
            self.y = self._io.read_u2le()
            self.z = self._io.read_u2le()


    class Lev(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = self._root.SceneHeader(self._io, self, self._root)
            if self.header.ptr_restart_main != 0:
                self.restart_main = self._root.Posang(self._io, self, self._root)

            self.restart_pts = [None] * (self.header.cnt_restart_pts)
            for i in range(self.header.cnt_restart_pts):
                self.restart_pts[i] = self._root.Posang(self._io, self, self._root)

            self.instances = [None] * (self.header.num_instances)
            for i in range(self.header.num_instances):
                self.instances[i] = self._root.Instance(self._io, self, self._root)

            self.model_pointers = [None] * (self.header.num_models)
            for i in range(self.header.num_models):
                self.model_pointers[i] = self._io.read_u4le()

            self.mesh_info_header = self._root.MeshInfo(self._io, self, self._root)
            self.quad_block_array = [None] * (self.mesh_info_header.cnt_quad_block)
            for i in range(self.mesh_info_header.cnt_quad_block):
                self.quad_block_array[i] = self._root.QuadBlock(self._io, self, self._root)

            self.vertex_array = [None] * (self.mesh_info_header.vertexnum)
            for i in range(self.mesh_info_header.vertexnum):
                self.vertex_array[i] = self._root.Vertex(self._io, self, self._root)


        @property
        def water_data(self):
            if hasattr(self, '_m_water_data'):
                return self._m_water_data if hasattr(self, '_m_water_data') else None

            _pos = self._io.pos()
            self._io.seek(self.header.ptr_water)
            self._m_water_data = [None] * (self.header.cnt_water)
            for i in range(self.header.cnt_water):
                self._m_water_data[i] = self._root.WaterPacket(self._io, self, self._root)

            self._io.seek(_pos)
            return self._m_water_data if hasattr(self, '_m_water_data') else None

        @property
        def vis_data_array(self):
            if hasattr(self, '_m_vis_data_array'):
                return self._m_vis_data_array if hasattr(self, '_m_vis_data_array') else None

            _pos = self._io.pos()
            self._io.seek(self.mesh_info_header.ptr_vis_data_array)
            self._m_vis_data_array = [None] * (self.mesh_info_header.cnt_vis_data)
            for i in range(self.mesh_info_header.cnt_vis_data):
                self._m_vis_data_array[i] = self._root.VisData(self._io, self, self._root)

            self._io.seek(_pos)
            return self._m_vis_data_array if hasattr(self, '_m_vis_data_array') else None

        @property
        def ai_nav(self):
            if hasattr(self, '_m_ai_nav'):
                return self._m_ai_nav if hasattr(self, '_m_ai_nav') else None

            _pos = self._io.pos()
            self._io.seek(self.header.ptr_ai_nav)
            self._m_ai_nav = self._root.AiPaths(self._io, self, self._root)
            self._io.seek(_pos)
            return self._m_ai_nav if hasattr(self, '_m_ai_nav') else None

        @property
        def unk_struct1_array(self):
            if hasattr(self, '_m_unk_struct1_array'):
                return self._m_unk_struct1_array if hasattr(self, '_m_unk_struct1_array') else None

            _pos = self._io.pos()
            self._io.seek(self.header.ptr_tex_array)
            self._m_unk_struct1_array = self._root.UnkStruct(self._io, self, self._root)
            self._io.seek(_pos)
            return self._m_unk_struct1_array if hasattr(self, '_m_unk_struct1_array') else None

        @property
        def skybox(self):
            if hasattr(self, '_m_skybox'):
                return self._m_skybox if hasattr(self, '_m_skybox') else None

            if self.header.ptr_skybox != 0:
                _pos = self._io.pos()
                self._io.seek(self.header.ptr_skybox)
                self._m_skybox = self._root.Skybox(self._io, self, self._root)
                self._io.seek(_pos)

            return self._m_skybox if hasattr(self, '_m_skybox') else None

        @property
        def trial(self):
            if hasattr(self, '_m_trial'):
                return self._m_trial if hasattr(self, '_m_trial') else None

            if self.header.cnt_trial_data > 0:
                _pos = self._io.pos()
                self._io.seek(self.header.ptr_trial_data)
                self._m_trial = self._root.TrialData(self._io, self, self._root)
                self._io.seek(_pos)

            return self._m_trial if hasattr(self, '_m_trial') else None


    class Instance(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (self._io.read_bytes(16)).decode(u"ascii")
            self.model_ptr = self._io.read_u4le()
            self.scale = self._root.Vector3s(self._io, self, self._root)
            self.scale1 = self._io.read_u2le()
            self.null1 = self._io.read_u4le()
            self.unk1 = self._io.read_u4le()
            self.skip = self._io.read_bytes(12)
            self.position = self._root.Vector3s(self._io, self, self._root)
            self.angle = self._root.Vector3s(self._io, self, self._root)
            self.event = self._io.read_u4le()


    class Color(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.r = self._io.read_u1()
            self.g = self._io.read_u1()
            self.b = self._io.read_u1()
            self.a = self._io.read_u1()


    class AiPath(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.header = self._root.AiFrameHeader(self._io, self, self._root)
            self.start = self._root.NavFrame(self._io, self, self._root)
            self.frames = [None] * (self.header.num_frames)
            for i in range(self.header.num_frames):
                self.frames[i] = self._root.NavFrame(self._io, self, self._root)



    class TextureLayout(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.uv1 = self._root.Vector2b(self._io, self, self._root)
            self.pal_x = self._io.read_bits_int(6)
            self.pal_y = self._io.read_bits_int(10)
            self._io.align_to_byte()
            self.uv2 = self._root.Vector2b(self._io, self, self._root)
            self.page_x = self._io.read_bits_int(4)
            self.page_y = self._io.read_bits_int(12)
            self._io.align_to_byte()
            self.uv3 = self._root.Vector2b(self._io, self, self._root)
            self.uv4 = self._root.Vector2b(self._io, self, self._root)


    class CtrTex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.mid_tex = [None] * (3)
            for i in range(3):
                self.mid_tex[i] = self._root.TextureLayout(self._io, self, self._root)

            self.ptr_hi = self._io.read_u4le()


    class UnkStruct(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.self_ptr = self._io.read_u4le()
            self.cnt_entries = self._io.read_u4le()
            self.some_ptr2 = self._io.read_u4le()
            self.nil = self._io.read_u4le()
            self.some_ptr3 = self._io.read_u4le()
            self.entries = [None] * (self.cnt_entries)
            for i in range(self.cnt_entries):
                self.entries[i] = self._root.UnkEntry(self._io, self, self._root)



    class WaterPacket(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ptr_vertex = self._io.read_u4le()
            self.ptr_anim = self._io.read_u4le()


    class Somedata(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.s1 = self._io.read_u2le()
            self.s2 = self._io.read_u2le()
            self.s3 = self._io.read_u4le()
            self.s4 = self._io.read_u4le()


    class UnkEntry(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"ascii")
            self.entry_type = self._io.read_u4le()
            if self.entry_type != 134:
                self.layout = self._root.TextureLayout(self._io, self, self._root)



    class SkyboxVertex(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.position = self._root.Vector4s(self._io, self, self._root)
            self.colorz = self._root.Color(self._io, self, self._root)


    class VisData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.flag = self._io.read_u2le()
            self.id = self._io.read_u2le()
            self.bbox_min = self._root.Vector3s(self._io, self, self._root)
            self.bbox_max = self._root.Vector3s(self._io, self, self._root)
            _on = (self.flag & 1)
            if _on == 0:
                self.data = self._root.VisDataBranch(self._io, self, self._root)
            elif _on == 1:
                self.data = self._root.VisDataLeaf(self._io, self, self._root)


    class AiPaths(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.ptr = [None] * (3)
            for i in range(3):
                self.ptr[i] = self._io.read_u4le()

            if  ((self.ptr[0] != 0) and (self.ptr[1] != 0) and (self.ptr[2] != 0)) :
                self.paths = [None] * (3)
                for i in range(3):
                    self.paths[i] = self._root.AiPath(self._io, self, self._root)




    class VisDataLeaf(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unk = self._io.read_u4le()
            self.ptr_some_data = self._io.read_u4le()
            self.num_quads = self._io.read_u4le()
            self.ptr_quads = self._io.read_u4le()


    class BoundingBox(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.min = self._root.Vector3s(self._io, self, self._root)
            self.max = self._root.Vector3s(self._io, self, self._root)


    class Vector2b(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x = self._io.read_u1()
            self.y = self._io.read_u1()


    class TrialData(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cnt_pointers = self._io.read_u4le()
            self.ptr_map = self._io.read_u4le()
            self.ptr_null = self._io.read_u4le()
            self.ptr_post_cam = self._io.read_u4le()
            self.ptr_intro_cam = self._io.read_u4le()
            self.ptr_tropy_ghost = self._io.read_u4le()
            self.ptr_oxide_ghost = self._io.read_u4le()


    class MeshInfo(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cnt_quad_block = self._io.read_u4le()
            self.vertexnum = self._io.read_u4le()
            self.unk1 = self._io.read_u4le()
            self.ptr_quadblock_array = self._io.read_u4le()
            self.ptr_vert_array = self._io.read_u4le()
            self.unk2 = self._io.read_u4le()
            self.ptr_vis_data_array = self._io.read_u4le()
            self.cnt_vis_data = self._io.read_u4le()


    class Skybox(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_vertex = self._io.read_u4le()
            self.ptr_vertex = self._io.read_u4le()
            self.num8 = [None] * (8)
            for i in range(8):
                self.num8[i] = self._io.read_u2le()

            self.ptr8 = [None] * (8)
            for i in range(8):
                self.ptr8[i] = self._io.read_u4le()

            self.vertex_array = [None] * (self.num_vertex)
            for i in range(self.num_vertex):
                self.vertex_array[i] = self._root.SkyboxVertex(self._io, self, self._root)




