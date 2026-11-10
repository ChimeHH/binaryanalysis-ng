# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Gdfw(KaitaiStruct):
    """
    .. seealso::
       Source - https://granitedevices.com/wiki/Firmware_file_format_(.gdf)
    """

    class TargetDriveTypes(IntEnum):
        argon = 4000
        ion = 11000
        atomi = 14000
    SEQ_FIELDS = ["header", "hostfw", "gcfw", "checksum"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Gdfw, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Gdfw.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['hostfw']['start'] = self._io.pos()
        self.hostfw = self._io.read_bytes(self.header.len_hostfw)
        self._debug['hostfw']['end'] = self._io.pos()
        self._debug['gcfw']['start'] = self._io.pos()
        self.gcfw = self._io.read_bytes(self.header.len_gcfw)
        self._debug['gcfw']['end'] = self._io.pos()
        self._debug['checksum']['start'] = self._io.pos()
        self.checksum = self._io.read_u4le()
        self._debug['checksum']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "target_drive_type", "len_hostfw", "gcfw_len"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Gdfw.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x47\x44\x46\x57":
                raise kaitaistruct.ValidationNotEqualError(b"\x47\x44\x46\x57", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u2le()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 300:
                raise kaitaistruct.ValidationNotEqualError(300, self.version, self._io, u"/types/header/seq/1")
            self._debug['target_drive_type']['start'] = self._io.pos()
            self.target_drive_type = KaitaiStream.resolve_enum(Gdfw.TargetDriveTypes, self._io.read_u2le())
            self._debug['target_drive_type']['end'] = self._io.pos()
            if not  ((self.target_drive_type == Gdfw.TargetDriveTypes.argon) or (self.target_drive_type == Gdfw.TargetDriveTypes.ion) or (self.target_drive_type == Gdfw.TargetDriveTypes.atomi)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.target_drive_type, self._io, u"/types/header/seq/2")
            self._debug['len_hostfw']['start'] = self._io.pos()
            self.len_hostfw = self._io.read_u4le()
            self._debug['len_hostfw']['end'] = self._io.pos()
            self._debug['gcfw_len']['start'] = self._io.pos()
            self.gcfw_len = self._io.read_u4le()
            self._debug['gcfw_len']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def len_gcfw(self):
            if hasattr(self, '_m_len_gcfw'):
                return self._m_len_gcfw

            self._m_len_gcfw = (0 if self.gcfw_len == 4294967295 else self.gcfw_len)
            return getattr(self, '_m_len_gcfw', None)



