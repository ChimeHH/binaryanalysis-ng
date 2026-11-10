# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ubifs(KaitaiStruct):
    """UBIFS is a file system for raw flash memory devices. It works on top of
    UBI (Unsorted Block Images), which works as an abstraction layer so UBIFS
    does not need to care about low level details. This specification only covers
    UBIFS, not UBI.
    
    A UBIFS image is divided into several Logical Erase Blocks (LEB). The first
    LEB (LEB0) contains the superblock node, which includes information about LEB
    size, amongst others. The next two LEBs (LEB1 and LEB2) comprise the so called
    "master area" and both contain a copy of the master node, which includes
    information about where to find the root index node, which is then used to
    access all the files on the file system.
    
    **Limitations of this Kaitai Struct implementation:**
    
    1. It only supports UBIFS images created by `mkfs.ubifs` (such as those in
       firmware images built by OpenWrt), not file systems modified after
       creation, e.g. by writing files to them on a running Linux system. The
       Linux kernel appends a new copy of the master node to LEB1 and LEB2
       whenever it mounts the file system read-write, unmounts it, or commits
       changes (updates the index on flash to include them). When mounting, Linux
       uses the
       [last copy](https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/master.c#L84-L165),
       whereas this implementation reads the first one (`master_1`), which still
       describes the file system as it was created. Changes made since then are
       therefore not visible via `index_root`.
    2. Changes that have not been committed yet are not in the index at all, so
       they are not visible via `index_root` either. Until they are committed,
       UBIFS keeps them only in the journal. This only matters for file systems
       that were not unmounted cleanly, because unmounting
       [commits](https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/super.c#L486-L493)
       all changes.
    3. Parsing doesn't advance the stream position. This implementation reads
       the image only through instances, so that parsing doesn't copy the
       whole image into memory. To find where the image ends, e.g. when
       carving it out of a larger file, use `len_image`. For the same reason,
       parsing doesn't fail if the image is truncated. To detect that, check
       that the stream is at least `len_image` bytes long
       (`_io.size >= len_image`).
    
    .. seealso::
       Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h
    
    
    .. seealso::
       Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/key.h
    
    
    .. seealso::
       Source - http://www.linux-mtd.infradead.org/doc/ubifs.pdf
    """

    class Compression(IntEnum):
        no_compression = 0
        lzo = 1
        zlib = 2
        zstd = 3

    class HashAlgos(IntEnum):
        md4 = 0
        md5 = 1
        sha1 = 2
        ripe_md_160 = 3
        sha256 = 4
        sha384 = 5
        sha512 = 6
        sha224 = 7
        ripe_md_128 = 8
        ripe_md_256 = 9
        ripe_md_320 = 10
        wp_256 = 11
        wp_384 = 12
        wp_512 = 13
        tgr_128 = 14
        tgr_160 = 15
        tgr_192 = 16
        sm3_256 = 17
        streebog_256 = 18
        streebog_512 = 19
        sha3_256 = 20
        sha3_384 = 21
        sha3_512 = 22

    class Hashes(IntEnum):
        r5 = 0
        test_hash = 1

    class InodeTypes(IntEnum):
        regular = 0
        directory = 1
        link = 2
        block_device = 3
        character_device = 4
        fifo = 5
        socket = 6

    class KeyFormats(IntEnum):
        simple = 0

    class KeyTypes(IntEnum):
        inode = 0
        data = 1
        directory = 2
        extended_attribute = 3

    class NodeGroupTypes(IntEnum):
        no_node_group = 0
        in_node_group = 1
        last_of_node_group = 2

    class NodeTypes(IntEnum):
        inode = 0
        data = 1
        directory = 2
        extended_attribute = 3
        truncation = 4
        padding = 5
        superblock = 6
        master = 7
        reference = 8
        index = 9
        commit_start = 10
        orphan = 11
        authentication = 12
        signature = 13
    SEQ_FIELDS = []
    def __init__(self, _io, _parent=None, _root=None):
        super(Ubifs, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        pass


    def _fetch_instances(self):
        pass
        _ = self.index
        if hasattr(self, '_m_index'):
            pass
            self._m_index._fetch_instances()

        _ = self.index_root
        if hasattr(self, '_m_index_root'):
            pass
            self._m_index_root._fetch_instances()

        _ = self.lebs
        if hasattr(self, '_m_lebs'):
            pass
            for i in range(len(self._m_lebs)):
                pass


        _ = self.master_1
        if hasattr(self, '_m_master_1'):
            pass
            self._m_master_1._fetch_instances()

        _ = self.master_2
        if hasattr(self, '_m_master_2'):
            pass
            self._m_master_2._fetch_instances()

        _ = self.superblock
        if hasattr(self, '_m_superblock'):
            pass
            self._m_superblock._fetch_instances()


    class AuthenticationHeader(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L774-L782
        """
        SEQ_FIELDS = ["hmac"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.AuthenticationHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['hmac']['start'] = self._io.pos()
            self.hmac = self._io.read_bytes(self._root.superblock.node_header.len_hash)
            self._debug['hmac']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["header", "node_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Ubifs.CommonHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['node_header']['start'] = self._io.pos()
            _on = self.header.node_type
            if _on == Ubifs.NodeTypes.authentication:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.AuthenticationHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.commit_start:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.CommitStartHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.data:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.DataHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.directory:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.DirectoryHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.extended_attribute:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.DirectoryHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.index:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.IndexHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.inode:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.InodeHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.master:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.MasterHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.orphan:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.OrphanHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.padding:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.PaddingHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.reference:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.ReferenceHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.signature:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.SignatureHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.superblock:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.SuperblockHeader(_io__raw_node_header, self, self._root)
            elif _on == Ubifs.NodeTypes.truncation:
                pass
                self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
                _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
                self.node_header = Ubifs.TruncationHeader(_io__raw_node_header, self, self._root)
            else:
                pass
                self.node_header = self._io.read_bytes(self.header.len_full_node - 24)
            self._debug['node_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            _on = self.header.node_type
            if _on == Ubifs.NodeTypes.authentication:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.commit_start:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.data:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.directory:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.extended_attribute:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.index:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.inode:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.master:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.orphan:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.padding:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.reference:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.signature:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.superblock:
                pass
                self.node_header._fetch_instances()
            elif _on == Ubifs.NodeTypes.truncation:
                pass
                self.node_header._fetch_instances()
            else:
                pass


    class Branch(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L801-L817
        """
        SEQ_FIELDS = ["target_leb", "ofs_target", "len_target", "key", "hash"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.Branch, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['target_leb']['start'] = self._io.pos()
            self.target_leb = self._io.read_u4le()
            self._debug['target_leb']['end'] = self._io.pos()
            self._debug['ofs_target']['start'] = self._io.pos()
            self.ofs_target = self._io.read_u4le()
            self._debug['ofs_target']['end'] = self._io.pos()
            self._debug['len_target']['start'] = self._io.pos()
            self.len_target = self._io.read_u4le()
            self._debug['len_target']['end'] = self._io.pos()
            self._debug['key']['start'] = self._io.pos()
            self._raw_key = self._io.read_bytes(8)
            _io__raw_key = KaitaiStream(BytesIO(self._raw_key))
            self.key = Ubifs.Key(_io__raw_key, self, self._root)
            self._debug['key']['end'] = self._io.pos()
            self._debug['hash']['start'] = self._io.pos()
            self.hash = self._io.read_bytes(self._root.superblock.node_header.len_hash)
            self._debug['hash']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.key._fetch_instances()
            _ = self.target
            if hasattr(self, '_m_target'):
                pass
                self._m_target._fetch_instances()


        @property
        def target(self):
            if hasattr(self, '_m_target'):
                return self._m_target

            io = self._root._io
            _pos = io.pos()
            io.seek(self._root.superblock.node_header.leb_size * self.target_leb + self.ofs_target)
            self._debug['_m_target']['start'] = io.pos()
            self._raw__m_target = io.read_bytes(self.len_target)
            _io__raw__m_target = KaitaiStream(BytesIO(self._raw__m_target))
            self._m_target = Ubifs.Block(_io__raw__m_target, self, self._root)
            self._debug['_m_target']['end'] = io.pos()
            _ = self._m_target
            if not  ((_.header.len_full_node == self.len_target) and ((_.header.node_type == Ubifs.NodeTypes.index if self._parent.level != 0 else int(_.header.node_type) == int(self.key.type)))) :
                raise kaitaistruct.ValidationExprError(self._m_target, self._io, u"/types/branch/instances/target")
            io.seek(_pos)
            return getattr(self, '_m_target', None)


    class CommitStartHeader(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L833-L841
        """
        SEQ_FIELDS = ["commit_number"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.CommitStartHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['commit_number']['start'] = self._io.pos()
            self.commit_number = self._io.read_u8le()
            self._debug['commit_number']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class CommonHeader(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L443-L464
        """
        SEQ_FIELDS = ["magic", "crc", "sequence_number", "len_full_node", "node_type", "group_type", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.CommonHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_u4le()
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == 101718065:
                raise kaitaistruct.ValidationNotEqualError(101718065, self.magic, self._io, u"/types/common_header/seq/0")
            self._debug['crc']['start'] = self._io.pos()
            self.crc = self._io.read_u4le()
            self._debug['crc']['end'] = self._io.pos()
            self._debug['sequence_number']['start'] = self._io.pos()
            self.sequence_number = self._io.read_u8le()
            self._debug['sequence_number']['end'] = self._io.pos()
            self._debug['len_full_node']['start'] = self._io.pos()
            self.len_full_node = self._io.read_u4le()
            self._debug['len_full_node']['end'] = self._io.pos()
            self._debug['node_type']['start'] = self._io.pos()
            self.node_type = KaitaiStream.resolve_enum(Ubifs.NodeTypes, self._io.read_u1())
            self._debug['node_type']['end'] = self._io.pos()
            self._debug['group_type']['start'] = self._io.pos()
            self.group_type = KaitaiStream.resolve_enum(Ubifs.NodeGroupTypes, self._io.read_u1())
            self._debug['group_type']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(2)
            self._debug['padding']['end'] = self._io.pos()
            if not self.padding == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.padding, self._io, u"/types/common_header/seq/6")


        def _fetch_instances(self):
            pass


    class DataHeader(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L567-L584
        """
        SEQ_FIELDS = ["key", "len_uncompressed", "compression", "len_compressed_data", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.DataHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['key']['start'] = self._io.pos()
            self._raw_key = self._io.read_bytes(16)
            _io__raw_key = KaitaiStream(BytesIO(self._raw_key))
            self.key = Ubifs.Key(_io__raw_key, self, self._root)
            self._debug['key']['end'] = self._io.pos()
            self._debug['len_uncompressed']['start'] = self._io.pos()
            self.len_uncompressed = self._io.read_u4le()
            self._debug['len_uncompressed']['end'] = self._io.pos()
            if not self.len_uncompressed >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.len_uncompressed, self._io, u"/types/data_header/seq/1")
            if not self.len_uncompressed <= 4096:
                raise kaitaistruct.ValidationGreaterThanError(4096, self.len_uncompressed, self._io, u"/types/data_header/seq/1")
            self._debug['compression']['start'] = self._io.pos()
            self.compression = KaitaiStream.resolve_enum(Ubifs.Compression, self._io.read_u2le())
            self._debug['compression']['end'] = self._io.pos()
            if not isinstance(self.compression, Ubifs.Compression):
                raise kaitaistruct.ValidationNotInEnumError(self.compression, self._io, u"/types/data_header/seq/2")
            self._debug['len_compressed_data']['start'] = self._io.pos()
            self.len_compressed_data = self._io.read_u2le()
            self._debug['len_compressed_data']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes_full()
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.key._fetch_instances()


    class DirectoryHeader(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L541-L565
        """
        SEQ_FIELDS = ["key", "inode_number", "padding1", "inode_type", "len_name", "cookie", "name", "name_terminator"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.DirectoryHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['key']['start'] = self._io.pos()
            self._raw_key = self._io.read_bytes(16)
            _io__raw_key = KaitaiStream(BytesIO(self._raw_key))
            self.key = Ubifs.Key(_io__raw_key, self, self._root)
            self._debug['key']['end'] = self._io.pos()
            _ = self.key
            if not  ((_.type == Ubifs.KeyTypes.directory) or (_.type == Ubifs.KeyTypes.extended_attribute)) :
                raise kaitaistruct.ValidationExprError(self.key, self._io, u"/types/directory_header/seq/0")
            self._debug['inode_number']['start'] = self._io.pos()
            self.inode_number = self._io.read_u8le()
            self._debug['inode_number']['end'] = self._io.pos()
            if not self.inode_number <= 4294967295:
                raise kaitaistruct.ValidationGreaterThanError(4294967295, self.inode_number, self._io, u"/types/directory_header/seq/1")
            self._debug['padding1']['start'] = self._io.pos()
            self.padding1 = self._io.read_bytes(1)
            self._debug['padding1']['end'] = self._io.pos()
            if not self.padding1 == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.padding1, self._io, u"/types/directory_header/seq/2")
            self._debug['inode_type']['start'] = self._io.pos()
            self.inode_type = KaitaiStream.resolve_enum(Ubifs.InodeTypes, self._io.read_u1())
            self._debug['inode_type']['end'] = self._io.pos()
            if not isinstance(self.inode_type, Ubifs.InodeTypes):
                raise kaitaistruct.ValidationNotInEnumError(self.inode_type, self._io, u"/types/directory_header/seq/3")
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_u2le()
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['cookie']['start'] = self._io.pos()
            self.cookie = self._io.read_u4le()
            self._debug['cookie']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = self._io.read_bytes(self.len_name)
            self._debug['name']['end'] = self._io.pos()
            self._debug['name_terminator']['start'] = self._io.pos()
            self.name_terminator = self._io.read_bytes(1)
            self._debug['name_terminator']['end'] = self._io.pos()
            if not self.name_terminator == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.name_terminator, self._io, u"/types/directory_header/seq/7")


        def _fetch_instances(self):
            pass
            self.key._fetch_instances()


    class Dummy(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.Dummy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class IndexBlock(KaitaiStruct):
        SEQ_FIELDS = ["header", "node_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.IndexBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Ubifs.CommonHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            _ = self.header
            if not _.node_type == Ubifs.NodeTypes.index:
                raise kaitaistruct.ValidationExprError(self.header, self._io, u"/types/index_block/seq/0")
            self._debug['node_header']['start'] = self._io.pos()
            self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
            _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
            self.node_header = Ubifs.IndexHeader(_io__raw_node_header, self, self._root)
            self._debug['node_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.node_header._fetch_instances()


    class IndexHeader(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L819-L831
        """
        SEQ_FIELDS = ["num_branches", "level", "branches"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.IndexHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_branches']['start'] = self._io.pos()
            self.num_branches = self._io.read_u2le()
            self._debug['num_branches']['end'] = self._io.pos()
            self._debug['level']['start'] = self._io.pos()
            self.level = self._io.read_u2le()
            self._debug['level']['end'] = self._io.pos()
            self._debug['branches']['start'] = self._io.pos()
            self._debug['branches']['arr'] = []
            self.branches = []
            for i in range(self.num_branches):
                self._debug['branches']['arr'].append({'start': self._io.pos()})
                self.branches.append(Ubifs.Branch(self._io, self, self._root))
                self._debug['branches']['arr'][i]['end'] = self._io.pos()

            self._debug['branches']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.branches)):
                pass
                self.branches[i]._fetch_instances()



    class InodeHeader(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L480-L539
        """
        SEQ_FIELDS = ["key", "creation_sequence_number", "len_uncompressed", "atime_sec", "ctime_sec", "mtime_sec", "atime_nsec", "ctime_nsec", "mtime_nsec", "num_links", "uid", "gid", "mode", "flags", "len_data", "num_xattrs", "xattr_size", "padding1", "xattr_names", "compression", "padding2", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.InodeHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['key']['start'] = self._io.pos()
            self._raw_key = self._io.read_bytes(16)
            _io__raw_key = KaitaiStream(BytesIO(self._raw_key))
            self.key = Ubifs.Key(_io__raw_key, self, self._root)
            self._debug['key']['end'] = self._io.pos()
            self._debug['creation_sequence_number']['start'] = self._io.pos()
            self.creation_sequence_number = self._io.read_u8le()
            self._debug['creation_sequence_number']['end'] = self._io.pos()
            self._debug['len_uncompressed']['start'] = self._io.pos()
            self.len_uncompressed = self._io.read_u8le()
            self._debug['len_uncompressed']['end'] = self._io.pos()
            self._debug['atime_sec']['start'] = self._io.pos()
            self.atime_sec = self._io.read_u8le()
            self._debug['atime_sec']['end'] = self._io.pos()
            self._debug['ctime_sec']['start'] = self._io.pos()
            self.ctime_sec = self._io.read_u8le()
            self._debug['ctime_sec']['end'] = self._io.pos()
            self._debug['mtime_sec']['start'] = self._io.pos()
            self.mtime_sec = self._io.read_u8le()
            self._debug['mtime_sec']['end'] = self._io.pos()
            self._debug['atime_nsec']['start'] = self._io.pos()
            self.atime_nsec = self._io.read_u4le()
            self._debug['atime_nsec']['end'] = self._io.pos()
            self._debug['ctime_nsec']['start'] = self._io.pos()
            self.ctime_nsec = self._io.read_u4le()
            self._debug['ctime_nsec']['end'] = self._io.pos()
            self._debug['mtime_nsec']['start'] = self._io.pos()
            self.mtime_nsec = self._io.read_u4le()
            self._debug['mtime_nsec']['end'] = self._io.pos()
            self._debug['num_links']['start'] = self._io.pos()
            self.num_links = self._io.read_u4le()
            self._debug['num_links']['end'] = self._io.pos()
            self._debug['uid']['start'] = self._io.pos()
            self.uid = self._io.read_u4le()
            self._debug['uid']['end'] = self._io.pos()
            self._debug['gid']['start'] = self._io.pos()
            self.gid = self._io.read_u4le()
            self._debug['gid']['end'] = self._io.pos()
            self._debug['mode']['start'] = self._io.pos()
            self.mode = self._io.read_u4le()
            self._debug['mode']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['num_xattrs']['start'] = self._io.pos()
            self.num_xattrs = self._io.read_u4le()
            self._debug['num_xattrs']['end'] = self._io.pos()
            self._debug['xattr_size']['start'] = self._io.pos()
            self.xattr_size = self._io.read_u4le()
            self._debug['xattr_size']['end'] = self._io.pos()
            self._debug['padding1']['start'] = self._io.pos()
            self.padding1 = self._io.read_bytes(4)
            self._debug['padding1']['end'] = self._io.pos()
            if not self.padding1 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.padding1, self._io, u"/types/inode_header/seq/17")
            self._debug['xattr_names']['start'] = self._io.pos()
            self.xattr_names = self._io.read_u4le()
            self._debug['xattr_names']['end'] = self._io.pos()
            self._debug['compression']['start'] = self._io.pos()
            self.compression = KaitaiStream.resolve_enum(Ubifs.Compression, self._io.read_u2le())
            self._debug['compression']['end'] = self._io.pos()
            if not isinstance(self.compression, Ubifs.Compression):
                raise kaitaistruct.ValidationNotInEnumError(self.compression, self._io, u"/types/inode_header/seq/19")
            self._debug['padding2']['start'] = self._io.pos()
            self.padding2 = self._io.read_bytes(26)
            self._debug['padding2']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.key._fetch_instances()

        @property
        def append(self):
            """writes to the inode may only append data."""
            if hasattr(self, '_m_append'):
                return self._m_append

            self._m_append = self.flags & 8 != 0
            return getattr(self, '_m_append', None)

        @property
        def compressed(self):
            """use compression for this inode."""
            if hasattr(self, '_m_compressed'):
                return self._m_compressed

            self._m_compressed = self.flags & 1 != 0
            return getattr(self, '_m_compressed', None)

        @property
        def dirsync(self):
            """I/O on this directory inode has to be synchronous."""
            if hasattr(self, '_m_dirsync'):
                return self._m_dirsync

            self._m_dirsync = self.flags & 16 != 0
            return getattr(self, '_m_dirsync', None)

        @property
        def encrypted(self):
            """use encryption for this inode."""
            if hasattr(self, '_m_encrypted'):
                return self._m_encrypted

            self._m_encrypted = self.flags & 64 != 0
            return getattr(self, '_m_encrypted', None)

        @property
        def immutable(self):
            """inode is immutable."""
            if hasattr(self, '_m_immutable'):
                return self._m_immutable

            self._m_immutable = self.flags & 4 != 0
            return getattr(self, '_m_immutable', None)

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

        @property
        def synchronous(self):
            """I/O on this inode has to be synchronous."""
            if hasattr(self, '_m_synchronous'):
                return self._m_synchronous

            self._m_synchronous = self.flags & 2 != 0
            return getattr(self, '_m_synchronous', None)

        @property
        def xattr(self):
            """this inode is the inode for an extended attribute value."""
            if hasattr(self, '_m_xattr'):
                return self._m_xattr

            self._m_xattr = self.flags & 32 != 0
            return getattr(self, '_m_xattr', None)


    class Key(KaitaiStruct):
        """Inode nodes (`inode_header`), directory and extended attribute entry
        nodes (`directory_header`) and data nodes (`data_header`) store keys in a
        16-byte field (`UBIFS_MAX_KEY_LEN`). The simple key format, the only one
        there is (see `<superblock_header>.key_fmt`), uses only the first 8
        bytes, and Linux (v7.2)
        [zeroes](https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/key.h#L432-L440)
        the rest. Branches of index nodes (`branch`)
        [store only these 8 bytes](https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/key.h#L448-L455).
        
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/key.h#L16-L22
        """
        SEQ_FIELDS = ["inode_number", "value", "type", "unused"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.Key, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['inode_number']['start'] = self._io.pos()
            self.inode_number = self._io.read_u4le()
            self._debug['inode_number']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_bits_int_le(29)
            self._debug['value']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Ubifs.KeyTypes, self._io.read_bits_int_le(3))
            self._debug['type']['end'] = self._io.pos()
            if not isinstance(self.type, Ubifs.KeyTypes):
                raise kaitaistruct.ValidationNotInEnumError(self.type, self._io, u"/types/key/seq/2")
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_bytes_full()
            self._debug['unused']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class MasterHeader(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L685-L756
        """
        SEQ_FIELDS = ["highest_inum", "commit_number", "flags", "leb_log", "leb_root", "ofs_root", "len_root", "leb_garbage_collect", "leb_index_head", "ofs_index_head", "len_index", "total_free", "total_dirty", "total_used", "total_dead", "total_dark", "leb_lpt", "ofs_lpt", "leb_nhead", "ofs_nhead", "leb_lprops_table", "ofs_lprops_table", "leb_save_table", "ofs_save_table", "leb_last_lpt_scan", "num_empty_lebs", "num_index_lebs", "num_lebs", "hash_root_index", "hash_lpt", "hmac", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.MasterHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['highest_inum']['start'] = self._io.pos()
            self.highest_inum = self._io.read_u8le()
            self._debug['highest_inum']['end'] = self._io.pos()
            self._debug['commit_number']['start'] = self._io.pos()
            self.commit_number = self._io.read_u8le()
            self._debug['commit_number']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['leb_log']['start'] = self._io.pos()
            self.leb_log = self._io.read_u4le()
            self._debug['leb_log']['end'] = self._io.pos()
            self._debug['leb_root']['start'] = self._io.pos()
            self.leb_root = self._io.read_u4le()
            self._debug['leb_root']['end'] = self._io.pos()
            self._debug['ofs_root']['start'] = self._io.pos()
            self.ofs_root = self._io.read_u4le()
            self._debug['ofs_root']['end'] = self._io.pos()
            self._debug['len_root']['start'] = self._io.pos()
            self.len_root = self._io.read_u4le()
            self._debug['len_root']['end'] = self._io.pos()
            self._debug['leb_garbage_collect']['start'] = self._io.pos()
            self.leb_garbage_collect = self._io.read_u4le()
            self._debug['leb_garbage_collect']['end'] = self._io.pos()
            self._debug['leb_index_head']['start'] = self._io.pos()
            self.leb_index_head = self._io.read_u4le()
            self._debug['leb_index_head']['end'] = self._io.pos()
            self._debug['ofs_index_head']['start'] = self._io.pos()
            self.ofs_index_head = self._io.read_u4le()
            self._debug['ofs_index_head']['end'] = self._io.pos()
            self._debug['len_index']['start'] = self._io.pos()
            self.len_index = self._io.read_u8le()
            self._debug['len_index']['end'] = self._io.pos()
            self._debug['total_free']['start'] = self._io.pos()
            self.total_free = self._io.read_u8le()
            self._debug['total_free']['end'] = self._io.pos()
            self._debug['total_dirty']['start'] = self._io.pos()
            self.total_dirty = self._io.read_u8le()
            self._debug['total_dirty']['end'] = self._io.pos()
            self._debug['total_used']['start'] = self._io.pos()
            self.total_used = self._io.read_u8le()
            self._debug['total_used']['end'] = self._io.pos()
            self._debug['total_dead']['start'] = self._io.pos()
            self.total_dead = self._io.read_u8le()
            self._debug['total_dead']['end'] = self._io.pos()
            self._debug['total_dark']['start'] = self._io.pos()
            self.total_dark = self._io.read_u8le()
            self._debug['total_dark']['end'] = self._io.pos()
            self._debug['leb_lpt']['start'] = self._io.pos()
            self.leb_lpt = self._io.read_u4le()
            self._debug['leb_lpt']['end'] = self._io.pos()
            self._debug['ofs_lpt']['start'] = self._io.pos()
            self.ofs_lpt = self._io.read_u4le()
            self._debug['ofs_lpt']['end'] = self._io.pos()
            self._debug['leb_nhead']['start'] = self._io.pos()
            self.leb_nhead = self._io.read_u4le()
            self._debug['leb_nhead']['end'] = self._io.pos()
            self._debug['ofs_nhead']['start'] = self._io.pos()
            self.ofs_nhead = self._io.read_u4le()
            self._debug['ofs_nhead']['end'] = self._io.pos()
            self._debug['leb_lprops_table']['start'] = self._io.pos()
            self.leb_lprops_table = self._io.read_u4le()
            self._debug['leb_lprops_table']['end'] = self._io.pos()
            self._debug['ofs_lprops_table']['start'] = self._io.pos()
            self.ofs_lprops_table = self._io.read_u4le()
            self._debug['ofs_lprops_table']['end'] = self._io.pos()
            self._debug['leb_save_table']['start'] = self._io.pos()
            self.leb_save_table = self._io.read_u4le()
            self._debug['leb_save_table']['end'] = self._io.pos()
            self._debug['ofs_save_table']['start'] = self._io.pos()
            self.ofs_save_table = self._io.read_u4le()
            self._debug['ofs_save_table']['end'] = self._io.pos()
            self._debug['leb_last_lpt_scan']['start'] = self._io.pos()
            self.leb_last_lpt_scan = self._io.read_u4le()
            self._debug['leb_last_lpt_scan']['end'] = self._io.pos()
            self._debug['num_empty_lebs']['start'] = self._io.pos()
            self.num_empty_lebs = self._io.read_u4le()
            self._debug['num_empty_lebs']['end'] = self._io.pos()
            self._debug['num_index_lebs']['start'] = self._io.pos()
            self.num_index_lebs = self._io.read_u4le()
            self._debug['num_index_lebs']['end'] = self._io.pos()
            self._debug['num_lebs']['start'] = self._io.pos()
            self.num_lebs = self._io.read_u4le()
            self._debug['num_lebs']['end'] = self._io.pos()
            self._debug['hash_root_index']['start'] = self._io.pos()
            self.hash_root_index = self._io.read_bytes(64)
            self._debug['hash_root_index']['end'] = self._io.pos()
            self._debug['hash_lpt']['start'] = self._io.pos()
            self.hash_lpt = self._io.read_bytes(64)
            self._debug['hash_lpt']['end'] = self._io.pos()
            self._debug['hmac']['start'] = self._io.pos()
            self.hmac = self._io.read_bytes(64)
            self._debug['hmac']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(152)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def dirty(self):
            """master node is dirty."""
            if hasattr(self, '_m_dirty'):
                return self._m_dirty

            self._m_dirty = self.flags & 1 != 0
            return getattr(self, '_m_dirty', None)

        @property
        def no_orphans(self):
            """no orphan inodes present."""
            if hasattr(self, '_m_no_orphans'):
                return self._m_no_orphans

            self._m_no_orphans = self.flags & 2 != 0
            return getattr(self, '_m_no_orphans', None)

        @property
        def recovery(self):
            """written by recovery."""
            if hasattr(self, '_m_recovery'):
                return self._m_recovery

            self._m_recovery = self.flags & 4 != 0
            return getattr(self, '_m_recovery', None)


    class MasterblockNode(KaitaiStruct):
        SEQ_FIELDS = ["header", "node_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.MasterblockNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Ubifs.CommonHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            _ = self.header
            if not _.node_type == Ubifs.NodeTypes.master:
                raise kaitaistruct.ValidationExprError(self.header, self._io, u"/types/masterblock_node/seq/0")
            self._debug['node_header']['start'] = self._io.pos()
            self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
            _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
            self.node_header = Ubifs.MasterHeader(_io__raw_node_header, self, self._root)
            self._debug['node_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.node_header._fetch_instances()


    class OrphanHeader(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L843-L853
        """
        SEQ_FIELDS = ["commit_number", "inode_numbers"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.OrphanHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['commit_number']['start'] = self._io.pos()
            self.commit_number = self._io.read_u8le()
            self._debug['commit_number']['end'] = self._io.pos()
            self._debug['inode_numbers']['start'] = self._io.pos()
            self._debug['inode_numbers']['arr'] = []
            self.inode_numbers = []
            i = 0
            while not self._io.is_eof():
                self._debug['inode_numbers']['arr'].append({'start': self._io.pos()})
                self.inode_numbers.append(self._io.read_u8le())
                self._debug['inode_numbers']['arr'][len(self.inode_numbers) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['inode_numbers']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.inode_numbers)):
                pass



    class PaddingHeader(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L606-L615
        """
        SEQ_FIELDS = ["len_padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.PaddingHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_padding']['start'] = self._io.pos()
            self.len_padding = self._io.read_u4le()
            self._debug['len_padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class ReferenceHeader(KaitaiStruct):
        """logical eraseblock reference node.
        
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L758-L772
        """
        SEQ_FIELDS = ["leb_number", "ofs_leb", "journal_head_number", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.ReferenceHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['leb_number']['start'] = self._io.pos()
            self.leb_number = self._io.read_u4le()
            self._debug['leb_number']['end'] = self._io.pos()
            self._debug['ofs_leb']['start'] = self._io.pos()
            self.ofs_leb = self._io.read_u4le()
            self._debug['ofs_leb']['end'] = self._io.pos()
            self._debug['journal_head_number']['start'] = self._io.pos()
            self.journal_head_number = self._io.read_u4le()
            self._debug['journal_head_number']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(28)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class SignatureHeader(KaitaiStruct):
        """Signature of the superblock node of a file system signed when it was
        created (`mkfs.ubifs` with a key). Linux
        [expects it](https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/auth.c#L198-L216)
        as the first node after the superblock node in LEB0.
        
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L784-L799
        """
        SEQ_FIELDS = ["type", "len_signature", "padding", "signature"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.SignatureHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u4le()
            self._debug['type']['end'] = self._io.pos()
            if not self.type == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.type, self._io, u"/types/signature_header/seq/0")
            self._debug['len_signature']['start'] = self._io.pos()
            self.len_signature = self._io.read_u4le()
            self._debug['len_signature']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(32)
            self._debug['padding']['end'] = self._io.pos()
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(self.len_signature)
            self._debug['signature']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class SuperblockHeader(KaitaiStruct):
        """
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L617-L683
        """
        SEQ_FIELDS = ["padding0", "key_hash", "key_fmt", "flags", "min_io_size", "leb_size", "num_lebs", "max_num_lebs", "max_bud_bytes", "num_log_lebs", "num_lpt_lebs", "num_orphan_lebs", "num_journal_heads", "fanout", "num_save_table_entries", "fmt_version", "default_compression", "padding1", "reserve_pool_uid", "reserve_pool_gid", "reserve_pool_size", "time_granularity", "uuid", "ro_compat_version", "hmac", "hmac_wkm", "hash_algo", "hash_algo_unused", "hash_mst", "padding2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.SuperblockHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['padding0']['start'] = self._io.pos()
            self.padding0 = self._io.read_bytes(2)
            self._debug['padding0']['end'] = self._io.pos()
            if not self.padding0 == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.padding0, self._io, u"/types/superblock_header/seq/0")
            self._debug['key_hash']['start'] = self._io.pos()
            self.key_hash = KaitaiStream.resolve_enum(Ubifs.Hashes, self._io.read_u1())
            self._debug['key_hash']['end'] = self._io.pos()
            if not isinstance(self.key_hash, Ubifs.Hashes):
                raise kaitaistruct.ValidationNotInEnumError(self.key_hash, self._io, u"/types/superblock_header/seq/1")
            self._debug['key_fmt']['start'] = self._io.pos()
            self.key_fmt = KaitaiStream.resolve_enum(Ubifs.KeyFormats, self._io.read_u1())
            self._debug['key_fmt']['end'] = self._io.pos()
            if not self.key_fmt == Ubifs.KeyFormats.simple:
                raise kaitaistruct.ValidationNotEqualError(Ubifs.KeyFormats.simple, self.key_fmt, self._io, u"/types/superblock_header/seq/2")
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['min_io_size']['start'] = self._io.pos()
            self.min_io_size = self._io.read_u4le()
            self._debug['min_io_size']['end'] = self._io.pos()
            self._debug['leb_size']['start'] = self._io.pos()
            self.leb_size = self._io.read_u4le()
            self._debug['leb_size']['end'] = self._io.pos()
            self._debug['num_lebs']['start'] = self._io.pos()
            self.num_lebs = self._io.read_u4le()
            self._debug['num_lebs']['end'] = self._io.pos()
            self._debug['max_num_lebs']['start'] = self._io.pos()
            self.max_num_lebs = self._io.read_u4le()
            self._debug['max_num_lebs']['end'] = self._io.pos()
            if not self.max_num_lebs >= self.num_lebs:
                raise kaitaistruct.ValidationLessThanError(self.num_lebs, self.max_num_lebs, self._io, u"/types/superblock_header/seq/7")
            self._debug['max_bud_bytes']['start'] = self._io.pos()
            self.max_bud_bytes = self._io.read_u8le()
            self._debug['max_bud_bytes']['end'] = self._io.pos()
            self._debug['num_log_lebs']['start'] = self._io.pos()
            self.num_log_lebs = self._io.read_u4le()
            self._debug['num_log_lebs']['end'] = self._io.pos()
            if not self.num_log_lebs >= 2:
                raise kaitaistruct.ValidationLessThanError(2, self.num_log_lebs, self._io, u"/types/superblock_header/seq/9")
            self._debug['num_lpt_lebs']['start'] = self._io.pos()
            self.num_lpt_lebs = self._io.read_u4le()
            self._debug['num_lpt_lebs']['end'] = self._io.pos()
            if not self.num_lpt_lebs >= 2:
                raise kaitaistruct.ValidationLessThanError(2, self.num_lpt_lebs, self._io, u"/types/superblock_header/seq/10")
            self._debug['num_orphan_lebs']['start'] = self._io.pos()
            self.num_orphan_lebs = self._io.read_u4le()
            self._debug['num_orphan_lebs']['end'] = self._io.pos()
            if not self.num_orphan_lebs >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.num_orphan_lebs, self._io, u"/types/superblock_header/seq/11")
            self._debug['num_journal_heads']['start'] = self._io.pos()
            self.num_journal_heads = self._io.read_u4le()
            self._debug['num_journal_heads']['end'] = self._io.pos()
            self._debug['fanout']['start'] = self._io.pos()
            self.fanout = self._io.read_u4le()
            self._debug['fanout']['end'] = self._io.pos()
            self._debug['num_save_table_entries']['start'] = self._io.pos()
            self.num_save_table_entries = self._io.read_u4le()
            self._debug['num_save_table_entries']['end'] = self._io.pos()
            self._debug['fmt_version']['start'] = self._io.pos()
            self.fmt_version = self._io.read_u4le()
            self._debug['fmt_version']['end'] = self._io.pos()
            if not self.fmt_version >= 4:
                raise kaitaistruct.ValidationLessThanError(4, self.fmt_version, self._io, u"/types/superblock_header/seq/15")
            self._debug['default_compression']['start'] = self._io.pos()
            self.default_compression = KaitaiStream.resolve_enum(Ubifs.Compression, self._io.read_u2le())
            self._debug['default_compression']['end'] = self._io.pos()
            if not isinstance(self.default_compression, Ubifs.Compression):
                raise kaitaistruct.ValidationNotInEnumError(self.default_compression, self._io, u"/types/superblock_header/seq/16")
            self._debug['padding1']['start'] = self._io.pos()
            self.padding1 = self._io.read_bytes(2)
            self._debug['padding1']['end'] = self._io.pos()
            if not self.padding1 == b"\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00", self.padding1, self._io, u"/types/superblock_header/seq/17")
            self._debug['reserve_pool_uid']['start'] = self._io.pos()
            self.reserve_pool_uid = self._io.read_u4le()
            self._debug['reserve_pool_uid']['end'] = self._io.pos()
            self._debug['reserve_pool_gid']['start'] = self._io.pos()
            self.reserve_pool_gid = self._io.read_u4le()
            self._debug['reserve_pool_gid']['end'] = self._io.pos()
            self._debug['reserve_pool_size']['start'] = self._io.pos()
            self.reserve_pool_size = self._io.read_u8le()
            self._debug['reserve_pool_size']['end'] = self._io.pos()
            self._debug['time_granularity']['start'] = self._io.pos()
            self.time_granularity = self._io.read_u4le()
            self._debug['time_granularity']['end'] = self._io.pos()
            if not self.time_granularity >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.time_granularity, self._io, u"/types/superblock_header/seq/21")
            if not self.time_granularity <= 1000000000:
                raise kaitaistruct.ValidationGreaterThanError(1000000000, self.time_granularity, self._io, u"/types/superblock_header/seq/21")
            self._debug['uuid']['start'] = self._io.pos()
            self.uuid = self._io.read_bytes(16)
            self._debug['uuid']['end'] = self._io.pos()
            self._debug['ro_compat_version']['start'] = self._io.pos()
            self.ro_compat_version = self._io.read_u4le()
            self._debug['ro_compat_version']['end'] = self._io.pos()
            self._debug['hmac']['start'] = self._io.pos()
            self.hmac = self._io.read_bytes(64)
            self._debug['hmac']['end'] = self._io.pos()
            self._debug['hmac_wkm']['start'] = self._io.pos()
            self.hmac_wkm = self._io.read_bytes(64)
            self._debug['hmac_wkm']['end'] = self._io.pos()
            if self.authenticated:
                pass
                self._debug['hash_algo']['start'] = self._io.pos()
                self.hash_algo = KaitaiStream.resolve_enum(Ubifs.HashAlgos, self._io.read_u2le())
                self._debug['hash_algo']['end'] = self._io.pos()
                if not isinstance(self.hash_algo, Ubifs.HashAlgos):
                    raise kaitaistruct.ValidationNotInEnumError(self.hash_algo, self._io, u"/types/superblock_header/seq/26")

            if (not (self.authenticated)):
                pass
                self._debug['hash_algo_unused']['start'] = self._io.pos()
                self.hash_algo_unused = self._io.read_u2le()
                self._debug['hash_algo_unused']['end'] = self._io.pos()

            self._debug['hash_mst']['start'] = self._io.pos()
            self.hash_mst = self._io.read_bytes(64)
            self._debug['hash_mst']['end'] = self._io.pos()
            self._debug['padding2']['start'] = self._io.pos()
            self.padding2 = self._io.read_bytes(3774)
            self._debug['padding2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            if self.authenticated:
                pass

            if (not (self.authenticated)):
                pass


        @property
        def authenticated(self):
            """this filesystem contains hashes for authentication."""
            if hasattr(self, '_m_authenticated'):
                return self._m_authenticated

            self._m_authenticated = self.flags & 32 != 0
            return getattr(self, '_m_authenticated', None)

        @property
        def biglpt(self):
            """if "big" LPT model is used if set."""
            if hasattr(self, '_m_biglpt'):
                return self._m_biglpt

            self._m_biglpt = self.flags & 2 != 0
            return getattr(self, '_m_biglpt', None)

        @property
        def double_hash(self):
            """store a 32bit cookie in directory entry nodes to
            support 64bit cookies for lookups by hash
            """
            if hasattr(self, '_m_double_hash'):
                return self._m_double_hash

            self._m_double_hash = self.flags & 8 != 0
            return getattr(self, '_m_double_hash', None)

        @property
        def encrypted(self):
            """filesystem contains encrypted files."""
            if hasattr(self, '_m_encrypted'):
                return self._m_encrypted

            self._m_encrypted = self.flags & 16 != 0
            return getattr(self, '_m_encrypted', None)

        @property
        def len_hash(self):
            """Length in bytes of the hash of a node (`c->hash_len` in Linux), e.g.
            in each branch of an index node. In an authenticated file system, it
            is determined by `hash_algo`. Otherwise, it is 0.
            """
            if hasattr(self, '_m_len_hash'):
                return self._m_len_hash

            self._m_len_hash = (0 if (not (self.authenticated)) else (16 if  ((self.hash_algo == Ubifs.HashAlgos.md4) or (self.hash_algo == Ubifs.HashAlgos.md5) or (self.hash_algo == Ubifs.HashAlgos.ripe_md_128) or (self.hash_algo == Ubifs.HashAlgos.tgr_128))  else (20 if  ((self.hash_algo == Ubifs.HashAlgos.sha1) or (self.hash_algo == Ubifs.HashAlgos.ripe_md_160) or (self.hash_algo == Ubifs.HashAlgos.tgr_160))  else (24 if self.hash_algo == Ubifs.HashAlgos.tgr_192 else (28 if self.hash_algo == Ubifs.HashAlgos.sha224 else (32 if  ((self.hash_algo == Ubifs.HashAlgos.sha256) or (self.hash_algo == Ubifs.HashAlgos.ripe_md_256) or (self.hash_algo == Ubifs.HashAlgos.wp_256) or (self.hash_algo == Ubifs.HashAlgos.sm3_256) or (self.hash_algo == Ubifs.HashAlgos.streebog_256) or (self.hash_algo == Ubifs.HashAlgos.sha3_256))  else (40 if self.hash_algo == Ubifs.HashAlgos.ripe_md_320 else (48 if  ((self.hash_algo == Ubifs.HashAlgos.sha384) or (self.hash_algo == Ubifs.HashAlgos.wp_384) or (self.hash_algo == Ubifs.HashAlgos.sha3_384))  else (64 if  ((self.hash_algo == Ubifs.HashAlgos.sha512) or (self.hash_algo == Ubifs.HashAlgos.wp_512) or (self.hash_algo == Ubifs.HashAlgos.streebog_512) or (self.hash_algo == Ubifs.HashAlgos.sha3_512))  else -1)))))))))
            return getattr(self, '_m_len_hash', None)

        @property
        def space_fixup(self):
            """first-mount "fixup" of free space within LEBs needed."""
            if hasattr(self, '_m_space_fixup'):
                return self._m_space_fixup

            self._m_space_fixup = self.flags & 4 != 0
            return getattr(self, '_m_space_fixup', None)


    class SuperblockNode(KaitaiStruct):
        SEQ_FIELDS = ["header", "node_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.SuperblockNode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Ubifs.CommonHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            _ = self.header
            if not _.node_type == Ubifs.NodeTypes.superblock:
                raise kaitaistruct.ValidationExprError(self.header, self._io, u"/types/superblock_node/seq/0")
            self._debug['node_header']['start'] = self._io.pos()
            self._raw_node_header = self._io.read_bytes(self.header.len_full_node - 24)
            _io__raw_node_header = KaitaiStream(BytesIO(self._raw_node_header))
            self.node_header = Ubifs.SuperblockHeader(_io__raw_node_header, self, self._root)
            self._debug['node_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.node_header._fetch_instances()


    class TruncationHeader(KaitaiStruct):
        """This node exists only in the journal and never goes to the main area.
        
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/ubifs-media.h#L586-L604
        """
        SEQ_FIELDS = ["inode_number", "padding", "old_size", "new_size"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ubifs.TruncationHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['inode_number']['start'] = self._io.pos()
            self.inode_number = self._io.read_u4le()
            self._debug['inode_number']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(12)
            self._debug['padding']['end'] = self._io.pos()
            self._debug['old_size']['start'] = self._io.pos()
            self.old_size = self._io.read_u8le()
            self._debug['old_size']['end'] = self._io.pos()
            if not self.old_size >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.old_size, self._io, u"/types/truncation_header/seq/2")
            self._debug['new_size']['start'] = self._io.pos()
            self.new_size = self._io.read_u8le()
            self._debug['new_size']['end'] = self._io.pos()
            if not self.new_size <= self.old_size - 1:
                raise kaitaistruct.ValidationGreaterThanError(self.old_size - 1, self.new_size, self._io, u"/types/truncation_header/seq/3")


        def _fetch_instances(self):
            pass


    @property
    def index(self):
        """The LEB containing the root index node, as given by `leb_root` in
        `master_1`.
        
        This instance only provides the substream for `index_root`, which can then
        use `ofs_root` (an offset within the LEB) as its `pos` directly.
        """
        if hasattr(self, '_m_index'):
            return self._m_index

        _pos = self._io.pos()
        self._io.seek(self.superblock.node_header.leb_size * self.master_1.node_header.leb_root)
        self._debug['_m_index']['start'] = self._io.pos()
        self._raw__m_index = self._io.read_bytes(self.superblock.node_header.leb_size)
        _io__raw__m_index = KaitaiStream(BytesIO(self._raw__m_index))
        self._m_index = Ubifs.Dummy(_io__raw__m_index, self, self._root)
        self._debug['_m_index']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_index', None)

    @property
    def index_root(self):
        """The root index node, in the `index` LEB at the offset given by
        `ofs_root` in `master_1`. All other index nodes, and through them all
        the files, are reached from it by recursively following the `target` of
        each of the `branches`.
        """
        if hasattr(self, '_m_index_root'):
            return self._m_index_root

        io = self.index._io
        _pos = io.pos()
        io.seek(self.master_1.node_header.ofs_root)
        self._debug['_m_index_root']['start'] = io.pos()
        self._m_index_root = Ubifs.IndexBlock(io, self, self._root)
        self._debug['_m_index_root']['end'] = io.pos()
        _ = self._m_index_root
        if not _.header.len_full_node == self.master_1.node_header.len_root:
            raise kaitaistruct.ValidationExprError(self._m_index_root, self._io, u"/instances/index_root")
        io.seek(_pos)
        return getattr(self, '_m_index_root', None)

    @property
    def lebs(self):
        """All LEBs of the file system: `lebs[n]` is LEB number `n`, which starts
        at offset `n * <superblock_header>.leb_size`.
        
        Accessing this instance reads the whole image into memory. To get a
        single LEB, it's cheaper to read `<superblock_header>.leb_size` bytes
        at the offset of that LEB.
        """
        if hasattr(self, '_m_lebs'):
            return self._m_lebs

        _pos = self._io.pos()
        self._io.seek(0)
        self._debug['_m_lebs']['start'] = self._io.pos()
        self._debug['_m_lebs']['arr'] = []
        self._m_lebs = []
        for i in range(self.superblock.node_header.num_lebs):
            self._debug['_m_lebs']['arr'].append({'start': self._io.pos()})
            self._m_lebs.append(self._io.read_bytes(self.superblock.node_header.leb_size))
            self._debug['_m_lebs']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_lebs']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_lebs', None)

    @property
    def len_image(self):
        """Length of the file system image in bytes:
        `<superblock_header>.num_lebs` LEBs of `<superblock_header>.leb_size`
        bytes each. Use it to find where the image ends and to detect a
        truncated image (see the top-level `doc`).
        """
        if hasattr(self, '_m_len_image'):
            return self._m_len_image

        self._m_len_image = self.superblock.node_header.leb_size * self.superblock.node_header.num_lebs
        return getattr(self, '_m_len_image', None)

    @property
    def master_1(self):
        """The first copy of the master node in LEB1. This Kaitai Struct
        implementation uses it to locate `index_root`. In an image created by
        `mkfs.ubifs`, it is the only copy in LEB1.
        
        .. seealso::
           Git tag "v2.3.1" - https://github.com/sigma-star/mtd-utils/blob/053ee1038e5dedae61a88cadfb7bdfe9894d8bb6/ubifs-utils/mkfs.ubifs/mkfs.ubifs.c#L2627-L2633
        """
        if hasattr(self, '_m_master_1'):
            return self._m_master_1

        _pos = self._io.pos()
        self._io.seek(self.superblock.node_header.leb_size)
        self._debug['_m_master_1']['start'] = self._io.pos()
        self._raw__m_master_1 = self._io.read_bytes(self.superblock.node_header.leb_size)
        _io__raw__m_master_1 = KaitaiStream(BytesIO(self._raw__m_master_1))
        self._m_master_1 = Ubifs.MasterblockNode(_io__raw__m_master_1, self, self._root)
        self._debug['_m_master_1']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_master_1', None)

    @property
    def master_2(self):
        """The first copy of the master node in LEB2. In an image created by
        `mkfs.ubifs`, it is the same as `master_1` except for the sequence
        number and CRC in the common header. Linux keeps the master node in both
        LEB1 and LEB2 for redundancy, and when mounting, it checks that the
        copies in both match.
        
        .. seealso::
           Git tag "v2.3.1" - https://github.com/sigma-star/mtd-utils/blob/053ee1038e5dedae61a88cadfb7bdfe9894d8bb6/ubifs-utils/mkfs.ubifs/mkfs.ubifs.c#L2627-L2633
        
        
        .. seealso::
           Git tag "v7.2" - https://github.com/torvalds/linux/blob/8d3ae59288f1e7d58d76558a6ee96d533bc5019f/fs/ubifs/master.c#L115-L130
        """
        if hasattr(self, '_m_master_2'):
            return self._m_master_2

        _pos = self._io.pos()
        self._io.seek(self.superblock.node_header.leb_size * 2)
        self._debug['_m_master_2']['start'] = self._io.pos()
        self._raw__m_master_2 = self._io.read_bytes(self.superblock.node_header.leb_size)
        _io__raw__m_master_2 = KaitaiStream(BytesIO(self._raw__m_master_2))
        self._m_master_2 = Ubifs.MasterblockNode(_io__raw__m_master_2, self, self._root)
        self._debug['_m_master_2']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_master_2', None)

    @property
    def superblock(self):
        """The superblock node will always be at the start of
        the first LEB.
        """
        if hasattr(self, '_m_superblock'):
            return self._m_superblock

        _pos = self._io.pos()
        self._io.seek(0)
        self._debug['_m_superblock']['start'] = self._io.pos()
        self._m_superblock = Ubifs.SuperblockNode(self._io, self, self._root)
        self._debug['_m_superblock']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_superblock', None)


