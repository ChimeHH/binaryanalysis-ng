# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Milbeaut(KaitaiStruct):
    """A reverse engineered file format used by Socionext for their Milbeaut
    SoC platform. One prominent user of this platform is GoPro. The firmware
    this specification was derived from is the Hero 9 (GoPro Labs firmware).
    
    <https://community.gopro.com/html/assets/LABS_HERO9_01_60_70.zip>
    """
    SEQ_FIELDS = ["magic", "unknown", "len_data", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Milbeaut, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(8)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x4D\x49\x4C\x42\x45\x41\x55\x54":
            raise kaitaistruct.ValidationNotEqualError(b"\x4D\x49\x4C\x42\x45\x41\x55\x54", self.magic, self._io, u"/seq/0")
        self._debug['unknown']['start'] = self._io.pos()
        self.unknown = self._io.read_u4le()
        self._debug['unknown']['end'] = self._io.pos()
        self._debug['len_data']['start'] = self._io.pos()
        self.len_data = self._io.read_u4le()
        self._debug['len_data']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self.data = self._io.read_bytes(self.len_data)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass


