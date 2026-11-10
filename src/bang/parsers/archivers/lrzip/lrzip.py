# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Lrzip(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/ckolivas/lrzip/blob/master/doc/magic.header.txt
    """

    class Compression(IntEnum):
        no_compression = 3
        bzip2 = 4
        lzo = 5
        lzma = 6
        gzip = 7
        zpaq = 8
    SEQ_FIELDS = ["header", "rchunks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Lrzip, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(24)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Lrzip.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        if (not (self.header.is_encrypted)):
            pass
            self._debug['rchunks']['start'] = self._io.pos()
            self._debug['rchunks']['arr'] = []
            self.rchunks = []
            i = 0
            while True:
                self._debug['rchunks']['arr'].append({'start': self._io.pos()})
                _ = Lrzip.Rchunk(self._io, self, self._root)
                self.rchunks.append(_)
                self._debug['rchunks']['arr'][len(self.rchunks) - 1]['end'] = self._io.pos()
                if _.last_chunk:
                    break
                i += 1
            self._debug['rchunks']['end'] = self._io.pos()



    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        if (not (self.header.is_encrypted)):
            pass
            for i in range(len(self.rchunks)):
                pass
                self.rchunks[i]._fetch_instances()



    class Header(KaitaiStruct):
        SEQ_FIELDS = ["signature", "version", "len_file_or_salt", "unused_1", "lzma_properties", "md5sum_flag", "encryption_flag", "unused_2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Lrzip.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(4)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x4C\x52\x5A\x49":
                raise kaitaistruct.ValidationNotEqualError(b"\x4C\x52\x5A\x49", self.signature, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = Lrzip.Version(self._io, self, self._root)
            self._debug['version']['end'] = self._io.pos()
            self._debug['len_file_or_salt']['start'] = self._io.pos()
            self.len_file_or_salt = self._io.read_u8le()
            self._debug['len_file_or_salt']['end'] = self._io.pos()
            self._debug['unused_1']['start'] = self._io.pos()
            self.unused_1 = self._io.read_bytes(2)
            self._debug['unused_1']['end'] = self._io.pos()
            self._debug['lzma_properties']['start'] = self._io.pos()
            self.lzma_properties = Lrzip.LzmaProperties(self._io, self, self._root)
            self._debug['lzma_properties']['end'] = self._io.pos()
            self._debug['md5sum_flag']['start'] = self._io.pos()
            self.md5sum_flag = self._io.read_u1()
            self._debug['md5sum_flag']['end'] = self._io.pos()
            self._debug['encryption_flag']['start'] = self._io.pos()
            self.encryption_flag = self._io.read_u1()
            self._debug['encryption_flag']['end'] = self._io.pos()
            self._debug['unused_2']['start'] = self._io.pos()
            self.unused_2 = self._io.read_bytes(1)
            self._debug['unused_2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.version._fetch_instances()
            self.lzma_properties._fetch_instances()

        @property
        def has_md5(self):
            if hasattr(self, '_m_has_md5'):
                return self._m_has_md5

            self._m_has_md5 = self.md5sum_flag & 1 == 1
            return getattr(self, '_m_has_md5', None)

        @property
        def is_encrypted(self):
            if hasattr(self, '_m_is_encrypted'):
                return self._m_is_encrypted

            self._m_is_encrypted = self.encryption_flag & 1 == 1
            return getattr(self, '_m_is_encrypted', None)


    class LzmaProperties(KaitaiStruct):
        SEQ_FIELDS = ["lc", "lp", "pb", "fb", "len_dictionary"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Lrzip.LzmaProperties, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['lc']['start'] = self._io.pos()
            self.lc = self._io.read_u1()
            self._debug['lc']['end'] = self._io.pos()
            self._debug['lp']['start'] = self._io.pos()
            self.lp = self._io.read_u1()
            self._debug['lp']['end'] = self._io.pos()
            self._debug['pb']['start'] = self._io.pos()
            self.pb = self._io.read_u1()
            self._debug['pb']['end'] = self._io.pos()
            self._debug['fb']['start'] = self._io.pos()
            self.fb = self._io.read_u1()
            self._debug['fb']['end'] = self._io.pos()
            self._debug['len_dictionary']['start'] = self._io.pos()
            self.len_dictionary = self._io.read_u1()
            self._debug['len_dictionary']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Rchunk(KaitaiStruct):
        SEQ_FIELDS = ["byte_width", "eof_flag", "len_uncompressed", "stream_0", "stream_1"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Lrzip.Rchunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['byte_width']['start'] = self._io.pos()
            self.byte_width = self._io.read_u1()
            self._debug['byte_width']['end'] = self._io.pos()
            if not self.byte_width >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.byte_width, self._io, u"/types/rchunk/seq/0")
            if not self.byte_width <= 4:
                raise kaitaistruct.ValidationGreaterThanError(4, self.byte_width, self._io, u"/types/rchunk/seq/0")
            self._debug['eof_flag']['start'] = self._io.pos()
            self.eof_flag = self._io.read_u1()
            self._debug['eof_flag']['end'] = self._io.pos()
            self._debug['len_uncompressed']['start'] = self._io.pos()
            _on = self.byte_width
            if _on == 1:
                pass
                self.len_uncompressed = self._io.read_u1()
            elif _on == 2:
                pass
                self.len_uncompressed = self._io.read_u2le()
            elif _on == 3:
                pass
                self.len_uncompressed = self._io.read_bits_int_le(24)
            elif _on == 4:
                pass
                self.len_uncompressed = self._io.read_u4le()
            elif _on == 8:
                pass
                self.len_uncompressed = self._io.read_u8le()
            self._debug['len_uncompressed']['end'] = self._io.pos()
            self._debug['stream_0']['start'] = self._io.pos()
            self.stream_0 = Lrzip.StreamHeaderData(self.byte_width, self._io.pos(), self._io, self, self._root)
            self._debug['stream_0']['end'] = self._io.pos()
            self._debug['stream_1']['start'] = self._io.pos()
            self.stream_1 = Lrzip.StreamHeaderData(self.byte_width, self._io.pos() - self.stream_0.size, self._io, self, self._root)
            self._debug['stream_1']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.byte_width
            if _on == 1:
                pass
            elif _on == 2:
                pass
            elif _on == 3:
                pass
            elif _on == 4:
                pass
            elif _on == 8:
                pass
            self.stream_0._fetch_instances()
            self.stream_1._fetch_instances()

        @property
        def last_chunk(self):
            if hasattr(self, '_m_last_chunk'):
                return self._m_last_chunk

            self._m_last_chunk = self.eof_flag == 1
            return getattr(self, '_m_last_chunk', None)


    class StreamHeaderData(KaitaiStruct):
        SEQ_FIELDS = ["compressed_data_type", "len_data", "len_uncompressed_data", "next_block_head", "data"]
        def __init__(self, byte_width, start_position, _io, _parent=None, _root=None):
            super(Lrzip.StreamHeaderData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.byte_width = byte_width
            self.start_position = start_position
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['compressed_data_type']['start'] = self._io.pos()
            self.compressed_data_type = KaitaiStream.resolve_enum(Lrzip.Compression, self._io.read_u1())
            self._debug['compressed_data_type']['end'] = self._io.pos()
            if not  ((self.compressed_data_type == Lrzip.Compression.no_compression) or (self.compressed_data_type == Lrzip.Compression.bzip2) or (self.compressed_data_type == Lrzip.Compression.lzo) or (self.compressed_data_type == Lrzip.Compression.lzma) or (self.compressed_data_type == Lrzip.Compression.gzip) or (self.compressed_data_type == Lrzip.Compression.zpaq)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.compressed_data_type, self._io, u"/types/stream_header_data/seq/0")
            self._debug['len_data']['start'] = self._io.pos()
            _on = self.byte_width
            if _on == 1:
                pass
                self.len_data = self._io.read_u1()
            elif _on == 2:
                pass
                self.len_data = self._io.read_u2le()
            elif _on == 3:
                pass
                self.len_data = self._io.read_bits_int_le(24)
            elif _on == 4:
                pass
                self.len_data = self._io.read_u4le()
            elif _on == 8:
                pass
                self.len_data = self._io.read_u8le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['len_uncompressed_data']['start'] = self._io.pos()
            _on = self.byte_width
            if _on == 1:
                pass
                self.len_uncompressed_data = self._io.read_u1()
            elif _on == 2:
                pass
                self.len_uncompressed_data = self._io.read_u2le()
            elif _on == 3:
                pass
                self.len_uncompressed_data = self._io.read_bits_int_le(24)
            elif _on == 4:
                pass
                self.len_uncompressed_data = self._io.read_u4le()
            elif _on == 8:
                pass
                self.len_uncompressed_data = self._io.read_u8le()
            self._debug['len_uncompressed_data']['end'] = self._io.pos()
            self._debug['next_block_head']['start'] = self._io.pos()
            _on = self.byte_width
            if _on == 1:
                pass
                self.next_block_head = self._io.read_u1()
            elif _on == 2:
                pass
                self.next_block_head = self._io.read_u2le()
            elif _on == 3:
                pass
                self.next_block_head = self._io.read_bits_int_le(24)
            elif _on == 4:
                pass
                self.next_block_head = self._io.read_u4le()
            elif _on == 8:
                pass
                self.next_block_head = self._io.read_u8le()
            self._debug['next_block_head']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.byte_width
            if _on == 1:
                pass
            elif _on == 2:
                pass
            elif _on == 3:
                pass
            elif _on == 4:
                pass
            elif _on == 8:
                pass
            _on = self.byte_width
            if _on == 1:
                pass
            elif _on == 2:
                pass
            elif _on == 3:
                pass
            elif _on == 4:
                pass
            elif _on == 8:
                pass
            _on = self.byte_width
            if _on == 1:
                pass
            elif _on == 2:
                pass
            elif _on == 3:
                pass
            elif _on == 4:
                pass
            elif _on == 8:
                pass
            _ = self.next
            if hasattr(self, '_m_next'):
                pass
                self._m_next._fetch_instances()


        @property
        def next(self):
            if hasattr(self, '_m_next'):
                return self._m_next

            if self.next_block_head != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.next_block_head + self.start_position)
                self._debug['_m_next']['start'] = io.pos()
                self._m_next = Lrzip.StreamHeaderData(self.byte_width, self.start_position, io, self, self._root)
                self._debug['_m_next']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_next', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 1 + 3 * self.byte_width
            return getattr(self, '_m_size', None)


    class Version(KaitaiStruct):
        SEQ_FIELDS = ["major", "minor"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Lrzip.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u1()
            self._debug['major']['end'] = self._io.pos()
            if not self.major == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.major, self._io, u"/types/version/seq/0")
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u1()
            self._debug['minor']['end'] = self._io.pos()
            if not self.minor == 6:
                raise kaitaistruct.ValidationNotEqualError(6, self.minor, self._io, u"/types/version/seq/1")


        def _fetch_instances(self):
            pass



