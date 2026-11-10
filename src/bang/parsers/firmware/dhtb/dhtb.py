# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Dhtb(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/osm0sis/dhtbsign
    """
    SEQ_FIELDS = ["header", "payload"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Dhtb, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(512)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Dhtb.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['payload']['start'] = self._io.pos()
        self.payload = self._io.read_bytes(self.header.len_payload)
        self._debug['payload']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "sha256", "padding1", "len_payload", "padding2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Dhtb.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x44\x48\x54\x42\x01\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x44\x48\x54\x42\x01\x00\x00\x00", self.magic, self._io, u"/types/header/seq/0")
            self._debug['sha256']['start'] = self._io.pos()
            self.sha256 = self._io.read_bytes(32)
            self._debug['sha256']['end'] = self._io.pos()
            self._debug['padding1']['start'] = self._io.pos()
            self.padding1 = self._io.read_bytes(8)
            self._debug['padding1']['end'] = self._io.pos()
            if not self.padding1 == b"\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00", self.padding1, self._io, u"/types/header/seq/2")
            self._debug['len_payload']['start'] = self._io.pos()
            self.len_payload = self._io.read_u4le()
            self._debug['len_payload']['end'] = self._io.pos()
            self._debug['padding2']['start'] = self._io.pos()
            self._debug['padding2']['arr'] = []
            self.padding2 = []
            i = 0
            while not self._io.is_eof():
                self._debug['padding2']['arr'].append({'start': self._io.pos()})
                self.padding2.append(Dhtb.PaddingByte(self._io, self, self._root))
                self._debug['padding2']['arr'][len(self.padding2) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['padding2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.padding2)):
                pass
                self.padding2[i]._fetch_instances()



    class PaddingByte(KaitaiStruct):
        SEQ_FIELDS = ["padding_byte"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Dhtb.PaddingByte, self).__init__(_io)
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



