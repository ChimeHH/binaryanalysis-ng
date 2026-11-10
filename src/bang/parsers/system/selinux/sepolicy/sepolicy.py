# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Sepolicy(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/SELinuxProject/selinux/blob/b550c0e/libsepol/src/write.c#L2122
    """
    SEQ_FIELDS = ["magic", "len_policydb_string", "policydb_string", "policy_version", "config", "num_symbols", "num_ocons", "symbols", "avtab"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Sepolicy, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x8C\xFF\x7C\xF9":
            raise kaitaistruct.ValidationNotEqualError(b"\x8C\xFF\x7C\xF9", self.magic, self._io, u"/seq/0")
        self._debug['len_policydb_string']['start'] = self._io.pos()
        self.len_policydb_string = self._io.read_u4le()
        self._debug['len_policydb_string']['end'] = self._io.pos()
        self._debug['policydb_string']['start'] = self._io.pos()
        self.policydb_string = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_policydb_string), 0, False)).decode(u"UTF-8")
        self._debug['policydb_string']['end'] = self._io.pos()
        self._debug['policy_version']['start'] = self._io.pos()
        self.policy_version = self._io.read_u4le()
        self._debug['policy_version']['end'] = self._io.pos()
        if not self.policy_version >= 24:
            raise kaitaistruct.ValidationLessThanError(24, self.policy_version, self._io, u"/seq/3")
        self._debug['config']['start'] = self._io.pos()
        self.config = self._io.read_u4le()
        self._debug['config']['end'] = self._io.pos()
        self._debug['num_symbols']['start'] = self._io.pos()
        self.num_symbols = self._io.read_u4le()
        self._debug['num_symbols']['end'] = self._io.pos()
        self._debug['num_ocons']['start'] = self._io.pos()
        self.num_ocons = self._io.read_u4le()
        self._debug['num_ocons']['end'] = self._io.pos()
        self._debug['symbols']['start'] = self._io.pos()
        self._debug['symbols']['arr'] = []
        self.symbols = []
        for i in range(self.num_symbols):
            self._debug['symbols']['arr'].append({'start': self._io.pos()})
            self.symbols.append(Sepolicy.Symbol(self._io, self, self._root))
            self._debug['symbols']['arr'][i]['end'] = self._io.pos()

        self._debug['symbols']['end'] = self._io.pos()
        self._debug['avtab']['start'] = self._io.pos()
        self.avtab = Sepolicy.Avtab(self._io, self, self._root)
        self._debug['avtab']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.symbols)):
            pass
            self.symbols[i]._fetch_instances()

        self.avtab._fetch_instances()

    class Avtab(KaitaiStruct):
        SEQ_FIELDS = ["source_type", "target_type", "target_class", "specified"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Sepolicy.Avtab, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['source_type']['start'] = self._io.pos()
            self.source_type = self._io.read_u2le()
            self._debug['source_type']['end'] = self._io.pos()
            self._debug['target_type']['start'] = self._io.pos()
            self.target_type = self._io.read_u2le()
            self._debug['target_type']['end'] = self._io.pos()
            self._debug['target_class']['start'] = self._io.pos()
            self.target_class = self._io.read_u2le()
            self._debug['target_class']['end'] = self._io.pos()
            self._debug['specified']['start'] = self._io.pos()
            self.specified = self._io.read_u2le()
            self._debug['specified']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Symbol(KaitaiStruct):
        SEQ_FIELDS = ["nprim", "nel"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Sepolicy.Symbol, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['nprim']['start'] = self._io.pos()
            self.nprim = self._io.read_u4le()
            self._debug['nprim']['end'] = self._io.pos()
            self._debug['nel']['start'] = self._io.pos()
            self.nel = self._io.read_u4le()
            self._debug['nel']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



