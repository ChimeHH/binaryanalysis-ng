# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Eot(KaitaiStruct):
    """
    .. seealso::
       Source - https://www.w3.org/submissions/2008/SUBM-EOT-20080305/
    """
    SEQ_FIELDS = ["header", "font_data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Eot, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Eot.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['font_data']['start'] = self._io.pos()
        self.font_data = self._io.read_bytes(self.header.len_data_size)
        self._debug['font_data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["len_eot", "len_data_size", "version", "processing_flags", "font_panose", "charset", "italic", "weight", "fs_type", "magic_number", "unicode_range_1", "unicode_range_2", "unicode_range_3", "unicode_range_4", "codepage_range_1", "codepage_range_2", "checksum_adjustment", "reserved_1", "reserved_2", "reserved_3", "reserved_4", "padding_1", "len_family_name", "family_name", "padding_2", "len_style_name", "style_name", "padding_3", "len_version_name", "version_name", "padding_4", "len_full_name", "full_name", "padding_5", "len_root_string", "root_string", "version_header_22"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Eot.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_eot']['start'] = self._io.pos()
            self.len_eot = self._io.read_u4le()
            self._debug['len_eot']['end'] = self._io.pos()
            self._debug['len_data_size']['start'] = self._io.pos()
            self.len_data_size = self._io.read_u4le()
            self._debug['len_data_size']['end'] = self._io.pos()
            if not self.len_data_size >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.len_data_size, self._io, u"/types/header/seq/1")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            if not  ((self.version == 131073) or (self.version == 131074)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/types/header/seq/2")
            self._debug['processing_flags']['start'] = self._io.pos()
            self.processing_flags = self._io.read_u4le()
            self._debug['processing_flags']['end'] = self._io.pos()
            self._debug['font_panose']['start'] = self._io.pos()
            self.font_panose = self._io.read_bytes(10)
            self._debug['font_panose']['end'] = self._io.pos()
            self._debug['charset']['start'] = self._io.pos()
            self.charset = self._io.read_u1()
            self._debug['charset']['end'] = self._io.pos()
            self._debug['italic']['start'] = self._io.pos()
            self.italic = self._io.read_u1()
            self._debug['italic']['end'] = self._io.pos()
            self._debug['weight']['start'] = self._io.pos()
            self.weight = self._io.read_u4le()
            self._debug['weight']['end'] = self._io.pos()
            self._debug['fs_type']['start'] = self._io.pos()
            self.fs_type = self._io.read_u2le()
            self._debug['fs_type']['end'] = self._io.pos()
            self._debug['magic_number']['start'] = self._io.pos()
            self.magic_number = self._io.read_bytes(2)
            self._debug['magic_number']['end'] = self._io.pos()
            if not self.magic_number == b"\x4C\x50":
                raise kaitaistruct.ValidationNotEqualError(b"\x4C\x50", self.magic_number, self._io, u"/types/header/seq/9")
            self._debug['unicode_range_1']['start'] = self._io.pos()
            self.unicode_range_1 = self._io.read_u4le()
            self._debug['unicode_range_1']['end'] = self._io.pos()
            self._debug['unicode_range_2']['start'] = self._io.pos()
            self.unicode_range_2 = self._io.read_u4le()
            self._debug['unicode_range_2']['end'] = self._io.pos()
            self._debug['unicode_range_3']['start'] = self._io.pos()
            self.unicode_range_3 = self._io.read_u4le()
            self._debug['unicode_range_3']['end'] = self._io.pos()
            self._debug['unicode_range_4']['start'] = self._io.pos()
            self.unicode_range_4 = self._io.read_u4le()
            self._debug['unicode_range_4']['end'] = self._io.pos()
            self._debug['codepage_range_1']['start'] = self._io.pos()
            self.codepage_range_1 = self._io.read_u4le()
            self._debug['codepage_range_1']['end'] = self._io.pos()
            self._debug['codepage_range_2']['start'] = self._io.pos()
            self.codepage_range_2 = self._io.read_u4le()
            self._debug['codepage_range_2']['end'] = self._io.pos()
            self._debug['checksum_adjustment']['start'] = self._io.pos()
            self.checksum_adjustment = self._io.read_u4le()
            self._debug['checksum_adjustment']['end'] = self._io.pos()
            self._debug['reserved_1']['start'] = self._io.pos()
            self.reserved_1 = self._io.read_u4le()
            self._debug['reserved_1']['end'] = self._io.pos()
            if not self.reserved_1 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.reserved_1, self._io, u"/types/header/seq/17")
            self._debug['reserved_2']['start'] = self._io.pos()
            self.reserved_2 = self._io.read_u4le()
            self._debug['reserved_2']['end'] = self._io.pos()
            if not self.reserved_2 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.reserved_2, self._io, u"/types/header/seq/18")
            self._debug['reserved_3']['start'] = self._io.pos()
            self.reserved_3 = self._io.read_u4le()
            self._debug['reserved_3']['end'] = self._io.pos()
            if not self.reserved_3 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.reserved_3, self._io, u"/types/header/seq/19")
            self._debug['reserved_4']['start'] = self._io.pos()
            self.reserved_4 = self._io.read_u4le()
            self._debug['reserved_4']['end'] = self._io.pos()
            if not self.reserved_4 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.reserved_4, self._io, u"/types/header/seq/20")
            self._debug['padding_1']['start'] = self._io.pos()
            self.padding_1 = self._io.read_u2le()
            self._debug['padding_1']['end'] = self._io.pos()
            if not self.padding_1 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.padding_1, self._io, u"/types/header/seq/21")
            self._debug['len_family_name']['start'] = self._io.pos()
            self.len_family_name = self._io.read_u2le()
            self._debug['len_family_name']['end'] = self._io.pos()
            self._debug['family_name']['start'] = self._io.pos()
            self.family_name = (self._io.read_bytes(self.len_family_name)).decode(u"utf-16")
            self._debug['family_name']['end'] = self._io.pos()
            self._debug['padding_2']['start'] = self._io.pos()
            self.padding_2 = self._io.read_u2le()
            self._debug['padding_2']['end'] = self._io.pos()
            if not self.padding_2 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.padding_2, self._io, u"/types/header/seq/24")
            self._debug['len_style_name']['start'] = self._io.pos()
            self.len_style_name = self._io.read_u2le()
            self._debug['len_style_name']['end'] = self._io.pos()
            self._debug['style_name']['start'] = self._io.pos()
            self.style_name = (self._io.read_bytes(self.len_style_name)).decode(u"utf-16")
            self._debug['style_name']['end'] = self._io.pos()
            self._debug['padding_3']['start'] = self._io.pos()
            self.padding_3 = self._io.read_u2le()
            self._debug['padding_3']['end'] = self._io.pos()
            if not self.padding_3 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.padding_3, self._io, u"/types/header/seq/27")
            self._debug['len_version_name']['start'] = self._io.pos()
            self.len_version_name = self._io.read_u2le()
            self._debug['len_version_name']['end'] = self._io.pos()
            self._debug['version_name']['start'] = self._io.pos()
            self.version_name = (self._io.read_bytes(self.len_version_name)).decode(u"utf-16")
            self._debug['version_name']['end'] = self._io.pos()
            self._debug['padding_4']['start'] = self._io.pos()
            self.padding_4 = self._io.read_u2le()
            self._debug['padding_4']['end'] = self._io.pos()
            if not self.padding_4 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.padding_4, self._io, u"/types/header/seq/30")
            self._debug['len_full_name']['start'] = self._io.pos()
            self.len_full_name = self._io.read_u2le()
            self._debug['len_full_name']['end'] = self._io.pos()
            self._debug['full_name']['start'] = self._io.pos()
            self.full_name = (self._io.read_bytes(self.len_full_name)).decode(u"utf-16")
            self._debug['full_name']['end'] = self._io.pos()
            self._debug['padding_5']['start'] = self._io.pos()
            self.padding_5 = self._io.read_u2le()
            self._debug['padding_5']['end'] = self._io.pos()
            if not self.padding_5 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.padding_5, self._io, u"/types/header/seq/33")
            self._debug['len_root_string']['start'] = self._io.pos()
            self.len_root_string = self._io.read_u2le()
            self._debug['len_root_string']['end'] = self._io.pos()
            self._debug['root_string']['start'] = self._io.pos()
            self.root_string = (self._io.read_bytes(self.len_root_string)).decode(u"utf-16")
            self._debug['root_string']['end'] = self._io.pos()
            if self.version == 131074:
                pass
                self._debug['version_header_22']['start'] = self._io.pos()
                self.version_header_22 = Eot.VersionHeader22(self._io, self, self._root)
                self._debug['version_header_22']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.version == 131074:
                pass
                self.version_header_22._fetch_instances()



    class VersionHeader22(KaitaiStruct):
        SEQ_FIELDS = ["root_string_checksum", "eucd_code_page", "padding_6", "len_signature", "signature", "eucd_flags", "len_eucd_font", "eucd_font_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Eot.VersionHeader22, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['root_string_checksum']['start'] = self._io.pos()
            self.root_string_checksum = self._io.read_u4le()
            self._debug['root_string_checksum']['end'] = self._io.pos()
            self._debug['eucd_code_page']['start'] = self._io.pos()
            self.eucd_code_page = self._io.read_u4le()
            self._debug['eucd_code_page']['end'] = self._io.pos()
            self._debug['padding_6']['start'] = self._io.pos()
            self.padding_6 = self._io.read_u2le()
            self._debug['padding_6']['end'] = self._io.pos()
            if not self.padding_6 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.padding_6, self._io, u"/types/version_header_22/seq/2")
            self._debug['len_signature']['start'] = self._io.pos()
            self.len_signature = self._io.read_u2le()
            self._debug['len_signature']['end'] = self._io.pos()
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(self.len_signature)
            self._debug['signature']['end'] = self._io.pos()
            self._debug['eucd_flags']['start'] = self._io.pos()
            self.eucd_flags = self._io.read_u4le()
            self._debug['eucd_flags']['end'] = self._io.pos()
            self._debug['len_eucd_font']['start'] = self._io.pos()
            self.len_eucd_font = self._io.read_u4le()
            self._debug['len_eucd_font']['end'] = self._io.pos()
            self._debug['eucd_font_data']['start'] = self._io.pos()
            self.eucd_font_data = self._io.read_bytes(self.len_eucd_font)
            self._debug['eucd_font_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



