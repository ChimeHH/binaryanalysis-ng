# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Lz4(KaitaiStruct):
    """This specification describes a single LZ4 frame.
    
    The original LZ4 frame format specification has the following notice:
    
    Copyright (c) 2013-2020 Yann Collet
    
    Permission is granted to copy and distribute this document for any purpose and
    without charge, including translations into other languages and incorporation
    into compilations, provided that the copyright notice and this notice are preserved,
    and that any substantive changes or deletions from the original are clearly
    marked. Distribution of this document is unlimited.
    
    .. seealso::
       Source - https://github.com/lz4/lz4/blob/dev/doc/lz4_Frame_format.md
    """
    SEQ_FIELDS = ["magic", "frame_descriptor", "blocks", "content_checksum"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Lz4, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_u4le()
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == 407708164:
            raise kaitaistruct.ValidationNotEqualError(407708164, self.magic, self._io, u"/seq/0")
        self._debug['frame_descriptor']['start'] = self._io.pos()
        self.frame_descriptor = Lz4.FrameDescriptor(self._io, self, self._root)
        self._debug['frame_descriptor']['end'] = self._io.pos()
        self._debug['blocks']['start'] = self._io.pos()
        self._debug['blocks']['arr'] = []
        self.blocks = []
        i = 0
        while True:
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            _ = Lz4.Block(self._io, self, self._root)
            self.blocks.append(_)
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            if _.is_endmark:
                break
            i += 1
        self._debug['blocks']['end'] = self._io.pos()
        if self.frame_descriptor.flag.content_checksum:
            pass
            self._debug['content_checksum']['start'] = self._io.pos()
            self.content_checksum = self._io.read_u4le()
            self._debug['content_checksum']['end'] = self._io.pos()



    def _fetch_instances(self):
        pass
        self.frame_descriptor._fetch_instances()
        for i in range(len(self.blocks)):
            pass
            self.blocks[i]._fetch_instances()

        if self.frame_descriptor.flag.content_checksum:
            pass


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["len_block", "uncompressed", "data", "checksum"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Lz4.Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_block']['start'] = self._io.pos()
            self.len_block = self._io.read_bits_int_le(31)
            self._debug['len_block']['end'] = self._io.pos()
            self._debug['uncompressed']['start'] = self._io.pos()
            self.uncompressed = self._io.read_bits_int_le(1) != 0
            self._debug['uncompressed']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_block)
            self._debug['data']['end'] = self._io.pos()
            if  ((self._root.frame_descriptor.flag.block_checksum) and ((not (self.is_endmark)))) :
                pass
                self._debug['checksum']['start'] = self._io.pos()
                self.checksum = self._io.read_u4le()
                self._debug['checksum']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if  ((self._root.frame_descriptor.flag.block_checksum) and ((not (self.is_endmark)))) :
                pass


        @property
        def is_endmark(self):
            if hasattr(self, '_m_is_endmark'):
                return self._m_is_endmark

            self._m_is_endmark =  (((not (self.uncompressed))) and (self.len_block == 0)) 
            return getattr(self, '_m_is_endmark', None)


    class FrameDescriptor(KaitaiStruct):
        SEQ_FIELDS = ["flag", "bd", "content_size", "dictionary_id", "header_checksum"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Lz4.FrameDescriptor, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flag']['start'] = self._io.pos()
            self.flag = Lz4.FrameDescriptor.Flag(self._io, self, self._root)
            self._debug['flag']['end'] = self._io.pos()
            self._debug['bd']['start'] = self._io.pos()
            self.bd = Lz4.FrameDescriptor.Bd(self._io, self, self._root)
            self._debug['bd']['end'] = self._io.pos()
            if self.flag.content_size:
                pass
                self._debug['content_size']['start'] = self._io.pos()
                self.content_size = self._io.read_u8le()
                self._debug['content_size']['end'] = self._io.pos()

            if self.flag.dictionary_id:
                pass
                self._debug['dictionary_id']['start'] = self._io.pos()
                self.dictionary_id = self._io.read_u4le()
                self._debug['dictionary_id']['end'] = self._io.pos()

            self._debug['header_checksum']['start'] = self._io.pos()
            self.header_checksum = self._io.read_u1()
            self._debug['header_checksum']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.flag._fetch_instances()
            self.bd._fetch_instances()
            if self.flag.content_size:
                pass

            if self.flag.dictionary_id:
                pass


        class Bd(KaitaiStruct):
            SEQ_FIELDS = ["reserved", "block_maxsize", "reserved2"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Lz4.FrameDescriptor.Bd, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_bits_int_be(1) != 0
                self._debug['reserved']['end'] = self._io.pos()
                if not self.reserved == False:
                    raise kaitaistruct.ValidationNotEqualError(False, self.reserved, self._io, u"/types/frame_descriptor/types/bd/seq/0")
                self._debug['block_maxsize']['start'] = self._io.pos()
                self.block_maxsize = self._io.read_bits_int_be(3)
                self._debug['block_maxsize']['end'] = self._io.pos()
                if not  ((self.block_maxsize == 4) or (self.block_maxsize == 5) or (self.block_maxsize == 6) or (self.block_maxsize == 7)) :
                    raise kaitaistruct.ValidationNotAnyOfError(self.block_maxsize, self._io, u"/types/frame_descriptor/types/bd/seq/1")
                self._debug['reserved2']['start'] = self._io.pos()
                self.reserved2 = self._io.read_bits_int_be(4)
                self._debug['reserved2']['end'] = self._io.pos()
                if not self.reserved2 == 0:
                    raise kaitaistruct.ValidationNotEqualError(0, self.reserved2, self._io, u"/types/frame_descriptor/types/bd/seq/2")


            def _fetch_instances(self):
                pass


        class Flag(KaitaiStruct):
            SEQ_FIELDS = ["version", "block_independence", "block_checksum", "content_size", "content_checksum", "reserved", "dictionary_id"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Lz4.FrameDescriptor.Flag, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['version']['start'] = self._io.pos()
                self.version = self._io.read_bits_int_be(2)
                self._debug['version']['end'] = self._io.pos()
                self._debug['block_independence']['start'] = self._io.pos()
                self.block_independence = self._io.read_bits_int_be(1) != 0
                self._debug['block_independence']['end'] = self._io.pos()
                self._debug['block_checksum']['start'] = self._io.pos()
                self.block_checksum = self._io.read_bits_int_be(1) != 0
                self._debug['block_checksum']['end'] = self._io.pos()
                self._debug['content_size']['start'] = self._io.pos()
                self.content_size = self._io.read_bits_int_be(1) != 0
                self._debug['content_size']['end'] = self._io.pos()
                self._debug['content_checksum']['start'] = self._io.pos()
                self.content_checksum = self._io.read_bits_int_be(1) != 0
                self._debug['content_checksum']['end'] = self._io.pos()
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_bits_int_be(1) != 0
                self._debug['reserved']['end'] = self._io.pos()
                if not self.reserved == False:
                    raise kaitaistruct.ValidationNotEqualError(False, self.reserved, self._io, u"/types/frame_descriptor/types/flag/seq/5")
                self._debug['dictionary_id']['start'] = self._io.pos()
                self.dictionary_id = self._io.read_bits_int_be(1) != 0
                self._debug['dictionary_id']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass




