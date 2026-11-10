# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class HpBdl(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/tylerwhall/hpbdl
    
    
    .. seealso::
       Source - https://github.com/onekey-sec/unblob/blob/main/unblob/handlers/archive/hp/bdl.py
    
    
    .. seealso::
       Source - https://github.com/onekey-sec/unblob/blob/main/unblob/handlers/archive/hp/ipkg.py
    """
    SEQ_FIELDS = ["header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(HpBdl, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = HpBdl.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        _ = self.file_offset_table
        if hasattr(self, '_m_file_offset_table'):
            pass
            self._m_file_offset_table._fetch_instances()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "major", "minor", "ofs_toc", "unknown", "num_toc_entries", "unknown_2", "release", "brand", "device_id", "unknown_3", "version", "revision"]
        def __init__(self, _io, _parent=None, _root=None):
            super(HpBdl.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x69\x62\x64\x6C":
                raise kaitaistruct.ValidationNotEqualError(b"\x69\x62\x64\x6C", self.magic, self._io, u"/types/header/seq/0")
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u2le()
            self._debug['major']['end'] = self._io.pos()
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u2le()
            self._debug['minor']['end'] = self._io.pos()
            self._debug['ofs_toc']['start'] = self._io.pos()
            self.ofs_toc = self._io.read_u4le()
            self._debug['ofs_toc']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(4)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['num_toc_entries']['start'] = self._io.pos()
            self.num_toc_entries = self._io.read_u4le()
            self._debug['num_toc_entries']['end'] = self._io.pos()
            self._debug['unknown_2']['start'] = self._io.pos()
            self.unknown_2 = self._io.read_bytes(12)
            self._debug['unknown_2']['end'] = self._io.pos()
            self._debug['release']['start'] = self._io.pos()
            self.release = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['release']['end'] = self._io.pos()
            self._debug['brand']['start'] = self._io.pos()
            self.brand = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['brand']['end'] = self._io.pos()
            self._debug['device_id']['start'] = self._io.pos()
            self.device_id = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['device_id']['end'] = self._io.pos()
            self._debug['unknown_3']['start'] = self._io.pos()
            self.unknown_3 = self._io.read_bytes(9)
            self._debug['unknown_3']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['version']['end'] = self._io.pos()
            self._debug['revision']['start'] = self._io.pos()
            self.revision = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['revision']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Ipkg(KaitaiStruct):
        SEQ_FIELDS = ["magic", "major", "minor", "ofs_toc", "unknown_1", "num_toc_entries", "unknown_2", "reserved", "file_version", "product_name", "ipkg_name", "signature"]
        def __init__(self, _io, _parent=None, _root=None):
            super(HpBdl.Ipkg, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x69\x70\x6B\x67":
                raise kaitaistruct.ValidationNotEqualError(b"\x69\x70\x6B\x67", self.magic, self._io, u"/types/ipkg/seq/0")
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u2le()
            self._debug['major']['end'] = self._io.pos()
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u2le()
            self._debug['minor']['end'] = self._io.pos()
            self._debug['ofs_toc']['start'] = self._io.pos()
            self.ofs_toc = self._io.read_u4le()
            self._debug['ofs_toc']['end'] = self._io.pos()
            self._debug['unknown_1']['start'] = self._io.pos()
            self.unknown_1 = self._io.read_bytes(4)
            self._debug['unknown_1']['end'] = self._io.pos()
            self._debug['num_toc_entries']['start'] = self._io.pos()
            self.num_toc_entries = self._io.read_u4le()
            self._debug['num_toc_entries']['end'] = self._io.pos()
            self._debug['unknown_2']['start'] = self._io.pos()
            self.unknown_2 = self._io.read_bytes(8)
            self._debug['unknown_2']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(4)
            self._debug['reserved']['end'] = self._io.pos()
            if not self.reserved == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.reserved, self._io, u"/types/ipkg/seq/7")
            self._debug['file_version']['start'] = self._io.pos()
            self.file_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['file_version']['end'] = self._io.pos()
            self._debug['product_name']['start'] = self._io.pos()
            self.product_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['product_name']['end'] = self._io.pos()
            self._debug['ipkg_name']['start'] = self._io.pos()
            self.ipkg_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['ipkg_name']['end'] = self._io.pos()
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(256)
            self._debug['signature']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.entries
            if hasattr(self, '_m_entries'):
                pass
                for i in range(len(self._m_entries)):
                    pass
                    self._m_entries[i]._fetch_instances()



        class Entry(KaitaiStruct):
            SEQ_FIELDS = ["name", "ofs_data", "len_data", "crc32"]
            def __init__(self, _io, _parent=None, _root=None):
                super(HpBdl.Ipkg.Entry, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['name']['start'] = self._io.pos()
                self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
                self._debug['name']['end'] = self._io.pos()
                self._debug['ofs_data']['start'] = self._io.pos()
                self.ofs_data = self._io.read_u8le()
                self._debug['ofs_data']['end'] = self._io.pos()
                self._debug['len_data']['start'] = self._io.pos()
                self.len_data = self._io.read_u8le()
                self._debug['len_data']['end'] = self._io.pos()
                self._debug['crc32']['start'] = self._io.pos()
                self.crc32 = self._io.read_u4le()
                self._debug['crc32']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _ = self.data
                if hasattr(self, '_m_data'):
                    pass


            @property
            def data(self):
                if hasattr(self, '_m_data'):
                    return self._m_data

                _pos = self._io.pos()
                self._io.seek(self.ofs_data)
                self._debug['_m_data']['start'] = self._io.pos()
                self._m_data = self._io.read_bytes(self.len_data)
                self._debug['_m_data']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_data', None)


        @property
        def entries(self):
            if hasattr(self, '_m_entries'):
                return self._m_entries

            _pos = self._io.pos()
            self._io.seek(self.ofs_toc)
            self._debug['_m_entries']['start'] = self._io.pos()
            self._debug['_m_entries']['arr'] = []
            self._m_entries = []
            for i in range(self.num_toc_entries):
                self._debug['_m_entries']['arr'].append({'start': self._io.pos()})
                self._m_entries.append(HpBdl.Ipkg.Entry(self._io, self, self._root))
                self._debug['_m_entries']['arr'][i]['end'] = self._io.pos()

            self._debug['_m_entries']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_entries', None)


    class Toc(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, num_toc_entries, _io, _parent=None, _root=None):
            super(HpBdl.Toc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_toc_entries = num_toc_entries
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_toc_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(HpBdl.TocEntry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class TocEntry(KaitaiStruct):
        SEQ_FIELDS = ["ofs_entry", "len_entry"]
        def __init__(self, _io, _parent=None, _root=None):
            super(HpBdl.TocEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_entry']['start'] = self._io.pos()
            self.ofs_entry = self._io.read_u8le()
            self._debug['ofs_entry']['end'] = self._io.pos()
            self._debug['len_entry']['start'] = self._io.pos()
            self.len_entry = self._io.read_u8le()
            self._debug['len_entry']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.entry
            if hasattr(self, '_m_entry'):
                pass
                self._m_entry._fetch_instances()


        @property
        def entry(self):
            if hasattr(self, '_m_entry'):
                return self._m_entry

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_entry)
            self._debug['_m_entry']['start'] = io.pos()
            self._raw__m_entry = io.read_bytes(self.len_entry)
            _io__raw__m_entry = KaitaiStream(BytesIO(self._raw__m_entry))
            self._m_entry = HpBdl.Ipkg(_io__raw__m_entry, self, self._root)
            self._debug['_m_entry']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_entry', None)


    @property
    def file_offset_table(self):
        if hasattr(self, '_m_file_offset_table'):
            return self._m_file_offset_table

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_toc)
        self._debug['_m_file_offset_table']['start'] = self._io.pos()
        self._m_file_offset_table = HpBdl.Toc(self.header.num_toc_entries, self._io, self, self._root)
        self._debug['_m_file_offset_table']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_file_offset_table', None)


