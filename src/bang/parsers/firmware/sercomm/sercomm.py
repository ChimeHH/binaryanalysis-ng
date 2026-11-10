# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Sercomm(KaitaiStruct):
    """A simple 512 byte header that can be found on devices made by Sercomm,
    an ODM from Taiwan. Examples are several NETGEAR devices, such as the
    NETGEAR DGND4000.
    
    The header does not contain any information about the data that follows
    and only has a one byte checksum.
    
    .. seealso::
       Source - https://raw.githubusercontent.com/openwrt/openwrt/3f5619f259de/tools/firmware-utils/src/mksercommfw.c
    
    
    .. seealso::
       Source - https://raw.githubusercontent.com/ReFirmLabs/binwalk/563a19d5c/src/binwalk/magic/firmware
    """
    SEQ_FIELDS = ["magic", "version", "hardware_id", "hardware_version", "software_version", "magic2", "padding_bytes", "checksum"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Sercomm, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(7)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x73\x45\x72\x43\x6F\x4D\x6D":
            raise kaitaistruct.ValidationNotEqualError(b"\x73\x45\x72\x43\x6F\x4D\x6D", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_bytes(4)
        self._debug['version']['end'] = self._io.pos()
        self._debug['hardware_id']['start'] = self._io.pos()
        self.hardware_id = (KaitaiStream.bytes_terminate(self._io.read_bytes(34), 0, False)).decode(u"ASCII")
        self._debug['hardware_id']['end'] = self._io.pos()
        self._debug['hardware_version']['start'] = self._io.pos()
        self.hardware_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(10), 0, False)).decode(u"ASCII")
        self._debug['hardware_version']['end'] = self._io.pos()
        self._debug['software_version']['start'] = self._io.pos()
        self.software_version = self._io.read_bytes(8)
        self._debug['software_version']['end'] = self._io.pos()
        self._debug['magic2']['start'] = self._io.pos()
        self.magic2 = self._io.read_bytes(7)
        self._debug['magic2']['end'] = self._io.pos()
        if not self.magic2 == b"\x73\x45\x72\x43\x6F\x4D\x6D":
            raise kaitaistruct.ValidationNotEqualError(b"\x73\x45\x72\x43\x6F\x4D\x6D", self.magic2, self._io, u"/seq/5")
        self._debug['padding_bytes']['start'] = self._io.pos()
        self._debug['padding_bytes']['arr'] = []
        self.padding_bytes = []
        for i in range(441):
            self._debug['padding_bytes']['arr'].append({'start': self._io.pos()})
            self.padding_bytes.append(Sercomm.PaddingByte(self._io, self, self._root))
            self._debug['padding_bytes']['arr'][i]['end'] = self._io.pos()

        self._debug['padding_bytes']['end'] = self._io.pos()
        self._debug['checksum']['start'] = self._io.pos()
        self.checksum = self._io.read_bytes(1)
        self._debug['checksum']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.padding_bytes)):
            pass
            self.padding_bytes[i]._fetch_instances()


    class PaddingByte(KaitaiStruct):
        SEQ_FIELDS = ["padding_byte"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Sercomm.PaddingByte, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['padding_byte']['start'] = self._io.pos()
            self.padding_byte = self._io.read_bytes(1)
            self._debug['padding_byte']['end'] = self._io.pos()
            if not self.padding_byte == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.padding_byte, self._io, u"/types/padding_byte/seq/0")


        def _fetch_instances(self):
            pass



