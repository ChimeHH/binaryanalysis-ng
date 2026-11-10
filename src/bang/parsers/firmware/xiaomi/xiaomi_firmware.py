# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class XiaomiFirmware(KaitaiStruct):
    """Test files: https://miuirom.org/miwifi/xiaomi-router-ax9000
    
    .. seealso::
       Source - https://lxr.openwrt.org/source/firmware-utils/src/xiaomifw.c
    
    
    .. seealso::
       Source - https://forum.openwrt.org/t/openwrt-support-for-xiaomi-ax9000/98908/251
    """

    class BlobType(IntEnum):
        uboot = 1
        fw_uimage = 4
        fw_os2 = 6
        fw_uimage2 = 7

    class DeviceIds(IntEnum):
        r1cm = 3
        r2d = 4
        r1cl = 5
        r3 = 7
        r3d = 8
        r3g = 13
        r4cm = 18
        r2100 = 22
        ra70 = 37

    class Magic(IntEnum):
        header_1 = 827475016
        header_2 = 844252232
    SEQ_FIELDS = ["header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(XiaomiFirmware, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = XiaomiFirmware.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Blob(KaitaiStruct):
        SEQ_FIELDS = ["magic", "ofs_flash", "len_data", "blob_type", "unused", "name", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(XiaomiFirmware.Blob, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\xBE\xBA\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\xBE\xBA\x00\x00", self.magic, self._io, u"/types/blob/seq/0")
            self._debug['ofs_flash']['start'] = self._io.pos()
            self.ofs_flash = self._io.read_u4le()
            self._debug['ofs_flash']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['blob_type']['start'] = self._io.pos()
            self.blob_type = KaitaiStream.resolve_enum(XiaomiFirmware.BlobType, self._io.read_u2le())
            self._debug['blob_type']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_u2le()
            self._debug['unused']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class BlobOffset(KaitaiStruct):
        SEQ_FIELDS = ["ofs_blob"]
        def __init__(self, _io, _parent=None, _root=None):
            super(XiaomiFirmware.BlobOffset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_blob']['start'] = self._io.pos()
            self.ofs_blob = self._io.read_u4le()
            self._debug['ofs_blob']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.blob
            if hasattr(self, '_m_blob'):
                pass
                self._m_blob._fetch_instances()


        @property
        def blob(self):
            if hasattr(self, '_m_blob'):
                return self._m_blob

            if self.ofs_blob != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_blob)
                self._debug['_m_blob']['start'] = io.pos()
                self._m_blob = XiaomiFirmware.Blob(io, self, self._root)
                self._debug['_m_blob']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_blob', None)


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "ofs_signature", "crc32", "unused", "rest_of_header", "ofs_blobs"]
        def __init__(self, _io, _parent=None, _root=None):
            super(XiaomiFirmware.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = KaitaiStream.resolve_enum(XiaomiFirmware.Magic, self._io.read_u4le())
            self._debug['magic']['end'] = self._io.pos()
            if not  ((self.magic == XiaomiFirmware.Magic.header_1) or (self.magic == XiaomiFirmware.Magic.header_2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.magic, self._io, u"/types/header/seq/0")
            self._debug['ofs_signature']['start'] = self._io.pos()
            self.ofs_signature = self._io.read_u4le()
            self._debug['ofs_signature']['end'] = self._io.pos()
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_bytes(2)
            self._debug['unused']['end'] = self._io.pos()
            if not self.unused == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.unused, self._io, u"/types/header/seq/3")
            self._debug['rest_of_header']['start'] = self._io.pos()
            _on = self.magic
            if _on == XiaomiFirmware.Magic.header_1:
                pass
                self.rest_of_header = XiaomiFirmware.RestOfHeader1(self._io, self, self._root)
            elif _on == XiaomiFirmware.Magic.header_2:
                pass
                self.rest_of_header = XiaomiFirmware.RestOfHeader2(self._io, self, self._root)
            self._debug['rest_of_header']['end'] = self._io.pos()
            self._debug['ofs_blobs']['start'] = self._io.pos()
            self._debug['ofs_blobs']['arr'] = []
            self.ofs_blobs = []
            for i in range(8):
                self._debug['ofs_blobs']['arr'].append({'start': self._io.pos()})
                self.ofs_blobs.append(XiaomiFirmware.BlobOffset(self._io, self, self._root))
                self._debug['ofs_blobs']['arr'][i]['end'] = self._io.pos()

            self._debug['ofs_blobs']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.magic
            if _on == XiaomiFirmware.Magic.header_1:
                pass
                self.rest_of_header._fetch_instances()
            elif _on == XiaomiFirmware.Magic.header_2:
                pass
                self.rest_of_header._fetch_instances()
            for i in range(len(self.ofs_blobs)):
                pass
                self.ofs_blobs[i]._fetch_instances()

            _ = self.signature
            if hasattr(self, '_m_signature'):
                pass
                self._m_signature._fetch_instances()


        @property
        def signature(self):
            if hasattr(self, '_m_signature'):
                return self._m_signature

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_signature)
            self._debug['_m_signature']['start'] = io.pos()
            self._m_signature = XiaomiFirmware.Signature(io, self, self._root)
            self._debug['_m_signature']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_signature', None)


    class RestOfHeader1(KaitaiStruct):
        SEQ_FIELDS = ["device_id"]
        def __init__(self, _io, _parent=None, _root=None):
            super(XiaomiFirmware.RestOfHeader1, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['device_id']['start'] = self._io.pos()
            self.device_id = KaitaiStream.resolve_enum(XiaomiFirmware.DeviceIds, self._io.read_u2le())
            self._debug['device_id']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class RestOfHeader2(KaitaiStruct):
        SEQ_FIELDS = ["unused", "device_name", "market", "unknown"]
        def __init__(self, _io, _parent=None, _root=None):
            super(XiaomiFirmware.RestOfHeader2, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_bytes(2)
            self._debug['unused']['end'] = self._io.pos()
            if not self.unused == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.unused, self._io, u"/types/rest_of_header_2/seq/0")
            self._debug['device_name']['start'] = self._io.pos()
            self.device_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)).decode(u"UTF-8")
            self._debug['device_name']['end'] = self._io.pos()
            self._debug['market']['start'] = self._io.pos()
            self.market = (KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)).decode(u"UTF-8")
            self._debug['market']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(16)
            self._debug['unknown']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Signature(KaitaiStruct):
        SEQ_FIELDS = ["len_signature", "padding", "signature"]
        def __init__(self, _io, _parent=None, _root=None):
            super(XiaomiFirmware.Signature, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_signature']['start'] = self._io.pos()
            self.len_signature = self._io.read_u4le()
            self._debug['len_signature']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(12)
            self._debug['padding']['end'] = self._io.pos()
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(self.len_signature)
            self._debug['signature']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



