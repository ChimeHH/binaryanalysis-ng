# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class GitIndex(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/git/git/blob/main/Documentation/technical/index-format.txt
    """

    class GitExtensions(IntEnum):
        end_of_index_entry = 1162824005
        file_system_monitor = 1179864398
        index_entry_offset_table = 1229279060
        resolve_undo = 1380275523
        cache_tree = 1414677829
        untracked_cache = 1431196754
        split_index = 1818848875
        sparse_directory_entries = 1935960434

    class ObjectTypeMode(IntEnum):
        regular = 8
        symbolic_link = 10
        gitlink = 14
    SEQ_FIELDS = ["header", "entries", "extensions", "checksum"]
    def __init__(self, _io, _parent=None, _root=None):
        super(GitIndex, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = GitIndex.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['entries']['start'] = self._io.pos()
        self._debug['entries']['arr'] = []
        self.entries = []
        for i in range(self.header.num_entries):
            self._debug['entries']['arr'].append({'start': self._io.pos()})
            self.entries.append(GitIndex.Entry(self._io, self, self._root))
            self._debug['entries']['arr'][i]['end'] = self._io.pos()

        self._debug['entries']['end'] = self._io.pos()
        self._debug['extensions']['start'] = self._io.pos()
        self._debug['extensions']['arr'] = []
        self.extensions = []
        i = 0
        while True:
            self._debug['extensions']['arr'].append({'start': self._io.pos()})
            _ = GitIndex.Extension(self._io, self, self._root)
            self.extensions.append(_)
            self._debug['extensions']['arr'][len(self.extensions) - 1]['end'] = self._io.pos()
            if self._io.pos() >= self._io.size() - self.len_hash:
                break
            i += 1
        self._debug['extensions']['end'] = self._io.pos()
        self._debug['checksum']['start'] = self._io.pos()
        self.checksum = self._io.read_bytes(self.len_hash)
        self._debug['checksum']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.entries)):
            pass
            self.entries[i]._fetch_instances()

        for i in range(len(self.extensions)):
            pass
            self.extensions[i]._fetch_instances()


    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["entry", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GitIndex.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entry']['start'] = self._io.pos()
            self.entry = GitIndex.EntryBody(self._io, self, self._root)
            self._debug['entry']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(self.padding_needed)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.entry._fetch_instances()

        @property
        def padding_needed(self):
            if hasattr(self, '_m_padding_needed'):
                return self._m_padding_needed

            self._m_padding_needed = (8 if (self._io.pos() - 12) % 8 == 0 else -(self._io.pos() - 12) % 8)
            return getattr(self, '_m_padding_needed', None)


    class EntryBody(KaitaiStruct):
        SEQ_FIELDS = ["ctime_seconds", "ctime_nanoseconds", "mtime_seconds", "mtime_nanoseconds", "dev", "inode", "mode", "uid", "gid", "file_size", "object_name", "name_flag", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GitIndex.EntryBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ctime_seconds']['start'] = self._io.pos()
            self.ctime_seconds = self._io.read_u4be()
            self._debug['ctime_seconds']['end'] = self._io.pos()
            self._debug['ctime_nanoseconds']['start'] = self._io.pos()
            self.ctime_nanoseconds = self._io.read_u4be()
            self._debug['ctime_nanoseconds']['end'] = self._io.pos()
            self._debug['mtime_seconds']['start'] = self._io.pos()
            self.mtime_seconds = self._io.read_u4be()
            self._debug['mtime_seconds']['end'] = self._io.pos()
            self._debug['mtime_nanoseconds']['start'] = self._io.pos()
            self.mtime_nanoseconds = self._io.read_u4be()
            self._debug['mtime_nanoseconds']['end'] = self._io.pos()
            self._debug['dev']['start'] = self._io.pos()
            self.dev = self._io.read_u4be()
            self._debug['dev']['end'] = self._io.pos()
            self._debug['inode']['start'] = self._io.pos()
            self.inode = self._io.read_u4be()
            self._debug['inode']['end'] = self._io.pos()
            self._debug['mode']['start'] = self._io.pos()
            self._raw_mode = self._io.read_bytes(4)
            _io__raw_mode = KaitaiStream(BytesIO(self._raw_mode))
            self.mode = GitIndex.Mode(_io__raw_mode, self, self._root)
            self._debug['mode']['end'] = self._io.pos()
            self._debug['uid']['start'] = self._io.pos()
            self.uid = self._io.read_u4be()
            self._debug['uid']['end'] = self._io.pos()
            self._debug['gid']['start'] = self._io.pos()
            self.gid = self._io.read_u4be()
            self._debug['gid']['end'] = self._io.pos()
            self._debug['file_size']['start'] = self._io.pos()
            self.file_size = self._io.read_u4be()
            self._debug['file_size']['end'] = self._io.pos()
            self._debug['object_name']['start'] = self._io.pos()
            self.object_name = self._io.read_bytes(self._root.len_hash)
            self._debug['object_name']['end'] = self._io.pos()
            self._debug['name_flag']['start'] = self._io.pos()
            self.name_flag = GitIndex.NameFlag(self._io, self, self._root)
            self._debug['name_flag']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(self.name_flag.len_name)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.mode._fetch_instances()
            self.name_flag._fetch_instances()


    class Extension(KaitaiStruct):
        SEQ_FIELDS = ["signature", "len_extension_data", "extension_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GitIndex.Extension, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = KaitaiStream.resolve_enum(GitIndex.GitExtensions, self._io.read_u4be())
            self._debug['signature']['end'] = self._io.pos()
            if not  ((self.signature == GitIndex.GitExtensions.cache_tree) or (self.signature == GitIndex.GitExtensions.resolve_undo) or (self.signature == GitIndex.GitExtensions.split_index) or (self.signature == GitIndex.GitExtensions.untracked_cache) or (self.signature == GitIndex.GitExtensions.file_system_monitor) or (self.signature == GitIndex.GitExtensions.end_of_index_entry) or (self.signature == GitIndex.GitExtensions.index_entry_offset_table) or (self.signature == GitIndex.GitExtensions.sparse_directory_entries)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.signature, self._io, u"/types/extension/seq/0")
            self._debug['len_extension_data']['start'] = self._io.pos()
            self.len_extension_data = self._io.read_u4be()
            self._debug['len_extension_data']['end'] = self._io.pos()
            self._debug['extension_data']['start'] = self._io.pos()
            _on = self.signature
            if _on == GitIndex.GitExtensions.cache_tree:
                pass
                self._raw_extension_data = self._io.read_bytes(self.len_extension_data)
                _io__raw_extension_data = KaitaiStream(BytesIO(self._raw_extension_data))
                self.extension_data = GitIndex.Tree(_io__raw_extension_data, self, self._root)
            else:
                pass
                self.extension_data = self._io.read_bytes(self.len_extension_data)
            self._debug['extension_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.signature
            if _on == GitIndex.GitExtensions.cache_tree:
                pass
                self.extension_data._fetch_instances()
            else:
                pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "num_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GitIndex.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x44\x49\x52\x43":
                raise kaitaistruct.ValidationNotEqualError(b"\x44\x49\x52\x43", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4be()
            self._debug['version']['end'] = self._io.pos()
            if not  ((self.version == 2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/types/header/seq/1")
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u4be()
            self._debug['num_entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Mode(KaitaiStruct):
        SEQ_FIELDS = ["unused", "object_type", "unused1", "permissions"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GitIndex.Mode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_bits_int_be(16)
            self._debug['unused']['end'] = self._io.pos()
            self._debug['object_type']['start'] = self._io.pos()
            self.object_type = KaitaiStream.resolve_enum(GitIndex.ObjectTypeMode, self._io.read_bits_int_be(4))
            self._debug['object_type']['end'] = self._io.pos()
            if not  ((self.object_type == GitIndex.ObjectTypeMode.regular) or (self.object_type == GitIndex.ObjectTypeMode.symbolic_link) or (self.object_type == GitIndex.ObjectTypeMode.gitlink)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.object_type, self._io, u"/types/mode/seq/1")
            self._debug['unused1']['start'] = self._io.pos()
            self.unused1 = self._io.read_bits_int_be(3)
            self._debug['unused1']['end'] = self._io.pos()
            if not self.unused1 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.unused1, self._io, u"/types/mode/seq/2")
            self._debug['permissions']['start'] = self._io.pos()
            self.permissions = self._io.read_bits_int_be(9)
            self._debug['permissions']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class NameFlag(KaitaiStruct):
        SEQ_FIELDS = ["assume_valid", "extended_flag", "stage", "len_name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GitIndex.NameFlag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['assume_valid']['start'] = self._io.pos()
            self.assume_valid = self._io.read_bits_int_be(1) != 0
            self._debug['assume_valid']['end'] = self._io.pos()
            self._debug['extended_flag']['start'] = self._io.pos()
            self.extended_flag = self._io.read_bits_int_be(1) != 0
            self._debug['extended_flag']['end'] = self._io.pos()
            self._debug['stage']['start'] = self._io.pos()
            self.stage = self._io.read_bits_int_be(2)
            self._debug['stage']['end'] = self._io.pos()
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_bits_int_be(12)
            self._debug['len_name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Tree(KaitaiStruct):
        SEQ_FIELDS = ["tree_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GitIndex.Tree, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tree_entries']['start'] = self._io.pos()
            self._debug['tree_entries']['arr'] = []
            self.tree_entries = []
            i = 0
            while not self._io.is_eof():
                self._debug['tree_entries']['arr'].append({'start': self._io.pos()})
                self.tree_entries.append(GitIndex.TreeEntry(self._io, self, self._root))
                self._debug['tree_entries']['arr'][len(self.tree_entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['tree_entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.tree_entries)):
                pass
                self.tree_entries[i]._fetch_instances()



    class TreeEntry(KaitaiStruct):
        SEQ_FIELDS = ["path_component", "num_entries", "num_subtries", "object_name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GitIndex.TreeEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['path_component']['start'] = self._io.pos()
            self.path_component = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['path_component']['end'] = self._io.pos()
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = (self._io.read_bytes_term(32, False, True, True)).decode(u"UTF-8")
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['num_subtries']['start'] = self._io.pos()
            self.num_subtries = (self._io.read_bytes_term(10, False, True, True)).decode(u"UTF-8")
            self._debug['num_subtries']['end'] = self._io.pos()
            self._debug['object_name']['start'] = self._io.pos()
            self.object_name = self._io.read_bytes(self._root.len_hash)
            self._debug['object_name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def len_hash(self):
        if hasattr(self, '_m_len_hash'):
            return self._m_len_hash

        self._m_len_hash = 20
        return getattr(self, '_m_len_hash', None)


