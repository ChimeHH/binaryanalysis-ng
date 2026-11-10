# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class VxworksMemfs(KaitaiStruct):
    """
    .. seealso::
       Source - https://blog.quarkslab.com/reverse-engineering-a-vxworks-os-based-router.html
    
    
    .. seealso::
       Source - https://web.archive.org/web/20110831171246/devttys0.com/2011/06/mystery-file-system
    """
    SEQ_FIELDS = ["header", "entries"]
    def __init__(self, _io, _parent=None, _root=None):
        super(VxworksMemfs, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = VxworksMemfs.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['entries']['start'] = self._io.pos()
        self._debug['entries']['arr'] = []
        self.entries = []
        for i in range(self.header.num_files):
            self._debug['entries']['arr'].append({'start': self._io.pos()})
            self.entries.append(VxworksMemfs.Entry(self._io, self, self._root))
            self._debug['entries']['arr'][i]['end'] = self._io.pos()

        self._debug['entries']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.entries)):
            pass
            self.entries[i]._fetch_instances()


    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["name", "len_data", "ofs_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VxworksMemfs.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(40), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4be()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['ofs_data']['start'] = self._io.pos()
            self.ofs_data = self._io.read_u4be()
            self._debug['ofs_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.data
            if hasattr(self, '_m_data'):
                pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_data)
            self._debug['_m_data']['start'] = io.pos()
            self._m_data = io.read_bytes(self.len_data)
            self._debug['_m_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_data', None)


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "num_files", "data_2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VxworksMemfs.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(32)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77":
                raise kaitaistruct.ValidationNotEqualError(b"\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77\x6F\x77", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4be()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.version, self._io, u"/types/header/seq/1")
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u4be()
            self._debug['num_files']['end'] = self._io.pos()
            self._debug['data_2']['start'] = self._io.pos()
            self.data_2 = self._io.read_bytes(4)
            self._debug['data_2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



