# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Romfs(KaitaiStruct):
    """
    .. seealso::
       Source - https://www.kernel.org/doc/Documentation/filesystems/romfs.rst
    """

    class Filetypes(IntEnum):
        hardlink = 0
        directory = 1
        regular_file = 2
        symbolic_link = 3
        block_device = 4
        character_device = 5
        socket = 6
        fifo = 7
    SEQ_FIELDS = ["magic", "len_file", "checksum", "volume_name", "padding", "files"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Romfs, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(8)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x2D\x72\x6F\x6D\x31\x66\x73\x2D":
            raise kaitaistruct.ValidationNotEqualError(b"\x2D\x72\x6F\x6D\x31\x66\x73\x2D", self.magic, self._io, u"/seq/0")
        self._debug['len_file']['start'] = self._io.pos()
        self.len_file = self._io.read_u4be()
        self._debug['len_file']['end'] = self._io.pos()
        self._debug['checksum']['start'] = self._io.pos()
        self.checksum = self._io.read_u4be()
        self._debug['checksum']['end'] = self._io.pos()
        self._debug['volume_name']['start'] = self._io.pos()
        self.volume_name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
        self._debug['volume_name']['end'] = self._io.pos()
        self._debug['padding']['start'] = self._io.pos()
        self.padding = self._io.read_bytes(-(self._io.pos()) % 16)
        self._debug['padding']['end'] = self._io.pos()
        self._debug['files']['start'] = self._io.pos()
        self._raw_files = self._io.read_bytes(self.len_file - self._io.pos())
        _io__raw_files = KaitaiStream(BytesIO(self._raw_files))
        self.files = Romfs.Files(_io__raw_files, self, self._root)
        self._debug['files']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.files._fetch_instances()

    class Fileheader(KaitaiStruct):
        SEQ_FIELDS = ["next_fileheader_and_flags", "spec_info", "len_file", "checksum", "name", "padding1", "data", "padding2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Romfs.Fileheader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['next_fileheader_and_flags']['start'] = self._io.pos()
            self.next_fileheader_and_flags = self._io.read_u4be()
            self._debug['next_fileheader_and_flags']['end'] = self._io.pos()
            self._debug['spec_info']['start'] = self._io.pos()
            self.spec_info = self._io.read_u4be()
            self._debug['spec_info']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4be()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_u4be()
            self._debug['checksum']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['padding1']['start'] = self._io.pos()
            self.padding1 = self._io.read_bytes(-(self._io.pos()) % 16)
            self._debug['padding1']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_file)
            self._debug['data']['end'] = self._io.pos()
            self._debug['padding2']['start'] = self._io.pos()
            self.padding2 = self._io.read_bytes(-(self._io.pos()) % 16)
            self._debug['padding2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def executable(self):
            if hasattr(self, '_m_executable'):
                return self._m_executable

            self._m_executable = self.next_fileheader_and_flags & 8 == 8
            return getattr(self, '_m_executable', None)

        @property
        def filetype(self):
            if hasattr(self, '_m_filetype'):
                return self._m_filetype

            self._m_filetype = KaitaiStream.resolve_enum(Romfs.Filetypes, self.next_fileheader_and_flags & 7)
            return getattr(self, '_m_filetype', None)

        @property
        def next_fileheader(self):
            if hasattr(self, '_m_next_fileheader'):
                return self._m_next_fileheader

            self._m_next_fileheader = self.next_fileheader_and_flags & 4294967280
            return getattr(self, '_m_next_fileheader', None)


    class Files(KaitaiStruct):
        SEQ_FIELDS = ["files"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Romfs.Files, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['files']['start'] = self._io.pos()
            self._debug['files']['arr'] = []
            self.files = []
            i = 0
            while True:
                self._debug['files']['arr'].append({'start': self._io.pos()})
                _ = Romfs.Fileheader(self._io, self, self._root)
                self.files.append(_)
                self._debug['files']['arr'][len(self.files) - 1]['end'] = self._io.pos()
                if self._io.is_eof():
                    break
                i += 1
            self._debug['files']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.files)):
                pass
                self.files[i]._fetch_instances()



    @property
    def files_offset(self):
        if hasattr(self, '_m_files_offset'):
            return self._m_files_offset

        self._m_files_offset = ((((8 + 4) + 4) + len(self.volume_name)) + 1) + len(self.padding)
        return getattr(self, '_m_files_offset', None)


