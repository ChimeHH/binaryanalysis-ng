# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import riff
from .riff import *
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ani(KaitaiStruct):
    """This Kaitai implementation was adapted from the WAV Kaitai implementation,
    which was written by John Byrd of Gigantic Software
    (jbyrd@giganticsoftware.com), and it is likely to contain bugs.
    """

    class Fourcc(IntEnum):
        seq = 544302451
        riff = 1179011410
        acon = 1313817409
        icon = 1313817417
        info = 1330007625
        list = 1414744396
        data = 1635017060
        rate = 1702125938
        anih = 1751740001
    SEQ_FIELDS = ["chunk"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Ani, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['chunk']['start'] = self._io.pos()
        self.chunk = riff.Riff.Chunk(self._io)
        self._debug['chunk']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.chunk._fetch_instances()
        _ = self.parent_chunk_data
        if hasattr(self, '_m_parent_chunk_data'):
            pass
            self._m_parent_chunk_data._fetch_instances()

        _ = self.subchunks
        if hasattr(self, '_m_subchunks'):
            pass
            for i in range(len(self._m_subchunks)):
                pass
                self._m_subchunks[i]._fetch_instances()



    class ChunkType(KaitaiStruct):
        SEQ_FIELDS = ["chunk"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ani.ChunkType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['chunk']['start'] = self._io.pos()
            self.chunk = riff.Riff.Chunk(self._io)
            self._debug['chunk']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.chunk._fetch_instances()
            _ = self.chunk_data
            if hasattr(self, '_m_chunk_data'):
                pass
                _on = self.chunk_id
                if _on == Ani.Fourcc.data:
                    pass
                    self._m_chunk_data._fetch_instances()
                elif _on == Ani.Fourcc.list:
                    pass
                    self._m_chunk_data._fetch_instances()


        @property
        def chunk_data(self):
            if hasattr(self, '_m_chunk_data'):
                return self._m_chunk_data

            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_chunk_data']['start'] = io.pos()
            _on = self.chunk_id
            if _on == Ani.Fourcc.data:
                pass
                self._m_chunk_data = Ani.DataChunkType(io, self, self._root)
            elif _on == Ani.Fourcc.list:
                pass
                self._m_chunk_data = Ani.ListChunkType(io, self, self._root)
            self._debug['_m_chunk_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_chunk_data', None)

        @property
        def chunk_id(self):
            if hasattr(self, '_m_chunk_id'):
                return self._m_chunk_id

            self._m_chunk_id = KaitaiStream.resolve_enum(Ani.Fourcc, self.chunk.id)
            return getattr(self, '_m_chunk_id', None)


    class DataChunkType(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ani.DataChunkType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes_full()
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Dummy(KaitaiStruct):
        SEQ_FIELDS = ["dummy_id"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ani.Dummy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['dummy_id']['start'] = self._io.pos()
            self.dummy_id = riff.Riff(self._io)
            self._debug['dummy_id']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.dummy_id._fetch_instances()


    class InfoChunkType(KaitaiStruct):
        SEQ_FIELDS = ["chunk"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ani.InfoChunkType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['chunk']['start'] = self._io.pos()
            self.chunk = riff.Riff.Chunk(self._io)
            self._debug['chunk']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.chunk._fetch_instances()
            _ = self.chunk_data
            if hasattr(self, '_m_chunk_data'):
                pass


        @property
        def chunk_data(self):
            if hasattr(self, '_m_chunk_data'):
                return self._m_chunk_data

            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_chunk_data']['start'] = io.pos()
            self._m_chunk_data = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['_m_chunk_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_chunk_data', None)


    class ListChunkType(KaitaiStruct):
        SEQ_FIELDS = ["parent_chunk_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ani.ListChunkType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['parent_chunk_data']['start'] = self._io.pos()
            self.parent_chunk_data = riff.Riff.ParentChunkData(self._io)
            self._debug['parent_chunk_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.parent_chunk_data._fetch_instances()
            _ = self.subchunks
            if hasattr(self, '_m_subchunks'):
                pass
                for i in range(len(self._m_subchunks)):
                    pass
                    _on = self.form_type
                    if _on == Ani.Fourcc.info:
                        pass
                        self._m_subchunks[i]._fetch_instances()



        @property
        def form_type(self):
            if hasattr(self, '_m_form_type'):
                return self._m_form_type

            self._m_form_type = KaitaiStream.resolve_enum(Ani.Fourcc, self.parent_chunk_data.form_type)
            return getattr(self, '_m_form_type', None)

        @property
        def subchunks(self):
            if hasattr(self, '_m_subchunks'):
                return self._m_subchunks

            io = self.parent_chunk_data.subchunks_slot._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_subchunks']['start'] = io.pos()
            self._debug['_m_subchunks']['arr'] = []
            self._m_subchunks = []
            i = 0
            while not io.is_eof():
                self._debug['_m_subchunks']['arr'].append({'start': io.pos()})
                _on = self.form_type
                if _on == Ani.Fourcc.info:
                    pass
                    self._m_subchunks.append(Ani.InfoChunkType(io, self, self._root))
                self._debug['_m_subchunks']['arr'][len(self._m_subchunks) - 1]['end'] = io.pos()
                i += 1

            self._debug['_m_subchunks']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_subchunks', None)


    @property
    def chunk_id(self):
        if hasattr(self, '_m_chunk_id'):
            return self._m_chunk_id

        self._m_chunk_id = KaitaiStream.resolve_enum(Ani.Fourcc, self.chunk.id)
        return getattr(self, '_m_chunk_id', None)

    @property
    def form_type(self):
        if hasattr(self, '_m_form_type'):
            return self._m_form_type

        self._m_form_type = KaitaiStream.resolve_enum(Ani.Fourcc, self.parent_chunk_data.form_type)
        return getattr(self, '_m_form_type', None)

    @property
    def is_form_type_ani(self):
        if hasattr(self, '_m_is_form_type_ani'):
            return self._m_is_form_type_ani

        self._m_is_form_type_ani =  ((self.is_riff_chunk) and (self.form_type == Ani.Fourcc.acon)) 
        return getattr(self, '_m_is_form_type_ani', None)

    @property
    def is_riff_chunk(self):
        if hasattr(self, '_m_is_riff_chunk'):
            return self._m_is_riff_chunk

        self._m_is_riff_chunk = self.chunk_id == Ani.Fourcc.riff
        return getattr(self, '_m_is_riff_chunk', None)

    @property
    def parent_chunk_data(self):
        if hasattr(self, '_m_parent_chunk_data'):
            return self._m_parent_chunk_data

        if self.is_riff_chunk:
            pass
            io = self.chunk.data_slot._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_parent_chunk_data']['start'] = io.pos()
            self._m_parent_chunk_data = riff.Riff.ParentChunkData(io)
            self._debug['_m_parent_chunk_data']['end'] = io.pos()
            io.seek(_pos)

        return getattr(self, '_m_parent_chunk_data', None)

    @property
    def subchunks(self):
        if hasattr(self, '_m_subchunks'):
            return self._m_subchunks

        if self.is_form_type_ani:
            pass
            io = self.parent_chunk_data.subchunks_slot._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_subchunks']['start'] = io.pos()
            self._debug['_m_subchunks']['arr'] = []
            self._m_subchunks = []
            i = 0
            while not io.is_eof():
                self._debug['_m_subchunks']['arr'].append({'start': io.pos()})
                self._m_subchunks.append(Ani.ChunkType(io, self, self._root))
                self._debug['_m_subchunks']['arr'][len(self._m_subchunks) - 1]['end'] = io.pos()
                i += 1

            self._debug['_m_subchunks']['end'] = io.pos()
            io.seek(_pos)

        return getattr(self, '_m_subchunks', None)


