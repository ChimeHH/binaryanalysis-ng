# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Pef(KaitaiStruct):
    """
    .. seealso::
       Source - https://en.wikipedia.org/wiki/Preferred_Executable_Format
    
    
    .. seealso::
       Source - https://web.archive.org/web/20020208214155/http://developer.apple.com/techpubs/mac/runtimehtml/RTArch-89.html
    """

    class Architectures(IntEnum):
        m68k = 1832269931
        powerpc = 1886875747

    class Section(IntEnum):
        code = 0
        unpacked_data = 1
        pattern_initialized_data = 2
        constant = 3
        loader = 4
        debug = 5
        executable_data = 6
        exception = 7
        traceback = 8

    class Share(IntEnum):
        process_share = 1
        global_share = 4
        protected_share = 5

    class SymbolClasses(IntEnum):
        code_address = 0
        data_address = 1
        standard_procedure_pointer = 2
        direct_data_area = 3
        linker_inserted_glue = 4
    SEQ_FIELDS = ["header", "section_headers"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Pef, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Pef.ContainerHeader(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['section_headers']['start'] = self._io.pos()
        self._debug['section_headers']['arr'] = []
        self.section_headers = []
        for i in range(self.header.num_sections):
            self._debug['section_headers']['arr'].append({'start': self._io.pos()})
            self.section_headers.append(Pef.SectionHeader(self._io, self, self._root))
            self._debug['section_headers']['arr'][i]['end'] = self._io.pos()

        self._debug['section_headers']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.section_headers)):
            pass
            self.section_headers[i]._fetch_instances()


    class ContainerHeader(KaitaiStruct):
        SEQ_FIELDS = ["type_tag1", "type_tag2", "architecture", "format_version", "date", "old_def_version", "old_imp_version", "current_version", "num_sections", "num_instantiated_sections", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pef.ContainerHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type_tag1']['start'] = self._io.pos()
            self.type_tag1 = self._io.read_bytes(4)
            self._debug['type_tag1']['end'] = self._io.pos()
            if not self.type_tag1 == b"\x4A\x6F\x79\x21":
                raise kaitaistruct.ValidationNotEqualError(b"\x4A\x6F\x79\x21", self.type_tag1, self._io, u"/types/container_header/seq/0")
            self._debug['type_tag2']['start'] = self._io.pos()
            self.type_tag2 = self._io.read_bytes(4)
            self._debug['type_tag2']['end'] = self._io.pos()
            if not self.type_tag2 == b"\x70\x65\x66\x66":
                raise kaitaistruct.ValidationNotEqualError(b"\x70\x65\x66\x66", self.type_tag2, self._io, u"/types/container_header/seq/1")
            self._debug['architecture']['start'] = self._io.pos()
            self.architecture = KaitaiStream.resolve_enum(Pef.Architectures, self._io.read_u4be())
            self._debug['architecture']['end'] = self._io.pos()
            self._debug['format_version']['start'] = self._io.pos()
            self.format_version = self._io.read_u4be()
            self._debug['format_version']['end'] = self._io.pos()
            self._debug['date']['start'] = self._io.pos()
            self.date = self._io.read_u4be()
            self._debug['date']['end'] = self._io.pos()
            self._debug['old_def_version']['start'] = self._io.pos()
            self.old_def_version = self._io.read_u4be()
            self._debug['old_def_version']['end'] = self._io.pos()
            self._debug['old_imp_version']['start'] = self._io.pos()
            self.old_imp_version = self._io.read_u4be()
            self._debug['old_imp_version']['end'] = self._io.pos()
            self._debug['current_version']['start'] = self._io.pos()
            self.current_version = self._io.read_u4be()
            self._debug['current_version']['end'] = self._io.pos()
            self._debug['num_sections']['start'] = self._io.pos()
            self.num_sections = self._io.read_u2be()
            self._debug['num_sections']['end'] = self._io.pos()
            self._debug['num_instantiated_sections']['start'] = self._io.pos()
            self.num_instantiated_sections = self._io.read_u2be()
            self._debug['num_instantiated_sections']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(4)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class ImportedLibrary(KaitaiStruct):
        SEQ_FIELDS = ["ofs_name", "old_imp_version", "current_version", "num_imported_symbols", "first_imported_symbol", "options", "reserved1", "reserved2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pef.ImportedLibrary, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_name']['start'] = self._io.pos()
            self.ofs_name = self._io.read_u4be()
            self._debug['ofs_name']['end'] = self._io.pos()
            self._debug['old_imp_version']['start'] = self._io.pos()
            self.old_imp_version = self._io.read_u4be()
            self._debug['old_imp_version']['end'] = self._io.pos()
            self._debug['current_version']['start'] = self._io.pos()
            self.current_version = self._io.read_u4be()
            self._debug['current_version']['end'] = self._io.pos()
            self._debug['num_imported_symbols']['start'] = self._io.pos()
            self.num_imported_symbols = self._io.read_u4be()
            self._debug['num_imported_symbols']['end'] = self._io.pos()
            self._debug['first_imported_symbol']['start'] = self._io.pos()
            self.first_imported_symbol = self._io.read_u4be()
            self._debug['first_imported_symbol']['end'] = self._io.pos()
            self._debug['options']['start'] = self._io.pos()
            self.options = self._io.read_u1()
            self._debug['options']['end'] = self._io.pos()
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bytes(1)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bytes(2)
            self._debug['reserved2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.name
            if hasattr(self, '_m_name'):
                pass


        @property
        def name(self):
            if hasattr(self, '_m_name'):
                return self._m_name

            io = self._parent._io
            _pos = io.pos()
            io.seek(self._parent.header.ofs_loader_strings + self.ofs_name)
            self._debug['_m_name']['start'] = io.pos()
            self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['_m_name']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_name', None)


    class ImportedSymbol(KaitaiStruct):
        SEQ_FIELDS = ["symbol_class_data", "ofs_name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pef.ImportedSymbol, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['symbol_class_data']['start'] = self._io.pos()
            self.symbol_class_data = self._io.read_u1()
            self._debug['symbol_class_data']['end'] = self._io.pos()
            self._debug['ofs_name']['start'] = self._io.pos()
            self.ofs_name = self._io.read_bits_int_be(24)
            self._debug['ofs_name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.name
            if hasattr(self, '_m_name'):
                pass


        @property
        def is_weak(self):
            if hasattr(self, '_m_is_weak'):
                return self._m_is_weak

            self._m_is_weak = self.symbol_class_data & 128 == 128
            return getattr(self, '_m_is_weak', None)

        @property
        def name(self):
            if hasattr(self, '_m_name'):
                return self._m_name

            io = self._parent._io
            _pos = io.pos()
            io.seek(self._parent.header.ofs_loader_strings + self.ofs_name)
            self._debug['_m_name']['start'] = io.pos()
            self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['_m_name']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_name', None)

        @property
        def symbol_class(self):
            if hasattr(self, '_m_symbol_class'):
                return self._m_symbol_class

            self._m_symbol_class = KaitaiStream.resolve_enum(Pef.SymbolClasses, self.symbol_class_data & 15)
            return getattr(self, '_m_symbol_class', None)


    class Loader(KaitaiStruct):
        SEQ_FIELDS = ["header", "imported_library_table", "imported_symbol_table", "relocation_headers_table", "export_hashtable", "export_keytable", "exported_symbol_table"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pef.Loader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Pef.LoaderHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['imported_library_table']['start'] = self._io.pos()
            self._debug['imported_library_table']['arr'] = []
            self.imported_library_table = []
            for i in range(self.header.num_imported_libraries):
                self._debug['imported_library_table']['arr'].append({'start': self._io.pos()})
                self.imported_library_table.append(Pef.ImportedLibrary(self._io, self, self._root))
                self._debug['imported_library_table']['arr'][i]['end'] = self._io.pos()

            self._debug['imported_library_table']['end'] = self._io.pos()
            self._debug['imported_symbol_table']['start'] = self._io.pos()
            self._debug['imported_symbol_table']['arr'] = []
            self.imported_symbol_table = []
            for i in range(self.header.num_total_imported_symbols):
                self._debug['imported_symbol_table']['arr'].append({'start': self._io.pos()})
                self.imported_symbol_table.append(Pef.ImportedSymbol(self._io, self, self._root))
                self._debug['imported_symbol_table']['arr'][i]['end'] = self._io.pos()

            self._debug['imported_symbol_table']['end'] = self._io.pos()
            self._debug['relocation_headers_table']['start'] = self._io.pos()
            self._debug['relocation_headers_table']['arr'] = []
            self.relocation_headers_table = []
            for i in range(self.header.num_reloc_sections):
                self._debug['relocation_headers_table']['arr'].append({'start': self._io.pos()})
                self.relocation_headers_table.append(Pef.RelocationHeaderEntry(self._io, self, self._root))
                self._debug['relocation_headers_table']['arr'][i]['end'] = self._io.pos()

            self._debug['relocation_headers_table']['end'] = self._io.pos()
            self._debug['export_hashtable']['start'] = self._io.pos()
            self.export_hashtable = self._io.read_bytes(0)
            self._debug['export_hashtable']['end'] = self._io.pos()
            self._debug['export_keytable']['start'] = self._io.pos()
            self.export_keytable = self._io.read_bytes(0)
            self._debug['export_keytable']['end'] = self._io.pos()
            self._debug['exported_symbol_table']['start'] = self._io.pos()
            self.exported_symbol_table = self._io.read_bytes(0)
            self._debug['exported_symbol_table']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            for i in range(len(self.imported_library_table)):
                pass
                self.imported_library_table[i]._fetch_instances()

            for i in range(len(self.imported_symbol_table)):
                pass
                self.imported_symbol_table[i]._fetch_instances()

            for i in range(len(self.relocation_headers_table)):
                pass
                self.relocation_headers_table[i]._fetch_instances()



    class LoaderHeader(KaitaiStruct):
        SEQ_FIELDS = ["main_section", "ofs_main", "init_section", "ofs_init", "term_section", "ofs_term", "num_imported_libraries", "num_total_imported_symbols", "num_reloc_sections", "ofs_reloc_instructions", "ofs_loader_strings", "ofs_export_hash", "export_hash_table_power", "num_exported_symbols"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pef.LoaderHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['main_section']['start'] = self._io.pos()
            self.main_section = self._io.read_s4be()
            self._debug['main_section']['end'] = self._io.pos()
            self._debug['ofs_main']['start'] = self._io.pos()
            self.ofs_main = self._io.read_u4be()
            self._debug['ofs_main']['end'] = self._io.pos()
            self._debug['init_section']['start'] = self._io.pos()
            self.init_section = self._io.read_s4be()
            self._debug['init_section']['end'] = self._io.pos()
            self._debug['ofs_init']['start'] = self._io.pos()
            self.ofs_init = self._io.read_u4be()
            self._debug['ofs_init']['end'] = self._io.pos()
            self._debug['term_section']['start'] = self._io.pos()
            self.term_section = self._io.read_s4be()
            self._debug['term_section']['end'] = self._io.pos()
            self._debug['ofs_term']['start'] = self._io.pos()
            self.ofs_term = self._io.read_u4be()
            self._debug['ofs_term']['end'] = self._io.pos()
            self._debug['num_imported_libraries']['start'] = self._io.pos()
            self.num_imported_libraries = self._io.read_u4be()
            self._debug['num_imported_libraries']['end'] = self._io.pos()
            self._debug['num_total_imported_symbols']['start'] = self._io.pos()
            self.num_total_imported_symbols = self._io.read_u4be()
            self._debug['num_total_imported_symbols']['end'] = self._io.pos()
            self._debug['num_reloc_sections']['start'] = self._io.pos()
            self.num_reloc_sections = self._io.read_u4be()
            self._debug['num_reloc_sections']['end'] = self._io.pos()
            self._debug['ofs_reloc_instructions']['start'] = self._io.pos()
            self.ofs_reloc_instructions = self._io.read_u4be()
            self._debug['ofs_reloc_instructions']['end'] = self._io.pos()
            self._debug['ofs_loader_strings']['start'] = self._io.pos()
            self.ofs_loader_strings = self._io.read_u4be()
            self._debug['ofs_loader_strings']['end'] = self._io.pos()
            self._debug['ofs_export_hash']['start'] = self._io.pos()
            self.ofs_export_hash = self._io.read_u4be()
            self._debug['ofs_export_hash']['end'] = self._io.pos()
            self._debug['export_hash_table_power']['start'] = self._io.pos()
            self.export_hash_table_power = self._io.read_u4be()
            self._debug['export_hash_table_power']['end'] = self._io.pos()
            self._debug['num_exported_symbols']['start'] = self._io.pos()
            self.num_exported_symbols = self._io.read_u4be()
            self._debug['num_exported_symbols']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.symbols
            if hasattr(self, '_m_symbols'):
                pass
                for i in range(len(self._m_symbols)):
                    pass



        @property
        def symbols(self):
            if hasattr(self, '_m_symbols'):
                return self._m_symbols

            _pos = self._io.pos()
            self._io.seek(self.ofs_loader_strings)
            self._debug['_m_symbols']['start'] = self._io.pos()
            self._debug['_m_symbols']['arr'] = []
            self._m_symbols = []
            i = 0
            while not self._io.is_eof():
                self._debug['_m_symbols']['arr'].append({'start': self._io.pos()})
                self._m_symbols.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII"))
                self._debug['_m_symbols']['arr'][len(self._m_symbols) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['_m_symbols']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_symbols', None)


    class RelocationHeaderEntry(KaitaiStruct):
        SEQ_FIELDS = ["section_index", "reserved", "num_reloc", "ofs_first_reloc"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pef.RelocationHeaderEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['section_index']['start'] = self._io.pos()
            self.section_index = self._io.read_u2be()
            self._debug['section_index']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(2)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['num_reloc']['start'] = self._io.pos()
            self.num_reloc = self._io.read_u4be()
            self._debug['num_reloc']['end'] = self._io.pos()
            self._debug['ofs_first_reloc']['start'] = self._io.pos()
            self.ofs_first_reloc = self._io.read_u4be()
            self._debug['ofs_first_reloc']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.relocations
            if hasattr(self, '_m_relocations'):
                pass
                for i in range(len(self._m_relocations)):
                    pass



        @property
        def relocations(self):
            if hasattr(self, '_m_relocations'):
                return self._m_relocations

            io = self._parent._io
            _pos = io.pos()
            io.seek(self._parent.header.ofs_reloc_instructions + self.ofs_first_reloc)
            self._debug['_m_relocations']['start'] = io.pos()
            self._debug['_m_relocations']['arr'] = []
            self._m_relocations = []
            for i in range(self.num_reloc):
                self._debug['_m_relocations']['arr'].append({'start': io.pos()})
                self._m_relocations.append(io.read_u2be())
                self._debug['_m_relocations']['arr'][i]['end'] = io.pos()

            self._debug['_m_relocations']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_relocations', None)


    class SectionHeader(KaitaiStruct):
        SEQ_FIELDS = ["ofs_name", "default_address", "len_total", "len_unpacked", "len_packed", "ofs_container", "section_kind", "share_kind", "alignment", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pef.SectionHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_name']['start'] = self._io.pos()
            self.ofs_name = self._io.read_s4be()
            self._debug['ofs_name']['end'] = self._io.pos()
            self._debug['default_address']['start'] = self._io.pos()
            self.default_address = self._io.read_u4be()
            self._debug['default_address']['end'] = self._io.pos()
            self._debug['len_total']['start'] = self._io.pos()
            self.len_total = self._io.read_u4be()
            self._debug['len_total']['end'] = self._io.pos()
            self._debug['len_unpacked']['start'] = self._io.pos()
            self.len_unpacked = self._io.read_u4be()
            self._debug['len_unpacked']['end'] = self._io.pos()
            self._debug['len_packed']['start'] = self._io.pos()
            self.len_packed = self._io.read_u4be()
            self._debug['len_packed']['end'] = self._io.pos()
            self._debug['ofs_container']['start'] = self._io.pos()
            self.ofs_container = self._io.read_u4be()
            self._debug['ofs_container']['end'] = self._io.pos()
            self._debug['section_kind']['start'] = self._io.pos()
            self.section_kind = KaitaiStream.resolve_enum(Pef.Section, self._io.read_u1())
            self._debug['section_kind']['end'] = self._io.pos()
            self._debug['share_kind']['start'] = self._io.pos()
            self.share_kind = KaitaiStream.resolve_enum(Pef.Share, self._io.read_u1())
            self._debug['share_kind']['end'] = self._io.pos()
            self._debug['alignment']['start'] = self._io.pos()
            self.alignment = self._io.read_u1()
            self._debug['alignment']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(1)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.section
            if hasattr(self, '_m_section'):
                pass
                _on = self.section_kind
                if _on == Pef.Section.loader:
                    pass
                    self._m_section._fetch_instances()
                else:
                    pass


        @property
        def section(self):
            if hasattr(self, '_m_section'):
                return self._m_section

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_container)
            self._debug['_m_section']['start'] = io.pos()
            _on = self.section_kind
            if _on == Pef.Section.loader:
                pass
                self._raw__m_section = io.read_bytes(self.len_packed)
                _io__raw__m_section = KaitaiStream(BytesIO(self._raw__m_section))
                self._m_section = Pef.Loader(_io__raw__m_section, self, self._root)
            else:
                pass
                self._m_section = io.read_bytes(self.len_packed)
            self._debug['_m_section']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_section', None)



