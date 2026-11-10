# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Anjvision(KaitaiStruct):
    """ANJVision is a Chinese manufacturer of IP cameras. The company uses
    its own firmware format, which is a fairly simple wrapper around U-boot
    and a file system. So far the only observed file system is Squashfs.
    """
    SEQ_FIELDS = ["header", "rest_of_header", "uboot", "file_system"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Anjvision, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Anjvision.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['rest_of_header']['start'] = self._io.pos()
        self.rest_of_header = self._io.read_bytes(self.header.len_header - 32)
        self._debug['rest_of_header']['end'] = self._io.pos()
        self._debug['uboot']['start'] = self._io.pos()
        self.uboot = self._io.read_bytes(self.header.len_data)
        self._debug['uboot']['end'] = self._io.pos()
        self._debug['file_system']['start'] = self._io.pos()
        self.file_system = self._io.read_bytes((self.header.len_file - self.header.len_data) - self.header.len_header)
        self._debug['file_system']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "unknown", "len_file", "unknown_1", "len_header", "len_data", "unknown_2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Anjvision.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x41\x4E\x4A\x4F\x59\x38\x38\x38":
                raise kaitaistruct.ValidationNotEqualError(b"\x41\x4E\x4A\x4F\x59\x38\x38\x38", self.magic, self._io, u"/types/header/seq/0")
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(4)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['unknown_1']['start'] = self._io.pos()
            self.unknown_1 = self._io.read_u4le()
            self._debug['unknown_1']['end'] = self._io.pos()
            if not self.unknown_1 == 3:
                raise kaitaistruct.ValidationNotEqualError(3, self.unknown_1, self._io, u"/types/header/seq/3")
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['unknown_2']['start'] = self._io.pos()
            self.unknown_2 = self._io.read_u4le()
            self._debug['unknown_2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



