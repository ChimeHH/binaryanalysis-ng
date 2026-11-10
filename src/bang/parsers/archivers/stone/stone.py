# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Stone(KaitaiStruct):
    """
    .. seealso::
       <https://github.com/serpent-os/libmoss/blob/841a6d67/source/moss/format/binary/archive_header.d>
    """

    class Compression(IntEnum):
        unknown = 0
        no_compression = 1
        zstd = 2

    class FileTypes(IntEnum):
        unknown = 0
        binary = 1
        delta = 2
        repository = 3
        build_manifest = 4

    class PayloadType(IntEnum):
        unknown = 0
        meta = 1
        content = 2
        layout = 3
        index = 4
        attributes = 5
        dumb = 6

    class RecordTags(IntEnum):
        unknown = 0
        name = 1
        architecture = 2
        version = 3
        summary = 4
        description = 5
        homepage = 6
        source_id = 7
        depends = 8
        provides = 9
        conflicts = 10
        release = 11
        license = 12
        build_release = 13
        package_uri = 14
        package_hash = 15
        package_size = 16
        build_depends = 17
        source_uri = 18
        source_path = 19
        source_ref = 20

    class RecordTypes(IntEnum):
        unknown = 0
        int8 = 1
        uint8 = 2
        int16 = 3
        uint16 = 4
        int32 = 5
        uint32 = 6
        int64 = 7
        uint64 = 8
        string = 9
        dependency = 10
        provider = 11
    SEQ_FIELDS = ["header", "payloads"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Stone, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(32)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Stone.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['payloads']['start'] = self._io.pos()
        self._debug['payloads']['arr'] = []
        self.payloads = []
        for i in range(self.header.num_payloads):
            self._debug['payloads']['arr'].append({'start': self._io.pos()})
            self.payloads.append(Stone.Payload(self._io, self, self._root))
            self._debug['payloads']['arr'][i]['end'] = self._io.pos()

        self._debug['payloads']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.payloads)):
            pass
            self.payloads[i]._fetch_instances()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["signature", "num_payloads", "integrity_check", "type", "version"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Stone.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(4)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x00\x6D\x6F\x73":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x6D\x6F\x73", self.signature, self._io, u"/types/header/seq/0")
            self._debug['num_payloads']['start'] = self._io.pos()
            self.num_payloads = self._io.read_u2be()
            self._debug['num_payloads']['end'] = self._io.pos()
            self._debug['integrity_check']['start'] = self._io.pos()
            self.integrity_check = self._io.read_bytes(21)
            self._debug['integrity_check']['end'] = self._io.pos()
            if not self.integrity_check == b"\x00\x00\x01\x00\x00\x02\x00\x00\x03\x00\x00\x04\x00\x00\x05\x00\x00\x06\x00\x00\x07":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x01\x00\x00\x02\x00\x00\x03\x00\x00\x04\x00\x00\x05\x00\x00\x06\x00\x00\x07", self.integrity_check, self._io, u"/types/header/seq/2")
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Stone.FileTypes, self._io.read_u1())
            self._debug['type']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4be()
            self._debug['version']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class IndexEntries(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Stone.IndexEntries, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Stone.IndexEntry(self._io, self, self._root))
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class IndexEntry(KaitaiStruct):
        SEQ_FIELDS = ["ofs_start", "ofs_end", "hash_digest"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Stone.IndexEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_start']['start'] = self._io.pos()
            self.ofs_start = self._io.read_u8be()
            self._debug['ofs_start']['end'] = self._io.pos()
            self._debug['ofs_end']['start'] = self._io.pos()
            self.ofs_end = self._io.read_u8be()
            self._debug['ofs_end']['end'] = self._io.pos()
            self._debug['hash_digest']['start'] = self._io.pos()
            self.hash_digest = self._io.read_bytes(16)
            self._debug['hash_digest']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def len_file(self):
            if hasattr(self, '_m_len_file'):
                return self._m_len_file

            self._m_len_file = self.ofs_end - self.ofs_start
            return getattr(self, '_m_len_file', None)


    class LayoutEntries(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Stone.LayoutEntries, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Stone.LayoutEntry(self._io, self, self._root))
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class LayoutEntry(KaitaiStruct):

        class FileType(IntEnum):
            unknown = 0
            regular = 1
            symlink = 2
            directory = 3
            character_device = 4
            block_device = 5
            fifo = 6
            socket = 7
        SEQ_FIELDS = ["uid", "gid", "mode", "tag", "len_source", "len_target", "file_type", "padding", "source", "target"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Stone.LayoutEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['uid']['start'] = self._io.pos()
            self.uid = self._io.read_u4be()
            self._debug['uid']['end'] = self._io.pos()
            self._debug['gid']['start'] = self._io.pos()
            self.gid = self._io.read_u4be()
            self._debug['gid']['end'] = self._io.pos()
            self._debug['mode']['start'] = self._io.pos()
            self.mode = self._io.read_u4be()
            self._debug['mode']['end'] = self._io.pos()
            self._debug['tag']['start'] = self._io.pos()
            self.tag = self._io.read_u4be()
            self._debug['tag']['end'] = self._io.pos()
            self._debug['len_source']['start'] = self._io.pos()
            self.len_source = self._io.read_u2be()
            self._debug['len_source']['end'] = self._io.pos()
            self._debug['len_target']['start'] = self._io.pos()
            self.len_target = self._io.read_u2be()
            self._debug['len_target']['end'] = self._io.pos()
            self._debug['file_type']['start'] = self._io.pos()
            self.file_type = KaitaiStream.resolve_enum(Stone.LayoutEntry.FileType, self._io.read_u1())
            self._debug['file_type']['end'] = self._io.pos()
            if not  ((self.file_type == Stone.LayoutEntry.FileType.regular) or (self.file_type == Stone.LayoutEntry.FileType.symlink) or (self.file_type == Stone.LayoutEntry.FileType.directory) or (self.file_type == Stone.LayoutEntry.FileType.character_device) or (self.file_type == Stone.LayoutEntry.FileType.block_device) or (self.file_type == Stone.LayoutEntry.FileType.fifo) or (self.file_type == Stone.LayoutEntry.FileType.socket)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.file_type, self._io, u"/types/layout_entry/seq/6")
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(11)
            self._debug['padding']['end'] = self._io.pos()
            self._debug['source']['start'] = self._io.pos()
            self.source = self._io.read_bytes(self.len_source)
            self._debug['source']['end'] = self._io.pos()
            self._debug['target']['start'] = self._io.pos()
            self.target = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_target), 0, False)).decode(u"UTF-8")
            self._debug['target']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class MetaRecord(KaitaiStruct):
        SEQ_FIELDS = ["len_record", "record_tag", "record_type", "reserved", "record"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Stone.MetaRecord, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_record']['start'] = self._io.pos()
            self.len_record = self._io.read_u4be()
            self._debug['len_record']['end'] = self._io.pos()
            self._debug['record_tag']['start'] = self._io.pos()
            self.record_tag = KaitaiStream.resolve_enum(Stone.RecordTags, self._io.read_u2be())
            self._debug['record_tag']['end'] = self._io.pos()
            if not  ((self.record_tag == Stone.RecordTags.name) or (self.record_tag == Stone.RecordTags.architecture) or (self.record_tag == Stone.RecordTags.version) or (self.record_tag == Stone.RecordTags.summary) or (self.record_tag == Stone.RecordTags.description) or (self.record_tag == Stone.RecordTags.homepage) or (self.record_tag == Stone.RecordTags.source_id) or (self.record_tag == Stone.RecordTags.depends) or (self.record_tag == Stone.RecordTags.provides) or (self.record_tag == Stone.RecordTags.conflicts) or (self.record_tag == Stone.RecordTags.release) or (self.record_tag == Stone.RecordTags.license) or (self.record_tag == Stone.RecordTags.build_release) or (self.record_tag == Stone.RecordTags.package_uri) or (self.record_tag == Stone.RecordTags.package_hash) or (self.record_tag == Stone.RecordTags.package_size) or (self.record_tag == Stone.RecordTags.build_depends) or (self.record_tag == Stone.RecordTags.source_uri) or (self.record_tag == Stone.RecordTags.source_path) or (self.record_tag == Stone.RecordTags.source_ref)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.record_tag, self._io, u"/types/meta_record/seq/1")
            self._debug['record_type']['start'] = self._io.pos()
            self.record_type = KaitaiStream.resolve_enum(Stone.RecordTypes, self._io.read_u1())
            self._debug['record_type']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(1)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['record']['start'] = self._io.pos()
            _on = self.record_type
            if _on == Stone.RecordTypes.int16:
                pass
                self.record = self._io.read_s2be()
            elif _on == Stone.RecordTypes.int32:
                pass
                self.record = self._io.read_s4be()
            elif _on == Stone.RecordTypes.int64:
                pass
                self.record = self._io.read_s8be()
            elif _on == Stone.RecordTypes.int8:
                pass
                self.record = self._io.read_s1()
            elif _on == Stone.RecordTypes.string:
                pass
                self.record = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_record), 0, False)).decode(u"UTF-8")
            elif _on == Stone.RecordTypes.uint16:
                pass
                self.record = self._io.read_u2be()
            elif _on == Stone.RecordTypes.uint32:
                pass
                self.record = self._io.read_u4be()
            elif _on == Stone.RecordTypes.uint64:
                pass
                self.record = self._io.read_u8be()
            elif _on == Stone.RecordTypes.uint8:
                pass
                self.record = self._io.read_u1()
            else:
                pass
                self.record = self._io.read_bytes(self.len_record)
            self._debug['record']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.record_type
            if _on == Stone.RecordTypes.int16:
                pass
            elif _on == Stone.RecordTypes.int32:
                pass
            elif _on == Stone.RecordTypes.int64:
                pass
            elif _on == Stone.RecordTypes.int8:
                pass
            elif _on == Stone.RecordTypes.string:
                pass
            elif _on == Stone.RecordTypes.uint16:
                pass
            elif _on == Stone.RecordTypes.uint32:
                pass
            elif _on == Stone.RecordTypes.uint64:
                pass
            elif _on == Stone.RecordTypes.uint8:
                pass
            else:
                pass


    class MetaRecords(KaitaiStruct):
        SEQ_FIELDS = ["records"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Stone.MetaRecords, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['records']['start'] = self._io.pos()
            self._debug['records']['arr'] = []
            self.records = []
            i = 0
            while not self._io.is_eof():
                self._debug['records']['arr'].append({'start': self._io.pos()})
                self.records.append(Stone.MetaRecord(self._io, self, self._root))
                self._debug['records']['arr'][len(self.records) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['records']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.records)):
                pass
                self.records[i]._fetch_instances()



    class Payload(KaitaiStruct):
        SEQ_FIELDS = ["len_data", "len_usable_data", "xxhash3_64", "num_records", "payload_version", "type", "compression", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Stone.Payload, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u8be()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['len_usable_data']['start'] = self._io.pos()
            self.len_usable_data = self._io.read_u8be()
            self._debug['len_usable_data']['end'] = self._io.pos()
            self._debug['xxhash3_64']['start'] = self._io.pos()
            self.xxhash3_64 = self._io.read_bytes(8)
            self._debug['xxhash3_64']['end'] = self._io.pos()
            self._debug['num_records']['start'] = self._io.pos()
            self.num_records = self._io.read_u4be()
            self._debug['num_records']['end'] = self._io.pos()
            self._debug['payload_version']['start'] = self._io.pos()
            self.payload_version = self._io.read_u2be()
            self._debug['payload_version']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Stone.PayloadType, self._io.read_u1())
            self._debug['type']['end'] = self._io.pos()
            self._debug['compression']['start'] = self._io.pos()
            self.compression = KaitaiStream.resolve_enum(Stone.Compression, self._io.read_u1())
            self._debug['compression']['end'] = self._io.pos()
            if not  ((self.compression == Stone.Compression.no_compression) or (self.compression == Stone.Compression.zstd)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.compression, self._io, u"/types/payload/seq/6")
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



