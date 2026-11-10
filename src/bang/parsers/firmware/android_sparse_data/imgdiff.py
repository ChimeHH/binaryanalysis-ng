# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Imgdiff(KaitaiStruct):
    """
    .. seealso::
       Source - https://android.googlesource.com/platform/bootable/recovery/+/d1ba38f7c96e74901779089fea6d09b0c7c2521d/applypatch/imgdiff.cpp#53
    """

    class ChunkTypes(IntEnum):
        normal = 0
        gzip = 1
        deflate = 2
        raw = 3
    SEQ_FIELDS = ["magic", "version", "num_chunks", "chunks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Imgdiff, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(7)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x49\x4D\x47\x44\x49\x46\x46":
            raise kaitaistruct.ValidationNotEqualError(b"\x49\x4D\x47\x44\x49\x46\x46", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u1()
        self._debug['version']['end'] = self._io.pos()
        if not  ((self.version == 49) or (self.version == 50)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/seq/1")
        self._debug['num_chunks']['start'] = self._io.pos()
        self.num_chunks = self._io.read_u4le()
        self._debug['num_chunks']['end'] = self._io.pos()
        self._debug['chunks']['start'] = self._io.pos()
        self._debug['chunks']['arr'] = []
        self.chunks = []
        for i in range(self.num_chunks):
            self._debug['chunks']['arr'].append({'start': self._io.pos()})
            self.chunks.append(Imgdiff.Chunk(self._io, self, self._root))
            self._debug['chunks']['arr'][i]['end'] = self._io.pos()

        self._debug['chunks']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.chunks)):
            pass
            self.chunks[i]._fetch_instances()


    class Bsdiff40(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_control_block", "len_diff_block", "len_new_file", "control_block", "diff_block"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Imgdiff.Bsdiff40, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x42\x53\x44\x49\x46\x46\x34\x30":
                raise kaitaistruct.ValidationNotEqualError(b"\x42\x53\x44\x49\x46\x46\x34\x30", self.magic, self._io, u"/types/bsdiff40/seq/0")
            self._debug['len_control_block']['start'] = self._io.pos()
            self.len_control_block = self._io.read_u8le()
            self._debug['len_control_block']['end'] = self._io.pos()
            self._debug['len_diff_block']['start'] = self._io.pos()
            self.len_diff_block = self._io.read_u8le()
            self._debug['len_diff_block']['end'] = self._io.pos()
            self._debug['len_new_file']['start'] = self._io.pos()
            self.len_new_file = self._io.read_u8le()
            self._debug['len_new_file']['end'] = self._io.pos()
            self._debug['control_block']['start'] = self._io.pos()
            self.control_block = self._io.read_bytes(self.len_control_block)
            self._debug['control_block']['end'] = self._io.pos()
            self._debug['diff_block']['start'] = self._io.pos()
            self.diff_block = self._io.read_bytes(self.len_diff_block)
            self._debug['diff_block']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Chunk(KaitaiStruct):
        SEQ_FIELDS = ["chunk_type", "chunk_body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Imgdiff.Chunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['chunk_type']['start'] = self._io.pos()
            self.chunk_type = KaitaiStream.resolve_enum(Imgdiff.ChunkTypes, self._io.read_u4le())
            self._debug['chunk_type']['end'] = self._io.pos()
            self._debug['chunk_body']['start'] = self._io.pos()
            _on = self.chunk_type
            if _on == Imgdiff.ChunkTypes.deflate:
                pass
                self.chunk_body = Imgdiff.ChunkDeflate(self._io, self, self._root)
            elif _on == Imgdiff.ChunkTypes.gzip:
                pass
                self.chunk_body = Imgdiff.ChunkGzip(self._io, self, self._root)
            elif _on == Imgdiff.ChunkTypes.normal:
                pass
                self.chunk_body = Imgdiff.ChunkNormal(self._io, self, self._root)
            elif _on == Imgdiff.ChunkTypes.raw:
                pass
                self.chunk_body = Imgdiff.ChunkRaw(self._io, self, self._root)
            self._debug['chunk_body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.chunk_type
            if _on == Imgdiff.ChunkTypes.deflate:
                pass
                self.chunk_body._fetch_instances()
            elif _on == Imgdiff.ChunkTypes.gzip:
                pass
                self.chunk_body._fetch_instances()
            elif _on == Imgdiff.ChunkTypes.normal:
                pass
                self.chunk_body._fetch_instances()
            elif _on == Imgdiff.ChunkTypes.raw:
                pass
                self.chunk_body._fetch_instances()


    class ChunkDeflate(KaitaiStruct):
        SEQ_FIELDS = ["ofs_source", "len_source", "ofs_bsdiff_patch", "len_expanded_source", "len_expanded_target", "gzip_info"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Imgdiff.ChunkDeflate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_source']['start'] = self._io.pos()
            self.ofs_source = self._io.read_u8le()
            self._debug['ofs_source']['end'] = self._io.pos()
            self._debug['len_source']['start'] = self._io.pos()
            self.len_source = self._io.read_u8le()
            self._debug['len_source']['end'] = self._io.pos()
            self._debug['ofs_bsdiff_patch']['start'] = self._io.pos()
            self.ofs_bsdiff_patch = self._io.read_u8le()
            self._debug['ofs_bsdiff_patch']['end'] = self._io.pos()
            self._debug['len_expanded_source']['start'] = self._io.pos()
            self.len_expanded_source = self._io.read_u8le()
            self._debug['len_expanded_source']['end'] = self._io.pos()
            self._debug['len_expanded_target']['start'] = self._io.pos()
            self.len_expanded_target = self._io.read_u8le()
            self._debug['len_expanded_target']['end'] = self._io.pos()
            self._debug['gzip_info']['start'] = self._io.pos()
            self.gzip_info = Imgdiff.GzipInfo(self._io, self, self._root)
            self._debug['gzip_info']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.gzip_info._fetch_instances()
            _ = self.bsdiff
            if hasattr(self, '_m_bsdiff'):
                pass
                self._m_bsdiff._fetch_instances()


        @property
        def bsdiff(self):
            if hasattr(self, '_m_bsdiff'):
                return self._m_bsdiff

            _pos = self._io.pos()
            self._io.seek(self.ofs_bsdiff_patch)
            self._debug['_m_bsdiff']['start'] = self._io.pos()
            self._m_bsdiff = Imgdiff.Bsdiff40(self._io, self, self._root)
            self._debug['_m_bsdiff']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_bsdiff', None)


    class ChunkGzip(KaitaiStruct):
        SEQ_FIELDS = ["ofs_source", "len_source", "ofs_bsdiff_patch", "len_expanded_source", "len_expanded_target", "gzip_info", "len_gzip_header", "gzip_header", "gzip_footer"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Imgdiff.ChunkGzip, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_source']['start'] = self._io.pos()
            self.ofs_source = self._io.read_u8le()
            self._debug['ofs_source']['end'] = self._io.pos()
            self._debug['len_source']['start'] = self._io.pos()
            self.len_source = self._io.read_u8le()
            self._debug['len_source']['end'] = self._io.pos()
            self._debug['ofs_bsdiff_patch']['start'] = self._io.pos()
            self.ofs_bsdiff_patch = self._io.read_u8le()
            self._debug['ofs_bsdiff_patch']['end'] = self._io.pos()
            self._debug['len_expanded_source']['start'] = self._io.pos()
            self.len_expanded_source = self._io.read_u8le()
            self._debug['len_expanded_source']['end'] = self._io.pos()
            self._debug['len_expanded_target']['start'] = self._io.pos()
            self.len_expanded_target = self._io.read_u8le()
            self._debug['len_expanded_target']['end'] = self._io.pos()
            self._debug['gzip_info']['start'] = self._io.pos()
            self.gzip_info = Imgdiff.GzipInfo(self._io, self, self._root)
            self._debug['gzip_info']['end'] = self._io.pos()
            self._debug['len_gzip_header']['start'] = self._io.pos()
            self.len_gzip_header = self._io.read_u4le()
            self._debug['len_gzip_header']['end'] = self._io.pos()
            self._debug['gzip_header']['start'] = self._io.pos()
            self.gzip_header = self._io.read_bytes(self.len_gzip_header)
            self._debug['gzip_header']['end'] = self._io.pos()
            self._debug['gzip_footer']['start'] = self._io.pos()
            self.gzip_footer = self._io.read_bytes(8)
            self._debug['gzip_footer']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.gzip_info._fetch_instances()
            _ = self.bsdiff
            if hasattr(self, '_m_bsdiff'):
                pass
                self._m_bsdiff._fetch_instances()


        @property
        def bsdiff(self):
            if hasattr(self, '_m_bsdiff'):
                return self._m_bsdiff

            _pos = self._io.pos()
            self._io.seek(self.ofs_bsdiff_patch)
            self._debug['_m_bsdiff']['start'] = self._io.pos()
            self._m_bsdiff = Imgdiff.Bsdiff40(self._io, self, self._root)
            self._debug['_m_bsdiff']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_bsdiff', None)


    class ChunkNormal(KaitaiStruct):
        SEQ_FIELDS = ["ofs_source", "len_source", "ofs_bsdiff_patch"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Imgdiff.ChunkNormal, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_source']['start'] = self._io.pos()
            self.ofs_source = self._io.read_u8le()
            self._debug['ofs_source']['end'] = self._io.pos()
            self._debug['len_source']['start'] = self._io.pos()
            self.len_source = self._io.read_u8le()
            self._debug['len_source']['end'] = self._io.pos()
            self._debug['ofs_bsdiff_patch']['start'] = self._io.pos()
            self.ofs_bsdiff_patch = self._io.read_u8le()
            self._debug['ofs_bsdiff_patch']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.bsdiff
            if hasattr(self, '_m_bsdiff'):
                pass
                self._m_bsdiff._fetch_instances()


        @property
        def bsdiff(self):
            if hasattr(self, '_m_bsdiff'):
                return self._m_bsdiff

            _pos = self._io.pos()
            self._io.seek(self.ofs_bsdiff_patch)
            self._debug['_m_bsdiff']['start'] = self._io.pos()
            self._m_bsdiff = Imgdiff.Bsdiff40(self._io, self, self._root)
            self._debug['_m_bsdiff']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_bsdiff', None)


    class ChunkRaw(KaitaiStruct):
        SEQ_FIELDS = ["len_target", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Imgdiff.ChunkRaw, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_target']['start'] = self._io.pos()
            self.len_target = self._io.read_u4le()
            self._debug['len_target']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_target)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class GzipInfo(KaitaiStruct):
        SEQ_FIELDS = ["level", "method", "window_bits", "mem_level", "strategy"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Imgdiff.GzipInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['level']['start'] = self._io.pos()
            self.level = self._io.read_u4le()
            self._debug['level']['end'] = self._io.pos()
            self._debug['method']['start'] = self._io.pos()
            self.method = self._io.read_u4le()
            self._debug['method']['end'] = self._io.pos()
            self._debug['window_bits']['start'] = self._io.pos()
            self.window_bits = self._io.read_u4le()
            self._debug['window_bits']['end'] = self._io.pos()
            self._debug['mem_level']['start'] = self._io.pos()
            self.mem_level = self._io.read_u4le()
            self._debug['mem_level']['end'] = self._io.pos()
            self._debug['strategy']['start'] = self._io.pos()
            self.strategy = self._io.read_u4le()
            self._debug['strategy']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



