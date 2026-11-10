# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import vfat_directory_rec
from .vfat_directory_rec import *
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class VfatDirectory(KaitaiStruct):
    SEQ_FIELDS = ["records"]
    def __init__(self, _io, _parent=None, _root=None):
        super(VfatDirectory, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['records']['start'] = self._io.pos()
        self._debug['records']['arr'] = []
        self._raw_records = []
        self.records = []
        i = 0
        while not self._io.is_eof():
            self._debug['records']['arr'].append({'start': self._io.pos()})
            self._raw_records.append(self._io.read_bytes(32))
            _io__raw_records = KaitaiStream(BytesIO(self._raw_records[-1]))
            self.records.append(vfat_directory_rec.VfatDirectoryRec(_io__raw_records))
            self._debug['records']['arr'][len(self.records) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['records']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.records)):
            pass
            self.records[i]._fetch_instances()



