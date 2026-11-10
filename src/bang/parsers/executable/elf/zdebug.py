# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections
import zlib


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Zdebug(KaitaiStruct):
    """Generate test file for a simple 'Hello World':
    $ cc -g hello.c -gz=zlib-gnu
    
    .. seealso::
       <http://www.linker-aliens.org/blogs/ali/entry/elf_section_compression/>
    """
    SEQ_FIELDS = ["magic", "len_data", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Zdebug, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x5A\x4C\x49\x42":
            raise kaitaistruct.ValidationNotEqualError(b"\x5A\x4C\x49\x42", self.magic, self._io, u"/seq/0")
        self._debug['len_data']['start'] = self._io.pos()
        self.len_data = self._io.read_u8be()
        self._debug['len_data']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self._raw_data = self._io.read_bytes_full()
        self.data = zlib.decompress(self._raw_data)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass


