# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class AndroidUpdate(KaitaiStruct):
    """Format of payload.bin OTA update files. The payload is in Google Protobuf
    format. The structure of the payload data depend on the contents of the
    manifest. Parsing currently has to be done outside of Kaitai Struct.
    
    .. seealso::
       Source - https://android.googlesource.com/platform/system/update_engine/+/refs/heads/main/README.md#Update-Payload-File-Specification
    
    
    .. seealso::
       Source - https://android.googlesource.com/platform/system/update_engine/+/refs/heads/main/update_metadata.proto
    """
    SEQ_FIELDS = ["magic", "major_version", "len_manifest", "len_manifest_signature", "manifest", "manifest_signature"]
    def __init__(self, _io, _parent=None, _root=None):
        super(AndroidUpdate, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x43\x72\x41\x55":
            raise kaitaistruct.ValidationNotEqualError(b"\x43\x72\x41\x55", self.magic, self._io, u"/seq/0")
        self._debug['major_version']['start'] = self._io.pos()
        self.major_version = self._io.read_u8be()
        self._debug['major_version']['end'] = self._io.pos()
        if not  ((self.major_version == 2)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.major_version, self._io, u"/seq/1")
        self._debug['len_manifest']['start'] = self._io.pos()
        self.len_manifest = self._io.read_u8be()
        self._debug['len_manifest']['end'] = self._io.pos()
        if self.major_version == 2:
            pass
            self._debug['len_manifest_signature']['start'] = self._io.pos()
            self.len_manifest_signature = self._io.read_u4be()
            self._debug['len_manifest_signature']['end'] = self._io.pos()

        self._debug['manifest']['start'] = self._io.pos()
        self.manifest = self._io.read_bytes(self.len_manifest)
        self._debug['manifest']['end'] = self._io.pos()
        self._debug['manifest_signature']['start'] = self._io.pos()
        self.manifest_signature = self._io.read_bytes(self.len_manifest_signature)
        self._debug['manifest_signature']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        if self.major_version == 2:
            pass



