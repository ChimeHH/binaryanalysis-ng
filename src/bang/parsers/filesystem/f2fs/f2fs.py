# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class F2fs(KaitaiStruct):
    """
    .. seealso::
       Source - https://elinux.org/images/1/12/Elc2013_Hwang.pdf
    
    
    .. seealso::
       Source - https://docs.kernel.org/filesystems/f2fs.html
    """
    SEQ_FIELDS = ["superblock_segment", "checkpoint_segment", "segment_info", "node_address_table", "segment_summary_area", "main_area"]
    def __init__(self, _io, _parent=None, _root=None):
        super(F2fs, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['superblock_segment']['start'] = self._io.pos()
        self._raw_superblock_segment = self._io.read_bytes(self.segment_size)
        _io__raw_superblock_segment = KaitaiStream(BytesIO(self._raw_superblock_segment))
        self.superblock_segment = F2fs.SuperblockSegment(_io__raw_superblock_segment, self, self._root)
        self._debug['superblock_segment']['end'] = self._io.pos()
        self._debug['checkpoint_segment']['start'] = self._io.pos()
        self._raw_checkpoint_segment = self._io.read_bytes(self.superblock_segment.superblock.num_segments_checkpoint * self.segment_size)
        _io__raw_checkpoint_segment = KaitaiStream(BytesIO(self._raw_checkpoint_segment))
        self.checkpoint_segment = F2fs.CheckpointSegment(_io__raw_checkpoint_segment, self, self._root)
        self._debug['checkpoint_segment']['end'] = self._io.pos()
        self._debug['segment_info']['start'] = self._io.pos()
        self.segment_info = self._io.read_bytes(self.superblock_segment.superblock.num_segments_sit * self.segment_size)
        self._debug['segment_info']['end'] = self._io.pos()
        self._debug['node_address_table']['start'] = self._io.pos()
        self.node_address_table = self._io.read_bytes(self.superblock_segment.superblock.num_segments_nat * self.segment_size)
        self._debug['node_address_table']['end'] = self._io.pos()
        self._debug['segment_summary_area']['start'] = self._io.pos()
        self.segment_summary_area = self._io.read_bytes(self.superblock_segment.superblock.num_segments_ssa * self.segment_size)
        self._debug['segment_summary_area']['end'] = self._io.pos()
        self._debug['main_area']['start'] = self._io.pos()
        self.main_area = self._io.read_bytes(self.superblock_segment.superblock.num_segments_main * self.segment_size)
        self._debug['main_area']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.superblock_segment._fetch_instances()
        self.checkpoint_segment._fetch_instances()

    class Checkpoint(KaitaiStruct):
        SEQ_FIELDS = ["version", "num_user_blocks", "num_valid_blocks", "num_reserved_blocks", "num_overprovision_blocks", "num_free_segments", "cur_node_segment_numbers", "cur_node_block_offsets", "cur_data_segment_numbers", "cur_data_block_offsets", "flags", "num_pack_total_blocks", "data_summary_block_number", "num_valid_nodes", "num_valid_inodes", "next_free_node", "sit_ver_bitmap_bytesize", "nat_ver_bitmap_bytesize", "ofs_checksum", "elapsed_time", "alloc_type"]
        def __init__(self, _io, _parent=None, _root=None):
            super(F2fs.Checkpoint, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u8le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['num_user_blocks']['start'] = self._io.pos()
            self.num_user_blocks = self._io.read_u8le()
            self._debug['num_user_blocks']['end'] = self._io.pos()
            self._debug['num_valid_blocks']['start'] = self._io.pos()
            self.num_valid_blocks = self._io.read_u8le()
            self._debug['num_valid_blocks']['end'] = self._io.pos()
            self._debug['num_reserved_blocks']['start'] = self._io.pos()
            self.num_reserved_blocks = self._io.read_u4le()
            self._debug['num_reserved_blocks']['end'] = self._io.pos()
            self._debug['num_overprovision_blocks']['start'] = self._io.pos()
            self.num_overprovision_blocks = self._io.read_u4le()
            self._debug['num_overprovision_blocks']['end'] = self._io.pos()
            self._debug['num_free_segments']['start'] = self._io.pos()
            self.num_free_segments = self._io.read_u4le()
            self._debug['num_free_segments']['end'] = self._io.pos()
            self._debug['cur_node_segment_numbers']['start'] = self._io.pos()
            self._debug['cur_node_segment_numbers']['arr'] = []
            self.cur_node_segment_numbers = []
            for i in range(8):
                self._debug['cur_node_segment_numbers']['arr'].append({'start': self._io.pos()})
                self.cur_node_segment_numbers.append(self._io.read_u4le())
                self._debug['cur_node_segment_numbers']['arr'][i]['end'] = self._io.pos()

            self._debug['cur_node_segment_numbers']['end'] = self._io.pos()
            self._debug['cur_node_block_offsets']['start'] = self._io.pos()
            self._debug['cur_node_block_offsets']['arr'] = []
            self.cur_node_block_offsets = []
            for i in range(8):
                self._debug['cur_node_block_offsets']['arr'].append({'start': self._io.pos()})
                self.cur_node_block_offsets.append(self._io.read_u2le())
                self._debug['cur_node_block_offsets']['arr'][i]['end'] = self._io.pos()

            self._debug['cur_node_block_offsets']['end'] = self._io.pos()
            self._debug['cur_data_segment_numbers']['start'] = self._io.pos()
            self._debug['cur_data_segment_numbers']['arr'] = []
            self.cur_data_segment_numbers = []
            for i in range(8):
                self._debug['cur_data_segment_numbers']['arr'].append({'start': self._io.pos()})
                self.cur_data_segment_numbers.append(self._io.read_u4le())
                self._debug['cur_data_segment_numbers']['arr'][i]['end'] = self._io.pos()

            self._debug['cur_data_segment_numbers']['end'] = self._io.pos()
            self._debug['cur_data_block_offsets']['start'] = self._io.pos()
            self._debug['cur_data_block_offsets']['arr'] = []
            self.cur_data_block_offsets = []
            for i in range(8):
                self._debug['cur_data_block_offsets']['arr'].append({'start': self._io.pos()})
                self.cur_data_block_offsets.append(self._io.read_u2le())
                self._debug['cur_data_block_offsets']['arr'][i]['end'] = self._io.pos()

            self._debug['cur_data_block_offsets']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['num_pack_total_blocks']['start'] = self._io.pos()
            self.num_pack_total_blocks = self._io.read_u4le()
            self._debug['num_pack_total_blocks']['end'] = self._io.pos()
            self._debug['data_summary_block_number']['start'] = self._io.pos()
            self.data_summary_block_number = self._io.read_u4le()
            self._debug['data_summary_block_number']['end'] = self._io.pos()
            self._debug['num_valid_nodes']['start'] = self._io.pos()
            self.num_valid_nodes = self._io.read_u4le()
            self._debug['num_valid_nodes']['end'] = self._io.pos()
            self._debug['num_valid_inodes']['start'] = self._io.pos()
            self.num_valid_inodes = self._io.read_u4le()
            self._debug['num_valid_inodes']['end'] = self._io.pos()
            self._debug['next_free_node']['start'] = self._io.pos()
            self.next_free_node = self._io.read_u4le()
            self._debug['next_free_node']['end'] = self._io.pos()
            self._debug['sit_ver_bitmap_bytesize']['start'] = self._io.pos()
            self.sit_ver_bitmap_bytesize = self._io.read_u4le()
            self._debug['sit_ver_bitmap_bytesize']['end'] = self._io.pos()
            self._debug['nat_ver_bitmap_bytesize']['start'] = self._io.pos()
            self.nat_ver_bitmap_bytesize = self._io.read_u4le()
            self._debug['nat_ver_bitmap_bytesize']['end'] = self._io.pos()
            self._debug['ofs_checksum']['start'] = self._io.pos()
            self.ofs_checksum = self._io.read_u4le()
            self._debug['ofs_checksum']['end'] = self._io.pos()
            self._debug['elapsed_time']['start'] = self._io.pos()
            self.elapsed_time = self._io.read_u8le()
            self._debug['elapsed_time']['end'] = self._io.pos()
            self._debug['alloc_type']['start'] = self._io.pos()
            self.alloc_type = self._io.read_bytes(16)
            self._debug['alloc_type']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.cur_node_segment_numbers)):
                pass

            for i in range(len(self.cur_node_block_offsets)):
                pass

            for i in range(len(self.cur_data_segment_numbers)):
                pass

            for i in range(len(self.cur_data_block_offsets)):
                pass


        @property
        def compact_summary(self):
            if hasattr(self, '_m_compact_summary'):
                return self._m_compact_summary

            self._m_compact_summary = self.flags & 4 == 4
            return getattr(self, '_m_compact_summary', None)

        @property
        def crc_recovery(self):
            if hasattr(self, '_m_crc_recovery'):
                return self._m_crc_recovery

            self._m_crc_recovery = self.flags & 64 == 64
            return getattr(self, '_m_crc_recovery', None)

        @property
        def disabled(self):
            if hasattr(self, '_m_disabled'):
                return self._m_disabled

            self._m_disabled = self.flags & 4096 == 4096
            return getattr(self, '_m_disabled', None)

        @property
        def error(self):
            if hasattr(self, '_m_error'):
                return self._m_error

            self._m_error = self.flags & 8 == 8
            return getattr(self, '_m_error', None)

        @property
        def fastboot(self):
            if hasattr(self, '_m_fastboot'):
                return self._m_fastboot

            self._m_fastboot = self.flags & 32 == 32
            return getattr(self, '_m_fastboot', None)

        @property
        def fsck(self):
            if hasattr(self, '_m_fsck'):
                return self._m_fsck

            self._m_fsck = self.flags & 16 == 16
            return getattr(self, '_m_fsck', None)

        @property
        def large_nat_bitmap(self):
            if hasattr(self, '_m_large_nat_bitmap'):
                return self._m_large_nat_bitmap

            self._m_large_nat_bitmap = self.flags & 1024 == 1024
            return getattr(self, '_m_large_nat_bitmap', None)

        @property
        def nat_bits(self):
            if hasattr(self, '_m_nat_bits'):
                return self._m_nat_bits

            self._m_nat_bits = self.flags & 128 == 128
            return getattr(self, '_m_nat_bits', None)

        @property
        def no_crc_recovery(self):
            if hasattr(self, '_m_no_crc_recovery'):
                return self._m_no_crc_recovery

            self._m_no_crc_recovery = self.flags & 512 == 512
            return getattr(self, '_m_no_crc_recovery', None)

        @property
        def orphan_present(self):
            if hasattr(self, '_m_orphan_present'):
                return self._m_orphan_present

            self._m_orphan_present = self.flags & 2 == 2
            return getattr(self, '_m_orphan_present', None)

        @property
        def quota_need_fsck(self):
            if hasattr(self, '_m_quota_need_fsck'):
                return self._m_quota_need_fsck

            self._m_quota_need_fsck = self.flags & 2048 == 2048
            return getattr(self, '_m_quota_need_fsck', None)

        @property
        def resizefs(self):
            if hasattr(self, '_m_resizefs'):
                return self._m_resizefs

            self._m_resizefs = self.flags & 16384 == 16384
            return getattr(self, '_m_resizefs', None)

        @property
        def trimmed(self):
            if hasattr(self, '_m_trimmed'):
                return self._m_trimmed

            self._m_trimmed = self.flags & 256 == 256
            return getattr(self, '_m_trimmed', None)

        @property
        def unmount(self):
            if hasattr(self, '_m_unmount'):
                return self._m_unmount

            self._m_unmount = self.flags & 1 == 1
            return getattr(self, '_m_unmount', None)


    class CheckpointSegment(KaitaiStruct):
        SEQ_FIELDS = ["checkpoint"]
        def __init__(self, _io, _parent=None, _root=None):
            super(F2fs.CheckpointSegment, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['checkpoint']['start'] = self._io.pos()
            self._raw_checkpoint = self._io.read_bytes(192)
            _io__raw_checkpoint = KaitaiStream(BytesIO(self._raw_checkpoint))
            self.checkpoint = F2fs.Checkpoint(_io__raw_checkpoint, self, self._root)
            self._debug['checkpoint']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.checkpoint._fetch_instances()


    class F2fsDevice(KaitaiStruct):
        SEQ_FIELDS = ["path", "total_segments"]
        def __init__(self, _io, _parent=None, _root=None):
            super(F2fs.F2fsDevice, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['path']['start'] = self._io.pos()
            self.path = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"UTF-8")
            self._debug['path']['end'] = self._io.pos()
            self._debug['total_segments']['start'] = self._io.pos()
            self.total_segments = self._io.read_u4le()
            self._debug['total_segments']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Superblock(KaitaiStruct):
        SEQ_FIELDS = ["reserved", "magic", "version", "log_sector_size", "log_sectors_per_block", "log_blocksize", "log_blocks_per_segment", "segments_per_section", "sections_per_zone", "ofs_checksum", "num_blocks", "num_sections", "num_segments", "num_segments_checkpoint", "num_segments_sit", "num_segments_nat", "num_segments_ssa", "num_segments_main", "segment0_block_address", "checkpoint_block_address", "sit_block_address", "nat_block_address", "ssa_block_address", "main_area_block_address", "root_inode_numner", "node_inode_numner", "meta_inode_numner", "uuid", "volume_name", "extension_count", "extension_list", "checkpoint_payload", "kernel_version", "initial_kernel_version", "features", "encryption_level", "encrypt_password_salt", "f2fs_devices", "qf_infos", "num_hot_extensions", "filename_charset_encoding", "filename_charset_encoding_flags", "stop_checkpoint_reason", "errors", "reserved_2", "crc"]
        def __init__(self, _io, _parent=None, _root=None):
            super(F2fs.Superblock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(1024)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_u4le()
            self._debug['magic']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = F2fs.Version(self._io, self, self._root)
            self._debug['version']['end'] = self._io.pos()
            self._debug['log_sector_size']['start'] = self._io.pos()
            self.log_sector_size = self._io.read_u4le()
            self._debug['log_sector_size']['end'] = self._io.pos()
            self._debug['log_sectors_per_block']['start'] = self._io.pos()
            self.log_sectors_per_block = self._io.read_u4le()
            self._debug['log_sectors_per_block']['end'] = self._io.pos()
            self._debug['log_blocksize']['start'] = self._io.pos()
            self.log_blocksize = self._io.read_u4le()
            self._debug['log_blocksize']['end'] = self._io.pos()
            self._debug['log_blocks_per_segment']['start'] = self._io.pos()
            self.log_blocks_per_segment = self._io.read_u4le()
            self._debug['log_blocks_per_segment']['end'] = self._io.pos()
            self._debug['segments_per_section']['start'] = self._io.pos()
            self.segments_per_section = self._io.read_u4le()
            self._debug['segments_per_section']['end'] = self._io.pos()
            self._debug['sections_per_zone']['start'] = self._io.pos()
            self.sections_per_zone = self._io.read_u4le()
            self._debug['sections_per_zone']['end'] = self._io.pos()
            self._debug['ofs_checksum']['start'] = self._io.pos()
            self.ofs_checksum = self._io.read_u4le()
            self._debug['ofs_checksum']['end'] = self._io.pos()
            self._debug['num_blocks']['start'] = self._io.pos()
            self.num_blocks = self._io.read_u8le()
            self._debug['num_blocks']['end'] = self._io.pos()
            self._debug['num_sections']['start'] = self._io.pos()
            self.num_sections = self._io.read_u4le()
            self._debug['num_sections']['end'] = self._io.pos()
            self._debug['num_segments']['start'] = self._io.pos()
            self.num_segments = self._io.read_u4le()
            self._debug['num_segments']['end'] = self._io.pos()
            self._debug['num_segments_checkpoint']['start'] = self._io.pos()
            self.num_segments_checkpoint = self._io.read_u4le()
            self._debug['num_segments_checkpoint']['end'] = self._io.pos()
            self._debug['num_segments_sit']['start'] = self._io.pos()
            self.num_segments_sit = self._io.read_u4le()
            self._debug['num_segments_sit']['end'] = self._io.pos()
            self._debug['num_segments_nat']['start'] = self._io.pos()
            self.num_segments_nat = self._io.read_u4le()
            self._debug['num_segments_nat']['end'] = self._io.pos()
            self._debug['num_segments_ssa']['start'] = self._io.pos()
            self.num_segments_ssa = self._io.read_u4le()
            self._debug['num_segments_ssa']['end'] = self._io.pos()
            self._debug['num_segments_main']['start'] = self._io.pos()
            self.num_segments_main = self._io.read_u4le()
            self._debug['num_segments_main']['end'] = self._io.pos()
            self._debug['segment0_block_address']['start'] = self._io.pos()
            self.segment0_block_address = self._io.read_u4le()
            self._debug['segment0_block_address']['end'] = self._io.pos()
            self._debug['checkpoint_block_address']['start'] = self._io.pos()
            self.checkpoint_block_address = self._io.read_u4le()
            self._debug['checkpoint_block_address']['end'] = self._io.pos()
            self._debug['sit_block_address']['start'] = self._io.pos()
            self.sit_block_address = self._io.read_u4le()
            self._debug['sit_block_address']['end'] = self._io.pos()
            self._debug['nat_block_address']['start'] = self._io.pos()
            self.nat_block_address = self._io.read_u4le()
            self._debug['nat_block_address']['end'] = self._io.pos()
            self._debug['ssa_block_address']['start'] = self._io.pos()
            self.ssa_block_address = self._io.read_u4le()
            self._debug['ssa_block_address']['end'] = self._io.pos()
            self._debug['main_area_block_address']['start'] = self._io.pos()
            self.main_area_block_address = self._io.read_u4le()
            self._debug['main_area_block_address']['end'] = self._io.pos()
            self._debug['root_inode_numner']['start'] = self._io.pos()
            self.root_inode_numner = self._io.read_u4le()
            self._debug['root_inode_numner']['end'] = self._io.pos()
            self._debug['node_inode_numner']['start'] = self._io.pos()
            self.node_inode_numner = self._io.read_u4le()
            self._debug['node_inode_numner']['end'] = self._io.pos()
            self._debug['meta_inode_numner']['start'] = self._io.pos()
            self.meta_inode_numner = self._io.read_u4le()
            self._debug['meta_inode_numner']['end'] = self._io.pos()
            self._debug['uuid']['start'] = self._io.pos()
            self.uuid = self._io.read_bytes(16)
            self._debug['uuid']['end'] = self._io.pos()
            self._debug['volume_name']['start'] = self._io.pos()
            self.volume_name = self._io.read_bytes(1024)
            self._debug['volume_name']['end'] = self._io.pos()
            self._debug['extension_count']['start'] = self._io.pos()
            self.extension_count = self._io.read_u4le()
            self._debug['extension_count']['end'] = self._io.pos()
            self._debug['extension_list']['start'] = self._io.pos()
            self._debug['extension_list']['arr'] = []
            self.extension_list = []
            for i in range(64):
                self._debug['extension_list']['arr'].append({'start': self._io.pos()})
                self.extension_list.append((KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)).decode(u"UTF-8"))
                self._debug['extension_list']['arr'][i]['end'] = self._io.pos()

            self._debug['extension_list']['end'] = self._io.pos()
            self._debug['checkpoint_payload']['start'] = self._io.pos()
            self.checkpoint_payload = self._io.read_u4le()
            self._debug['checkpoint_payload']['end'] = self._io.pos()
            self._debug['kernel_version']['start'] = self._io.pos()
            self.kernel_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['kernel_version']['end'] = self._io.pos()
            self._debug['initial_kernel_version']['start'] = self._io.pos()
            self.initial_kernel_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['initial_kernel_version']['end'] = self._io.pos()
            self._debug['features']['start'] = self._io.pos()
            self.features = self._io.read_u4le()
            self._debug['features']['end'] = self._io.pos()
            self._debug['encryption_level']['start'] = self._io.pos()
            self.encryption_level = self._io.read_u1()
            self._debug['encryption_level']['end'] = self._io.pos()
            self._debug['encrypt_password_salt']['start'] = self._io.pos()
            self.encrypt_password_salt = self._io.read_bytes(16)
            self._debug['encrypt_password_salt']['end'] = self._io.pos()
            self._debug['f2fs_devices']['start'] = self._io.pos()
            self._debug['f2fs_devices']['arr'] = []
            self.f2fs_devices = []
            for i in range(8):
                self._debug['f2fs_devices']['arr'].append({'start': self._io.pos()})
                self.f2fs_devices.append(F2fs.F2fsDevice(self._io, self, self._root))
                self._debug['f2fs_devices']['arr'][i]['end'] = self._io.pos()

            self._debug['f2fs_devices']['end'] = self._io.pos()
            self._debug['qf_infos']['start'] = self._io.pos()
            self._debug['qf_infos']['arr'] = []
            self.qf_infos = []
            for i in range(3):
                self._debug['qf_infos']['arr'].append({'start': self._io.pos()})
                self.qf_infos.append(self._io.read_u4le())
                self._debug['qf_infos']['arr'][i]['end'] = self._io.pos()

            self._debug['qf_infos']['end'] = self._io.pos()
            self._debug['num_hot_extensions']['start'] = self._io.pos()
            self.num_hot_extensions = self._io.read_u1()
            self._debug['num_hot_extensions']['end'] = self._io.pos()
            self._debug['filename_charset_encoding']['start'] = self._io.pos()
            self.filename_charset_encoding = self._io.read_u2le()
            self._debug['filename_charset_encoding']['end'] = self._io.pos()
            self._debug['filename_charset_encoding_flags']['start'] = self._io.pos()
            self.filename_charset_encoding_flags = self._io.read_u2le()
            self._debug['filename_charset_encoding_flags']['end'] = self._io.pos()
            self._debug['stop_checkpoint_reason']['start'] = self._io.pos()
            self.stop_checkpoint_reason = self._io.read_bytes(32)
            self._debug['stop_checkpoint_reason']['end'] = self._io.pos()
            self._debug['errors']['start'] = self._io.pos()
            self.errors = self._io.read_bytes(16)
            self._debug['errors']['end'] = self._io.pos()
            self._debug['reserved_2']['start'] = self._io.pos()
            self.reserved_2 = self._io.read_bytes(258)
            self._debug['reserved_2']['end'] = self._io.pos()
            self._debug['crc']['start'] = self._io.pos()
            self.crc = self._io.read_u4le()
            self._debug['crc']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.version._fetch_instances()
            for i in range(len(self.extension_list)):
                pass

            for i in range(len(self.f2fs_devices)):
                pass
                self.f2fs_devices[i]._fetch_instances()

            for i in range(len(self.qf_infos)):
                pass


        @property
        def atomic_write(self):
            if hasattr(self, '_m_atomic_write'):
                return self._m_atomic_write

            self._m_atomic_write = self.features & 4 == 4
            return getattr(self, '_m_atomic_write', None)

        @property
        def blocksize(self):
            if hasattr(self, '_m_blocksize'):
                return self._m_blocksize

            self._m_blocksize = 1 << self.log_blocksize
            return getattr(self, '_m_blocksize', None)

        @property
        def blockzoned(self):
            if hasattr(self, '_m_blockzoned'):
                return self._m_blockzoned

            self._m_blockzoned = self.features & 2 == 2
            return getattr(self, '_m_blockzoned', None)

        @property
        def casefold(self):
            if hasattr(self, '_m_casefold'):
                return self._m_casefold

            self._m_casefold = self.features & 4096 == 4096
            return getattr(self, '_m_casefold', None)

        @property
        def checkpoint_offset(self):
            if hasattr(self, '_m_checkpoint_offset'):
                return self._m_checkpoint_offset

            self._m_checkpoint_offset = self.blocksize * self.checkpoint_block_address
            return getattr(self, '_m_checkpoint_offset', None)

        @property
        def compression(self):
            if hasattr(self, '_m_compression'):
                return self._m_compression

            self._m_compression = self.features & 8192 == 8192
            return getattr(self, '_m_compression', None)

        @property
        def encrypted(self):
            if hasattr(self, '_m_encrypted'):
                return self._m_encrypted

            self._m_encrypted = self.features & 1 == 1
            return getattr(self, '_m_encrypted', None)

        @property
        def extra_attrs(self):
            if hasattr(self, '_m_extra_attrs'):
                return self._m_extra_attrs

            self._m_extra_attrs = self.features & 8 == 8
            return getattr(self, '_m_extra_attrs', None)

        @property
        def flexible_inline_xattr(self):
            if hasattr(self, '_m_flexible_inline_xattr'):
                return self._m_flexible_inline_xattr

            self._m_flexible_inline_xattr = self.features & 64 == 64
            return getattr(self, '_m_flexible_inline_xattr', None)

        @property
        def inode_checksum(self):
            if hasattr(self, '_m_inode_checksum'):
                return self._m_inode_checksum

            self._m_inode_checksum = self.features & 32 == 32
            return getattr(self, '_m_inode_checksum', None)

        @property
        def inode_crtime(self):
            if hasattr(self, '_m_inode_crtime'):
                return self._m_inode_crtime

            self._m_inode_crtime = self.features & 256 == 256
            return getattr(self, '_m_inode_crtime', None)

        @property
        def lost_found(self):
            if hasattr(self, '_m_lost_found'):
                return self._m_lost_found

            self._m_lost_found = self.features & 512 == 512
            return getattr(self, '_m_lost_found', None)

        @property
        def prj_quota(self):
            if hasattr(self, '_m_prj_quota'):
                return self._m_prj_quota

            self._m_prj_quota = self.features & 16 == 16
            return getattr(self, '_m_prj_quota', None)

        @property
        def quota_ino(self):
            if hasattr(self, '_m_quota_ino'):
                return self._m_quota_ino

            self._m_quota_ino = self.features & 128 == 128
            return getattr(self, '_m_quota_ino', None)

        @property
        def readonly(self):
            if hasattr(self, '_m_readonly'):
                return self._m_readonly

            self._m_readonly = self.features & 16384 == 16384
            return getattr(self, '_m_readonly', None)

        @property
        def sit_offset(self):
            if hasattr(self, '_m_sit_offset'):
                return self._m_sit_offset

            self._m_sit_offset = self.blocksize * self.sit_block_address
            return getattr(self, '_m_sit_offset', None)

        @property
        def superblock_checksum(self):
            if hasattr(self, '_m_superblock_checksum'):
                return self._m_superblock_checksum

            self._m_superblock_checksum = self.features & 2048 == 2048
            return getattr(self, '_m_superblock_checksum', None)

        @property
        def verity(self):
            if hasattr(self, '_m_verity'):
                return self._m_verity

            self._m_verity = self.features & 1024 == 1024
            return getattr(self, '_m_verity', None)


    class SuperblockSegment(KaitaiStruct):
        SEQ_FIELDS = ["superblock", "superblock_backup"]
        def __init__(self, _io, _parent=None, _root=None):
            super(F2fs.SuperblockSegment, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['superblock']['start'] = self._io.pos()
            self._raw_superblock = self._io.read_bytes(4096)
            _io__raw_superblock = KaitaiStream(BytesIO(self._raw_superblock))
            self.superblock = F2fs.Superblock(_io__raw_superblock, self, self._root)
            self._debug['superblock']['end'] = self._io.pos()
            self._debug['superblock_backup']['start'] = self._io.pos()
            self._raw_superblock_backup = self._io.read_bytes(4096)
            _io__raw_superblock_backup = KaitaiStream(BytesIO(self._raw_superblock_backup))
            self.superblock_backup = F2fs.Superblock(_io__raw_superblock_backup, self, self._root)
            self._debug['superblock_backup']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.superblock._fetch_instances()
            self.superblock_backup._fetch_instances()


    class Version(KaitaiStruct):
        SEQ_FIELDS = ["major", "minor"]
        def __init__(self, _io, _parent=None, _root=None):
            super(F2fs.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u2le()
            self._debug['major']['end'] = self._io.pos()
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u2le()
            self._debug['minor']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def segment_size(self):
        if hasattr(self, '_m_segment_size'):
            return self._m_segment_size

        self._m_segment_size = 2097152
        return getattr(self, '_m_segment_size', None)


