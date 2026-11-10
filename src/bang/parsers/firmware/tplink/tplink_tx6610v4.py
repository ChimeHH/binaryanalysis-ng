# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class TplinkTx6610v4(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/alexandernst/TPLink-TX6610-firmware-tools
    """
    SEQ_FIELDS = ["header", "kernel", "padding", "rootfs", "padding2", "trailer"]
    def __init__(self, _io, _parent=None, _root=None):
        super(TplinkTx6610v4, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = TplinkTx6610v4.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['kernel']['start'] = self._io.pos()
        self.kernel = self._io.read_bytes(self.header.rest_of_header.len_kernel)
        self._debug['kernel']['end'] = self._io.pos()
        self._debug['padding']['start'] = self._io.pos()
        self.padding = self._io.read_bytes((1376256 - self.header.rest_of_header.len_kernel) - self.header.len_header)
        self._debug['padding']['end'] = self._io.pos()
        self._debug['rootfs']['start'] = self._io.pos()
        self.rootfs = self._io.read_bytes(self.header.rest_of_header.len_rootfs)
        self._debug['rootfs']['end'] = self._io.pos()
        self._debug['padding2']['start'] = self._io.pos()
        self.padding2 = self._io.read_bytes(self.header.rest_of_header.len_file - (1376256 + self.header.rest_of_header.len_rootfs))
        self._debug['padding2']['end'] = self._io.pos()
        self._debug['trailer']['start'] = self._io.pos()
        self.trailer = self._io.read_bytes(232)
        self._debug['trailer']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_header", "rest_of_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(TplinkTx6610v4.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x32\x52\x44\x48":
                raise kaitaistruct.ValidationNotEqualError(b"\x32\x52\x44\x48", self.magic, self._io, u"/types/header/seq/0")
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4be()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['rest_of_header']['start'] = self._io.pos()
            self._raw_rest_of_header = self._io.read_bytes((self.len_header - 4) - 4)
            _io__raw_rest_of_header = KaitaiStream(BytesIO(self._raw_rest_of_header))
            self.rest_of_header = TplinkTx6610v4.RestOfHeader(_io__raw_rest_of_header, self, self._root)
            self._debug['rest_of_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.rest_of_header._fetch_instances()


    class RestOfHeader(KaitaiStruct):
        SEQ_FIELDS = ["len_file", "crc32", "name", "customer_version", "len_kernel", "len_rootfs", "len_ctrom", "model", "unknown", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(TplinkTx6610v4.RestOfHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4be()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4be()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['customer_version']['start'] = self._io.pos()
            self.customer_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['customer_version']['end'] = self._io.pos()
            self._debug['len_kernel']['start'] = self._io.pos()
            self.len_kernel = self._io.read_u4be()
            self._debug['len_kernel']['end'] = self._io.pos()
            self._debug['len_rootfs']['start'] = self._io.pos()
            self.len_rootfs = self._io.read_u4be()
            self._debug['len_rootfs']['end'] = self._io.pos()
            if not self.len_rootfs <= self.len_file - 1376256:
                raise kaitaistruct.ValidationGreaterThanError(self.len_file - 1376256, self.len_rootfs, self._io, u"/types/rest_of_header/seq/5")
            self._debug['len_ctrom']['start'] = self._io.pos()
            self.len_ctrom = self._io.read_u4be()
            self._debug['len_ctrom']['end'] = self._io.pos()
            self._debug['model']['start'] = self._io.pos()
            self.model = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['model']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(4)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes_full()
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



