# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import vfat_directory_rec
from .vfat_directory_rec import *
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Vfat(KaitaiStruct):

    class MediaDescriptor(IntEnum):
        drdos_8inch = 229
        tandy2000_525inch = 237
        drdos_nonstandard = 238
        drdos_superfloppy = 239
        standard_35inch = 240
        altos_double_density = 244
        altos_fixed_disk = 245
        media_f8 = 248
        media_f9 = 249
        media_fa = 250
        double_sided_640k = 251
        single_sided_180k = 252
        media_fd = 253
        media_fe = 254
        media_ff = 255
    SEQ_FIELDS = ["boot_sector"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Vfat, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['boot_sector']['start'] = self._io.pos()
        self.boot_sector = Vfat.BootSector(self._io, self, self._root)
        self._debug['boot_sector']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.boot_sector._fetch_instances()
        _ = self.fats
        if hasattr(self, '_m_fats'):
            pass
            for i in range(len(self._m_fats)):
                pass


        _ = self.root_dir
        if hasattr(self, '_m_root_dir'):
            pass
            self._m_root_dir._fetch_instances()


    class BiosParamBlock(KaitaiStruct):
        SEQ_FIELDS = ["bytes_per_ls", "ls_per_clus", "num_reserved_ls", "num_fats", "max_root_dir_rec", "total_ls_2", "media_code", "ls_per_fat", "ps_per_track", "num_heads", "num_hidden_sectors", "total_ls_4"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vfat.BiosParamBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['bytes_per_ls']['start'] = self._io.pos()
            self.bytes_per_ls = self._io.read_u2le()
            self._debug['bytes_per_ls']['end'] = self._io.pos()
            if not self.bytes_per_ls >= 32:
                raise kaitaistruct.ValidationLessThanError(32, self.bytes_per_ls, self._io, u"/types/bios_param_block/seq/0")
            self._debug['ls_per_clus']['start'] = self._io.pos()
            self.ls_per_clus = self._io.read_u1()
            self._debug['ls_per_clus']['end'] = self._io.pos()
            if not  ((self.ls_per_clus == 1) or (self.ls_per_clus == 2) or (self.ls_per_clus == 4) or (self.ls_per_clus == 8) or (self.ls_per_clus == 16) or (self.ls_per_clus == 32) or (self.ls_per_clus == 64) or (self.ls_per_clus == 128)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.ls_per_clus, self._io, u"/types/bios_param_block/seq/1")
            self._debug['num_reserved_ls']['start'] = self._io.pos()
            self.num_reserved_ls = self._io.read_u2le()
            self._debug['num_reserved_ls']['end'] = self._io.pos()
            self._debug['num_fats']['start'] = self._io.pos()
            self.num_fats = self._io.read_u1()
            self._debug['num_fats']['end'] = self._io.pos()
            self._debug['max_root_dir_rec']['start'] = self._io.pos()
            self.max_root_dir_rec = self._io.read_u2le()
            self._debug['max_root_dir_rec']['end'] = self._io.pos()
            self._debug['total_ls_2']['start'] = self._io.pos()
            self.total_ls_2 = self._io.read_u2le()
            self._debug['total_ls_2']['end'] = self._io.pos()
            self._debug['media_code']['start'] = self._io.pos()
            self.media_code = KaitaiStream.resolve_enum(Vfat.MediaDescriptor, self._io.read_u1())
            self._debug['media_code']['end'] = self._io.pos()
            self._debug['ls_per_fat']['start'] = self._io.pos()
            self.ls_per_fat = self._io.read_u2le()
            self._debug['ls_per_fat']['end'] = self._io.pos()
            self._debug['ps_per_track']['start'] = self._io.pos()
            self.ps_per_track = self._io.read_u2le()
            self._debug['ps_per_track']['end'] = self._io.pos()
            self._debug['num_heads']['start'] = self._io.pos()
            self.num_heads = self._io.read_u2le()
            self._debug['num_heads']['end'] = self._io.pos()
            self._debug['num_hidden_sectors']['start'] = self._io.pos()
            self.num_hidden_sectors = self._io.read_u4le()
            self._debug['num_hidden_sectors']['end'] = self._io.pos()
            self._debug['total_ls_4']['start'] = self._io.pos()
            self.total_ls_4 = self._io.read_u4le()
            self._debug['total_ls_4']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class BootSector(KaitaiStruct):
        SEQ_FIELDS = ["jmp_instruction", "oem_name", "bpb", "ebpb_fat16", "ebpb_fat32"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vfat.BootSector, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['jmp_instruction']['start'] = self._io.pos()
            self.jmp_instruction = Vfat.JmpInstruction(self._io, self, self._root)
            self._debug['jmp_instruction']['end'] = self._io.pos()
            _ = self.jmp_instruction
            if not self.jmp_instruction.is_valid:
                raise kaitaistruct.ValidationExprError(self.jmp_instruction, self._io, u"/types/boot_sector/seq/0")
            self._debug['oem_name']['start'] = self._io.pos()
            self.oem_name = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32)).decode(u"ASCII")
            self._debug['oem_name']['end'] = self._io.pos()
            self._debug['bpb']['start'] = self._io.pos()
            self.bpb = Vfat.BiosParamBlock(self._io, self, self._root)
            self._debug['bpb']['end'] = self._io.pos()
            if (not (self.is_fat32)):
                pass
                self._debug['ebpb_fat16']['start'] = self._io.pos()
                self.ebpb_fat16 = Vfat.ExtBiosParamBlockFat16(self._io, self, self._root)
                self._debug['ebpb_fat16']['end'] = self._io.pos()

            if self.is_fat32:
                pass
                self._debug['ebpb_fat32']['start'] = self._io.pos()
                self.ebpb_fat32 = Vfat.ExtBiosParamBlockFat32(self._io, self, self._root)
                self._debug['ebpb_fat32']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.jmp_instruction._fetch_instances()
            self.bpb._fetch_instances()
            if (not (self.is_fat32)):
                pass
                self.ebpb_fat16._fetch_instances()

            if self.is_fat32:
                pass
                self.ebpb_fat32._fetch_instances()


        @property
        def is_fat32(self):
            """Determines if filesystem is FAT32 (true) or FAT12/16 (false)
            by analyzing some preliminary conditions in BPB. Used to
            determine whether we should parse post-BPB data as
            `ext_bios_param_block_fat16` or `ext_bios_param_block_fat32`.
            """
            if hasattr(self, '_m_is_fat32'):
                return self._m_is_fat32

            self._m_is_fat32 = self.bpb.max_root_dir_rec == 0
            return getattr(self, '_m_is_fat32', None)

        @property
        def ls_per_fat(self):
            if hasattr(self, '_m_ls_per_fat'):
                return self._m_ls_per_fat

            self._m_ls_per_fat = (self.ebpb_fat32.ls_per_fat if self.is_fat32 else self.bpb.ls_per_fat)
            return getattr(self, '_m_ls_per_fat', None)

        @property
        def ls_per_root_dir(self):
            """Size of root directory in logical sectors.
            
            .. seealso::
               FAT: General Overview of On-Disk Format, section "FAT Data Structure"
            """
            if hasattr(self, '_m_ls_per_root_dir'):
                return self._m_ls_per_root_dir

            self._m_ls_per_root_dir = ((self.bpb.max_root_dir_rec * 32 + self.bpb.bytes_per_ls) - 1) // self.bpb.bytes_per_ls
            return getattr(self, '_m_ls_per_root_dir', None)

        @property
        def pos_fats(self):
            """Offset of FATs in bytes from start of filesystem."""
            if hasattr(self, '_m_pos_fats'):
                return self._m_pos_fats

            self._m_pos_fats = self.bpb.bytes_per_ls * self.bpb.num_reserved_ls
            return getattr(self, '_m_pos_fats', None)

        @property
        def pos_root_dir(self):
            """Offset of root directory in bytes from start of filesystem."""
            if hasattr(self, '_m_pos_root_dir'):
                return self._m_pos_root_dir

            self._m_pos_root_dir = self.bpb.bytes_per_ls * (self.bpb.num_reserved_ls + self.ls_per_fat * self.bpb.num_fats)
            return getattr(self, '_m_pos_root_dir', None)

        @property
        def size_fat(self):
            """Size of one FAT in bytes."""
            if hasattr(self, '_m_size_fat'):
                return self._m_size_fat

            self._m_size_fat = self.bpb.bytes_per_ls * self.ls_per_fat
            return getattr(self, '_m_size_fat', None)

        @property
        def size_root_dir(self):
            """Size of root directory in bytes."""
            if hasattr(self, '_m_size_root_dir'):
                return self._m_size_root_dir

            self._m_size_root_dir = self.ls_per_root_dir * self.bpb.bytes_per_ls
            return getattr(self, '_m_size_root_dir', None)


    class ExtBiosParamBlockFat16(KaitaiStruct):
        """Extended BIOS Parameter Block (DOS 4.0+, OS/2 1.0+). Used only
        for FAT12 and FAT16.
        """
        SEQ_FIELDS = ["phys_drive_num", "reserved1", "ext_boot_sign", "volume_id", "partition_volume_label", "fs_type_str"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vfat.ExtBiosParamBlockFat16, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['phys_drive_num']['start'] = self._io.pos()
            self.phys_drive_num = self._io.read_u1()
            self._debug['phys_drive_num']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_u1()
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['ext_boot_sign']['start'] = self._io.pos()
            self.ext_boot_sign = self._io.read_u1()
            self._debug['ext_boot_sign']['end'] = self._io.pos()
            if not  ((self.ext_boot_sign == 40) or (self.ext_boot_sign == 41)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.ext_boot_sign, self._io, u"/types/ext_bios_param_block_fat16/seq/2")
            self._debug['volume_id']['start'] = self._io.pos()
            self.volume_id = self._io.read_bytes(4)
            self._debug['volume_id']['end'] = self._io.pos()
            if self.is_extended:
                pass
                self._debug['partition_volume_label']['start'] = self._io.pos()
                self.partition_volume_label = (KaitaiStream.bytes_strip_right(self._io.read_bytes(11), 32)).decode(u"ASCII")
                self._debug['partition_volume_label']['end'] = self._io.pos()

            if self.is_extended:
                pass
                self._debug['fs_type_str']['start'] = self._io.pos()
                self.fs_type_str = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32)).decode(u"ASCII")
                self._debug['fs_type_str']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.is_extended:
                pass

            if self.is_extended:
                pass


        @property
        def is_extended(self):
            if hasattr(self, '_m_is_extended'):
                return self._m_is_extended

            self._m_is_extended = self.ext_boot_sign == 41
            return getattr(self, '_m_is_extended', None)


    class ExtBiosParamBlockFat32(KaitaiStruct):
        """Extended BIOS Parameter Block for FAT32."""
        SEQ_FIELDS = ["ls_per_fat", "has_active_fat", "reserved1", "active_fat_id", "reserved2", "fat_version", "root_dir_start_clus", "ls_fs_info", "boot_sectors_copy_start_ls", "reserved3", "phys_drive_num", "reserved4", "ext_boot_sign", "volume_id", "partition_volume_label", "fs_type_str"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vfat.ExtBiosParamBlockFat32, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ls_per_fat']['start'] = self._io.pos()
            self.ls_per_fat = self._io.read_u4le()
            self._debug['ls_per_fat']['end'] = self._io.pos()
            self._debug['has_active_fat']['start'] = self._io.pos()
            self.has_active_fat = self._io.read_bits_int_be(1) != 0
            self._debug['has_active_fat']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bits_int_be(3)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['active_fat_id']['start'] = self._io.pos()
            self.active_fat_id = self._io.read_bits_int_be(4)
            self._debug['active_fat_id']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bytes(1)
            self._debug['reserved2']['end'] = self._io.pos()
            if not self.reserved2 == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.reserved2, self._io, u"/types/ext_bios_param_block_fat32/seq/4")
            self._debug['fat_version']['start'] = self._io.pos()
            self.fat_version = self._io.read_u2le()
            self._debug['fat_version']['end'] = self._io.pos()
            self._debug['root_dir_start_clus']['start'] = self._io.pos()
            self.root_dir_start_clus = self._io.read_u4le()
            self._debug['root_dir_start_clus']['end'] = self._io.pos()
            self._debug['ls_fs_info']['start'] = self._io.pos()
            self.ls_fs_info = self._io.read_u2le()
            self._debug['ls_fs_info']['end'] = self._io.pos()
            self._debug['boot_sectors_copy_start_ls']['start'] = self._io.pos()
            self.boot_sectors_copy_start_ls = self._io.read_u2le()
            self._debug['boot_sectors_copy_start_ls']['end'] = self._io.pos()
            self._debug['reserved3']['start'] = self._io.pos()
            self.reserved3 = self._io.read_bytes(12)
            self._debug['reserved3']['end'] = self._io.pos()
            self._debug['phys_drive_num']['start'] = self._io.pos()
            self.phys_drive_num = self._io.read_u1()
            self._debug['phys_drive_num']['end'] = self._io.pos()
            self._debug['reserved4']['start'] = self._io.pos()
            self.reserved4 = self._io.read_u1()
            self._debug['reserved4']['end'] = self._io.pos()
            self._debug['ext_boot_sign']['start'] = self._io.pos()
            self.ext_boot_sign = self._io.read_u1()
            self._debug['ext_boot_sign']['end'] = self._io.pos()
            self._debug['volume_id']['start'] = self._io.pos()
            self.volume_id = self._io.read_bytes(4)
            self._debug['volume_id']['end'] = self._io.pos()
            self._debug['partition_volume_label']['start'] = self._io.pos()
            self.partition_volume_label = (KaitaiStream.bytes_strip_right(self._io.read_bytes(11), 32)).decode(u"ASCII")
            self._debug['partition_volume_label']['end'] = self._io.pos()
            self._debug['fs_type_str']['start'] = self._io.pos()
            self.fs_type_str = (KaitaiStream.bytes_strip_right(self._io.read_bytes(8), 32)).decode(u"ASCII")
            self._debug['fs_type_str']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class JmpInstruction(KaitaiStruct):
        SEQ_FIELDS = ["jmp_1", "jmp_2", "jmp_3"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vfat.JmpInstruction, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['jmp_1']['start'] = self._io.pos()
            self.jmp_1 = self._io.read_u1()
            self._debug['jmp_1']['end'] = self._io.pos()
            self._debug['jmp_2']['start'] = self._io.pos()
            self.jmp_2 = self._io.read_u1()
            self._debug['jmp_2']['end'] = self._io.pos()
            self._debug['jmp_3']['start'] = self._io.pos()
            self.jmp_3 = self._io.read_u1()
            self._debug['jmp_3']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def is_valid(self):
            if hasattr(self, '_m_is_valid'):
                return self._m_is_valid

            self._m_is_valid =  (( ((self.jmp_1 == 235) and (self.jmp_3 == 144)) ) or (self.jmp_1 == 233)) 
            return getattr(self, '_m_is_valid', None)


    class RootDirectory(KaitaiStruct):
        SEQ_FIELDS = ["records"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vfat.RootDirectory, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['records']['start'] = self._io.pos()
            self._debug['records']['arr'] = []
            self._raw_records = []
            self.records = []
            for i in range(self._root.boot_sector.bpb.max_root_dir_rec):
                self._debug['records']['arr'].append({'start': self._io.pos()})
                self._raw_records.append(self._io.read_bytes(32))
                _io__raw_records = KaitaiStream(BytesIO(self._raw_records[i]))
                self.records.append(vfat_directory_rec.VfatDirectoryRec(_io__raw_records))
                self._debug['records']['arr'][i]['end'] = self._io.pos()

            self._debug['records']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.records)):
                pass
                self.records[i]._fetch_instances()



    @property
    def fats(self):
        if hasattr(self, '_m_fats'):
            return self._m_fats

        _pos = self._io.pos()
        self._io.seek(self.boot_sector.pos_fats)
        self._debug['_m_fats']['start'] = self._io.pos()
        self._debug['_m_fats']['arr'] = []
        self._m_fats = []
        for i in range(self.boot_sector.bpb.num_fats):
            self._debug['_m_fats']['arr'].append({'start': self._io.pos()})
            self._m_fats.append(self._io.read_bytes(self.boot_sector.size_fat))
            self._debug['_m_fats']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_fats']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_fats', None)

    @property
    def root_dir(self):
        if hasattr(self, '_m_root_dir'):
            return self._m_root_dir

        _pos = self._io.pos()
        self._io.seek(self.boot_sector.pos_root_dir)
        self._debug['_m_root_dir']['start'] = self._io.pos()
        self._raw__m_root_dir = self._io.read_bytes(self.boot_sector.size_root_dir)
        _io__raw__m_root_dir = KaitaiStream(BytesIO(self._raw__m_root_dir))
        self._m_root_dir = Vfat.RootDirectory(_io__raw__m_root_dir, self, self._root)
        self._debug['_m_root_dir']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_root_dir', None)


