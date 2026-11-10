# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Otff(KaitaiStruct):
    """An open type font file collection contains data, in table format, that comprises
    multiple outline fonts.
    
    Test files can be found in google-noto-sans-cjk-ttc-fonts (name of Fedora package)
    
    .. seealso::
       Source - https://docs.microsoft.com/en-us/typography/opentype/spec/otff#collections
    """
    SEQ_FIELDS = ["magic", "version", "num_fonts", "ofs_tables", "dsig_tag", "dsig_length", "ofs_dsig"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Otff, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x74\x74\x63\x66":
            raise kaitaistruct.ValidationNotEqualError(b"\x74\x74\x63\x66", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = Otff.Version(self._io, self, self._root)
        self._debug['version']['end'] = self._io.pos()
        self._debug['num_fonts']['start'] = self._io.pos()
        self.num_fonts = self._io.read_u4be()
        self._debug['num_fonts']['end'] = self._io.pos()
        if not self.num_fonts >= 1:
            raise kaitaistruct.ValidationLessThanError(1, self.num_fonts, self._io, u"/seq/2")
        self._debug['ofs_tables']['start'] = self._io.pos()
        self._debug['ofs_tables']['arr'] = []
        self.ofs_tables = []
        for i in range(self.num_fonts):
            self._debug['ofs_tables']['arr'].append({'start': self._io.pos()})
            self.ofs_tables.append(self._io.read_u4be())
            self._debug['ofs_tables']['arr'][i]['end'] = self._io.pos()

        self._debug['ofs_tables']['end'] = self._io.pos()
        if self.version.major > 1:
            pass
            self._debug['dsig_tag']['start'] = self._io.pos()
            self.dsig_tag = self._io.read_u4be()
            self._debug['dsig_tag']['end'] = self._io.pos()

        if self.version.major > 1:
            pass
            self._debug['dsig_length']['start'] = self._io.pos()
            self.dsig_length = self._io.read_u4be()
            self._debug['dsig_length']['end'] = self._io.pos()

        if self.version.major > 1:
            pass
            self._debug['ofs_dsig']['start'] = self._io.pos()
            self.ofs_dsig = self._io.read_u4be()
            self._debug['ofs_dsig']['end'] = self._io.pos()



    def _fetch_instances(self):
        pass
        self.version._fetch_instances()
        for i in range(len(self.ofs_tables)):
            pass

        if self.version.major > 1:
            pass

        if self.version.major > 1:
            pass

        if self.version.major > 1:
            pass

        _ = self.fonts
        if hasattr(self, '_m_fonts'):
            pass
            for i in range(len(self._m_fonts)):
                pass
                self._m_fonts[i]._fetch_instances()



    class DirTableEntry(KaitaiStruct):
        SEQ_FIELDS = ["tag", "checksum", "offset", "length"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Otff.DirTableEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tag']['start'] = self._io.pos()
            self.tag = (self._io.read_bytes(4)).decode(u"ASCII")
            self._debug['tag']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_u4be()
            self._debug['checksum']['end'] = self._io.pos()
            self._debug['offset']['start'] = self._io.pos()
            self.offset = self._io.read_u4be()
            self._debug['offset']['end'] = self._io.pos()
            self._debug['length']['start'] = self._io.pos()
            self.length = self._io.read_u4be()
            self._debug['length']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.raw_value
            if hasattr(self, '_m_raw_value'):
                pass


        @property
        def raw_value(self):
            if hasattr(self, '_m_raw_value'):
                return self._m_raw_value

            io = self._root._io
            _pos = io.pos()
            io.seek(self.offset)
            self._debug['_m_raw_value']['start'] = io.pos()
            self._m_raw_value = io.read_bytes(self.length)
            self._debug['_m_raw_value']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_raw_value', None)


    class Font(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, index, _io, _parent=None, _root=None):
            super(Otff.Font, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.index = index
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.offset_table
            if hasattr(self, '_m_offset_table'):
                pass
                self._m_offset_table._fetch_instances()


        @property
        def offset_table(self):
            if hasattr(self, '_m_offset_table'):
                return self._m_offset_table

            _pos = self._io.pos()
            self._io.seek(self._root.ofs_tables[self.index])
            self._debug['_m_offset_table']['start'] = self._io.pos()
            self._m_offset_table = Otff.OffsetTable(self._io, self, self._root)
            self._debug['_m_offset_table']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_offset_table', None)


    class OffsetTable(KaitaiStruct):
        SEQ_FIELDS = ["magic", "num_tables", "search_range", "entry_selector", "range_shift", "directory_table"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Otff.OffsetTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x4F\x54\x54\x4F":
                raise kaitaistruct.ValidationNotEqualError(b"\x4F\x54\x54\x4F", self.magic, self._io, u"/types/offset_table/seq/0")
            self._debug['num_tables']['start'] = self._io.pos()
            self.num_tables = self._io.read_u2be()
            self._debug['num_tables']['end'] = self._io.pos()
            self._debug['search_range']['start'] = self._io.pos()
            self.search_range = self._io.read_u2be()
            self._debug['search_range']['end'] = self._io.pos()
            self._debug['entry_selector']['start'] = self._io.pos()
            self.entry_selector = self._io.read_u2be()
            self._debug['entry_selector']['end'] = self._io.pos()
            self._debug['range_shift']['start'] = self._io.pos()
            self.range_shift = self._io.read_u2be()
            self._debug['range_shift']['end'] = self._io.pos()
            self._debug['directory_table']['start'] = self._io.pos()
            self._debug['directory_table']['arr'] = []
            self.directory_table = []
            for i in range(self.num_tables):
                self._debug['directory_table']['arr'].append({'start': self._io.pos()})
                self.directory_table.append(Otff.DirTableEntry(self._io, self, self._root))
                self._debug['directory_table']['arr'][i]['end'] = self._io.pos()

            self._debug['directory_table']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.directory_table)):
                pass
                self.directory_table[i]._fetch_instances()



    class Version(KaitaiStruct):
        SEQ_FIELDS = ["major", "minor"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Otff.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u2be()
            self._debug['major']['end'] = self._io.pos()
            if not  ((self.major == 1) or (self.major == 2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.major, self._io, u"/types/version/seq/0")
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u2be()
            self._debug['minor']['end'] = self._io.pos()
            if not self.minor == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.minor, self._io, u"/types/version/seq/1")


        def _fetch_instances(self):
            pass


    @property
    def fonts(self):
        if hasattr(self, '_m_fonts'):
            return self._m_fonts

        self._debug['_m_fonts']['start'] = self._io.pos()
        self._debug['_m_fonts']['arr'] = []
        self._m_fonts = []
        for i in range(self.num_fonts):
            self._debug['_m_fonts']['arr'].append({'start': self._io.pos()})
            self._m_fonts.append(Otff.Font(i, self._io, self, self._root))
            self._debug['_m_fonts']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_fonts']['end'] = self._io.pos()
        return getattr(self, '_m_fonts', None)


