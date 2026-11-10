# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Bflt(KaitaiStruct):
    """
    .. seealso::
       Source - https://web.archive.org/web/20120123212024/http://retired.beyondlogic.org/uClinux/bflt.htm
    
    
    .. seealso::
       Source - http://web.archive.org/web/20180317070540/https://blog.tangrs.id.au/2012/04/07/bflt-format-implementation-notes/
    """
    SEQ_FIELDS = ["header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Bflt, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(64)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Bflt.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        _ = self.data
        if hasattr(self, '_m_data'):
            pass

        _ = self.relocations
        if hasattr(self, '_m_relocations'):
            pass
            self._m_relocations._fetch_instances()

        _ = self.text
        if hasattr(self, '_m_text'):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "ofs_entry", "ofs_data_start", "ofs_data_end", "ofs_bss_end", "stack_size", "ofs_reloc_start", "reloc_count", "flags", "build_date", "filler"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Bflt.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x62\x46\x4C\x54":
                raise kaitaistruct.ValidationNotEqualError(b"\x62\x46\x4C\x54", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4be()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 4:
                raise kaitaistruct.ValidationNotEqualError(4, self.version, self._io, u"/types/header/seq/1")
            self._debug['ofs_entry']['start'] = self._io.pos()
            self.ofs_entry = self._io.read_u4be()
            self._debug['ofs_entry']['end'] = self._io.pos()
            self._debug['ofs_data_start']['start'] = self._io.pos()
            self.ofs_data_start = self._io.read_u4be()
            self._debug['ofs_data_start']['end'] = self._io.pos()
            self._debug['ofs_data_end']['start'] = self._io.pos()
            self.ofs_data_end = self._io.read_u4be()
            self._debug['ofs_data_end']['end'] = self._io.pos()
            self._debug['ofs_bss_end']['start'] = self._io.pos()
            self.ofs_bss_end = self._io.read_u4be()
            self._debug['ofs_bss_end']['end'] = self._io.pos()
            self._debug['stack_size']['start'] = self._io.pos()
            self.stack_size = self._io.read_u4be()
            self._debug['stack_size']['end'] = self._io.pos()
            self._debug['ofs_reloc_start']['start'] = self._io.pos()
            self.ofs_reloc_start = self._io.read_u4be()
            self._debug['ofs_reloc_start']['end'] = self._io.pos()
            self._debug['reloc_count']['start'] = self._io.pos()
            self.reloc_count = self._io.read_u4be()
            self._debug['reloc_count']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['build_date']['start'] = self._io.pos()
            self.build_date = self._io.read_u4be()
            self._debug['build_date']['end'] = self._io.pos()
            self._debug['filler']['start'] = self._io.pos()
            self.filler = self._io.read_bytes(20)
            self._debug['filler']['end'] = self._io.pos()
            if not self.filler == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.filler, self._io, u"/types/header/seq/11")


        def _fetch_instances(self):
            pass

        @property
        def got_pic(self):
            """program is PIC with GOT."""
            if hasattr(self, '_m_got_pic'):
                return self._m_got_pic

            self._m_got_pic = self.flags & 2 == 2
            return getattr(self, '_m_got_pic', None)

        @property
        def gzdata(self):
            """only data/relocs are compressed (for XIP)."""
            if hasattr(self, '_m_gzdata'):
                return self._m_gzdata

            self._m_gzdata = self.flags & 8 == 8
            return getattr(self, '_m_gzdata', None)

        @property
        def gzip(self):
            """all but the header is compressed."""
            if hasattr(self, '_m_gzip'):
                return self._m_gzip

            self._m_gzip = self.flags & 4 == 4
            return getattr(self, '_m_gzip', None)

        @property
        def ktrace(self):
            """output useful kernel trace for debugging."""
            if hasattr(self, '_m_ktrace'):
                return self._m_ktrace

            self._m_ktrace = self.flags & 16 == 16
            return getattr(self, '_m_ktrace', None)

        @property
        def load_into_ram(self):
            """load program entirely into RAM."""
            if hasattr(self, '_m_load_into_ram'):
                return self._m_load_into_ram

            self._m_load_into_ram = self.flags & 1 == 1
            return getattr(self, '_m_load_into_ram', None)


    class Relocations(KaitaiStruct):
        SEQ_FIELDS = ["relocation"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Bflt.Relocations, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['relocation']['start'] = self._io.pos()
            self._debug['relocation']['arr'] = []
            self.relocation = []
            for i in range(self._root.header.reloc_count):
                self._debug['relocation']['arr'].append({'start': self._io.pos()})
                self.relocation.append(self._io.read_u4be())
                self._debug['relocation']['arr'][i]['end'] = self._io.pos()

            self._debug['relocation']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.relocation)):
                pass



    @property
    def data(self):
        if hasattr(self, '_m_data'):
            return self._m_data

        if (not ( ((self.header.gzip) or (self.header.gzdata)) )):
            pass
            _pos = self._io.pos()
            self._io.seek(self.header.ofs_data_start)
            self._debug['_m_data']['start'] = self._io.pos()
            self._m_data = self._io.read_bytes(self.len_data)
            self._debug['_m_data']['end'] = self._io.pos()
            self._io.seek(_pos)

        return getattr(self, '_m_data', None)

    @property
    def len_data(self):
        if hasattr(self, '_m_len_data'):
            return self._m_len_data

        self._m_len_data = self.header.ofs_data_end - self.header.ofs_data_start
        return getattr(self, '_m_len_data', None)

    @property
    def len_text(self):
        if hasattr(self, '_m_len_text'):
            return self._m_len_text

        self._m_len_text = self.header.ofs_data_start - self.header.ofs_entry
        return getattr(self, '_m_len_text', None)

    @property
    def relocations(self):
        if hasattr(self, '_m_relocations'):
            return self._m_relocations

        if (not ( ((self.header.gzip) or (self.header.gzdata)) )):
            pass
            _pos = self._io.pos()
            self._io.seek(self.header.ofs_reloc_start)
            self._debug['_m_relocations']['start'] = self._io.pos()
            self._m_relocations = Bflt.Relocations(self._io, self, self._root)
            self._debug['_m_relocations']['end'] = self._io.pos()
            self._io.seek(_pos)

        return getattr(self, '_m_relocations', None)

    @property
    def text(self):
        if hasattr(self, '_m_text'):
            return self._m_text

        if (not (self.header.gzip)):
            pass
            _pos = self._io.pos()
            self._io.seek(self.header.ofs_entry)
            self._debug['_m_text']['start'] = self._io.pos()
            self._m_text = self._io.read_bytes(self.len_text)
            self._debug['_m_text']['end'] = self._io.pos()
            self._io.seek(_pos)

        return getattr(self, '_m_text', None)


