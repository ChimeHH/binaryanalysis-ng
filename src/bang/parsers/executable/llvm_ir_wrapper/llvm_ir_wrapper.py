# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class LlvmIrWrapper(KaitaiStruct):
    """
    .. seealso::
       Source - https://llvm.org/docs/BitCodeFormat.html
    """
    SEQ_FIELDS = ["magic", "version", "ofs_bytecode", "len_bytecode", "cpu_type"]
    def __init__(self, _io, _parent=None, _root=None):
        super(LlvmIrWrapper, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\xDE\xC0\x17\x0B":
            raise kaitaistruct.ValidationNotEqualError(b"\xDE\xC0\x17\x0B", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        if not self.version == 0:
            raise kaitaistruct.ValidationNotEqualError(0, self.version, self._io, u"/seq/1")
        self._debug['ofs_bytecode']['start'] = self._io.pos()
        self.ofs_bytecode = self._io.read_u4le()
        self._debug['ofs_bytecode']['end'] = self._io.pos()
        self._debug['len_bytecode']['start'] = self._io.pos()
        self.len_bytecode = self._io.read_u4le()
        self._debug['len_bytecode']['end'] = self._io.pos()
        self._debug['cpu_type']['start'] = self._io.pos()
        self.cpu_type = self._io.read_u4le()
        self._debug['cpu_type']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _ = self.bytecode
        if hasattr(self, '_m_bytecode'):
            pass


    @property
    def bytecode(self):
        if hasattr(self, '_m_bytecode'):
            return self._m_bytecode

        _pos = self._io.pos()
        self._io.seek(self.ofs_bytecode)
        self._debug['_m_bytecode']['start'] = self._io.pos()
        self._m_bytecode = self._io.read_bytes(self.len_bytecode)
        self._debug['_m_bytecode']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_bytecode', None)


