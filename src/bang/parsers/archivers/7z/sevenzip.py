# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Sevenzip(KaitaiStruct):
    SEQ_FIELDS = ["header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Sevenzip, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Sevenzip.SignatureHeader(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class SignatureHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "major_version", "minor_version", "start_header_crc", "start_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Sevenzip.SignatureHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(6)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x37\x7A\xBC\xAF\x27\x1C":
                raise kaitaistruct.ValidationNotEqualError(b"\x37\x7A\xBC\xAF\x27\x1C", self.magic, self._io, u"/types/signature_header/seq/0")
            self._debug['major_version']['start'] = self._io.pos()
            self.major_version = self._io.read_u1()
            self._debug['major_version']['end'] = self._io.pos()
            if not self.major_version == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.major_version, self._io, u"/types/signature_header/seq/1")
            self._debug['minor_version']['start'] = self._io.pos()
            self.minor_version = self._io.read_u1()
            self._debug['minor_version']['end'] = self._io.pos()
            self._debug['start_header_crc']['start'] = self._io.pos()
            self.start_header_crc = self._io.read_u4le()
            self._debug['start_header_crc']['end'] = self._io.pos()
            self._debug['start_header']['start'] = self._io.pos()
            self._raw_start_header = self._io.read_bytes(20)
            _io__raw_start_header = KaitaiStream(BytesIO(self._raw_start_header))
            self.start_header = Sevenzip.StartHeader(_io__raw_start_header, self, self._root)
            self._debug['start_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.start_header._fetch_instances()


    class StartHeader(KaitaiStruct):
        SEQ_FIELDS = ["ofs_next_header", "len_next_header", "next_header_crc"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Sevenzip.StartHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_next_header']['start'] = self._io.pos()
            self.ofs_next_header = self._io.read_u8le()
            self._debug['ofs_next_header']['end'] = self._io.pos()
            self._debug['len_next_header']['start'] = self._io.pos()
            self.len_next_header = self._io.read_u8le()
            self._debug['len_next_header']['end'] = self._io.pos()
            self._debug['next_header_crc']['start'] = self._io.pos()
            self.next_header_crc = self._io.read_u4le()
            self._debug['next_header_crc']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.next_header
            if hasattr(self, '_m_next_header'):
                pass


        @property
        def next_header(self):
            if hasattr(self, '_m_next_header'):
                return self._m_next_header

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_next_header + 32)
            self._debug['_m_next_header']['start'] = io.pos()
            self._m_next_header = io.read_bytes(self.len_next_header)
            self._debug['_m_next_header']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_next_header', None)



