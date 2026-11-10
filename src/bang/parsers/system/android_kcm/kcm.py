# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Kcm(KaitaiStruct):
    """
    .. seealso::
       Source - https://android.googlesource.com/platform/build/+/android-2.3.5_r1/tools/kcm/kcm.cpp#212
    """

    class KeyboardType(IntEnum):
        numeric = 1
        q14 = 2
        qwerty = 3
    SEQ_FIELDS = ["magic", "endian_marker", "version", "num_keys", "keyboard_type", "padding", "keys"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Kcm, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(8)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x6B\x65\x79\x63\x68\x61\x72\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x6B\x65\x79\x63\x68\x61\x72\x00", self.magic, self._io, u"/seq/0")
        self._debug['endian_marker']['start'] = self._io.pos()
        self.endian_marker = self._io.read_u4le()
        self._debug['endian_marker']['end'] = self._io.pos()
        if not self.endian_marker == 305419896:
            raise kaitaistruct.ValidationNotEqualError(305419896, self.endian_marker, self._io, u"/seq/1")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        if not self.version == 2:
            raise kaitaistruct.ValidationNotEqualError(2, self.version, self._io, u"/seq/2")
        self._debug['num_keys']['start'] = self._io.pos()
        self.num_keys = self._io.read_u4le()
        self._debug['num_keys']['end'] = self._io.pos()
        self._debug['keyboard_type']['start'] = self._io.pos()
        self.keyboard_type = KaitaiStream.resolve_enum(Kcm.KeyboardType, self._io.read_u1())
        self._debug['keyboard_type']['end'] = self._io.pos()
        if not  ((self.keyboard_type == Kcm.KeyboardType.numeric) or (self.keyboard_type == Kcm.KeyboardType.q14) or (self.keyboard_type == Kcm.KeyboardType.qwerty)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.keyboard_type, self._io, u"/seq/4")
        self._debug['padding']['start'] = self._io.pos()
        self.padding = self._io.read_bytes(11)
        self._debug['padding']['end'] = self._io.pos()
        self._debug['keys']['start'] = self._io.pos()
        self._debug['keys']['arr'] = []
        self.keys = []
        for i in range(self.num_keys):
            self._debug['keys']['arr'].append({'start': self._io.pos()})
            self.keys.append(Kcm.Key(self._io, self, self._root))
            self._debug['keys']['arr'][i]['end'] = self._io.pos()

        self._debug['keys']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.keys)):
            pass
            self.keys[i]._fetch_instances()


    class Key(KaitaiStruct):
        SEQ_FIELDS = ["keycode", "columns"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Kcm.Key, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['keycode']['start'] = self._io.pos()
            self.keycode = self._io.read_u4le()
            self._debug['keycode']['end'] = self._io.pos()
            self._debug['columns']['start'] = self._io.pos()
            self.columns = self._io.read_bytes(12)
            self._debug['columns']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



