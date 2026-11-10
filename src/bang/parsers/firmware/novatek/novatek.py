# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Novatek(KaitaiStruct):
    """An incomplete parser for firmware files for Novatek chipset based
    devices (dashcams, etc.). The file format seems to be somewhat based
    on the BCL library, although it seems there were modifications.
    
    Only LZ77 compression seems to be used.
    
    .. seealso::
       Source - https://web.archive.org/web/20210516004049/https://limkopi.me/analysing-sj4000s-firmware/
    """

    class CompressionMethod(IntEnum):
        rle = 1
        huffman = 2
        rice8 = 3
        rice16 = 4
        rice32 = 5
        rice8signed = 6
        rice16signed = 7
        rice32signed = 8
        lz77 = 9
        shannonfano = 10
    SEQ_FIELDS = ["magic", "unknown", "compression", "len_original", "len_data", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Novatek, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x42\x43\x4C\x31":
            raise kaitaistruct.ValidationNotEqualError(b"\x42\x43\x4C\x31", self.magic, self._io, u"/seq/0")
        self._debug['unknown']['start'] = self._io.pos()
        self.unknown = self._io.read_u2be()
        self._debug['unknown']['end'] = self._io.pos()
        self._debug['compression']['start'] = self._io.pos()
        self.compression = KaitaiStream.resolve_enum(Novatek.CompressionMethod, self._io.read_u2be())
        self._debug['compression']['end'] = self._io.pos()
        if not  ((self.compression == Novatek.CompressionMethod.lz77)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.compression, self._io, u"/seq/2")
        self._debug['len_original']['start'] = self._io.pos()
        self.len_original = self._io.read_u4be()
        self._debug['len_original']['end'] = self._io.pos()
        self._debug['len_data']['start'] = self._io.pos()
        self.len_data = self._io.read_u4be()
        self._debug['len_data']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self.data = self._io.read_bytes(self.len_data)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass


