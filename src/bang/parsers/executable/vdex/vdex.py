# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Vdex(KaitaiStruct):
    """Verified Dex
    
    version 006: Android 8 (verified: walleye-opd1.170816.010-factory-63083164.zip )
    version 010: Android 8.1 (verified: walleye-opm1.171019.011-factory-f74dd4fd.zip )
    version 019: Android 9 (verified: walleye-ppr1.180610.009-factory-4149f7e5.zip )
    version 021: Android 10 & 11
    version 027: Android 12 (verified: raven-sd1a.210817.015.a4-factory-bd6cb030.zip )
    
    .. seealso::
       Source - https://android.googlesource.com/platform/art/+/master/runtime/vdex_file.h
    """

    class VdexSection(IntEnum):
        checksum = 0
        dex_file = 1
        verifier_deps = 2
        type_lookup_table = 3
        number_of_sections = 4
    SEQ_FIELDS = ["magic", "version", "dex_header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Vdex, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x76\x64\x65\x78":
            raise kaitaistruct.ValidationNotEqualError(b"\x76\x64\x65\x78", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"UTF-8")
        self._debug['version']['end'] = self._io.pos()
        if not  ((self.version == u"006") or (self.version == u"010") or (self.version == u"019") or (self.version == u"021") or (self.version == u"027")) :
            raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/seq/1")
        self._debug['dex_header']['start'] = self._io.pos()
        _on = self.version
        if _on == u"006":
            pass
            self.dex_header = Vdex.Header006010(self._io, self, self._root)
        elif _on == u"010":
            pass
            self.dex_header = Vdex.Header006010(self._io, self, self._root)
        elif _on == u"019":
            pass
            self.dex_header = Vdex.Header019021(self.version, self._io, self, self._root)
        elif _on == u"021":
            pass
            self.dex_header = Vdex.Header019021(self.version, self._io, self, self._root)
        elif _on == u"027":
            pass
            self.dex_header = Vdex.Header027(self._io, self, self._root)
        self._debug['dex_header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _on = self.version
        if _on == u"006":
            pass
            self.dex_header._fetch_instances()
        elif _on == u"010":
            pass
            self.dex_header._fetch_instances()
        elif _on == u"019":
            pass
            self.dex_header._fetch_instances()
        elif _on == u"021":
            pass
            self.dex_header._fetch_instances()
        elif _on == u"027":
            pass
            self.dex_header._fetch_instances()

    class CdexHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "checksum", "sha1", "len_file", "len_header", "endian_tag", "len_link", "ofs_link", "ofs_map", "len_string_ids", "ofs_string_ids", "len_type_ids", "ofs_type_ids", "len_proto_ids", "ofs_proto_ids", "len_field_ids", "ofs_field_ids", "len_method_ids", "ofs_method_ids", "len_class_defs", "ofs_class_defs", "len_data", "ofs_data", "feature_flags", "ofs_debug_info_offsets", "ofs_debug_info_offsets_table", "debug_info_base", "owned_data_begin", "owned_data_end"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vdex.CdexHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x63\x64\x65\x78":
                raise kaitaistruct.ValidationNotEqualError(b"\x63\x64\x65\x78", self.magic, self._io, u"/types/cdex_header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"UTF-8")
            self._debug['version']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_u4le()
            self._debug['checksum']['end'] = self._io.pos()
            self._debug['sha1']['start'] = self._io.pos()
            self.sha1 = self._io.read_bytes(20)
            self._debug['sha1']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['endian_tag']['start'] = self._io.pos()
            self.endian_tag = self._io.read_u4le()
            self._debug['endian_tag']['end'] = self._io.pos()
            self._debug['len_link']['start'] = self._io.pos()
            self.len_link = self._io.read_u4le()
            self._debug['len_link']['end'] = self._io.pos()
            self._debug['ofs_link']['start'] = self._io.pos()
            self.ofs_link = self._io.read_u4le()
            self._debug['ofs_link']['end'] = self._io.pos()
            self._debug['ofs_map']['start'] = self._io.pos()
            self.ofs_map = self._io.read_u4le()
            self._debug['ofs_map']['end'] = self._io.pos()
            self._debug['len_string_ids']['start'] = self._io.pos()
            self.len_string_ids = self._io.read_u4le()
            self._debug['len_string_ids']['end'] = self._io.pos()
            self._debug['ofs_string_ids']['start'] = self._io.pos()
            self.ofs_string_ids = self._io.read_u4le()
            self._debug['ofs_string_ids']['end'] = self._io.pos()
            self._debug['len_type_ids']['start'] = self._io.pos()
            self.len_type_ids = self._io.read_u4le()
            self._debug['len_type_ids']['end'] = self._io.pos()
            self._debug['ofs_type_ids']['start'] = self._io.pos()
            self.ofs_type_ids = self._io.read_u4le()
            self._debug['ofs_type_ids']['end'] = self._io.pos()
            self._debug['len_proto_ids']['start'] = self._io.pos()
            self.len_proto_ids = self._io.read_u4le()
            self._debug['len_proto_ids']['end'] = self._io.pos()
            self._debug['ofs_proto_ids']['start'] = self._io.pos()
            self.ofs_proto_ids = self._io.read_u4le()
            self._debug['ofs_proto_ids']['end'] = self._io.pos()
            self._debug['len_field_ids']['start'] = self._io.pos()
            self.len_field_ids = self._io.read_u4le()
            self._debug['len_field_ids']['end'] = self._io.pos()
            self._debug['ofs_field_ids']['start'] = self._io.pos()
            self.ofs_field_ids = self._io.read_u4le()
            self._debug['ofs_field_ids']['end'] = self._io.pos()
            self._debug['len_method_ids']['start'] = self._io.pos()
            self.len_method_ids = self._io.read_u4le()
            self._debug['len_method_ids']['end'] = self._io.pos()
            self._debug['ofs_method_ids']['start'] = self._io.pos()
            self.ofs_method_ids = self._io.read_u4le()
            self._debug['ofs_method_ids']['end'] = self._io.pos()
            self._debug['len_class_defs']['start'] = self._io.pos()
            self.len_class_defs = self._io.read_u4le()
            self._debug['len_class_defs']['end'] = self._io.pos()
            self._debug['ofs_class_defs']['start'] = self._io.pos()
            self.ofs_class_defs = self._io.read_u4le()
            self._debug['ofs_class_defs']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['ofs_data']['start'] = self._io.pos()
            self.ofs_data = self._io.read_u4le()
            self._debug['ofs_data']['end'] = self._io.pos()
            self._debug['feature_flags']['start'] = self._io.pos()
            self.feature_flags = self._io.read_u4le()
            self._debug['feature_flags']['end'] = self._io.pos()
            self._debug['ofs_debug_info_offsets']['start'] = self._io.pos()
            self.ofs_debug_info_offsets = self._io.read_u4le()
            self._debug['ofs_debug_info_offsets']['end'] = self._io.pos()
            self._debug['ofs_debug_info_offsets_table']['start'] = self._io.pos()
            self.ofs_debug_info_offsets_table = self._io.read_u4le()
            self._debug['ofs_debug_info_offsets_table']['end'] = self._io.pos()
            self._debug['debug_info_base']['start'] = self._io.pos()
            self.debug_info_base = self._io.read_u4le()
            self._debug['debug_info_base']['end'] = self._io.pos()
            self._debug['owned_data_begin']['start'] = self._io.pos()
            self.owned_data_begin = self._io.read_u4le()
            self._debug['owned_data_begin']['end'] = self._io.pos()
            self._debug['owned_data_end']['start'] = self._io.pos()
            self.owned_data_end = self._io.read_u4le()
            self._debug['owned_data_end']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class DexSectionHeader019021(KaitaiStruct):
        SEQ_FIELDS = ["len_dex", "len_dex_shared_data", "len_quickening_info", "quicken_and_dex"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vdex.DexSectionHeader019021, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_dex']['start'] = self._io.pos()
            self.len_dex = self._io.read_u4le()
            self._debug['len_dex']['end'] = self._io.pos()
            self._debug['len_dex_shared_data']['start'] = self._io.pos()
            self.len_dex_shared_data = self._io.read_u4le()
            self._debug['len_dex_shared_data']['end'] = self._io.pos()
            self._debug['len_quickening_info']['start'] = self._io.pos()
            self.len_quickening_info = self._io.read_u4le()
            self._debug['len_quickening_info']['end'] = self._io.pos()
            self._debug['quicken_and_dex']['start'] = self._io.pos()
            self.quicken_and_dex = self._io.read_bytes(self.len_dex + self.len_dex_shared_data)
            self._debug['quicken_and_dex']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header006010(KaitaiStruct):
        SEQ_FIELDS = ["num_dex", "len_dex", "len_verifier_deps", "len_quickening_info", "location_checksum", "dex_files", "verifier_deps", "quickening_info"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vdex.Header006010, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_dex']['start'] = self._io.pos()
            self.num_dex = self._io.read_u4le()
            self._debug['num_dex']['end'] = self._io.pos()
            self._debug['len_dex']['start'] = self._io.pos()
            self.len_dex = self._io.read_u4le()
            self._debug['len_dex']['end'] = self._io.pos()
            self._debug['len_verifier_deps']['start'] = self._io.pos()
            self.len_verifier_deps = self._io.read_u4le()
            self._debug['len_verifier_deps']['end'] = self._io.pos()
            self._debug['len_quickening_info']['start'] = self._io.pos()
            self.len_quickening_info = self._io.read_u4le()
            self._debug['len_quickening_info']['end'] = self._io.pos()
            self._debug['location_checksum']['start'] = self._io.pos()
            self.location_checksum = self._io.read_u4le()
            self._debug['location_checksum']['end'] = self._io.pos()
            self._debug['dex_files']['start'] = self._io.pos()
            self.dex_files = self._io.read_bytes(self.len_dex)
            self._debug['dex_files']['end'] = self._io.pos()
            self._debug['verifier_deps']['start'] = self._io.pos()
            self.verifier_deps = self._io.read_bytes(self.len_verifier_deps)
            self._debug['verifier_deps']['end'] = self._io.pos()
            self._debug['quickening_info']['start'] = self._io.pos()
            self.quickening_info = self._io.read_bytes(self.len_quickening_info)
            self._debug['quickening_info']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header019021(KaitaiStruct):
        SEQ_FIELDS = ["dex_section_version", "num_dex", "len_verifier_deps", "len_bootclasspath_checksum", "len_classloader_context", "dex_checksums", "dex_section_header", "verifier_deps", "quickening_info"]
        def __init__(self, version, _io, _parent=None, _root=None):
            super(Vdex.Header019021, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.version = version
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['dex_section_version']['start'] = self._io.pos()
            self.dex_section_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"UTF-8")
            self._debug['dex_section_version']['end'] = self._io.pos()
            self._debug['num_dex']['start'] = self._io.pos()
            self.num_dex = self._io.read_u4le()
            self._debug['num_dex']['end'] = self._io.pos()
            self._debug['len_verifier_deps']['start'] = self._io.pos()
            self.len_verifier_deps = self._io.read_u4le()
            self._debug['len_verifier_deps']['end'] = self._io.pos()
            if self.version == u"021":
                pass
                self._debug['len_bootclasspath_checksum']['start'] = self._io.pos()
                self.len_bootclasspath_checksum = self._io.read_u4le()
                self._debug['len_bootclasspath_checksum']['end'] = self._io.pos()

            if self.version == u"021":
                pass
                self._debug['len_classloader_context']['start'] = self._io.pos()
                self.len_classloader_context = self._io.read_u4le()
                self._debug['len_classloader_context']['end'] = self._io.pos()

            self._debug['dex_checksums']['start'] = self._io.pos()
            self._debug['dex_checksums']['arr'] = []
            self.dex_checksums = []
            for i in range(self.num_dex):
                self._debug['dex_checksums']['arr'].append({'start': self._io.pos()})
                self.dex_checksums.append(self._io.read_u4le())
                self._debug['dex_checksums']['arr'][i]['end'] = self._io.pos()

            self._debug['dex_checksums']['end'] = self._io.pos()
            if self.dex_section_version != u"000":
                pass
                self._debug['dex_section_header']['start'] = self._io.pos()
                self.dex_section_header = Vdex.DexSectionHeader019021(self._io, self, self._root)
                self._debug['dex_section_header']['end'] = self._io.pos()

            self._debug['verifier_deps']['start'] = self._io.pos()
            self.verifier_deps = self._io.read_bytes(self.len_verifier_deps)
            self._debug['verifier_deps']['end'] = self._io.pos()
            if self.dex_section_version != u"000":
                pass
                self._debug['quickening_info']['start'] = self._io.pos()
                self.quickening_info = self._io.read_bytes(self.dex_section_header.len_quickening_info)
                self._debug['quickening_info']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.version == u"021":
                pass

            if self.version == u"021":
                pass

            for i in range(len(self.dex_checksums)):
                pass

            if self.dex_section_version != u"000":
                pass
                self.dex_section_header._fetch_instances()

            if self.dex_section_version != u"000":
                pass



    class Header027(KaitaiStruct):
        SEQ_FIELDS = ["num_sections", "sections"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vdex.Header027, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_sections']['start'] = self._io.pos()
            self.num_sections = self._io.read_u4le()
            self._debug['num_sections']['end'] = self._io.pos()
            if not self.num_sections == 4:
                raise kaitaistruct.ValidationNotEqualError(4, self.num_sections, self._io, u"/types/header_027/seq/0")
            self._debug['sections']['start'] = self._io.pos()
            self._debug['sections']['arr'] = []
            self.sections = []
            for i in range(self.num_sections):
                self._debug['sections']['arr'].append({'start': self._io.pos()})
                self.sections.append(Vdex.Section027(self._io, self, self._root))
                self._debug['sections']['arr'][i]['end'] = self._io.pos()

            self._debug['sections']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.sections)):
                pass
                self.sections[i]._fetch_instances()



    class Section027(KaitaiStruct):
        SEQ_FIELDS = ["section_kind", "ofs_section", "len_section"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Vdex.Section027, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['section_kind']['start'] = self._io.pos()
            self.section_kind = KaitaiStream.resolve_enum(Vdex.VdexSection, self._io.read_u4le())
            self._debug['section_kind']['end'] = self._io.pos()
            self._debug['ofs_section']['start'] = self._io.pos()
            self.ofs_section = self._io.read_u4le()
            self._debug['ofs_section']['end'] = self._io.pos()
            self._debug['len_section']['start'] = self._io.pos()
            self.len_section = self._io.read_u4le()
            self._debug['len_section']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.section
            if hasattr(self, '_m_section'):
                pass


        @property
        def section(self):
            if hasattr(self, '_m_section'):
                return self._m_section

            if self.ofs_section != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_section)
                self._debug['_m_section']['start'] = io.pos()
                self._m_section = io.read_bytes(self.len_section)
                self._debug['_m_section']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_section', None)



