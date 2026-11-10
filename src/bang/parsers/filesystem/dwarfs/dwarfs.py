# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Dwarfs(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/mhx/dwarfs/blob/main/doc/dwarfs-format.md
    """

    class Compression(IntEnum):
        no_compression = 0
        lzma = 1
        zstd = 2
        lz4 = 3
        lz4hc = 4

    class Sections(IntEnum):
        block = 0
        schema = 7
        metadata = 8
        index = 9
    SEQ_FIELDS = ["blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Dwarfs, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['blocks']['start'] = self._io.pos()
        self._debug['blocks']['arr'] = []
        self.blocks = []
        i = 0
        while not self._io.is_eof():
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            self.blocks.append(Dwarfs.Block(self._io, self, self._root))
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['blocks']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.blocks)):
            pass
            self.blocks[i]._fetch_instances()


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["magic", "major", "minor", "sha512_256", "xxhash", "section_number", "section_type", "compression_algorithm", "len_data", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Dwarfs.Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(6)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x44\x57\x41\x52\x46\x53":
                raise kaitaistruct.ValidationNotEqualError(b"\x44\x57\x41\x52\x46\x53", self.magic, self._io, u"/types/block/seq/0")
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u1()
            self._debug['major']['end'] = self._io.pos()
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u1()
            self._debug['minor']['end'] = self._io.pos()
            self._debug['sha512_256']['start'] = self._io.pos()
            self.sha512_256 = self._io.read_bytes(32)
            self._debug['sha512_256']['end'] = self._io.pos()
            self._debug['xxhash']['start'] = self._io.pos()
            self.xxhash = self._io.read_bytes(8)
            self._debug['xxhash']['end'] = self._io.pos()
            self._debug['section_number']['start'] = self._io.pos()
            self.section_number = self._io.read_u4le()
            self._debug['section_number']['end'] = self._io.pos()
            self._debug['section_type']['start'] = self._io.pos()
            self.section_type = KaitaiStream.resolve_enum(Dwarfs.Sections, self._io.read_u2le())
            self._debug['section_type']['end'] = self._io.pos()
            self._debug['compression_algorithm']['start'] = self._io.pos()
            self.compression_algorithm = KaitaiStream.resolve_enum(Dwarfs.Compression, self._io.read_u2le())
            self._debug['compression_algorithm']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u8le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



