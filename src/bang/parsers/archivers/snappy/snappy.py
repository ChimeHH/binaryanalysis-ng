# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Snappy(KaitaiStruct):
    """snappy's framing2 format
    
    Test files can be created with snzip: <https://github.com/kubo/snzip>
    
    .. seealso::
       Source - https://github.com/google/snappy/blob/main/framing_format.txt
    """

    class ChunkTypes(IntEnum):
        compressed = 0
        uncompressed = 1
        padding = 254
        stream_identifier = 255
    SEQ_FIELDS = ["chunks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Snappy, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['chunks']['start'] = self._io.pos()
        self._debug['chunks']['arr'] = []
        self.chunks = []
        i = 0
        while True:
            self._debug['chunks']['arr'].append({'start': self._io.pos()})
            _ = Snappy.Chunk(self._io, self, self._root)
            self.chunks.append(_)
            self._debug['chunks']['arr'][len(self.chunks) - 1]['end'] = self._io.pos()
            if  ((self._io.is_eof()) or ((not (_.is_valid)))) :
                break
            i += 1
        self._debug['chunks']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.chunks)):
            pass
            self.chunks[i]._fetch_instances()


    class Chunk(KaitaiStruct):
        SEQ_FIELDS = ["identifier", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Snappy.Chunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['identifier']['start'] = self._io.pos()
            self.identifier = KaitaiStream.resolve_enum(Snappy.ChunkTypes, self._io.read_u1())
            self._debug['identifier']['end'] = self._io.pos()
            if self.is_valid:
                pass
                self._debug['body']['start'] = self._io.pos()
                self.body = Snappy.ChunkBody(self._io, self, self._root)
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

            self._m_is_valid =  ((self.identifier == Snappy.ChunkTypes.compressed) or (self.identifier == Snappy.ChunkTypes.uncompressed) or (self.identifier == Snappy.ChunkTypes.padding) or (self.identifier == Snappy.ChunkTypes.stream_identifier)) 
            return getattr(self, '_m_is_valid', None)


    class ChunkBody(KaitaiStruct):
        SEQ_FIELDS = ["len_chunk", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Snappy.ChunkBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_chunk']['start'] = self._io.pos()
            self.len_chunk = Snappy.Int3(self._io, self, self._root)
            self._debug['len_chunk']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_chunk.value)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.len_chunk._fetch_instances()


    class Int3(KaitaiStruct):
        SEQ_FIELDS = ["lower", "higher"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Snappy.Int3, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['lower']['start'] = self._io.pos()
            self.lower = self._io.read_u2le()
            self._debug['lower']['end'] = self._io.pos()
            self._debug['higher']['start'] = self._io.pos()
            self.higher = self._io.read_u1()
            self._debug['higher']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.higher * 65536 + self.lower
            return getattr(self, '_m_value', None)



