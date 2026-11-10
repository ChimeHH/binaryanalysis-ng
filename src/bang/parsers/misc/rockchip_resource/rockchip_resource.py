# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class RockchipResource(KaitaiStruct):
    """
    .. seealso::
       Source - https://gitlab.com/postmarketOS/pmbootstrap/-/issues/2031
    """
    SEQ_FIELDS = ["header", "entries"]
    def __init__(self, _io, _parent=None, _root=None):
        super(RockchipResource, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = RockchipResource.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['entries']['start'] = self._io.pos()
        self._debug['entries']['arr'] = []
        self.entries = []
        for i in range(self.header.num_files):
            self._debug['entries']['arr'].append({'start': self._io.pos()})
            self.entries.append(RockchipResource.Entry(self._io, self, self._root))
            self._debug['entries']['arr'][i]['end'] = self._io.pos()

        self._debug['entries']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.entries)):
            pass
            self.entries[i]._fetch_instances()


    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["magic", "name", "ofs_file_block", "len_file", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(RockchipResource.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x45\x4E\x54\x52":
                raise kaitaistruct.ValidationNotEqualError(b"\x45\x4E\x54\x52", self.magic, self._io, u"/types/entry/seq/0")
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['ofs_file_block']['start'] = self._io.pos()
            self.ofs_file_block = self._io.read_u4le()
            self._debug['ofs_file_block']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(244)
            self._debug['reserved']['end'] = self._io.pos()


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
            self._io.seek(self.ofs_file_block * 512)
            self._debug['_m_data']['start'] = self._io.pos()
            self._m_data = self._io.read_bytes(self.len_file)
            self._debug['_m_data']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_data', None)


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "file_table_version", "len_header", "ofs_file_table", "len_file_table_entry", "unknown1", "num_files", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(RockchipResource.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x52\x53\x43\x45":
                raise kaitaistruct.ValidationNotEqualError(b"\x52\x53\x43\x45", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u2le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['file_table_version']['start'] = self._io.pos()
            self.file_table_version = self._io.read_u2le()
            self._debug['file_table_version']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u1()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['ofs_file_table']['start'] = self._io.pos()
            self.ofs_file_table = self._io.read_u1()
            self._debug['ofs_file_table']['end'] = self._io.pos()
            self._debug['len_file_table_entry']['start'] = self._io.pos()
            self.len_file_table_entry = self._io.read_u1()
            self._debug['len_file_table_entry']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_bytes(1)
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u4le()
            self._debug['num_files']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self._debug['reserved']['arr'] = []
            self.reserved = []
            for i in range(496):
                self._debug['reserved']['arr'].append({'start': self._io.pos()})
                self.reserved.append(RockchipResource.PaddingByte(self._io, self, self._root))
                self._debug['reserved']['arr'][i]['end'] = self._io.pos()

            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.reserved)):
                pass
                self.reserved[i]._fetch_instances()



    class PaddingByte(KaitaiStruct):
        SEQ_FIELDS = ["padding_byte"]
        def __init__(self, _io, _parent=None, _root=None):
            super(RockchipResource.PaddingByte, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['padding_byte']['start'] = self._io.pos()
            self.padding_byte = self._io.read_bytes(1)
            self._debug['padding_byte']['end'] = self._io.pos()
            if not self.padding_byte == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.padding_byte, self._io, u"/types/padding_byte/seq/0")


        def _fetch_instances(self):
            pass



