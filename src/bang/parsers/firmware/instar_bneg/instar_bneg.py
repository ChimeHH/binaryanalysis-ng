# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class InstarBneg(KaitaiStruct):
    """An old uClinux based firmware format for IP cameras. Test files:
    - https://wiki.instar.com/en/Downloads/Outdoor_Cameras/IN-2905_V2/
    
    .. seealso::
       Source - https://web.archive.org/web/20160404193454/http://wiki.openipcam.com/index.php/Firmware_Structure
    
    
    .. seealso::
       Source - https://github.com/onekey-sec/unblob/blob/5d9fd6d8/unblob/handlers/archive/instar/bneg.py
    """
    SEQ_FIELDS = ["header", "kernel", "rootfs"]
    def __init__(self, _io, _parent=None, _root=None):
        super(InstarBneg, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = InstarBneg.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['kernel']['start'] = self._io.pos()
        self.kernel = self._io.read_bytes(self.header.len_kernel)
        self._debug['kernel']['end'] = self._io.pos()
        self._debug['rootfs']['start'] = self._io.pos()
        self.rootfs = self._io.read_bytes(self.header.len_rootfs)
        self._debug['rootfs']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "major", "minor", "len_kernel", "len_rootfs"]
        def __init__(self, _io, _parent=None, _root=None):
            super(InstarBneg.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x42\x4E\x45\x47":
                raise kaitaistruct.ValidationNotEqualError(b"\x42\x4E\x45\x47", self.magic, self._io, u"/types/header/seq/0")
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u4le()
            self._debug['major']['end'] = self._io.pos()
            if not self.major == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.major, self._io, u"/types/header/seq/1")
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u4le()
            self._debug['minor']['end'] = self._io.pos()
            if not self.minor == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.minor, self._io, u"/types/header/seq/2")
            self._debug['len_kernel']['start'] = self._io.pos()
            self.len_kernel = self._io.read_u4le()
            self._debug['len_kernel']['end'] = self._io.pos()
            self._debug['len_rootfs']['start'] = self._io.pos()
            self.len_rootfs = self._io.read_u4le()
            self._debug['len_rootfs']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



