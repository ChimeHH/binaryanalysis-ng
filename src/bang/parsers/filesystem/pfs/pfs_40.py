# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Pfs40(KaitaiStruct):
    """
    .. seealso::
       Source - http://web.archive.org/web/20140107233423/http://www.cba.si/pfs/_README
    """
    SEQ_FIELDS = ["header", "entries"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Pfs40, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Pfs40.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['entries']['start'] = self._io.pos()
        self.entries = Pfs40.Entries(self._io, self, self._root)
        self._debug['entries']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.entries._fetch_instances()
        _ = self.files
        if hasattr(self, '_m_files'):
            pass
            for i in range(len(self._m_files)):
                pass
                self._m_files[i]._fetch_instances()



    class Data(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, index, root_pos, _io, _parent=None, _root=None):
            super(Pfs40.Data, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.index = index
            self.root_pos = root_pos
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.data
            if hasattr(self, '_m_data'):
                pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            _pos = self._io.pos()
            self._io.seek(self.pos)
            self._debug['_m_data']['start'] = self._io.pos()
            self._m_data = self._io.read_bytes(self._root.entries.entries[self.index].len_file)
            self._debug['_m_data']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_data', None)

        @property
        def name(self):
            if hasattr(self, '_m_name'):
                return self._m_name

            self._m_name = self._root.entries.entries[self.index].name
            return getattr(self, '_m_name', None)

        @property
        def pos(self):
            if hasattr(self, '_m_pos'):
                return self._m_pos

            self._m_pos = self._root.entries.entries[self.index].ofs_file + self.root_pos
            return getattr(self, '_m_pos', None)


    class Entries(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pfs40.Entries, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self._root.header.num_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Pfs40.Entry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["name", "unknown", "ofs_file", "len_file"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pfs40.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(40), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(4)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['ofs_file']['start'] = self._io.pos()
            self.ofs_file = self._io.read_u4le()
            self._debug['ofs_file']['end'] = self._io.pos()
            if not self.ofs_file <= self._root._io.size():
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size(), self.ofs_file, self._io, u"/types/entry/seq/2")
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()
            if not self.len_file <= self._root._io.size() - self.ofs_file:
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size() - self.ofs_file, self.len_file, self._io, u"/types/entry/seq/3")


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "padding", "num_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pfs40.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x50\x46\x53\x2F\x30\x2E\x39\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x50\x46\x53\x2F\x30\x2E\x39\x00", self.magic, self._io, u"/types/header/seq/0")
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(6)
            self._debug['padding']['end'] = self._io.pos()
            if not self.padding == b"\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00", self.padding, self._io, u"/types/header/seq/1")
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u2le()
            self._debug['num_entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def files(self):
        if hasattr(self, '_m_files'):
            return self._m_files

        self._debug['_m_files']['start'] = self._io.pos()
        self._debug['_m_files']['arr'] = []
        self._m_files = []
        for i in range(self.header.num_entries):
            self._debug['_m_files']['arr'].append({'start': self._io.pos()})
            self._m_files.append(Pfs40.Data(i, self._io.pos(), self._io, self, self._root))
            self._debug['_m_files']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_files']['end'] = self._io.pos()
        return getattr(self, '_m_files', None)


