# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Gvariant(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/GNOME/gvdb/blob/main/gvdb/gvdb-format.h
    """
    SEQ_FIELDS = ["signature", "version", "options", "root"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Gvariant, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['signature']['start'] = self._io.pos()
        self.signature = self._io.read_bytes(8)
        self._debug['signature']['end'] = self._io.pos()
        if not self.signature == b"\x47\x56\x61\x72\x69\x61\x6E\x74":
            raise kaitaistruct.ValidationNotEqualError(b"\x47\x56\x61\x72\x69\x61\x6E\x74", self.signature, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        self._debug['options']['start'] = self._io.pos()
        self.options = self._io.read_u4le()
        self._debug['options']['end'] = self._io.pos()
        self._debug['root']['start'] = self._io.pos()
        self.root = Gvariant.Pointer(self._io, self, self._root)
        self._debug['root']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.root._fetch_instances()

    class HashHeader(KaitaiStruct):
        SEQ_FIELDS = ["n_bloom_words", "n_buckets"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Gvariant.HashHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['n_bloom_words']['start'] = self._io.pos()
            self.n_bloom_words = self._io.read_u4le()
            self._debug['n_bloom_words']['end'] = self._io.pos()
            self._debug['n_buckets']['start'] = self._io.pos()
            self.n_buckets = self._io.read_u4le()
            self._debug['n_buckets']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def num_bloom_words(self):
            if hasattr(self, '_m_num_bloom_words'):
                return self._m_num_bloom_words

            self._m_num_bloom_words = self.n_bloom_words & (1 << 27) - 1
            return getattr(self, '_m_num_bloom_words', None)


    class Pointer(KaitaiStruct):
        SEQ_FIELDS = ["start", "end"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Gvariant.Pointer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['start']['start'] = self._io.pos()
            self.start = self._io.read_u4le()
            self._debug['start']['end'] = self._io.pos()
            self._debug['end']['start'] = self._io.pos()
            self.end = self._io.read_u4le()
            self._debug['end']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.data
            if hasattr(self, '_m_data'):
                pass
                self._m_data._fetch_instances()


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            _pos = self._io.pos()
            self._io.seek(self.start)
            self._debug['_m_data']['start'] = self._io.pos()
            self._raw__m_data = self._io.read_bytes(self.end - self.start)
            _io__raw__m_data = KaitaiStream(BytesIO(self._raw__m_data))
            self._m_data = Gvariant.HashHeader(_io__raw__m_data, self, self._root)
            self._debug['_m_data']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_data', None)



