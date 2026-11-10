# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Lzop(KaitaiStruct):
    """lzop is a compression/decompression program using the LZO library, similar
    as gzip using zlib.
    
    .. seealso::
       Source - https://www.lzop.org/
    """

    class LzopMethod(IntEnum):
        lzo1x_1 = 1
        lzo1x_1_15 = 2
        lzo1x_999 = 3
        zlib = 128
    SEQ_FIELDS = ["magic", "version", "library_version", "version_needed", "method", "level", "flags", "filter", "mode", "mtime", "len_name", "name", "checksum", "blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Lzop, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(9)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x89\x4C\x5A\x4F\x00\x0D\x0A\x1A\x0A":
            raise kaitaistruct.ValidationNotEqualError(b"\x89\x4C\x5A\x4F\x00\x0D\x0A\x1A\x0A", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u2be()
        self._debug['version']['end'] = self._io.pos()
        self._debug['library_version']['start'] = self._io.pos()
        self.library_version = self._io.read_u2be()
        self._debug['library_version']['end'] = self._io.pos()
        self._debug['version_needed']['start'] = self._io.pos()
        self.version_needed = self._io.read_u2be()
        self._debug['version_needed']['end'] = self._io.pos()
        if not self.version_needed >= 2368:
            raise kaitaistruct.ValidationLessThanError(2368, self.version_needed, self._io, u"/seq/3")
        self._debug['method']['start'] = self._io.pos()
        self.method = KaitaiStream.resolve_enum(Lzop.LzopMethod, self._io.read_u1())
        self._debug['method']['end'] = self._io.pos()
        if not  ((self.method == Lzop.LzopMethod.lzo1x_1) or (self.method == Lzop.LzopMethod.lzo1x_1_15) or (self.method == Lzop.LzopMethod.lzo1x_999) or (self.method == Lzop.LzopMethod.zlib)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.method, self._io, u"/seq/4")
        self._debug['level']['start'] = self._io.pos()
        self.level = self._io.read_u1()
        self._debug['level']['end'] = self._io.pos()
        if not self.level <= 9:
            raise kaitaistruct.ValidationGreaterThanError(9, self.level, self._io, u"/seq/5")
        self._debug['flags']['start'] = self._io.pos()
        self.flags = self._io.read_u4be()
        self._debug['flags']['end'] = self._io.pos()
        if self.flags & 2048 != 0:
            pass
            self._debug['filter']['start'] = self._io.pos()
            self.filter = self._io.read_u4be()
            self._debug['filter']['end'] = self._io.pos()

        self._debug['mode']['start'] = self._io.pos()
        self.mode = self._io.read_u4be()
        self._debug['mode']['end'] = self._io.pos()
        self._debug['mtime']['start'] = self._io.pos()
        self.mtime = self._io.read_u8be()
        self._debug['mtime']['end'] = self._io.pos()
        self._debug['len_name']['start'] = self._io.pos()
        self.len_name = self._io.read_u1()
        self._debug['len_name']['end'] = self._io.pos()
        self._debug['name']['start'] = self._io.pos()
        self.name = (self._io.read_bytes(self.len_name)).decode(u"UTF-8")
        self._debug['name']['end'] = self._io.pos()
        self._debug['checksum']['start'] = self._io.pos()
        self.checksum = self._io.read_u4be()
        self._debug['checksum']['end'] = self._io.pos()
        self._debug['blocks']['start'] = self._io.pos()
        self._debug['blocks']['arr'] = []
        self.blocks = []
        i = 0
        while True:
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            _ = Lzop.Block(self._io, self, self._root)
            self.blocks.append(_)
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            if _.len_decompressed == 0:
                break
            i += 1
        self._debug['blocks']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        if self.flags & 2048 != 0:
            pass

        for i in range(len(self.blocks)):
            pass
            self.blocks[i]._fetch_instances()


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["len_decompressed", "block_type"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Lzop.Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_decompressed']['start'] = self._io.pos()
            self.len_decompressed = self._io.read_u4be()
            self._debug['len_decompressed']['end'] = self._io.pos()
            self._debug['block_type']['start'] = self._io.pos()
            _on = self.len_decompressed
            if _on == 0:
                pass
                self.block_type = Lzop.Terminator(self._io, self, self._root)
            else:
                pass
                self.block_type = Lzop.RegularBlock(self._io, self, self._root)
            self._debug['block_type']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.len_decompressed
            if _on == 0:
                pass
                self.block_type._fetch_instances()
            else:
                pass
                self.block_type._fetch_instances()


    class RegularBlock(KaitaiStruct):
        SEQ_FIELDS = ["len_compressed", "uncompressed_checksum", "compressed_checksum", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Lzop.RegularBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_compressed']['start'] = self._io.pos()
            self.len_compressed = self._io.read_u4be()
            self._debug['len_compressed']['end'] = self._io.pos()
            if  ((self._root.flags & 1 != 0) or (self._root.flags & 256 != 0)) :
                pass
                self._debug['uncompressed_checksum']['start'] = self._io.pos()
                self.uncompressed_checksum = self._io.read_u4be()
                self._debug['uncompressed_checksum']['end'] = self._io.pos()

            if  ((self._root.flags & 2 != 0) or (self._root.flags & 512 != 0)) :
                pass
                self._debug['compressed_checksum']['start'] = self._io.pos()
                self.compressed_checksum = self._io.read_u4be()
                self._debug['compressed_checksum']['end'] = self._io.pos()

            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_compressed)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            if  ((self._root.flags & 1 != 0) or (self._root.flags & 256 != 0)) :
                pass

            if  ((self._root.flags & 2 != 0) or (self._root.flags & 512 != 0)) :
                pass



    class Terminator(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(Lzop.Terminator, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    @property
    def lzop_version(self):
        if hasattr(self, '_m_lzop_version'):
            return self._m_lzop_version

        self._m_lzop_version = self.version & 240
        return getattr(self, '_m_lzop_version', None)


