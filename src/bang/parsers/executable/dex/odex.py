# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Odex(KaitaiStruct):
    """
    .. seealso::
       Source - http://web.archive.org/web/20180816094438/https://android.googlesource.com/platform/dalvik.git/+/master/libdex/DexFile.h
    """
    SEQ_FIELDS = ["magic", "version", "ofs_dex", "len_dex", "ofs_deps", "len_deps", "ofs_opt", "len_opt", "flags", "adler32"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Odex, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x64\x65\x79\x0A":
            raise kaitaistruct.ValidationNotEqualError(b"\x64\x65\x79\x0A", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"UTF-8")
        self._debug['version']['end'] = self._io.pos()
        self._debug['ofs_dex']['start'] = self._io.pos()
        self.ofs_dex = self._io.read_u4le()
        self._debug['ofs_dex']['end'] = self._io.pos()
        self._debug['len_dex']['start'] = self._io.pos()
        self.len_dex = self._io.read_u4le()
        self._debug['len_dex']['end'] = self._io.pos()
        self._debug['ofs_deps']['start'] = self._io.pos()
        self.ofs_deps = self._io.read_u4le()
        self._debug['ofs_deps']['end'] = self._io.pos()
        self._debug['len_deps']['start'] = self._io.pos()
        self.len_deps = self._io.read_u4le()
        self._debug['len_deps']['end'] = self._io.pos()
        self._debug['ofs_opt']['start'] = self._io.pos()
        self.ofs_opt = self._io.read_u4le()
        self._debug['ofs_opt']['end'] = self._io.pos()
        self._debug['len_opt']['start'] = self._io.pos()
        self.len_opt = self._io.read_u4le()
        self._debug['len_opt']['end'] = self._io.pos()
        self._debug['flags']['start'] = self._io.pos()
        self.flags = self._io.read_u4le()
        self._debug['flags']['end'] = self._io.pos()
        self._debug['adler32']['start'] = self._io.pos()
        self.adler32 = self._io.read_u4le()
        self._debug['adler32']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _ = self.deps
        if hasattr(self, '_m_deps'):
            pass

        _ = self.deps_padding
        if hasattr(self, '_m_deps_padding'):
            pass

        _ = self.dex
        if hasattr(self, '_m_dex'):
            pass

        _ = self.opt
        if hasattr(self, '_m_opt'):
            pass


    @property
    def deps(self):
        if hasattr(self, '_m_deps'):
            return self._m_deps

        _pos = self._io.pos()
        self._io.seek(self.ofs_deps)
        self._debug['_m_deps']['start'] = self._io.pos()
        self._m_deps = self._io.read_bytes(self.len_deps)
        self._debug['_m_deps']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_deps', None)

    @property
    def deps_padding(self):
        if hasattr(self, '_m_deps_padding'):
            return self._m_deps_padding

        _pos = self._io.pos()
        self._io.seek(self.ofs_deps + self.len_deps)
        self._debug['_m_deps_padding']['start'] = self._io.pos()
        self._m_deps_padding = self._io.read_bytes(-(self.len_deps) % 8)
        self._debug['_m_deps_padding']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_deps_padding', None)

    @property
    def dex(self):
        if hasattr(self, '_m_dex'):
            return self._m_dex

        _pos = self._io.pos()
        self._io.seek(self.ofs_dex)
        self._debug['_m_dex']['start'] = self._io.pos()
        self._m_dex = self._io.read_bytes(self.len_dex)
        self._debug['_m_dex']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_dex', None)

    @property
    def opt(self):
        if hasattr(self, '_m_opt'):
            return self._m_opt

        _pos = self._io.pos()
        self._io.seek(self.ofs_opt)
        self._debug['_m_opt']['start'] = self._io.pos()
        self._m_opt = self._io.read_bytes(self.len_opt)
        self._debug['_m_opt']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_opt', None)


