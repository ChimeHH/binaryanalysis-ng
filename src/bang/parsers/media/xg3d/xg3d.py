# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Xg3d(KaitaiStruct):
    """a proprietary file format from 3D Studio Max. There is not
    much to extract, but at least the size of the file can be verified.
    This analysis was based on just a few samples found inside the
    firmware of an Android phone made by LG Electronics.
    
    Test file: LGF320S-V21j-MAR-15-2014.tot
    """
    SEQ_FIELDS = ["header", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Xg3d, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Xg3d.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self.data = self._io.read_bytes(self.header.len_file - 71)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "unknown", "len_file", "len_file_2", "tool_name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Xg3d.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x58\x47\x33\x44":
                raise kaitaistruct.ValidationNotEqualError(b"\x58\x47\x33\x44", self.magic, self._io, u"/types/header/seq/0")
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(25)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['len_file_2']['start'] = self._io.pos()
            self.len_file_2 = self._io.read_u4le()
            self._debug['len_file_2']['end'] = self._io.pos()
            self._debug['tool_name']['start'] = self._io.pos()
            self.tool_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(34), 0, False)).decode(u"UTF-8")
            self._debug['tool_name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



