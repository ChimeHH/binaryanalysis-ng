# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class JavaKeystore(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/openjdk-mirror/jdk7u-jdk/blob/master/src/share/classes/sun/security/provider/JavaKeyStore.java
    
    
    .. seealso::
       Source - https://github.com/kurtbrose/pyjks
    """
    SEQ_FIELDS = ["magic", "version", "num_key_entries", "key_entries", "sha1"]
    def __init__(self, _io, _parent=None, _root=None):
        super(JavaKeystore, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\xFE\xED\xFE\xED":
            raise kaitaistruct.ValidationNotEqualError(b"\xFE\xED\xFE\xED", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4be()
        self._debug['version']['end'] = self._io.pos()
        if not self.version == 2:
            raise kaitaistruct.ValidationNotEqualError(2, self.version, self._io, u"/seq/1")
        self._debug['num_key_entries']['start'] = self._io.pos()
        self.num_key_entries = self._io.read_u4be()
        self._debug['num_key_entries']['end'] = self._io.pos()
        if not self.num_key_entries <= self._root._io.size():
            raise kaitaistruct.ValidationGreaterThanError(self._root._io.size(), self.num_key_entries, self._io, u"/seq/2")
        self._debug['key_entries']['start'] = self._io.pos()
        self._debug['key_entries']['arr'] = []
        self.key_entries = []
        for i in range(self.num_key_entries):
            self._debug['key_entries']['arr'].append({'start': self._io.pos()})
            self.key_entries.append(JavaKeystore.KeyEntry(self._io, self, self._root))
            self._debug['key_entries']['arr'][i]['end'] = self._io.pos()

        self._debug['key_entries']['end'] = self._io.pos()
        self._debug['sha1']['start'] = self._io.pos()
        self.sha1 = self._io.read_bytes(20)
        self._debug['sha1']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.key_entries)):
            pass
            self.key_entries[i]._fetch_instances()


    class Certificate(KaitaiStruct):
        SEQ_FIELDS = ["len_name", "name", "len_certificate", "certificate"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaKeystore.Certificate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_u2be()
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(self.len_name)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['len_certificate']['start'] = self._io.pos()
            self.len_certificate = self._io.read_u4be()
            self._debug['len_certificate']['end'] = self._io.pos()
            self._debug['certificate']['start'] = self._io.pos()
            self.certificate = self._io.read_bytes(self.len_certificate)
            self._debug['certificate']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class KeyEntry(KaitaiStruct):
        SEQ_FIELDS = ["tag", "len_alias", "alias", "timestamp", "key_entry_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaKeystore.KeyEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tag']['start'] = self._io.pos()
            self.tag = self._io.read_u4be()
            self._debug['tag']['end'] = self._io.pos()
            if not  ((self.tag == 1) or (self.tag == 2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.tag, self._io, u"/types/key_entry/seq/0")
            self._debug['len_alias']['start'] = self._io.pos()
            self.len_alias = self._io.read_u2be()
            self._debug['len_alias']['end'] = self._io.pos()
            self._debug['alias']['start'] = self._io.pos()
            self.alias = (self._io.read_bytes(self.len_alias)).decode(u"UTF-8")
            self._debug['alias']['end'] = self._io.pos()
            self._debug['timestamp']['start'] = self._io.pos()
            self.timestamp = self._io.read_u8be()
            self._debug['timestamp']['end'] = self._io.pos()
            self._debug['key_entry_data']['start'] = self._io.pos()
            _on = self.tag
            if _on == 1:
                pass
                self.key_entry_data = JavaKeystore.KeyEntryData1(self._io, self, self._root)
            elif _on == 2:
                pass
                self.key_entry_data = JavaKeystore.KeyEntryData2(self._io, self, self._root)
            self._debug['key_entry_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.tag
            if _on == 1:
                pass
                self.key_entry_data._fetch_instances()
            elif _on == 2:
                pass
                self.key_entry_data._fetch_instances()


    class KeyEntryData1(KaitaiStruct):
        SEQ_FIELDS = ["len_private_key", "private_key", "num_certificates", "certificates"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaKeystore.KeyEntryData1, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_private_key']['start'] = self._io.pos()
            self.len_private_key = self._io.read_u4be()
            self._debug['len_private_key']['end'] = self._io.pos()
            self._debug['private_key']['start'] = self._io.pos()
            self.private_key = self._io.read_bytes(self.len_private_key)
            self._debug['private_key']['end'] = self._io.pos()
            self._debug['num_certificates']['start'] = self._io.pos()
            self.num_certificates = self._io.read_u4be()
            self._debug['num_certificates']['end'] = self._io.pos()
            self._debug['certificates']['start'] = self._io.pos()
            self._debug['certificates']['arr'] = []
            self.certificates = []
            for i in range(self.num_certificates):
                self._debug['certificates']['arr'].append({'start': self._io.pos()})
                self.certificates.append(JavaKeystore.Certificate(self._io, self, self._root))
                self._debug['certificates']['arr'][i]['end'] = self._io.pos()

            self._debug['certificates']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.certificates)):
                pass
                self.certificates[i]._fetch_instances()



    class KeyEntryData2(KaitaiStruct):
        SEQ_FIELDS = ["certificate"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaKeystore.KeyEntryData2, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['certificate']['start'] = self._io.pos()
            self.certificate = JavaKeystore.Certificate(self._io, self, self._root)
            self._debug['certificate']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.certificate._fetch_instances()



