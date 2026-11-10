# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Cramfs(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/npitre/cramfs-tools
    """

    class Magic(IntEnum):
        big = 684539205
        little = 1161678120

    class Modes(IntEnum):
        fifo = 4096
        character_device = 8192
        directory = 16384
        block_device = 24576
        regular = 32768
        link = 40960
        socket = 49152
    SEQ_FIELDS = ["magic", "header", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Cramfs, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = KaitaiStream.resolve_enum(Cramfs.Magic, self._io.read_u4be())
        self._debug['magic']['end'] = self._io.pos()
        if not  ((self.magic == Cramfs.Magic.big) or (self.magic == Cramfs.Magic.little)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.magic, self._io, u"/seq/0")
        self._debug['header']['start'] = self._io.pos()
        self.header = Cramfs.EndianHeader(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self._raw_data = self._io.read_bytes((self.header.len_cramfs - 4) - 60)
        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
        self.data = Cramfs.Inodes(self.header.num_files, _io__raw_data, self, self._root)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.data._fetch_instances()

    class EndianHeader(KaitaiStruct):
        SEQ_FIELDS = ["len_cramfs", "feature_flags", "reserved", "signature", "crc32", "edition", "num_blocks", "num_files", "volume_name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Cramfs.EndianHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            _on = self._root.magic
            if _on == Cramfs.Magic.little:
                pass
                self._is_le = True
            elif _on == Cramfs.Magic.big:
                pass
                self._is_le = False
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/endian_header")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self._debug['len_cramfs']['start'] = self._io.pos()
            self.len_cramfs = self._io.read_u4le()
            self._debug['len_cramfs']['end'] = self._io.pos()
            self._debug['feature_flags']['start'] = self._io.pos()
            self.feature_flags = self._io.read_u4le()
            self._debug['feature_flags']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(4)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(16)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x43\x6F\x6D\x70\x72\x65\x73\x73\x65\x64\x20\x52\x4F\x4D\x46\x53":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x6F\x6D\x70\x72\x65\x73\x73\x65\x64\x20\x52\x4F\x4D\x46\x53", self.signature, self._io, u"/types/endian_header/seq/3")
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['edition']['start'] = self._io.pos()
            self.edition = self._io.read_u4le()
            self._debug['edition']['end'] = self._io.pos()
            self._debug['num_blocks']['start'] = self._io.pos()
            self.num_blocks = self._io.read_u4le()
            self._debug['num_blocks']['end'] = self._io.pos()
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u4le()
            self._debug['num_files']['end'] = self._io.pos()
            self._debug['volume_name']['start'] = self._io.pos()
            self.volume_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"UTF-8")
            self._debug['volume_name']['end'] = self._io.pos()

        def _read_be(self):
            self._debug['len_cramfs']['start'] = self._io.pos()
            self.len_cramfs = self._io.read_u4be()
            self._debug['len_cramfs']['end'] = self._io.pos()
            self._debug['feature_flags']['start'] = self._io.pos()
            self.feature_flags = self._io.read_u4be()
            self._debug['feature_flags']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(4)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(16)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x43\x6F\x6D\x70\x72\x65\x73\x73\x65\x64\x20\x52\x4F\x4D\x46\x53":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x6F\x6D\x70\x72\x65\x73\x73\x65\x64\x20\x52\x4F\x4D\x46\x53", self.signature, self._io, u"/types/endian_header/seq/3")
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4be()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['edition']['start'] = self._io.pos()
            self.edition = self._io.read_u4be()
            self._debug['edition']['end'] = self._io.pos()
            self._debug['num_blocks']['start'] = self._io.pos()
            self.num_blocks = self._io.read_u4be()
            self._debug['num_blocks']['end'] = self._io.pos()
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u4be()
            self._debug['num_files']['end'] = self._io.pos()
            self._debug['volume_name']['start'] = self._io.pos()
            self.volume_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"UTF-8")
            self._debug['volume_name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def block_pointer_extensions(self):
            if hasattr(self, '_m_block_pointer_extensions'):
                return self._m_block_pointer_extensions

            self._m_block_pointer_extensions = self.feature_flags & 2048 == 2048
            return getattr(self, '_m_block_pointer_extensions', None)

        @property
        def holes(self):
            if hasattr(self, '_m_holes'):
                return self._m_holes

            self._m_holes = self.feature_flags & 256 == 256
            return getattr(self, '_m_holes', None)

        @property
        def shifted_root_offset(self):
            if hasattr(self, '_m_shifted_root_offset'):
                return self._m_shifted_root_offset

            self._m_shifted_root_offset = self.feature_flags & 1024 == 1024
            return getattr(self, '_m_shifted_root_offset', None)

        @property
        def sorted_dirs(self):
            if hasattr(self, '_m_sorted_dirs'):
                return self._m_sorted_dirs

            self._m_sorted_dirs = self.feature_flags & 2 == 2
            return getattr(self, '_m_sorted_dirs', None)

        @property
        def version(self):
            if hasattr(self, '_m_version'):
                return self._m_version

            self._m_version = (2 if self.feature_flags & 1 == 1 else 0)
            return getattr(self, '_m_version', None)


    class Inodes(KaitaiStruct):
        SEQ_FIELDS = ["inodes"]
        def __init__(self, num_files, _io, _parent=None, _root=None):
            super(Cramfs.Inodes, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_files = num_files
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            _on = self._root.magic
            if _on == Cramfs.Magic.little:
                pass
                self._is_le = True
            elif _on == Cramfs.Magic.big:
                pass
                self._is_le = False
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/inodes")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self._debug['inodes']['start'] = self._io.pos()
            self._debug['inodes']['arr'] = []
            self.inodes = []
            for i in range(self.num_files):
                self._debug['inodes']['arr'].append({'start': self._io.pos()})
                self.inodes.append(Cramfs.Inodes.Inode(self._io, self, self._root, self._is_le))
                self._debug['inodes']['arr'][i]['end'] = self._io.pos()

            self._debug['inodes']['end'] = self._io.pos()

        def _read_be(self):
            self._debug['inodes']['start'] = self._io.pos()
            self._debug['inodes']['arr'] = []
            self.inodes = []
            for i in range(self.num_files):
                self._debug['inodes']['arr'].append({'start': self._io.pos()})
                self.inodes.append(Cramfs.Inodes.Inode(self._io, self, self._root, self._is_le))
                self._debug['inodes']['arr'][i]['end'] = self._io.pos()

            self._debug['inodes']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.inodes)):
                pass
                self.inodes[i]._fetch_instances()


        class BlockPointers(KaitaiStruct):
            SEQ_FIELDS = ["block_pointers"]
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                super(Cramfs.Inodes.BlockPointers, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._is_le = _is_le
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/inodes/types/block_pointers")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self._debug['block_pointers']['start'] = self._io.pos()
                self._debug['block_pointers']['arr'] = []
                self.block_pointers = []
                i = 0
                while not self._io.is_eof():
                    self._debug['block_pointers']['arr'].append({'start': self._io.pos()})
                    self.block_pointers.append(self._io.read_u4le())
                    self._debug['block_pointers']['arr'][len(self.block_pointers) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['block_pointers']['end'] = self._io.pos()

            def _read_be(self):
                self._debug['block_pointers']['start'] = self._io.pos()
                self._debug['block_pointers']['arr'] = []
                self.block_pointers = []
                i = 0
                while not self._io.is_eof():
                    self._debug['block_pointers']['arr'].append({'start': self._io.pos()})
                    self.block_pointers.append(self._io.read_u4be())
                    self._debug['block_pointers']['arr'][len(self.block_pointers) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['block_pointers']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.block_pointers)):
                    pass



        class Inode(KaitaiStruct):
            SEQ_FIELDS = ["mode", "uid", "len_decompressed", "gid", "name_length", "name"]
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                super(Cramfs.Inodes.Inode, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._is_le = _is_le
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/inodes/types/inode")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self._debug['mode']['start'] = self._io.pos()
                self.mode = self._io.read_u2le()
                self._debug['mode']['end'] = self._io.pos()
                self._debug['uid']['start'] = self._io.pos()
                self.uid = self._io.read_u2le()
                self._debug['uid']['end'] = self._io.pos()
                self._debug['len_decompressed']['start'] = self._io.pos()
                _on = self._root.magic
                if _on == Cramfs.Magic.big:
                    pass
                    self.len_decompressed = self._io.read_bits_int_be(24)
                elif _on == Cramfs.Magic.little:
                    pass
                    self.len_decompressed = self._io.read_bits_int_le(24)
                self._debug['len_decompressed']['end'] = self._io.pos()
                self._debug['gid']['start'] = self._io.pos()
                self.gid = self._io.read_u1()
                self._debug['gid']['end'] = self._io.pos()
                self._debug['name_length']['start'] = self._io.pos()
                self.name_length = self._io.read_u4le()
                self._debug['name_length']['end'] = self._io.pos()
                self._debug['name']['start'] = self._io.pos()
                self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_name), 0, False)).decode(u"UTF-8")
                self._debug['name']['end'] = self._io.pos()

            def _read_be(self):
                self._debug['mode']['start'] = self._io.pos()
                self.mode = self._io.read_u2be()
                self._debug['mode']['end'] = self._io.pos()
                self._debug['uid']['start'] = self._io.pos()
                self.uid = self._io.read_u2be()
                self._debug['uid']['end'] = self._io.pos()
                self._debug['len_decompressed']['start'] = self._io.pos()
                _on = self._root.magic
                if _on == Cramfs.Magic.big:
                    pass
                    self.len_decompressed = self._io.read_bits_int_be(24)
                elif _on == Cramfs.Magic.little:
                    pass
                    self.len_decompressed = self._io.read_bits_int_le(24)
                self._debug['len_decompressed']['end'] = self._io.pos()
                self._debug['gid']['start'] = self._io.pos()
                self.gid = self._io.read_u1()
                self._debug['gid']['end'] = self._io.pos()
                self._debug['name_length']['start'] = self._io.pos()
                self.name_length = self._io.read_u4be()
                self._debug['name_length']['end'] = self._io.pos()
                self._debug['name']['start'] = self._io.pos()
                self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_name), 0, False)).decode(u"UTF-8")
                self._debug['name']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _on = self._root.magic
                if _on == Cramfs.Magic.big:
                    pass
                elif _on == Cramfs.Magic.little:
                    pass
                _ = self.block_pointers
                if hasattr(self, '_m_block_pointers'):
                    pass
                    self._m_block_pointers._fetch_instances()


            @property
            def block_pointers(self):
                if hasattr(self, '_m_block_pointers'):
                    return self._m_block_pointers

                if  ((self.file_mode == Cramfs.Modes.regular) or (self.file_mode == Cramfs.Modes.link)) :
                    pass
                    io = self._root._io
                    _pos = io.pos()
                    io.seek(self.ofs_data)
                    if self._is_le:
                        self._debug['_m_block_pointers']['start'] = io.pos()
                        self._raw__m_block_pointers = io.read_bytes(self.nblocks * 4)
                        _io__raw__m_block_pointers = KaitaiStream(BytesIO(self._raw__m_block_pointers))
                        self._m_block_pointers = Cramfs.Inodes.BlockPointers(_io__raw__m_block_pointers, self, self._root, self._is_le)
                        self._debug['_m_block_pointers']['end'] = io.pos()
                    else:
                        self._debug['_m_block_pointers']['start'] = io.pos()
                        self._raw__m_block_pointers = io.read_bytes(self.nblocks * 4)
                        _io__raw__m_block_pointers = KaitaiStream(BytesIO(self._raw__m_block_pointers))
                        self._m_block_pointers = Cramfs.Inodes.BlockPointers(_io__raw__m_block_pointers, self, self._root, self._is_le)
                        self._debug['_m_block_pointers']['end'] = io.pos()
                    io.seek(_pos)

                return getattr(self, '_m_block_pointers', None)

            @property
            def file_mode(self):
                if hasattr(self, '_m_file_mode'):
                    return self._m_file_mode

                self._m_file_mode = KaitaiStream.resolve_enum(Cramfs.Modes, self.mode & 61440)
                return getattr(self, '_m_file_mode', None)

            @property
            def len_name(self):
                if hasattr(self, '_m_len_name'):
                    return self._m_len_name

                self._m_len_name = (((self.name_length & 4227858432) >> 26) * 4 if self._root.magic == Cramfs.Magic.big else (self.name_length & 63) * 4)
                return getattr(self, '_m_len_name', None)

            @property
            def nblocks(self):
                if hasattr(self, '_m_nblocks'):
                    return self._m_nblocks

                self._m_nblocks = (self.len_decompressed - 1) // self._root.block_size + 1
                return getattr(self, '_m_nblocks', None)

            @property
            def ofs_data(self):
                if hasattr(self, '_m_ofs_data'):
                    return self._m_ofs_data

                self._m_ofs_data = ((self.name_length & 67108863) * 4 if self._root.magic == Cramfs.Magic.big else ((self.name_length & 67108863) >> 6) * 4)
                return getattr(self, '_m_ofs_data', None)



    @property
    def block_size(self):
        if hasattr(self, '_m_block_size'):
            return self._m_block_size

        self._m_block_size = 4096
        return getattr(self, '_m_block_size', None)


