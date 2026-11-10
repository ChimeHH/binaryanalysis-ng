# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import zip
from .zip import *
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Crx(KaitaiStruct):
    """
    .. seealso::
       Source - https://chromium.googlesource.com/chromium/src.git/+/62.0.3178.1/chrome/common/extensions/docs/templates/articles/crx.html
    
    
    .. seealso::
       Source - https://pypi.org/project/crx-unpack/
    """
    SEQ_FIELDS = ["header", "zip"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Crx, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Crx.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['zip']['start'] = self._io.pos()
        self.zip = zip.Zip(self._io)
        self._debug['zip']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.zip._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "len_public_key", "len_signature", "public_key", "signature"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Crx.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x43\x72\x32\x34":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x72\x32\x34", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 2:
                raise kaitaistruct.ValidationNotEqualError(2, self.version, self._io, u"/types/header/seq/1")
            self._debug['len_public_key']['start'] = self._io.pos()
            self.len_public_key = self._io.read_u4le()
            self._debug['len_public_key']['end'] = self._io.pos()
            self._debug['len_signature']['start'] = self._io.pos()
            self.len_signature = self._io.read_u4le()
            self._debug['len_signature']['end'] = self._io.pos()
            self._debug['public_key']['start'] = self._io.pos()
            self.public_key = self._io.read_bytes(self.len_public_key)
            self._debug['public_key']['end'] = self._io.pos()
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(self.len_signature)
            self._debug['signature']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def len_header(self):
            if hasattr(self, '_m_len_header'):
                return self._m_len_header

            self._m_len_header = ((((4 + 4) + 4) + 4) + self.len_public_key) + self.len_signature
            return getattr(self, '_m_len_header', None)



