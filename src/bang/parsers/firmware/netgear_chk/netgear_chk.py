# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class NetgearChk(KaitaiStruct):
    """
    .. seealso::
       Source - https://lxr.openwrt.org/source/firmware-utils/src/mkchkimg.c
    
    
    .. seealso::
       Source - https://github.com/onekey-sec/unblob/blob/5d9fd6d8/unblob/handlers/archive/netgear/chk.py
    """

    class RegionCodes(IntEnum):
        worldwide = 1
        north_america = 2
    SEQ_FIELDS = ["header", "kernel", "rootfs"]
    def __init__(self, _io, _parent=None, _root=None):
        super(NetgearChk, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = NetgearChk.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['kernel']['start'] = self._io.pos()
        self.kernel = self._io.read_bytes(self.header.rest_of_header.len_kernel)
        self._debug['kernel']['end'] = self._io.pos()
        self._debug['rootfs']['start'] = self._io.pos()
        self.rootfs = self._io.read_bytes(self.header.rest_of_header.len_rootfs)
        self._debug['rootfs']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_header", "rest_of_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(NetgearChk.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x2A\x23\x24\x5E":
                raise kaitaistruct.ValidationNotEqualError(b"\x2A\x23\x24\x5E", self.magic, self._io, u"/types/header/seq/0")
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4be()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['rest_of_header']['start'] = self._io.pos()
            self._raw_rest_of_header = self._io.read_bytes((self.len_header - 4) - 4)
            _io__raw_rest_of_header = KaitaiStream(BytesIO(self._raw_rest_of_header))
            self.rest_of_header = NetgearChk.RestOfHeader(_io__raw_rest_of_header, self, self._root)
            self._debug['rest_of_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.rest_of_header._fetch_instances()


    class RestOfHeader(KaitaiStruct):
        SEQ_FIELDS = ["region_code", "reserved", "kernel_checksum", "rootfs_checksum", "len_kernel", "len_rootfs", "image_checksum", "header_checksum", "board_id"]
        def __init__(self, _io, _parent=None, _root=None):
            super(NetgearChk.RestOfHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['region_code']['start'] = self._io.pos()
            self.region_code = KaitaiStream.resolve_enum(NetgearChk.RegionCodes, self._io.read_u1())
            self._debug['region_code']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(7)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['kernel_checksum']['start'] = self._io.pos()
            self.kernel_checksum = self._io.read_u4be()
            self._debug['kernel_checksum']['end'] = self._io.pos()
            self._debug['rootfs_checksum']['start'] = self._io.pos()
            self.rootfs_checksum = self._io.read_u4be()
            self._debug['rootfs_checksum']['end'] = self._io.pos()
            self._debug['len_kernel']['start'] = self._io.pos()
            self.len_kernel = self._io.read_u4be()
            self._debug['len_kernel']['end'] = self._io.pos()
            self._debug['len_rootfs']['start'] = self._io.pos()
            self.len_rootfs = self._io.read_u4be()
            self._debug['len_rootfs']['end'] = self._io.pos()
            self._debug['image_checksum']['start'] = self._io.pos()
            self.image_checksum = self._io.read_u4be()
            self._debug['image_checksum']['end'] = self._io.pos()
            self._debug['header_checksum']['start'] = self._io.pos()
            self.header_checksum = self._io.read_u4be()
            self._debug['header_checksum']['end'] = self._io.pos()
            self._debug['board_id']['start'] = self._io.pos()
            self.board_id = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._debug['board_id']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



