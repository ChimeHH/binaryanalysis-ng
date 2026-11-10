# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class ReolinkLogo(KaitaiStruct):
    SEQ_FIELDS = ["header", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(ReolinkLogo, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = ReolinkLogo.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self._raw_data = self._io.read_bytes(self.header.len_file - 32)
        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
        self.data = ReolinkLogo.Dummy(_io__raw_data, self, self._root)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.data._fetch_instances()
        _ = self.jpeg_1
        if hasattr(self, '_m_jpeg_1'):
            pass

        _ = self.jpeg_2
        if hasattr(self, '_m_jpeg_2'):
            pass


    class Dummy(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(ReolinkLogo.Dummy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_file", "unknown", "ofs_jpeg_1", "ofs_jpeg_2", "len_jpeg_1", "len_jpeg_2", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(ReolinkLogo.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x47\x4C\x4F\x52":
                raise kaitaistruct.ValidationNotEqualError(b"\x47\x4C\x4F\x52", self.magic, self._io, u"/types/header/seq/0")
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_u4le()
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['ofs_jpeg_1']['start'] = self._io.pos()
            self.ofs_jpeg_1 = self._io.read_u4le()
            self._debug['ofs_jpeg_1']['end'] = self._io.pos()
            self._debug['ofs_jpeg_2']['start'] = self._io.pos()
            self.ofs_jpeg_2 = self._io.read_u4le()
            self._debug['ofs_jpeg_2']['end'] = self._io.pos()
            self._debug['len_jpeg_1']['start'] = self._io.pos()
            self.len_jpeg_1 = self._io.read_u4le()
            self._debug['len_jpeg_1']['end'] = self._io.pos()
            self._debug['len_jpeg_2']['start'] = self._io.pos()
            self.len_jpeg_2 = self._io.read_u4le()
            self._debug['len_jpeg_2']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(4)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def jpeg_1(self):
        if hasattr(self, '_m_jpeg_1'):
            return self._m_jpeg_1

        io = self.data._io
        _pos = io.pos()
        io.seek(self.header.ofs_jpeg_1 - 32)
        self._debug['_m_jpeg_1']['start'] = io.pos()
        self._m_jpeg_1 = io.read_bytes(self.header.len_jpeg_1)
        self._debug['_m_jpeg_1']['end'] = io.pos()
        io.seek(_pos)
        return getattr(self, '_m_jpeg_1', None)

    @property
    def jpeg_2(self):
        if hasattr(self, '_m_jpeg_2'):
            return self._m_jpeg_2

        io = self.data._io
        _pos = io.pos()
        io.seek(self.header.ofs_jpeg_2 - 32)
        self._debug['_m_jpeg_2']['start'] = io.pos()
        self._m_jpeg_2 = io.read_bytes(self.header.len_jpeg_2)
        self._debug['_m_jpeg_2']['end'] = io.pos()
        io.seek(_pos)
        return getattr(self, '_m_jpeg_2', None)


