# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SerializedJava(KaitaiStruct):
    """
    .. seealso::
       Source - https://docs.oracle.com/javase/8/docs/platform/serialization/spec/protocol.html
    """

    class Symbols(IntEnum):
        null_symbol = 112
        reference = 113
        class_description = 114
        object_symbol = 115
        string_symbol = 116
        array_symbol = 117
        class_symbol = 118
        block_data = 119
        end_block_data = 120
        reset = 121
        block_data_long = 122
        exception_symbol = 123
        long_string = 124
        proxy_class_description = 125
        enum_symbol = 126
    SEQ_FIELDS = ["magic", "version", "blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SerializedJava, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(2)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\xAC\xED":
            raise kaitaistruct.ValidationNotEqualError(b"\xAC\xED", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u2be()
        self._debug['version']['end'] = self._io.pos()
        if not self.version == 5:
            raise kaitaistruct.ValidationNotEqualError(5, self.version, self._io, u"/seq/1")
        self._debug['blocks']['start'] = self._io.pos()
        self._debug['blocks']['arr'] = []
        self.blocks = []
        i = 0
        while True:
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            _ = SerializedJava.Block(self._io, self, self._root)
            self.blocks.append(_)
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            if  ((self._io.is_eof()) or ((not (_.is_valid)))) :
                break
            i += 1
        self._debug['blocks']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.blocks)):
            pass
            self.blocks[i]._fetch_instances()


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["symbol", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SerializedJava.Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['symbol']['start'] = self._io.pos()
            self.symbol = KaitaiStream.resolve_enum(SerializedJava.Symbols, self._io.read_u1())
            self._debug['symbol']['end'] = self._io.pos()
            if self.is_valid:
                pass
                self._debug['body']['start'] = self._io.pos()
                self.body = SerializedJava.BlockBody(self._io, self, self._root)
                self._debug['body']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.is_valid:
                pass
                self.body._fetch_instances()


        @property
        def is_valid(self):
            if hasattr(self, '_m_is_valid'):
                return self._m_is_valid

            self._m_is_valid =  ((self.symbol == SerializedJava.Symbols.block_data) or (self.symbol == SerializedJava.Symbols.block_data_long)) 
            return getattr(self, '_m_is_valid', None)


    class BlockBody(KaitaiStruct):
        SEQ_FIELDS = ["len_data", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SerializedJava.BlockBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_data']['start'] = self._io.pos()
            _on = self._parent.symbol
            if _on == SerializedJava.Symbols.block_data:
                pass
                self.len_data = self._io.read_u1()
            elif _on == SerializedJava.Symbols.block_data_long:
                pass
                self.len_data = self._io.read_u4be()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self._parent.symbol
            if _on == SerializedJava.Symbols.block_data:
                pass
            elif _on == SerializedJava.Symbols.block_data_long:
                pass



