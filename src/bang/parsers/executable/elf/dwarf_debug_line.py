# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import vlq_base128_le
from .vlq_base128_le import *
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class DwarfDebugLine(KaitaiStruct):
    """
    .. seealso::
       <https://dwarfstd.org/doc/DWARF4.pdf>
    """
    SEQ_FIELDS = ["compilation_units"]
    def __init__(self, _io, _parent=None, _root=None):
        super(DwarfDebugLine, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['compilation_units']['start'] = self._io.pos()
        self._debug['compilation_units']['arr'] = []
        self.compilation_units = []
        i = 0
        while not self._io.is_eof():
            self._debug['compilation_units']['arr'].append({'start': self._io.pos()})
            self.compilation_units.append(DwarfDebugLine.CompilationUnit(self._io, self, self._root))
            self._debug['compilation_units']['arr'][len(self.compilation_units) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['compilation_units']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.compilation_units)):
            pass
            self.compilation_units[i]._fetch_instances()


    class CompilationUnit(KaitaiStruct):
        SEQ_FIELDS = ["header", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DwarfDebugLine.CompilationUnit, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = DwarfDebugLine.DebugLineHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self._raw_data = self._io.read_bytes((self.header.length - 28) + 4)
            _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
            self.data = DwarfDebugLine.Data(_io__raw_data, self, self._root)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.data._fetch_instances()


    class Data(KaitaiStruct):
        SEQ_FIELDS = ["include_directories"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DwarfDebugLine.Data, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['include_directories']['start'] = self._io.pos()
            self._debug['include_directories']['arr'] = []
            self.include_directories = []
            i = 0
            while True:
                self._debug['include_directories']['arr'].append({'start': self._io.pos()})
                _ = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self.include_directories.append(_)
                self._debug['include_directories']['arr'][len(self.include_directories) - 1]['end'] = self._io.pos()
                if _ == u"":
                    break
                i += 1
            self._debug['include_directories']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.include_directories)):
                pass



    class DebugLineHeader(KaitaiStruct):
        SEQ_FIELDS = ["length", "version", "len_header", "min_instruction_length", "max_operations_per_instruction", "default_is_stmt", "line_base", "line_range", "opcode_base", "opcode_lengths"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DwarfDebugLine.DebugLineHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['length']['start'] = self._io.pos()
            self.length = self._io.read_u4le()
            self._debug['length']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u2le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['min_instruction_length']['start'] = self._io.pos()
            self.min_instruction_length = self._io.read_u1()
            self._debug['min_instruction_length']['end'] = self._io.pos()
            self._debug['max_operations_per_instruction']['start'] = self._io.pos()
            self.max_operations_per_instruction = self._io.read_u1()
            self._debug['max_operations_per_instruction']['end'] = self._io.pos()
            self._debug['default_is_stmt']['start'] = self._io.pos()
            self.default_is_stmt = self._io.read_u1()
            self._debug['default_is_stmt']['end'] = self._io.pos()
            self._debug['line_base']['start'] = self._io.pos()
            self.line_base = self._io.read_s1()
            self._debug['line_base']['end'] = self._io.pos()
            self._debug['line_range']['start'] = self._io.pos()
            self.line_range = self._io.read_u1()
            self._debug['line_range']['end'] = self._io.pos()
            self._debug['opcode_base']['start'] = self._io.pos()
            self.opcode_base = self._io.read_u1()
            self._debug['opcode_base']['end'] = self._io.pos()
            self._debug['opcode_lengths']['start'] = self._io.pos()
            self._debug['opcode_lengths']['arr'] = []
            self.opcode_lengths = []
            for i in range(12):
                self._debug['opcode_lengths']['arr'].append({'start': self._io.pos()})
                self.opcode_lengths.append(self._io.read_u1())
                self._debug['opcode_lengths']['arr'][i]['end'] = self._io.pos()

            self._debug['opcode_lengths']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.opcode_lengths)):
                pass



    class FileNameEntry(KaitaiStruct):
        SEQ_FIELDS = ["name", "dir_index", "time_of_last_modification", "len_bytes"]
        def __init__(self, _io, _parent=None, _root=None):
            super(DwarfDebugLine.FileNameEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['dir_index']['start'] = self._io.pos()
            self.dir_index = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['dir_index']['end'] = self._io.pos()
            self._debug['time_of_last_modification']['start'] = self._io.pos()
            self.time_of_last_modification = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['time_of_last_modification']['end'] = self._io.pos()
            self._debug['len_bytes']['start'] = self._io.pos()
            self.len_bytes = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['len_bytes']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.dir_index._fetch_instances()
            self.time_of_last_modification._fetch_instances()
            self.len_bytes._fetch_instances()

        @property
        def directory_index(self):
            if hasattr(self, '_m_directory_index'):
                return self._m_directory_index

            self._m_directory_index = self.dir_index.value
            return getattr(self, '_m_directory_index', None)

        @property
        def last_modification_time(self):
            if hasattr(self, '_m_last_modification_time'):
                return self._m_last_modification_time

            self._m_last_modification_time = self.time_of_last_modification.value
            return getattr(self, '_m_last_modification_time', None)

        @property
        def len_bytes_in_file(self):
            if hasattr(self, '_m_len_bytes_in_file'):
                return self._m_len_bytes_in_file

            self._m_len_bytes_in_file = self.len_bytes.value
            return getattr(self, '_m_len_bytes_in_file', None)



