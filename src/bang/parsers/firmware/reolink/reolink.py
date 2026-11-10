# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Reolink(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/vmallet/pakler/blob/acbf084b/pakler/__init__.py
    """
    SEQ_FIELDS = ["header", "sections", "partitions"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Reolink, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        _on = self.is_64
        if _on == False:
            pass
            self.header = Reolink.Header32(self._io, self, self._root)
        elif _on == True:
            pass
            self.header = Reolink.Header64(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['sections']['start'] = self._io.pos()
        self._debug['sections']['arr'] = []
        self.sections = []
        for i in range(self.num_sections):
            self._debug['sections']['arr'].append({'start': self._io.pos()})
            _on = self.is_64
            if _on == False:
                pass
                self.sections.append(Reolink.Section32(self._io, self, self._root))
            elif _on == True:
                pass
                self.sections.append(Reolink.Section64(self._io, self, self._root))
            self._debug['sections']['arr'][i]['end'] = self._io.pos()

        self._debug['sections']['end'] = self._io.pos()
        self._debug['partitions']['start'] = self._io.pos()
        self._debug['partitions']['arr'] = []
        self.partitions = []
        for i in range(self.num_sections):
            self._debug['partitions']['arr'].append({'start': self._io.pos()})
            self.partitions.append(Reolink.Partition(self._io, self, self._root))
            self._debug['partitions']['arr'][i]['end'] = self._io.pos()

        self._debug['partitions']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _on = self.is_64
        if _on == False:
            pass
            self.header._fetch_instances()
        elif _on == True:
            pass
            self.header._fetch_instances()
        for i in range(len(self.sections)):
            pass
            _on = self.is_64
            if _on == False:
                pass
                self.sections[i]._fetch_instances()
            elif _on == True:
                pass
                self.sections[i]._fetch_instances()

        for i in range(len(self.partitions)):
            pass
            self.partitions[i]._fetch_instances()

        _ = self.header_crc32
        if hasattr(self, '_m_header_crc32'):
            pass


    class Header32(KaitaiStruct):
        SEQ_FIELDS = ["magic", "crc32", "board"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Reolink.Header32, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x13\x59\x72\x32":
                raise kaitaistruct.ValidationNotEqualError(b"\x13\x59\x72\x32", self.magic, self._io, u"/types/header32/seq/0")
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['board']['start'] = self._io.pos()
            self.board = self._io.read_bytes(4)
            self._debug['board']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.first_section
            if hasattr(self, '_m_first_section'):
                pass
                self._m_first_section._fetch_instances()


        @property
        def first_section(self):
            if hasattr(self, '_m_first_section'):
                return self._m_first_section

            io = self._root._io
            _pos = io.pos()
            io.seek(12)
            self._debug['_m_first_section']['start'] = io.pos()
            self._m_first_section = Reolink.Section32(io, self, self._root)
            self._debug['_m_first_section']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_first_section', None)

        @property
        def num_sections(self):
            if hasattr(self, '_m_num_sections'):
                return self._m_num_sections

            self._m_num_sections = (self.first_section.ofs_section - 12) // (64 + 76)
            return getattr(self, '_m_num_sections', None)


    class Header64(KaitaiStruct):
        SEQ_FIELDS = ["magic", "crc32", "board"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Reolink.Header64, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x13\x59\x72\x32\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x13\x59\x72\x32\x00\x00\x00\x00", self.magic, self._io, u"/types/header64/seq/0")
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u8le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['board']['start'] = self._io.pos()
            self.board = self._io.read_bytes(8)
            self._debug['board']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.first_section
            if hasattr(self, '_m_first_section'):
                pass
                self._m_first_section._fetch_instances()


        @property
        def first_section(self):
            if hasattr(self, '_m_first_section'):
                return self._m_first_section

            io = self._root._io
            _pos = io.pos()
            io.seek(24)
            self._debug['_m_first_section']['start'] = io.pos()
            self._m_first_section = Reolink.Section64(io, self, self._root)
            self._debug['_m_first_section']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_first_section', None)

        @property
        def num_sections(self):
            if hasattr(self, '_m_num_sections'):
                return self._m_num_sections

            self._m_num_sections = (self.first_section.ofs_section - 24) // (72 + 76)
            return getattr(self, '_m_num_sections', None)


    class Partition(KaitaiStruct):
        SEQ_FIELDS = ["name", "ofs_partition", "mtd", "start_address", "len_partition"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Reolink.Partition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['ofs_partition']['start'] = self._io.pos()
            self.ofs_partition = self._io.read_u4le()
            self._debug['ofs_partition']['end'] = self._io.pos()
            self._debug['mtd']['start'] = self._io.pos()
            self.mtd = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['mtd']['end'] = self._io.pos()
            self._debug['start_address']['start'] = self._io.pos()
            self.start_address = self._io.read_bytes(4)
            self._debug['start_address']['end'] = self._io.pos()
            self._debug['len_partition']['start'] = self._io.pos()
            self.len_partition = self._io.read_u4le()
            self._debug['len_partition']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Section32(KaitaiStruct):
        SEQ_FIELDS = ["name", "version", "ofs_section", "len_section"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Reolink.Section32, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_bytes(24)
            self._debug['version']['end'] = self._io.pos()
            self._debug['ofs_section']['start'] = self._io.pos()
            self.ofs_section = self._io.read_u4le()
            self._debug['ofs_section']['end'] = self._io.pos()
            self._debug['len_section']['start'] = self._io.pos()
            self.len_section = self._io.read_u4le()
            self._debug['len_section']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.section
            if hasattr(self, '_m_section'):
                pass


        @property
        def section(self):
            if hasattr(self, '_m_section'):
                return self._m_section

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_section)
            self._debug['_m_section']['start'] = io.pos()
            self._m_section = io.read_bytes(self.len_section)
            self._debug['_m_section']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_section', None)


    class Section64(KaitaiStruct):
        SEQ_FIELDS = ["name", "version", "ofs_section", "len_section"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Reolink.Section64, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_bytes(24)
            self._debug['version']['end'] = self._io.pos()
            self._debug['ofs_section']['start'] = self._io.pos()
            self.ofs_section = self._io.read_u8le()
            self._debug['ofs_section']['end'] = self._io.pos()
            self._debug['len_section']['start'] = self._io.pos()
            self.len_section = self._io.read_u8le()
            self._debug['len_section']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.section
            if hasattr(self, '_m_section'):
                pass


        @property
        def section(self):
            if hasattr(self, '_m_section'):
                return self._m_section

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_section)
            self._debug['_m_section']['start'] = io.pos()
            self._m_section = io.read_bytes(self.len_section)
            self._debug['_m_section']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_section', None)


    @property
    def header_crc32(self):
        if hasattr(self, '_m_header_crc32'):
            return self._m_header_crc32

        _pos = self._io.pos()
        self._io.seek(4)
        self._debug['_m_header_crc32']['start'] = self._io.pos()
        self._m_header_crc32 = self._io.read_u4le()
        self._debug['_m_header_crc32']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_header_crc32', None)

    @property
    def is_64(self):
        if hasattr(self, '_m_is_64'):
            return self._m_is_64

        self._m_is_64 = self.header_crc32 == 0
        return getattr(self, '_m_is_64', None)

    @property
    def num_sections(self):
        if hasattr(self, '_m_num_sections'):
            return self._m_num_sections

        self._m_num_sections = self.header.num_sections
        return getattr(self, '_m_num_sections', None)


