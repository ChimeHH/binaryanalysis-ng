# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Sgi(KaitaiStruct):
    """
    .. seealso::
       Source - https://media.xiph.org/svt/SGIIMAGESPEC
    """

    class Colormap(IntEnum):
        normal = 0
        dithered = 1
        screen = 2
        colormap = 3

    class StorageFormat(IntEnum):
        verbatim = 0
        rle = 1
    SEQ_FIELDS = ["header", "body"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Sgi, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(512)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Sgi.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['body']['start'] = self._io.pos()
        _on = self.header.storage_format
        if _on == Sgi.StorageFormat.rle:
            pass
            self.body = Sgi.Rle(self._io, self, self._root)
        elif _on == Sgi.StorageFormat.verbatim:
            pass
            self.body = Sgi.Verbatim(self._io, self, self._root)
        self._debug['body']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        _on = self.header.storage_format
        if _on == Sgi.StorageFormat.rle:
            pass
            self.body._fetch_instances()
        elif _on == Sgi.StorageFormat.verbatim:
            pass
            self.body._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "storage_format", "bytes_per_pixel", "num_dimensions", "xsize", "ysize", "zsize", "min_pix", "max_pix", "ignored1", "name", "colormap", "ignored"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Sgi.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x01\xDA":
                raise kaitaistruct.ValidationNotEqualError(b"\x01\xDA", self.magic, self._io, u"/types/header/seq/0")
            self._debug['storage_format']['start'] = self._io.pos()
            self.storage_format = KaitaiStream.resolve_enum(Sgi.StorageFormat, self._io.read_u1())
            self._debug['storage_format']['end'] = self._io.pos()
            self._debug['bytes_per_pixel']['start'] = self._io.pos()
            self.bytes_per_pixel = self._io.read_u1()
            self._debug['bytes_per_pixel']['end'] = self._io.pos()
            self._debug['num_dimensions']['start'] = self._io.pos()
            self.num_dimensions = self._io.read_u2be()
            self._debug['num_dimensions']['end'] = self._io.pos()
            if not  ((self.num_dimensions == 1) or (self.num_dimensions == 2) or (self.num_dimensions == 3)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.num_dimensions, self._io, u"/types/header/seq/3")
            self._debug['xsize']['start'] = self._io.pos()
            self.xsize = self._io.read_u2be()
            self._debug['xsize']['end'] = self._io.pos()
            self._debug['ysize']['start'] = self._io.pos()
            self.ysize = self._io.read_u2be()
            self._debug['ysize']['end'] = self._io.pos()
            self._debug['zsize']['start'] = self._io.pos()
            self.zsize = self._io.read_u2be()
            self._debug['zsize']['end'] = self._io.pos()
            self._debug['min_pix']['start'] = self._io.pos()
            self.min_pix = self._io.read_u4be()
            self._debug['min_pix']['end'] = self._io.pos()
            self._debug['max_pix']['start'] = self._io.pos()
            self.max_pix = self._io.read_u4be()
            self._debug['max_pix']['end'] = self._io.pos()
            self._debug['ignored1']['start'] = self._io.pos()
            self.ignored1 = Sgi.Padding(4, self._io, self, self._root)
            self._debug['ignored1']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(80), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['colormap']['start'] = self._io.pos()
            self.colormap = KaitaiStream.resolve_enum(Sgi.Colormap, self._io.read_u4be())
            self._debug['colormap']['end'] = self._io.pos()
            if not isinstance(self.colormap, Sgi.Colormap):
                raise kaitaistruct.ValidationNotInEnumError(self.colormap, self._io, u"/types/header/seq/11")
            self._debug['ignored']['start'] = self._io.pos()
            self.ignored = Sgi.Padding(404, self._io, self, self._root)
            self._debug['ignored']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.ignored1._fetch_instances()
            self.ignored._fetch_instances()


    class Padding(KaitaiStruct):
        SEQ_FIELDS = ["padding_bytes"]
        def __init__(self, num_padding, _io, _parent=None, _root=None):
            super(Sgi.Padding, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_padding = num_padding
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['padding_bytes']['start'] = self._io.pos()
            self._debug['padding_bytes']['arr'] = []
            self.padding_bytes = []
            for i in range(self.num_padding):
                self._debug['padding_bytes']['arr'].append({'start': self._io.pos()})
                self.padding_bytes.append(Sgi.PaddingByte(self._io, self, self._root))
                self._debug['padding_bytes']['arr'][i]['end'] = self._io.pos()

            self._debug['padding_bytes']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.padding_bytes)):
                pass
                self.padding_bytes[i]._fetch_instances()



    class PaddingByte(KaitaiStruct):
        SEQ_FIELDS = ["padding_byte"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Sgi.PaddingByte, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['padding_byte']['start'] = self._io.pos()
            self.padding_byte = self._io.read_bytes(1)
            self._debug['padding_byte']['end'] = self._io.pos()
            if not self.padding_byte == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.padding_byte, self._io, u"/types/padding_byte/seq/0")


        def _fetch_instances(self):
            pass


    class Rle(KaitaiStruct):
        SEQ_FIELDS = ["start_table_entries", "length_table_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Sgi.Rle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['start_table_entries']['start'] = self._io.pos()
            self._debug['start_table_entries']['arr'] = []
            self.start_table_entries = []
            for i in range(self._root.header.ysize * self._root.header.zsize):
                self._debug['start_table_entries']['arr'].append({'start': self._io.pos()})
                self.start_table_entries.append(self._io.read_u4be())
                self._debug['start_table_entries']['arr'][i]['end'] = self._io.pos()

            self._debug['start_table_entries']['end'] = self._io.pos()
            self._debug['length_table_entries']['start'] = self._io.pos()
            self._debug['length_table_entries']['arr'] = []
            self.length_table_entries = []
            for i in range(self._root.header.ysize * self._root.header.zsize):
                self._debug['length_table_entries']['arr'].append({'start': self._io.pos()})
                self.length_table_entries.append(self._io.read_u4be())
                self._debug['length_table_entries']['arr'][i]['end'] = self._io.pos()

            self._debug['length_table_entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.start_table_entries)):
                pass

            for i in range(len(self.length_table_entries)):
                pass

            _ = self.scanlines
            if hasattr(self, '_m_scanlines'):
                pass
                for i in range(len(self._m_scanlines)):
                    pass
                    self._m_scanlines[i]._fetch_instances()



        @property
        def scanlines(self):
            if hasattr(self, '_m_scanlines'):
                return self._m_scanlines

            self._debug['_m_scanlines']['start'] = self._io.pos()
            self._debug['_m_scanlines']['arr'] = []
            self._m_scanlines = []
            for i in range(self._root.header.ysize * self._root.header.zsize):
                self._debug['_m_scanlines']['arr'].append({'start': self._io.pos()})
                self._m_scanlines.append(Sgi.Scanline(i, self._io, self, self._root))
                self._debug['_m_scanlines']['arr'][i]['end'] = self._io.pos()

            self._debug['_m_scanlines']['end'] = self._io.pos()
            return getattr(self, '_m_scanlines', None)


    class Scanline(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, i, _io, _parent=None, _root=None):
            super(Sgi.Scanline, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.i = i
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.data
            if hasattr(self, '_m_data'):
                pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            io = self._root._io
            _pos = io.pos()
            io.seek(self._parent.start_table_entries[self.i])
            self._debug['_m_data']['start'] = io.pos()
            self._m_data = io.read_bytes(self._parent.length_table_entries[self.i])
            self._debug['_m_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_data', None)


    class Verbatim(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Sgi.Verbatim, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(((self._root.header.xsize * self._root.header.ysize) * self._root.header.zsize) * self._root.header.bytes_per_pixel)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



