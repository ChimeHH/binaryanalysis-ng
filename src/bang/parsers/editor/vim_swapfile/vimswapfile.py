# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Vimswapfile(KaitaiStruct):
    """Vim swap file, see `runtime/doc/recover.txt` in the Vim source code and
    `block0` in `memline.c`
    """
    SEQ_FIELDS = ["header", "header_padding", "blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Vimswapfile, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Vimswapfile.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['header_padding']['start'] = self._io.pos()
        self.header_padding = self._io.read_bytes(self.header.len_page - 1023)
        self._debug['header_padding']['end'] = self._io.pos()
        self._debug['blocks']['start'] = self._io.pos()
        self._debug['blocks']['arr'] = []
        self._raw_blocks = []
        self.blocks = []
        i = 0
        while not self._io.is_eof():
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            self._raw_blocks.append(self._io.read_bytes(self.header.len_page))
            _io__raw_blocks = KaitaiStream(BytesIO(self._raw_blocks[-1]))
            self.blocks.append(Vimswapfile.Block(_io__raw_blocks, self, self._root))
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['blocks']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.blocks)):
            pass
            self.blocks[i]._fetch_instances()


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["magic", "block_contents"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vimswapfile.Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['magic']['end'] = self._io.pos()
            if not  ((self.magic == u"ad") or (self.magic == u"tp")) :
                raise kaitaistruct.ValidationNotAnyOfError(self.magic, self._io, u"/types/block/seq/0")
            self._debug['block_contents']['start'] = self._io.pos()
            _on = self.magic
            if _on == u"ad":
                pass
                self.block_contents = Vimswapfile.DataBlock(self._io, self, self._root)
            elif _on == u"tp":
                pass
                self.block_contents = Vimswapfile.PointerBlock(self._io, self, self._root)
            self._debug['block_contents']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.magic
            if _on == u"ad":
                pass
                self.block_contents._fetch_instances()
            elif _on == u"tp":
                pass
                self.block_contents._fetch_instances()


    class DataBlock(KaitaiStruct):
        SEQ_FIELDS = ["free_space", "text_start", "text_end"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vimswapfile.DataBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['free_space']['start'] = self._io.pos()
            self.free_space = self._io.read_u4le()
            self._debug['free_space']['end'] = self._io.pos()
            self._debug['text_start']['start'] = self._io.pos()
            self.text_start = self._io.read_u4le()
            self._debug['text_start']['end'] = self._io.pos()
            self._debug['text_end']['start'] = self._io.pos()
            self.text_end = self._io.read_u4le()
            self._debug['text_end']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "len_page", "mtime", "inode", "pid", "user_name", "host_name", "file_name", "magic_long", "magic_int", "magic_short", "magic_char"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vimswapfile.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x62\x30":
                raise kaitaistruct.ValidationNotEqualError(b"\x62\x30", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self._raw_version = self._io.read_bytes(10)
            _io__raw_version = KaitaiStream(BytesIO(self._raw_version))
            self.version = Vimswapfile.Version(_io__raw_version, self, self._root)
            self._debug['version']['end'] = self._io.pos()
            self._debug['len_page']['start'] = self._io.pos()
            self.len_page = self._io.read_u4le()
            self._debug['len_page']['end'] = self._io.pos()
            self._debug['mtime']['start'] = self._io.pos()
            self.mtime = self._io.read_bytes(4)
            self._debug['mtime']['end'] = self._io.pos()
            self._debug['inode']['start'] = self._io.pos()
            self.inode = self._io.read_u4le()
            self._debug['inode']['end'] = self._io.pos()
            self._debug['pid']['start'] = self._io.pos()
            self.pid = self._io.read_u4le()
            self._debug['pid']['end'] = self._io.pos()
            self._debug['user_name']['start'] = self._io.pos()
            self.user_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(40), 0, False)).decode(u"ASCII")
            self._debug['user_name']['end'] = self._io.pos()
            self._debug['host_name']['start'] = self._io.pos()
            self.host_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(40), 0, False)).decode(u"ASCII")
            self._debug['host_name']['end'] = self._io.pos()
            self._debug['file_name']['start'] = self._io.pos()
            self.file_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(900), 0, False)).decode(u"ASCII")
            self._debug['file_name']['end'] = self._io.pos()
            self._debug['magic_long']['start'] = self._io.pos()
            self.magic_long = self._io.read_u8le()
            self._debug['magic_long']['end'] = self._io.pos()
            self._debug['magic_int']['start'] = self._io.pos()
            self.magic_int = self._io.read_u4le()
            self._debug['magic_int']['end'] = self._io.pos()
            self._debug['magic_short']['start'] = self._io.pos()
            self.magic_short = self._io.read_u2le()
            self._debug['magic_short']['end'] = self._io.pos()
            self._debug['magic_char']['start'] = self._io.pos()
            self.magic_char = self._io.read_bytes(1)
            self._debug['magic_char']['end'] = self._io.pos()
            if not self.magic_char == b"\x55":
                raise kaitaistruct.ValidationNotEqualError(b"\x55", self.magic_char, self._io, u"/types/header/seq/12")


        def _fetch_instances(self):
            pass
            self.version._fetch_instances()


    class PointerBlock(KaitaiStruct):
        SEQ_FIELDS = ["num_pointer", "pointer_count_max"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vimswapfile.PointerBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_pointer']['start'] = self._io.pos()
            self.num_pointer = self._io.read_u2le()
            self._debug['num_pointer']['end'] = self._io.pos()
            self._debug['pointer_count_max']['start'] = self._io.pos()
            self.pointer_count_max = self._io.read_u2le()
            self._debug['pointer_count_max']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PointerEntry(KaitaiStruct):
        SEQ_FIELDS = ["block_number", "line_number", "old_line_number", "page_count"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vimswapfile.PointerEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['block_number']['start'] = self._io.pos()
            self.block_number = self._io.read_u8le()
            self._debug['block_number']['end'] = self._io.pos()
            self._debug['line_number']['start'] = self._io.pos()
            self.line_number = self._io.read_u8le()
            self._debug['line_number']['end'] = self._io.pos()
            self._debug['old_line_number']['start'] = self._io.pos()
            self.old_line_number = self._io.read_u8le()
            self._debug['old_line_number']['end'] = self._io.pos()
            self._debug['page_count']['start'] = self._io.pos()
            self.page_count = self._io.read_u4le()
            self._debug['page_count']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Version(KaitaiStruct):
        SEQ_FIELDS = ["vim", "major", "dot", "minor"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vimswapfile.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['vim']['start'] = self._io.pos()
            self.vim = self._io.read_bytes(4)
            self._debug['vim']['end'] = self._io.pos()
            if not self.vim == b"\x56\x49\x4D\x20":
                raise kaitaistruct.ValidationNotEqualError(b"\x56\x49\x4D\x20", self.vim, self._io, u"/types/version/seq/0")
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u1()
            self._debug['major']['end'] = self._io.pos()
            self._debug['dot']['start'] = self._io.pos()
            self.dot = self._io.read_bytes(1)
            self._debug['dot']['end'] = self._io.pos()
            if not self.dot == b"\x2E":
                raise kaitaistruct.ValidationNotEqualError(b"\x2E", self.dot, self._io, u"/types/version/seq/2")
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u1()
            self._debug['minor']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



