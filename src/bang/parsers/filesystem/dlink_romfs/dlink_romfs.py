# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class DlinkRomfs(KaitaiStruct):
    """File system used by D-Link in certain routers, such as DIR-600. This is
    apparently a modified version of the romfs file system used in eCos.
    
    .. seealso::
       Source - https://raw.githubusercontent.com/ReFirmLabs/binwalk/ec47069/src/binwalk/plugins/dlromfsextract.py
    
    
    .. seealso::
       Source - http://web.archive.org/web/20201208093903/https://github.com/syschmod/dlink_patch_utils/wiki/D-Link-GO-RT-N150---vulnerabilities-and-firmware-modification
    
    
    .. seealso::
       Source - https://github.com/antmicro/ecos-openrisc/blob/0891c1c/packages/fs/rom/current/src/romfs.c
    """
    SEQ_FIELDS = ["super_block", "entries"]
    def __init__(self, _io, _parent=None, _root=None):
        super(DlinkRomfs, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['super_block']['start'] = self._io.pos()
        self._raw_super_block = self._io.read_bytes(32)
        _io__raw_super_block = KaitaiStream(BytesIO(self._raw_super_block))
        self.super_block = DlinkRomfs.SuperBlock(_io__raw_super_block, self, self._root)
        self._debug['super_block']['end'] = self._io.pos()
        self._debug['entries']['start'] = self._io.pos()
        self._debug['entries']['arr'] = []
        self.entries = []
        for i in range(self.super_block.num_entries):
            self._debug['entries']['arr'].append({'start': self._io.pos()})
            self.entries.append(DlinkRomfs.Entry(self._io, self, self._root))
            self._debug['entries']['arr'][i]['end'] = self._io.pos()

        self._debug['entries']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.super_block._fetch_instances()
        for i in range(len(self.entries)):
            pass
            self.entries[i]._fetch_instances()


    class DirEntries(KaitaiStruct):
        SEQ_FIELDS = ["dir_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DlinkRomfs.DirEntries, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['dir_entries']['start'] = self._io.pos()
            self._debug['dir_entries']['arr'] = []
            self.dir_entries = []
            i = 0
            while not self._io.is_eof():
                self._debug['dir_entries']['arr'].append({'start': self._io.pos()})
                self.dir_entries.append(DlinkRomfs.DirEntry(self._io, self, self._root))
                self._debug['dir_entries']['arr'][len(self.dir_entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['dir_entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.dir_entries)):
                pass
                self.dir_entries[i]._fetch_instances()



    class DirEntry(KaitaiStruct):
        SEQ_FIELDS = ["directory_id", "next", "name", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DlinkRomfs.DirEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['directory_id']['start'] = self._io.pos()
            self.directory_id = self._io.read_u4le()
            self._debug['directory_id']['end'] = self._io.pos()
            self._debug['next']['start'] = self._io.pos()
            self.next = self._io.read_u4le()
            self._debug['next']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(self.next - self._parent._io.pos())
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Entry(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/antmicro/ecos-openrisc/blob/0891c1c/packages/fs/rom/current/src/romfs.c#L273
        """
        SEQ_FIELDS = ["entry_type", "num_links", "owner", "group", "len_entry", "ctime", "ofs_entry", "len_decompressed", "entry_id_block"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DlinkRomfs.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entry_type']['start'] = self._io.pos()
            self.entry_type = self._io.read_u4le()
            self._debug['entry_type']['end'] = self._io.pos()
            self._debug['num_links']['start'] = self._io.pos()
            self.num_links = self._io.read_u4le()
            self._debug['num_links']['end'] = self._io.pos()
            self._debug['owner']['start'] = self._io.pos()
            self.owner = self._io.read_u2le()
            self._debug['owner']['end'] = self._io.pos()
            self._debug['group']['start'] = self._io.pos()
            self.group = self._io.read_u2le()
            self._debug['group']['end'] = self._io.pos()
            self._debug['len_entry']['start'] = self._io.pos()
            self.len_entry = self._io.read_u4le()
            self._debug['len_entry']['end'] = self._io.pos()
            self._debug['ctime']['start'] = self._io.pos()
            self.ctime = self._io.read_u4le()
            self._debug['ctime']['end'] = self._io.pos()
            self._debug['ofs_entry']['start'] = self._io.pos()
            self.ofs_entry = self._io.read_u4le()
            self._debug['ofs_entry']['end'] = self._io.pos()
            if self._root.super_block.signature.version.major == 9:
                pass
                self._debug['len_decompressed']['start'] = self._io.pos()
                self.len_decompressed = self._io.read_u4le()
                self._debug['len_decompressed']['end'] = self._io.pos()

            self._debug['entry_id_block']['start'] = self._io.pos()
            _on = self._root.super_block.signature.version.major
            if _on == 1:
                pass
                self.entry_id_block = DlinkRomfs.EntryIdBlockV1(self._io, self, self._root)
            elif _on == 9:
                pass
                self.entry_id_block = DlinkRomfs.EntryIdBlockV9(self._io, self, self._root)
            self._debug['entry_id_block']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            if self._root.super_block.signature.version.major == 9:
                pass

            _on = self._root.super_block.signature.version.major
            if _on == 1:
                pass
                self.entry_id_block._fetch_instances()
            elif _on == 9:
                pass
                self.entry_id_block._fetch_instances()
            _ = self.data
            if hasattr(self, '_m_data'):
                pass
                _on = self.is_directory
                if _on == True:
                    pass
                    self._m_data._fetch_instances()
                else:
                    pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            _pos = self._io.pos()
            self._io.seek(self.ofs_entry)
            self._debug['_m_data']['start'] = self._io.pos()
            _on = self.is_directory
            if _on == True:
                pass
                self._raw__m_data = self._io.read_bytes(self.len_entry)
                _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
                self._m_data = DlinkRomfs.DirEntries(_io__raw__m_data, self, self._root)
            else:
                pass
                self._m_data = self._io.read_bytes(self.len_entry)
            self._debug['_m_data']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_data', None)

        @property
        def is_block_device(self):
            if hasattr(self, '_m_is_block_device'):
                return self._m_is_block_device

            self._m_is_block_device = self.entry_type & 4 == 4
            return getattr(self, '_m_is_block_device', None)

        @property
        def is_character_device(self):
            if hasattr(self, '_m_is_character_device'):
                return self._m_is_character_device

            self._m_is_character_device = self.entry_type & 2 == 2
            return getattr(self, '_m_is_character_device', None)

        @property
        def is_compressed(self):
            if hasattr(self, '_m_is_compressed'):
                return self._m_is_compressed

            if self._root.super_block.signature.version.major == 9:
                pass
                self._m_is_compressed = self.len_decompressed != 0

            return getattr(self, '_m_is_compressed', None)

        @property
        def is_directory(self):
            if hasattr(self, '_m_is_directory'):
                return self._m_is_directory

            self._m_is_directory = self.entry_type & 1 == 1
            return getattr(self, '_m_is_directory', None)

        @property
        def is_fifo(self):
            if hasattr(self, '_m_is_fifo'):
                return self._m_is_fifo

            self._m_is_fifo = self.entry_type & 16 == 16
            return getattr(self, '_m_is_fifo', None)

        @property
        def is_regular(self):
            if hasattr(self, '_m_is_regular'):
                return self._m_is_regular

            self._m_is_regular = self.entry_type & 8 == 8
            return getattr(self, '_m_is_regular', None)

        @property
        def is_symlink(self):
            """https://github.com/antmicro/ecos-openrisc/blob/0891c1c/packages/fs/rom/current/support/mk_romfs.c#L94."""
            if hasattr(self, '_m_is_symlink'):
                return self._m_is_symlink

            self._m_is_symlink = (not ( ((self.is_directory) or (self.is_character_device) or (self.is_block_device) or (self.is_regular) or (self.is_fifo)) ))
            return getattr(self, '_m_is_symlink', None)


    class EntryIdBlockV1(KaitaiStruct):
        SEQ_FIELDS = ["open_bracket", "entry_id_str", "closing_bracket"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DlinkRomfs.EntryIdBlockV1, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['open_bracket']['start'] = self._io.pos()
            self.open_bracket = self._io.read_bytes(1)
            self._debug['open_bracket']['end'] = self._io.pos()
            if not self.open_bracket == b"\x3C":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C", self.open_bracket, self._io, u"/types/entry_id_block_v1/seq/0")
            self._debug['entry_id_str']['start'] = self._io.pos()
            self.entry_id_str = (self._io.read_bytes(6)).decode(u"ASCII")
            self._debug['entry_id_str']['end'] = self._io.pos()
            self._debug['closing_bracket']['start'] = self._io.pos()
            self.closing_bracket = self._io.read_bytes(1)
            self._debug['closing_bracket']['end'] = self._io.pos()
            if not self.closing_bracket == b"\x3E":
                raise kaitaistruct.ValidationNotEqualError(b"\x3E", self.closing_bracket, self._io, u"/types/entry_id_block_v1/seq/2")


        def _fetch_instances(self):
            pass

        @property
        def entry_id(self):
            if hasattr(self, '_m_entry_id'):
                return self._m_entry_id

            self._m_entry_id = int(self.entry_id_str)
            return getattr(self, '_m_entry_id', None)


    class EntryIdBlockV9(KaitaiStruct):
        SEQ_FIELDS = ["entry_id_str"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DlinkRomfs.EntryIdBlockV9, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entry_id_str']['start'] = self._io.pos()
            self.entry_id_str = (self._io.read_bytes(4)).decode(u"ASCII")
            self._debug['entry_id_str']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def entry_id(self):
            if hasattr(self, '_m_entry_id'):
                return self._m_entry_id

            self._m_entry_id = int(self.entry_id_str)
            return getattr(self, '_m_entry_id', None)


    class Signature(KaitaiStruct):
        SEQ_FIELDS = ["romfs_name", "version"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DlinkRomfs.Signature, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['romfs_name']['start'] = self._io.pos()
            self.romfs_name = self._io.read_bytes(7)
            self._debug['romfs_name']['end'] = self._io.pos()
            if not self.romfs_name == b"\x52\x4F\x4D\x46\x53\x20\x76":
                raise kaitaistruct.ValidationNotEqualError(b"\x52\x4F\x4D\x46\x53\x20\x76", self.romfs_name, self._io, u"/types/signature/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self._raw_version = self._io.read_bytes(3)
            _io__raw_version = KaitaiStream(BytesIO(self._raw_version))
            self.version = DlinkRomfs.Version(_io__raw_version, self, self._root)
            self._debug['version']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.version._fetch_instances()


    class SuperBlock(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/antmicro/ecos-openrisc/blob/0891c1c/packages/fs/rom/current/src/romfs.c#L302
        """
        SEQ_FIELDS = ["magic", "num_entries", "unknown1", "unknown2", "signature"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DlinkRomfs.SuperBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x2E\x6D\x6F\x52":
                raise kaitaistruct.ValidationNotEqualError(b"\x2E\x6D\x6F\x52", self.magic, self._io, u"/types/super_block/seq/0")
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u4le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u4le()
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_u4le()
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['signature']['start'] = self._io.pos()
            self._raw_signature = self._io.read_bytes(16)
            _io__raw_signature = KaitaiStream(BytesIO(self._raw_signature))
            self.signature = DlinkRomfs.Signature(_io__raw_signature, self, self._root)
            self._debug['signature']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.signature._fetch_instances()


    class Version(KaitaiStruct):
        SEQ_FIELDS = ["major_version", "separator", "minor_version"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DlinkRomfs.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['major_version']['start'] = self._io.pos()
            self.major_version = (self._io.read_bytes(1)).decode(u"ASCII")
            self._debug['major_version']['end'] = self._io.pos()
            self._debug['separator']['start'] = self._io.pos()
            self.separator = self._io.read_bytes(1)
            self._debug['separator']['end'] = self._io.pos()
            if not self.separator == b"\x2E":
                raise kaitaistruct.ValidationNotEqualError(b"\x2E", self.separator, self._io, u"/types/version/seq/1")
            self._debug['minor_version']['start'] = self._io.pos()
            self.minor_version = (self._io.read_bytes(1)).decode(u"ASCII")
            self._debug['minor_version']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def major(self):
            if hasattr(self, '_m_major'):
                return self._m_major

            self._m_major = int(self.major_version)
            return getattr(self, '_m_major', None)

        @property
        def minor(self):
            if hasattr(self, '_m_minor'):
                return self._m_minor

            self._m_minor = int(self.minor_version)
            return getattr(self, '_m_minor', None)



