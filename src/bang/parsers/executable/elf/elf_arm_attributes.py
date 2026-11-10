# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class ElfArmAttributes(KaitaiStruct):
    SEQ_FIELDS = ["version", "sections"]
    def __init__(self, _io, _parent=None, _root=None):
        super(ElfArmAttributes, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u1()
        self._debug['version']['end'] = self._io.pos()
        self._debug['sections']['start'] = self._io.pos()
        self._debug['sections']['arr'] = []
        self.sections = []
        i = 0
        while not self._io.is_eof():
            self._debug['sections']['arr'].append({'start': self._io.pos()})
            self.sections.append(ElfArmAttributes.ArmAttributesSectionEntry(self._io, self, self._root))
            self._debug['sections']['arr'][len(self.sections) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['sections']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.sections)):
            pass
            self.sections[i]._fetch_instances()


    class ArmAttributesSectionEntry(KaitaiStruct):
        SEQ_FIELDS = ["len_section", "rest_of_entry"]
        def __init__(self, _io, _parent=None, _root=None):
            super(ElfArmAttributes.ArmAttributesSectionEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_section']['start'] = self._io.pos()
            self.len_section = self._io.read_u4le()
            self._debug['len_section']['end'] = self._io.pos()
            self._debug['rest_of_entry']['start'] = self._io.pos()
            self._raw_rest_of_entry = self._io.read_bytes(self.len_section - 4)
            _io__raw_rest_of_entry = KaitaiStream(BytesIO(self._raw_rest_of_entry))
            self.rest_of_entry = ElfArmAttributes.ArmAttributesSectionEntryRest(_io__raw_rest_of_entry, self, self._root)
            self._debug['rest_of_entry']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.rest_of_entry._fetch_instances()


    class ArmAttributesSectionEntryRest(KaitaiStruct):
        SEQ_FIELDS = ["vendor_name", "attribute_tags"]
        def __init__(self, _io, _parent=None, _root=None):
            super(ElfArmAttributes.ArmAttributesSectionEntryRest, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['vendor_name']['start'] = self._io.pos()
            self.vendor_name = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['vendor_name']['end'] = self._io.pos()
            self._debug['attribute_tags']['start'] = self._io.pos()
            self.attribute_tags = self._io.read_bytes_full()
            self._debug['attribute_tags']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



