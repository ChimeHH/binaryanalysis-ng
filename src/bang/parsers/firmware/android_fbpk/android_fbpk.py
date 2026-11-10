# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class AndroidFbpk(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/anestisb/qc_image_unpacker/blob/master/src/packed_image.h
    
    
    .. seealso::
       Source - https://source.android.com/devices/bootloader/tools/pixel/fw_unpack/fbpack.py
    """

    class FbptTypes(IntEnum):
        mbr = 0
        gpt = 1
        gpt_backup = 2
    SEQ_FIELDS = ["header", "body"]
    def __init__(self, _io, _parent=None, _root=None):
        super(AndroidFbpk, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = AndroidFbpk.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['body']['start'] = self._io.pos()
        _on = self.header.version
        if _on == 1:
            pass
            self.body = AndroidFbpk.Bodyv1(self._io, self, self._root)
        elif _on == 2:
            pass
            self.body = AndroidFbpk.Bodyv2(self._io, self, self._root)
        self._debug['body']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        _on = self.header.version
        if _on == 1:
            pass
            self.body._fetch_instances()
        elif _on == 2:
            pass
            self.body._fetch_instances()

    class Bodyv1(KaitaiStruct):
        SEQ_FIELDS = ["img_version", "num_entries", "total_file_size", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidFbpk.Bodyv1, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['img_version']['start'] = self._io.pos()
            self.img_version = self._io.read_bytes(68)
            self._debug['img_version']['end'] = self._io.pos()
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u4le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['total_file_size']['start'] = self._io.pos()
            self.total_file_size = self._io.read_u4le()
            self._debug['total_file_size']['end'] = self._io.pos()
            if self.num_entries != 0:
                pass
                self._debug['entries']['start'] = self._io.pos()
                self._debug['entries']['arr'] = []
                self.entries = []
                i = 0
                while True:
                    self._debug['entries']['arr'].append({'start': self._io.pos()})
                    _ = AndroidFbpk.Entryv1(self._io, self, self._root)
                    self.entries.append(_)
                    self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                    if  ((i == self.num_entries - 1) or (self._io.is_eof())) :
                        break
                    i += 1
                self._debug['entries']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.num_entries != 0:
                pass
                for i in range(len(self.entries)):
                    pass
                    self.entries[i]._fetch_instances()




    class Bodyv2(KaitaiStruct):
        SEQ_FIELDS = ["len_header", "len_entry", "chip_id", "img_version", "slot_type", "data_align", "num_entries", "total_file_size", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidFbpk.Bodyv2, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['len_entry']['start'] = self._io.pos()
            self.len_entry = self._io.read_u4le()
            self._debug['len_entry']['end'] = self._io.pos()
            self._debug['chip_id']['start'] = self._io.pos()
            self.chip_id = self._io.read_bytes(16)
            self._debug['chip_id']['end'] = self._io.pos()
            self._debug['img_version']['start'] = self._io.pos()
            self.img_version = self._io.read_bytes(64)
            self._debug['img_version']['end'] = self._io.pos()
            self._debug['slot_type']['start'] = self._io.pos()
            self.slot_type = self._io.read_u4le()
            self._debug['slot_type']['end'] = self._io.pos()
            self._debug['data_align']['start'] = self._io.pos()
            self.data_align = self._io.read_u4le()
            self._debug['data_align']['end'] = self._io.pos()
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u4le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['total_file_size']['start'] = self._io.pos()
            self.total_file_size = self._io.read_u4le()
            self._debug['total_file_size']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self._raw_entries = []
            self.entries = []
            for i in range(self.num_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self._raw_entries.append(self._io.read_bytes(self.len_entry))
                _io__raw_entries = KaitaiStream(BytesIO(self._raw_entries[i]))
                self.entries.append(AndroidFbpk.Entryv2(self.total_file_size, _io__raw_entries, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class Entryv1(KaitaiStruct):
        SEQ_FIELDS = ["type", "partition_name", "padding1", "len_partition", "padding2", "next_offset", "checksum", "partition", "padding3"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidFbpk.Entryv1, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u4le()
            self._debug['type']['end'] = self._io.pos()
            self._debug['partition_name']['start'] = self._io.pos()
            self.partition_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['partition_name']['end'] = self._io.pos()
            self._debug['padding1']['start'] = self._io.pos()
            self.padding1 = self._io.read_u4le()
            self._debug['padding1']['end'] = self._io.pos()
            self._debug['len_partition']['start'] = self._io.pos()
            self.len_partition = self._io.read_u4le()
            self._debug['len_partition']['end'] = self._io.pos()
            self._debug['padding2']['start'] = self._io.pos()
            self.padding2 = self._io.read_u4le()
            self._debug['padding2']['end'] = self._io.pos()
            self._debug['next_offset']['start'] = self._io.pos()
            self.next_offset = self._io.read_u4le()
            self._debug['next_offset']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_u4le()
            self._debug['checksum']['end'] = self._io.pos()
            self._debug['partition']['start'] = self._io.pos()
            self.partition = self._io.read_bytes(self.len_partition)
            self._debug['partition']['end'] = self._io.pos()
            if self.next_offset <= self._parent.total_file_size:
                pass
                self._debug['padding3']['start'] = self._io.pos()
                self.padding3 = self._io.read_bytes(self.next_offset - self._io.pos())
                self._debug['padding3']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.next_offset <= self._parent.total_file_size:
                pass



    class Entryv2(KaitaiStruct):
        SEQ_FIELDS = ["type", "partition_name", "product_name", "ofs_partition", "len_partition", "slotted", "crc32"]
        def __init__(self, total_file_size, _io, _parent=None, _root=None):
            super(AndroidFbpk.Entryv2, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.total_file_size = total_file_size
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_bytes(4)
            self._debug['type']['end'] = self._io.pos()
            self._debug['partition_name']['start'] = self._io.pos()
            self.partition_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(36), 0, False)).decode(u"UTF-8")
            self._debug['partition_name']['end'] = self._io.pos()
            self._debug['product_name']['start'] = self._io.pos()
            self.product_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(40), 0, False)).decode(u"UTF-8")
            self._debug['product_name']['end'] = self._io.pos()
            self._debug['ofs_partition']['start'] = self._io.pos()
            self.ofs_partition = self._io.read_u8le()
            self._debug['ofs_partition']['end'] = self._io.pos()
            if not self.ofs_partition <= self.total_file_size:
                raise kaitaistruct.ValidationGreaterThanError(self.total_file_size, self.ofs_partition, self._io, u"/types/entryv2/seq/3")
            self._debug['len_partition']['start'] = self._io.pos()
            self.len_partition = self._io.read_u8le()
            self._debug['len_partition']['end'] = self._io.pos()
            if not self.len_partition <= self.total_file_size - self.ofs_partition:
                raise kaitaistruct.ValidationGreaterThanError(self.total_file_size - self.ofs_partition, self.len_partition, self._io, u"/types/entryv2/seq/4")
            self._debug['slotted']['start'] = self._io.pos()
            self.slotted = self._io.read_u4le()
            self._debug['slotted']['end'] = self._io.pos()
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_bytes(4)
            self._debug['crc32']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.magic
            if hasattr(self, '_m_magic'):
                pass

            _ = self.partition
            if hasattr(self, '_m_partition'):
                pass

            _ = self.partition_parsed
            if hasattr(self, '_m_partition_parsed'):
                pass
                _on = self.magic
                if _on == 1414545990:
                    pass
                    self._m_partition_parsed._fetch_instances()
                else:
                    pass


        @property
        def magic(self):
            if hasattr(self, '_m_magic'):
                return self._m_magic

            if self.len_partition >= 4:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_partition)
                self._debug['_m_magic']['start'] = io.pos()
                self._m_magic = io.read_u4le()
                self._debug['_m_magic']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_magic', None)

        @property
        def partition(self):
            if hasattr(self, '_m_partition'):
                return self._m_partition

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_partition)
            self._debug['_m_partition']['start'] = io.pos()
            self._m_partition = io.read_bytes(self.len_partition)
            self._debug['_m_partition']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_partition', None)

        @property
        def partition_parsed(self):
            if hasattr(self, '_m_partition_parsed'):
                return self._m_partition_parsed

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_partition)
            self._debug['_m_partition_parsed']['start'] = io.pos()
            _on = self.magic
            if _on == 1414545990:
                pass
                self._raw__m_partition_parsed = io.read_bytes(self.len_partition)
                _io__raw__m_partition_parsed = KaitaiStream(BytesIO(self._raw__m_partition_parsed))
                self._m_partition_parsed = AndroidFbpk.Fbptv2(_io__raw__m_partition_parsed, self, self._root)
            else:
                pass
                self._m_partition_parsed = io.read_bytes(self.len_partition)
            self._debug['_m_partition_parsed']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_partition_parsed', None)


    class FbptEntry(KaitaiStruct):
        SEQ_FIELDS = ["size", "unknown", "attributes", "partition_name", "type_guid", "partition_guid", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidFbpk.FbptEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(4)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['attributes']['start'] = self._io.pos()
            self.attributes = self._io.read_u4le()
            self._debug['attributes']['end'] = self._io.pos()
            self._debug['partition_name']['start'] = self._io.pos()
            self.partition_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(36), 0, False)).decode(u"UTF-8")
            self._debug['partition_name']['end'] = self._io.pos()
            self._debug['type_guid']['start'] = self._io.pos()
            self.type_guid = (KaitaiStream.bytes_terminate(self._io.read_bytes(37), 0, False)).decode(u"UTF-8")
            self._debug['type_guid']['end'] = self._io.pos()
            self._debug['partition_guid']['start'] = self._io.pos()
            self.partition_guid = (KaitaiStream.bytes_terminate(self._io.read_bytes(37), 0, False)).decode(u"UTF-8")
            self._debug['partition_guid']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(2)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class FbptEntryv2(KaitaiStruct):
        SEQ_FIELDS = ["size", "unknown", "attributes", "partition_name", "type_guid", "partition_guid", "file_system_type"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidFbpk.FbptEntryv2, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(4)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['attributes']['start'] = self._io.pos()
            self.attributes = self._io.read_u4le()
            self._debug['attributes']['end'] = self._io.pos()
            self._debug['partition_name']['start'] = self._io.pos()
            self.partition_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(36), 0, False)).decode(u"UTF-8")
            self._debug['partition_name']['end'] = self._io.pos()
            self._debug['type_guid']['start'] = self._io.pos()
            self.type_guid = (KaitaiStream.bytes_terminate(self._io.read_bytes(37), 0, False)).decode(u"UTF-8")
            self._debug['type_guid']['end'] = self._io.pos()
            self._debug['partition_guid']['start'] = self._io.pos()
            self.partition_guid = (KaitaiStream.bytes_terminate(self._io.read_bytes(37), 0, False)).decode(u"UTF-8")
            self._debug['partition_guid']['end'] = self._io.pos()
            self._debug['file_system_type']['start'] = self._io.pos()
            self.file_system_type = self._io.read_bytes(14)
            self._debug['file_system_type']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Fbptv1(KaitaiStruct):
        SEQ_FIELDS = ["magic", "type", "lun", "unknown1", "num_partitions", "unknown2", "padding", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidFbpk.Fbptv1, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x46\x42\x50\x54":
                raise kaitaistruct.ValidationNotEqualError(b"\x46\x42\x50\x54", self.magic, self._io, u"/types/fbptv1/seq/0")
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(AndroidFbpk.FbptTypes, self._io.read_u4le())
            self._debug['type']['end'] = self._io.pos()
            self._debug['lun']['start'] = self._io.pos()
            self.lun = self._io.read_u4le()
            self._debug['lun']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_bytes(4)
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['num_partitions']['start'] = self._io.pos()
            self.num_partitions = self._io.read_u4le()
            self._debug['num_partitions']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_bytes(37)
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(3)
            self._debug['padding']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(AndroidFbpk.FbptEntry(self._io, self, self._root))
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class Fbptv2(KaitaiStruct):
        SEQ_FIELDS = ["magic", "type", "lun", "unknown1", "num_partitions", "unknown2", "padding", "unknown3", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidFbpk.Fbptv2, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x46\x42\x50\x54":
                raise kaitaistruct.ValidationNotEqualError(b"\x46\x42\x50\x54", self.magic, self._io, u"/types/fbptv2/seq/0")
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(AndroidFbpk.FbptTypes, self._io.read_u4le())
            self._debug['type']['end'] = self._io.pos()
            self._debug['lun']['start'] = self._io.pos()
            self.lun = self._io.read_u4le()
            self._debug['lun']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_bytes(4)
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['num_partitions']['start'] = self._io.pos()
            self.num_partitions = self._io.read_u4le()
            self._debug['num_partitions']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_bytes(37)
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(3)
            self._debug['padding']['end'] = self._io.pos()
            self._debug['unknown3']['start'] = self._io.pos()
            self.unknown3 = self._io.read_bytes(4)
            self._debug['unknown3']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_partitions):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(AndroidFbpk.FbptEntryv2(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidFbpk.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x46\x42\x50\x4B":
                raise kaitaistruct.ValidationNotEqualError(b"\x46\x42\x50\x4B", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            if not  ((self.version == 1) or (self.version == 2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/types/header/seq/1")


        def _fetch_instances(self):
            pass



