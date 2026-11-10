# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Pif(KaitaiStruct):
    """The Portable Image Format (PIF) is a basic, bitmap-like image format with the
    focus on ease of use (implementation) and small size for embedded
    applications.
    
    See <https://github.com/gfcwfzkm/PIF-Image-Format> for more info.
    
    .. seealso::
       Source - https://github.com/gfcwfzkm/PIF-Image-Format/blob/4ec261b/Specification/PIF%20Format%20Specification.pdf
    
    
    .. seealso::
       Source - https://github.com/gfcwfzkm/PIF-Image-Format/blob/4ec261b/C%20Library/pifdec.c#L300
    """

    class CompressionType(IntEnum):
        none = 0
        rle = 32222

    class ImageType(IntEnum):
        rgb332 = 7763
        rgb888 = 17212
        indexed_rgb332 = 18754
        indexed_rgb565 = 18759
        indexed_rgb888 = 18770
        black_white = 32170
        rgb16c = 47253
        rgb565 = 58821
    SEQ_FIELDS = ["file_header", "info_header", "color_table"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Pif, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['file_header']['start'] = self._io.pos()
        self.file_header = Pif.PifHeader(self._io, self, self._root)
        self._debug['file_header']['end'] = self._io.pos()
        self._debug['info_header']['start'] = self._io.pos()
        self.info_header = Pif.InformationHeader(self._io, self, self._root)
        self._debug['info_header']['end'] = self._io.pos()
        if self.info_header.uses_indexed_mode:
            pass
            self._debug['color_table']['start'] = self._io.pos()
            self._raw_color_table = self._io.read_bytes(self.info_header.len_color_table)
            _io__raw_color_table = KaitaiStream(BytesIO(self._raw_color_table))
            self.color_table = Pif.ColorTableData(_io__raw_color_table, self, self._root)
            self._debug['color_table']['end'] = self._io.pos()



    def _fetch_instances(self):
        pass
        self.file_header._fetch_instances()
        self.info_header._fetch_instances()
        if self.info_header.uses_indexed_mode:
            pass
            self.color_table._fetch_instances()

        _ = self.image_data
        if hasattr(self, '_m_image_data'):
            pass


    class ColorTableData(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pif.ColorTableData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                _on = self._root.info_header.image_type
                if _on == Pif.ImageType.indexed_rgb332:
                    pass
                    self.entries.append(self._io.read_bits_int_le(8))
                elif _on == Pif.ImageType.indexed_rgb565:
                    pass
                    self.entries.append(self._io.read_bits_int_le(16))
                elif _on == Pif.ImageType.indexed_rgb888:
                    pass
                    self.entries.append(self._io.read_bits_int_le(24))
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                _on = self._root.info_header.image_type
                if _on == Pif.ImageType.indexed_rgb332:
                    pass
                elif _on == Pif.ImageType.indexed_rgb565:
                    pass
                elif _on == Pif.ImageType.indexed_rgb888:
                    pass



    class InformationHeader(KaitaiStruct):
        SEQ_FIELDS = ["image_type", "bits_per_pixel", "width", "height", "len_image_data", "len_color_table", "compression"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pif.InformationHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['image_type']['start'] = self._io.pos()
            self.image_type = KaitaiStream.resolve_enum(Pif.ImageType, self._io.read_u2le())
            self._debug['image_type']['end'] = self._io.pos()
            if not  ((self.image_type == Pif.ImageType.rgb888) or (self.image_type == Pif.ImageType.rgb565) or (self.image_type == Pif.ImageType.rgb332) or (self.image_type == Pif.ImageType.rgb16c) or (self.image_type == Pif.ImageType.black_white) or (self.image_type == Pif.ImageType.indexed_rgb888) or (self.image_type == Pif.ImageType.indexed_rgb565) or (self.image_type == Pif.ImageType.indexed_rgb332)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.image_type, self._io, u"/types/information_header/seq/0")
            self._debug['bits_per_pixel']['start'] = self._io.pos()
            self.bits_per_pixel = self._io.read_u2le()
            self._debug['bits_per_pixel']['end'] = self._io.pos()
            _ = self.bits_per_pixel
            if not (_ == 24 if self.image_type == Pif.ImageType.rgb888 else (_ == 16 if self.image_type == Pif.ImageType.rgb565 else (_ == 8 if self.image_type == Pif.ImageType.rgb332 else (_ == 4 if self.image_type == Pif.ImageType.rgb16c else (_ == 1 if self.image_type == Pif.ImageType.black_white else (_ <= 8 if self.uses_indexed_mode else True)))))):
                raise kaitaistruct.ValidationExprError(self.bits_per_pixel, self._io, u"/types/information_header/seq/1")
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u2le()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u2le()
            self._debug['height']['end'] = self._io.pos()
            self._debug['len_image_data']['start'] = self._io.pos()
            self.len_image_data = self._io.read_u4le()
            self._debug['len_image_data']['end'] = self._io.pos()
            if not self.len_image_data <= self._root.file_header.len_file - self._root.file_header.ofs_image_data:
                raise kaitaistruct.ValidationGreaterThanError(self._root.file_header.len_file - self._root.file_header.ofs_image_data, self.len_image_data, self._io, u"/types/information_header/seq/4")
            self._debug['len_color_table']['start'] = self._io.pos()
            self.len_color_table = self._io.read_u2le()
            self._debug['len_color_table']['end'] = self._io.pos()
            if not self.len_color_table >= (self.len_color_table_entry * 1 if self.uses_indexed_mode else 0):
                raise kaitaistruct.ValidationLessThanError((self.len_color_table_entry * 1 if self.uses_indexed_mode else 0), self.len_color_table, self._io, u"/types/information_header/seq/5")
            if not self.len_color_table <= ((self.len_color_table_max if self.len_color_table_max < self.len_color_table_full else self.len_color_table_full) if self.uses_indexed_mode else 0):
                raise kaitaistruct.ValidationGreaterThanError(((self.len_color_table_max if self.len_color_table_max < self.len_color_table_full else self.len_color_table_full) if self.uses_indexed_mode else 0), self.len_color_table, self._io, u"/types/information_header/seq/5")
            self._debug['compression']['start'] = self._io.pos()
            self.compression = KaitaiStream.resolve_enum(Pif.CompressionType, self._io.read_u2le())
            self._debug['compression']['end'] = self._io.pos()
            if not  ((self.compression == Pif.CompressionType.none) or (self.compression == Pif.CompressionType.rle)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.compression, self._io, u"/types/information_header/seq/6")


        def _fetch_instances(self):
            pass

        @property
        def len_color_table_entry(self):
            if hasattr(self, '_m_len_color_table_entry'):
                return self._m_len_color_table_entry

            self._m_len_color_table_entry = (3 if self.image_type == Pif.ImageType.indexed_rgb888 else (2 if self.image_type == Pif.ImageType.indexed_rgb565 else (1 if self.image_type == Pif.ImageType.indexed_rgb332 else 0)))
            return getattr(self, '_m_len_color_table_entry', None)

        @property
        def len_color_table_full(self):
            if hasattr(self, '_m_len_color_table_full'):
                return self._m_len_color_table_full

            self._m_len_color_table_full = self.len_color_table_entry * (1 << self.bits_per_pixel)
            return getattr(self, '_m_len_color_table_full', None)

        @property
        def len_color_table_max(self):
            if hasattr(self, '_m_len_color_table_max'):
                return self._m_len_color_table_max

            self._m_len_color_table_max = self._root.file_header.ofs_image_data - self._root.file_header.ofs_image_data_min
            return getattr(self, '_m_len_color_table_max', None)

        @property
        def uses_indexed_mode(self):
            if hasattr(self, '_m_uses_indexed_mode'):
                return self._m_uses_indexed_mode

            self._m_uses_indexed_mode = self.len_color_table_entry != 0
            return getattr(self, '_m_uses_indexed_mode', None)


    class PifHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_file", "ofs_image_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pif.PifHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x50\x49\x46\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x50\x49\x46\x00", self.magic, self._io, u"/types/pif_header/seq/0")
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()
            if not self.len_file >= self.ofs_image_data_min:
                raise kaitaistruct.ValidationLessThanError(self.ofs_image_data_min, self.len_file, self._io, u"/types/pif_header/seq/1")
            self._debug['ofs_image_data']['start'] = self._io.pos()
            self.ofs_image_data = self._io.read_u4le()
            self._debug['ofs_image_data']['end'] = self._io.pos()
            if not self.ofs_image_data >= self.ofs_image_data_min:
                raise kaitaistruct.ValidationLessThanError(self.ofs_image_data_min, self.ofs_image_data, self._io, u"/types/pif_header/seq/2")
            if not self.ofs_image_data <= self.len_file:
                raise kaitaistruct.ValidationGreaterThanError(self.len_file, self.ofs_image_data, self._io, u"/types/pif_header/seq/2")


        def _fetch_instances(self):
            pass

        @property
        def ofs_image_data_min(self):
            if hasattr(self, '_m_ofs_image_data_min'):
                return self._m_ofs_image_data_min

            self._m_ofs_image_data_min = 12 + 16
            return getattr(self, '_m_ofs_image_data_min', None)


    @property
    def image_data(self):
        if hasattr(self, '_m_image_data'):
            return self._m_image_data

        _pos = self._io.pos()
        self._io.seek(self.file_header.ofs_image_data)
        self._debug['_m_image_data']['start'] = self._io.pos()
        self._m_image_data = self._io.read_bytes(self.info_header.len_image_data)
        self._debug['_m_image_data']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_image_data', None)


