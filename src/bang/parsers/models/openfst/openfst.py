# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Openfst(KaitaiStruct):
    """OpenFst parser for a subset of OpenFst files, inspired by:
    https://github.com/steveash/jopenfst/pull/11/files
    """
    SEQ_FIELDS = ["magic", "len_fst_type", "fst_type", "len_arc_type", "arc_type", "version", "flags", "properties", "start", "num_states", "num_arcs", "input_symbol_table", "output_symbol_table", "states"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Openfst, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\xD6\xFD\xB2\x7E":
            raise kaitaistruct.ValidationNotEqualError(b"\xD6\xFD\xB2\x7E", self.magic, self._io, u"/seq/0")
        self._debug['len_fst_type']['start'] = self._io.pos()
        self.len_fst_type = self._io.read_u4le()
        self._debug['len_fst_type']['end'] = self._io.pos()
        self._debug['fst_type']['start'] = self._io.pos()
        self.fst_type = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_fst_type), 0, False)).decode(u"UTF-8")
        self._debug['fst_type']['end'] = self._io.pos()
        if not self.fst_type == u"vector":
            raise kaitaistruct.ValidationNotEqualError(u"vector", self.fst_type, self._io, u"/seq/2")
        self._debug['len_arc_type']['start'] = self._io.pos()
        self.len_arc_type = self._io.read_u4le()
        self._debug['len_arc_type']['end'] = self._io.pos()
        self._debug['arc_type']['start'] = self._io.pos()
        self.arc_type = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_arc_type), 0, False)).decode(u"UTF-8")
        self._debug['arc_type']['end'] = self._io.pos()
        if not self.arc_type == u"standard":
            raise kaitaistruct.ValidationNotEqualError(u"standard", self.arc_type, self._io, u"/seq/4")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        if not self.version == 2:
            raise kaitaistruct.ValidationNotEqualError(2, self.version, self._io, u"/seq/5")
        self._debug['flags']['start'] = self._io.pos()
        self.flags = self._io.read_u4le()
        self._debug['flags']['end'] = self._io.pos()
        self._debug['properties']['start'] = self._io.pos()
        self.properties = self._io.read_u8le()
        self._debug['properties']['end'] = self._io.pos()
        self._debug['start']['start'] = self._io.pos()
        self.start = self._io.read_u8le()
        self._debug['start']['end'] = self._io.pos()
        self._debug['num_states']['start'] = self._io.pos()
        self.num_states = self._io.read_s8le()
        self._debug['num_states']['end'] = self._io.pos()
        if not self.num_states >= 0:
            raise kaitaistruct.ValidationLessThanError(0, self.num_states, self._io, u"/seq/9")
        self._debug['num_arcs']['start'] = self._io.pos()
        self.num_arcs = self._io.read_u8le()
        self._debug['num_arcs']['end'] = self._io.pos()
        if self.has_input_symbol_table:
            pass
            self._debug['input_symbol_table']['start'] = self._io.pos()
            self.input_symbol_table = Openfst.SymbolTable(self._io, self, self._root)
            self._debug['input_symbol_table']['end'] = self._io.pos()

        if self.has_output_symbol_table:
            pass
            self._debug['output_symbol_table']['start'] = self._io.pos()
            self.output_symbol_table = Openfst.SymbolTable(self._io, self, self._root)
            self._debug['output_symbol_table']['end'] = self._io.pos()

        self._debug['states']['start'] = self._io.pos()
        self._debug['states']['arr'] = []
        self.states = []
        for i in range(self.num_states):
            self._debug['states']['arr'].append({'start': self._io.pos()})
            self.states.append(Openfst.State(self._io, self, self._root))
            self._debug['states']['arr'][i]['end'] = self._io.pos()

        self._debug['states']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        if self.has_input_symbol_table:
            pass
            self.input_symbol_table._fetch_instances()

        if self.has_output_symbol_table:
            pass
            self.output_symbol_table._fetch_instances()

        for i in range(len(self.states)):
            pass
            self.states[i]._fetch_instances()


    class Arc(KaitaiStruct):
        SEQ_FIELDS = ["input_label_idx", "output_label_idx", "weight", "next_state_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Openfst.Arc, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['input_label_idx']['start'] = self._io.pos()
            self.input_label_idx = self._io.read_u4le()
            self._debug['input_label_idx']['end'] = self._io.pos()
            self._debug['output_label_idx']['start'] = self._io.pos()
            self.output_label_idx = self._io.read_u4le()
            self._debug['output_label_idx']['end'] = self._io.pos()
            self._debug['weight']['start'] = self._io.pos()
            self.weight = self._io.read_u4le()
            self._debug['weight']['end'] = self._io.pos()
            self._debug['next_state_idx']['start'] = self._io.pos()
            self.next_state_idx = self._io.read_u4le()
            self._debug['next_state_idx']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class State(KaitaiStruct):
        SEQ_FIELDS = ["weight", "num_arcs", "arcs"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Openfst.State, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['weight']['start'] = self._io.pos()
            self.weight = self._io.read_u4le()
            self._debug['weight']['end'] = self._io.pos()
            self._debug['num_arcs']['start'] = self._io.pos()
            self.num_arcs = self._io.read_u8le()
            self._debug['num_arcs']['end'] = self._io.pos()
            self._debug['arcs']['start'] = self._io.pos()
            self._debug['arcs']['arr'] = []
            self.arcs = []
            for i in range(self.num_arcs):
                self._debug['arcs']['arr'].append({'start': self._io.pos()})
                self.arcs.append(Openfst.Arc(self._io, self, self._root))
                self._debug['arcs']['arr'][i]['end'] = self._io.pos()

            self._debug['arcs']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.arcs)):
                pass
                self.arcs[i]._fetch_instances()



    class Symbol(KaitaiStruct):
        SEQ_FIELDS = ["len_name", "name", "key"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Openfst.Symbol, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_u4le()
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_name), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['key']['start'] = self._io.pos()
            self.key = self._io.read_u8le()
            self._debug['key']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class SymbolTable(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_name", "name", "available_key", "num_symbols", "symbols"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Openfst.SymbolTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x74\xFB\xB2\x7E":
                raise kaitaistruct.ValidationNotEqualError(b"\x74\xFB\xB2\x7E", self.magic, self._io, u"/types/symbol_table/seq/0")
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_u4le()
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_name), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['available_key']['start'] = self._io.pos()
            self.available_key = self._io.read_u8le()
            self._debug['available_key']['end'] = self._io.pos()
            self._debug['num_symbols']['start'] = self._io.pos()
            self.num_symbols = self._io.read_u8le()
            self._debug['num_symbols']['end'] = self._io.pos()
            self._debug['symbols']['start'] = self._io.pos()
            self._debug['symbols']['arr'] = []
            self.symbols = []
            for i in range(self.num_symbols):
                self._debug['symbols']['arr'].append({'start': self._io.pos()})
                self.symbols.append(Openfst.Symbol(self._io, self, self._root))
                self._debug['symbols']['arr'][i]['end'] = self._io.pos()

            self._debug['symbols']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.symbols)):
                pass
                self.symbols[i]._fetch_instances()



    @property
    def has_input_symbol_table(self):
        if hasattr(self, '_m_has_input_symbol_table'):
            return self._m_has_input_symbol_table

        self._m_has_input_symbol_table = self.flags & 1 == 1
        return getattr(self, '_m_has_input_symbol_table', None)

    @property
    def has_output_symbol_table(self):
        if hasattr(self, '_m_has_output_symbol_table'):
            return self._m_has_output_symbol_table

        self._m_has_output_symbol_table = self.flags & 2 == 2
        return getattr(self, '_m_has_output_symbol_table', None)

    @property
    def is_aligned(self):
        if hasattr(self, '_m_is_aligned'):
            return self._m_is_aligned

        self._m_is_aligned = self.flags & 4 == 4
        return getattr(self, '_m_is_aligned', None)


