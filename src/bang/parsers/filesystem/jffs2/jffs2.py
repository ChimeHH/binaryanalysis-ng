# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Jffs2(KaitaiStruct):

    class Compression(IntEnum):
        no_compression = 0
        zero = 1
        rtime = 2
        rubinmips = 3
        copy = 4
        dynrubin = 5
        zlib = 6
        lzo = 7
        lzma = 8

    class InodeType(IntEnum):
        clean_marker = 8195
        padding = 8196
        summary = 8198
        dirent = 57345
        inode = 57346
        xattr = 57352
        xref = 57353

    class Magic(IntEnum):
        dirty = 0
        be = 6533
        le = 34073

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
        super(Jffs2, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = KaitaiStream.resolve_enum(Jffs2.Magic, self._io.read_u2be())
        self._debug['magic']['end'] = self._io.pos()
        if not  ((self.magic == Jffs2.Magic.be) or (self.magic == Jffs2.Magic.le) or (self.magic == Jffs2.Magic.dirty)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.magic, self._io, u"/seq/0")
        self._debug['header']['start'] = self._io.pos()
        self.header = Jffs2.InodeHeader(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        _on = self.header.inode_type
        if _on == Jffs2.InodeType.dirent:
            pass
            self._raw_data = self._io.read_bytes((self.header.len_inode - 6) - 2)
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = Jffs2.Dirent(_io__raw_data, self, self._root)
        elif _on == Jffs2.InodeType.inode:
            pass
            self._raw_data = self._io.read_bytes((self.header.len_inode - 6) - 2)
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = Jffs2.Inode(_io__raw_data, self, self._root)
        else:
            pass
            self.data = self._io.read_bytes((self.header.len_inode - 6) - 2)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        _on = self.header.inode_type
        if _on == Jffs2.InodeType.dirent:
            pass
            self.data._fetch_instances()
        elif _on == Jffs2.InodeType.inode:
            pass
            self.data._fetch_instances()
        else:
            pass

    class Dirent(KaitaiStruct):
        SEQ_FIELDS = ["header_crc", "parent_inode", "inode_version", "inode_number", "mctime", "len_name", "dirent_type", "unused", "node_crc", "name_crc", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Jffs2.Dirent, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            _on = self._root.magic
            if _on == Jffs2.Magic.le:
                pass
                self._is_le = True
            elif _on == Jffs2.Magic.be:
                pass
                self._is_le = False
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/dirent")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self._debug['header_crc']['start'] = self._io.pos()
            self.header_crc = self._io.read_u4le()
            self._debug['header_crc']['end'] = self._io.pos()
            self._debug['parent_inode']['start'] = self._io.pos()
            self.parent_inode = self._io.read_u4le()
            self._debug['parent_inode']['end'] = self._io.pos()
            self._debug['inode_version']['start'] = self._io.pos()
            self.inode_version = self._io.read_u4le()
            self._debug['inode_version']['end'] = self._io.pos()
            self._debug['inode_number']['start'] = self._io.pos()
            self.inode_number = self._io.read_u4le()
            self._debug['inode_number']['end'] = self._io.pos()
            self._debug['mctime']['start'] = self._io.pos()
            self.mctime = self._io.read_u4le()
            self._debug['mctime']['end'] = self._io.pos()
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_u1()
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['dirent_type']['start'] = self._io.pos()
            self.dirent_type = self._io.read_u1()
            self._debug['dirent_type']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_bytes(2)
            self._debug['unused']['end'] = self._io.pos()
            self._debug['node_crc']['start'] = self._io.pos()
            self.node_crc = self._io.read_u4le()
            self._debug['node_crc']['end'] = self._io.pos()
            self._debug['name_crc']['start'] = self._io.pos()
            self.name_crc = self._io.read_u4le()
            self._debug['name_crc']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = self._io.read_bytes(self.len_name)
            self._debug['name']['end'] = self._io.pos()

        def _read_be(self):
            self._debug['header_crc']['start'] = self._io.pos()
            self.header_crc = self._io.read_u4be()
            self._debug['header_crc']['end'] = self._io.pos()
            self._debug['parent_inode']['start'] = self._io.pos()
            self.parent_inode = self._io.read_u4be()
            self._debug['parent_inode']['end'] = self._io.pos()
            self._debug['inode_version']['start'] = self._io.pos()
            self.inode_version = self._io.read_u4be()
            self._debug['inode_version']['end'] = self._io.pos()
            self._debug['inode_number']['start'] = self._io.pos()
            self.inode_number = self._io.read_u4be()
            self._debug['inode_number']['end'] = self._io.pos()
            self._debug['mctime']['start'] = self._io.pos()
            self.mctime = self._io.read_u4be()
            self._debug['mctime']['end'] = self._io.pos()
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_u1()
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['dirent_type']['start'] = self._io.pos()
            self.dirent_type = self._io.read_u1()
            self._debug['dirent_type']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_bytes(2)
            self._debug['unused']['end'] = self._io.pos()
            self._debug['node_crc']['start'] = self._io.pos()
            self.node_crc = self._io.read_u4be()
            self._debug['node_crc']['end'] = self._io.pos()
            self._debug['name_crc']['start'] = self._io.pos()
            self.name_crc = self._io.read_u4be()
            self._debug['name_crc']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = self._io.read_bytes(self.len_name)
            self._debug['name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Inode(KaitaiStruct):
        SEQ_FIELDS = ["header_crc", "inode_number", "inode_version", "mode", "uid", "gid", "isize", "atime", "mtime", "ctime", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Jffs2.Inode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            _on = self._root.magic
            if _on == Jffs2.Magic.le:
                pass
                self._is_le = True
            elif _on == Jffs2.Magic.be:
                pass
                self._is_le = False
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/inode")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self._debug['header_crc']['start'] = self._io.pos()
            self.header_crc = self._io.read_u4le()
            self._debug['header_crc']['end'] = self._io.pos()
            self._debug['inode_number']['start'] = self._io.pos()
            self.inode_number = self._io.read_u4le()
            self._debug['inode_number']['end'] = self._io.pos()
            self._debug['inode_version']['start'] = self._io.pos()
            self.inode_version = self._io.read_u4le()
            self._debug['inode_version']['end'] = self._io.pos()
            self._debug['mode']['start'] = self._io.pos()
            self.mode = self._io.read_u4le()
            self._debug['mode']['end'] = self._io.pos()
            self._debug['uid']['start'] = self._io.pos()
            self.uid = self._io.read_u2le()
            self._debug['uid']['end'] = self._io.pos()
            self._debug['gid']['start'] = self._io.pos()
            self.gid = self._io.read_u2le()
            self._debug['gid']['end'] = self._io.pos()
            self._debug['isize']['start'] = self._io.pos()
            self.isize = self._io.read_u4le()
            self._debug['isize']['end'] = self._io.pos()
            self._debug['atime']['start'] = self._io.pos()
            self.atime = self._io.read_u4le()
            self._debug['atime']['end'] = self._io.pos()
            self._debug['mtime']['start'] = self._io.pos()
            self.mtime = self._io.read_u4le()
            self._debug['mtime']['end'] = self._io.pos()
            self._debug['ctime']['start'] = self._io.pos()
            self.ctime = self._io.read_u4le()
            self._debug['ctime']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.file_mode
            if _on == Jffs2.Modes.link:
                pass
                self._raw_body = self._io.read_bytes_full()
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Jffs2.Inode.Regular(_io__raw_body, self, self._root, self._is_le)
            elif _on == Jffs2.Modes.regular:
                pass
                self._raw_body = self._io.read_bytes_full()
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Jffs2.Inode.Regular(_io__raw_body, self, self._root, self._is_le)
            else:
                pass
                self.body = self._io.read_bytes_full()
            self._debug['body']['end'] = self._io.pos()

        def _read_be(self):
            self._debug['header_crc']['start'] = self._io.pos()
            self.header_crc = self._io.read_u4be()
            self._debug['header_crc']['end'] = self._io.pos()
            self._debug['inode_number']['start'] = self._io.pos()
            self.inode_number = self._io.read_u4be()
            self._debug['inode_number']['end'] = self._io.pos()
            self._debug['inode_version']['start'] = self._io.pos()
            self.inode_version = self._io.read_u4be()
            self._debug['inode_version']['end'] = self._io.pos()
            self._debug['mode']['start'] = self._io.pos()
            self.mode = self._io.read_u4be()
            self._debug['mode']['end'] = self._io.pos()
            self._debug['uid']['start'] = self._io.pos()
            self.uid = self._io.read_u2be()
            self._debug['uid']['end'] = self._io.pos()
            self._debug['gid']['start'] = self._io.pos()
            self.gid = self._io.read_u2be()
            self._debug['gid']['end'] = self._io.pos()
            self._debug['isize']['start'] = self._io.pos()
            self.isize = self._io.read_u4be()
            self._debug['isize']['end'] = self._io.pos()
            self._debug['atime']['start'] = self._io.pos()
            self.atime = self._io.read_u4be()
            self._debug['atime']['end'] = self._io.pos()
            self._debug['mtime']['start'] = self._io.pos()
            self.mtime = self._io.read_u4be()
            self._debug['mtime']['end'] = self._io.pos()
            self._debug['ctime']['start'] = self._io.pos()
            self.ctime = self._io.read_u4be()
            self._debug['ctime']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.file_mode
            if _on == Jffs2.Modes.link:
                pass
                self._raw_body = self._io.read_bytes_full()
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Jffs2.Inode.Regular(_io__raw_body, self, self._root, self._is_le)
            elif _on == Jffs2.Modes.regular:
                pass
                self._raw_body = self._io.read_bytes_full()
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Jffs2.Inode.Regular(_io__raw_body, self, self._root, self._is_le)
            else:
                pass
                self.body = self._io.read_bytes_full()
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.file_mode
            if _on == Jffs2.Modes.link:
                pass
                self.body._fetch_instances()
            elif _on == Jffs2.Modes.regular:
                pass
                self.body._fetch_instances()
            else:
                pass

        class Regular(KaitaiStruct):
            SEQ_FIELDS = ["ofs_write", "len_compressed", "len_decompressed", "compression", "requested_compression", "flags", "data_crc", "node_crc", "data"]
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                super(Jffs2.Inode.Regular, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._is_le = _is_le
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                if not hasattr(self, '_is_le'):
                    raise kaitaistruct.UndecidedEndiannessError("/types/inode/types/regular")
                elif self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()

            def _read_le(self):
                self._debug['ofs_write']['start'] = self._io.pos()
                self.ofs_write = self._io.read_u4le()
                self._debug['ofs_write']['end'] = self._io.pos()
                self._debug['len_compressed']['start'] = self._io.pos()
                self.len_compressed = self._io.read_u4le()
                self._debug['len_compressed']['end'] = self._io.pos()
                self._debug['len_decompressed']['start'] = self._io.pos()
                self.len_decompressed = self._io.read_u4le()
                self._debug['len_decompressed']['end'] = self._io.pos()
                self._debug['compression']['start'] = self._io.pos()
                self.compression = KaitaiStream.resolve_enum(Jffs2.Compression, self._io.read_u1())
                self._debug['compression']['end'] = self._io.pos()
                if not  ((self.compression == Jffs2.Compression.no_compression) or (self.compression == Jffs2.Compression.zero) or (self.compression == Jffs2.Compression.rtime) or (self.compression == Jffs2.Compression.rubinmips) or (self.compression == Jffs2.Compression.copy) or (self.compression == Jffs2.Compression.dynrubin) or (self.compression == Jffs2.Compression.zlib) or (self.compression == Jffs2.Compression.lzo) or (self.compression == Jffs2.Compression.lzma)) :
                    raise kaitaistruct.ValidationNotAnyOfError(self.compression, self._io, u"/types/inode/types/regular/seq/3")
                self._debug['requested_compression']['start'] = self._io.pos()
                self.requested_compression = self._io.read_u1()
                self._debug['requested_compression']['end'] = self._io.pos()
                self._debug['flags']['start'] = self._io.pos()
                self.flags = self._io.read_u2le()
                self._debug['flags']['end'] = self._io.pos()
                self._debug['data_crc']['start'] = self._io.pos()
                self.data_crc = self._io.read_u4le()
                self._debug['data_crc']['end'] = self._io.pos()
                self._debug['node_crc']['start'] = self._io.pos()
                self.node_crc = self._io.read_u4le()
                self._debug['node_crc']['end'] = self._io.pos()
                self._debug['data']['start'] = self._io.pos()
                self.data = self._io.read_bytes_full()
                self._debug['data']['end'] = self._io.pos()

            def _read_be(self):
                self._debug['ofs_write']['start'] = self._io.pos()
                self.ofs_write = self._io.read_u4be()
                self._debug['ofs_write']['end'] = self._io.pos()
                self._debug['len_compressed']['start'] = self._io.pos()
                self.len_compressed = self._io.read_u4be()
                self._debug['len_compressed']['end'] = self._io.pos()
                self._debug['len_decompressed']['start'] = self._io.pos()
                self.len_decompressed = self._io.read_u4be()
                self._debug['len_decompressed']['end'] = self._io.pos()
                self._debug['compression']['start'] = self._io.pos()
                self.compression = KaitaiStream.resolve_enum(Jffs2.Compression, self._io.read_u1())
                self._debug['compression']['end'] = self._io.pos()
                if not  ((self.compression == Jffs2.Compression.no_compression) or (self.compression == Jffs2.Compression.zero) or (self.compression == Jffs2.Compression.rtime) or (self.compression == Jffs2.Compression.rubinmips) or (self.compression == Jffs2.Compression.copy) or (self.compression == Jffs2.Compression.dynrubin) or (self.compression == Jffs2.Compression.zlib) or (self.compression == Jffs2.Compression.lzo) or (self.compression == Jffs2.Compression.lzma)) :
                    raise kaitaistruct.ValidationNotAnyOfError(self.compression, self._io, u"/types/inode/types/regular/seq/3")
                self._debug['requested_compression']['start'] = self._io.pos()
                self.requested_compression = self._io.read_u1()
                self._debug['requested_compression']['end'] = self._io.pos()
                self._debug['flags']['start'] = self._io.pos()
                self.flags = self._io.read_u2be()
                self._debug['flags']['end'] = self._io.pos()
                self._debug['data_crc']['start'] = self._io.pos()
                self.data_crc = self._io.read_u4be()
                self._debug['data_crc']['end'] = self._io.pos()
                self._debug['node_crc']['start'] = self._io.pos()
                self.node_crc = self._io.read_u4be()
                self._debug['node_crc']['end'] = self._io.pos()
                self._debug['data']['start'] = self._io.pos()
                self.data = self._io.read_bytes_full()
                self._debug['data']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        @property
        def file_mode(self):
            if hasattr(self, '_m_file_mode'):
                return self._m_file_mode

            self._m_file_mode = KaitaiStream.resolve_enum(Jffs2.Modes, self.mode & 61440)
            return getattr(self, '_m_file_mode', None)


    class InodeHeader(KaitaiStruct):
        SEQ_FIELDS = ["inode_type", "len_inode"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Jffs2.InodeHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            _on = self._root.magic
            if _on == Jffs2.Magic.le:
                pass
                self._is_le = True
            elif _on == Jffs2.Magic.be:
                pass
                self._is_le = False
            if not hasattr(self, '_is_le'):
                raise kaitaistruct.UndecidedEndiannessError("/types/inode_header")
            elif self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()

        def _read_le(self):
            self._debug['inode_type']['start'] = self._io.pos()
            self.inode_type = KaitaiStream.resolve_enum(Jffs2.InodeType, self._io.read_u2le())
            self._debug['inode_type']['end'] = self._io.pos()
            self._debug['len_inode']['start'] = self._io.pos()
            self.len_inode = self._io.read_u4le()
            self._debug['len_inode']['end'] = self._io.pos()

        def _read_be(self):
            self._debug['inode_type']['start'] = self._io.pos()
            self.inode_type = KaitaiStream.resolve_enum(Jffs2.InodeType, self._io.read_u2be())
            self._debug['inode_type']['end'] = self._io.pos()
            self._debug['len_inode']['start'] = self._io.pos()
            self.len_inode = self._io.read_u4be()
            self._debug['len_inode']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



