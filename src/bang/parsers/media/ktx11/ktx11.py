# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ktx11(KaitaiStruct):
    """
    .. seealso::
       Source - https://www.khronos.org/registry/KTX/specs/1.0/ktxspec_v1.html
    """

    class Endian(IntEnum):
        be = 16909060
        le = 67305985

    class Format(IntEnum):
        rgb = 6407
        rgba = 6408
        luminance = 6409
        luminance_alpha = 6410
        bgr = 32993
        bgra = 32994
        rgb_s3tc = 33696
        rgb4_s3tc = 33697
        rgba_s3tc = 33698
        rgba4_s3tc = 33699
        rgba_dxt5_s3tc = 33700
        rgba4_dxt5_s3tc = 33701
        compressed_rgb_s3tc_dxt1_ext = 33776
        compressed_rgba_s3tc_dxt1_ext = 33777
        compressed_rgba_s3tc_dxt3_ext = 33778
        compressed_rgba_s3tc_dxt5_ext = 33779
        palette4_rgb8_eos = 35728
        palette4_rgba8_eos = 35729
        palette4_r5_g6_b5_eos = 35730
        palette4_rgba4_eos = 35731
        palette4_rgb5_a1_eos = 35732
        palette8_rgb8_eos = 35733
        palette8_rgba8_eos = 35734
        palette8_r5_g6_b5_eos = 35735
        palette8_rgba4_eos = 35736
        palette8_rgb5_a1_eos = 35737
        etc1_rgb8_oes = 36196
        compressed_r11_eac = 37488
        compressed_signed_r11_eac = 37489
        compressed_rg11_eac = 37490
        compressed_signed_rg11_eac = 37491
        compressed_rgb8_etc2 = 37492
        compressed_srgb8_etc2 = 37493
        compressed_rgb8_punchthrough_alpha1_etc2 = 37494
        compressed_srgb8_punchthrough_alpha1_etc2 = 37495
        compressed_rgba2_etc2_eac = 37496
        compressed_srgb8_alpha8_etc2_eac = 37497
        compressed_rgba_astc_4x4_khr = 37808
        compressed_rgba_astc_5x4_khr = 37809
        compressed_rgba_astc_5x5_khr = 37810
        compressed_rgba_astc_6x5_khr = 37811
        compressed_rgba_astc_6x6_khr = 37812
        compressed_rgba_astc_8x5_khr = 37813
        compressed_rgba_astc_8x6_khr = 37814
        compressed_rgba_astc_8x8_khr = 37815
        compressed_rgba_astc_10x5_khr = 37816
        compressed_rgba_astc_10x6_khr = 37817
        compressed_rgba_astc_10x8_khr = 37818
        compressed_rgba_astc_10x10_khr = 37819
        compressed_rgba_astc_12x10_khr = 37820
        compressed_rgba_astc_12x12_khr = 37821
        compressed_srgb8_alpha8_astc_4x4_khr = 37840
        compressed_srgb8_alpha8_astc_5x4_khr = 37841
        compressed_srgb8_alpha8_astc_5x5_khr = 37842
        compressed_srgb8_alpha8_astc_6x5_khr = 37843
        compressed_srgb8_alpha8_astc_6x6_khr = 37844
        compressed_srgb8_alpha8_astc_8x5_khr = 37845
        compressed_srgb8_alpha8_astc_8x6_khr = 37846
        compressed_srgb8_alpha8_astc_8x8_khr = 37847
        compressed_srgb8_alpha8_astc_10x5_khr = 37848
        compressed_srgb8_alpha8_astc_10x6_khr = 37849
        compressed_srgb8_alpha8_astc_10x8_khr = 37850
        compressed_srgb8_alpha8_astc_10x10_khr = 37851
        compressed_srgb8_alpha8_astc_12x10_khr = 37852
        compressed_srgb8_alpha8_astc_12x12_khr = 37853
    SEQ_FIELDS = ["magic", "endian", "endian_ktx"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Ktx11, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(12)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\xAB\x4B\x54\x58\x20\x31\x31\xBB\x0D\x0A\x1A\x0A":
            raise kaitaistruct.ValidationNotEqualError(b"\xAB\x4B\x54\x58\x20\x31\x31\xBB\x0D\x0A\x1A\x0A", self.magic, self._io, u"/seq/0")
        self._debug['endian']['start'] = self._io.pos()
        self.endian = KaitaiStream.resolve_enum(Ktx11.Endian, self._io.read_u4le())
        self._debug['endian']['end'] = self._io.pos()
        self._debug['endian_ktx']['start'] = self._io.pos()
        self.endian_ktx = Ktx11.Ktx(self._io, self, self._root)
        self._debug['endian_ktx']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.endian_ktx._fetch_instances()

    class Ktx(KaitaiStruct):
        SEQ_FIELDS = ["type", "type_size", "format", "internal_format", "base_internal_format", "pixel_width", "pixel_height", "pixel_depth", "array_elements_num", "num_faces", "mipmap_levels_num", "len_key_value_data", "key_value_data", "mipmap_levels"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ktx11.Ktx, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            _on = self._root.endian
            if _on == Ktx11.Endian.le:
                pass
                self._is_le = True
            elif _on == Ktx11.Endian.be:
                pass
                self._is_le = False
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/ktx")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u4le()
            self._debug['type']['end'] = self._io.pos()
            self._debug['type_size']['start'] = self._io.pos()
            self.type_size = self._io.read_u4le()
            self._debug['type_size']['end'] = self._io.pos()
            self._debug['format']['start'] = self._io.pos()
            self.format = self._io.read_u4le()
            self._debug['format']['end'] = self._io.pos()
            self._debug['internal_format']['start'] = self._io.pos()
            self.internal_format = KaitaiStream.resolve_enum(Ktx11.Format, self._io.read_u4le())
            self._debug['internal_format']['end'] = self._io.pos()
            self._debug['base_internal_format']['start'] = self._io.pos()
            self.base_internal_format = self._io.read_u4le()
            self._debug['base_internal_format']['end'] = self._io.pos()
            self._debug['pixel_width']['start'] = self._io.pos()
            self.pixel_width = self._io.read_u4le()
            self._debug['pixel_width']['end'] = self._io.pos()
            self._debug['pixel_height']['start'] = self._io.pos()
            self.pixel_height = self._io.read_u4le()
            self._debug['pixel_height']['end'] = self._io.pos()
            self._debug['pixel_depth']['start'] = self._io.pos()
            self.pixel_depth = self._io.read_u4le()
            self._debug['pixel_depth']['end'] = self._io.pos()
            self._debug['array_elements_num']['start'] = self._io.pos()
            self.array_elements_num = self._io.read_u4le()
            self._debug['array_elements_num']['end'] = self._io.pos()
            self._debug['num_faces']['start'] = self._io.pos()
            self.num_faces = self._io.read_u4le()
            self._debug['num_faces']['end'] = self._io.pos()
            self._debug['mipmap_levels_num']['start'] = self._io.pos()
            self.mipmap_levels_num = self._io.read_u4le()
            self._debug['mipmap_levels_num']['end'] = self._io.pos()
            self._debug['len_key_value_data']['start'] = self._io.pos()
            self.len_key_value_data = self._io.read_u4le()
            self._debug['len_key_value_data']['end'] = self._io.pos()
            self._debug['key_value_data']['start'] = self._io.pos()
            self._raw_key_value_data = self._io.read_bytes(self.len_key_value_data)
            _io__raw_key_value_data = KaitaiStream(BytesIO(self._raw_key_value_data))
            self.key_value_data = Ktx11.Ktx.KeyValueData(_io__raw_key_value_data, self, self._root, self._is_le)
            self._debug['key_value_data']['end'] = self._io.pos()
            self._debug['mipmap_levels']['start'] = self._io.pos()
            self._debug['mipmap_levels']['arr'] = []
            self.mipmap_levels = []
            for i in range(self.num_mipmap_levels):
                self._debug['mipmap_levels']['arr'].append({'start': self._io.pos()})
                self.mipmap_levels.append(Ktx11.Ktx.MipmapLevel(self._io, self, self._root, self._is_le))
                self._debug['mipmap_levels']['arr'][i]['end'] = self._io.pos()

            self._debug['mipmap_levels']['end'] = self._io.pos()

        def _read_be(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u4be()
            self._debug['type']['end'] = self._io.pos()
            self._debug['type_size']['start'] = self._io.pos()
            self.type_size = self._io.read_u4be()
            self._debug['type_size']['end'] = self._io.pos()
            self._debug['format']['start'] = self._io.pos()
            self.format = self._io.read_u4be()
            self._debug['format']['end'] = self._io.pos()
            self._debug['internal_format']['start'] = self._io.pos()
            self.internal_format = KaitaiStream.resolve_enum(Ktx11.Format, self._io.read_u4be())
            self._debug['internal_format']['end'] = self._io.pos()
            self._debug['base_internal_format']['start'] = self._io.pos()
            self.base_internal_format = self._io.read_u4be()
            self._debug['base_internal_format']['end'] = self._io.pos()
            self._debug['pixel_width']['start'] = self._io.pos()
            self.pixel_width = self._io.read_u4be()
            self._debug['pixel_width']['end'] = self._io.pos()
            self._debug['pixel_height']['start'] = self._io.pos()
            self.pixel_height = self._io.read_u4be()
            self._debug['pixel_height']['end'] = self._io.pos()
            self._debug['pixel_depth']['start'] = self._io.pos()
            self.pixel_depth = self._io.read_u4be()
            self._debug['pixel_depth']['end'] = self._io.pos()
            self._debug['array_elements_num']['start'] = self._io.pos()
            self.array_elements_num = self._io.read_u4be()
            self._debug['array_elements_num']['end'] = self._io.pos()
            self._debug['num_faces']['start'] = self._io.pos()
            self.num_faces = self._io.read_u4be()
            self._debug['num_faces']['end'] = self._io.pos()
            self._debug['mipmap_levels_num']['start'] = self._io.pos()
            self.mipmap_levels_num = self._io.read_u4be()
            self._debug['mipmap_levels_num']['end'] = self._io.pos()
            self._debug['len_key_value_data']['start'] = self._io.pos()
            self.len_key_value_data = self._io.read_u4be()
            self._debug['len_key_value_data']['end'] = self._io.pos()
            self._debug['key_value_data']['start'] = self._io.pos()
            self._raw_key_value_data = self._io.read_bytes(self.len_key_value_data)
            _io__raw_key_value_data = KaitaiStream(BytesIO(self._raw_key_value_data))
            self.key_value_data = Ktx11.Ktx.KeyValueData(_io__raw_key_value_data, self, self._root, self._is_le)
            self._debug['key_value_data']['end'] = self._io.pos()
            self._debug['mipmap_levels']['start'] = self._io.pos()
            self._debug['mipmap_levels']['arr'] = []
            self.mipmap_levels = []
            for i in range(self.num_mipmap_levels):
                self._debug['mipmap_levels']['arr'].append({'start': self._io.pos()})
                self.mipmap_levels.append(Ktx11.Ktx.MipmapLevel(self._io, self, self._root, self._is_le))
                self._debug['mipmap_levels']['arr'][i]['end'] = self._io.pos()

            self._debug['mipmap_levels']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.key_value_data._fetch_instances()
            for i in range(len(self.mipmap_levels)):
                pass
                self.mipmap_levels[i]._fetch_instances()


        class KeyValue(KaitaiStruct):
            SEQ_FIELDS = ["len_key_value", "key_value", "padding"]
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                super(Ktx11.Ktx.KeyValue, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._is_le = _is_le
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/ktx/types/key_value")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self._debug['len_key_value']['start'] = self._io.pos()
                self.len_key_value = self._io.read_u4le()
                self._debug['len_key_value']['end'] = self._io.pos()
                self._debug['key_value']['start'] = self._io.pos()
                self.key_value = self._io.read_bytes(self.len_key_value)
                self._debug['key_value']['end'] = self._io.pos()
                self._debug['padding']['start'] = self._io.pos()
                self.padding = self._io.read_bytes(-(self.len_key_value) % 4)
                self._debug['padding']['end'] = self._io.pos()

            def _read_be(self):
                self._debug['len_key_value']['start'] = self._io.pos()
                self.len_key_value = self._io.read_u4be()
                self._debug['len_key_value']['end'] = self._io.pos()
                self._debug['key_value']['start'] = self._io.pos()
                self.key_value = self._io.read_bytes(self.len_key_value)
                self._debug['key_value']['end'] = self._io.pos()
                self._debug['padding']['start'] = self._io.pos()
                self.padding = self._io.read_bytes(-(self.len_key_value) % 4)
                self._debug['padding']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class KeyValueData(KaitaiStruct):
            SEQ_FIELDS = ["key_value"]
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                super(Ktx11.Ktx.KeyValueData, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._is_le = _is_le
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/ktx/types/key_value_data")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self._debug['key_value']['start'] = self._io.pos()
                self._debug['key_value']['arr'] = []
                self.key_value = []
                i = 0
                while not self._io.is_eof():
                    self._debug['key_value']['arr'].append({'start': self._io.pos()})
                    self.key_value.append(Ktx11.Ktx.KeyValue(self._io, self, self._root, self._is_le))
                    self._debug['key_value']['arr'][len(self.key_value) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['key_value']['end'] = self._io.pos()

            def _read_be(self):
                self._debug['key_value']['start'] = self._io.pos()
                self._debug['key_value']['arr'] = []
                self.key_value = []
                i = 0
                while not self._io.is_eof():
                    self._debug['key_value']['arr'].append({'start': self._io.pos()})
                    self.key_value.append(Ktx11.Ktx.KeyValue(self._io, self, self._root, self._is_le))
                    self._debug['key_value']['arr'][len(self.key_value) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['key_value']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.key_value)):
                    pass
                    self.key_value[i]._fetch_instances()



        class MipmapLevel(KaitaiStruct):
            SEQ_FIELDS = ["len_image", "image", "padding"]
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                super(Ktx11.Ktx.MipmapLevel, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._is_le = _is_le
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/ktx/types/mipmap_level")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self._debug['len_image']['start'] = self._io.pos()
                self.len_image = self._io.read_u4le()
                self._debug['len_image']['end'] = self._io.pos()
                self._debug['image']['start'] = self._io.pos()
                self.image = self._io.read_bytes(self.len_image)
                self._debug['image']['end'] = self._io.pos()
                self._debug['padding']['start'] = self._io.pos()
                self.padding = self._io.read_bytes(-(self.len_image) % 4)
                self._debug['padding']['end'] = self._io.pos()

            def _read_be(self):
                self._debug['len_image']['start'] = self._io.pos()
                self.len_image = self._io.read_u4be()
                self._debug['len_image']['end'] = self._io.pos()
                self._debug['image']['start'] = self._io.pos()
                self.image = self._io.read_bytes(self.len_image)
                self._debug['image']['end'] = self._io.pos()
                self._debug['padding']['start'] = self._io.pos()
                self.padding = self._io.read_bytes(-(self.len_image) % 4)
                self._debug['padding']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        @property
        def compressed(self):
            if hasattr(self, '_m_compressed'):
                return self._m_compressed

            self._m_compressed = self.type == 0
            return getattr(self, '_m_compressed', None)

        @property
        def num_array_elements(self):
            if hasattr(self, '_m_num_array_elements'):
                return self._m_num_array_elements

            self._m_num_array_elements = (1 if self.array_elements_num == 0 else self.array_elements_num)
            return getattr(self, '_m_num_array_elements', None)

        @property
        def num_mipmap_levels(self):
            if hasattr(self, '_m_num_mipmap_levels'):
                return self._m_num_mipmap_levels

            self._m_num_mipmap_levels = (1 if self.mipmap_levels_num == 0 else (1 if  ((self.internal_format == Ktx11.Format.palette4_rgb8_eos) or (self.internal_format == Ktx11.Format.palette4_rgba8_eos) or (self.internal_format == Ktx11.Format.palette4_r5_g6_b5_eos) or (self.internal_format == Ktx11.Format.palette4_rgba4_eos) or (self.internal_format == Ktx11.Format.palette4_rgb5_a1_eos) or (self.internal_format == Ktx11.Format.palette8_rgb8_eos) or (self.internal_format == Ktx11.Format.palette8_rgba8_eos) or (self.internal_format == Ktx11.Format.palette8_r5_g6_b5_eos) or (self.internal_format == Ktx11.Format.palette8_rgba4_eos) or (self.internal_format == Ktx11.Format.palette8_rgb5_a1_eos))  else self.mipmap_levels_num))
            return getattr(self, '_m_num_mipmap_levels', None)



