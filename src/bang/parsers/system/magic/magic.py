# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Magic(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/file/file/blob/master/src/file.h
    
    
    .. seealso::
       Source - https://github.com/file/file/blob/master/src/apprentice.c
    """

    class ComparisonTypes(IntEnum):
        file_invalid = 0
        file_byte = 1
        file_short = 2
        file_default = 3
        file_long = 4
        file_string = 5
        file_date = 6
        file_beshort = 7
        file_belong = 8
        file_bedate = 9
        file_leshort = 10
        file_lelong = 11
        file_ledate = 12
        file_pstring = 13
        file_ldate = 14
        file_beldate = 15
        file_leldate = 16
        file_regex = 17
        file_bestring16 = 18
        file_lestring16 = 19
        file_search = 20
        file_medate = 21
        file_meldate = 22
        file_melong = 23
        file_quad = 24
        file_lequad = 25
        file_bequad = 26
        file_qdate = 27
        file_leqdate = 28
        file_beqdate = 29
        file_qldate = 30
        file_leqldate = 31
        file_beqldate = 32
        file_float = 33
        file_befloat = 34
        file_lefloat = 35
        file_double = 36
        file_bedouble = 37
        file_ledouble = 38
        file_beid3 = 39
        file_leid3 = 40
        file_indirect = 41
        file_qwdate = 42
        file_leqwdate = 43
        file_beqwdate = 44
        file_name = 45
        file_use = 46
        file_clear = 47
        file_der = 48
        file_guid = 49
        file_offset = 50
        file_bevarint = 51
        file_levarint = 52
        file_msdosdate = 53
        file_lemsdosdate = 54
        file_bemsdosdate = 55
        file_msdostime = 56
        file_lemsdostime = 57
        file_bemsdostime = 58
        file_octal = 59
    SEQ_FIELDS = ["header", "magic"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Magic, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Magic.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['magic']['start'] = self._io.pos()
        self._debug['magic']['arr'] = []
        self.magic = []
        i = 0
        while True:
            self._debug['magic']['arr'].append({'start': self._io.pos()})
            _ = Magic.MagicType(self._io, self, self._root)
            self.magic.append(_)
            self._debug['magic']['arr'][len(self.magic) - 1]['end'] = self._io.pos()
            if self._io.is_eof():
                break
            i += 1
        self._debug['magic']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.magic)):
            pass
            self.magic[i]._fetch_instances()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["signature", "version", "rest_of_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Magic.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(4)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x1C\x04\x1E\xF1":
                raise kaitaistruct.ValidationNotEqualError(b"\x1C\x04\x1E\xF1", self.signature, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            if not  ((self.version == 12) or (self.version == 13) or (self.version == 14) or (self.version == 15) or (self.version == 16) or (self.version == 17) or (self.version == 18)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/types/header/seq/1")
            self._debug['rest_of_header']['start'] = self._io.pos()
            _on = self.version
            if _on == 12:
                pass
                self.rest_of_header = Magic.Header12(self._io, self, self._root)
            elif _on == 13:
                pass
                self.rest_of_header = Magic.Header13(self._io, self, self._root)
            elif _on == 14:
                pass
                self.rest_of_header = Magic.Header14(self._io, self, self._root)
            elif _on == 15:
                pass
                self.rest_of_header = Magic.Header15(self._io, self, self._root)
            elif _on == 16:
                pass
                self.rest_of_header = Magic.Header15(self._io, self, self._root)
            elif _on == 17:
                pass
                self.rest_of_header = Magic.Header15(self._io, self, self._root)
            elif _on == 18:
                pass
                self.rest_of_header = Magic.Header15(self._io, self, self._root)
            self._debug['rest_of_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.version
            if _on == 12:
                pass
                self.rest_of_header._fetch_instances()
            elif _on == 13:
                pass
                self.rest_of_header._fetch_instances()
            elif _on == 14:
                pass
                self.rest_of_header._fetch_instances()
            elif _on == 15:
                pass
                self.rest_of_header._fetch_instances()
            elif _on == 16:
                pass
                self.rest_of_header._fetch_instances()
            elif _on == 17:
                pass
                self.rest_of_header._fetch_instances()
            elif _on == 18:
                pass
                self.rest_of_header._fetch_instances()


    class Header12(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Magic.Header12, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(240)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header13(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Magic.Header13, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(304)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header14(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Magic.Header14, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(336)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header15(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Magic.Header15, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(368)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class MagicType(KaitaiStruct):
        SEQ_FIELDS = ["common", "version_specific"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Magic.MagicType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['common']['start'] = self._io.pos()
            self.common = Magic.MagicTypeCommon(self._io, self, self._root)
            self._debug['common']['end'] = self._io.pos()
            self._debug['version_specific']['start'] = self._io.pos()
            _on = self._root.header.version
            if _on == 12:
                pass
                self.version_specific = Magic.MagicType1213(self._io, self, self._root)
            elif _on == 13:
                pass
                self.version_specific = Magic.MagicType1213(self._io, self, self._root)
            elif _on == 14:
                pass
                self.version_specific = Magic.MagicType14(self._io, self, self._root)
            elif _on == 15:
                pass
                self.version_specific = Magic.MagicType15(self._io, self, self._root)
            elif _on == 16:
                pass
                self.version_specific = Magic.MagicType15(self._io, self, self._root)
            elif _on == 17:
                pass
                self.version_specific = Magic.MagicType15(self._io, self, self._root)
            elif _on == 18:
                pass
                self.version_specific = Magic.MagicType15(self._io, self, self._root)
            self._debug['version_specific']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.common._fetch_instances()
            _on = self._root.header.version
            if _on == 12:
                pass
                self.version_specific._fetch_instances()
            elif _on == 13:
                pass
                self.version_specific._fetch_instances()
            elif _on == 14:
                pass
                self.version_specific._fetch_instances()
            elif _on == 15:
                pass
                self.version_specific._fetch_instances()
            elif _on == 16:
                pass
                self.version_specific._fetch_instances()
            elif _on == 17:
                pass
                self.version_specific._fetch_instances()
            elif _on == 18:
                pass
                self.version_specific._fetch_instances()


    class MagicType1213(KaitaiStruct):
        SEQ_FIELDS = ["value", "description", "mimetype", "apple_creator_type", "extensions"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Magic.MagicType1213, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            _on = self._parent.common.is_string
            if _on == True:
                pass
                self.value = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"ASCII")
            else:
                pass
                self.value = self._io.read_bytes(64)
            self._debug['value']['end'] = self._io.pos()
            self._debug['description']['start'] = self._io.pos()
            self.description = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"ASCII")
            self._debug['description']['end'] = self._io.pos()
            self._debug['mimetype']['start'] = self._io.pos()
            self.mimetype = (KaitaiStream.bytes_terminate(self._io.read_bytes(80), 0, False)).decode(u"ASCII")
            self._debug['mimetype']['end'] = self._io.pos()
            self._debug['apple_creator_type']['start'] = self._io.pos()
            self.apple_creator_type = (KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)).decode(u"ASCII")
            self._debug['apple_creator_type']['end'] = self._io.pos()
            if self._root.header.version > 12:
                pass
                self._debug['extensions']['start'] = self._io.pos()
                self.extensions = self._io.read_bytes(64)
                self._debug['extensions']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            _on = self._parent.common.is_string
            if _on == True:
                pass
            else:
                pass
            if self._root.header.version > 12:
                pass



    class MagicType14(KaitaiStruct):
        SEQ_FIELDS = ["value", "description", "mimetype", "apple_creator_type", "extensions"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Magic.MagicType14, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            _on = self._parent.common.is_string
            if _on == True:
                pass
                self.value = (KaitaiStream.bytes_terminate(self._io.read_bytes(96), 0, False)).decode(u"ASCII")
            else:
                pass
                self.value = self._io.read_bytes(96)
            self._debug['value']['end'] = self._io.pos()
            self._debug['description']['start'] = self._io.pos()
            self.description = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"ASCII")
            self._debug['description']['end'] = self._io.pos()
            self._debug['mimetype']['start'] = self._io.pos()
            self.mimetype = (KaitaiStream.bytes_terminate(self._io.read_bytes(80), 0, False)).decode(u"ASCII")
            self._debug['mimetype']['end'] = self._io.pos()
            self._debug['apple_creator_type']['start'] = self._io.pos()
            self.apple_creator_type = (KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)).decode(u"ASCII")
            self._debug['apple_creator_type']['end'] = self._io.pos()
            self._debug['extensions']['start'] = self._io.pos()
            self.extensions = self._io.read_bytes(64)
            self._debug['extensions']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self._parent.common.is_string
            if _on == True:
                pass
            else:
                pass


    class MagicType15(KaitaiStruct):
        SEQ_FIELDS = ["value", "description", "mimetype", "apple_creator_type", "extensions"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Magic.MagicType15, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            _on = self._parent.common.is_string
            if _on == True:
                pass
                self.value = (KaitaiStream.bytes_terminate(self._io.read_bytes(128), 0, False)).decode(u"ASCII")
            else:
                pass
                self.value = self._io.read_bytes(128)
            self._debug['value']['end'] = self._io.pos()
            self._debug['description']['start'] = self._io.pos()
            self.description = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"ASCII")
            self._debug['description']['end'] = self._io.pos()
            self._debug['mimetype']['start'] = self._io.pos()
            self.mimetype = (KaitaiStream.bytes_terminate(self._io.read_bytes(80), 0, False)).decode(u"ASCII")
            self._debug['mimetype']['end'] = self._io.pos()
            self._debug['apple_creator_type']['start'] = self._io.pos()
            self.apple_creator_type = (KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)).decode(u"ASCII")
            self._debug['apple_creator_type']['end'] = self._io.pos()
            self._debug['extensions']['start'] = self._io.pos()
            self.extensions = self._io.read_bytes(64)
            self._debug['extensions']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self._parent.common.is_string
            if _on == True:
                pass
            else:
                pass


    class MagicTypeCommon(KaitaiStruct):
        SEQ_FIELDS = ["continuation_level", "flag", "factor", "relation", "len_string", "comparison_type", "indirection_type", "indirection_operator", "mask_operator", "conditional_or_dummy", "factor_operator", "ofs_magic_number", "ofs_from_indirection", "line_number", "mask", "line_count", "modifier_flags"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Magic.MagicTypeCommon, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['continuation_level']['start'] = self._io.pos()
            self.continuation_level = self._io.read_u2le()
            self._debug['continuation_level']['end'] = self._io.pos()
            self._debug['flag']['start'] = self._io.pos()
            self.flag = self._io.read_u1()
            self._debug['flag']['end'] = self._io.pos()
            self._debug['factor']['start'] = self._io.pos()
            self.factor = self._io.read_u1()
            self._debug['factor']['end'] = self._io.pos()
            self._debug['relation']['start'] = self._io.pos()
            self.relation = self._io.read_u1()
            self._debug['relation']['end'] = self._io.pos()
            self._debug['len_string']['start'] = self._io.pos()
            self.len_string = self._io.read_u1()
            self._debug['len_string']['end'] = self._io.pos()
            self._debug['comparison_type']['start'] = self._io.pos()
            self.comparison_type = KaitaiStream.resolve_enum(Magic.ComparisonTypes, self._io.read_u1())
            self._debug['comparison_type']['end'] = self._io.pos()
            self._debug['indirection_type']['start'] = self._io.pos()
            self.indirection_type = self._io.read_u1()
            self._debug['indirection_type']['end'] = self._io.pos()
            self._debug['indirection_operator']['start'] = self._io.pos()
            self.indirection_operator = self._io.read_u1()
            self._debug['indirection_operator']['end'] = self._io.pos()
            self._debug['mask_operator']['start'] = self._io.pos()
            self.mask_operator = self._io.read_u1()
            self._debug['mask_operator']['end'] = self._io.pos()
            self._debug['conditional_or_dummy']['start'] = self._io.pos()
            self.conditional_or_dummy = self._io.read_u1()
            self._debug['conditional_or_dummy']['end'] = self._io.pos()
            self._debug['factor_operator']['start'] = self._io.pos()
            self.factor_operator = self._io.read_u1()
            self._debug['factor_operator']['end'] = self._io.pos()
            self._debug['ofs_magic_number']['start'] = self._io.pos()
            self.ofs_magic_number = self._io.read_u4le()
            self._debug['ofs_magic_number']['end'] = self._io.pos()
            self._debug['ofs_from_indirection']['start'] = self._io.pos()
            self.ofs_from_indirection = self._io.read_u4le()
            self._debug['ofs_from_indirection']['end'] = self._io.pos()
            self._debug['line_number']['start'] = self._io.pos()
            self.line_number = self._io.read_u4le()
            self._debug['line_number']['end'] = self._io.pos()
            if (not (self.is_string)):
                pass
                self._debug['mask']['start'] = self._io.pos()
                self.mask = self._io.read_u8le()
                self._debug['mask']['end'] = self._io.pos()

            if self.is_string:
                pass
                self._debug['line_count']['start'] = self._io.pos()
                self.line_count = self._io.read_u4le()
                self._debug['line_count']['end'] = self._io.pos()

            if self.is_string:
                pass
                self._debug['modifier_flags']['start'] = self._io.pos()
                self.modifier_flags = self._io.read_u4le()
                self._debug['modifier_flags']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if (not (self.is_string)):
                pass

            if self.is_string:
                pass

            if self.is_string:
                pass


        @property
        def bin_test(self):
            if hasattr(self, '_m_bin_test'):
                return self._m_bin_test

            self._m_bin_test = self.flag & 32 == 32
            return getattr(self, '_m_bin_test', None)

        @property
        def in_dir(self):
            if hasattr(self, '_m_in_dir'):
                return self._m_in_dir

            self._m_in_dir = self.flag & 1 == 1
            return getattr(self, '_m_in_dir', None)

        @property
        def indir_off_add(self):
            if hasattr(self, '_m_indir_off_add'):
                return self._m_indir_off_add

            self._m_indir_off_add = self.flag & 4 == 4
            return getattr(self, '_m_indir_off_add', None)

        @property
        def is_string(self):
            if hasattr(self, '_m_is_string'):
                return self._m_is_string

            self._m_is_string =  ((self.comparison_type == Magic.ComparisonTypes.file_string) or (self.comparison_type == Magic.ComparisonTypes.file_pstring) or (self.comparison_type == Magic.ComparisonTypes.file_bestring16) or (self.comparison_type == Magic.ComparisonTypes.file_lestring16) or (self.comparison_type == Magic.ComparisonTypes.file_regex) or (self.comparison_type == Magic.ComparisonTypes.file_search) or (self.comparison_type == Magic.ComparisonTypes.file_indirect) or (self.comparison_type == Magic.ComparisonTypes.file_name) or (self.comparison_type == Magic.ComparisonTypes.file_use)) 
            return getattr(self, '_m_is_string', None)

        @property
        def no_space(self):
            if hasattr(self, '_m_no_space'):
                return self._m_no_space

            self._m_no_space = self.flag & 16 == 16
            return getattr(self, '_m_no_space', None)

        @property
        def off_add(self):
            if hasattr(self, '_m_off_add'):
                return self._m_off_add

            self._m_off_add = self.flag & 2 == 2
            return getattr(self, '_m_off_add', None)

        @property
        def off_negative(self):
            if hasattr(self, '_m_off_negative'):
                return self._m_off_negative

            self._m_off_negative = self.flag & 128 == 128
            return getattr(self, '_m_off_negative', None)

        @property
        def text_test(self):
            if hasattr(self, '_m_text_test'):
                return self._m_text_test

            self._m_text_test = self.flag & 64 == 64
            return getattr(self, '_m_text_test', None)

        @property
        def unsigned(self):
            if hasattr(self, '_m_unsigned'):
                return self._m_unsigned

            self._m_unsigned = self.flag & 8 == 8
            return getattr(self, '_m_unsigned', None)



