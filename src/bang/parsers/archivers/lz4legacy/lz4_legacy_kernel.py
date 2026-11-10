# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Lz4LegacyKernel(KaitaiStruct):
    """Specification has the following notice:
    
    Copyright (c) 2013-2020 Yann Collet
    
    Permission is granted to copy and distribute this document for any purpose and
    without charge, including translations into other languages and incorporation
    into compilations, provided that the copyright notice and this notice are preserved,
    and that any substantive changes or deletions from the original are clearly
    marked. Distribution of this document is unlimited.
    
    .. seealso::
       Source - https://github.com/lz4/lz4/blob/dev/doc/lz4_Frame_format.md#legacy-frame
    
    
    .. seealso::
       Source - https://github.com/armijnhemel/binaryanalysis-ng/issues/356
    """
    SEQ_FIELDS = ["magic", "blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Lz4LegacyKernel, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_u4le()
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == 407642370:
            raise kaitaistruct.ValidationNotEqualError(407642370, self.magic, self._io, u"/seq/0")
        self._debug['blocks']['start'] = self._io.pos()
        self._debug['blocks']['arr'] = []
        self.blocks = []
        i = 0
        while True:
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            _ = Lz4LegacyKernel.Block(self._io, self, self._root)
            self.blocks.append(_)
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            if  ((self._io.is_eof()) or (_.is_magic) or (self._io.size() - self._io.pos() <= 4)) :
                break
            i += 1
        self._debug['blocks']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.blocks)):
            pass
            self.blocks[i]._fetch_instances()


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["len_data", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Lz4LegacyKernel.Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            if (not (self.is_magic)):
                pass
                self._debug['data']['start'] = self._io.pos()
                self.data = self._io.read_bytes(self.len_data)
                self._debug['data']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if (not (self.is_magic)):
                pass


        @property
        def is_magic(self):
            if hasattr(self, '_m_is_magic'):
                return self._m_is_magic

            self._m_is_magic = self.len_data == 407642370
            return getattr(self, '_m_is_magic', None)



