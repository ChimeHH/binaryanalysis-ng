# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Plf(KaitaiStruct):
    """Parrot (drone manufacturer) has its own update files that have some sort
    of file system (PLF) with various types of partitions. Only some of these
    partitions are somewhat documented. It seems that there is also some
    inconsistency in the formats, but there is too little documentation.
    Not all data from this format might be unpacked in a sane way.
    
    .. seealso::
       Source - http://embedded-software.blogspot.com/2010/12/plf-file-format.html
    
    
    .. seealso::
       Source - https://web.archive.org/web/20170109192314/http://thecyberrecce.net/2017/01/09/reversing-the-parrot-skycontroller-firmware/
    
    
    .. seealso::
       Source - https://github.com/Parrot-Developers/libARUpdater/blob/5b3667dd97c4ba0e38cb5f9a477773012c1e55d3/Sources/ARUPDATER_Plf.h
    
    
    .. seealso::
       Source - https://github.com/Parrot-Developers/libpuf/blob/master/src/libpuf_plf.h
    
    
    .. seealso::
       Source - https://github.com/scorp2kk/ardrone-tool
    """

    class FileTypes(IntEnum):
        unknown = 0
        executable = 1
        archive = 2

    class SectionTypes(IntEnum):
        section0 = 0
        section1 = 1
        section2 = 2
        section3 = 3
        section4 = 4
        section5 = 5
        section6 = 6
        section7 = 7
        section8 = 8
        section9 = 9
        section10 = 10
        section11 = 11
        section12 = 12
    SEQ_FIELDS = ["header", "padding", "partitions"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Plf, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Plf.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['padding']['start'] = self._io.pos()
        self.padding = self._io.read_bytes(self.header.len_header - 56)
        self._debug['padding']['end'] = self._io.pos()
        self._debug['partitions']['start'] = self._io.pos()
        self._raw_partitions = self._io.read_bytes(self.header.len_file - self.header.len_header)
        _io__raw_partitions = KaitaiStream(BytesIO(self._raw_partitions))
        self.partitions = Plf.Partitions(_io__raw_partitions, self, self._root)
        self._debug['partitions']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.partitions._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "header_version", "len_header", "len_entry_header", "file_type", "entry_point", "target_platform", "target_application", "hardware_compatibility", "version", "language_zone", "len_file"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Plf.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x50\x4C\x46\x21":
                raise kaitaistruct.ValidationNotEqualError(b"\x50\x4C\x46\x21", self.magic, self._io, u"/types/header/seq/0")
            self._debug['header_version']['start'] = self._io.pos()
            self.header_version = self._io.read_u4le()
            self._debug['header_version']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['len_entry_header']['start'] = self._io.pos()
            self.len_entry_header = self._io.read_u4le()
            self._debug['len_entry_header']['end'] = self._io.pos()
            if not self.len_entry_header == 20:
                raise kaitaistruct.ValidationNotEqualError(20, self.len_entry_header, self._io, u"/types/header/seq/3")
            self._debug['file_type']['start'] = self._io.pos()
            self.file_type = KaitaiStream.resolve_enum(Plf.FileTypes, self._io.read_u4le())
            self._debug['file_type']['end'] = self._io.pos()
            self._debug['entry_point']['start'] = self._io.pos()
            self.entry_point = self._io.read_u4le()
            self._debug['entry_point']['end'] = self._io.pos()
            self._debug['target_platform']['start'] = self._io.pos()
            self.target_platform = self._io.read_u4le()
            self._debug['target_platform']['end'] = self._io.pos()
            self._debug['target_application']['start'] = self._io.pos()
            self.target_application = self._io.read_u4le()
            self._debug['target_application']['end'] = self._io.pos()
            self._debug['hardware_compatibility']['start'] = self._io.pos()
            self.hardware_compatibility = self._io.read_u4le()
            self._debug['hardware_compatibility']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = Plf.Version(self._io, self, self._root)
            self._debug['version']['end'] = self._io.pos()
            self._debug['language_zone']['start'] = self._io.pos()
            self.language_zone = self._io.read_u4le()
            self._debug['language_zone']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.version._fetch_instances()


    class Partition(KaitaiStruct):
        SEQ_FIELDS = ["section_type", "len_section", "crc32", "load_address", "uncompressed_size", "data", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Plf.Partition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['section_type']['start'] = self._io.pos()
            self.section_type = KaitaiStream.resolve_enum(Plf.SectionTypes, self._io.read_u4le())
            self._debug['section_type']['end'] = self._io.pos()
            self._debug['len_section']['start'] = self._io.pos()
            self.len_section = self._io.read_u4le()
            self._debug['len_section']['end'] = self._io.pos()
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['load_address']['start'] = self._io.pos()
            self.load_address = self._io.read_u4le()
            self._debug['load_address']['end'] = self._io.pos()
            self._debug['uncompressed_size']['start'] = self._io.pos()
            self.uncompressed_size = self._io.read_u4le()
            self._debug['uncompressed_size']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            _on = self.section_type
            if _on == Plf.SectionTypes.section11:
                pass
                self._raw_data = self._io.read_bytes(self.len_section)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Plf.PartitionTable(_io__raw_data, self, self._root)
            else:
                pass
                self.data = self._io.read_bytes(self.len_section)
            self._debug['data']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self.len_section) % 4)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.section_type
            if _on == Plf.SectionTypes.section11:
                pass
                self.data._fetch_instances()
            else:
                pass


    class PartitionEntry(KaitaiStruct):
        SEQ_FIELDS = ["device", "volume_type", "volume", "unknown", "len_volume", "volume_action", "volume_name", "mount_name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Plf.PartitionEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['device']['start'] = self._io.pos()
            self.device = self._io.read_u2le()
            self._debug['device']['end'] = self._io.pos()
            self._debug['volume_type']['start'] = self._io.pos()
            self.volume_type = self._io.read_u2le()
            self._debug['volume_type']['end'] = self._io.pos()
            self._debug['volume']['start'] = self._io.pos()
            self.volume = self._io.read_u2le()
            self._debug['volume']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_u2le()
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['len_volume']['start'] = self._io.pos()
            self.len_volume = self._io.read_u4le()
            self._debug['len_volume']['end'] = self._io.pos()
            self._debug['volume_action']['start'] = self._io.pos()
            self.volume_action = self._io.read_u4le()
            self._debug['volume_action']['end'] = self._io.pos()
            self._debug['volume_name']['start'] = self._io.pos()
            self.volume_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['volume_name']['end'] = self._io.pos()
            self._debug['mount_name']['start'] = self._io.pos()
            self.mount_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['mount_name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PartitionTable(KaitaiStruct):
        SEQ_FIELDS = ["table_version", "major_version", "minor_version", "bugfix_version", "unknown1", "unknown2", "unknown3", "unknown4", "unknown5", "num_entries", "partition_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Plf.PartitionTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['table_version']['start'] = self._io.pos()
            self.table_version = self._io.read_u4le()
            self._debug['table_version']['end'] = self._io.pos()
            self._debug['major_version']['start'] = self._io.pos()
            self.major_version = self._io.read_u4le()
            self._debug['major_version']['end'] = self._io.pos()
            self._debug['minor_version']['start'] = self._io.pos()
            self.minor_version = self._io.read_u4le()
            self._debug['minor_version']['end'] = self._io.pos()
            self._debug['bugfix_version']['start'] = self._io.pos()
            self.bugfix_version = self._io.read_u4le()
            self._debug['bugfix_version']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u4le()
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_u4le()
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['unknown3']['start'] = self._io.pos()
            self.unknown3 = self._io.read_u4le()
            self._debug['unknown3']['end'] = self._io.pos()
            self._debug['unknown4']['start'] = self._io.pos()
            self.unknown4 = self._io.read_u4le()
            self._debug['unknown4']['end'] = self._io.pos()
            self._debug['unknown5']['start'] = self._io.pos()
            self.unknown5 = self._io.read_u4le()
            self._debug['unknown5']['end'] = self._io.pos()
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u4le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['partition_entries']['start'] = self._io.pos()
            self._debug['partition_entries']['arr'] = []
            self.partition_entries = []
            for i in range(self.num_entries):
                self._debug['partition_entries']['arr'].append({'start': self._io.pos()})
                self.partition_entries.append(Plf.PartitionEntry(self._io, self, self._root))
                self._debug['partition_entries']['arr'][i]['end'] = self._io.pos()

            self._debug['partition_entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.partition_entries)):
                pass
                self.partition_entries[i]._fetch_instances()



    class Partitions(KaitaiStruct):
        SEQ_FIELDS = ["partitions"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Plf.Partitions, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['partitions']['start'] = self._io.pos()
            self._debug['partitions']['arr'] = []
            self.partitions = []
            i = 0
            while not self._io.is_eof():
                self._debug['partitions']['arr'].append({'start': self._io.pos()})
                self.partitions.append(Plf.Partition(self._io, self, self._root))
                self._debug['partitions']['arr'][len(self.partitions) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['partitions']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.partitions)):
                pass
                self.partitions[i]._fetch_instances()



    class Version(KaitaiStruct):
        SEQ_FIELDS = ["major_version", "minor_version", "bugfix_version"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Plf.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['major_version']['start'] = self._io.pos()
            self.major_version = self._io.read_u4le()
            self._debug['major_version']['end'] = self._io.pos()
            self._debug['minor_version']['start'] = self._io.pos()
            self.minor_version = self._io.read_u4le()
            self._debug['minor_version']['end'] = self._io.pos()
            self._debug['bugfix_version']['start'] = self._io.pos()
            self.bugfix_version = self._io.read_u4le()
            self._debug['bugfix_version']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



