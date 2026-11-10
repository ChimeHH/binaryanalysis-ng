# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ambarella(KaitaiStruct):
    """
    .. seealso::
       (section 4.2) - http://web.archive.org/web/20190402224117/https://courses.cs.ut.ee/MTAT.07.022/2015_spring/uploads/Main/karl-report-s15.pdf
    
    
    .. seealso::
       (post - http://web.archive.org/web/20140627194326/http://forum.dashcamtalk.com/threads/r-d-a7-r-d-thread.5119/page-2
    """
    SEQ_FIELDS = ["start_offsets", "end_offsets"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Ambarella, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['start_offsets']['start'] = self._io.pos()
        self._debug['start_offsets']['arr'] = []
        self.start_offsets = []
        for i in range(32):
            self._debug['start_offsets']['arr'].append({'start': self._io.pos()})
            self.start_offsets.append(self._io.read_u4le())
            self._debug['start_offsets']['arr'][i]['end'] = self._io.pos()

        self._debug['start_offsets']['end'] = self._io.pos()
        self._debug['end_offsets']['start'] = self._io.pos()
        self._debug['end_offsets']['arr'] = []
        self.end_offsets = []
        for i in range(32):
            self._debug['end_offsets']['arr'].append({'start': self._io.pos()})
            self.end_offsets.append(self._io.read_u4le())
            self._debug['end_offsets']['arr'][i]['end'] = self._io.pos()

        self._debug['end_offsets']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.start_offsets)):
            pass

        for i in range(len(self.end_offsets)):
            pass

        _ = self.sections
        if hasattr(self, '_m_sections'):
            pass
            for i in range(len(self._m_sections)):
                pass
                self._m_sections[i]._fetch_instances()



    class Section(KaitaiStruct):
        SEQ_FIELDS = ["header", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ambarella.Section, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self._raw_header = self._io.read_bytes(256)
            _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
            self.header = Ambarella.SectionHeader(_io__raw_header, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.header.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()


    class SectionData(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, i, _io, _parent=None, _root=None):
            super(Ambarella.SectionData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.i = i
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.body
            if hasattr(self, '_m_body'):
                pass
                self._m_body._fetch_instances()


        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body

            if self._parent.start_offsets[self.i] != 0:
                pass
                _pos = self._io.pos()
                self._io.seek(self._parent.start_offsets[self.i])
                self._debug['_m_body']['start'] = self._io.pos()
                self._raw__m_body = self._io.read_bytes(self._parent.end_offsets[self.i] - self._parent.start_offsets[self.i])
                _io__raw__m_body = KaitaiStream(BytesIO(self._raw__m_body))
                self._m_body = Ambarella.Section(_io__raw__m_body, self, self._root)
                self._debug['_m_body']['end'] = self._io.pos()
                self._io.seek(_pos)

            return getattr(self, '_m_body', None)


    class SectionHeader(KaitaiStruct):
        SEQ_FIELDS = ["crc32", "version", "build_date", "len_data", "memory_location", "flags", "magic", "flags_2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ambarella.SectionHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['build_date']['start'] = self._io.pos()
            self.build_date = self._io.read_u4le()
            self._debug['build_date']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['memory_location']['start'] = self._io.pos()
            self.memory_location = self._io.read_u4le()
            self._debug['memory_location']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x90\xEB\x24\xA3":
                raise kaitaistruct.ValidationNotEqualError(b"\x90\xEB\x24\xA3", self.magic, self._io, u"/types/section_header/seq/6")
            self._debug['flags_2']['start'] = self._io.pos()
            self.flags_2 = self._io.read_u4le()
            self._debug['flags_2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def sections(self):
        if hasattr(self, '_m_sections'):
            return self._m_sections

        self._debug['_m_sections']['start'] = self._io.pos()
        self._debug['_m_sections']['arr'] = []
        self._m_sections = []
        for i in range(32):
            self._debug['_m_sections']['arr'].append({'start': self._io.pos()})
            self._m_sections.append(Ambarella.SectionData(i, self._io, self, self._root))
            self._debug['_m_sections']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_sections']['end'] = self._io.pos()
        return getattr(self, '_m_sections', None)


