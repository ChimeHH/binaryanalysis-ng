# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Seama(KaitaiStruct):
    """The original source code from the developer (Alphanetworks) says:
    
    "(SEA)ttle i(MA)ge is the image which used in project seattle."
    
    .. seealso::
       Source - https://git.openwrt.org/?p=openwrt/svn-archive/archive.git;a=blob;f=tools/firmware-utils/src/seama.h;h=02683b6e98d1be37d3dc835b34d4221a1f73a677;hb=HEAD
    """
    SEQ_FIELDS = ["magic", "reserved", "len_meta", "len_image", "md5_digest", "metadata", "image"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Seama, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x5E\xA3\xA4\x17":
            raise kaitaistruct.ValidationNotEqualError(b"\x5E\xA3\xA4\x17", self.magic, self._io, u"/seq/0")
        self._debug['reserved']['start'] = self._io.pos()
        self.reserved = self._io.read_bytes(2)
        self._debug['reserved']['end'] = self._io.pos()
        self._debug['len_meta']['start'] = self._io.pos()
        self.len_meta = self._io.read_u2be()
        self._debug['len_meta']['end'] = self._io.pos()
        self._debug['len_image']['start'] = self._io.pos()
        self.len_image = self._io.read_u4be()
        self._debug['len_image']['end'] = self._io.pos()
        if self.len_image != 0:
            pass
            self._debug['md5_digest']['start'] = self._io.pos()
            self.md5_digest = self._io.read_bytes(16)
            self._debug['md5_digest']['end'] = self._io.pos()

        self._debug['metadata']['start'] = self._io.pos()
        self.metadata = self._io.read_bytes(self.len_meta)
        self._debug['metadata']['end'] = self._io.pos()
        self._debug['image']['start'] = self._io.pos()
        self.image = self._io.read_bytes(self.len_image)
        self._debug['image']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        if self.len_image != 0:
            pass



