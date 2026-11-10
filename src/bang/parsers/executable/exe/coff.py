# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Coff(KaitaiStruct):
    """
    .. seealso::
       Source - https://wiki.osdev.org/COFF
    """
    SEQ_FIELDS = ["header", "optional_header", "section_headers"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Coff, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Coff.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        if self.header.len_optional_header != 0:
            pass
            self._debug['optional_header']['start'] = self._io.pos()
            self.optional_header = Coff.OptionalHeader(self._io, self, self._root)
            self._debug['optional_header']['end'] = self._io.pos()

        self._debug['section_headers']['start'] = self._io.pos()
        self._debug['section_headers']['arr'] = []
        self.section_headers = []
        for i in range(self.header.num_sections):
            self._debug['section_headers']['arr'].append({'start': self._io.pos()})
            self.section_headers.append(Coff.SectionHeader(self._io, self, self._root))
            self._debug['section_headers']['arr'][i]['end'] = self._io.pos()

        self._debug['section_headers']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        if self.header.len_optional_header != 0:
            pass
            self.optional_header._fetch_instances()

        for i in range(len(self.section_headers)):
            pass
            self.section_headers[i]._fetch_instances()

        _ = self.symbol_table_and_string_table
        if hasattr(self, '_m_symbol_table_and_string_table'):
            pass
            self._m_symbol_table_and_string_table._fetch_instances()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "num_sections", "time_and_date", "ofs_symbol_table", "num_symbols", "len_optional_header", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            self._debug['num_sections']['start'] = self._io.pos()
            self.num_sections = self._io.read_u2le()
            self._debug['num_sections']['end'] = self._io.pos()
            self._debug['time_and_date']['start'] = self._io.pos()
            self.time_and_date = self._io.read_u4le()
            self._debug['time_and_date']['end'] = self._io.pos()
            self._debug['ofs_symbol_table']['start'] = self._io.pos()
            self.ofs_symbol_table = self._io.read_u4le()
            self._debug['ofs_symbol_table']['end'] = self._io.pos()
            self._debug['num_symbols']['start'] = self._io.pos()
            self.num_symbols = self._io.read_u4le()
            self._debug['num_symbols']['end'] = self._io.pos()
            self._debug['len_optional_header']['start'] = self._io.pos()
            self.len_optional_header = self._io.read_u2le()
            self._debug['len_optional_header']['end'] = self._io.pos()
            if not  ((self.len_optional_header == 0) or (self.len_optional_header == 28)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.len_optional_header, self._io, u"/types/header/seq/5")
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2le()
            self._debug['flags']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def has_relocation_information(self):
            if hasattr(self, '_m_has_relocation_information'):
                return self._m_has_relocation_information

            self._m_has_relocation_information = self.flags & 1 != 1
            return getattr(self, '_m_has_relocation_information', None)

        @property
        def is_32_bit(self):
            if hasattr(self, '_m_is_32_bit'):
                return self._m_is_32_bit

            self._m_is_32_bit = self.flags & 256 == 256
            return getattr(self, '_m_is_32_bit', None)

        @property
        def is_executable(self):
            if hasattr(self, '_m_is_executable'):
                return self._m_is_executable

            self._m_is_executable = self.flags & 2 == 2
            return getattr(self, '_m_is_executable', None)

        @property
        def line_numbers_removed(self):
            if hasattr(self, '_m_line_numbers_removed'):
                return self._m_line_numbers_removed

            self._m_line_numbers_removed = self.flags & 4 == 4
            return getattr(self, '_m_line_numbers_removed', None)

        @property
        def local_symbols_removed(self):
            if hasattr(self, '_m_local_symbols_removed'):
                return self._m_local_symbols_removed

            self._m_local_symbols_removed = self.flags & 8 == 8
            return getattr(self, '_m_local_symbols_removed', None)


    class LineNumberEntry(KaitaiStruct):
        SEQ_FIELDS = ["symbol_index_or_physical_address", "line_number"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.LineNumberEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['symbol_index_or_physical_address']['start'] = self._io.pos()
            self.symbol_index_or_physical_address = self._io.read_u4le()
            self._debug['symbol_index_or_physical_address']['end'] = self._io.pos()
            self._debug['line_number']['start'] = self._io.pos()
            self.line_number = self._io.read_u2le()
            self._debug['line_number']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class LineNumberTable(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, num_line_number_table_entries, _io, _parent=None, _root=None):
            super(Coff.LineNumberTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_line_number_table_entries = num_line_number_table_entries
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_line_number_table_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Coff.LineNumberEntry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class OptionalHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version_stamp", "len_text", "len_initialized_data", "len_uninitialized_data", "entry_point", "text_start", "data_start"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.OptionalHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_u2le()
            self._debug['magic']['end'] = self._io.pos()
            self._debug['version_stamp']['start'] = self._io.pos()
            self.version_stamp = self._io.read_u2le()
            self._debug['version_stamp']['end'] = self._io.pos()
            self._debug['len_text']['start'] = self._io.pos()
            self.len_text = self._io.read_u4le()
            self._debug['len_text']['end'] = self._io.pos()
            self._debug['len_initialized_data']['start'] = self._io.pos()
            self.len_initialized_data = self._io.read_u4le()
            self._debug['len_initialized_data']['end'] = self._io.pos()
            self._debug['len_uninitialized_data']['start'] = self._io.pos()
            self.len_uninitialized_data = self._io.read_u4le()
            self._debug['len_uninitialized_data']['end'] = self._io.pos()
            self._debug['entry_point']['start'] = self._io.pos()
            self.entry_point = self._io.read_u4le()
            self._debug['entry_point']['end'] = self._io.pos()
            self._debug['text_start']['start'] = self._io.pos()
            self.text_start = self._io.read_u4le()
            self._debug['text_start']['end'] = self._io.pos()
            self._debug['data_start']['start'] = self._io.pos()
            self.data_start = self._io.read_u4le()
            self._debug['data_start']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class RelocationEntry(KaitaiStruct):
        SEQ_FIELDS = ["reference_address", "symbol_index", "relocation_type"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.RelocationEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reference_address']['start'] = self._io.pos()
            self.reference_address = self._io.read_u4le()
            self._debug['reference_address']['end'] = self._io.pos()
            self._debug['symbol_index']['start'] = self._io.pos()
            self.symbol_index = self._io.read_u4le()
            self._debug['symbol_index']['end'] = self._io.pos()
            self._debug['relocation_type']['start'] = self._io.pos()
            self.relocation_type = self._io.read_u2le()
            self._debug['relocation_type']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class RelocationTable(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, num_relocation_entries, _io, _parent=None, _root=None):
            super(Coff.RelocationTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_relocation_entries = num_relocation_entries
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_relocation_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Coff.RelocationEntry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class SectionHeader(KaitaiStruct):
        SEQ_FIELDS = ["name", "physical_address", "virtual_address", "len_section", "ofs_section", "ofs_relocation_table", "ofs_line_number_table", "num_relocation_entries", "num_line_number_table_entries", "flags"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.SectionHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(8), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['physical_address']['start'] = self._io.pos()
            self.physical_address = self._io.read_u4le()
            self._debug['physical_address']['end'] = self._io.pos()
            self._debug['virtual_address']['start'] = self._io.pos()
            self.virtual_address = self._io.read_u4le()
            self._debug['virtual_address']['end'] = self._io.pos()
            self._debug['len_section']['start'] = self._io.pos()
            self.len_section = self._io.read_u4le()
            self._debug['len_section']['end'] = self._io.pos()
            self._debug['ofs_section']['start'] = self._io.pos()
            self.ofs_section = self._io.read_u4le()
            self._debug['ofs_section']['end'] = self._io.pos()
            self._debug['ofs_relocation_table']['start'] = self._io.pos()
            self.ofs_relocation_table = self._io.read_u4le()
            self._debug['ofs_relocation_table']['end'] = self._io.pos()
            self._debug['ofs_line_number_table']['start'] = self._io.pos()
            self.ofs_line_number_table = self._io.read_u4le()
            self._debug['ofs_line_number_table']['end'] = self._io.pos()
            self._debug['num_relocation_entries']['start'] = self._io.pos()
            self.num_relocation_entries = self._io.read_u2le()
            self._debug['num_relocation_entries']['end'] = self._io.pos()
            self._debug['num_line_number_table_entries']['start'] = self._io.pos()
            self.num_line_number_table_entries = self._io.read_u2le()
            self._debug['num_line_number_table_entries']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.line_number_table
            if hasattr(self, '_m_line_number_table'):
                pass
                self._m_line_number_table._fetch_instances()

            _ = self.relocation_table
            if hasattr(self, '_m_relocation_table'):
                pass
                self._m_relocation_table._fetch_instances()

            _ = self.section
            if hasattr(self, '_m_section'):
                pass


        @property
        def is_bss(self):
            if hasattr(self, '_m_is_bss'):
                return self._m_is_bss

            self._m_is_bss = self.flags & 128 == 128
            return getattr(self, '_m_is_bss', None)

        @property
        def is_data(self):
            if hasattr(self, '_m_is_data'):
                return self._m_is_data

            self._m_is_data = self.flags & 64 == 64
            return getattr(self, '_m_is_data', None)

        @property
        def is_text(self):
            if hasattr(self, '_m_is_text'):
                return self._m_is_text

            self._m_is_text = self.flags & 32 == 32
            return getattr(self, '_m_is_text', None)

        @property
        def line_number_table(self):
            if hasattr(self, '_m_line_number_table'):
                return self._m_line_number_table

            if  ((self.ofs_line_number_table != 0) and (self.num_line_number_table_entries != 0)) :
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_line_number_table)
                self._debug['_m_line_number_table']['start'] = io.pos()
                self._m_line_number_table = Coff.LineNumberTable(self.num_line_number_table_entries, io, self, self._root)
                self._debug['_m_line_number_table']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_line_number_table', None)

        @property
        def relocation_table(self):
            if hasattr(self, '_m_relocation_table'):
                return self._m_relocation_table

            if  ((self.ofs_relocation_table != 0) and (self.num_relocation_entries != 0)) :
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_relocation_table)
                self._debug['_m_relocation_table']['start'] = io.pos()
                self._m_relocation_table = Coff.RelocationTable(self.num_relocation_entries, io, self, self._root)
                self._debug['_m_relocation_table']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_relocation_table', None)

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


    class StringTable(KaitaiStruct):
        SEQ_FIELDS = ["strings"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.StringTable, self).__init__(_io)
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
                self.strings.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII"))
                self._debug['strings']['arr'][len(self.strings) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['strings']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.strings)):
                pass



    class Symbol(KaitaiStruct):
        SEQ_FIELDS = ["name", "value", "section_number", "symbol_type", "storage_class", "auxiliary_count"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Coff.Symbol, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = self._io.read_bytes(8)
            self._debug['name']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_u4le()
            self._debug['value']['end'] = self._io.pos()
            self._debug['section_number']['start'] = self._io.pos()
            self.section_number = self._io.read_u2le()
            self._debug['section_number']['end'] = self._io.pos()
            self._debug['symbol_type']['start'] = self._io.pos()
            self.symbol_type = self._io.read_u2le()
            self._debug['symbol_type']['end'] = self._io.pos()
            self._debug['storage_class']['start'] = self._io.pos()
            self.storage_class = self._io.read_u1()
            self._debug['storage_class']['end'] = self._io.pos()
            self._debug['auxiliary_count']['start'] = self._io.pos()
            self.auxiliary_count = self._io.read_u1()
            self._debug['auxiliary_count']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class SymbolTableAndStringTable(KaitaiStruct):
        SEQ_FIELDS = ["symbols", "len_string_table", "string_table"]
        def __init__(self, num_symbols, _io, _parent=None, _root=None):
            super(Coff.SymbolTableAndStringTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_symbols = num_symbols
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['symbols']['start'] = self._io.pos()
            self._debug['symbols']['arr'] = []
            self.symbols = []
            for i in range(self.num_symbols):
                self._debug['symbols']['arr'].append({'start': self._io.pos()})
                self.symbols.append(Coff.Symbol(self._io, self, self._root))
                self._debug['symbols']['arr'][i]['end'] = self._io.pos()

            self._debug['symbols']['end'] = self._io.pos()
            self._debug['len_string_table']['start'] = self._io.pos()
            self.len_string_table = self._io.read_u4le()
            self._debug['len_string_table']['end'] = self._io.pos()
            self._debug['string_table']['start'] = self._io.pos()
            self._raw_string_table = self._io.read_bytes(self.len_string_table - 4)
            _io__raw_string_table = KaitaiStream(BytesIO(self._raw_string_table))
            self.string_table = Coff.StringTable(_io__raw_string_table, self, self._root)
            self._debug['string_table']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.symbols)):
                pass
                self.symbols[i]._fetch_instances()

            self.string_table._fetch_instances()


    @property
    def symbol_table_and_string_table(self):
        if hasattr(self, '_m_symbol_table_and_string_table'):
            return self._m_symbol_table_and_string_table

        if self.header.ofs_symbol_table != 0:
            pass
            _pos = self._io.pos()
            self._io.seek(self.header.ofs_symbol_table)
            self._debug['_m_symbol_table_and_string_table']['start'] = self._io.pos()
            self._m_symbol_table_and_string_table = Coff.SymbolTableAndStringTable(self.header.num_symbols, self._io, self, self._root)
            self._debug['_m_symbol_table_and_string_table']['end'] = self._io.pos()
            self._io.seek(_pos)

        return getattr(self, '_m_symbol_table_and_string_table', None)


