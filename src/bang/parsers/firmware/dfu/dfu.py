# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Dfu(KaitaiStruct):
    """Device Firmware Upgrade files
    
    Test files: <https://micropython.org/download/espruino_pico/>
    
    .. seealso::
       Source - https://raw.githubusercontent.com/micropython/micropython/247d7e2/tools/pydfu.py
    """
    SEQ_FIELDS = ["magic", "version", "len_dfu", "num_targets", "targets", "device", "product", "vendor", "dfu_version", "ufd", "len_suffix", "checksum"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Dfu, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(5)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x44\x66\x75\x53\x65":
            raise kaitaistruct.ValidationNotEqualError(b"\x44\x66\x75\x53\x65", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u1()
        self._debug['version']['end'] = self._io.pos()
        if not self.version == 1:
            raise kaitaistruct.ValidationNotEqualError(1, self.version, self._io, u"/seq/1")
        self._debug['len_dfu']['start'] = self._io.pos()
        self.len_dfu = self._io.read_u4le()
        self._debug['len_dfu']['end'] = self._io.pos()
        self._debug['num_targets']['start'] = self._io.pos()
        self.num_targets = self._io.read_u1()
        self._debug['num_targets']['end'] = self._io.pos()
        self._debug['targets']['start'] = self._io.pos()
        self._debug['targets']['arr'] = []
        self.targets = []
        for i in range(self.num_targets):
            self._debug['targets']['arr'].append({'start': self._io.pos()})
            self.targets.append(Dfu.Target(self._io, self, self._root))
            self._debug['targets']['arr'][i]['end'] = self._io.pos()

        self._debug['targets']['end'] = self._io.pos()
        self._debug['device']['start'] = self._io.pos()
        self.device = self._io.read_u2le()
        self._debug['device']['end'] = self._io.pos()
        self._debug['product']['start'] = self._io.pos()
        self.product = self._io.read_u2le()
        self._debug['product']['end'] = self._io.pos()
        self._debug['vendor']['start'] = self._io.pos()
        self.vendor = self._io.read_u2le()
        self._debug['vendor']['end'] = self._io.pos()
        self._debug['dfu_version']['start'] = self._io.pos()
        self.dfu_version = self._io.read_u2le()
        self._debug['dfu_version']['end'] = self._io.pos()
        if not self.dfu_version == 282:
            raise kaitaistruct.ValidationNotEqualError(282, self.dfu_version, self._io, u"/seq/8")
        self._debug['ufd']['start'] = self._io.pos()
        self.ufd = self._io.read_bytes(3)
        self._debug['ufd']['end'] = self._io.pos()
        if not self.ufd == b"\x55\x46\x44":
            raise kaitaistruct.ValidationNotEqualError(b"\x55\x46\x44", self.ufd, self._io, u"/seq/9")
        self._debug['len_suffix']['start'] = self._io.pos()
        self.len_suffix = self._io.read_u1()
        self._debug['len_suffix']['end'] = self._io.pos()
        if not self.len_suffix == 16:
            raise kaitaistruct.ValidationNotEqualError(16, self.len_suffix, self._io, u"/seq/10")
        self._debug['checksum']['start'] = self._io.pos()
        self.checksum = self._io.read_u4le()
        self._debug['checksum']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.targets)):
            pass
            self.targets[i]._fetch_instances()


    class Element(KaitaiStruct):
        SEQ_FIELDS = ["address", "len_element", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Dfu.Element, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['address']['start'] = self._io.pos()
            self.address = self._io.read_u4le()
            self._debug['address']['end'] = self._io.pos()
            self._debug['len_element']['start'] = self._io.pos()
            self.len_element = self._io.read_u4le()
            self._debug['len_element']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_element)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Target(KaitaiStruct):
        SEQ_FIELDS = ["signature", "alt_setting", "named", "name", "len_target", "num_elements", "elements"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Dfu.Target, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(6)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x54\x61\x72\x67\x65\x74":
                raise kaitaistruct.ValidationNotEqualError(b"\x54\x61\x72\x67\x65\x74", self.signature, self._io, u"/types/target/seq/0")
            self._debug['alt_setting']['start'] = self._io.pos()
            self.alt_setting = self._io.read_u1()
            self._debug['alt_setting']['end'] = self._io.pos()
            self._debug['named']['start'] = self._io.pos()
            self.named = self._io.read_u4le()
            self._debug['named']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(255), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['len_target']['start'] = self._io.pos()
            self.len_target = self._io.read_u4le()
            self._debug['len_target']['end'] = self._io.pos()
            self._debug['num_elements']['start'] = self._io.pos()
            self.num_elements = self._io.read_u4le()
            self._debug['num_elements']['end'] = self._io.pos()
            self._debug['elements']['start'] = self._io.pos()
            self._debug['elements']['arr'] = []
            self.elements = []
            for i in range(self.num_elements):
                self._debug['elements']['arr'].append({'start': self._io.pos()})
                self.elements.append(Dfu.Element(self._io, self, self._root))
                self._debug['elements']['arr'][i]['end'] = self._io.pos()

            self._debug['elements']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.elements)):
                pass
                self.elements[i]._fetch_instances()




