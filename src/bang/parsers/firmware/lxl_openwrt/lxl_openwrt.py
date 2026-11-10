# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class LxlOpenwrt(KaitaiStruct):
    """Luxul is a device manufacturer which has devices onto which OpenWrt
    can be installed. The format described here only applies to the OpenWrt
    builds, not to the firmware downloads from Luxul, which seem to have
    a different header.
    
    Only the header is described in this field.
    
    Test files: <https://openwrt.org/toh/hwdata/luxul/luxul_xbr-4500>
    
    .. seealso::
       Source - https://raw.githubusercontent.com/openwrt/openwrt/9aa6569a/tools/firmware-utils/src/lxlfw.c
    """
    SEQ_FIELDS = ["magic", "version", "len_header", "flags", "board", "release"]
    def __init__(self, _io, _parent=None, _root=None):
        super(LxlOpenwrt, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x4C\x58\x4C\x23":
            raise kaitaistruct.ValidationNotEqualError(b"\x4C\x58\x4C\x23", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        if not  ((self.version == 0) or (self.version == 1) or (self.version == 2)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/seq/1")
        self._debug['len_header']['start'] = self._io.pos()
        self.len_header = self._io.read_u4le()
        self._debug['len_header']['end'] = self._io.pos()
        if self.version > 0:
            pass
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()

        if self.version > 0:
            pass
            self._debug['board']['start'] = self._io.pos()
            self.board = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"UTF-8")
            self._debug['board']['end'] = self._io.pos()

        if self.version > 1:
            pass
            self._debug['release']['start'] = self._io.pos()
            self.release = self._io.read_bytes(16)
            self._debug['release']['end'] = self._io.pos()



    def _fetch_instances(self):
        pass
        if self.version > 0:
            pass

        if self.version > 0:
            pass

        if self.version > 1:
            pass



