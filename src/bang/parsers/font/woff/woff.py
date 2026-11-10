# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Woff(KaitaiStruct):
    """
    .. seealso::
       Source - https://www.w3.org/TR/2012/REC-WOFF-20121213/
    """
    SEQ_FIELDS = ["preheader", "woff"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Woff, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['preheader']['start'] = self._io.pos()
        self.preheader = Woff.Preheader(self._io, self, self._root)
        self._debug['preheader']['end'] = self._io.pos()
        self._debug['woff']['start'] = self._io.pos()
        self._raw_woff = self._io.read_bytes(self.preheader.len_file - 12)
        _io__raw_woff = KaitaiStream(BytesIO(self._raw_woff))
        self.woff = Woff.Woff(_io__raw_woff, self, self._root)
        self._debug['woff']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.preheader._fetch_instances()
        self.woff._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["num_tables", "reserved", "total_sfnt_size", "major_version", "minor_version", "ofs_meta", "len_meta", "meta_orig_length", "ofs_private_data_block", "len_private_data_block"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Woff.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_tables']['start'] = self._io.pos()
            self.num_tables = self._io.read_u2be()
            self._debug['num_tables']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(2)
            self._debug['reserved']['end'] = self._io.pos()
            if not self.reserved == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.reserved, self._io, u"/types/header/seq/1")
            self._debug['total_sfnt_size']['start'] = self._io.pos()
            self.total_sfnt_size = self._io.read_u4be()
            self._debug['total_sfnt_size']['end'] = self._io.pos()
            self._debug['major_version']['start'] = self._io.pos()
            self.major_version = self._io.read_u2be()
            self._debug['major_version']['end'] = self._io.pos()
            self._debug['minor_version']['start'] = self._io.pos()
            self.minor_version = self._io.read_u2be()
            self._debug['minor_version']['end'] = self._io.pos()
            self._debug['ofs_meta']['start'] = self._io.pos()
            self.ofs_meta = self._io.read_u4be()
            self._debug['ofs_meta']['end'] = self._io.pos()
            if not self.ofs_meta <= self._root.preheader.len_file:
                raise kaitaistruct.ValidationGreaterThanError(self._root.preheader.len_file, self.ofs_meta, self._io, u"/types/header/seq/5")
            self._debug['len_meta']['start'] = self._io.pos()
            self.len_meta = self._io.read_u4be()
            self._debug['len_meta']['end'] = self._io.pos()
            if not self.len_meta <= self._root.preheader.len_file - self.ofs_meta:
                raise kaitaistruct.ValidationGreaterThanError(self._root.preheader.len_file - self.ofs_meta, self.len_meta, self._io, u"/types/header/seq/6")
            self._debug['meta_orig_length']['start'] = self._io.pos()
            self.meta_orig_length = self._io.read_u4be()
            self._debug['meta_orig_length']['end'] = self._io.pos()
            self._debug['ofs_private_data_block']['start'] = self._io.pos()
            self.ofs_private_data_block = self._io.read_u4be()
            self._debug['ofs_private_data_block']['end'] = self._io.pos()
            if not self.ofs_private_data_block <= self._root.preheader.len_file:
                raise kaitaistruct.ValidationGreaterThanError(self._root.preheader.len_file, self.ofs_private_data_block, self._io, u"/types/header/seq/8")
            self._debug['len_private_data_block']['start'] = self._io.pos()
            self.len_private_data_block = self._io.read_u4be()
            self._debug['len_private_data_block']['end'] = self._io.pos()
            if not self.len_private_data_block <= self._root.preheader.len_file - self.ofs_private_data_block:
                raise kaitaistruct.ValidationGreaterThanError(self._root.preheader.len_file - self.ofs_private_data_block, self.len_private_data_block, self._io, u"/types/header/seq/9")


        def _fetch_instances(self):
            pass


    class Preheader(KaitaiStruct):
        SEQ_FIELDS = ["signature", "flavor", "len_file"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Woff.Preheader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(4)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x77\x4F\x46\x46":
                raise kaitaistruct.ValidationNotEqualError(b"\x77\x4F\x46\x46", self.signature, self._io, u"/types/preheader/seq/0")
            self._debug['flavor']['start'] = self._io.pos()
            self.flavor = self._io.read_u4be()
            self._debug['flavor']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4be()
            self._debug['len_file']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class TableData(KaitaiStruct):
        SEQ_FIELDS = ["data", "padding"]
        def __init__(self, len_data, _io, _parent=None, _root=None):
            super(Woff.TableData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.len_data = len_data
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self.len_data) % 4)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class TableDirectory(KaitaiStruct):
        SEQ_FIELDS = ["tag", "ofs_data", "len_data", "len_uncompressed_data", "checksum"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Woff.TableDirectory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tag']['start'] = self._io.pos()
            self.tag = self._io.read_u4be()
            self._debug['tag']['end'] = self._io.pos()
            self._debug['ofs_data']['start'] = self._io.pos()
            self.ofs_data = self._io.read_u4be()
            self._debug['ofs_data']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4be()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['len_uncompressed_data']['start'] = self._io.pos()
            self.len_uncompressed_data = self._io.read_u4be()
            self._debug['len_uncompressed_data']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_u4be()
            self._debug['checksum']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.data
            if hasattr(self, '_m_data'):
                pass
                self._m_data._fetch_instances()


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_data)
            self._debug['_m_data']['start'] = io.pos()
            self._m_data = Woff.TableData(self.len_data, io, self, self._root)
            self._debug['_m_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_data', None)


    class Woff(KaitaiStruct):
        SEQ_FIELDS = ["header", "table_directories"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Woff.Woff, self).__init__(_io)
            self._parent = _parent
            self._root = _root or self
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Woff.Header(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['table_directories']['start'] = self._io.pos()
            self._debug['table_directories']['arr'] = []
            self.table_directories = []
            for i in range(self.header.num_tables):
                self._debug['table_directories']['arr'].append({'start': self._io.pos()})
                self.table_directories.append(Woff.TableDirectory(self._io, self, self._root))
                self._debug['table_directories']['arr'][i]['end'] = self._io.pos()

            self._debug['table_directories']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            for i in range(len(self.table_directories)):
                pass
                self.table_directories[i]._fetch_instances()

            _ = self.extended_metadata
            if hasattr(self, '_m_extended_metadata'):
                pass

            _ = self.private_data
            if hasattr(self, '_m_private_data'):
                pass


        @property
        def extended_metadata(self):
            if hasattr(self, '_m_extended_metadata'):
                return self._m_extended_metadata

            if self.header.len_meta != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.header.ofs_meta)
                self._debug['_m_extended_metadata']['start'] = io.pos()
                self._m_extended_metadata = io.read_bytes(self.header.len_meta)
                self._debug['_m_extended_metadata']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_extended_metadata', None)

        @property
        def private_data(self):
            if hasattr(self, '_m_private_data'):
                return self._m_private_data

            if self.header.len_private_data_block != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.header.ofs_private_data_block)
                self._debug['_m_private_data']['start'] = io.pos()
                self._m_private_data = io.read_bytes(self.header.len_private_data_block)
                self._debug['_m_private_data']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_private_data', None)



