# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Erofs(KaitaiStruct):
    """Enhanced Read Only File System (erofs) is a file system for use on flash
    storage. It is used on Android, as well as for cloud services (particularly
    Alibaba's cloud solution).
    
    Test files can be easily created using mkfs.erofs from erofs-utils.
    
    .. seealso::
       Source - https://git.kernel.org/pub/scm/linux/kernel/git/xiang/erofs-utils.git
    
    
    .. seealso::
       Source - https://git.kernel.org/pub/scm/linux/kernel/git/xiang/erofs-utils.git/tree/include/erofs_fs.h
    """

    class Compression(IntEnum):
        lz4 = 0
        lzma = 1
        deflate = 2
        zstd = 3

    class FileTypes(IntEnum):
        unknown = 0
        regular_file = 1
        directory = 2
        character_device = 3
        block_device = 4
        fifo = 5
        socket = 6
        symlink = 7

    class XattrNameIndex(IntEnum):
        user = 1
        posix_acl_access = 2
        posix_acl_default = 3
        trusted = 4
        lustre = 5
        security = 6
    SEQ_FIELDS = ["data", "superblock"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Erofs, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['data']['start'] = self._io.pos()
        self.data = self._io.read_bytes(1024)
        self._debug['data']['end'] = self._io.pos()
        self._debug['superblock']['start'] = self._io.pos()
        self.superblock = Erofs.Superblock(self._io, self, self._root)
        self._debug['superblock']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.superblock._fetch_instances()
        _ = self.blocks
        if hasattr(self, '_m_blocks'):
            pass
            for i in range(len(self._m_blocks)):
                pass


        _ = self.root_inode
        if hasattr(self, '_m_root_inode'):
            pass
            self._m_root_inode._fetch_instances()


    class ChunkInfo(KaitaiStruct):
        SEQ_FIELDS = ["format", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.ChunkInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['format']['start'] = self._io.pos()
            self.format = self._io.read_u2le()
            self._debug['format']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(2)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class CompactInode(KaitaiStruct):
        SEQ_FIELDS = ["nlink", "len_inode", "reserved_1", "specific", "ino", "uid", "gid", "reserved_2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.CompactInode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['nlink']['start'] = self._io.pos()
            self.nlink = self._io.read_u2le()
            self._debug['nlink']['end'] = self._io.pos()
            self._debug['len_inode']['start'] = self._io.pos()
            self.len_inode = self._io.read_u4le()
            self._debug['len_inode']['end'] = self._io.pos()
            self._debug['reserved_1']['start'] = self._io.pos()
            self.reserved_1 = self._io.read_u4le()
            self._debug['reserved_1']['end'] = self._io.pos()
            self._debug['specific']['start'] = self._io.pos()
            self._raw_specific = self._io.read_bytes(4)
            _io__raw_specific = KaitaiStream(BytesIO(self._raw_specific))
            self.specific = Erofs.NodeSpecificUnion(_io__raw_specific, self, self._root)
            self._debug['specific']['end'] = self._io.pos()
            self._debug['ino']['start'] = self._io.pos()
            self.ino = self._io.read_u4le()
            self._debug['ino']['end'] = self._io.pos()
            self._debug['uid']['start'] = self._io.pos()
            self.uid = self._io.read_u2le()
            self._debug['uid']['end'] = self._io.pos()
            self._debug['gid']['start'] = self._io.pos()
            self.gid = self._io.read_u2le()
            self._debug['gid']['end'] = self._io.pos()
            self._debug['reserved_2']['start'] = self._io.pos()
            self.reserved_2 = self._io.read_u4le()
            self._debug['reserved_2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.specific._fetch_instances()


    class DirectoryEntries(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.DirectoryEntries, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Erofs.DirectoryEntry(i, self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()

            _ = self.first_name_offset
            if hasattr(self, '_m_first_name_offset'):
                pass

            _ = self.names
            if hasattr(self, '_m_names'):
                pass
                for i in range(len(self._m_names)):
                    pass
                    self._m_names[i]._fetch_instances()



        class Name(KaitaiStruct):
            SEQ_FIELDS = []
            def __init__(self, index, _io, _parent=None, _root=None):
                super(Erofs.DirectoryEntries.Name, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self.index = index
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                pass


            def _fetch_instances(self):
                pass
                _ = self.name
                if hasattr(self, '_m_name'):
                    pass


            @property
            def len_name(self):
                if hasattr(self, '_m_len_name'):
                    return self._m_len_name

                self._m_len_name = (self._parent._parent._parent.len_inode - self._parent.entries[self.index].ofs_name if self.index == len(self._parent.entries) - 1 else self._parent.entries[self.index + 1].ofs_name - self._parent.entries[self.index].ofs_name)
                return getattr(self, '_m_len_name', None)

            @property
            def name(self):
                if hasattr(self, '_m_name'):
                    return self._m_name

                _pos = self._io.pos()
                self._io.seek(self._parent.entries[self.index].ofs_name)
                self._debug['_m_name']['start'] = self._io.pos()
                self._m_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_name), 0, False)).decode(u"UTF-8")
                self._debug['_m_name']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_name', None)


        @property
        def first_name_offset(self):
            if hasattr(self, '_m_first_name_offset'):
                return self._m_first_name_offset

            _pos = self._io.pos()
            self._io.seek(8)
            self._debug['_m_first_name_offset']['start'] = self._io.pos()
            self._m_first_name_offset = self._io.read_u2le()
            self._debug['_m_first_name_offset']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_first_name_offset', None)

        @property
        def names(self):
            if hasattr(self, '_m_names'):
                return self._m_names

            self._debug['_m_names']['start'] = self._io.pos()
            self._debug['_m_names']['arr'] = []
            self._m_names = []
            for i in range(self.num_entries):
                self._debug['_m_names']['arr'].append({'start': self._io.pos()})
                self._m_names.append(Erofs.DirectoryEntries.Name(i, self._io, self, self._root))
                self._debug['_m_names']['arr'][i]['end'] = self._io.pos()

            self._debug['_m_names']['end'] = self._io.pos()
            return getattr(self, '_m_names', None)

        @property
        def num_entries(self):
            if hasattr(self, '_m_num_entries'):
                return self._m_num_entries

            self._m_num_entries = self.first_name_offset // 12
            return getattr(self, '_m_num_entries', None)


    class DirectoryEntry(KaitaiStruct):
        SEQ_FIELDS = ["node_id", "ofs_name", "file_type", "reserved"]
        def __init__(self, index, _io, _parent=None, _root=None):
            super(Erofs.DirectoryEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.index = index
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['node_id']['start'] = self._io.pos()
            self.node_id = self._io.read_u8le()
            self._debug['node_id']['end'] = self._io.pos()
            self._debug['ofs_name']['start'] = self._io.pos()
            self.ofs_name = self._io.read_u2le()
            self._debug['ofs_name']['end'] = self._io.pos()
            self._debug['file_type']['start'] = self._io.pos()
            self.file_type = KaitaiStream.resolve_enum(Erofs.FileTypes, self._io.read_u1())
            self._debug['file_type']['end'] = self._io.pos()
            if not  ((self.file_type == Erofs.FileTypes.regular_file) or (self.file_type == Erofs.FileTypes.directory) or (self.file_type == Erofs.FileTypes.character_device) or (self.file_type == Erofs.FileTypes.block_device) or (self.file_type == Erofs.FileTypes.fifo) or (self.file_type == Erofs.FileTypes.socket) or (self.file_type == Erofs.FileTypes.symlink)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.file_type, self._io, u"/types/directory_entry/seq/2")
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u1()
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.inode
            if hasattr(self, '_m_inode'):
                pass
                self._m_inode._fetch_instances()


        @property
        def inode(self):
            if hasattr(self, '_m_inode'):
                return self._m_inode

            io = self._root._io
            _pos = io.pos()
            io.seek(self._root.ofs_metadata_area + 32 * self.node_id)
            self._debug['_m_inode']['start'] = io.pos()
            self._m_inode = Erofs.Inode(io, self, self._root)
            self._debug['_m_inode']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_inode', None)

        @property
        def name(self):
            if hasattr(self, '_m_name'):
                return self._m_name

            self._m_name = self._parent.names[self.index]
            return getattr(self, '_m_name', None)


    class ExtendedInode(KaitaiStruct):
        SEQ_FIELDS = ["reserved_1", "len_inode", "specific", "ino", "uid", "gid", "ctime", "ctime_nsec", "nlink", "reserved_2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.ExtendedInode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved_1']['start'] = self._io.pos()
            self.reserved_1 = self._io.read_u2le()
            self._debug['reserved_1']['end'] = self._io.pos()
            self._debug['len_inode']['start'] = self._io.pos()
            self.len_inode = self._io.read_u8le()
            self._debug['len_inode']['end'] = self._io.pos()
            self._debug['specific']['start'] = self._io.pos()
            self._raw_specific = self._io.read_bytes(4)
            _io__raw_specific = KaitaiStream(BytesIO(self._raw_specific))
            self.specific = Erofs.NodeSpecificUnion(_io__raw_specific, self, self._root)
            self._debug['specific']['end'] = self._io.pos()
            self._debug['ino']['start'] = self._io.pos()
            self.ino = self._io.read_u4le()
            self._debug['ino']['end'] = self._io.pos()
            self._debug['uid']['start'] = self._io.pos()
            self.uid = self._io.read_u4le()
            self._debug['uid']['end'] = self._io.pos()
            self._debug['gid']['start'] = self._io.pos()
            self.gid = self._io.read_u4le()
            self._debug['gid']['end'] = self._io.pos()
            self._debug['ctime']['start'] = self._io.pos()
            self.ctime = self._io.read_u8le()
            self._debug['ctime']['end'] = self._io.pos()
            self._debug['ctime_nsec']['start'] = self._io.pos()
            self.ctime_nsec = self._io.read_u4le()
            self._debug['ctime_nsec']['end'] = self._io.pos()
            self._debug['nlink']['start'] = self._io.pos()
            self.nlink = self._io.read_u4le()
            self._debug['nlink']['end'] = self._io.pos()
            self._debug['reserved_2']['start'] = self._io.pos()
            self.reserved_2 = self._io.read_bytes(16)
            self._debug['reserved_2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.specific._fetch_instances()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["root_nid", "inos", "build_time", "build_time_nsec", "num_blocks", "meta_block_address", "xattr_block_address", "uuid", "volume_name", "feature_incompat_flags", "compression_information", "extra_devices", "devt_slotoff", "dir_block_bits", "num_xattr_prefix", "ofs_xattr_prefix", "packed_nid", "reserved_2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['root_nid']['start'] = self._io.pos()
            self.root_nid = self._io.read_u2le()
            self._debug['root_nid']['end'] = self._io.pos()
            self._debug['inos']['start'] = self._io.pos()
            self.inos = self._io.read_u8le()
            self._debug['inos']['end'] = self._io.pos()
            self._debug['build_time']['start'] = self._io.pos()
            self.build_time = self._io.read_u8le()
            self._debug['build_time']['end'] = self._io.pos()
            self._debug['build_time_nsec']['start'] = self._io.pos()
            self.build_time_nsec = self._io.read_u4le()
            self._debug['build_time_nsec']['end'] = self._io.pos()
            self._debug['num_blocks']['start'] = self._io.pos()
            self.num_blocks = self._io.read_u4le()
            self._debug['num_blocks']['end'] = self._io.pos()
            self._debug['meta_block_address']['start'] = self._io.pos()
            self.meta_block_address = self._io.read_u4le()
            self._debug['meta_block_address']['end'] = self._io.pos()
            self._debug['xattr_block_address']['start'] = self._io.pos()
            self.xattr_block_address = self._io.read_u4le()
            self._debug['xattr_block_address']['end'] = self._io.pos()
            self._debug['uuid']['start'] = self._io.pos()
            self.uuid = self._io.read_bytes(16)
            self._debug['uuid']['end'] = self._io.pos()
            self._debug['volume_name']['start'] = self._io.pos()
            self.volume_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"UTF-8")
            self._debug['volume_name']['end'] = self._io.pos()
            self._debug['feature_incompat_flags']['start'] = self._io.pos()
            self.feature_incompat_flags = self._io.read_u4le()
            self._debug['feature_incompat_flags']['end'] = self._io.pos()
            self._debug['compression_information']['start'] = self._io.pos()
            self._raw_compression_information = self._io.read_bytes(2)
            _io__raw_compression_information = KaitaiStream(BytesIO(self._raw_compression_information))
            self.compression_information = Erofs.Header.CompressionInformation(_io__raw_compression_information, self, self._root)
            self._debug['compression_information']['end'] = self._io.pos()
            self._debug['extra_devices']['start'] = self._io.pos()
            self.extra_devices = self._io.read_u2le()
            self._debug['extra_devices']['end'] = self._io.pos()
            self._debug['devt_slotoff']['start'] = self._io.pos()
            self.devt_slotoff = self._io.read_u2le()
            self._debug['devt_slotoff']['end'] = self._io.pos()
            self._debug['dir_block_bits']['start'] = self._io.pos()
            self.dir_block_bits = self._io.read_u1()
            self._debug['dir_block_bits']['end'] = self._io.pos()
            self._debug['num_xattr_prefix']['start'] = self._io.pos()
            self.num_xattr_prefix = self._io.read_u1()
            self._debug['num_xattr_prefix']['end'] = self._io.pos()
            self._debug['ofs_xattr_prefix']['start'] = self._io.pos()
            self.ofs_xattr_prefix = self._io.read_u4le()
            self._debug['ofs_xattr_prefix']['end'] = self._io.pos()
            self._debug['packed_nid']['start'] = self._io.pos()
            self.packed_nid = self._io.read_u8le()
            self._debug['packed_nid']['end'] = self._io.pos()
            self._debug['reserved_2']['start'] = self._io.pos()
            self.reserved_2 = self._io.read_bytes(24)
            self._debug['reserved_2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.compression_information._fetch_instances()

        class CompressionInformation(KaitaiStruct):
            SEQ_FIELDS = ["raw"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Erofs.Header.CompressionInformation, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['raw']['start'] = self._io.pos()
                self.raw = self._io.read_bytes(2)
                self._debug['raw']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _ = self.available_compression_algorithms
                if hasattr(self, '_m_available_compression_algorithms'):
                    pass

                _ = self.lz4_max_distance
                if hasattr(self, '_m_lz4_max_distance'):
                    pass


            @property
            def available_compression_algorithms(self):
                if hasattr(self, '_m_available_compression_algorithms'):
                    return self._m_available_compression_algorithms

                _pos = self._io.pos()
                self._io.seek(0)
                self._debug['_m_available_compression_algorithms']['start'] = self._io.pos()
                self._m_available_compression_algorithms = self._io.read_u2le()
                self._debug['_m_available_compression_algorithms']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_available_compression_algorithms', None)

            @property
            def lz4_max_distance(self):
                if hasattr(self, '_m_lz4_max_distance'):
                    return self._m_lz4_max_distance

                _pos = self._io.pos()
                self._io.seek(0)
                self._debug['_m_lz4_max_distance']['start'] = self._io.pos()
                self._m_lz4_max_distance = self._io.read_u2le()
                self._debug['_m_lz4_max_distance']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_lz4_max_distance', None)


        @property
        def big_pcluster(self):
            if hasattr(self, '_m_big_pcluster'):
                return self._m_big_pcluster

            self._m_big_pcluster = self.feature_incompat_flags & 2 == 2
            return getattr(self, '_m_big_pcluster', None)

        @property
        def chunked_file(self):
            if hasattr(self, '_m_chunked_file'):
                return self._m_chunked_file

            self._m_chunked_file = self.feature_incompat_flags & 4 == 4
            return getattr(self, '_m_chunked_file', None)

        @property
        def compr_cfgs(self):
            if hasattr(self, '_m_compr_cfgs'):
                return self._m_compr_cfgs

            self._m_compr_cfgs = self.feature_incompat_flags & 2 == 2
            return getattr(self, '_m_compr_cfgs', None)

        @property
        def dedupe(self):
            if hasattr(self, '_m_dedupe'):
                return self._m_dedupe

            self._m_dedupe = self.feature_incompat_flags & 32 == 32
            return getattr(self, '_m_dedupe', None)

        @property
        def device_table(self):
            if hasattr(self, '_m_device_table'):
                return self._m_device_table

            self._m_device_table = self.feature_incompat_flags & 8 == 8
            return getattr(self, '_m_device_table', None)

        @property
        def fragments(self):
            if hasattr(self, '_m_fragments'):
                return self._m_fragments

            self._m_fragments = self.feature_incompat_flags & 32 == 32
            return getattr(self, '_m_fragments', None)

        @property
        def len_file(self):
            if hasattr(self, '_m_len_file'):
                return self._m_len_file

            self._m_len_file = self.num_blocks * self._parent.magic_header.block_size
            return getattr(self, '_m_len_file', None)

        @property
        def lz4_zero_padding(self):
            if hasattr(self, '_m_lz4_zero_padding'):
                return self._m_lz4_zero_padding

            self._m_lz4_zero_padding = self.feature_incompat_flags & 1 == 1
            return getattr(self, '_m_lz4_zero_padding', None)

        @property
        def ztail_packing(self):
            if hasattr(self, '_m_ztail_packing'):
                return self._m_ztail_packing

            self._m_ztail_packing = self.feature_incompat_flags & 16 == 16
            return getattr(self, '_m_ztail_packing', None)


    class Inode(KaitaiStruct):

        class Layouts(IntEnum):
            plain = 0
            compression_legacy = 1
            inline = 2
            compression = 3
            chunk_based = 4
        SEQ_FIELDS = ["format", "inode", "xattrs", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.Inode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['format']['start'] = self._io.pos()
            self.format = self._io.read_u2le()
            self._debug['format']['end'] = self._io.pos()
            self._debug['inode']['start'] = self._io.pos()
            self.inode = Erofs.OndiskInode(self.extended, self._io, self, self._root)
            self._debug['inode']['end'] = self._io.pos()
            if self.inode.num_inline_xattr != 0:
                pass
                self._debug['xattrs']['start'] = self._io.pos()
                self.xattrs = Erofs.Xattrs(self.inode.num_inline_xattr, self._io, self, self._root)
                self._debug['xattrs']['end'] = self._io.pos()

            self._debug['data']['start'] = self._io.pos()
            _on = self.inode_layout
            if _on == Erofs.Inode.Layouts.compression:
                pass
                self.data = Erofs.Inode.Compression(self._io, self, self._root)
            elif _on == Erofs.Inode.Layouts.inline:
                pass
                self.data = Erofs.Inode.Inline(self._io, self, self._root)
            elif _on == Erofs.Inode.Layouts.plain:
                pass
                self.data = Erofs.Inode.Plain(self._io, self, self._root)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.inode._fetch_instances()
            if self.inode.num_inline_xattr != 0:
                pass
                self.xattrs._fetch_instances()

            _on = self.inode_layout
            if _on == Erofs.Inode.Layouts.compression:
                pass
                self.data._fetch_instances()
            elif _on == Erofs.Inode.Layouts.inline:
                pass
                self.data._fetch_instances()
            elif _on == Erofs.Inode.Layouts.plain:
                pass
                self.data._fetch_instances()

        class Compression(KaitaiStruct):
            SEQ_FIELDS = ["map_header"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Erofs.Inode.Compression, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['map_header']['start'] = self._io.pos()
                self.map_header = Erofs.MapHeader(self._io, self, self._root)
                self._debug['map_header']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.map_header._fetch_instances()


        class Inline(KaitaiStruct):
            SEQ_FIELDS = ["dir_entries", "link_data", "last_inline_data"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Erofs.Inode.Inline, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                if self._parent.inode.is_dir:
                    pass
                    self._debug['dir_entries']['start'] = self._io.pos()
                    self._raw_dir_entries = self._io.read_bytes(self._parent.len_inode)
                    _io__raw_dir_entries = KaitaiStream(BytesIO(self._raw_dir_entries))
                    self.dir_entries = Erofs.DirectoryEntries(_io__raw_dir_entries, self, self._root)
                    self._debug['dir_entries']['end'] = self._io.pos()

                if self._parent.inode.is_link:
                    pass
                    self._debug['link_data']['start'] = self._io.pos()
                    self.link_data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self._parent.len_inode), 0, False)).decode(u"UTF-8")
                    self._debug['link_data']['end'] = self._io.pos()

                if self._parent.inode.is_regular:
                    pass
                    self._debug['last_inline_data']['start'] = self._io.pos()
                    self.last_inline_data = self._io.read_bytes(self._parent.len_inode % self._root.superblock.magic_header.block_size)
                    self._debug['last_inline_data']['end'] = self._io.pos()



            def _fetch_instances(self):
                pass
                if self._parent.inode.is_dir:
                    pass
                    self.dir_entries._fetch_instances()

                if self._parent.inode.is_link:
                    pass

                if self._parent.inode.is_regular:
                    pass

                _ = self.node_data
                if hasattr(self, '_m_node_data'):
                    pass


            @property
            def node_data(self):
                if hasattr(self, '_m_node_data'):
                    return self._m_node_data

                if self._parent.inode.is_regular:
                    pass
                    io = self._root._io
                    _pos = io.pos()
                    io.seek(self.raw_block_address * self._root.superblock.magic_header.block_size)
                    self._debug['_m_node_data']['start'] = io.pos()
                    self._m_node_data = io.read_bytes((self._parent.len_inode // self._root.superblock.magic_header.block_size) * self._root.superblock.magic_header.block_size)
                    self._debug['_m_node_data']['end'] = io.pos()
                    io.seek(_pos)

                return getattr(self, '_m_node_data', None)

            @property
            def raw_block_address(self):
                if hasattr(self, '_m_raw_block_address'):
                    return self._m_raw_block_address

                self._m_raw_block_address = (self._parent.inode.body.specific.raw_block_address if self._parent.extended else self._parent.inode.body.specific.raw_block_address)
                return getattr(self, '_m_raw_block_address', None)


        class Plain(KaitaiStruct):
            SEQ_FIELDS = []
            def __init__(self, _io, _parent=None, _root=None):
                super(Erofs.Inode.Plain, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                pass


            def _fetch_instances(self):
                pass
                _ = self.node_data
                if hasattr(self, '_m_node_data'):
                    pass


            @property
            def node_data(self):
                if hasattr(self, '_m_node_data'):
                    return self._m_node_data

                if self._parent.inode.is_regular:
                    pass
                    io = self._root._io
                    _pos = io.pos()
                    io.seek(self.raw_block_address * self._root.superblock.magic_header.block_size)
                    self._debug['_m_node_data']['start'] = io.pos()
                    self._m_node_data = io.read_bytes((self._parent.len_inode // self._root.superblock.magic_header.block_size) * self._root.superblock.magic_header.block_size)
                    self._debug['_m_node_data']['end'] = io.pos()
                    io.seek(_pos)

                return getattr(self, '_m_node_data', None)

            @property
            def raw_block_address(self):
                if hasattr(self, '_m_raw_block_address'):
                    return self._m_raw_block_address

                self._m_raw_block_address = (self._parent.inode.body.specific.raw_block_address if self._parent.extended else self._parent.inode.body.specific.raw_block_address)
                return getattr(self, '_m_raw_block_address', None)


        @property
        def extended(self):
            if hasattr(self, '_m_extended'):
                return self._m_extended

            self._m_extended = self.format & 1 == 1
            return getattr(self, '_m_extended', None)

        @property
        def inode_layout(self):
            if hasattr(self, '_m_inode_layout'):
                return self._m_inode_layout

            self._m_inode_layout = KaitaiStream.resolve_enum(Erofs.Inode.Layouts, self.format >> 1)
            return getattr(self, '_m_inode_layout', None)

        @property
        def len_inode(self):
            if hasattr(self, '_m_len_inode'):
                return self._m_len_inode

            self._m_len_inode = (self.inode.body.len_inode if self.extended else self.inode.body.len_inode)
            return getattr(self, '_m_len_inode', None)


    class Lz4Configs(KaitaiStruct):
        SEQ_FIELDS = ["max_distance", "max_pcluster_blocks", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.Lz4Configs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['max_distance']['start'] = self._io.pos()
            self.max_distance = self._io.read_u2le()
            self._debug['max_distance']['end'] = self._io.pos()
            self._debug['max_pcluster_blocks']['start'] = self._io.pos()
            self.max_pcluster_blocks = self._io.read_u2le()
            self._debug['max_pcluster_blocks']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(10)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class LzmaConfigs(KaitaiStruct):
        SEQ_FIELDS = ["dict_size", "format", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.LzmaConfigs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['dict_size']['start'] = self._io.pos()
            self.dict_size = self._io.read_u4le()
            self._debug['dict_size']['end'] = self._io.pos()
            self._debug['format']['start'] = self._io.pos()
            self.format = self._io.read_u2le()
            self._debug['format']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(8)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class MagicHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "crc32", "feature_compat_flags", "block_size_bits", "ext_slots"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.MagicHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\xE2\xE1\xF5\xE0":
                raise kaitaistruct.ValidationNotEqualError(b"\xE2\xE1\xF5\xE0", self.magic, self._io, u"/types/magic_header/seq/0")
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['feature_compat_flags']['start'] = self._io.pos()
            self.feature_compat_flags = self._io.read_u4le()
            self._debug['feature_compat_flags']['end'] = self._io.pos()
            self._debug['block_size_bits']['start'] = self._io.pos()
            self.block_size_bits = self._io.read_u1()
            self._debug['block_size_bits']['end'] = self._io.pos()
            self._debug['ext_slots']['start'] = self._io.pos()
            self.ext_slots = self._io.read_u1()
            self._debug['ext_slots']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def block_size(self):
            if hasattr(self, '_m_block_size'):
                return self._m_block_size

            self._m_block_size = 1 << self.block_size_bits
            return getattr(self, '_m_block_size', None)

        @property
        def checksum(self):
            if hasattr(self, '_m_checksum'):
                return self._m_checksum

            self._m_checksum = self.feature_compat_flags & 1 == 1
            return getattr(self, '_m_checksum', None)

        @property
        def len_superblock(self):
            if hasattr(self, '_m_len_superblock'):
                return self._m_len_superblock

            self._m_len_superblock = 128 + self.ext_slots * 16
            return getattr(self, '_m_len_superblock', None)

        @property
        def mtime(self):
            if hasattr(self, '_m_mtime'):
                return self._m_mtime

            self._m_mtime = self.feature_compat_flags & 2 == 2
            return getattr(self, '_m_mtime', None)


    class MapHeader(KaitaiStruct):
        SEQ_FIELDS = ["offset_or_encoded_size", "advise", "algorithm_type", "cluster_bits"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.MapHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['offset_or_encoded_size']['start'] = self._io.pos()
            self._raw_offset_or_encoded_size = self._io.read_bytes(4)
            _io__raw_offset_or_encoded_size = KaitaiStream(BytesIO(self._raw_offset_or_encoded_size))
            self.offset_or_encoded_size = Erofs.MapHeader.MapHeaderUnion(_io__raw_offset_or_encoded_size, self, self._root)
            self._debug['offset_or_encoded_size']['end'] = self._io.pos()
            self._debug['advise']['start'] = self._io.pos()
            self.advise = self._io.read_u2le()
            self._debug['advise']['end'] = self._io.pos()
            self._debug['algorithm_type']['start'] = self._io.pos()
            self.algorithm_type = self._io.read_u1()
            self._debug['algorithm_type']['end'] = self._io.pos()
            self._debug['cluster_bits']['start'] = self._io.pos()
            self.cluster_bits = self._io.read_u1()
            self._debug['cluster_bits']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.offset_or_encoded_size._fetch_instances()

        class MapHeaderUnion(KaitaiStruct):
            SEQ_FIELDS = ["raw"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Erofs.MapHeader.MapHeaderUnion, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['raw']['start'] = self._io.pos()
                self.raw = self._io.read_bytes(4)
                self._debug['raw']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _ = self.len_encoded_tailpacking_data
                if hasattr(self, '_m_len_encoded_tailpacking_data'):
                    pass

                _ = self.ofs_fragment
                if hasattr(self, '_m_ofs_fragment'):
                    pass


            @property
            def len_encoded_tailpacking_data(self):
                if hasattr(self, '_m_len_encoded_tailpacking_data'):
                    return self._m_len_encoded_tailpacking_data

                _pos = self._io.pos()
                self._io.seek(2)
                self._debug['_m_len_encoded_tailpacking_data']['start'] = self._io.pos()
                self._m_len_encoded_tailpacking_data = self._io.read_u2le()
                self._debug['_m_len_encoded_tailpacking_data']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_len_encoded_tailpacking_data', None)

            @property
            def ofs_fragment(self):
                if hasattr(self, '_m_ofs_fragment'):
                    return self._m_ofs_fragment

                _pos = self._io.pos()
                self._io.seek(0)
                self._debug['_m_ofs_fragment']['start'] = self._io.pos()
                self._m_ofs_fragment = self._io.read_u4le()
                self._debug['_m_ofs_fragment']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_ofs_fragment', None)


        @property
        def algorithm_type_head_1(self):
            if hasattr(self, '_m_algorithm_type_head_1'):
                return self._m_algorithm_type_head_1

            self._m_algorithm_type_head_1 = KaitaiStream.resolve_enum(Erofs.Compression, self.algorithm_type & 15)
            return getattr(self, '_m_algorithm_type_head_1', None)

        @property
        def algorithm_type_head_2(self):
            if hasattr(self, '_m_algorithm_type_head_2'):
                return self._m_algorithm_type_head_2

            self._m_algorithm_type_head_2 = KaitaiStream.resolve_enum(Erofs.Compression, self.algorithm_type >> 4)
            return getattr(self, '_m_algorithm_type_head_2', None)

        @property
        def big_pcluster_1(self):
            if hasattr(self, '_m_big_pcluster_1'):
                return self._m_big_pcluster_1

            self._m_big_pcluster_1 = self.advise & 2 == 2
            return getattr(self, '_m_big_pcluster_1', None)

        @property
        def big_pcluster_2(self):
            if hasattr(self, '_m_big_pcluster_2'):
                return self._m_big_pcluster_2

            self._m_big_pcluster_2 = self.advise & 4 == 4
            return getattr(self, '_m_big_pcluster_2', None)

        @property
        def compacted_2b(self):
            if hasattr(self, '_m_compacted_2b'):
                return self._m_compacted_2b

            self._m_compacted_2b = self.advise & 1 == 1
            return getattr(self, '_m_compacted_2b', None)

        @property
        def inline_pcluster(self):
            if hasattr(self, '_m_inline_pcluster'):
                return self._m_inline_pcluster

            self._m_inline_pcluster = self.advise & 8 == 8
            return getattr(self, '_m_inline_pcluster', None)

        @property
        def interlaced_fragment_pcluster(self):
            if hasattr(self, '_m_interlaced_fragment_pcluster'):
                return self._m_interlaced_fragment_pcluster

            self._m_interlaced_fragment_pcluster = self.advise & 32 == 32
            return getattr(self, '_m_interlaced_fragment_pcluster', None)

        @property
        def interlaced_pcluster(self):
            if hasattr(self, '_m_interlaced_pcluster'):
                return self._m_interlaced_pcluster

            self._m_interlaced_pcluster = self.advise & 16 == 16
            return getattr(self, '_m_interlaced_pcluster', None)

        @property
        def logical_cluster_bits(self):
            if hasattr(self, '_m_logical_cluster_bits'):
                return self._m_logical_cluster_bits

            self._m_logical_cluster_bits = (self.cluster_bits & 7) + 12
            return getattr(self, '_m_logical_cluster_bits', None)

        @property
        def logical_cluster_size(self):
            if hasattr(self, '_m_logical_cluster_size'):
                return self._m_logical_cluster_size

            self._m_logical_cluster_size = 1 << self.logical_cluster_bits
            return getattr(self, '_m_logical_cluster_size', None)

        @property
        def whole_file_packed(self):
            if hasattr(self, '_m_whole_file_packed'):
                return self._m_whole_file_packed

            self._m_whole_file_packed = self.cluster_bits >> 7
            return getattr(self, '_m_whole_file_packed', None)


    class NodeSpecificUnion(KaitaiStruct):
        SEQ_FIELDS = ["raw"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.NodeSpecificUnion, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['raw']['start'] = self._io.pos()
            self.raw = self._io.read_bytes(4)
            self._debug['raw']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.chunk_info
            if hasattr(self, '_m_chunk_info'):
                pass
                self._m_chunk_info._fetch_instances()

            _ = self.compressed_blocks
            if hasattr(self, '_m_compressed_blocks'):
                pass

            _ = self.raw_block_address
            if hasattr(self, '_m_raw_block_address'):
                pass

            _ = self.rdev
            if hasattr(self, '_m_rdev'):
                pass


        @property
        def chunk_info(self):
            if hasattr(self, '_m_chunk_info'):
                return self._m_chunk_info

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_chunk_info']['start'] = self._io.pos()
            self._m_chunk_info = Erofs.ChunkInfo(self._io, self, self._root)
            self._debug['_m_chunk_info']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_chunk_info', None)

        @property
        def compressed_blocks(self):
            if hasattr(self, '_m_compressed_blocks'):
                return self._m_compressed_blocks

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_compressed_blocks']['start'] = self._io.pos()
            self._m_compressed_blocks = self._io.read_u4le()
            self._debug['_m_compressed_blocks']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_compressed_blocks', None)

        @property
        def raw_block_address(self):
            if hasattr(self, '_m_raw_block_address'):
                return self._m_raw_block_address

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_raw_block_address']['start'] = self._io.pos()
            self._m_raw_block_address = self._io.read_u4le()
            self._debug['_m_raw_block_address']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_raw_block_address', None)

        @property
        def rdev(self):
            if hasattr(self, '_m_rdev'):
                return self._m_rdev

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_rdev']['start'] = self._io.pos()
            self._m_rdev = self._io.read_u4le()
            self._debug['_m_rdev']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_rdev', None)


    class OndiskInode(KaitaiStruct):
        SEQ_FIELDS = ["num_inline_xattr", "mode", "body"]
        def __init__(self, is_extended, _io, _parent=None, _root=None):
            super(Erofs.OndiskInode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.is_extended = is_extended
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_inline_xattr']['start'] = self._io.pos()
            self.num_inline_xattr = self._io.read_u2le()
            self._debug['num_inline_xattr']['end'] = self._io.pos()
            self._debug['mode']['start'] = self._io.pos()
            self.mode = self._io.read_u2le()
            self._debug['mode']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.is_extended
            if _on == False:
                pass
                self.body = Erofs.CompactInode(self._io, self, self._root)
            elif _on == True:
                pass
                self.body = Erofs.ExtendedInode(self._io, self, self._root)
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.is_extended
            if _on == False:
                pass
                self.body._fetch_instances()
            elif _on == True:
                pass
                self.body._fetch_instances()

        @property
        def is_block_device(self):
            if hasattr(self, '_m_is_block_device'):
                return self._m_is_block_device

            self._m_is_block_device = self.mode & 61440 == 24576
            return getattr(self, '_m_is_block_device', None)

        @property
        def is_character_device(self):
            if hasattr(self, '_m_is_character_device'):
                return self._m_is_character_device

            self._m_is_character_device = self.mode & 61440 == 8192
            return getattr(self, '_m_is_character_device', None)

        @property
        def is_dir(self):
            if hasattr(self, '_m_is_dir'):
                return self._m_is_dir

            self._m_is_dir = self.mode & 61440 == 16384
            return getattr(self, '_m_is_dir', None)

        @property
        def is_fifo(self):
            if hasattr(self, '_m_is_fifo'):
                return self._m_is_fifo

            self._m_is_fifo = self.mode & 61440 == 4096
            return getattr(self, '_m_is_fifo', None)

        @property
        def is_link(self):
            if hasattr(self, '_m_is_link'):
                return self._m_is_link

            self._m_is_link = self.mode & 61440 == 40960
            return getattr(self, '_m_is_link', None)

        @property
        def is_regular(self):
            if hasattr(self, '_m_is_regular'):
                return self._m_is_regular

            self._m_is_regular = self.mode & 61440 == 32768
            return getattr(self, '_m_is_regular', None)

        @property
        def is_socket(self):
            if hasattr(self, '_m_is_socket'):
                return self._m_is_socket

            self._m_is_socket = self.mode & 61440 == 49152
            return getattr(self, '_m_is_socket', None)


    class Superblock(KaitaiStruct):
        SEQ_FIELDS = ["magic_header", "header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.Superblock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic_header']['start'] = self._io.pos()
            self.magic_header = Erofs.MagicHeader(self._io, self, self._root)
            self._debug['magic_header']['end'] = self._io.pos()
            self._debug['header']['start'] = self._io.pos()
            self._raw_header = self._io.read_bytes(self.magic_header.len_superblock - 14)
            _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
            self.header = Erofs.Header(_io__raw_header, self, self._root)
            self._debug['header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.magic_header._fetch_instances()
            self.header._fetch_instances()


    class VleDecompressedIndex(KaitaiStruct):
        SEQ_FIELDS = ["advise", "ofs_cluster", "cluster_union"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.VleDecompressedIndex, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['advise']['start'] = self._io.pos()
            self.advise = self._io.read_u2le()
            self._debug['advise']['end'] = self._io.pos()
            self._debug['ofs_cluster']['start'] = self._io.pos()
            self.ofs_cluster = self._io.read_u2le()
            self._debug['ofs_cluster']['end'] = self._io.pos()
            self._debug['cluster_union']['start'] = self._io.pos()
            self._raw_cluster_union = self._io.read_bytes(4)
            _io__raw_cluster_union = KaitaiStream(BytesIO(self._raw_cluster_union))
            self.cluster_union = Erofs.VleDecompressedIndex.ClusterUnion(_io__raw_cluster_union, self, self._root)
            self._debug['cluster_union']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.cluster_union._fetch_instances()

        class ClusterUnion(KaitaiStruct):
            SEQ_FIELDS = ["raw"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Erofs.VleDecompressedIndex.ClusterUnion, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['raw']['start'] = self._io.pos()
                self.raw = self._io.read_bytes(4)
                self._debug['raw']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _ = self.block_address
                if hasattr(self, '_m_block_address'):
                    pass

                _ = self.delta
                if hasattr(self, '_m_delta'):
                    pass
                    self._m_delta._fetch_instances()


            @property
            def block_address(self):
                if hasattr(self, '_m_block_address'):
                    return self._m_block_address

                _pos = self._io.pos()
                self._io.seek(0)
                self._debug['_m_block_address']['start'] = self._io.pos()
                self._m_block_address = self._io.read_u4le()
                self._debug['_m_block_address']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_block_address', None)

            @property
            def delta(self):
                if hasattr(self, '_m_delta'):
                    return self._m_delta

                _pos = self._io.pos()
                self._io.seek(0)
                self._debug['_m_delta']['start'] = self._io.pos()
                self._m_delta = Erofs.VleDecompressedIndex.Delta(self._io, self, self._root)
                self._debug['_m_delta']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_delta', None)


        class Delta(KaitaiStruct):
            SEQ_FIELDS = ["head_cluster", "tail_cluster"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Erofs.VleDecompressedIndex.Delta, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['head_cluster']['start'] = self._io.pos()
                self.head_cluster = self._io.read_u2le()
                self._debug['head_cluster']['end'] = self._io.pos()
                self._debug['tail_cluster']['start'] = self._io.pos()
                self.tail_cluster = self._io.read_u2le()
                self._debug['tail_cluster']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass



    class XattrEntry(KaitaiStruct):
        SEQ_FIELDS = ["len_name", "name_index", "len_value", "name", "value", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.XattrEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_u1()
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['name_index']['start'] = self._io.pos()
            self.name_index = KaitaiStream.resolve_enum(Erofs.XattrNameIndex, self._io.read_u1())
            self._debug['name_index']['end'] = self._io.pos()
            self._debug['len_value']['start'] = self._io.pos()
            self.len_value = self._io.read_u2le()
            self._debug['len_value']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(self.len_name)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_bytes(self.len_value)
            self._debug['value']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self.len_value + self.len_name) % 4)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class XattrIbodyHeader(KaitaiStruct):
        SEQ_FIELDS = ["reserved_1", "num_shared_count", "reserved_2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Erofs.XattrIbodyHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved_1']['start'] = self._io.pos()
            self.reserved_1 = self._io.read_bytes(4)
            self._debug['reserved_1']['end'] = self._io.pos()
            self._debug['num_shared_count']['start'] = self._io.pos()
            self.num_shared_count = self._io.read_u1()
            self._debug['num_shared_count']['end'] = self._io.pos()
            self._debug['reserved_2']['start'] = self._io.pos()
            self.reserved_2 = self._io.read_bytes(7)
            self._debug['reserved_2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Xattrs(KaitaiStruct):
        SEQ_FIELDS = ["header", "shared_xattrs_ids", "inline_xattr"]
        def __init__(self, num_inline_xattr, _io, _parent=None, _root=None):
            super(Erofs.Xattrs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_inline_xattr = num_inline_xattr
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Erofs.XattrIbodyHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['shared_xattrs_ids']['start'] = self._io.pos()
            self._debug['shared_xattrs_ids']['arr'] = []
            self.shared_xattrs_ids = []
            for i in range(self.header.num_shared_count):
                self._debug['shared_xattrs_ids']['arr'].append({'start': self._io.pos()})
                self.shared_xattrs_ids.append(Erofs.Xattrs.SharedXattrId(self._io, self, self._root))
                self._debug['shared_xattrs_ids']['arr'][i]['end'] = self._io.pos()

            self._debug['shared_xattrs_ids']['end'] = self._io.pos()
            self._debug['inline_xattr']['start'] = self._io.pos()
            self._raw_inline_xattr = self._io.read_bytes(((self.num_inline_xattr - 1) - self.header.num_shared_count) * 4)
            _io__raw_inline_xattr = KaitaiStream(BytesIO(self._raw_inline_xattr))
            self.inline_xattr = Erofs.Xattrs.InlineXattrs(_io__raw_inline_xattr, self, self._root)
            self._debug['inline_xattr']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            for i in range(len(self.shared_xattrs_ids)):
                pass
                self.shared_xattrs_ids[i]._fetch_instances()

            self.inline_xattr._fetch_instances()

        class InlineXattrs(KaitaiStruct):
            SEQ_FIELDS = ["entry"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Erofs.Xattrs.InlineXattrs, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['entry']['start'] = self._io.pos()
                self._debug['entry']['arr'] = []
                self.entry = []
                i = 0
                while not self._io.is_eof():
                    self._debug['entry']['arr'].append({'start': self._io.pos()})
                    self.entry.append(Erofs.XattrEntry(self._io, self, self._root))
                    self._debug['entry']['arr'][len(self.entry) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['entry']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.entry)):
                    pass
                    self.entry[i]._fetch_instances()



        class SharedXattrId(KaitaiStruct):
            SEQ_FIELDS = ["xattr_id"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Erofs.Xattrs.SharedXattrId, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['xattr_id']['start'] = self._io.pos()
                self.xattr_id = self._io.read_u4le()
                self._debug['xattr_id']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _ = self.xattr
                if hasattr(self, '_m_xattr'):
                    pass
                    self._m_xattr._fetch_instances()


            @property
            def xattr(self):
                if hasattr(self, '_m_xattr'):
                    return self._m_xattr

                io = self._root._io
                _pos = io.pos()
                io.seek(self._root.ofs_shared_xattr_area + 4 * self.xattr_id)
                self._debug['_m_xattr']['start'] = io.pos()
                self._m_xattr = Erofs.XattrEntry(io, self, self._root)
                self._debug['_m_xattr']['end'] = io.pos()
                io.seek(_pos)
                return getattr(self, '_m_xattr', None)



    @property
    def blocks(self):
        if hasattr(self, '_m_blocks'):
            return self._m_blocks

        _pos = self._io.pos()
        self._io.seek(0)
        self._debug['_m_blocks']['start'] = self._io.pos()
        self._debug['_m_blocks']['arr'] = []
        self._m_blocks = []
        for i in range(self.superblock.header.num_blocks):
            self._debug['_m_blocks']['arr'].append({'start': self._io.pos()})
            self._m_blocks.append(self._io.read_bytes(self.superblock.magic_header.block_size))
            self._debug['_m_blocks']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_blocks']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_blocks', None)

    @property
    def ofs_metadata_area(self):
        if hasattr(self, '_m_ofs_metadata_area'):
            return self._m_ofs_metadata_area

        self._m_ofs_metadata_area = self.superblock.header.meta_block_address * self.superblock.magic_header.block_size
        return getattr(self, '_m_ofs_metadata_area', None)

    @property
    def ofs_shared_xattr_area(self):
        if hasattr(self, '_m_ofs_shared_xattr_area'):
            return self._m_ofs_shared_xattr_area

        self._m_ofs_shared_xattr_area = self.superblock.header.xattr_block_address * self.superblock.magic_header.block_size
        return getattr(self, '_m_ofs_shared_xattr_area', None)

    @property
    def root_inode(self):
        if hasattr(self, '_m_root_inode'):
            return self._m_root_inode

        _pos = self._io.pos()
        self._io.seek(self.ofs_metadata_area + 32 * self.superblock.header.root_nid)
        self._debug['_m_root_inode']['start'] = self._io.pos()
        self._m_root_inode = Erofs.Inode(self._io, self, self._root)
        self._debug['_m_root_inode']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_root_inode', None)


