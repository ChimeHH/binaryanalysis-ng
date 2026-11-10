# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Bzip2(KaitaiStruct):
    """
    .. seealso::
       Source - https://raw.githubusercontent.com/dsnet/compress/master/doc/bzip2-format.pdf
    """
    SEQ_FIELDS = ["header", "block_header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Bzip2, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Bzip2.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['block_header']['start'] = self._io.pos()
        self.block_header = Bzip2.BlockHeader(self._io, self, self._root)
        self._debug['block_header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.block_header._fetch_instances()

    class BlockHeader(KaitaiStruct):
        SEQ_FIELDS = ["signature", "crc"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Bzip2.BlockHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(6)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x31\x41\x59\x26\x53\x59":
                raise kaitaistruct.ValidationNotEqualError(b"\x31\x41\x59\x26\x53\x59", self.signature, self._io, u"/types/block_header/seq/0")
            self._debug['crc']['start'] = self._io.pos()
            self.crc = self._io.read_u4be()
            self._debug['crc']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "level_char"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Bzip2.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x42\x5A":
                raise kaitaistruct.ValidationNotEqualError(b"\x42\x5A", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = (self._io.read_bytes(1)).decode(u"UTF-8")
            self._debug['version']['end'] = self._io.pos()
            if not self.version == u"h":
                raise kaitaistruct.ValidationNotEqualError(u"h", self.version, self._io, u"/types/header/seq/1")
            self._debug['level_char']['start'] = self._io.pos()
            self.level_char = (self._io.read_bytes(1)).decode(u"UTF-8")
            self._debug['level_char']['end'] = self._io.pos()
            if not  ((self.level_char == u"1") or (self.level_char == u"2") or (self.level_char == u"3") or (self.level_char == u"4") or (self.level_char == u"5") or (self.level_char == u"6") or (self.level_char == u"7") or (self.level_char == u"8") or (self.level_char == u"9")) :
                raise kaitaistruct.ValidationNotAnyOfError(self.level_char, self._io, u"/types/header/seq/2")


        def _fetch_instances(self):
            pass

        @property
        def level(self):
            if hasattr(self, '_m_level'):
                return self._m_level

            self._m_level = int(self.level_char)
            return getattr(self, '_m_level', None)



