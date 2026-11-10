# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Dds(KaitaiStruct):

    class D3d10ResourceDimensions(IntEnum):
        d3d10_resource_dimension_unknown = 0
        d3d10_resource_dimension_buffer = 1
        d3d10_resource_dimension_texture1d = 2
        d3d10_resource_dimension_texture2d = 3
        d3d10_resource_dimension_texture3d = 4

    class DxgiFormats(IntEnum):
        dxgi_format_unknown = 0
        dxgi_format_r32g32b32a32_typeless = 1
        dxgi_format_r32g32b32a32_float = 2
        dxgi_format_r32g32b32a32_uint = 3
        dxgi_format_r32g32b32a32_sint = 5
        dxgi_format_r32g32b32_typeless = 6
        dxgi_format_r32g32b32_float = 7
        dxgi_format_r32g32b32_uint = 8
        dxgi_format_r32g32b32_sint = 9
        dxgi_format_r16g16b16a16_typeless = 10
        dxgi_format_r16g16b16a16_float = 11
        dxgi_format_r16g16b16a16_unorm = 12
        dxgi_format_r16g16b16a16_uint = 13
        dxgi_format_r16g16b16a16_snorm = 14
        dxgi_format_r16g16b16a16_sint = 15
        dxgi_format_r32g32_typeless = 16
        dxgi_format_r32g32_float = 17
        dxgi_format_r32g32_uint = 18
        dxgi_format_r32g32_sint = 19
        dxgi_format_r32g8x24_typeless = 20
        dxgi_format_d32_float_s8x24_uint = 21
        dxgi_format_r32_float_x8x24_typeless = 22
        dxgi_format_x32_typeless_g8x24_uint = 23
        dxgi_format_r10g10b10a2_typeless = 24
        dxgi_format_r10g10b10a2_unorm = 25
        dxgi_format_r10g10b10a2_uint = 26
        dxgi_format_r11g11b10_float = 27
        dxgi_format_r8g8b8a8_typeless = 28
        dxgi_format_r8g8b8a8_unorm = 29
        dxgi_format_r8g8b8a8_unorm_srgb = 30
        dxgi_format_r8g8b8a8_uint = 31
        dxgi_format_r8g8b8a8_snorm = 32
        dxgi_format_r8g8b8a8_sint = 33
        dxgi_format_r16g16_typeless = 34
        dxgi_format_r16g16_float = 35
        dxgi_format_r16g16_unorm = 36
        dxgi_format_r16g16_uint = 37
        dxgi_format_r16g16_snorm = 38
        dxgi_format_r16g16_sint = 39
        dxgi_format_r32_typeless = 40
        dxgi_format_d32_float = 41
        dxgi_format_r32_float = 42
        dxgi_format_r32_uint = 43
        dxgi_format_r32_sint = 44
        dxgi_format_r24g8_typeless = 45
        dxgi_format_d24_unorm_s8_uint = 46
        dxgi_format_r24_unorm_x8_typeless = 47
        dxgi_format_x24_typeless_g8_uint = 48
        dxgi_format_r8g8_typeless = 49
        dxgi_format_r8g8_unorm = 50
        dxgi_format_r8g8_uint = 51
        dxgi_format_r8g8_snorm = 52
        dxgi_format_r8g8_sint = 53
        dxgi_format_r16_typeless = 54
        dxgi_format_r16_float = 55
        dxgi_format_d16_unorm = 56
        dxgi_format_r16_unorm = 57
        dxgi_format_r16_uint = 58
        dxgi_format_r16_snorm = 59
        dxgi_format_r16_sint = 60
        dxgi_format_r8_typeless = 61
        dxgi_format_r8_unorm = 62
        dxgi_format_r8_uint = 63
        dxgi_format_r8_snorm = 64
        dxgi_format_r8_sint = 65
        dxgi_format_a8_unorm = 66
        dxgi_format_r1_unorm = 67
        dxgi_format_r9g9b9e5_sharedexp = 68
        dxgi_format_r8g8_b8g8_unorm = 69
        dxgi_format_g8r8_g8b8_unorm = 70
        dxgi_format_bc1_typeless = 71
        dxgi_format_bc1_unorm = 72
        dxgi_format_bc1_unorm_srgb = 73
        dxgi_format_bc2_typeless = 74
        dxgi_format_bc2_unorm = 75
        dxgi_format_bc2_unorm_srgb = 76
        dxgi_format_bc3_typeless = 77
        dxgi_format_bc3_unorm = 78
        dxgi_format_bc3_unorm_srgb = 79
        dxgi_format_bc4_typeless = 80
        dxgi_format_bc4_unorm = 81
        dxgi_format_bc4_snorm = 82
        dxgi_format_bc5_typeless = 83
        dxgi_format_bc5_unorm = 84
        dxgi_format_bc5_snorm = 85
        dxgi_format_b5g6r5_unorm = 86
        dxgi_format_b5g5r5a1_unorm = 87
        dxgi_format_b8g8r8a8_unorm = 88
        dxgi_format_b8g8r8x8_unorm = 89
        dxgi_format_r10g10b10_xr_bias_a2_unorm = 90
        dxgi_format_b8g8r8a8_typeless = 91
        dxgi_format_b8g8r8a8_unorm_srgb = 92
        dxgi_format_b8g8r8x8_typeless = 93
        dxgi_format_b8g8r8x8_unorm_srgb = 94
        dxgi_format_bc6h_typeless = 95
        dxgi_format_bc6h_uf16 = 96
        dxgi_format_bc6h_sf16 = 97
        dxgi_format_bc7_typeless = 98
        dxgi_format_bc7_unorm = 99
        dxgi_format_bc7_unorm_srgb = 100
        dxgi_format_ayuv = 101
        dxgi_format_y410 = 102
        dxgi_format_y416 = 103
        dxgi_format_nv12 = 104
        dxgi_format_p010 = 105
        dxgi_format_p016 = 106
        dxgi_format_420_opaque = 107
        dxgi_format_yuy2 = 108
        dxgi_format_y210 = 109
        dxgi_format_y216 = 110
        dxgi_format_nv11 = 111
        dxgi_format_ai44 = 112
        dxgi_format_ia44 = 113
        dxgi_format_p8 = 114
        dxgi_format_a8p8 = 115
        dxgi_format_b4g4r4a4_unorm = 116
        dxgi_format_p208 = 117
        dxgi_format_v208 = 118
        dxgi_format_v408 = 119
        dxgi_format_sampler_feedback_min_mip_opaque = 120
        dxgi_format_sampler_feedback_mip_region_used_opaque = 121
        dxgi_format_force_uint = 122
    SEQ_FIELDS = ["magic", "dds_header", "dds_header_dxt10"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Dds, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x44\x44\x53\x20":
            raise kaitaistruct.ValidationNotEqualError(b"\x44\x44\x53\x20", self.magic, self._io, u"/seq/0")
        self._debug['dds_header']['start'] = self._io.pos()
        self.dds_header = Dds.DdsHeader(self._io, self, self._root)
        self._debug['dds_header']['end'] = self._io.pos()
        if self.dds_header.pixel_format.fourcc == u"DX10":
            pass
            self._debug['dds_header_dxt10']['start'] = self._io.pos()
            self.dds_header_dxt10 = Dds.DdsHeaderDxt10(self._io, self, self._root)
            self._debug['dds_header_dxt10']['end'] = self._io.pos()



    def _fetch_instances(self):
        pass
        self.dds_header._fetch_instances()
        if self.dds_header.pixel_format.fourcc == u"DX10":
            pass
            self.dds_header_dxt10._fetch_instances()


    class DdsHeader(KaitaiStruct):
        SEQ_FIELDS = ["size", "flags", "height", "width", "pitch_or_linear_size", "depth", "mip_map_count", "reserved", "pixel_format", "caps", "caps2", "caps3", "caps4", "reserved2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Dds.DdsHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            if not self.size == 124:
                raise kaitaistruct.ValidationNotEqualError(124, self.size, self._io, u"/types/dds_header/seq/0")
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u4le()
            self._debug['height']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u4le()
            self._debug['width']['end'] = self._io.pos()
            self._debug['pitch_or_linear_size']['start'] = self._io.pos()
            self.pitch_or_linear_size = self._io.read_u4le()
            self._debug['pitch_or_linear_size']['end'] = self._io.pos()
            self._debug['depth']['start'] = self._io.pos()
            self.depth = self._io.read_u4le()
            self._debug['depth']['end'] = self._io.pos()
            self._debug['mip_map_count']['start'] = self._io.pos()
            self.mip_map_count = self._io.read_u4le()
            self._debug['mip_map_count']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(44)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['pixel_format']['start'] = self._io.pos()
            self.pixel_format = Dds.PixelFormat(self._io, self, self._root)
            self._debug['pixel_format']['end'] = self._io.pos()
            self._debug['caps']['start'] = self._io.pos()
            self.caps = self._io.read_u4le()
            self._debug['caps']['end'] = self._io.pos()
            self._debug['caps2']['start'] = self._io.pos()
            self.caps2 = self._io.read_u4le()
            self._debug['caps2']['end'] = self._io.pos()
            self._debug['caps3']['start'] = self._io.pos()
            self.caps3 = self._io.read_u4le()
            self._debug['caps3']['end'] = self._io.pos()
            self._debug['caps4']['start'] = self._io.pos()
            self.caps4 = self._io.read_u4le()
            self._debug['caps4']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bytes(4)
            self._debug['reserved2']['end'] = self._io.pos()
            if not self.reserved2 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.reserved2, self._io, u"/types/dds_header/seq/13")


        def _fetch_instances(self):
            pass
            self.pixel_format._fetch_instances()


    class DdsHeaderDxt10(KaitaiStruct):
        SEQ_FIELDS = ["dxgi_format", "resource_dimension", "misc_flag", "array_size", "misc_flags2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Dds.DdsHeaderDxt10, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['dxgi_format']['start'] = self._io.pos()
            self.dxgi_format = KaitaiStream.resolve_enum(Dds.DxgiFormats, self._io.read_u4le())
            self._debug['dxgi_format']['end'] = self._io.pos()
            self._debug['resource_dimension']['start'] = self._io.pos()
            self.resource_dimension = KaitaiStream.resolve_enum(Dds.D3d10ResourceDimensions, self._io.read_u4le())
            self._debug['resource_dimension']['end'] = self._io.pos()
            self._debug['misc_flag']['start'] = self._io.pos()
            self.misc_flag = self._io.read_u4le()
            self._debug['misc_flag']['end'] = self._io.pos()
            self._debug['array_size']['start'] = self._io.pos()
            self.array_size = self._io.read_u4le()
            self._debug['array_size']['end'] = self._io.pos()
            self._debug['misc_flags2']['start'] = self._io.pos()
            self.misc_flags2 = self._io.read_u4le()
            self._debug['misc_flags2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PixelFormat(KaitaiStruct):
        SEQ_FIELDS = ["size", "flags", "fourcc", "rgb_bit_count", "red_bit_mask", "green_bit_mask", "blue_bit_mask", "alpha_bit_mask"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Dds.PixelFormat, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            if not self.size == 32:
                raise kaitaistruct.ValidationNotEqualError(32, self.size, self._io, u"/types/pixel_format/seq/0")
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['fourcc']['start'] = self._io.pos()
            self.fourcc = (self._io.read_bytes(4)).decode(u"ASCII")
            self._debug['fourcc']['end'] = self._io.pos()
            self._debug['rgb_bit_count']['start'] = self._io.pos()
            self.rgb_bit_count = self._io.read_u4le()
            self._debug['rgb_bit_count']['end'] = self._io.pos()
            self._debug['red_bit_mask']['start'] = self._io.pos()
            self.red_bit_mask = self._io.read_u4le()
            self._debug['red_bit_mask']['end'] = self._io.pos()
            self._debug['green_bit_mask']['start'] = self._io.pos()
            self.green_bit_mask = self._io.read_u4le()
            self._debug['green_bit_mask']['end'] = self._io.pos()
            self._debug['blue_bit_mask']['start'] = self._io.pos()
            self.blue_bit_mask = self._io.read_u4le()
            self._debug['blue_bit_mask']['end'] = self._io.pos()
            self._debug['alpha_bit_mask']['start'] = self._io.pos()
            self.alpha_bit_mask = self._io.read_u4le()
            self._debug['alpha_bit_mask']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



