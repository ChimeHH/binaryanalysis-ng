# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SpreadtrumPac(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/divinebird/pacextractor/blob/master/pacextractor.c
    
    
    .. seealso::
       Source - https://github.com/yonglongliu/vendor/blob/f0e4a4c5025b8f7a13e69db3af9446717702f4f2/sprd/build/buildpac/tools/unpac_perl/unpac.pl#L145
    """
    SEQ_FIELDS = ["header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SpreadtrumPac, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = SpreadtrumPac.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        _ = self.entries
        if hasattr(self, '_m_entries'):
            pass
            self._m_entries._fetch_instances()


    class Entries(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, num_partitions, _io, _parent=None, _root=None):
            super(SpreadtrumPac.Entries, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_partitions = num_partitions
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_partitions):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(SpreadtrumPac.Entry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["header", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SpreadtrumPac.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = SpreadtrumPac.EntryHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(self.header.len - 2580)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            _ = self.data
            if hasattr(self, '_m_data'):
                pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            io = self._root._io
            _pos = io.pos()
            io.seek(self.header.ofs_partition)
            self._debug['_m_data']['start'] = io.pos()
            self._m_data = io.read_bytes(self.header.len_partition)
            self._debug['_m_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_data', None)


    class EntryHeader(KaitaiStruct):
        SEQ_FIELDS = ["len", "name", "file_name", "len_partition", "file_flag", "check_flag", "ofs_partition", "omit_flag", "addr_num", "addresses", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SpreadtrumPac.EntryHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u4le()
            self._debug['len']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = self._io.read_bytes(512)
            self._debug['name']['end'] = self._io.pos()
            self._debug['file_name']['start'] = self._io.pos()
            self.file_name = self._io.read_bytes(1024)
            self._debug['file_name']['end'] = self._io.pos()
            self._debug['len_partition']['start'] = self._io.pos()
            self.len_partition = self._io.read_u4le()
            self._debug['len_partition']['end'] = self._io.pos()
            if not self.len_partition <= self._root._io.size():
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size(), self.len_partition, self._io, u"/types/entry_header/seq/3")
            self._debug['file_flag']['start'] = self._io.pos()
            self.file_flag = self._io.read_u4le()
            self._debug['file_flag']['end'] = self._io.pos()
            self._debug['check_flag']['start'] = self._io.pos()
            self.check_flag = self._io.read_u4le()
            self._debug['check_flag']['end'] = self._io.pos()
            self._debug['ofs_partition']['start'] = self._io.pos()
            self.ofs_partition = self._io.read_u4le()
            self._debug['ofs_partition']['end'] = self._io.pos()
            if not self.ofs_partition <= self._root._io.size():
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size(), self.ofs_partition, self._io, u"/types/entry_header/seq/6")
            self._debug['omit_flag']['start'] = self._io.pos()
            self.omit_flag = self._io.read_u4le()
            self._debug['omit_flag']['end'] = self._io.pos()
            self._debug['addr_num']['start'] = self._io.pos()
            self.addr_num = self._io.read_u4le()
            self._debug['addr_num']['end'] = self._io.pos()
            self._debug['addresses']['start'] = self._io.pos()
            self._debug['addresses']['arr'] = []
            self.addresses = []
            for i in range(5):
                self._debug['addresses']['arr'].append({'start': self._io.pos()})
                self.addresses.append(self._io.read_u4le())
                self._debug['addresses']['arr'][i]['end'] = self._io.pos()

            self._debug['addresses']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(996)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.addresses)):
                pass



    class Header(KaitaiStruct):
        SEQ_FIELDS = ["version", "len_file", "product_name", "firmware_name", "num_partitions", "ofs_partitions_list", "mode", "flash_type", "nand_strategy", "is_nv_backup", "nand_page_type", "product_name2", "oma_dm_product_flag", "is_oma_dm", "is_preload", "reserved", "magic", "crc1", "crc2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SpreadtrumPac.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_bytes(48)
            self._debug['version']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()
            if not self.len_file >= 2124:
                raise kaitaistruct.ValidationLessThanError(2124, self.len_file, self._io, u"/types/header/seq/1")
            if not self.len_file <= self._root._io.size():
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size(), self.len_file, self._io, u"/types/header/seq/1")
            self._debug['product_name']['start'] = self._io.pos()
            self.product_name = self._io.read_bytes(512)
            self._debug['product_name']['end'] = self._io.pos()
            self._debug['firmware_name']['start'] = self._io.pos()
            self.firmware_name = self._io.read_bytes(512)
            self._debug['firmware_name']['end'] = self._io.pos()
            self._debug['num_partitions']['start'] = self._io.pos()
            self.num_partitions = self._io.read_u4le()
            self._debug['num_partitions']['end'] = self._io.pos()
            if not self.num_partitions >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.num_partitions, self._io, u"/types/header/seq/4")
            if not self.num_partitions <= self._root._io.size():
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size(), self.num_partitions, self._io, u"/types/header/seq/4")
            self._debug['ofs_partitions_list']['start'] = self._io.pos()
            self.ofs_partitions_list = self._io.read_u4le()
            self._debug['ofs_partitions_list']['end'] = self._io.pos()
            if not self.ofs_partitions_list >= 2124:
                raise kaitaistruct.ValidationLessThanError(2124, self.ofs_partitions_list, self._io, u"/types/header/seq/5")
            if not self.ofs_partitions_list <= self._root._io.size():
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size(), self.ofs_partitions_list, self._io, u"/types/header/seq/5")
            self._debug['mode']['start'] = self._io.pos()
            self.mode = self._io.read_u4le()
            self._debug['mode']['end'] = self._io.pos()
            self._debug['flash_type']['start'] = self._io.pos()
            self.flash_type = self._io.read_u4le()
            self._debug['flash_type']['end'] = self._io.pos()
            self._debug['nand_strategy']['start'] = self._io.pos()
            self.nand_strategy = self._io.read_u4le()
            self._debug['nand_strategy']['end'] = self._io.pos()
            self._debug['is_nv_backup']['start'] = self._io.pos()
            self.is_nv_backup = self._io.read_u4le()
            self._debug['is_nv_backup']['end'] = self._io.pos()
            self._debug['nand_page_type']['start'] = self._io.pos()
            self.nand_page_type = self._io.read_u4le()
            self._debug['nand_page_type']['end'] = self._io.pos()
            self._debug['product_name2']['start'] = self._io.pos()
            self.product_name2 = self._io.read_bytes(200)
            self._debug['product_name2']['end'] = self._io.pos()
            self._debug['oma_dm_product_flag']['start'] = self._io.pos()
            self.oma_dm_product_flag = self._io.read_u4le()
            self._debug['oma_dm_product_flag']['end'] = self._io.pos()
            self._debug['is_oma_dm']['start'] = self._io.pos()
            self.is_oma_dm = self._io.read_u4le()
            self._debug['is_oma_dm']['end'] = self._io.pos()
            self._debug['is_preload']['start'] = self._io.pos()
            self.is_preload = self._io.read_u4le()
            self._debug['is_preload']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self._debug['reserved']['arr'] = []
            self.reserved = []
            for i in range(200):
                self._debug['reserved']['arr'].append({'start': self._io.pos()})
                self.reserved.append(SpreadtrumPac.Padding4(self._io, self, self._root))
                self._debug['reserved']['arr'][i]['end'] = self._io.pos()

            self._debug['reserved']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\xFA\xFF\xFA\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFA\xFF\xFA\xFF", self.magic, self._io, u"/types/header/seq/16")
            self._debug['crc1']['start'] = self._io.pos()
            self.crc1 = self._io.read_u2le()
            self._debug['crc1']['end'] = self._io.pos()
            self._debug['crc2']['start'] = self._io.pos()
            self.crc2 = self._io.read_u2le()
            self._debug['crc2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.reserved)):
                pass
                self.reserved[i]._fetch_instances()



    class Padding4(KaitaiStruct):
        SEQ_FIELDS = ["padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SpreadtrumPac.Padding4, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(4)
            self._debug['padding']['end'] = self._io.pos()
            if not self.padding == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.padding, self._io, u"/types/padding4/seq/0")


        def _fetch_instances(self):
            pass


    @property
    def entries(self):
        if hasattr(self, '_m_entries'):
            return self._m_entries

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_partitions_list)
        self._debug['_m_entries']['start'] = self._io.pos()
        self._m_entries = SpreadtrumPac.Entries(self.header.num_partitions, self._io, self, self._root)
        self._debug['_m_entries']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_entries', None)


