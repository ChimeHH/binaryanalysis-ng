# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Winhelp(KaitaiStruct):
    """
    .. seealso::
       Source - http://www.oocities.org/mwinterhoff/helpfile.htm
    """

    class FormatVersion(IntEnum):
        windows_30 = 15
        windows_31 = 21
        media_view = 27
        windows_95 = 33

    class SystemRecordTypes(IntEnum):
        title = 1
        copyright = 2
        contents = 3
        config = 4
        icon = 5
        window = 6
        language_id = 9
        charset = 11
    SEQ_FIELDS = ["magic", "ofs_internal_directory", "ofs_first_free_block", "len_file"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Winhelp, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x3F\x5F\x03\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x3F\x5F\x03\x00", self.magic, self._io, u"/seq/0")
        self._debug['ofs_internal_directory']['start'] = self._io.pos()
        self.ofs_internal_directory = self._io.read_u4le()
        self._debug['ofs_internal_directory']['end'] = self._io.pos()
        self._debug['ofs_first_free_block']['start'] = self._io.pos()
        self.ofs_first_free_block = self._io.read_s4le()
        self._debug['ofs_first_free_block']['end'] = self._io.pos()
        self._debug['len_file']['start'] = self._io.pos()
        self.len_file = self._io.read_u4le()
        self._debug['len_file']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _ = self.internal_directory
        if hasattr(self, '_m_internal_directory'):
            pass
            self._m_internal_directory._fetch_instances()


    class BTree(KaitaiStruct):
        SEQ_FIELDS = ["magic", "flags", "page_size", "structure", "zero", "page_splits", "root_page", "negative_one", "num_pages", "num_levels", "num_entries", "pages", "leaf_page"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Winhelp.BTree, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x3B\x29":
                raise kaitaistruct.ValidationNotEqualError(b"\x3B\x29", self.magic, self._io, u"/types/b_tree/seq/0")
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['page_size']['start'] = self._io.pos()
            self.page_size = self._io.read_u2le()
            self._debug['page_size']['end'] = self._io.pos()
            self._debug['structure']['start'] = self._io.pos()
            self.structure = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"ASCII")
            self._debug['structure']['end'] = self._io.pos()
            self._debug['zero']['start'] = self._io.pos()
            self.zero = self._io.read_u2le()
            self._debug['zero']['end'] = self._io.pos()
            if not self.zero == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.zero, self._io, u"/types/b_tree/seq/4")
            self._debug['page_splits']['start'] = self._io.pos()
            self.page_splits = self._io.read_u2le()
            self._debug['page_splits']['end'] = self._io.pos()
            self._debug['root_page']['start'] = self._io.pos()
            self.root_page = self._io.read_u2le()
            self._debug['root_page']['end'] = self._io.pos()
            self._debug['negative_one']['start'] = self._io.pos()
            self.negative_one = self._io.read_s2le()
            self._debug['negative_one']['end'] = self._io.pos()
            if not self.negative_one == -1:
                raise kaitaistruct.ValidationNotEqualError(-1, self.negative_one, self._io, u"/types/b_tree/seq/7")
            self._debug['num_pages']['start'] = self._io.pos()
            self.num_pages = self._io.read_u2le()
            self._debug['num_pages']['end'] = self._io.pos()
            self._debug['num_levels']['start'] = self._io.pos()
            self.num_levels = self._io.read_u2le()
            self._debug['num_levels']['end'] = self._io.pos()
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u4le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['pages']['start'] = self._io.pos()
            self._debug['pages']['arr'] = []
            self.pages = []
            for i in range(self.num_pages - 1):
                self._debug['pages']['arr'].append({'start': self._io.pos()})
                self.pages.append(self._io.read_bytes(self.page_size))
                self._debug['pages']['arr'][i]['end'] = self._io.pos()

            self._debug['pages']['end'] = self._io.pos()
            self._debug['leaf_page']['start'] = self._io.pos()
            self._raw_leaf_page = self._io.read_bytes(self.page_size)
            _io__raw_leaf_page = KaitaiStream(BytesIO(self._raw_leaf_page))
            self.leaf_page = Winhelp.LeafPage(_io__raw_leaf_page, self, self._root)
            self._debug['leaf_page']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.pages)):
                pass

            self.leaf_page._fetch_instances()


    class Ctxomap(KaitaiStruct):
        SEQ_FIELDS = ["num_entries", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Winhelp.Ctxomap, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u2le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Winhelp.Ctxomap.CtxoMapEntry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()


        class CtxoMapEntry(KaitaiStruct):
            SEQ_FIELDS = ["map_id", "ofs_topic"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Winhelp.Ctxomap.CtxoMapEntry, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['map_id']['start'] = self._io.pos()
                self.map_id = self._io.read_u4le()
                self._debug['map_id']['end'] = self._io.pos()
                self._debug['ofs_topic']['start'] = self._io.pos()
                self.ofs_topic = self._io.read_u4le()
                self._debug['ofs_topic']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass



    class FileData(KaitaiStruct):
        SEQ_FIELDS = ["header", "body", "free_space"]
        def __init__(self, filename, _io, _parent=None, _root=None):
            super(Winhelp.FileData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.filename = filename
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Winhelp.FileHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.filename
            if _on == u"|CTXOMAP":
                pass
                self._raw_body = self._io.read_bytes(self.header.len_used_space)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Winhelp.Ctxomap(_io__raw_body, self, self._root)
            elif _on == u"|FONT":
                pass
                self._raw_body = self._io.read_bytes(self.header.len_used_space)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Winhelp.Font(_io__raw_body, self, self._root)
            elif _on == u"|SYSTEM":
                pass
                self._raw_body = self._io.read_bytes(self.header.len_used_space)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Winhelp.System(_io__raw_body, self, self._root)
            else:
                pass
                self.body = self._io.read_bytes(self.header.len_used_space)
            self._debug['body']['end'] = self._io.pos()
            self._debug['free_space']['start'] = self._io.pos()
            self.free_space = self._io.read_bytes((self.header.len_reserved_space - self.header.len_used_space) - 9)
            self._debug['free_space']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            _on = self.filename
            if _on == u"|CTXOMAP":
                pass
                self.body._fetch_instances()
            elif _on == u"|FONT":
                pass
                self.body._fetch_instances()
            elif _on == u"|SYSTEM":
                pass
                self.body._fetch_instances()
            else:
                pass


    class FileHeader(KaitaiStruct):
        SEQ_FIELDS = ["len_reserved_space", "len_used_space", "file_flags"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Winhelp.FileHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_reserved_space']['start'] = self._io.pos()
            self.len_reserved_space = self._io.read_u4le()
            self._debug['len_reserved_space']['end'] = self._io.pos()
            self._debug['len_used_space']['start'] = self._io.pos()
            self.len_used_space = self._io.read_u4le()
            self._debug['len_used_space']['end'] = self._io.pos()
            self._debug['file_flags']['start'] = self._io.pos()
            self.file_flags = self._io.read_u1()
            self._debug['file_flags']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Font(KaitaiStruct):
        SEQ_FIELDS = ["num_face_names", "num_descriptors", "ofs_facenames", "ofs_descriptors", "num_styles", "ofs_styles", "num_char_map_tables", "ofs_char_map_tables"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Winhelp.Font, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_face_names']['start'] = self._io.pos()
            self.num_face_names = self._io.read_u2le()
            self._debug['num_face_names']['end'] = self._io.pos()
            self._debug['num_descriptors']['start'] = self._io.pos()
            self.num_descriptors = self._io.read_u2le()
            self._debug['num_descriptors']['end'] = self._io.pos()
            self._debug['ofs_facenames']['start'] = self._io.pos()
            self.ofs_facenames = self._io.read_u2le()
            self._debug['ofs_facenames']['end'] = self._io.pos()
            self._debug['ofs_descriptors']['start'] = self._io.pos()
            self.ofs_descriptors = self._io.read_u2le()
            self._debug['ofs_descriptors']['end'] = self._io.pos()
            if self.ofs_facenames >= 12:
                pass
                self._debug['num_styles']['start'] = self._io.pos()
                self.num_styles = self._io.read_u2le()
                self._debug['num_styles']['end'] = self._io.pos()

            if self.ofs_facenames >= 12:
                pass
                self._debug['ofs_styles']['start'] = self._io.pos()
                self.ofs_styles = self._io.read_u2le()
                self._debug['ofs_styles']['end'] = self._io.pos()

            if self.ofs_facenames >= 16:
                pass
                self._debug['num_char_map_tables']['start'] = self._io.pos()
                self.num_char_map_tables = self._io.read_u2le()
                self._debug['num_char_map_tables']['end'] = self._io.pos()

            if self.ofs_facenames >= 16:
                pass
                self._debug['ofs_char_map_tables']['start'] = self._io.pos()
                self.ofs_char_map_tables = self._io.read_u2le()
                self._debug['ofs_char_map_tables']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.ofs_facenames >= 12:
                pass

            if self.ofs_facenames >= 12:
                pass

            if self.ofs_facenames >= 16:
                pass

            if self.ofs_facenames >= 16:
                pass



    class InternalDirectory(KaitaiStruct):
        SEQ_FIELDS = ["header", "contents", "free_space"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Winhelp.InternalDirectory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Winhelp.FileHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['contents']['start'] = self._io.pos()
            self._raw_contents = self._io.read_bytes(self.header.len_used_space)
            _io__raw_contents = KaitaiStream(BytesIO(self._raw_contents))
            self.contents = Winhelp.BTree(_io__raw_contents, self, self._root)
            self._debug['contents']['end'] = self._io.pos()
            self._debug['free_space']['start'] = self._io.pos()
            self.free_space = self._io.read_bytes((self.header.len_reserved_space - self.header.len_used_space) - 9)
            self._debug['free_space']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.contents._fetch_instances()


    class LeafEntry(KaitaiStruct):
        SEQ_FIELDS = ["filename", "ofs_fileheader"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Winhelp.LeafEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['filename']['start'] = self._io.pos()
            self.filename = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['filename']['end'] = self._io.pos()
            self._debug['ofs_fileheader']['start'] = self._io.pos()
            self.ofs_fileheader = self._io.read_u4le()
            self._debug['ofs_fileheader']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.file
            if hasattr(self, '_m_file'):
                pass
                self._m_file._fetch_instances()


        @property
        def file(self):
            if hasattr(self, '_m_file'):
                return self._m_file

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_fileheader)
            self._debug['_m_file']['start'] = io.pos()
            self._m_file = Winhelp.FileData(self.filename, io, self, self._root)
            self._debug['_m_file']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_file', None)


    class LeafPage(KaitaiStruct):
        SEQ_FIELDS = ["num_unused", "num_entries", "previous_leaf_page", "next_leaf_page", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Winhelp.LeafPage, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_unused']['start'] = self._io.pos()
            self.num_unused = self._io.read_u2le()
            self._debug['num_unused']['end'] = self._io.pos()
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u2le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['previous_leaf_page']['start'] = self._io.pos()
            self.previous_leaf_page = self._io.read_s2le()
            self._debug['previous_leaf_page']['end'] = self._io.pos()
            self._debug['next_leaf_page']['start'] = self._io.pos()
            self.next_leaf_page = self._io.read_s2le()
            self._debug['next_leaf_page']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Winhelp.LeafEntry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class System(KaitaiStruct):
        SEQ_FIELDS = ["magic", "minor", "major", "date", "flags", "system_records"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Winhelp.System, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x6C\x03":
                raise kaitaistruct.ValidationNotEqualError(b"\x6C\x03", self.magic, self._io, u"/types/system/seq/0")
            self._debug['minor']['start'] = self._io.pos()
            self.minor = KaitaiStream.resolve_enum(Winhelp.FormatVersion, self._io.read_u2le())
            self._debug['minor']['end'] = self._io.pos()
            if not  ((self.minor == Winhelp.FormatVersion.windows_31)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.minor, self._io, u"/types/system/seq/1")
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u2le()
            self._debug['major']['end'] = self._io.pos()
            if not self.major == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.major, self._io, u"/types/system/seq/2")
            self._debug['date']['start'] = self._io.pos()
            self.date = self._io.read_u4le()
            self._debug['date']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['system_records']['start'] = self._io.pos()
            self._debug['system_records']['arr'] = []
            self.system_records = []
            i = 0
            while not self._io.is_eof():
                self._debug['system_records']['arr'].append({'start': self._io.pos()})
                self.system_records.append(Winhelp.System.SystemRecord(self._io, self, self._root))
                self._debug['system_records']['arr'][len(self.system_records) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['system_records']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.system_records)):
                pass
                self.system_records[i]._fetch_instances()


        class SystemRecord(KaitaiStruct):
            SEQ_FIELDS = ["record_type", "len_data", "data"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Winhelp.System.SystemRecord, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['record_type']['start'] = self._io.pos()
                self.record_type = KaitaiStream.resolve_enum(Winhelp.SystemRecordTypes, self._io.read_u2le())
                self._debug['record_type']['end'] = self._io.pos()
                self._debug['len_data']['start'] = self._io.pos()
                self.len_data = self._io.read_u2le()
                self._debug['len_data']['end'] = self._io.pos()
                self._debug['data']['start'] = self._io.pos()
                _on = self.record_type
                if _on == Winhelp.SystemRecordTypes.config:
                    pass
                    self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_data), 0, False)).decode(u"ASCII")
                elif _on == Winhelp.SystemRecordTypes.copyright:
                    pass
                    self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_data), 0, False)).decode(u"ASCII")
                elif _on == Winhelp.SystemRecordTypes.title:
                    pass
                    self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_data), 0, False)).decode(u"ASCII")
                elif _on == Winhelp.SystemRecordTypes.window:
                    pass
                    self._raw_data = self._io.read_bytes(self.len_data)
                    _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                    self.data = Winhelp.System.Window(_io__raw_data, self, self._root)
                else:
                    pass
                    self.data = self._io.read_bytes(self.len_data)
                self._debug['data']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _on = self.record_type
                if _on == Winhelp.SystemRecordTypes.config:
                    pass
                elif _on == Winhelp.SystemRecordTypes.copyright:
                    pass
                elif _on == Winhelp.SystemRecordTypes.title:
                    pass
                elif _on == Winhelp.SystemRecordTypes.window:
                    pass
                    self.data._fetch_instances()
                else:
                    pass


        class Window(KaitaiStruct):
            SEQ_FIELDS = ["flags", "window_type", "name", "caption", "x_coordinate", "y_coordinate", "width", "height", "maximize"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Winhelp.System.Window, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['flags']['start'] = self._io.pos()
                self.flags = self._io.read_u2le()
                self._debug['flags']['end'] = self._io.pos()
                self._debug['window_type']['start'] = self._io.pos()
                self.window_type = self._io.read_bytes(10)
                self._debug['window_type']['end'] = self._io.pos()
                self._debug['name']['start'] = self._io.pos()
                self.name = self._io.read_bytes(9)
                self._debug['name']['end'] = self._io.pos()
                self._debug['caption']['start'] = self._io.pos()
                self.caption = self._io.read_bytes(51)
                self._debug['caption']['end'] = self._io.pos()
                self._debug['x_coordinate']['start'] = self._io.pos()
                self.x_coordinate = self._io.read_u2le()
                self._debug['x_coordinate']['end'] = self._io.pos()
                self._debug['y_coordinate']['start'] = self._io.pos()
                self.y_coordinate = self._io.read_u2le()
                self._debug['y_coordinate']['end'] = self._io.pos()
                self._debug['width']['start'] = self._io.pos()
                self.width = self._io.read_u2le()
                self._debug['width']['end'] = self._io.pos()
                self._debug['height']['start'] = self._io.pos()
                self.height = self._io.read_u2le()
                self._debug['height']['end'] = self._io.pos()
                self._debug['maximize']['start'] = self._io.pos()
                self.maximize = self._io.read_u2le()
                self._debug['maximize']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass



    @property
    def internal_directory(self):
        if hasattr(self, '_m_internal_directory'):
            return self._m_internal_directory

        _pos = self._io.pos()
        self._io.seek(self.ofs_internal_directory)
        self._debug['_m_internal_directory']['start'] = self._io.pos()
        self._m_internal_directory = Winhelp.InternalDirectory(self._io, self, self._root)
        self._debug['_m_internal_directory']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_internal_directory', None)


