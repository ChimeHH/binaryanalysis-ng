# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Fls(KaitaiStruct):
    """Test files:
    - https://www.nvripc.com/new-chinese-ip-camera-firmwares-update/
    - https://www.herospeed.net/hs/ipc_test/fuhan/
    """
    SEQ_FIELDS = ["header", "entries", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Fls, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Fls.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['entries']['start'] = self._io.pos()
        self._debug['entries']['arr'] = []
        self.entries = []
        for i in range(self.header.num_entries):
            self._debug['entries']['arr'].append({'start': self._io.pos()})
            self.entries.append(Fls.Entry(self._io, self, self._root))
            self._debug['entries']['arr'][i]['end'] = self._io.pos()

        self._debug['entries']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self._raw_data = self._io.read_bytes(self.header.len_file - self.ofs_data)
        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
        self.data = Fls.Dummy(_io__raw_data, self, self._root)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.entries)):
            pass
            self.entries[i]._fetch_instances()

        self.data._fetch_instances()

    class Dummy(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(Fls.Dummy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["name", "len_data", "ofs_data", "unknown"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Fls.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(128), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['ofs_data']['start'] = self._io.pos()
            self.ofs_data = self._io.read_u4le()
            self._debug['ofs_data']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(120)
            self._debug['unknown']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.data
            if hasattr(self, '_m_data'):
                pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            io = self._root.data._io
            _pos = io.pos()
            io.seek(self.ofs_data - self._root.ofs_data)
            self._debug['_m_data']['start'] = io.pos()
            self._m_data = io.read_bytes(self.len_data)
            self._debug['_m_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_data', None)


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["model", "submodel", "len_file", "num_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Fls.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['model']['start'] = self._io.pos()
            self.model = (KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)).decode(u"UTF-8")
            self._debug['model']['end'] = self._io.pos()
            self._debug['submodel']['start'] = self._io.pos()
            self.submodel = (KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)).decode(u"UTF-8")
            self._debug['submodel']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u4le()
            self._debug['num_entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def ofs_data(self):
        if hasattr(self, '_m_ofs_data'):
            return self._m_ofs_data

        self._m_ofs_data = 24 + self.header.num_entries * 256
        return getattr(self, '_m_ofs_data', None)


