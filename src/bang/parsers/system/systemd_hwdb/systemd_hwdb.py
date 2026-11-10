# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SystemdHwdb(KaitaiStruct):
    SEQ_FIELDS = ["header", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SystemdHwdb, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = SystemdHwdb.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self._raw_data = self._io.read_bytes(self.header.len_file - self.len_header)
        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
        self.data = SystemdHwdb.Dummy(_io__raw_data, self, self._root)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.data._fetch_instances()
        _ = self.root_node
        if hasattr(self, '_m_root_node'):
            pass
            self._m_root_node._fetch_instances()


    class ChildNode(KaitaiStruct):
        SEQ_FIELDS = ["index", "padding", "ofs_child"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SystemdHwdb.ChildNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['index']['start'] = self._io.pos()
            self.index = self._io.read_u1()
            self._debug['index']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(7)
            self._debug['padding']['end'] = self._io.pos()
            self._debug['ofs_child']['start'] = self._io.pos()
            self.ofs_child = self._io.read_u8le()
            self._debug['ofs_child']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.child
            if hasattr(self, '_m_child'):
                pass
                self._m_child._fetch_instances()


        @property
        def child(self):
            if hasattr(self, '_m_child'):
                return self._m_child

            io = self._root.data._io
            _pos = io.pos()
            io.seek(self.ofs_child - self._root.len_header)
            self._debug['_m_child']['start'] = io.pos()
            self._m_child = SystemdHwdb.TrieNode(io, self, self._root)
            self._debug['_m_child']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_child', None)


    class Dummy(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(SystemdHwdb.Dummy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["signature", "tool_version", "len_file", "len_header", "len_node", "len_child_entry", "len_value_entry", "ofs_nodes_root", "len_nodes", "len_strings"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SystemdHwdb.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(8)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x4B\x53\x4C\x50\x48\x48\x52\x48":
                raise kaitaistruct.ValidationNotEqualError(b"\x4B\x53\x4C\x50\x48\x48\x52\x48", self.signature, self._io, u"/types/header/seq/0")
            self._debug['tool_version']['start'] = self._io.pos()
            self.tool_version = self._io.read_u8le()
            self._debug['tool_version']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u8le()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u8le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['len_node']['start'] = self._io.pos()
            self.len_node = self._io.read_u8le()
            self._debug['len_node']['end'] = self._io.pos()
            self._debug['len_child_entry']['start'] = self._io.pos()
            self.len_child_entry = self._io.read_u8le()
            self._debug['len_child_entry']['end'] = self._io.pos()
            self._debug['len_value_entry']['start'] = self._io.pos()
            self.len_value_entry = self._io.read_u8le()
            self._debug['len_value_entry']['end'] = self._io.pos()
            if not  ((self.len_value_entry == 16) or (self.len_value_entry == 32)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.len_value_entry, self._io, u"/types/header/seq/6")
            self._debug['ofs_nodes_root']['start'] = self._io.pos()
            self.ofs_nodes_root = self._io.read_u8le()
            self._debug['ofs_nodes_root']['end'] = self._io.pos()
            self._debug['len_nodes']['start'] = self._io.pos()
            self.len_nodes = self._io.read_u8le()
            self._debug['len_nodes']['end'] = self._io.pos()
            self._debug['len_strings']['start'] = self._io.pos()
            self.len_strings = self._io.read_u8le()
            self._debug['len_strings']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class TrieNode(KaitaiStruct):
        SEQ_FIELDS = ["ofs_prefix", "num_children", "padding", "num_values", "children_entries", "value_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SystemdHwdb.TrieNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_prefix']['start'] = self._io.pos()
            self.ofs_prefix = self._io.read_u8le()
            self._debug['ofs_prefix']['end'] = self._io.pos()
            self._debug['num_children']['start'] = self._io.pos()
            self.num_children = self._io.read_u1()
            self._debug['num_children']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(7)
            self._debug['padding']['end'] = self._io.pos()
            self._debug['num_values']['start'] = self._io.pos()
            self.num_values = self._io.read_u8le()
            self._debug['num_values']['end'] = self._io.pos()
            self._debug['children_entries']['start'] = self._io.pos()
            self._debug['children_entries']['arr'] = []
            self._raw_children_entries = []
            self.children_entries = []
            for i in range(self.num_children):
                self._debug['children_entries']['arr'].append({'start': self._io.pos()})
                self._raw_children_entries.append(self._io.read_bytes(self._root.header.len_child_entry))
                _io__raw_children_entries = KaitaiStream(BytesIO(self._raw_children_entries[i]))
                self.children_entries.append(SystemdHwdb.ChildNode(_io__raw_children_entries, self, self._root))
                self._debug['children_entries']['arr'][i]['end'] = self._io.pos()

            self._debug['children_entries']['end'] = self._io.pos()
            self._debug['value_entries']['start'] = self._io.pos()
            self._debug['value_entries']['arr'] = []
            self.value_entries = []
            for i in range(self.num_values):
                self._debug['value_entries']['arr'].append({'start': self._io.pos()})
                _on = self._root.is_value_entry_v2
                if _on == False:
                    pass
                    self.value_entries.append(SystemdHwdb.ValueEntry(self._io, self, self._root))
                elif _on == True:
                    pass
                    self.value_entries.append(SystemdHwdb.ValueEntry2(self._io, self, self._root))
                self._debug['value_entries']['arr'][i]['end'] = self._io.pos()

            self._debug['value_entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.children_entries)):
                pass
                self.children_entries[i]._fetch_instances()

            for i in range(len(self.value_entries)):
                pass
                _on = self._root.is_value_entry_v2
                if _on == False:
                    pass
                    self.value_entries[i]._fetch_instances()
                elif _on == True:
                    pass
                    self.value_entries[i]._fetch_instances()



    class ValueEntry(KaitaiStruct):
        SEQ_FIELDS = ["ofs_key", "ofs_value"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SystemdHwdb.ValueEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_key']['start'] = self._io.pos()
            self.ofs_key = self._io.read_u8le()
            self._debug['ofs_key']['end'] = self._io.pos()
            self._debug['ofs_value']['start'] = self._io.pos()
            self.ofs_value = self._io.read_u8le()
            self._debug['ofs_value']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.key
            if hasattr(self, '_m_key'):
                pass

            _ = self.value
            if hasattr(self, '_m_value'):
                pass


        @property
        def key(self):
            if hasattr(self, '_m_key'):
                return self._m_key

            io = self._root.data._io
            _pos = io.pos()
            io.seek(self.ofs_key - self._root.len_header)
            self._debug['_m_key']['start'] = io.pos()
            self._m_key = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['_m_key']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_key', None)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            io = self._root.data._io
            _pos = io.pos()
            io.seek(self.ofs_value - self._root.len_header)
            self._debug['_m_value']['start'] = io.pos()
            self._m_value = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['_m_value']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_value', None)


    class ValueEntry2(KaitaiStruct):
        SEQ_FIELDS = ["ofs_key", "ofs_value", "ofs_filename", "line_number", "file_priority", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SystemdHwdb.ValueEntry2, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_key']['start'] = self._io.pos()
            self.ofs_key = self._io.read_u8le()
            self._debug['ofs_key']['end'] = self._io.pos()
            self._debug['ofs_value']['start'] = self._io.pos()
            self.ofs_value = self._io.read_u8le()
            self._debug['ofs_value']['end'] = self._io.pos()
            self._debug['ofs_filename']['start'] = self._io.pos()
            self.ofs_filename = self._io.read_u8le()
            self._debug['ofs_filename']['end'] = self._io.pos()
            self._debug['line_number']['start'] = self._io.pos()
            self.line_number = self._io.read_u4le()
            self._debug['line_number']['end'] = self._io.pos()
            self._debug['file_priority']['start'] = self._io.pos()
            self.file_priority = self._io.read_u2le()
            self._debug['file_priority']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(2)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.filename
            if hasattr(self, '_m_filename'):
                pass

            _ = self.key
            if hasattr(self, '_m_key'):
                pass

            _ = self.value
            if hasattr(self, '_m_value'):
                pass


        @property
        def filename(self):
            if hasattr(self, '_m_filename'):
                return self._m_filename

            io = self._root.data._io
            _pos = io.pos()
            io.seek(self.ofs_filename - self._root.len_header)
            self._debug['_m_filename']['start'] = io.pos()
            self._m_filename = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['_m_filename']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_filename', None)

        @property
        def key(self):
            if hasattr(self, '_m_key'):
                return self._m_key

            io = self._root.data._io
            _pos = io.pos()
            io.seek(self.ofs_key - self._root.len_header)
            self._debug['_m_key']['start'] = io.pos()
            self._m_key = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['_m_key']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_key', None)

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            io = self._root.data._io
            _pos = io.pos()
            io.seek(self.ofs_value - self._root.len_header)
            self._debug['_m_value']['start'] = io.pos()
            self._m_value = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['_m_value']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_value', None)


    @property
    def is_value_entry_v2(self):
        if hasattr(self, '_m_is_value_entry_v2'):
            return self._m_is_value_entry_v2

        self._m_is_value_entry_v2 = self.header.len_value_entry == 32
        return getattr(self, '_m_is_value_entry_v2', None)

    @property
    def len_header(self):
        if hasattr(self, '_m_len_header'):
            return self._m_len_header

        self._m_len_header = 80
        return getattr(self, '_m_len_header', None)

    @property
    def root_node(self):
        if hasattr(self, '_m_root_node'):
            return self._m_root_node

        io = self.data._io
        _pos = io.pos()
        io.seek(self.header.ofs_nodes_root - self.len_header)
        self._debug['_m_root_node']['start'] = io.pos()
        self._m_root_node = SystemdHwdb.TrieNode(io, self, self._root)
        self._debug['_m_root_node']['end'] = io.pos()
        io.seek(_pos)
        return getattr(self, '_m_root_node', None)


