# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class QtResource(KaitaiStruct):
    """
    .. seealso::
       <https://github.com/qt/qtbase/blob/5.4/src/tools/rcc/rcc.cpp>
    """
    SEQ_FIELDS = ["header", "data_block", "name_table", "tree"]
    def __init__(self, _io, _parent=None, _root=None):
        super(QtResource, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = QtResource.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['data_block']['start'] = self._io.pos()
        self._raw_data_block = self._io.read_bytes(self.len_data_block)
        _io__raw_data_block = KaitaiStream(BytesIO(self._raw_data_block))
        self.data_block = QtResource.EntryBlock(_io__raw_data_block, self, self._root)
        self._debug['data_block']['end'] = self._io.pos()
        self._debug['name_table']['start'] = self._io.pos()
        self._raw_name_table = self._io.read_bytes(self.len_name_table)
        _io__raw_name_table = KaitaiStream(BytesIO(self._raw_name_table))
        self.name_table = QtResource.NameTable(_io__raw_name_table, self, self._root)
        self._debug['name_table']['end'] = self._io.pos()
        self._debug['tree']['start'] = self._io.pos()
        self._debug['tree']['arr'] = []
        self.tree = []
        for i in range(len(self.data_block.entries) + 1):
            self._debug['tree']['arr'].append({'start': self._io.pos()})
            self.tree.append(QtResource.TreeEntry(self._io, self, self._root))
            self._debug['tree']['arr'][i]['end'] = self._io.pos()

        self._debug['tree']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.data_block._fetch_instances()
        self.name_table._fetch_instances()
        for i in range(len(self.tree)):
            pass
            self.tree[i]._fetch_instances()


    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["len_data", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtResource.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4be()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class EntryBlock(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtResource.EntryBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(QtResource.Entry(self._io, self, self._root))
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "ofs_tree", "ofs_data", "ofs_name_table"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtResource.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x71\x72\x65\x73":
                raise kaitaistruct.ValidationNotEqualError(b"\x71\x72\x65\x73", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4be()
            self._debug['version']['end'] = self._io.pos()
            self._debug['ofs_tree']['start'] = self._io.pos()
            self.ofs_tree = self._io.read_u4be()
            self._debug['ofs_tree']['end'] = self._io.pos()
            self._debug['ofs_data']['start'] = self._io.pos()
            self.ofs_data = self._io.read_u4be()
            self._debug['ofs_data']['end'] = self._io.pos()
            self._debug['ofs_name_table']['start'] = self._io.pos()
            self.ofs_name_table = self._io.read_u4be()
            self._debug['ofs_name_table']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class NameTable(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtResource.NameTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(QtResource.NameTableEntry(self._io, self, self._root))
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class NameTableEntry(KaitaiStruct):
        SEQ_FIELDS = ["len_name", "hash", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtResource.NameTableEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_u2be()
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['hash']['start'] = self._io.pos()
            self.hash = self._io.read_u4be()
            self._debug['hash']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = self._io.read_bytes(self.len_name * 2)
            self._debug['name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class TreeEntry(KaitaiStruct):
        SEQ_FIELDS = ["name_offset", "flags", "num_children", "ofs_first_child"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtResource.TreeEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name_offset']['start'] = self._io.pos()
            self.name_offset = self._io.read_u4be()
            self._debug['name_offset']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['num_children']['start'] = self._io.pos()
            self.num_children = self._io.read_u4be()
            self._debug['num_children']['end'] = self._io.pos()
            self._debug['ofs_first_child']['start'] = self._io.pos()
            self.ofs_first_child = self._io.read_u4be()
            self._debug['ofs_first_child']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def len_data_block(self):
        if hasattr(self, '_m_len_data_block'):
            return self._m_len_data_block

        self._m_len_data_block = (self.header.ofs_tree - self.len_name_table) - 20
        return getattr(self, '_m_len_data_block', None)

    @property
    def len_name_table(self):
        if hasattr(self, '_m_len_name_table'):
            return self._m_len_name_table

        self._m_len_name_table = self.header.ofs_tree - self.header.ofs_name_table
        return getattr(self, '_m_len_name_table', None)


