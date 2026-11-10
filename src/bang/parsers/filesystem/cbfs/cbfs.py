# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Cbfs(KaitaiStruct):
    """
    .. seealso::
       Source - https://www.coreboot.org/CBFS
    """

    class Compression(IntEnum):
        no_compression = 0
        lzma = 1
        nrv2b = 2

    class PayloadTypes(IntEnum):
        stage = 16
        payload = 32
        option_roms = 48
    SEQ_FIELDS = []
    def __init__(self, _io, _parent=None, _root=None):
        super(Cbfs, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        pass


    def _fetch_instances(self):
        pass

    class Component(KaitaiStruct):
        SEQ_FIELDS = ["header", "name", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Cbfs.Component, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Cbfs.ComponentHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.header.offset - 24), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.header.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()


    class ComponentHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_data", "type", "checksum", "offset"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Cbfs.ComponentHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x4C\x41\x52\x43\x48\x49\x56\x45":
                raise kaitaistruct.ValidationNotEqualError(b"\x4C\x41\x52\x43\x48\x49\x56\x45", self.magic, self._io, u"/types/component_header/seq/0")
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4be()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Cbfs.PayloadTypes, self._io.read_u4be())
            self._debug['type']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_u4be()
            self._debug['checksum']['end'] = self._io.pos()
            self._debug['offset']['start'] = self._io.pos()
            self.offset = self._io.read_u4be()
            self._debug['offset']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "len_rom", "len_boot_block", "align", "cbfs_offset", "architecture", "pad"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Cbfs.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x4F\x52\x42\x43":
                raise kaitaistruct.ValidationNotEqualError(b"\x4F\x52\x42\x43", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4be()
            self._debug['version']['end'] = self._io.pos()
            self._debug['len_rom']['start'] = self._io.pos()
            self.len_rom = self._io.read_u4be()
            self._debug['len_rom']['end'] = self._io.pos()
            self._debug['len_boot_block']['start'] = self._io.pos()
            self.len_boot_block = self._io.read_u4be()
            self._debug['len_boot_block']['end'] = self._io.pos()
            self._debug['align']['start'] = self._io.pos()
            self.align = self._io.read_u4be()
            self._debug['align']['end'] = self._io.pos()
            if not self.align == 64:
                raise kaitaistruct.ValidationNotEqualError(64, self.align, self._io, u"/types/header/seq/4")
            self._debug['cbfs_offset']['start'] = self._io.pos()
            self.cbfs_offset = self._io.read_u4be()
            self._debug['cbfs_offset']['end'] = self._io.pos()
            self._debug['architecture']['start'] = self._io.pos()
            self.architecture = self._io.read_u4be()
            self._debug['architecture']['end'] = self._io.pos()
            self._debug['pad']['start'] = self._io.pos()
            self.pad = self._io.read_bytes(4)
            self._debug['pad']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Payload(KaitaiStruct):

        class PayloadSegments(IntEnum):
            bss = 542331714
            params = 1095909712
            data = 1096040772
            code = 1162104643
            entry = 1381256773
        SEQ_FIELDS = ["type", "compression", "offset", "load_addr", "len", "len_mem"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Cbfs.Payload, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Cbfs.Payload.PayloadSegments, self._io.read_u4be())
            self._debug['type']['end'] = self._io.pos()
            self._debug['compression']['start'] = self._io.pos()
            self.compression = KaitaiStream.resolve_enum(Cbfs.Compression, self._io.read_u4be())
            self._debug['compression']['end'] = self._io.pos()
            self._debug['offset']['start'] = self._io.pos()
            self.offset = self._io.read_u4be()
            self._debug['offset']['end'] = self._io.pos()
            self._debug['load_addr']['start'] = self._io.pos()
            self.load_addr = self._io.read_u8be()
            self._debug['load_addr']['end'] = self._io.pos()
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u4be()
            self._debug['len']['end'] = self._io.pos()
            self._debug['len_mem']['start'] = self._io.pos()
            self.len_mem = self._io.read_u4be()
            self._debug['len_mem']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



