# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import bytes_with_io
from .bytes_with_io import *
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Exfat(KaitaiStruct):
    """
    .. seealso::
       Source - https://learn.microsoft.com/en-us/windows/win32/fileio/exfat-specification
    """

    class TypeImportance(IntEnum):
        critical = 0
        benign = 1
    SEQ_FIELDS = ["main_boot_region", "backup_boot_region", "fat_region", "data_region"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Exfat, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['main_boot_region']['start'] = self._io.pos()
        self._raw_main_boot_region = self._io.read_bytes(self.len_sector * 12)
        _io__raw_main_boot_region = KaitaiStream(BytesIO(self._raw_main_boot_region))
        self.main_boot_region = Exfat.BootRegion(_io__raw_main_boot_region, self, self._root)
        self._debug['main_boot_region']['end'] = self._io.pos()
        self._debug['backup_boot_region']['start'] = self._io.pos()
        self._raw_backup_boot_region = self._io.read_bytes(self.len_sector * 12)
        _io__raw_backup_boot_region = KaitaiStream(BytesIO(self._raw_backup_boot_region))
        self.backup_boot_region = Exfat.BootRegion(_io__raw_backup_boot_region, self, self._root)
        self._debug['backup_boot_region']['end'] = self._io.pos()
        self._debug['fat_region']['start'] = self._io.pos()
        self._raw_fat_region = self._io.read_bytes(((self.main_boot_region.boot_sector.ofs_fat + self.main_boot_region.boot_sector.len_fat * self.main_boot_region.boot_sector.num_fat) - 24) * self.len_sector)
        _io__raw_fat_region = KaitaiStream(BytesIO(self._raw_fat_region))
        self.fat_region = Exfat.FatRegion(_io__raw_fat_region, self, self._root)
        self._debug['fat_region']['end'] = self._io.pos()
        self._debug['data_region']['start'] = self._io.pos()
        self._raw_data_region = self._io.read_bytes((self.main_boot_region.boot_sector.len_volume - (self.main_boot_region.boot_sector.ofs_fat + self.main_boot_region.boot_sector.len_fat * self.main_boot_region.boot_sector.num_fat)) * self.len_sector)
        _io__raw_data_region = KaitaiStream(BytesIO(self._raw_data_region))
        self.data_region = Exfat.DataRegion(_io__raw_data_region, self, self._root)
        self._debug['data_region']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.main_boot_region._fetch_instances()
        self.backup_boot_region._fetch_instances()
        self.fat_region._fetch_instances()
        self.data_region._fetch_instances()
        _ = self.bytes_per_sector_shift
        if hasattr(self, '_m_bytes_per_sector_shift'):
            pass

        _ = self.root_directory
        if hasattr(self, '_m_root_directory'):
            pass
            self._m_root_directory._fetch_instances()

        _ = self.sectors_per_cluster_shift
        if hasattr(self, '_m_sectors_per_cluster_shift'):
            pass


    class BootRegion(KaitaiStruct):
        SEQ_FIELDS = ["boot_sector", "extended_boot_sectors", "oem_parameters", "reserved", "boot_checksum"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Exfat.BootRegion, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['boot_sector']['start'] = self._io.pos()
            self._raw_boot_sector = self._io.read_bytes(self._root.len_sector)
            _io__raw_boot_sector = KaitaiStream(BytesIO(self._raw_boot_sector))
            self.boot_sector = Exfat.BootSector(_io__raw_boot_sector, self, self._root)
            self._debug['boot_sector']['end'] = self._io.pos()
            self._debug['extended_boot_sectors']['start'] = self._io.pos()
            self._debug['extended_boot_sectors']['arr'] = []
            self.extended_boot_sectors = []
            for i in range(8):
                self._debug['extended_boot_sectors']['arr'].append({'start': self._io.pos()})
                self.extended_boot_sectors.append(self._io.read_bytes(self._root.len_sector))
                self._debug['extended_boot_sectors']['arr'][i]['end'] = self._io.pos()

            self._debug['extended_boot_sectors']['end'] = self._io.pos()
            self._debug['oem_parameters']['start'] = self._io.pos()
            self.oem_parameters = self._io.read_bytes(self._root.len_sector)
            self._debug['oem_parameters']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(self._root.len_sector)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['boot_checksum']['start'] = self._io.pos()
            self.boot_checksum = self._io.read_bytes(self._root.len_sector)
            self._debug['boot_checksum']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.boot_sector._fetch_instances()
            for i in range(len(self.extended_boot_sectors)):
                pass



    class BootSector(KaitaiStruct):

        class Active(IntEnum):
            first = 0
            second = 1

        class Dirty(IntEnum):
            consistent = 0
            inconsistent = 1

        class MediaFailure(IntEnum):
            no_failure = 0
            failure = 1
        SEQ_FIELDS = ["jump_boot", "file_system_name", "must_be_zero", "ofs_partition", "len_volume", "ofs_fat", "len_fat", "ofs_cluster_heap", "num_clusters", "first_cluster_of_root_directory", "volume_serial_number", "revision", "volume_flags", "bytes_per_sector_shift", "sectors_per_cluster_shift", "num_fat", "drive_select", "percent_in_use", "reserved", "boot_code", "boot_signature", "excess"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Exfat.BootSector, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['jump_boot']['start'] = self._io.pos()
            self.jump_boot = self._io.read_bytes(3)
            self._debug['jump_boot']['end'] = self._io.pos()
            if not self.jump_boot == b"\xEB\x76\x90":
                raise kaitaistruct.ValidationNotEqualError(b"\xEB\x76\x90", self.jump_boot, self._io, u"/types/boot_sector/seq/0")
            self._debug['file_system_name']['start'] = self._io.pos()
            self.file_system_name = self._io.read_bytes(8)
            self._debug['file_system_name']['end'] = self._io.pos()
            if not self.file_system_name == b"\x45\x58\x46\x41\x54\x20\x20\x20":
                raise kaitaistruct.ValidationNotEqualError(b"\x45\x58\x46\x41\x54\x20\x20\x20", self.file_system_name, self._io, u"/types/boot_sector/seq/1")
            self._debug['must_be_zero']['start'] = self._io.pos()
            self.must_be_zero = self._io.read_bytes(53)
            self._debug['must_be_zero']['end'] = self._io.pos()
            self._debug['ofs_partition']['start'] = self._io.pos()
            self.ofs_partition = self._io.read_u8le()
            self._debug['ofs_partition']['end'] = self._io.pos()
            self._debug['len_volume']['start'] = self._io.pos()
            self.len_volume = self._io.read_u8le()
            self._debug['len_volume']['end'] = self._io.pos()
            self._debug['ofs_fat']['start'] = self._io.pos()
            self.ofs_fat = self._io.read_u4le()
            self._debug['ofs_fat']['end'] = self._io.pos()
            if not self.ofs_fat >= 24:
                raise kaitaistruct.ValidationLessThanError(24, self.ofs_fat, self._io, u"/types/boot_sector/seq/5")
            self._debug['len_fat']['start'] = self._io.pos()
            self.len_fat = self._io.read_u4le()
            self._debug['len_fat']['end'] = self._io.pos()
            self._debug['ofs_cluster_heap']['start'] = self._io.pos()
            self.ofs_cluster_heap = self._io.read_u4le()
            self._debug['ofs_cluster_heap']['end'] = self._io.pos()
            self._debug['num_clusters']['start'] = self._io.pos()
            self.num_clusters = self._io.read_u4le()
            self._debug['num_clusters']['end'] = self._io.pos()
            self._debug['first_cluster_of_root_directory']['start'] = self._io.pos()
            self.first_cluster_of_root_directory = self._io.read_u4le()
            self._debug['first_cluster_of_root_directory']['end'] = self._io.pos()
            if not self.first_cluster_of_root_directory >= 2:
                raise kaitaistruct.ValidationLessThanError(2, self.first_cluster_of_root_directory, self._io, u"/types/boot_sector/seq/9")
            if not self.first_cluster_of_root_directory <= self.num_clusters + 1:
                raise kaitaistruct.ValidationGreaterThanError(self.num_clusters + 1, self.first_cluster_of_root_directory, self._io, u"/types/boot_sector/seq/9")
            self._debug['volume_serial_number']['start'] = self._io.pos()
            self.volume_serial_number = self._io.read_u4le()
            self._debug['volume_serial_number']['end'] = self._io.pos()
            self._debug['revision']['start'] = self._io.pos()
            self.revision = Exfat.BootSector.Revision(self._io, self, self._root)
            self._debug['revision']['end'] = self._io.pos()
            self._debug['volume_flags']['start'] = self._io.pos()
            self.volume_flags = self._io.read_u2le()
            self._debug['volume_flags']['end'] = self._io.pos()
            self._debug['bytes_per_sector_shift']['start'] = self._io.pos()
            self.bytes_per_sector_shift = self._io.read_u1()
            self._debug['bytes_per_sector_shift']['end'] = self._io.pos()
            if not self.bytes_per_sector_shift == self._root.bytes_per_sector_shift:
                raise kaitaistruct.ValidationNotEqualError(self._root.bytes_per_sector_shift, self.bytes_per_sector_shift, self._io, u"/types/boot_sector/seq/13")
            self._debug['sectors_per_cluster_shift']['start'] = self._io.pos()
            self.sectors_per_cluster_shift = self._io.read_u1()
            self._debug['sectors_per_cluster_shift']['end'] = self._io.pos()
            if not self.sectors_per_cluster_shift == self._root.sectors_per_cluster_shift:
                raise kaitaistruct.ValidationNotEqualError(self._root.sectors_per_cluster_shift, self.sectors_per_cluster_shift, self._io, u"/types/boot_sector/seq/14")
            self._debug['num_fat']['start'] = self._io.pos()
            self.num_fat = self._io.read_u1()
            self._debug['num_fat']['end'] = self._io.pos()
            if not  ((self.num_fat == 1) or (self.num_fat == 2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.num_fat, self._io, u"/types/boot_sector/seq/15")
            self._debug['drive_select']['start'] = self._io.pos()
            self.drive_select = self._io.read_u1()
            self._debug['drive_select']['end'] = self._io.pos()
            self._debug['percent_in_use']['start'] = self._io.pos()
            self.percent_in_use = self._io.read_u1()
            self._debug['percent_in_use']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(7)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['boot_code']['start'] = self._io.pos()
            self.boot_code = self._io.read_bytes(390)
            self._debug['boot_code']['end'] = self._io.pos()
            self._debug['boot_signature']['start'] = self._io.pos()
            self.boot_signature = self._io.read_bytes(2)
            self._debug['boot_signature']['end'] = self._io.pos()
            if not self.boot_signature == b"\x55\xAA":
                raise kaitaistruct.ValidationNotEqualError(b"\x55\xAA", self.boot_signature, self._io, u"/types/boot_sector/seq/20")
            self._debug['excess']['start'] = self._io.pos()
            self.excess = self._io.read_bytes_full()
            self._debug['excess']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.revision._fetch_instances()

        class Revision(KaitaiStruct):
            SEQ_FIELDS = ["minor", "major"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Exfat.BootSector.Revision, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['minor']['start'] = self._io.pos()
                self.minor = self._io.read_u1()
                self._debug['minor']['end'] = self._io.pos()
                if not self.minor >= 0:
                    raise kaitaistruct.ValidationLessThanError(0, self.minor, self._io, u"/types/boot_sector/types/revision/seq/0")
                if not self.minor <= 99:
                    raise kaitaistruct.ValidationGreaterThanError(99, self.minor, self._io, u"/types/boot_sector/types/revision/seq/0")
                self._debug['major']['start'] = self._io.pos()
                self.major = self._io.read_u1()
                self._debug['major']['end'] = self._io.pos()
                if not self.major >= 1:
                    raise kaitaistruct.ValidationLessThanError(1, self.major, self._io, u"/types/boot_sector/types/revision/seq/1")
                if not self.major <= 99:
                    raise kaitaistruct.ValidationGreaterThanError(99, self.major, self._io, u"/types/boot_sector/types/revision/seq/1")


            def _fetch_instances(self):
                pass


        @property
        def active_fat(self):
            if hasattr(self, '_m_active_fat'):
                return self._m_active_fat

            self._m_active_fat = KaitaiStream.resolve_enum(Exfat.BootSector.Active, self.volume_flags & 1)
            return getattr(self, '_m_active_fat', None)

        @property
        def clear_to_zero(self):
            if hasattr(self, '_m_clear_to_zero'):
                return self._m_clear_to_zero

            self._m_clear_to_zero = self.volume_flags & 8
            return getattr(self, '_m_clear_to_zero', None)

        @property
        def media_failure(self):
            if hasattr(self, '_m_media_failure'):
                return self._m_media_failure

            self._m_media_failure = KaitaiStream.resolve_enum(Exfat.BootSector.MediaFailure, self.volume_flags & 4)
            return getattr(self, '_m_media_failure', None)

        @property
        def volume_dirty(self):
            if hasattr(self, '_m_volume_dirty'):
                return self._m_volume_dirty

            self._m_volume_dirty = KaitaiStream.resolve_enum(Exfat.BootSector.Dirty, self.volume_flags & 2)
            return getattr(self, '_m_volume_dirty', None)


    class DataRegion(KaitaiStruct):
        SEQ_FIELDS = ["heap_alignment", "heap", "excess_space"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Exfat.DataRegion, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['heap_alignment']['start'] = self._io.pos()
            self.heap_alignment = self._io.read_bytes((self._root.main_boot_region.boot_sector.ofs_cluster_heap - (self._root.main_boot_region.boot_sector.ofs_fat + self._root.main_boot_region.boot_sector.len_fat * self._root.main_boot_region.boot_sector.num_fat)) * self._root.len_sector)
            self._debug['heap_alignment']['end'] = self._io.pos()
            self._debug['heap']['start'] = self._io.pos()
            self._raw_heap = self._io.read_bytes(self._root.main_boot_region.boot_sector.num_clusters * self._root.len_cluster)
            _io__raw_heap = KaitaiStream(BytesIO(self._raw_heap))
            self.heap = bytes_with_io.BytesWithIo(_io__raw_heap)
            self._debug['heap']['end'] = self._io.pos()
            self._debug['excess_space']['start'] = self._io.pos()
            self.excess_space = self._io.read_bytes_full()
            self._debug['excess_space']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.heap._fetch_instances()
            _ = self.clusters
            if hasattr(self, '_m_clusters'):
                pass
                self._m_clusters._fetch_instances()


        class Clusters(KaitaiStruct):
            SEQ_FIELDS = ["cluster"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Exfat.DataRegion.Clusters, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['cluster']['start'] = self._io.pos()
                self._debug['cluster']['arr'] = []
                self._raw_cluster = []
                self.cluster = []
                i = 0
                while not self._io.is_eof():
                    self._debug['cluster']['arr'].append({'start': self._io.pos()})
                    self._raw_cluster.append(self._io.read_bytes(self._root.len_cluster))
                    _io__raw_cluster = KaitaiStream(BytesIO(self._raw_cluster[-1]))
                    self.cluster.append(bytes_with_io.BytesWithIo(_io__raw_cluster))
                    self._debug['cluster']['arr'][len(self.cluster) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['cluster']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.cluster)):
                    pass
                    self.cluster[i]._fetch_instances()



        @property
        def clusters(self):
            if hasattr(self, '_m_clusters'):
                return self._m_clusters

            io = self.heap._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_clusters']['start'] = io.pos()
            self._m_clusters = Exfat.DataRegion.Clusters(io, self, self._root)
            self._debug['_m_clusters']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_clusters', None)


    class Directory(KaitaiStruct):
        SEQ_FIELDS = ["directory_sets"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Exfat.Directory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['directory_sets']['start'] = self._io.pos()
            self._debug['directory_sets']['arr'] = []
            self.directory_sets = []
            i = 0
            while True:
                self._debug['directory_sets']['arr'].append({'start': self._io.pos()})
                _ = Exfat.Directory.DirectorySet(self._io, self, self._root)
                self.directory_sets.append(_)
                self._debug['directory_sets']['arr'][len(self.directory_sets) - 1]['end'] = self._io.pos()
                if _.primary.end_of_directory:
                    break
                i += 1
            self._debug['directory_sets']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.directory_sets)):
                pass
                self.directory_sets[i]._fetch_instances()


        class DirectorySet(KaitaiStruct):
            SEQ_FIELDS = ["primary", "secondaries"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Exfat.Directory.DirectorySet, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['primary']['start'] = self._io.pos()
                self._raw_primary = self._io.read_bytes(32)
                _io__raw_primary = KaitaiStream(BytesIO(self._raw_primary))
                self.primary = Exfat.Directory.Entry(_io__raw_primary, self, self._root)
                self._debug['primary']['end'] = self._io.pos()
                self._debug['secondaries']['start'] = self._io.pos()
                self._debug['secondaries']['arr'] = []
                self._raw_secondaries = []
                self.secondaries = []
                for i in range(self.primary.secondary_count):
                    self._debug['secondaries']['arr'].append({'start': self._io.pos()})
                    self._raw_secondaries.append(self._io.read_bytes(32))
                    _io__raw_secondaries = KaitaiStream(BytesIO(self._raw_secondaries[i]))
                    self.secondaries.append(Exfat.Directory.Entry(_io__raw_secondaries, self, self._root))
                    self._debug['secondaries']['arr'][i]['end'] = self._io.pos()

                self._debug['secondaries']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.primary._fetch_instances()
                for i in range(len(self.secondaries)):
                    pass
                    self.secondaries[i]._fetch_instances()



        class Entry(KaitaiStruct):

            class TypeCategory(IntEnum):
                primary = 0
                secondary = 1

            class TypeImportance(IntEnum):
                critical = 0
                benign = 1
            SEQ_FIELDS = ["entry_type", "data"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Exfat.Directory.Entry, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['entry_type']['start'] = self._io.pos()
                self.entry_type = self._io.read_u1()
                self._debug['entry_type']['end'] = self._io.pos()
                self._debug['data']['start'] = self._io.pos()
                _on = self.category
                if _on == Exfat.Directory.Entry.TypeCategory.primary:
                    pass
                    self.data = Exfat.Directory.Entry.Primary(self.importance, self.type_code, self._io, self, self._root)
                elif _on == Exfat.Directory.Entry.TypeCategory.secondary:
                    pass
                    self.data = Exfat.Directory.Entry.Secondary(self.importance, self.type_code, self._io, self, self._root)
                self._debug['data']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _on = self.category
                if _on == Exfat.Directory.Entry.TypeCategory.primary:
                    pass
                    self.data._fetch_instances()
                elif _on == Exfat.Directory.Entry.TypeCategory.secondary:
                    pass
                    self.data._fetch_instances()

            class AllocationBitmap(KaitaiStruct):
                SEQ_FIELDS = ["bitmap_flags", "reserved", "first_cluster", "len_bitmap"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.AllocationBitmap, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['bitmap_flags']['start'] = self._io.pos()
                    self.bitmap_flags = self._io.read_u1()
                    self._debug['bitmap_flags']['end'] = self._io.pos()
                    self._debug['reserved']['start'] = self._io.pos()
                    self.reserved = self._io.read_bytes(18)
                    self._debug['reserved']['end'] = self._io.pos()
                    self._debug['first_cluster']['start'] = self._io.pos()
                    self.first_cluster = self._io.read_u4le()
                    self._debug['first_cluster']['end'] = self._io.pos()
                    self._debug['len_bitmap']['start'] = self._io.pos()
                    self.len_bitmap = self._io.read_u8le()
                    self._debug['len_bitmap']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    _ = self.bitmap
                    if hasattr(self, '_m_bitmap'):
                        pass


                @property
                def bitmap(self):
                    if hasattr(self, '_m_bitmap'):
                        return self._m_bitmap

                    io = self._root.data_region.heap._io
                    _pos = io.pos()
                    io.seek((self.first_cluster - 2) * self._root.len_cluster)
                    self._debug['_m_bitmap']['start'] = io.pos()
                    self._m_bitmap = io.read_bytes(self.len_bitmap)
                    self._debug['_m_bitmap']['end'] = io.pos()
                    io.seek(_pos)
                    return getattr(self, '_m_bitmap', None)

                @property
                def secondary_count(self):
                    if hasattr(self, '_m_secondary_count'):
                        return self._m_secondary_count

                    self._m_secondary_count = 0
                    return getattr(self, '_m_secondary_count', None)


            class FileDirectory(KaitaiStruct):
                SEQ_FIELDS = ["secondary_count", "set_checksum", "attributes", "reserved_1", "ctime", "mtime", "atime", "ctime_ms_increment", "mtime_ms_increment", "ctime_utc_offset", "mtime_utc_offset", "atime_utc_offset", "reserved_2"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.FileDirectory, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['secondary_count']['start'] = self._io.pos()
                    self.secondary_count = self._io.read_u1()
                    self._debug['secondary_count']['end'] = self._io.pos()
                    if not self.secondary_count >= 2:
                        raise kaitaistruct.ValidationLessThanError(2, self.secondary_count, self._io, u"/types/directory/types/entry/types/file_directory/seq/0")
                    self._debug['set_checksum']['start'] = self._io.pos()
                    self.set_checksum = self._io.read_u2le()
                    self._debug['set_checksum']['end'] = self._io.pos()
                    self._debug['attributes']['start'] = self._io.pos()
                    self.attributes = self._io.read_u2le()
                    self._debug['attributes']['end'] = self._io.pos()
                    self._debug['reserved_1']['start'] = self._io.pos()
                    self.reserved_1 = self._io.read_bytes(2)
                    self._debug['reserved_1']['end'] = self._io.pos()
                    self._debug['ctime']['start'] = self._io.pos()
                    self._raw_ctime = self._io.read_bytes(4)
                    _io__raw_ctime = KaitaiStream(BytesIO(self._raw_ctime))
                    self.ctime = Exfat.Timestamp(_io__raw_ctime, self, self._root)
                    self._debug['ctime']['end'] = self._io.pos()
                    self._debug['mtime']['start'] = self._io.pos()
                    self._raw_mtime = self._io.read_bytes(4)
                    _io__raw_mtime = KaitaiStream(BytesIO(self._raw_mtime))
                    self.mtime = Exfat.Timestamp(_io__raw_mtime, self, self._root)
                    self._debug['mtime']['end'] = self._io.pos()
                    self._debug['atime']['start'] = self._io.pos()
                    self._raw_atime = self._io.read_bytes(4)
                    _io__raw_atime = KaitaiStream(BytesIO(self._raw_atime))
                    self.atime = Exfat.Timestamp(_io__raw_atime, self, self._root)
                    self._debug['atime']['end'] = self._io.pos()
                    self._debug['ctime_ms_increment']['start'] = self._io.pos()
                    self.ctime_ms_increment = self._io.read_u1()
                    self._debug['ctime_ms_increment']['end'] = self._io.pos()
                    self._debug['mtime_ms_increment']['start'] = self._io.pos()
                    self.mtime_ms_increment = self._io.read_u1()
                    self._debug['mtime_ms_increment']['end'] = self._io.pos()
                    self._debug['ctime_utc_offset']['start'] = self._io.pos()
                    self.ctime_utc_offset = self._io.read_u1()
                    self._debug['ctime_utc_offset']['end'] = self._io.pos()
                    self._debug['mtime_utc_offset']['start'] = self._io.pos()
                    self.mtime_utc_offset = self._io.read_u1()
                    self._debug['mtime_utc_offset']['end'] = self._io.pos()
                    self._debug['atime_utc_offset']['start'] = self._io.pos()
                    self.atime_utc_offset = self._io.read_u1()
                    self._debug['atime_utc_offset']['end'] = self._io.pos()
                    self._debug['reserved_2']['start'] = self._io.pos()
                    self.reserved_2 = self._io.read_bytes(7)
                    self._debug['reserved_2']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    self.ctime._fetch_instances()
                    self.mtime._fetch_instances()
                    self.atime._fetch_instances()

                @property
                def archive(self):
                    if hasattr(self, '_m_archive'):
                        return self._m_archive

                    self._m_archive = self.attributes & 32 != 0
                    return getattr(self, '_m_archive', None)

                @property
                def directory(self):
                    if hasattr(self, '_m_directory'):
                        return self._m_directory

                    self._m_directory = self.attributes & 16 != 0
                    return getattr(self, '_m_directory', None)

                @property
                def hidden(self):
                    if hasattr(self, '_m_hidden'):
                        return self._m_hidden

                    self._m_hidden = self.attributes & 2 != 0
                    return getattr(self, '_m_hidden', None)

                @property
                def read_only(self):
                    if hasattr(self, '_m_read_only'):
                        return self._m_read_only

                    self._m_read_only = self.attributes & 1 != 0
                    return getattr(self, '_m_read_only', None)

                @property
                def reserved(self):
                    if hasattr(self, '_m_reserved'):
                        return self._m_reserved

                    self._m_reserved = self.attributes & 8 != 0
                    return getattr(self, '_m_reserved', None)

                @property
                def system(self):
                    if hasattr(self, '_m_system'):
                        return self._m_system

                    self._m_system = self.attributes & 4 != 0
                    return getattr(self, '_m_system', None)


            class FileNameDirectory(KaitaiStruct):
                SEQ_FIELDS = ["general_secondary_flags", "name"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.FileNameDirectory, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['general_secondary_flags']['start'] = self._io.pos()
                    self.general_secondary_flags = self._io.read_u1()
                    self._debug['general_secondary_flags']['end'] = self._io.pos()
                    self._debug['name']['start'] = self._io.pos()
                    self.name = self._io.read_bytes_full()
                    self._debug['name']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def allocation_possible(self):
                    if hasattr(self, '_m_allocation_possible'):
                        return self._m_allocation_possible

                    self._m_allocation_possible = self.general_secondary_flags & 1 != 0
                    return getattr(self, '_m_allocation_possible', None)

                @property
                def no_fat_chain(self):
                    if hasattr(self, '_m_no_fat_chain'):
                        return self._m_no_fat_chain

                    self._m_no_fat_chain = self.general_secondary_flags & 2 != 0
                    return getattr(self, '_m_no_fat_chain', None)


            class GenericPrimaryTemplate(KaitaiStruct):
                SEQ_FIELDS = ["secondary_count", "set_checksum", "general_primary_flags", "custom", "first_cluster", "len_data"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.GenericPrimaryTemplate, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['secondary_count']['start'] = self._io.pos()
                    self.secondary_count = self._io.read_u1()
                    self._debug['secondary_count']['end'] = self._io.pos()
                    self._debug['set_checksum']['start'] = self._io.pos()
                    self.set_checksum = self._io.read_u2le()
                    self._debug['set_checksum']['end'] = self._io.pos()
                    self._debug['general_primary_flags']['start'] = self._io.pos()
                    self.general_primary_flags = self._io.read_u2le()
                    self._debug['general_primary_flags']['end'] = self._io.pos()
                    self._debug['custom']['start'] = self._io.pos()
                    self.custom = self._io.read_bytes(14)
                    self._debug['custom']['end'] = self._io.pos()
                    self._debug['first_cluster']['start'] = self._io.pos()
                    self.first_cluster = self._io.read_u4le()
                    self._debug['first_cluster']['end'] = self._io.pos()
                    self._debug['len_data']['start'] = self._io.pos()
                    self.len_data = self._io.read_u8le()
                    self._debug['len_data']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def allocation_possible(self):
                    if hasattr(self, '_m_allocation_possible'):
                        return self._m_allocation_possible

                    self._m_allocation_possible = self.general_primary_flags & 1 != 0
                    return getattr(self, '_m_allocation_possible', None)

                @property
                def no_fat_chain(self):
                    if hasattr(self, '_m_no_fat_chain'):
                        return self._m_no_fat_chain

                    self._m_no_fat_chain = self.general_primary_flags & 2 != 0
                    return getattr(self, '_m_no_fat_chain', None)


            class GenericSecondaryTemplate(KaitaiStruct):
                SEQ_FIELDS = ["general_secondary_flags", "custom", "first_cluster", "len_data"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.GenericSecondaryTemplate, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['general_secondary_flags']['start'] = self._io.pos()
                    self.general_secondary_flags = self._io.read_u1()
                    self._debug['general_secondary_flags']['end'] = self._io.pos()
                    self._debug['custom']['start'] = self._io.pos()
                    self.custom = self._io.read_bytes(18)
                    self._debug['custom']['end'] = self._io.pos()
                    self._debug['first_cluster']['start'] = self._io.pos()
                    self.first_cluster = self._io.read_u4le()
                    self._debug['first_cluster']['end'] = self._io.pos()
                    self._debug['len_data']['start'] = self._io.pos()
                    self.len_data = self._io.read_u8le()
                    self._debug['len_data']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def allocation_possible(self):
                    if hasattr(self, '_m_allocation_possible'):
                        return self._m_allocation_possible

                    self._m_allocation_possible = self.general_secondary_flags & 1 != 0
                    return getattr(self, '_m_allocation_possible', None)

                @property
                def no_fat_chain(self):
                    if hasattr(self, '_m_no_fat_chain'):
                        return self._m_no_fat_chain

                    self._m_no_fat_chain = self.general_secondary_flags & 2 != 0
                    return getattr(self, '_m_no_fat_chain', None)


            class GenericTemplate(KaitaiStruct):
                SEQ_FIELDS = ["custom", "first_cluster", "len_data"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.GenericTemplate, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['custom']['start'] = self._io.pos()
                    self.custom = self._io.read_bytes(19)
                    self._debug['custom']['end'] = self._io.pos()
                    self._debug['first_cluster']['start'] = self._io.pos()
                    self.first_cluster = self._io.read_u4le()
                    self._debug['first_cluster']['end'] = self._io.pos()
                    self._debug['len_data']['start'] = self._io.pos()
                    self.len_data = self._io.read_u8le()
                    self._debug['len_data']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass


            class Primary(KaitaiStruct):
                SEQ_FIELDS = ["data"]
                def __init__(self, importance, code, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.Primary, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self.importance = importance
                    self.code = code
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['data']['start'] = self._io.pos()
                    _on = self.importance
                    if _on == Exfat.Directory.Entry.TypeImportance.benign:
                        pass
                        self.data = Exfat.Directory.Entry.Primary.Benign(self.code, self._io, self, self._root)
                    elif _on == Exfat.Directory.Entry.TypeImportance.critical:
                        pass
                        self.data = Exfat.Directory.Entry.Primary.Critical(self.code, self._io, self, self._root)
                    self._debug['data']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    _on = self.importance
                    if _on == Exfat.Directory.Entry.TypeImportance.benign:
                        pass
                        self.data._fetch_instances()
                    elif _on == Exfat.Directory.Entry.TypeImportance.critical:
                        pass
                        self.data._fetch_instances()

                class Benign(KaitaiStruct):

                    class Code(IntEnum):
                        volume_guid = 0
                        texfat_padding = 1
                    SEQ_FIELDS = ["data"]
                    def __init__(self, code, _io, _parent=None, _root=None):
                        super(Exfat.Directory.Entry.Primary.Benign, self).__init__(_io)
                        self._parent = _parent
                        self._root = _root
                        self.code = code
                        self._debug = collections.defaultdict(dict)
                        self._read()

                    def _read(self):
                        self._debug['data']['start'] = self._io.pos()
                        _on = self.type_code
                        if _on == Exfat.Directory.Entry.Primary.Benign.Code.volume_guid:
                            pass
                            self.data = Exfat.Directory.Entry.VolumeGuid(self._io, self, self._root)
                        else:
                            pass
                            self.data = Exfat.Directory.Entry.GenericPrimaryTemplate(self._io, self, self._root)
                        self._debug['data']['end'] = self._io.pos()


                    def _fetch_instances(self):
                        pass
                        _on = self.type_code
                        if _on == Exfat.Directory.Entry.Primary.Benign.Code.volume_guid:
                            pass
                            self.data._fetch_instances()
                        else:
                            pass
                            self.data._fetch_instances()

                    @property
                    def type_code(self):
                        if hasattr(self, '_m_type_code'):
                            return self._m_type_code

                        self._m_type_code = KaitaiStream.resolve_enum(Exfat.Directory.Entry.Primary.Benign.Code, self.code)
                        return getattr(self, '_m_type_code', None)


                class Critical(KaitaiStruct):

                    class Code(IntEnum):
                        allocation_bitmap = 1
                        up_case_table = 2
                        volume_label = 3
                        file_directory = 5
                    SEQ_FIELDS = ["data"]
                    def __init__(self, code, _io, _parent=None, _root=None):
                        super(Exfat.Directory.Entry.Primary.Critical, self).__init__(_io)
                        self._parent = _parent
                        self._root = _root
                        self.code = code
                        self._debug = collections.defaultdict(dict)
                        self._read()

                    def _read(self):
                        self._debug['data']['start'] = self._io.pos()
                        _on = self.type_code
                        if _on == Exfat.Directory.Entry.Primary.Critical.Code.allocation_bitmap:
                            pass
                            self.data = Exfat.Directory.Entry.AllocationBitmap(self._io, self, self._root)
                        elif _on == Exfat.Directory.Entry.Primary.Critical.Code.file_directory:
                            pass
                            self.data = Exfat.Directory.Entry.FileDirectory(self._io, self, self._root)
                        elif _on == Exfat.Directory.Entry.Primary.Critical.Code.up_case_table:
                            pass
                            self.data = Exfat.Directory.Entry.UpCaseTable(self._io, self, self._root)
                        elif _on == Exfat.Directory.Entry.Primary.Critical.Code.volume_label:
                            pass
                            self.data = Exfat.Directory.Entry.VolumeLabel(self._io, self, self._root)
                        else:
                            pass
                            self.data = Exfat.Directory.Entry.GenericPrimaryTemplate(self._io, self, self._root)
                        self._debug['data']['end'] = self._io.pos()


                    def _fetch_instances(self):
                        pass
                        _on = self.type_code
                        if _on == Exfat.Directory.Entry.Primary.Critical.Code.allocation_bitmap:
                            pass
                            self.data._fetch_instances()
                        elif _on == Exfat.Directory.Entry.Primary.Critical.Code.file_directory:
                            pass
                            self.data._fetch_instances()
                        elif _on == Exfat.Directory.Entry.Primary.Critical.Code.up_case_table:
                            pass
                            self.data._fetch_instances()
                        elif _on == Exfat.Directory.Entry.Primary.Critical.Code.volume_label:
                            pass
                            self.data._fetch_instances()
                        else:
                            pass
                            self.data._fetch_instances()

                    @property
                    def secondary_count(self):
                        if hasattr(self, '_m_secondary_count'):
                            return self._m_secondary_count

                        self._m_secondary_count = self.data.secondary_count
                        return getattr(self, '_m_secondary_count', None)

                    @property
                    def type_code(self):
                        if hasattr(self, '_m_type_code'):
                            return self._m_type_code

                        self._m_type_code = KaitaiStream.resolve_enum(Exfat.Directory.Entry.Primary.Critical.Code, self.code)
                        return getattr(self, '_m_type_code', None)


                @property
                def secondary_count(self):
                    if hasattr(self, '_m_secondary_count'):
                        return self._m_secondary_count

                    self._m_secondary_count = self.data.secondary_count
                    return getattr(self, '_m_secondary_count', None)


            class Secondary(KaitaiStruct):
                SEQ_FIELDS = ["data"]
                def __init__(self, importance, code, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.Secondary, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self.importance = importance
                    self.code = code
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['data']['start'] = self._io.pos()
                    _on = self.importance
                    if _on == Exfat.Directory.Entry.TypeImportance.benign:
                        pass
                        self.data = Exfat.Directory.Entry.Secondary.Benign(self.code, self._io, self, self._root)
                    elif _on == Exfat.Directory.Entry.TypeImportance.critical:
                        pass
                        self.data = Exfat.Directory.Entry.Secondary.Critical(self.code, self._io, self, self._root)
                    self._debug['data']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    _on = self.importance
                    if _on == Exfat.Directory.Entry.TypeImportance.benign:
                        pass
                        self.data._fetch_instances()
                    elif _on == Exfat.Directory.Entry.TypeImportance.critical:
                        pass
                        self.data._fetch_instances()

                class Benign(KaitaiStruct):

                    class Code(IntEnum):
                        vendor_extension = 0
                        vendor_allocation = 1
                    SEQ_FIELDS = ["data"]
                    def __init__(self, code, _io, _parent=None, _root=None):
                        super(Exfat.Directory.Entry.Secondary.Benign, self).__init__(_io)
                        self._parent = _parent
                        self._root = _root
                        self.code = code
                        self._debug = collections.defaultdict(dict)
                        self._read()

                    def _read(self):
                        self._debug['data']['start'] = self._io.pos()
                        _on = self.type_code
                        if _on == Exfat.Directory.Entry.Secondary.Benign.Code.vendor_allocation:
                            pass
                            self.data = Exfat.Directory.Entry.VendorAllocation(self._io, self, self._root)
                        elif _on == Exfat.Directory.Entry.Secondary.Benign.Code.vendor_extension:
                            pass
                            self.data = Exfat.Directory.Entry.VendorExtension(self._io, self, self._root)
                        else:
                            pass
                            self.data = Exfat.Directory.Entry.GenericSecondaryTemplate(self._io, self, self._root)
                        self._debug['data']['end'] = self._io.pos()


                    def _fetch_instances(self):
                        pass
                        _on = self.type_code
                        if _on == Exfat.Directory.Entry.Secondary.Benign.Code.vendor_allocation:
                            pass
                            self.data._fetch_instances()
                        elif _on == Exfat.Directory.Entry.Secondary.Benign.Code.vendor_extension:
                            pass
                            self.data._fetch_instances()
                        else:
                            pass
                            self.data._fetch_instances()

                    @property
                    def type_code(self):
                        if hasattr(self, '_m_type_code'):
                            return self._m_type_code

                        self._m_type_code = KaitaiStream.resolve_enum(Exfat.Directory.Entry.Secondary.Benign.Code, self.code)
                        return getattr(self, '_m_type_code', None)


                class Critical(KaitaiStruct):

                    class Code(IntEnum):
                        stream_extension = 0
                        file_name_directory = 1
                    SEQ_FIELDS = ["data"]
                    def __init__(self, code, _io, _parent=None, _root=None):
                        super(Exfat.Directory.Entry.Secondary.Critical, self).__init__(_io)
                        self._parent = _parent
                        self._root = _root
                        self.code = code
                        self._debug = collections.defaultdict(dict)
                        self._read()

                    def _read(self):
                        self._debug['data']['start'] = self._io.pos()
                        _on = self.type_code
                        if _on == Exfat.Directory.Entry.Secondary.Critical.Code.file_name_directory:
                            pass
                            self.data = Exfat.Directory.Entry.FileNameDirectory(self._io, self, self._root)
                        elif _on == Exfat.Directory.Entry.Secondary.Critical.Code.stream_extension:
                            pass
                            self.data = Exfat.Directory.Entry.StreamExtension(self._io, self, self._root)
                        else:
                            pass
                            self.data = Exfat.Directory.Entry.GenericSecondaryTemplate(self._io, self, self._root)
                        self._debug['data']['end'] = self._io.pos()


                    def _fetch_instances(self):
                        pass
                        _on = self.type_code
                        if _on == Exfat.Directory.Entry.Secondary.Critical.Code.file_name_directory:
                            pass
                            self.data._fetch_instances()
                        elif _on == Exfat.Directory.Entry.Secondary.Critical.Code.stream_extension:
                            pass
                            self.data._fetch_instances()
                        else:
                            pass
                            self.data._fetch_instances()

                    @property
                    def type_code(self):
                        if hasattr(self, '_m_type_code'):
                            return self._m_type_code

                        self._m_type_code = KaitaiStream.resolve_enum(Exfat.Directory.Entry.Secondary.Critical.Code, self.code)
                        return getattr(self, '_m_type_code', None)



            class StreamExtension(KaitaiStruct):
                SEQ_FIELDS = ["general_secondary_flags", "reserved_1", "len_name", "name_hash", "reserved_2", "valid_data_length", "reserved_3", "first_cluster", "len_data"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.StreamExtension, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['general_secondary_flags']['start'] = self._io.pos()
                    self.general_secondary_flags = self._io.read_u1()
                    self._debug['general_secondary_flags']['end'] = self._io.pos()
                    self._debug['reserved_1']['start'] = self._io.pos()
                    self.reserved_1 = self._io.read_bytes(1)
                    self._debug['reserved_1']['end'] = self._io.pos()
                    self._debug['len_name']['start'] = self._io.pos()
                    self.len_name = self._io.read_u1()
                    self._debug['len_name']['end'] = self._io.pos()
                    self._debug['name_hash']['start'] = self._io.pos()
                    self.name_hash = self._io.read_u2le()
                    self._debug['name_hash']['end'] = self._io.pos()
                    self._debug['reserved_2']['start'] = self._io.pos()
                    self.reserved_2 = self._io.read_bytes(2)
                    self._debug['reserved_2']['end'] = self._io.pos()
                    self._debug['valid_data_length']['start'] = self._io.pos()
                    self.valid_data_length = self._io.read_u8le()
                    self._debug['valid_data_length']['end'] = self._io.pos()
                    self._debug['reserved_3']['start'] = self._io.pos()
                    self.reserved_3 = self._io.read_bytes(4)
                    self._debug['reserved_3']['end'] = self._io.pos()
                    self._debug['first_cluster']['start'] = self._io.pos()
                    self.first_cluster = self._io.read_u4le()
                    self._debug['first_cluster']['end'] = self._io.pos()
                    self._debug['len_data']['start'] = self._io.pos()
                    self.len_data = self._io.read_u8le()
                    self._debug['len_data']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    _ = self.data
                    if hasattr(self, '_m_data'):
                        pass

                    _ = self.subdirectory
                    if hasattr(self, '_m_subdirectory'):
                        pass
                        self._m_subdirectory._fetch_instances()


                @property
                def allocation_possible(self):
                    if hasattr(self, '_m_allocation_possible'):
                        return self._m_allocation_possible

                    self._m_allocation_possible = self.general_secondary_flags & 1 != 0
                    return getattr(self, '_m_allocation_possible', None)

                @property
                def archive(self):
                    if hasattr(self, '_m_archive'):
                        return self._m_archive

                    self._m_archive = self._parent._parent._parent._parent.primary.data.data.data.archive
                    return getattr(self, '_m_archive', None)

                @property
                def data(self):
                    if hasattr(self, '_m_data'):
                        return self._m_data

                    if  (((not (self.directory))) and (self.no_fat_chain)) :
                        pass
                        io = self._root.data_region.heap._io
                        _pos = io.pos()
                        io.seek((self.first_cluster - 2) * self._root.len_cluster)
                        self._debug['_m_data']['start'] = io.pos()
                        self._m_data = io.read_bytes(self.len_data)
                        self._debug['_m_data']['end'] = io.pos()
                        io.seek(_pos)

                    return getattr(self, '_m_data', None)

                @property
                def directory(self):
                    if hasattr(self, '_m_directory'):
                        return self._m_directory

                    self._m_directory = self._parent._parent._parent._parent.primary.data.data.data.directory
                    return getattr(self, '_m_directory', None)

                @property
                def no_fat_chain(self):
                    if hasattr(self, '_m_no_fat_chain'):
                        return self._m_no_fat_chain

                    self._m_no_fat_chain = self.general_secondary_flags & 2 != 0
                    return getattr(self, '_m_no_fat_chain', None)

                @property
                def subdirectory(self):
                    if hasattr(self, '_m_subdirectory'):
                        return self._m_subdirectory

                    if self.directory:
                        pass
                        io = self._root.data_region.heap._io
                        _pos = io.pos()
                        io.seek((self.first_cluster - 2) * self._root.len_cluster)
                        self._debug['_m_subdirectory']['start'] = io.pos()
                        self._raw__m_subdirectory = io.read_bytes(self.len_data)
                        _io__raw__m_subdirectory = KaitaiStream(BytesIO(self._raw__m_subdirectory))
                        self._m_subdirectory = Exfat.Directory(_io__raw__m_subdirectory, self, self._root)
                        self._debug['_m_subdirectory']['end'] = io.pos()
                        io.seek(_pos)

                    return getattr(self, '_m_subdirectory', None)


            class UpCaseTable(KaitaiStruct):
                SEQ_FIELDS = ["reserved_1", "table_checksum", "reserved_2", "first_cluster", "len_table"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.UpCaseTable, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['reserved_1']['start'] = self._io.pos()
                    self.reserved_1 = self._io.read_bytes(3)
                    self._debug['reserved_1']['end'] = self._io.pos()
                    self._debug['table_checksum']['start'] = self._io.pos()
                    self.table_checksum = self._io.read_u4le()
                    self._debug['table_checksum']['end'] = self._io.pos()
                    self._debug['reserved_2']['start'] = self._io.pos()
                    self.reserved_2 = self._io.read_bytes(12)
                    self._debug['reserved_2']['end'] = self._io.pos()
                    self._debug['first_cluster']['start'] = self._io.pos()
                    self.first_cluster = self._io.read_u4le()
                    self._debug['first_cluster']['end'] = self._io.pos()
                    self._debug['len_table']['start'] = self._io.pos()
                    self.len_table = self._io.read_u8le()
                    self._debug['len_table']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    _ = self.table
                    if hasattr(self, '_m_table'):
                        pass


                @property
                def secondary_count(self):
                    if hasattr(self, '_m_secondary_count'):
                        return self._m_secondary_count

                    self._m_secondary_count = 0
                    return getattr(self, '_m_secondary_count', None)

                @property
                def table(self):
                    if hasattr(self, '_m_table'):
                        return self._m_table

                    io = self._root.data_region.heap._io
                    _pos = io.pos()
                    io.seek((self.first_cluster - 2) * self._root.len_cluster)
                    self._debug['_m_table']['start'] = io.pos()
                    self._m_table = io.read_bytes(self.len_table)
                    self._debug['_m_table']['end'] = io.pos()
                    io.seek(_pos)
                    return getattr(self, '_m_table', None)


            class VendorAllocation(KaitaiStruct):
                SEQ_FIELDS = ["general_secondary_flags", "vendor_guid", "vendor_defined", "first_cluster", "len_data"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.VendorAllocation, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['general_secondary_flags']['start'] = self._io.pos()
                    self.general_secondary_flags = self._io.read_u1()
                    self._debug['general_secondary_flags']['end'] = self._io.pos()
                    self._debug['vendor_guid']['start'] = self._io.pos()
                    self.vendor_guid = self._io.read_bytes(16)
                    self._debug['vendor_guid']['end'] = self._io.pos()
                    self._debug['vendor_defined']['start'] = self._io.pos()
                    self.vendor_defined = self._io.read_u2le()
                    self._debug['vendor_defined']['end'] = self._io.pos()
                    self._debug['first_cluster']['start'] = self._io.pos()
                    self.first_cluster = self._io.read_u4le()
                    self._debug['first_cluster']['end'] = self._io.pos()
                    self._debug['len_data']['start'] = self._io.pos()
                    self.len_data = self._io.read_u8le()
                    self._debug['len_data']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def allocation_possible(self):
                    if hasattr(self, '_m_allocation_possible'):
                        return self._m_allocation_possible

                    self._m_allocation_possible = self.general_secondary_flags & 1 != 0
                    return getattr(self, '_m_allocation_possible', None)

                @property
                def no_fat_chain(self):
                    if hasattr(self, '_m_no_fat_chain'):
                        return self._m_no_fat_chain

                    self._m_no_fat_chain = self.general_secondary_flags & 2 != 0
                    return getattr(self, '_m_no_fat_chain', None)


            class VendorExtension(KaitaiStruct):
                SEQ_FIELDS = ["general_secondary_flags", "vendor_guid", "vendor_defined"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.VendorExtension, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['general_secondary_flags']['start'] = self._io.pos()
                    self.general_secondary_flags = self._io.read_u1()
                    self._debug['general_secondary_flags']['end'] = self._io.pos()
                    self._debug['vendor_guid']['start'] = self._io.pos()
                    self.vendor_guid = self._io.read_bytes(16)
                    self._debug['vendor_guid']['end'] = self._io.pos()
                    self._debug['vendor_defined']['start'] = self._io.pos()
                    self.vendor_defined = self._io.read_bytes(14)
                    self._debug['vendor_defined']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def allocation_possible(self):
                    if hasattr(self, '_m_allocation_possible'):
                        return self._m_allocation_possible

                    self._m_allocation_possible = self.general_secondary_flags & 1 != 0
                    return getattr(self, '_m_allocation_possible', None)

                @property
                def no_fat_chain(self):
                    if hasattr(self, '_m_no_fat_chain'):
                        return self._m_no_fat_chain

                    self._m_no_fat_chain = self.general_secondary_flags & 2 != 0
                    return getattr(self, '_m_no_fat_chain', None)


            class VolumeGuid(KaitaiStruct):
                SEQ_FIELDS = ["secondary_count", "set_checksum", "general_primary_flags", "volume_guid", "reserved"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.VolumeGuid, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['secondary_count']['start'] = self._io.pos()
                    self.secondary_count = self._io.read_u1()
                    self._debug['secondary_count']['end'] = self._io.pos()
                    self._debug['set_checksum']['start'] = self._io.pos()
                    self.set_checksum = self._io.read_u2le()
                    self._debug['set_checksum']['end'] = self._io.pos()
                    self._debug['general_primary_flags']['start'] = self._io.pos()
                    self.general_primary_flags = self._io.read_u2le()
                    self._debug['general_primary_flags']['end'] = self._io.pos()
                    self._debug['volume_guid']['start'] = self._io.pos()
                    self.volume_guid = self._io.read_bytes(16)
                    self._debug['volume_guid']['end'] = self._io.pos()
                    self._debug['reserved']['start'] = self._io.pos()
                    self.reserved = self._io.read_bytes(10)
                    self._debug['reserved']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def allocation_possible(self):
                    if hasattr(self, '_m_allocation_possible'):
                        return self._m_allocation_possible

                    self._m_allocation_possible = self.general_primary_flags & 1 != 0
                    return getattr(self, '_m_allocation_possible', None)

                @property
                def no_fat_chain(self):
                    if hasattr(self, '_m_no_fat_chain'):
                        return self._m_no_fat_chain

                    self._m_no_fat_chain = self.general_primary_flags & 2 != 0
                    return getattr(self, '_m_no_fat_chain', None)


            class VolumeLabel(KaitaiStruct):
                SEQ_FIELDS = ["num_characters", "label", "reserved"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Exfat.Directory.Entry.VolumeLabel, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['num_characters']['start'] = self._io.pos()
                    self.num_characters = self._io.read_u1()
                    self._debug['num_characters']['end'] = self._io.pos()
                    self._debug['label']['start'] = self._io.pos()
                    self.label = self._io.read_bytes(22)
                    self._debug['label']['end'] = self._io.pos()
                    self._debug['reserved']['start'] = self._io.pos()
                    self.reserved = self._io.read_bytes(8)
                    self._debug['reserved']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def secondary_count(self):
                    if hasattr(self, '_m_secondary_count'):
                        return self._m_secondary_count

                    self._m_secondary_count = 0
                    return getattr(self, '_m_secondary_count', None)


            @property
            def category(self):
                if hasattr(self, '_m_category'):
                    return self._m_category

                self._m_category = KaitaiStream.resolve_enum(Exfat.Directory.Entry.TypeCategory, int(self.entry_type & 64 != 0))
                return getattr(self, '_m_category', None)

            @property
            def end_of_directory(self):
                if hasattr(self, '_m_end_of_directory'):
                    return self._m_end_of_directory

                self._m_end_of_directory = self.entry_type == 0
                return getattr(self, '_m_end_of_directory', None)

            @property
            def importance(self):
                if hasattr(self, '_m_importance'):
                    return self._m_importance

                self._m_importance = KaitaiStream.resolve_enum(Exfat.Directory.Entry.TypeImportance, int(self.entry_type & 32 != 0))
                return getattr(self, '_m_importance', None)

            @property
            def in_use(self):
                if hasattr(self, '_m_in_use'):
                    return self._m_in_use

                self._m_in_use = self.entry_type & 128 != 0
                return getattr(self, '_m_in_use', None)

            @property
            def secondary_count(self):
                if hasattr(self, '_m_secondary_count'):
                    return self._m_secondary_count

                self._m_secondary_count = (0 if self.category == Exfat.Directory.Entry.TypeCategory.secondary else self.data.secondary_count)
                return getattr(self, '_m_secondary_count', None)

            @property
            def type_code(self):
                if hasattr(self, '_m_type_code'):
                    return self._m_type_code

                self._m_type_code = self.entry_type & 31
                return getattr(self, '_m_type_code', None)



    class Fat(KaitaiStruct):
        SEQ_FIELDS = ["entry_0", "entry_1", "entries", "excess_space"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Exfat.Fat, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entry_0']['start'] = self._io.pos()
            self.entry_0 = self._io.read_bytes(4)
            self._debug['entry_0']['end'] = self._io.pos()
            if not self.entry_0 == b"\xF8\xFF\xFF\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xF8\xFF\xFF\xFF", self.entry_0, self._io, u"/types/fat/seq/0")
            self._debug['entry_1']['start'] = self._io.pos()
            self.entry_1 = self._io.read_bytes(4)
            self._debug['entry_1']['end'] = self._io.pos()
            if not self.entry_1 == b"\xFF\xFF\xFF\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF\xFF\xFF\xFF", self.entry_1, self._io, u"/types/fat/seq/1")
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self._root.main_boot_region.boot_sector.num_clusters):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(self._io.read_bytes(4))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()
            self._debug['excess_space']['start'] = self._io.pos()
            self.excess_space = self._io.read_bytes_full()
            self._debug['excess_space']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass



    class FatRegion(KaitaiStruct):
        SEQ_FIELDS = ["alignment", "first_fat", "second_fat"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Exfat.FatRegion, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['alignment']['start'] = self._io.pos()
            self.alignment = self._io.read_bytes((self._root.main_boot_region.boot_sector.ofs_fat - 24) * self._root.len_sector)
            self._debug['alignment']['end'] = self._io.pos()
            self._debug['first_fat']['start'] = self._io.pos()
            self._raw_first_fat = self._io.read_bytes(self._root.main_boot_region.boot_sector.len_fat * self._root.len_sector)
            _io__raw_first_fat = KaitaiStream(BytesIO(self._raw_first_fat))
            self.first_fat = Exfat.Fat(_io__raw_first_fat, self, self._root)
            self._debug['first_fat']['end'] = self._io.pos()
            if self._root.main_boot_region.boot_sector.num_fat > 1:
                pass
                self._debug['second_fat']['start'] = self._io.pos()
                self._raw_second_fat = self._io.read_bytes((self._root.main_boot_region.boot_sector.len_fat * (self._root.main_boot_region.boot_sector.num_fat - 1)) * self._root.len_sector)
                _io__raw_second_fat = KaitaiStream(BytesIO(self._raw_second_fat))
                self.second_fat = Exfat.Fat(_io__raw_second_fat, self, self._root)
                self._debug['second_fat']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.first_fat._fetch_instances()
            if self._root.main_boot_region.boot_sector.num_fat > 1:
                pass
                self.second_fat._fetch_instances()



    class Timestamp(KaitaiStruct):
        SEQ_FIELDS = ["double_seconds", "minute", "hour", "day", "month", "year_from_1980"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Exfat.Timestamp, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['double_seconds']['start'] = self._io.pos()
            self.double_seconds = self._io.read_bits_int_le(5)
            self._debug['double_seconds']['end'] = self._io.pos()
            self._debug['minute']['start'] = self._io.pos()
            self.minute = self._io.read_bits_int_le(6)
            self._debug['minute']['end'] = self._io.pos()
            self._debug['hour']['start'] = self._io.pos()
            self.hour = self._io.read_bits_int_le(5)
            self._debug['hour']['end'] = self._io.pos()
            self._debug['day']['start'] = self._io.pos()
            self.day = self._io.read_bits_int_le(5)
            self._debug['day']['end'] = self._io.pos()
            self._debug['month']['start'] = self._io.pos()
            self.month = self._io.read_bits_int_le(4)
            self._debug['month']['end'] = self._io.pos()
            self._debug['year_from_1980']['start'] = self._io.pos()
            self.year_from_1980 = self._io.read_bits_int_le(7)
            self._debug['year_from_1980']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def seconds(self):
            if hasattr(self, '_m_seconds'):
                return self._m_seconds

            self._m_seconds = self.double_seconds * 2
            return getattr(self, '_m_seconds', None)

        @property
        def year(self):
            if hasattr(self, '_m_year'):
                return self._m_year

            self._m_year = self.year_from_1980 + 1980
            return getattr(self, '_m_year', None)


    @property
    def bytes_per_sector_shift(self):
        if hasattr(self, '_m_bytes_per_sector_shift'):
            return self._m_bytes_per_sector_shift

        _pos = self._io.pos()
        self._io.seek(108)
        self._debug['_m_bytes_per_sector_shift']['start'] = self._io.pos()
        self._m_bytes_per_sector_shift = self._io.read_u1()
        self._debug['_m_bytes_per_sector_shift']['end'] = self._io.pos()
        if not self._m_bytes_per_sector_shift >= 9:
            raise kaitaistruct.ValidationLessThanError(9, self._m_bytes_per_sector_shift, self._io, u"/instances/bytes_per_sector_shift")
        if not self._m_bytes_per_sector_shift <= 12:
            raise kaitaistruct.ValidationGreaterThanError(12, self._m_bytes_per_sector_shift, self._io, u"/instances/bytes_per_sector_shift")
        self._io.seek(_pos)
        return getattr(self, '_m_bytes_per_sector_shift', None)

    @property
    def len_cluster(self):
        if hasattr(self, '_m_len_cluster'):
            return self._m_len_cluster

        self._m_len_cluster = self.sectors_per_cluster * self.len_sector
        return getattr(self, '_m_len_cluster', None)

    @property
    def len_sector(self):
        if hasattr(self, '_m_len_sector'):
            return self._m_len_sector

        self._m_len_sector = 1 << self.bytes_per_sector_shift
        return getattr(self, '_m_len_sector', None)

    @property
    def root_directory(self):
        if hasattr(self, '_m_root_directory'):
            return self._m_root_directory

        io = self.data_region.clusters.cluster[self.main_boot_region.boot_sector.first_cluster_of_root_directory - 2]._io
        _pos = io.pos()
        io.seek(0)
        self._debug['_m_root_directory']['start'] = io.pos()
        self._m_root_directory = Exfat.Directory(io, self, self._root)
        self._debug['_m_root_directory']['end'] = io.pos()
        io.seek(_pos)
        return getattr(self, '_m_root_directory', None)

    @property
    def sectors_per_cluster(self):
        if hasattr(self, '_m_sectors_per_cluster'):
            return self._m_sectors_per_cluster

        self._m_sectors_per_cluster = 1 << self.sectors_per_cluster_shift
        return getattr(self, '_m_sectors_per_cluster', None)

    @property
    def sectors_per_cluster_shift(self):
        if hasattr(self, '_m_sectors_per_cluster_shift'):
            return self._m_sectors_per_cluster_shift

        _pos = self._io.pos()
        self._io.seek(109)
        self._debug['_m_sectors_per_cluster_shift']['start'] = self._io.pos()
        self._m_sectors_per_cluster_shift = self._io.read_u1()
        self._debug['_m_sectors_per_cluster_shift']['end'] = self._io.pos()
        if not self._m_sectors_per_cluster_shift >= 0:
            raise kaitaistruct.ValidationLessThanError(0, self._m_sectors_per_cluster_shift, self._io, u"/instances/sectors_per_cluster_shift")
        if not self._m_sectors_per_cluster_shift <= 25 - self.bytes_per_sector_shift:
            raise kaitaistruct.ValidationGreaterThanError(25 - self.bytes_per_sector_shift, self._m_sectors_per_cluster_shift, self._io, u"/instances/sectors_per_cluster_shift")
        self._io.seek(_pos)
        return getattr(self, '_m_sectors_per_cluster_shift', None)


