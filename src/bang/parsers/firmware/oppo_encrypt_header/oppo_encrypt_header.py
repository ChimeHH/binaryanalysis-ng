# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class OppoEncryptHeader(KaitaiStruct):
    """
    .. seealso::
       Source - https://web.archive.org/web/20190304142705/https://gist.github.com/wfjsw/7c8763dfd543b49b2a3ebf089acc83b0
    
    
    .. seealso::
       Source - https://web.archive.org/web/20221208034118/https://bkerler.github.io/reversing/2019/04/24/the-game-begins/
    """
    SEQ_FIELDS = ["signature", "size_str", "sha1", "reconstruct"]
    def __init__(self, _io, _parent=None, _root=None):
        super(OppoEncryptHeader, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['signature']['start'] = self._io.pos()
        self.signature = self._io.read_bytes(16)
        self._debug['signature']['end'] = self._io.pos()
        if not self.signature == b"\x4F\x50\x50\x4F\x45\x4E\x43\x52\x59\x50\x54\x21\x00\x00\x00\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x4F\x50\x50\x4F\x45\x4E\x43\x52\x59\x50\x54\x21\x00\x00\x00\x00", self.signature, self._io, u"/seq/0")
        self._debug['size_str']['start'] = self._io.pos()
        self.size_str = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"UTF-8")
        self._debug['size_str']['end'] = self._io.pos()
        self._debug['sha1']['start'] = self._io.pos()
        self.sha1 = (KaitaiStream.bytes_terminate(self._io.read_bytes(48), 0, False)).decode(u"UTF-8")
        self._debug['sha1']['end'] = self._io.pos()
        self._debug['reconstruct']['start'] = self._io.pos()
        self._raw_reconstruct = self._io.read_bytes(4096)
        _io__raw_reconstruct = KaitaiStream(BytesIO(self._raw_reconstruct))
        self.reconstruct = OppoEncryptHeader.Reconstruct(_io__raw_reconstruct, self, self._root)
        self._debug['reconstruct']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.reconstruct._fetch_instances()

    class Reconstruct(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(OppoEncryptHeader.Reconstruct, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.reconstruct_components
            if hasattr(self, '_m_reconstruct_components'):
                pass
                for i in range(len(self._m_reconstruct_components)):
                    pass


            _ = self.reconstruct_string
            if hasattr(self, '_m_reconstruct_string'):
                pass


        @property
        def reconstruct_components(self):
            if hasattr(self, '_m_reconstruct_components'):
                return self._m_reconstruct_components

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_reconstruct_components']['start'] = self._io.pos()
            self._debug['_m_reconstruct_components']['arr'] = []
            self._m_reconstruct_components = []
            i = 0
            while not self._io.is_eof():
                self._debug['_m_reconstruct_components']['arr'].append({'start': self._io.pos()})
                self._m_reconstruct_components.append((self._io.read_bytes_term(10, False, True, False)).decode(u"UTF-8"))
                self._debug['_m_reconstruct_components']['arr'][len(self._m_reconstruct_components) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['_m_reconstruct_components']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_reconstruct_components', None)

        @property
        def reconstruct_string(self):
            if hasattr(self, '_m_reconstruct_string'):
                return self._m_reconstruct_string

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_reconstruct_string']['start'] = self._io.pos()
            self._m_reconstruct_string = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['_m_reconstruct_string']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_reconstruct_string', None)


    @property
    def decompressed_size(self):
        if hasattr(self, '_m_decompressed_size'):
            return self._m_decompressed_size

        self._m_decompressed_size = int(self.size_str)
        return getattr(self, '_m_decompressed_size', None)


