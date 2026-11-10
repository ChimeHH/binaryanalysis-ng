# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MtkBrlyt(KaitaiStruct):
    """
    .. seealso::
       Source - https://source.denx.de/u-boot/u-boot/-/blob/cadb1a858d071e/tools/mtk_image.h
    
    
    .. seealso::
       Source - https://source.denx.de/u-boot/u-boot/-/blob/cadb1a858d071e/tools/mtk_image.c
    """

    class ImgType(IntEnum):
        invalid = 0
        nand = 65538
        emmc = 65541
        nor = 65543
        sdmmc = 65544
        snand = 65545
    SEQ_FIELDS = ["name", "version", "len_header", "len_total", "magic", "image_type", "len_header_2", "len_total_2", "unused"]
    def __init__(self, _io, _parent=None, _root=None):
        super(MtkBrlyt, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['name']['start'] = self._io.pos()
        self.name = self._io.read_bytes(8)
        self._debug['name']['end'] = self._io.pos()
        if not self.name == b"\x42\x52\x4C\x59\x54\x00\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x42\x52\x4C\x59\x54\x00\x00\x00", self.name, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        self._debug['len_header']['start'] = self._io.pos()
        self.len_header = self._io.read_u4le()
        self._debug['len_header']['end'] = self._io.pos()
        self._debug['len_total']['start'] = self._io.pos()
        self.len_total = self._io.read_u4le()
        self._debug['len_total']['end'] = self._io.pos()
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x42\x42\x42\x42":
            raise kaitaistruct.ValidationNotEqualError(b"\x42\x42\x42\x42", self.magic, self._io, u"/seq/4")
        self._debug['image_type']['start'] = self._io.pos()
        self.image_type = KaitaiStream.resolve_enum(MtkBrlyt.ImgType, self._io.read_u4le())
        self._debug['image_type']['end'] = self._io.pos()
        self._debug['len_header_2']['start'] = self._io.pos()
        self.len_header_2 = self._io.read_u4le()
        self._debug['len_header_2']['end'] = self._io.pos()
        if not self.len_header_2 == self.len_header:
            raise kaitaistruct.ValidationNotEqualError(self.len_header, self.len_header_2, self._io, u"/seq/6")
        self._debug['len_total_2']['start'] = self._io.pos()
        self.len_total_2 = self._io.read_u4le()
        self._debug['len_total_2']['end'] = self._io.pos()
        if not self.len_total_2 == self.len_total:
            raise kaitaistruct.ValidationNotEqualError(self.len_total, self.len_total_2, self._io, u"/seq/7")
        self._debug['unused']['start'] = self._io.pos()
        self.unused = self._io.read_bytes(4)
        self._debug['unused']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass


