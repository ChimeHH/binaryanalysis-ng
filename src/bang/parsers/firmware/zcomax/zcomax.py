# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Zcomax(KaitaiStruct):
    """
    .. seealso::
       Source - https://raw.githubusercontent.com/openwrt/openwrt/f705008d7e696/tools/firmware-utils/src/mkzcfw.c
    """
    SEQ_FIELDS = ["header", "firmware_body", "tail"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Zcomax, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Zcomax.Header(1836214630, self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['firmware_body']['start'] = self._io.pos()
        self._raw_firmware_body = self._io.read_bytes(self.header.len_body - 8)
        _io__raw_firmware_body = KaitaiStream(BytesIO(self._raw_firmware_body))
        self.firmware_body = Zcomax.FirmwareBody(_io__raw_firmware_body, self, self._root)
        self._debug['firmware_body']['end'] = self._io.pos()
        self._debug['tail']['start'] = self._io.pos()
        self.tail = Zcomax.Tail(self._io, self, self._root)
        self._debug['tail']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.firmware_body._fetch_instances()
        self.tail._fetch_instances()

    class FirmwareBody(KaitaiStruct):
        SEQ_FIELDS = ["kernel", "rootfs"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zcomax.FirmwareBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['kernel']['start'] = self._io.pos()
            self.kernel = Zcomax.Kernel(self._io, self, self._root)
            self._debug['kernel']['end'] = self._io.pos()
            self._debug['rootfs']['start'] = self._io.pos()
            self.rootfs = Zcomax.Rootfs(self._io, self, self._root)
            self._debug['rootfs']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.kernel._fetch_instances()
            self.rootfs._fetch_instances()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_body", "unknown"]
        def __init__(self, valid_contents, _io, _parent=None, _root=None):
            super(Zcomax.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.valid_contents = valid_contents
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_u4le()
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == self.valid_contents:
                raise kaitaistruct.ValidationNotEqualError(self.valid_contents, self.magic, self._io, u"/types/header/seq/0")
            self._debug['len_body']['start'] = self._io.pos()
            self.len_body = self._io.read_u4le()
            self._debug['len_body']['end'] = self._io.pos()
            if not self.len_body <= 104857600:
                raise kaitaistruct.ValidationGreaterThanError(104857600, self.len_body, self._io, u"/types/header/seq/1")
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(8)
            self._debug['unknown']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Kernel(KaitaiStruct):
        SEQ_FIELDS = ["header", "body", "tail"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zcomax.Kernel, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Zcomax.Header(1735223627, self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self.body = self._io.read_bytes(self.header.len_body - 8)
            self._debug['body']['end'] = self._io.pos()
            self._debug['tail']['start'] = self._io.pos()
            self.tail = Zcomax.Tail(self._io, self, self._root)
            self._debug['tail']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.tail._fetch_instances()


    class Rootfs(KaitaiStruct):
        SEQ_FIELDS = ["header", "body", "tail"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zcomax.Rootfs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Zcomax.Header(1735223634, self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self.body = self._io.read_bytes(self.header.len_body - 8)
            self._debug['body']['end'] = self._io.pos()
            self._debug['tail']['start'] = self._io.pos()
            self.tail = Zcomax.Tail(self._io, self, self._root)
            self._debug['tail']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.tail._fetch_instances()


    class Tail(KaitaiStruct):
        SEQ_FIELDS = ["hardware_identifier", "crc"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zcomax.Tail, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['hardware_identifier']['start'] = self._io.pos()
            self.hardware_identifier = self._io.read_u4le()
            self._debug['hardware_identifier']['end'] = self._io.pos()
            self._debug['crc']['start'] = self._io.pos()
            self.crc = self._io.read_u4le()
            self._debug['crc']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



