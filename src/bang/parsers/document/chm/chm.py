# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Chm(KaitaiStruct):
    """
    .. seealso::
       Source - http://www.russotto.net/chm/chmformat.html
    
    
    .. seealso::
       Source - https://www.nongnu.org/chmspec/latest/
    """

    class ChunkMagic(IntEnum):
        index = 1229409616
        listing = 1279741264
    SEQ_FIELDS = ["header", "header_section_table"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Chm, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Chm.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['header_section_table']['start'] = self._io.pos()
        self._raw_header_section_table = self._io.read_bytes(self.header.len_header - 56)
        _io__raw_header_section_table = KaitaiStream(BytesIO(self._raw_header_section_table))
        self.header_section_table = Chm.HeaderSectionTable(_io__raw_header_section_table, self, self._root)
        self._debug['header_section_table']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.header_section_table._fetch_instances()
        _ = self.content
        if hasattr(self, '_m_content'):
            pass

        _ = self.header0
        if hasattr(self, '_m_header0'):
            pass
            self._m_header0._fetch_instances()

        _ = self.header1
        if hasattr(self, '_m_header1'):
            pass
            self._m_header1._fetch_instances()


    class DirectoryChunk(KaitaiStruct):
        SEQ_FIELDS = ["magic", "directory_chunk_body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Chm.DirectoryChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = KaitaiStream.resolve_enum(Chm.ChunkMagic, self._io.read_u4le())
            self._debug['magic']['end'] = self._io.pos()
            self._debug['directory_chunk_body']['start'] = self._io.pos()
            _on = self.magic
            if _on == Chm.ChunkMagic.listing:
                pass
                self.directory_chunk_body = Chm.Listing(self._io, self, self._root)
            self._debug['directory_chunk_body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.magic
            if _on == Chm.ChunkMagic.listing:
                pass
                self.directory_chunk_body._fetch_instances()


    class EntriesAndQuickref(KaitaiStruct):
        SEQ_FIELDS = ["entry_quickref"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Chm.EntriesAndQuickref, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entry_quickref']['start'] = self._io.pos()
            self.entry_quickref = self._io.read_bytes_full()
            self._debug['entry_quickref']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "len_header", "unknown1", "timestamp", "windows_language_id", "guid1", "guid2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Chm.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x49\x54\x53\x46":
                raise kaitaistruct.ValidationNotEqualError(b"\x49\x54\x53\x46", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 3:
                raise kaitaistruct.ValidationNotEqualError(3, self.version, self._io, u"/types/header/seq/1")
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u4le()
            self._debug['unknown1']['end'] = self._io.pos()
            if not self.unknown1 == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.unknown1, self._io, u"/types/header/seq/3")
            self._debug['timestamp']['start'] = self._io.pos()
            self.timestamp = self._io.read_u4le()
            self._debug['timestamp']['end'] = self._io.pos()
            self._debug['windows_language_id']['start'] = self._io.pos()
            self.windows_language_id = self._io.read_u4le()
            self._debug['windows_language_id']['end'] = self._io.pos()
            self._debug['guid1']['start'] = self._io.pos()
            self.guid1 = self._io.read_bytes(16)
            self._debug['guid1']['end'] = self._io.pos()
            self._debug['guid2']['start'] = self._io.pos()
            self.guid2 = self._io.read_bytes(16)
            self._debug['guid2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header0(KaitaiStruct):
        SEQ_FIELDS = ["unknown1", "unknown2", "len_file", "unknown3", "unknown4"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Chm.Header0, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u4le()
            self._debug['unknown1']['end'] = self._io.pos()
            if not self.unknown1 == 510:
                raise kaitaistruct.ValidationNotEqualError(510, self.unknown1, self._io, u"/types/header0/seq/0")
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_u4le()
            self._debug['unknown2']['end'] = self._io.pos()
            if not self.unknown2 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.unknown2, self._io, u"/types/header0/seq/1")
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u8le()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['unknown3']['start'] = self._io.pos()
            self.unknown3 = self._io.read_u4le()
            self._debug['unknown3']['end'] = self._io.pos()
            if not self.unknown3 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.unknown3, self._io, u"/types/header0/seq/3")
            self._debug['unknown4']['start'] = self._io.pos()
            self.unknown4 = self._io.read_u4le()
            self._debug['unknown4']['end'] = self._io.pos()
            if not self.unknown4 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.unknown4, self._io, u"/types/header0/seq/4")


        def _fetch_instances(self):
            pass


    class Header1(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "len_directory_header", "unknown1", "len_directory_chunk", "density", "index_tree_depth", "root_index_chunk_number", "first_pmgl_chunk", "last_pmgl_chunk", "unknown2", "num_directory_chunks", "windows_language_id", "guid", "len_directory_header2", "unknown3", "unknown4", "unknown5", "directory_chunks"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Chm.Header1, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x49\x54\x53\x50":
                raise kaitaistruct.ValidationNotEqualError(b"\x49\x54\x53\x50", self.magic, self._io, u"/types/header1/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.version, self._io, u"/types/header1/seq/1")
            self._debug['len_directory_header']['start'] = self._io.pos()
            self.len_directory_header = self._io.read_u4le()
            self._debug['len_directory_header']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u4le()
            self._debug['unknown1']['end'] = self._io.pos()
            if not self.unknown1 == 10:
                raise kaitaistruct.ValidationNotEqualError(10, self.unknown1, self._io, u"/types/header1/seq/3")
            self._debug['len_directory_chunk']['start'] = self._io.pos()
            self.len_directory_chunk = self._io.read_u4le()
            self._debug['len_directory_chunk']['end'] = self._io.pos()
            if not self.len_directory_chunk == 4096:
                raise kaitaistruct.ValidationNotEqualError(4096, self.len_directory_chunk, self._io, u"/types/header1/seq/4")
            self._debug['density']['start'] = self._io.pos()
            self.density = self._io.read_u4le()
            self._debug['density']['end'] = self._io.pos()
            self._debug['index_tree_depth']['start'] = self._io.pos()
            self.index_tree_depth = self._io.read_u4le()
            self._debug['index_tree_depth']['end'] = self._io.pos()
            if not  ((self.index_tree_depth == 1) or (self.index_tree_depth == 2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.index_tree_depth, self._io, u"/types/header1/seq/6")
            self._debug['root_index_chunk_number']['start'] = self._io.pos()
            self.root_index_chunk_number = self._io.read_s4le()
            self._debug['root_index_chunk_number']['end'] = self._io.pos()
            self._debug['first_pmgl_chunk']['start'] = self._io.pos()
            self.first_pmgl_chunk = self._io.read_u4le()
            self._debug['first_pmgl_chunk']['end'] = self._io.pos()
            self._debug['last_pmgl_chunk']['start'] = self._io.pos()
            self.last_pmgl_chunk = self._io.read_u4le()
            self._debug['last_pmgl_chunk']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_s4le()
            self._debug['unknown2']['end'] = self._io.pos()
            if not self.unknown2 == -1:
                raise kaitaistruct.ValidationNotEqualError(-1, self.unknown2, self._io, u"/types/header1/seq/10")
            self._debug['num_directory_chunks']['start'] = self._io.pos()
            self.num_directory_chunks = self._io.read_u4le()
            self._debug['num_directory_chunks']['end'] = self._io.pos()
            self._debug['windows_language_id']['start'] = self._io.pos()
            self.windows_language_id = self._io.read_u4le()
            self._debug['windows_language_id']['end'] = self._io.pos()
            self._debug['guid']['start'] = self._io.pos()
            self.guid = self._io.read_bytes(16)
            self._debug['guid']['end'] = self._io.pos()
            self._debug['len_directory_header2']['start'] = self._io.pos()
            self.len_directory_header2 = self._io.read_u4le()
            self._debug['len_directory_header2']['end'] = self._io.pos()
            if not self.len_directory_header2 == 84:
                raise kaitaistruct.ValidationNotEqualError(84, self.len_directory_header2, self._io, u"/types/header1/seq/14")
            self._debug['unknown3']['start'] = self._io.pos()
            self.unknown3 = self._io.read_s4le()
            self._debug['unknown3']['end'] = self._io.pos()
            if not self.unknown3 == -1:
                raise kaitaistruct.ValidationNotEqualError(-1, self.unknown3, self._io, u"/types/header1/seq/15")
            self._debug['unknown4']['start'] = self._io.pos()
            self.unknown4 = self._io.read_s4le()
            self._debug['unknown4']['end'] = self._io.pos()
            if not self.unknown4 == -1:
                raise kaitaistruct.ValidationNotEqualError(-1, self.unknown4, self._io, u"/types/header1/seq/16")
            self._debug['unknown5']['start'] = self._io.pos()
            self.unknown5 = self._io.read_s4le()
            self._debug['unknown5']['end'] = self._io.pos()
            if not self.unknown5 == -1:
                raise kaitaistruct.ValidationNotEqualError(-1, self.unknown5, self._io, u"/types/header1/seq/17")
            self._debug['directory_chunks']['start'] = self._io.pos()
            self._debug['directory_chunks']['arr'] = []
            self._raw_directory_chunks = []
            self.directory_chunks = []
            for i in range(self.num_directory_chunks):
                self._debug['directory_chunks']['arr'].append({'start': self._io.pos()})
                self._raw_directory_chunks.append(self._io.read_bytes(self.len_directory_chunk))
                _io__raw_directory_chunks = KaitaiStream(BytesIO(self._raw_directory_chunks[i]))
                self.directory_chunks.append(Chm.DirectoryChunk(_io__raw_directory_chunks, self, self._root))
                self._debug['directory_chunks']['arr'][i]['end'] = self._io.pos()

            self._debug['directory_chunks']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.directory_chunks)):
                pass
                self.directory_chunks[i]._fetch_instances()



    class HeaderSectionTable(KaitaiStruct):
        SEQ_FIELDS = ["ofs_header0", "len_header0", "ofs_header1", "len_header1", "ofs_content0"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Chm.HeaderSectionTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_header0']['start'] = self._io.pos()
            self.ofs_header0 = self._io.read_u8le()
            self._debug['ofs_header0']['end'] = self._io.pos()
            self._debug['len_header0']['start'] = self._io.pos()
            self.len_header0 = self._io.read_u8le()
            self._debug['len_header0']['end'] = self._io.pos()
            self._debug['ofs_header1']['start'] = self._io.pos()
            self.ofs_header1 = self._io.read_u8le()
            self._debug['ofs_header1']['end'] = self._io.pos()
            self._debug['len_header1']['start'] = self._io.pos()
            self.len_header1 = self._io.read_u8le()
            self._debug['len_header1']['end'] = self._io.pos()
            self._debug['ofs_content0']['start'] = self._io.pos()
            self.ofs_content0 = self._io.read_u8le()
            self._debug['ofs_content0']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Listing(KaitaiStruct):
        SEQ_FIELDS = ["len_quickref", "unknown1", "previous_chunk", "next_chunk", "entries_and_quickref"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Chm.Listing, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_quickref']['start'] = self._io.pos()
            self.len_quickref = self._io.read_u4le()
            self._debug['len_quickref']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u4le()
            self._debug['unknown1']['end'] = self._io.pos()
            if not self.unknown1 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.unknown1, self._io, u"/types/listing/seq/1")
            self._debug['previous_chunk']['start'] = self._io.pos()
            self.previous_chunk = self._io.read_s4le()
            self._debug['previous_chunk']['end'] = self._io.pos()
            self._debug['next_chunk']['start'] = self._io.pos()
            self.next_chunk = self._io.read_s4le()
            self._debug['next_chunk']['end'] = self._io.pos()
            self._debug['entries_and_quickref']['start'] = self._io.pos()
            self._raw_entries_and_quickref = self._io.read_bytes_full()
            _io__raw_entries_and_quickref = KaitaiStream(BytesIO(self._raw_entries_and_quickref))
            self.entries_and_quickref = Chm.EntriesAndQuickref(_io__raw_entries_and_quickref, self, self._root)
            self._debug['entries_and_quickref']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.entries_and_quickref._fetch_instances()


    @property
    def content(self):
        if hasattr(self, '_m_content'):
            return self._m_content

        _pos = self._io.pos()
        self._io.seek(self.header_section_table.ofs_content0)
        self._debug['_m_content']['start'] = self._io.pos()
        self._m_content = self._io.read_bytes(self.filesize - self.header_section_table.ofs_content0)
        self._debug['_m_content']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_content', None)

    @property
    def filesize(self):
        if hasattr(self, '_m_filesize'):
            return self._m_filesize

        self._m_filesize = self.header0.len_file
        return getattr(self, '_m_filesize', None)

    @property
    def header0(self):
        if hasattr(self, '_m_header0'):
            return self._m_header0

        _pos = self._io.pos()
        self._io.seek(self.header_section_table.ofs_header0)
        self._debug['_m_header0']['start'] = self._io.pos()
        self._raw__m_header0 = self._io.read_bytes(self.header_section_table.len_header0)
        _io__raw__m_header0 = KaitaiStream(BytesIO(self._raw__m_header0))
        self._m_header0 = Chm.Header0(_io__raw__m_header0, self, self._root)
        self._debug['_m_header0']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_header0', None)

    @property
    def header1(self):
        if hasattr(self, '_m_header1'):
            return self._m_header1

        _pos = self._io.pos()
        self._io.seek(self.header_section_table.ofs_header1)
        self._debug['_m_header1']['start'] = self._io.pos()
        self._raw__m_header1 = self._io.read_bytes(self.header_section_table.len_header1)
        _io__raw__m_header1 = KaitaiStream(BytesIO(self._raw__m_header1))
        self._m_header1 = Chm.Header1(_io__raw__m_header1, self, self._root)
        self._debug['_m_header1']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_header1', None)


