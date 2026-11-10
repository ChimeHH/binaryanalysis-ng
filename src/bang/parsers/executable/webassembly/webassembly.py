# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import vlq_base128_le
from .vlq_base128_le import *
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Webassembly(KaitaiStruct):
    """WebAssembly is a web standard that defines a binary format and a corresponding
    assembly-like text format for executable code in Web pages. It is meant to
    enable executing code nearly as fast as running native machine code.
    
    .. seealso::
       Source - https://github.com/WebAssembly/design/blob/master/BinaryEncoding.md
    """

    class ConstructorType(IntEnum):
        empty_block = 64
        func = 96
        anyfunc = 112
        f64 = 124
        f32 = 125
        i64 = 126
        i32 = 127

    class ElemType(IntEnum):
        anyfunc = 112

    class KindType(IntEnum):
        function_kind = 0
        table_kind = 1
        memory_kind = 2
        global_kind = 3

    class LinkingMetadataPayloadType(IntEnum):
        segment_info = 5
        init_funcs = 6
        comdat_info = 7
        symbol_table = 8

    class MutabilityFlag(IntEnum):
        immutable = 0
        mutable = 1

    class PayloadType(IntEnum):
        custom_payload = 0
        type_payload = 1
        import_payload = 2
        function_payload = 3
        table_payload = 4
        memory_payload = 5
        global_payload = 6
        export_payload = 7
        start_payload = 8
        element_payload = 9
        code_payload = 10
        data_payload = 11
        data_count_payload = 12

    class Symflag(IntEnum):
        binding_weak = 1
        binding_local = 2
        visibility_hidden = 4
        undefined = 16
        exported = 32
        explicit_name = 64
        no_strip = 128

    class Symtab(IntEnum):
        function = 0
        data = 1
        global_symbol = 2
        section = 3
        event = 4
        table = 5

    class ValueType(IntEnum):
        f64 = 124
        f32 = 125
        i64 = 126
        i32 = 127
    SEQ_FIELDS = ["magic", "version", "sections"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Webassembly, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x00\x61\x73\x6D":
            raise kaitaistruct.ValidationNotEqualError(b"\x00\x61\x73\x6D", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        self._debug['sections']['start'] = self._io.pos()
        self.sections = Webassembly.Sections(self._io, self, self._root)
        self._debug['sections']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.sections._fetch_instances()

    class CodeSection(KaitaiStruct):
        SEQ_FIELDS = ["count", "bodies"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.CodeSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()
            self._debug['bodies']['start'] = self._io.pos()
            self._debug['bodies']['arr'] = []
            self.bodies = []
            for i in range(self.count.value):
                self._debug['bodies']['arr'].append({'start': self._io.pos()})
                self.bodies.append(Webassembly.FunctionBodyType(self._io, self, self._root))
                self._debug['bodies']['arr'][i]['end'] = self._io.pos()

            self._debug['bodies']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.count._fetch_instances()
            for i in range(len(self.bodies)):
                pass
                self.bodies[i]._fetch_instances()



    class DataCountSection(KaitaiStruct):
        SEQ_FIELDS = ["count"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.DataCountSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.count._fetch_instances()


    class DataSection(KaitaiStruct):
        SEQ_FIELDS = ["count", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.DataSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.count.value):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Webassembly.DataSegmentType(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.count._fetch_instances()
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class DataSegmentType(KaitaiStruct):
        SEQ_FIELDS = ["type", "offset_expr_opcode", "offset_expr_arg", "terminator", "size", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.DataSegmentType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['type']['end'] = self._io.pos()
            self._debug['offset_expr_opcode']['start'] = self._io.pos()
            self.offset_expr_opcode = self._io.read_u1()
            self._debug['offset_expr_opcode']['end'] = self._io.pos()
            self._debug['offset_expr_arg']['start'] = self._io.pos()
            self.offset_expr_arg = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['offset_expr_arg']['end'] = self._io.pos()
            self._debug['terminator']['start'] = self._io.pos()
            self.terminator = self._io.read_bytes(1)
            self._debug['terminator']['end'] = self._io.pos()
            if not self.terminator == b"\x0B":
                raise kaitaistruct.ValidationNotEqualError(b"\x0B", self.terminator, self._io, u"/types/data_segment_type/seq/3")
            self._debug['size']['start'] = self._io.pos()
            self.size = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['size']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self._debug['data']['arr'] = []
            self.data = []
            for i in range(self.size.value):
                self._debug['data']['arr'].append({'start': self._io.pos()})
                self.data.append(self._io.read_u1())
                self._debug['data']['arr'][i]['end'] = self._io.pos()

            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.type._fetch_instances()
            self.offset_expr_arg._fetch_instances()
            self.size._fetch_instances()
            for i in range(len(self.data)):
                pass



    class ElemSegmentType(KaitaiStruct):
        SEQ_FIELDS = ["index", "offset", "num_elem", "elems"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.ElemSegmentType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['index']['start'] = self._io.pos()
            self.index = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['index']['end'] = self._io.pos()
            self._debug['offset']['start'] = self._io.pos()
            self._debug['offset']['arr'] = []
            self.offset = []
            i = 0
            while True:
                self._debug['offset']['arr'].append({'start': self._io.pos()})
                _ = self._io.read_u1()
                self.offset.append(_)
                self._debug['offset']['arr'][len(self.offset) - 1]['end'] = self._io.pos()
                if _ == 11:
                    break
                i += 1
            self._debug['offset']['end'] = self._io.pos()
            self._debug['num_elem']['start'] = self._io.pos()
            self.num_elem = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['num_elem']['end'] = self._io.pos()
            self._debug['elems']['start'] = self._io.pos()
            self._debug['elems']['arr'] = []
            self.elems = []
            for i in range(self.num_elem.value):
                self._debug['elems']['arr'].append({'start': self._io.pos()})
                self.elems.append(vlq_base128_le.VlqBase128Le(self._io))
                self._debug['elems']['arr'][i]['end'] = self._io.pos()

            self._debug['elems']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.index._fetch_instances()
            for i in range(len(self.offset)):
                pass

            self.num_elem._fetch_instances()
            for i in range(len(self.elems)):
                pass
                self.elems[i]._fetch_instances()



    class ElementSection(KaitaiStruct):
        SEQ_FIELDS = ["count", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.ElementSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.count.value):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Webassembly.ElemSegmentType(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.count._fetch_instances()
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class ExportEntryType(KaitaiStruct):
        SEQ_FIELDS = ["field_len", "field_str", "kind", "index"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.ExportEntryType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['field_len']['start'] = self._io.pos()
            self.field_len = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['field_len']['end'] = self._io.pos()
            self._debug['field_str']['start'] = self._io.pos()
            self.field_str = (self._io.read_bytes(self.field_len.value)).decode(u"UTF-8")
            self._debug['field_str']['end'] = self._io.pos()
            self._debug['kind']['start'] = self._io.pos()
            self.kind = KaitaiStream.resolve_enum(Webassembly.KindType, self._io.read_u1())
            self._debug['kind']['end'] = self._io.pos()
            self._debug['index']['start'] = self._io.pos()
            self.index = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['index']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.field_len._fetch_instances()
            self.index._fetch_instances()


    class ExportSection(KaitaiStruct):
        SEQ_FIELDS = ["count", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.ExportSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.count.value):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Webassembly.ExportEntryType(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.count._fetch_instances()
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class FuncType(KaitaiStruct):
        SEQ_FIELDS = ["form", "param_count", "param_types", "return_count", "return_type"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.FuncType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['form']['start'] = self._io.pos()
            self.form = KaitaiStream.resolve_enum(Webassembly.ConstructorType, self._io.read_u1())
            self._debug['form']['end'] = self._io.pos()
            self._debug['param_count']['start'] = self._io.pos()
            self.param_count = self._io.read_u1()
            self._debug['param_count']['end'] = self._io.pos()
            if self.param_count > 0:
                pass
                self._debug['param_types']['start'] = self._io.pos()
                self._debug['param_types']['arr'] = []
                self.param_types = []
                for i in range(self.param_count):
                    self._debug['param_types']['arr'].append({'start': self._io.pos()})
                    self.param_types.append(KaitaiStream.resolve_enum(Webassembly.ValueType, self._io.read_u1()))
                    self._debug['param_types']['arr'][i]['end'] = self._io.pos()

                self._debug['param_types']['end'] = self._io.pos()

            self._debug['return_count']['start'] = self._io.pos()
            self.return_count = self._io.read_u1()
            self._debug['return_count']['end'] = self._io.pos()
            if self.return_count == 1:
                pass
                self._debug['return_type']['start'] = self._io.pos()
                self.return_type = KaitaiStream.resolve_enum(Webassembly.ValueType, self._io.read_u1())
                self._debug['return_type']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.param_count > 0:
                pass
                for i in range(len(self.param_types)):
                    pass


            if self.return_count == 1:
                pass



    class FunctionBodyDataType(KaitaiStruct):
        SEQ_FIELDS = ["local_count", "locals", "code"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.FunctionBodyDataType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['local_count']['start'] = self._io.pos()
            self.local_count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['local_count']['end'] = self._io.pos()
            self._debug['locals']['start'] = self._io.pos()
            self._debug['locals']['arr'] = []
            self.locals = []
            for i in range(self.local_count.value):
                self._debug['locals']['arr'].append({'start': self._io.pos()})
                self.locals.append(Webassembly.LocalEntryType(self._io, self, self._root))
                self._debug['locals']['arr'][i]['end'] = self._io.pos()

            self._debug['locals']['end'] = self._io.pos()
            self._debug['code']['start'] = self._io.pos()
            self.code = self._io.read_bytes_full()
            self._debug['code']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.local_count._fetch_instances()
            for i in range(len(self.locals)):
                pass
                self.locals[i]._fetch_instances()



    class FunctionBodyType(KaitaiStruct):
        SEQ_FIELDS = ["body_size", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.FunctionBodyType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['body_size']['start'] = self._io.pos()
            self.body_size = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['body_size']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self._raw_data = self._io.read_bytes(self.body_size.value)
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = Webassembly.FunctionBodyDataType(_io__raw_data, self, self._root)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.body_size._fetch_instances()
            self.data._fetch_instances()


    class FunctionSection(KaitaiStruct):
        SEQ_FIELDS = ["count", "types"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.FunctionSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()
            self._debug['types']['start'] = self._io.pos()
            self._debug['types']['arr'] = []
            self.types = []
            for i in range(self.count.value):
                self._debug['types']['arr'].append({'start': self._io.pos()})
                self.types.append(vlq_base128_le.VlqBase128Le(self._io))
                self._debug['types']['arr'][i]['end'] = self._io.pos()

            self._debug['types']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.count._fetch_instances()
            for i in range(len(self.types)):
                pass
                self.types[i]._fetch_instances()



    class GlobalSection(KaitaiStruct):
        SEQ_FIELDS = ["count", "globals"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.GlobalSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()
            self._debug['globals']['start'] = self._io.pos()
            self._debug['globals']['arr'] = []
            self.globals = []
            for i in range(self.count.value):
                self._debug['globals']['arr'].append({'start': self._io.pos()})
                self.globals.append(Webassembly.GlobalVariableType(self._io, self, self._root))
                self._debug['globals']['arr'][i]['end'] = self._io.pos()

            self._debug['globals']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.count._fetch_instances()
            for i in range(len(self.globals)):
                pass
                self.globals[i]._fetch_instances()



    class GlobalType(KaitaiStruct):
        SEQ_FIELDS = ["content_type", "mutability"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.GlobalType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['content_type']['start'] = self._io.pos()
            self.content_type = KaitaiStream.resolve_enum(Webassembly.ValueType, self._io.read_u1())
            self._debug['content_type']['end'] = self._io.pos()
            self._debug['mutability']['start'] = self._io.pos()
            self.mutability = KaitaiStream.resolve_enum(Webassembly.MutabilityFlag, self._io.read_u1())
            self._debug['mutability']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class GlobalVariableType(KaitaiStruct):
        SEQ_FIELDS = ["type", "init"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.GlobalVariableType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = Webassembly.GlobalType(self._io, self, self._root)
            self._debug['type']['end'] = self._io.pos()
            self._debug['init']['start'] = self._io.pos()
            self._debug['init']['arr'] = []
            self.init = []
            i = 0
            while True:
                self._debug['init']['arr'].append({'start': self._io.pos()})
                _ = self._io.read_u1()
                self.init.append(_)
                self._debug['init']['arr'][len(self.init) - 1]['end'] = self._io.pos()
                if _ == 11:
                    break
                i += 1
            self._debug['init']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.type._fetch_instances()
            for i in range(len(self.init)):
                pass



    class ImportEntry(KaitaiStruct):
        SEQ_FIELDS = ["module_len", "module_str", "field_len", "field_str", "kind", "type"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.ImportEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['module_len']['start'] = self._io.pos()
            self.module_len = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['module_len']['end'] = self._io.pos()
            self._debug['module_str']['start'] = self._io.pos()
            self.module_str = (self._io.read_bytes(self.module_len.value)).decode(u"UTF-8")
            self._debug['module_str']['end'] = self._io.pos()
            self._debug['field_len']['start'] = self._io.pos()
            self.field_len = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['field_len']['end'] = self._io.pos()
            self._debug['field_str']['start'] = self._io.pos()
            self.field_str = (self._io.read_bytes(self.field_len.value)).decode(u"UTF-8")
            self._debug['field_str']['end'] = self._io.pos()
            self._debug['kind']['start'] = self._io.pos()
            self.kind = KaitaiStream.resolve_enum(Webassembly.KindType, self._io.read_u1())
            self._debug['kind']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            _on = self.kind
            if _on == Webassembly.KindType.function_kind:
                pass
                self.type = vlq_base128_le.VlqBase128Le(self._io)
            elif _on == Webassembly.KindType.global_kind:
                pass
                self.type = Webassembly.GlobalType(self._io, self, self._root)
            elif _on == Webassembly.KindType.memory_kind:
                pass
                self.type = Webassembly.MemoryType(self._io, self, self._root)
            elif _on == Webassembly.KindType.table_kind:
                pass
                self.type = Webassembly.TableType(self._io, self, self._root)
            self._debug['type']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.module_len._fetch_instances()
            self.field_len._fetch_instances()
            _on = self.kind
            if _on == Webassembly.KindType.function_kind:
                pass
                self.type._fetch_instances()
            elif _on == Webassembly.KindType.global_kind:
                pass
                self.type._fetch_instances()
            elif _on == Webassembly.KindType.memory_kind:
                pass
                self.type._fetch_instances()
            elif _on == Webassembly.KindType.table_kind:
                pass
                self.type._fetch_instances()


    class ImportSection(KaitaiStruct):
        SEQ_FIELDS = ["count", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.ImportSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()
            if self.count.value > 0:
                pass
                self._debug['entries']['start'] = self._io.pos()
                self._debug['entries']['arr'] = []
                self.entries = []
                for i in range(self.count.value):
                    self._debug['entries']['arr'].append({'start': self._io.pos()})
                    self.entries.append(Webassembly.ImportEntry(self._io, self, self._root))
                    self._debug['entries']['arr'][i]['end'] = self._io.pos()

                self._debug['entries']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.count._fetch_instances()
            if self.count.value > 0:
                pass
                for i in range(len(self.entries)):
                    pass
                    self.entries[i]._fetch_instances()




    class LinkingCustomSubsectionType(KaitaiStruct):
        SEQ_FIELDS = ["type", "payload_len", "symbol_table", "payload_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.LinkingCustomSubsectionType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = self._io.read_u1()
            self._debug['type']['end'] = self._io.pos()
            self._debug['payload_len']['start'] = self._io.pos()
            self.payload_len = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['payload_len']['end'] = self._io.pos()
            if self.type == int(Webassembly.LinkingMetadataPayloadType.symbol_table):
                pass
                self._debug['symbol_table']['start'] = self._io.pos()
                self._raw_symbol_table = self._io.read_bytes(self.payload_len.value)
                _io__raw_symbol_table = KaitaiStream(BytesIO(self._raw_symbol_table))
                self.symbol_table = Webassembly.SymbolTableType(_io__raw_symbol_table, self, self._root)
                self._debug['symbol_table']['end'] = self._io.pos()

            if self.type != int(Webassembly.LinkingMetadataPayloadType.symbol_table):
                pass
                self._debug['payload_data']['start'] = self._io.pos()
                self._debug['payload_data']['arr'] = []
                self.payload_data = []
                for i in range(self.payload_len.value):
                    self._debug['payload_data']['arr'].append({'start': self._io.pos()})
                    self.payload_data.append(self._io.read_u1())
                    self._debug['payload_data']['arr'][i]['end'] = self._io.pos()

                self._debug['payload_data']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.payload_len._fetch_instances()
            if self.type == int(Webassembly.LinkingMetadataPayloadType.symbol_table):
                pass
                self.symbol_table._fetch_instances()

            if self.type != int(Webassembly.LinkingMetadataPayloadType.symbol_table):
                pass
                for i in range(len(self.payload_data)):
                    pass




    class LinkingCustomType(KaitaiStruct):
        SEQ_FIELDS = ["version", "subsections"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.LinkingCustomType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['version']['end'] = self._io.pos()
            self._debug['subsections']['start'] = self._io.pos()
            self._debug['subsections']['arr'] = []
            self.subsections = []
            i = 0
            while not self._io.is_eof():
                self._debug['subsections']['arr'].append({'start': self._io.pos()})
                self.subsections.append(Webassembly.LinkingCustomSubsectionType(self._io, self, self._root))
                self._debug['subsections']['arr'][len(self.subsections) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['subsections']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.version._fetch_instances()
            for i in range(len(self.subsections)):
                pass
                self.subsections[i]._fetch_instances()



    class LocalEntryType(KaitaiStruct):
        SEQ_FIELDS = ["count", "type"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.LocalEntryType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Webassembly.ValueType, self._io.read_u1())
            self._debug['type']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.count._fetch_instances()


    class MemorySection(KaitaiStruct):
        SEQ_FIELDS = ["count", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.MemorySection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.count.value):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Webassembly.MemoryType(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.count._fetch_instances()
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class MemoryType(KaitaiStruct):
        SEQ_FIELDS = ["limits"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.MemoryType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['limits']['start'] = self._io.pos()
            self.limits = Webassembly.ResizableLimitsType(self._io, self, self._root)
            self._debug['limits']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.limits._fetch_instances()


    class ResizableLimitsType(KaitaiStruct):
        SEQ_FIELDS = ["flags", "initial", "maximum"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.ResizableLimitsType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['initial']['start'] = self._io.pos()
            self.initial = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['initial']['end'] = self._io.pos()
            if self.flags == 1:
                pass
                self._debug['maximum']['start'] = self._io.pos()
                self.maximum = vlq_base128_le.VlqBase128Le(self._io)
                self._debug['maximum']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.initial._fetch_instances()
            if self.flags == 1:
                pass
                self.maximum._fetch_instances()



    class Section(KaitaiStruct):
        SEQ_FIELDS = ["header", "payload_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.Section, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Webassembly.SectionHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['payload_data']['start'] = self._io.pos()
            _on = self.header.id
            if _on == Webassembly.PayloadType.code_payload:
                pass
                self.payload_data = Webassembly.CodeSection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.custom_payload:
                pass
                self.payload_data = Webassembly.UnimplementedSection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.data_count_payload:
                pass
                self.payload_data = Webassembly.DataCountSection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.data_payload:
                pass
                self.payload_data = Webassembly.DataSection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.element_payload:
                pass
                self.payload_data = Webassembly.ElementSection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.export_payload:
                pass
                self.payload_data = Webassembly.ExportSection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.function_payload:
                pass
                self.payload_data = Webassembly.FunctionSection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.global_payload:
                pass
                self.payload_data = Webassembly.GlobalSection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.import_payload:
                pass
                self.payload_data = Webassembly.ImportSection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.memory_payload:
                pass
                self.payload_data = Webassembly.MemorySection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.start_payload:
                pass
                self.payload_data = Webassembly.StartSection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.table_payload:
                pass
                self.payload_data = Webassembly.TableSection(self._io, self, self._root)
            elif _on == Webassembly.PayloadType.type_payload:
                pass
                self.payload_data = Webassembly.TypeSection(self._io, self, self._root)
            self._debug['payload_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            _on = self.header.id
            if _on == Webassembly.PayloadType.code_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.custom_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.data_count_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.data_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.element_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.export_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.function_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.global_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.import_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.memory_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.start_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.table_payload:
                pass
                self.payload_data._fetch_instances()
            elif _on == Webassembly.PayloadType.type_payload:
                pass
                self.payload_data._fetch_instances()


    class SectionHeader(KaitaiStruct):
        SEQ_FIELDS = ["id", "payload_len"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.SectionHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['id']['start'] = self._io.pos()
            self.id = KaitaiStream.resolve_enum(Webassembly.PayloadType, self._io.read_u1())
            self._debug['id']['end'] = self._io.pos()
            self._debug['payload_len']['start'] = self._io.pos()
            self.payload_len = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['payload_len']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.payload_len._fetch_instances()


    class Sections(KaitaiStruct):
        SEQ_FIELDS = ["sections"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.Sections, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['sections']['start'] = self._io.pos()
            self._debug['sections']['arr'] = []
            self.sections = []
            i = 0
            while not self._io.is_eof():
                self._debug['sections']['arr'].append({'start': self._io.pos()})
                self.sections.append(Webassembly.Section(self._io, self, self._root))
                self._debug['sections']['arr'][len(self.sections) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['sections']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.sections)):
                pass
                self.sections[i]._fetch_instances()



    class StartSection(KaitaiStruct):
        SEQ_FIELDS = ["index"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.StartSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['index']['start'] = self._io.pos()
            self.index = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['index']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.index._fetch_instances()


    class SymbolTableType(KaitaiStruct):
        SEQ_FIELDS = ["count", "infos"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.SymbolTableType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()
            self._debug['infos']['start'] = self._io.pos()
            self._debug['infos']['arr'] = []
            self.infos = []
            for i in range(self.count.value):
                self._debug['infos']['arr'].append({'start': self._io.pos()})
                self.infos.append(Webassembly.SyminfoType(self._io, self, self._root))
                self._debug['infos']['arr'][i]['end'] = self._io.pos()

            self._debug['infos']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.count._fetch_instances()
            for i in range(len(self.infos)):
                pass
                self.infos[i]._fetch_instances()



    class SyminfoData(KaitaiStruct):
        SEQ_FIELDS = ["name_len", "name_data", "index", "offset", "size"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.SyminfoData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name_len']['start'] = self._io.pos()
            self.name_len = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['name_len']['end'] = self._io.pos()
            self._debug['name_data']['start'] = self._io.pos()
            self.name_data = (self._io.read_bytes(self.name_len.value)).decode(u"UTF-8")
            self._debug['name_data']['end'] = self._io.pos()
            if self._parent.flags.value & int(Webassembly.Symflag.undefined) == 0:
                pass
                self._debug['index']['start'] = self._io.pos()
                self.index = vlq_base128_le.VlqBase128Le(self._io)
                self._debug['index']['end'] = self._io.pos()

            if self._parent.flags.value & int(Webassembly.Symflag.undefined) == 0:
                pass
                self._debug['offset']['start'] = self._io.pos()
                self.offset = vlq_base128_le.VlqBase128Le(self._io)
                self._debug['offset']['end'] = self._io.pos()

            if self._parent.flags.value & int(Webassembly.Symflag.undefined) == 0:
                pass
                self._debug['size']['start'] = self._io.pos()
                self.size = vlq_base128_le.VlqBase128Le(self._io)
                self._debug['size']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.name_len._fetch_instances()
            if self._parent.flags.value & int(Webassembly.Symflag.undefined) == 0:
                pass
                self.index._fetch_instances()

            if self._parent.flags.value & int(Webassembly.Symflag.undefined) == 0:
                pass
                self.offset._fetch_instances()

            if self._parent.flags.value & int(Webassembly.Symflag.undefined) == 0:
                pass
                self.size._fetch_instances()



    class SyminfoExt(KaitaiStruct):
        SEQ_FIELDS = ["index", "name_len", "name_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.SyminfoExt, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['index']['start'] = self._io.pos()
            self.index = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['index']['end'] = self._io.pos()
            if self._parent.flags.value & int(Webassembly.Symflag.undefined) == 0:
                pass
                self._debug['name_len']['start'] = self._io.pos()
                self.name_len = vlq_base128_le.VlqBase128Le(self._io)
                self._debug['name_len']['end'] = self._io.pos()

            if self._parent.flags.value & int(Webassembly.Symflag.undefined) == 0:
                pass
                self._debug['name_data']['start'] = self._io.pos()
                self.name_data = (self._io.read_bytes(self.name_len.value)).decode(u"UTF-8")
                self._debug['name_data']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.index._fetch_instances()
            if self._parent.flags.value & int(Webassembly.Symflag.undefined) == 0:
                pass
                self.name_len._fetch_instances()

            if self._parent.flags.value & int(Webassembly.Symflag.undefined) == 0:
                pass



    class SyminfoSection(KaitaiStruct):
        SEQ_FIELDS = ["section"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.SyminfoSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['section']['start'] = self._io.pos()
            self.section = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['section']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.section._fetch_instances()


    class SyminfoType(KaitaiStruct):
        SEQ_FIELDS = ["kind", "flags", "data", "ext", "section"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.SyminfoType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['kind']['start'] = self._io.pos()
            self.kind = KaitaiStream.resolve_enum(Webassembly.Symtab, self._io.read_u1())
            self._debug['kind']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['flags']['end'] = self._io.pos()
            if self.kind == Webassembly.Symtab.data:
                pass
                self._debug['data']['start'] = self._io.pos()
                self.data = Webassembly.SyminfoData(self._io, self, self._root)
                self._debug['data']['end'] = self._io.pos()

            if  ((self.kind == Webassembly.Symtab.function) or (self.kind == Webassembly.Symtab.global_symbol) or (self.kind == Webassembly.Symtab.event) or (self.kind == Webassembly.Symtab.table)) :
                pass
                self._debug['ext']['start'] = self._io.pos()
                self.ext = Webassembly.SyminfoExt(self._io, self, self._root)
                self._debug['ext']['end'] = self._io.pos()

            if self.kind == Webassembly.Symtab.section:
                pass
                self._debug['section']['start'] = self._io.pos()
                self.section = Webassembly.SyminfoSection(self._io, self, self._root)
                self._debug['section']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.flags._fetch_instances()
            if self.kind == Webassembly.Symtab.data:
                pass
                self.data._fetch_instances()

            if  ((self.kind == Webassembly.Symtab.function) or (self.kind == Webassembly.Symtab.global_symbol) or (self.kind == Webassembly.Symtab.event) or (self.kind == Webassembly.Symtab.table)) :
                pass
                self.ext._fetch_instances()

            if self.kind == Webassembly.Symtab.section:
                pass
                self.section._fetch_instances()



    class TableSection(KaitaiStruct):
        SEQ_FIELDS = ["count", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.TableSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['count']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.count.value):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Webassembly.TableType(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.count._fetch_instances()
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class TableType(KaitaiStruct):
        SEQ_FIELDS = ["element_type", "limits"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.TableType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['element_type']['start'] = self._io.pos()
            self.element_type = KaitaiStream.resolve_enum(Webassembly.ElemType, self._io.read_u1())
            self._debug['element_type']['end'] = self._io.pos()
            self._debug['limits']['start'] = self._io.pos()
            self.limits = Webassembly.ResizableLimitsType(self._io, self, self._root)
            self._debug['limits']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.limits._fetch_instances()


    class TypeSection(KaitaiStruct):
        SEQ_FIELDS = ["count", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.TypeSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['count']['start'] = self._io.pos()
            self.count = self._io.read_u1()
            self._debug['count']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.count):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Webassembly.FuncType(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class UnimplementedSection(KaitaiStruct):
        SEQ_FIELDS = ["name_len", "name", "linking", "raw"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Webassembly.UnimplementedSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name_len']['start'] = self._io.pos()
            self.name_len = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['name_len']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(self.name_len.value)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            if self.name == u"linking":
                pass
                self._debug['linking']['start'] = self._io.pos()
                self._debug['linking']['arr'] = []
                self.linking = []
                i = 0
                while not self._io.is_eof():
                    self._debug['linking']['arr'].append({'start': self._io.pos()})
                    self.linking.append(Webassembly.LinkingCustomType(self._io, self, self._root))
                    self._debug['linking']['arr'][len(self.linking) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['linking']['end'] = self._io.pos()

            if self.name != u"linking":
                pass
                self._debug['raw']['start'] = self._io.pos()
                self._debug['raw']['arr'] = []
                self.raw = []
                for i in range((self._parent.header.payload_len.value - self.name_len.value) - self.name_len.len):
                    self._debug['raw']['arr'].append({'start': self._io.pos()})
                    self.raw.append(self._io.read_u1())
                    self._debug['raw']['arr'][i]['end'] = self._io.pos()

                self._debug['raw']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.name_len._fetch_instances()
            if self.name == u"linking":
                pass
                for i in range(len(self.linking)):
                    pass
                    self.linking[i]._fetch_instances()


            if self.name != u"linking":
                pass
                for i in range(len(self.raw)):
                    pass





