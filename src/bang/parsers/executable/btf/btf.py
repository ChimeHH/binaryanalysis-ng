# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Btf(KaitaiStruct):
    """
    .. seealso::
       Source - https://docs.kernel.org/bpf/btf.html
    """

    class Kind(IntEnum):
        void = 0
        integer = 1
        pointer = 2
        array = 3
        struct = 4
        union = 5
        enum = 6
        forward = 7
        typedef = 8
        volatile = 9
        const = 10
        restrict = 11
        function = 12
        function_proto = 13
        variable = 14
        section = 15
        floating_point = 16
        decl_tag = 17
        type_tag = 18
        enum64 = 19
    SEQ_FIELDS = ["header", "type_section", "string_section"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Btf, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Btf.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['type_section']['start'] = self._io.pos()
        self.type_section = self._io.read_bytes(self.header.rest_of_header.len_type_section)
        self._debug['type_section']['end'] = self._io.pos()
        self._debug['string_section']['start'] = self._io.pos()
        self._raw_string_section = self._io.read_bytes(self.header.rest_of_header.len_string_section)
        _io__raw_string_section = KaitaiStream(BytesIO(self._raw_string_section))
        self.string_section = Btf.StringSection(_io__raw_string_section, self, self._root)
        self._debug['string_section']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.string_section._fetch_instances()

    class BtfKindArray(KaitaiStruct):
        SEQ_FIELDS = ["btf_array"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Btf.BtfKindArray, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['btf_array']['start'] = self._io.pos()
            self.btf_array = Btf.BtfKindArray.BtfArray(self._io, self, self._root)
            self._debug['btf_array']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.btf_array._fetch_instances()

        class BtfArray(KaitaiStruct):
            SEQ_FIELDS = ["type", "index_type", "num_elems"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Btf.BtfKindArray.BtfArray, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['type']['start'] = self._io.pos()
                self.type = KaitaiStream.resolve_enum(Btf.Kind, self._io.read_u4le())
                self._debug['type']['end'] = self._io.pos()
                self._debug['index_type']['start'] = self._io.pos()
                self.index_type = self._io.read_u4le()
                self._debug['index_type']['end'] = self._io.pos()
                self._debug['num_elems']['start'] = self._io.pos()
                self.num_elems = self._io.read_u4le()
                self._debug['num_elems']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass



    class BtfKindDeclTag(KaitaiStruct):
        SEQ_FIELDS = ["component_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Btf.BtfKindDeclTag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['component_idx']['start'] = self._io.pos()
            self.component_idx = self._io.read_u4le()
            self._debug['component_idx']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class BtfKindEnum(KaitaiStruct):
        SEQ_FIELDS = ["enums"]
        def __init__(self, num_enums, _io, _parent=None, _root=None):
            super(Btf.BtfKindEnum, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_enums = num_enums
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['enums']['start'] = self._io.pos()
            self._debug['enums']['arr'] = []
            self.enums = []
            for i in range(self.num_enums):
                self._debug['enums']['arr'].append({'start': self._io.pos()})
                self.enums.append(Btf.BtfKindEnum.BtfEnum(self._io, self, self._root))
                self._debug['enums']['arr'][i]['end'] = self._io.pos()

            self._debug['enums']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.enums)):
                pass
                self.enums[i]._fetch_instances()


        class BtfEnum(KaitaiStruct):
            SEQ_FIELDS = ["ofs_name", "val"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Btf.BtfKindEnum.BtfEnum, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['ofs_name']['start'] = self._io.pos()
                self.ofs_name = self._io.read_u4le()
                self._debug['ofs_name']['end'] = self._io.pos()
                self._debug['val']['start'] = self._io.pos()
                self.val = self._io.read_s4le()
                self._debug['val']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _ = self.name
                if hasattr(self, '_m_name'):
                    pass


            @property
            def name(self):
                if hasattr(self, '_m_name'):
                    return self._m_name

                io = self._root.string_section._io
                _pos = io.pos()
                io.seek(self.ofs_name)
                self._debug['_m_name']['start'] = io.pos()
                self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self._debug['_m_name']['end'] = io.pos()
                io.seek(_pos)
                return getattr(self, '_m_name', None)



    class BtfKindEnum64(KaitaiStruct):
        SEQ_FIELDS = ["enums"]
        def __init__(self, num_enums, _io, _parent=None, _root=None):
            super(Btf.BtfKindEnum64, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_enums = num_enums
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['enums']['start'] = self._io.pos()
            self._debug['enums']['arr'] = []
            self.enums = []
            for i in range(self.num_enums):
                self._debug['enums']['arr'].append({'start': self._io.pos()})
                self.enums.append(Btf.BtfKindEnum64.BtfEnum64(self._io, self, self._root))
                self._debug['enums']['arr'][i]['end'] = self._io.pos()

            self._debug['enums']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.enums)):
                pass
                self.enums[i]._fetch_instances()


        class BtfEnum64(KaitaiStruct):
            SEQ_FIELDS = ["ofs_name", "val_lo32", "val_hi32"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Btf.BtfKindEnum64.BtfEnum64, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['ofs_name']['start'] = self._io.pos()
                self.ofs_name = self._io.read_u4le()
                self._debug['ofs_name']['end'] = self._io.pos()
                self._debug['val_lo32']['start'] = self._io.pos()
                self.val_lo32 = self._io.read_u4le()
                self._debug['val_lo32']['end'] = self._io.pos()
                self._debug['val_hi32']['start'] = self._io.pos()
                self.val_hi32 = self._io.read_u4le()
                self._debug['val_hi32']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _ = self.name
                if hasattr(self, '_m_name'):
                    pass


            @property
            def name(self):
                if hasattr(self, '_m_name'):
                    return self._m_name

                io = self._root.string_section._io
                _pos = io.pos()
                io.seek(self.ofs_name)
                self._debug['_m_name']['start'] = io.pos()
                self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self._debug['_m_name']['end'] = io.pos()
                io.seek(_pos)
                return getattr(self, '_m_name', None)



    class BtfKindFunctionProto(KaitaiStruct):
        SEQ_FIELDS = ["function_protos"]
        def __init__(self, num_function_protos, _io, _parent=None, _root=None):
            super(Btf.BtfKindFunctionProto, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_function_protos = num_function_protos
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['function_protos']['start'] = self._io.pos()
            self._debug['function_protos']['arr'] = []
            self.function_protos = []
            for i in range(self.num_function_protos):
                self._debug['function_protos']['arr'].append({'start': self._io.pos()})
                self.function_protos.append(Btf.BtfKindFunctionProto.BtfFunctionProto(self._io, self, self._root))
                self._debug['function_protos']['arr'][i]['end'] = self._io.pos()

            self._debug['function_protos']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.function_protos)):
                pass
                self.function_protos[i]._fetch_instances()


        class BtfFunctionProto(KaitaiStruct):
            SEQ_FIELDS = ["ofs_name", "type"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Btf.BtfKindFunctionProto.BtfFunctionProto, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['ofs_name']['start'] = self._io.pos()
                self.ofs_name = self._io.read_u4le()
                self._debug['ofs_name']['end'] = self._io.pos()
                self._debug['type']['start'] = self._io.pos()
                self.type = self._io.read_u4le()
                self._debug['type']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _ = self.name
                if hasattr(self, '_m_name'):
                    pass


            @property
            def name(self):
                if hasattr(self, '_m_name'):
                    return self._m_name

                io = self._root.string_section._io
                _pos = io.pos()
                io.seek(self.ofs_name)
                self._debug['_m_name']['start'] = io.pos()
                self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self._debug['_m_name']['end'] = io.pos()
                io.seek(_pos)
                return getattr(self, '_m_name', None)



    class BtfKindInt(KaitaiStruct):

        class BitEncodings(IntEnum):
            signed = 1
            char = 2
            bool = 4
        SEQ_FIELDS = ["int_flags"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Btf.BtfKindInt, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['int_flags']['start'] = self._io.pos()
            self.int_flags = self._io.read_u4le()
            self._debug['int_flags']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def int_bits(self):
            if hasattr(self, '_m_int_bits'):
                return self._m_int_bits

            self._m_int_bits = self.int_flags & 255
            return getattr(self, '_m_int_bits', None)

        @property
        def int_encoding(self):
            if hasattr(self, '_m_int_encoding'):
                return self._m_int_encoding

            self._m_int_encoding = KaitaiStream.resolve_enum(Btf.BtfKindInt.BitEncodings, (self.int_flags & 251658240) >> 24)
            return getattr(self, '_m_int_encoding', None)

        @property
        def int_offset(self):
            if hasattr(self, '_m_int_offset'):
                return self._m_int_offset

            self._m_int_offset = (self.int_flags & 16711680) >> 16
            return getattr(self, '_m_int_offset', None)


    class BtfKindSection(KaitaiStruct):
        SEQ_FIELDS = ["sections"]
        def __init__(self, num_sections, _io, _parent=None, _root=None):
            super(Btf.BtfKindSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_sections = num_sections
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['sections']['start'] = self._io.pos()
            self._debug['sections']['arr'] = []
            self.sections = []
            for i in range(self.num_sections):
                self._debug['sections']['arr'].append({'start': self._io.pos()})
                self.sections.append(Btf.BtfKindSection.BtfSection(self._io, self, self._root))
                self._debug['sections']['arr'][i]['end'] = self._io.pos()

            self._debug['sections']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.sections)):
                pass
                self.sections[i]._fetch_instances()


        class BtfSection(KaitaiStruct):
            SEQ_FIELDS = ["type", "offset", "size"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Btf.BtfKindSection.BtfSection, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['type']['start'] = self._io.pos()
                self.type = self._io.read_u4le()
                self._debug['type']['end'] = self._io.pos()
                self._debug['offset']['start'] = self._io.pos()
                self.offset = self._io.read_u4le()
                self._debug['offset']['end'] = self._io.pos()
                self._debug['size']['start'] = self._io.pos()
                self.size = self._io.read_u4le()
                self._debug['size']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass



    class BtfKindUnion(KaitaiStruct):
        SEQ_FIELDS = ["members"]
        def __init__(self, num_members, _io, _parent=None, _root=None):
            super(Btf.BtfKindUnion, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_members = num_members
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['members']['start'] = self._io.pos()
            self._debug['members']['arr'] = []
            self.members = []
            for i in range(self.num_members):
                self._debug['members']['arr'].append({'start': self._io.pos()})
                self.members.append(Btf.BtfKindUnion.Member(self._io, self, self._root))
                self._debug['members']['arr'][i]['end'] = self._io.pos()

            self._debug['members']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.members)):
                pass
                self.members[i]._fetch_instances()


        class Member(KaitaiStruct):
            SEQ_FIELDS = ["ofs_name", "type", "member_offset"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Btf.BtfKindUnion.Member, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['ofs_name']['start'] = self._io.pos()
                self.ofs_name = self._io.read_u4le()
                self._debug['ofs_name']['end'] = self._io.pos()
                self._debug['type']['start'] = self._io.pos()
                self.type = KaitaiStream.resolve_enum(Btf.Kind, self._io.read_u4le())
                self._debug['type']['end'] = self._io.pos()
                self._debug['member_offset']['start'] = self._io.pos()
                self.member_offset = self._io.read_u4le()
                self._debug['member_offset']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                _ = self.name
                if hasattr(self, '_m_name'):
                    pass


            @property
            def name(self):
                if hasattr(self, '_m_name'):
                    return self._m_name

                io = self._root.string_section._io
                _pos = io.pos()
                io.seek(self.ofs_name)
                self._debug['_m_name']['start'] = io.pos()
                self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self._debug['_m_name']['end'] = io.pos()
                io.seek(_pos)
                return getattr(self, '_m_name', None)



    class BtfKindVariable(KaitaiStruct):
        SEQ_FIELDS = ["linkage"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Btf.BtfKindVariable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['linkage']['start'] = self._io.pos()
            self.linkage = self._io.read_u4le()
            self._debug['linkage']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class BtfType(KaitaiStruct):
        SEQ_FIELDS = ["ofs_name", "info", "size_or_type", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Btf.BtfType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_name']['start'] = self._io.pos()
            self.ofs_name = self._io.read_u4le()
            self._debug['ofs_name']['end'] = self._io.pos()
            self._debug['info']['start'] = self._io.pos()
            self.info = Btf.Info(self._io, self, self._root)
            self._debug['info']['end'] = self._io.pos()
            self._debug['size_or_type']['start'] = self._io.pos()
            self.size_or_type = self._io.read_u4le()
            self._debug['size_or_type']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            _on = self.info.kind
            if _on == Btf.Kind.array:
                pass
                self.data = Btf.BtfKindArray(self._io, self, self._root)
            elif _on == Btf.Kind.decl_tag:
                pass
                self.data = Btf.BtfKindDeclTag(self._io, self, self._root)
            elif _on == Btf.Kind.enum:
                pass
                self.data = Btf.BtfKindEnum(self.info.vlen, self._io, self, self._root)
            elif _on == Btf.Kind.enum64:
                pass
                self.data = Btf.BtfKindEnum64(self.info.vlen, self._io, self, self._root)
            elif _on == Btf.Kind.function_proto:
                pass
                self.data = Btf.BtfKindFunctionProto(self.info.vlen, self._io, self, self._root)
            elif _on == Btf.Kind.integer:
                pass
                self.data = Btf.BtfKindInt(self._io, self, self._root)
            elif _on == Btf.Kind.section:
                pass
                self.data = Btf.BtfKindSection(self.info.vlen, self._io, self, self._root)
            elif _on == Btf.Kind.union:
                pass
                self.data = Btf.BtfKindUnion(self.info.vlen, self._io, self, self._root)
            elif _on == Btf.Kind.variable:
                pass
                self.data = Btf.BtfKindVariable(self._io, self, self._root)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.info._fetch_instances()
            _on = self.info.kind
            if _on == Btf.Kind.array:
                pass
                self.data._fetch_instances()
            elif _on == Btf.Kind.decl_tag:
                pass
                self.data._fetch_instances()
            elif _on == Btf.Kind.enum:
                pass
                self.data._fetch_instances()
            elif _on == Btf.Kind.enum64:
                pass
                self.data._fetch_instances()
            elif _on == Btf.Kind.function_proto:
                pass
                self.data._fetch_instances()
            elif _on == Btf.Kind.integer:
                pass
                self.data._fetch_instances()
            elif _on == Btf.Kind.section:
                pass
                self.data._fetch_instances()
            elif _on == Btf.Kind.union:
                pass
                self.data._fetch_instances()
            elif _on == Btf.Kind.variable:
                pass
                self.data._fetch_instances()
            _ = self.name
            if hasattr(self, '_m_name'):
                pass


        @property
        def name(self):
            if hasattr(self, '_m_name'):
                return self._m_name

            io = self._root.string_section._io
            _pos = io.pos()
            io.seek(self.ofs_name)
            self._debug['_m_name']['start'] = io.pos()
            self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['_m_name']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_name', None)


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "flags", "len_header", "rest_of_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Btf.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x9F\xEB":
                raise kaitaistruct.ValidationNotEqualError(b"\x9F\xEB", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u1()
            self._debug['version']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['rest_of_header']['start'] = self._io.pos()
            self._raw_rest_of_header = self._io.read_bytes((((self.len_header - 2) - 1) - 1) - 4)
            _io__raw_rest_of_header = KaitaiStream(BytesIO(self._raw_rest_of_header))
            self.rest_of_header = Btf.Header.RestOfHeader(_io__raw_rest_of_header, self, self._root)
            self._debug['rest_of_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.rest_of_header._fetch_instances()

        class RestOfHeader(KaitaiStruct):
            SEQ_FIELDS = ["ofs_type_section", "len_type_section", "ofs_string_section", "len_string_section"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Btf.Header.RestOfHeader, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['ofs_type_section']['start'] = self._io.pos()
                self.ofs_type_section = self._io.read_u4le()
                self._debug['ofs_type_section']['end'] = self._io.pos()
                self._debug['len_type_section']['start'] = self._io.pos()
                self.len_type_section = self._io.read_u4le()
                self._debug['len_type_section']['end'] = self._io.pos()
                self._debug['ofs_string_section']['start'] = self._io.pos()
                self.ofs_string_section = self._io.read_u4le()
                self._debug['ofs_string_section']['end'] = self._io.pos()
                self._debug['len_string_section']['start'] = self._io.pos()
                self.len_string_section = self._io.read_u4le()
                self._debug['len_string_section']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass



    class Info(KaitaiStruct):
        SEQ_FIELDS = ["vlen", "unused1", "kind", "unused2", "kind_flag"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Btf.Info, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['vlen']['start'] = self._io.pos()
            self.vlen = self._io.read_bits_int_le(16)
            self._debug['vlen']['end'] = self._io.pos()
            self._debug['unused1']['start'] = self._io.pos()
            self.unused1 = self._io.read_bits_int_le(8)
            self._debug['unused1']['end'] = self._io.pos()
            self._debug['kind']['start'] = self._io.pos()
            self.kind = KaitaiStream.resolve_enum(Btf.Kind, self._io.read_bits_int_le(5))
            self._debug['kind']['end'] = self._io.pos()
            self._debug['unused2']['start'] = self._io.pos()
            self.unused2 = self._io.read_bits_int_le(2)
            self._debug['unused2']['end'] = self._io.pos()
            self._debug['kind_flag']['start'] = self._io.pos()
            self.kind_flag = self._io.read_bits_int_le(1) != 0
            self._debug['kind_flag']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class StringSection(KaitaiStruct):
        SEQ_FIELDS = ["strings"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Btf.StringSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['strings']['start'] = self._io.pos()
            self._debug['strings']['arr'] = []
            self.strings = []
            i = 0
            while not self._io.is_eof():
                self._debug['strings']['arr'].append({'start': self._io.pos()})
                self.strings.append((self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8"))
                self._debug['strings']['arr'][len(self.strings) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['strings']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.strings)):
                pass



    class TypeSection(KaitaiStruct):
        SEQ_FIELDS = ["btf_types"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Btf.TypeSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['btf_types']['start'] = self._io.pos()
            self._debug['btf_types']['arr'] = []
            self.btf_types = []
            i = 0
            while not self._io.is_eof():
                self._debug['btf_types']['arr'].append({'start': self._io.pos()})
                self.btf_types.append(Btf.BtfType(self._io, self, self._root))
                self._debug['btf_types']['arr'][len(self.btf_types) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['btf_types']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.btf_types)):
                pass
                self.btf_types[i]._fetch_instances()




