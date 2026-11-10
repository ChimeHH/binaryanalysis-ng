# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SamsungTzar(KaitaiStruct):
    """
    .. seealso::
       Source - https://gist.github.com/astarasikov/f47cb7f46b5193872f376fa0ea842e4b
    """
    SEQ_FIELDS = ["header", "entries"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SamsungTzar, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = SamsungTzar.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['entries']['start'] = self._io.pos()
        self._raw_entries = self._io.read_bytes(self.header.tzar_len - 16)
        _io__raw_entries = KaitaiStream(BytesIO(self._raw_entries))
        self.entries = SamsungTzar.Entries(_io__raw_entries, self, self._root)
        self._debug['entries']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.entries._fetch_instances()

    class Entries(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SamsungTzar.Entries, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self._root.header.num_files):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(SamsungTzar.Entry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["len_filename", "len_data", "filename", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SamsungTzar.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_filename']['start'] = self._io.pos()
            self.len_filename = self._io.read_u4le()
            self._debug['len_filename']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['filename']['start'] = self._io.pos()
            self.filename = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_filename), 0, False)).decode(u"UTF-8")
            self._debug['filename']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "tzar_count", "tzar_len", "num_files"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SamsungTzar.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x7F\xA5\x54\x41":
                raise kaitaistruct.ValidationNotEqualError(b"\x7F\xA5\x54\x41", self.magic, self._io, u"/types/header/seq/0")
            self._debug['tzar_count']['start'] = self._io.pos()
            self.tzar_count = self._io.read_u4le()
            self._debug['tzar_count']['end'] = self._io.pos()
            self._debug['tzar_len']['start'] = self._io.pos()
            self.tzar_len = self._io.read_u4le()
            self._debug['tzar_len']['end'] = self._io.pos()
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u4le()
            self._debug['num_files']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



