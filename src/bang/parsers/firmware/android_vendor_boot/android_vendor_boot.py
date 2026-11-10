# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class AndroidVendorBoot(KaitaiStruct):
    """
    .. seealso::
       Source - https://android.googlesource.com/platform/system/tools/mkbootimg/+/b4b04c2a965d9b3ce1ebf0442fc8047fe103d4e6/include/bootimg/bootimg.h
    """

    class RamdiskTypes(IntEnum):
        no_type = 0
        platform = 1
        recovery = 2
        dlkm = 3
    SEQ_FIELDS = ["header", "padding1", "vendor_ramdisk", "padding2", "dtb", "padding3", "vendor_ramdisk_table", "padding4", "bootconfig", "padding5"]
    def __init__(self, _io, _parent=None, _root=None):
        super(AndroidVendorBoot, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = AndroidVendorBoot.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['padding1']['start'] = self._io.pos()
        self.padding1 = self._io.read_bytes(-(self._io.pos()) % self.header.page_size)
        self._debug['padding1']['end'] = self._io.pos()
        self._debug['vendor_ramdisk']['start'] = self._io.pos()
        self._raw_vendor_ramdisk = self._io.read_bytes(self.header.len_vendor_ramdisk)
        _io__raw_vendor_ramdisk = KaitaiStream(BytesIO(self._raw_vendor_ramdisk))
        self.vendor_ramdisk = AndroidVendorBoot.VendorRamdisk(_io__raw_vendor_ramdisk, self, self._root)
        self._debug['vendor_ramdisk']['end'] = self._io.pos()
        self._debug['padding2']['start'] = self._io.pos()
        self.padding2 = self._io.read_bytes(-(self._io.pos()) % self.header.page_size)
        self._debug['padding2']['end'] = self._io.pos()
        self._debug['dtb']['start'] = self._io.pos()
        self.dtb = self._io.read_bytes(self.header.len_dtb)
        self._debug['dtb']['end'] = self._io.pos()
        self._debug['padding3']['start'] = self._io.pos()
        self.padding3 = self._io.read_bytes(-(self._io.pos()) % self.header.page_size)
        self._debug['padding3']['end'] = self._io.pos()
        if self.header.version == 4:
            pass
            self._debug['vendor_ramdisk_table']['start'] = self._io.pos()
            self._raw_vendor_ramdisk_table = self._io.read_bytes(self.header.v4header.len_vendor_ramdisk_table)
            _io__raw_vendor_ramdisk_table = KaitaiStream(BytesIO(self._raw_vendor_ramdisk_table))
            self.vendor_ramdisk_table = AndroidVendorBoot.RamdiskTable(self.header.v4header.num_vendor_ramdisk_table_entry, self.header.v4header.len_vendor_ramdisk_table_entry, _io__raw_vendor_ramdisk_table, self, self._root)
            self._debug['vendor_ramdisk_table']['end'] = self._io.pos()

        if self.header.version == 4:
            pass
            self._debug['padding4']['start'] = self._io.pos()
            self.padding4 = self._io.read_bytes(-(self._io.pos()) % self.header.page_size)
            self._debug['padding4']['end'] = self._io.pos()

        if self.header.version == 4:
            pass
            self._debug['bootconfig']['start'] = self._io.pos()
            self.bootconfig = self._io.read_bytes(self.header.v4header.len_bootconfig)
            self._debug['bootconfig']['end'] = self._io.pos()

        if self.header.version == 4:
            pass
            self._debug['padding5']['start'] = self._io.pos()
            self.padding5 = self._io.read_bytes(-(self._io.pos()) % self.header.page_size)
            self._debug['padding5']['end'] = self._io.pos()



    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.vendor_ramdisk._fetch_instances()
        if self.header.version == 4:
            pass
            self.vendor_ramdisk_table._fetch_instances()

        if self.header.version == 4:
            pass

        if self.header.version == 4:
            pass

        if self.header.version == 4:
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "page_size", "kernel_address", "ramdisk_address", "len_vendor_ramdisk", "commandline", "tags_address", "name", "len_header", "len_dtb", "dtb_address", "v4header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidVendorBoot.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x56\x4E\x44\x52\x42\x4F\x4F\x54":
                raise kaitaistruct.ValidationNotEqualError(b"\x56\x4E\x44\x52\x42\x4F\x4F\x54", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            if not  ((self.version == 3) or (self.version == 4)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/types/header/seq/1")
            self._debug['page_size']['start'] = self._io.pos()
            self.page_size = self._io.read_u4le()
            self._debug['page_size']['end'] = self._io.pos()
            self._debug['kernel_address']['start'] = self._io.pos()
            self.kernel_address = self._io.read_u4le()
            self._debug['kernel_address']['end'] = self._io.pos()
            self._debug['ramdisk_address']['start'] = self._io.pos()
            self.ramdisk_address = self._io.read_u4le()
            self._debug['ramdisk_address']['end'] = self._io.pos()
            self._debug['len_vendor_ramdisk']['start'] = self._io.pos()
            self.len_vendor_ramdisk = self._io.read_u4le()
            self._debug['len_vendor_ramdisk']['end'] = self._io.pos()
            self._debug['commandline']['start'] = self._io.pos()
            self.commandline = (KaitaiStream.bytes_terminate(self._io.read_bytes(2048), 0, False)).decode(u"ASCII")
            self._debug['commandline']['end'] = self._io.pos()
            self._debug['tags_address']['start'] = self._io.pos()
            self.tags_address = self._io.read_u4le()
            self._debug['tags_address']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['len_dtb']['start'] = self._io.pos()
            self.len_dtb = self._io.read_u4le()
            self._debug['len_dtb']['end'] = self._io.pos()
            self._debug['dtb_address']['start'] = self._io.pos()
            self.dtb_address = self._io.read_u8le()
            self._debug['dtb_address']['end'] = self._io.pos()
            if self.version == 4:
                pass
                self._debug['v4header']['start'] = self._io.pos()
                self.v4header = AndroidVendorBoot.V4header(self._io, self, self._root)
                self._debug['v4header']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.version == 4:
                pass
                self.v4header._fetch_instances()



    class RamdiskTable(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, num_entries, len_entry, _io, _parent=None, _root=None):
            super(AndroidVendorBoot.RamdiskTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_entries = num_entries
            self.len_entry = len_entry
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self._raw_entries = []
            self.entries = []
            for i in range(self.num_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self._raw_entries.append(self._io.read_bytes(self.len_entry))
                _io__raw_entries = KaitaiStream(BytesIO(self._raw_entries[i]))
                self.entries.append(AndroidVendorBoot.RamdiskTableEntryV4(_io__raw_entries, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class RamdiskTableEntryV4(KaitaiStruct):
        SEQ_FIELDS = ["len_ramdisk", "ofs_ramdisk", "ramdisk_type", "name", "board_ids"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidVendorBoot.RamdiskTableEntryV4, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_ramdisk']['start'] = self._io.pos()
            self.len_ramdisk = self._io.read_u4le()
            self._debug['len_ramdisk']['end'] = self._io.pos()
            if not self.len_ramdisk <= self._root.header.len_vendor_ramdisk:
                raise kaitaistruct.ValidationGreaterThanError(self._root.header.len_vendor_ramdisk, self.len_ramdisk, self._io, u"/types/ramdisk_table_entry_v4/seq/0")
            self._debug['ofs_ramdisk']['start'] = self._io.pos()
            self.ofs_ramdisk = self._io.read_u4le()
            self._debug['ofs_ramdisk']['end'] = self._io.pos()
            if not self.ofs_ramdisk <= self._root.header.len_vendor_ramdisk - self.len_ramdisk:
                raise kaitaistruct.ValidationGreaterThanError(self._root.header.len_vendor_ramdisk - self.len_ramdisk, self.ofs_ramdisk, self._io, u"/types/ramdisk_table_entry_v4/seq/1")
            self._debug['ramdisk_type']['start'] = self._io.pos()
            self.ramdisk_type = KaitaiStream.resolve_enum(AndroidVendorBoot.RamdiskTypes, self._io.read_u4le())
            self._debug['ramdisk_type']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['board_ids']['start'] = self._io.pos()
            self._debug['board_ids']['arr'] = []
            self.board_ids = []
            for i in range(16):
                self._debug['board_ids']['arr'].append({'start': self._io.pos()})
                self.board_ids.append(self._io.read_u4le())
                self._debug['board_ids']['arr'][i]['end'] = self._io.pos()

            self._debug['board_ids']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.board_ids)):
                pass

            _ = self.ramdisk
            if hasattr(self, '_m_ramdisk'):
                pass


        @property
        def ramdisk(self):
            if hasattr(self, '_m_ramdisk'):
                return self._m_ramdisk

            io = self._root.vendor_ramdisk._io
            _pos = io.pos()
            io.seek(self.ofs_ramdisk)
            self._debug['_m_ramdisk']['start'] = io.pos()
            self._m_ramdisk = io.read_bytes(self.len_ramdisk)
            self._debug['_m_ramdisk']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_ramdisk', None)


    class V4header(KaitaiStruct):
        SEQ_FIELDS = ["len_vendor_ramdisk_table", "num_vendor_ramdisk_table_entry", "len_vendor_ramdisk_table_entry", "len_bootconfig"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidVendorBoot.V4header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_vendor_ramdisk_table']['start'] = self._io.pos()
            self.len_vendor_ramdisk_table = self._io.read_u4le()
            self._debug['len_vendor_ramdisk_table']['end'] = self._io.pos()
            self._debug['num_vendor_ramdisk_table_entry']['start'] = self._io.pos()
            self.num_vendor_ramdisk_table_entry = self._io.read_u4le()
            self._debug['num_vendor_ramdisk_table_entry']['end'] = self._io.pos()
            self._debug['len_vendor_ramdisk_table_entry']['start'] = self._io.pos()
            self.len_vendor_ramdisk_table_entry = self._io.read_u4le()
            self._debug['len_vendor_ramdisk_table_entry']['end'] = self._io.pos()
            self._debug['len_bootconfig']['start'] = self._io.pos()
            self.len_bootconfig = self._io.read_u4le()
            self._debug['len_bootconfig']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class VendorRamdisk(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidVendorBoot.VendorRamdisk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes_full()
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



