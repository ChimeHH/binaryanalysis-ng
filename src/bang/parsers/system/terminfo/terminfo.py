# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Terminfo(KaitaiStruct):
    """terminfo files, format described in the Linux man page for terminfo files
    man 5 term
    """
    SEQ_FIELDS = ["magic", "len_names_section", "len_boolean_section", "num_numbers_section", "num_strings_offsets", "len_string_table", "names_section", "boolean_section", "boolean_padding", "numbers_section", "strings_section", "string_table"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Terminfo, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(2)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x1A\x01":
            raise kaitaistruct.ValidationNotEqualError(b"\x1A\x01", self.magic, self._io, u"/seq/0")
        self._debug['len_names_section']['start'] = self._io.pos()
        self.len_names_section = self._io.read_u2le()
        self._debug['len_names_section']['end'] = self._io.pos()
        if not self.len_names_section >= 1:
            raise kaitaistruct.ValidationLessThanError(1, self.len_names_section, self._io, u"/seq/1")
        self._debug['len_boolean_section']['start'] = self._io.pos()
        self.len_boolean_section = self._io.read_u2le()
        self._debug['len_boolean_section']['end'] = self._io.pos()
        self._debug['num_numbers_section']['start'] = self._io.pos()
        self.num_numbers_section = self._io.read_u2le()
        self._debug['num_numbers_section']['end'] = self._io.pos()
        self._debug['num_strings_offsets']['start'] = self._io.pos()
        self.num_strings_offsets = self._io.read_u2le()
        self._debug['num_strings_offsets']['end'] = self._io.pos()
        self._debug['len_string_table']['start'] = self._io.pos()
        self.len_string_table = self._io.read_u2le()
        self._debug['len_string_table']['end'] = self._io.pos()
        self._debug['names_section']['start'] = self._io.pos()
        self._raw_names_section = self._io.read_bytes(self.len_names_section)
        _io__raw_names_section = KaitaiStream(BytesIO(self._raw_names_section))
        self.names_section = Terminfo.NamesSection(_io__raw_names_section, self, self._root)
        self._debug['names_section']['end'] = self._io.pos()
        self._debug['boolean_section']['start'] = self._io.pos()
        self._raw_boolean_section = self._io.read_bytes(self.len_boolean_section)
        _io__raw_boolean_section = KaitaiStream(BytesIO(self._raw_boolean_section))
        self.boolean_section = Terminfo.BooleanSection(_io__raw_boolean_section, self, self._root)
        self._debug['boolean_section']['end'] = self._io.pos()
        if (self.len_names_section + self.len_boolean_section) % 2 == 1:
            pass
            self._debug['boolean_padding']['start'] = self._io.pos()
            self.boolean_padding = self._io.read_bytes(1)
            self._debug['boolean_padding']['end'] = self._io.pos()

        self._debug['numbers_section']['start'] = self._io.pos()
        self._raw_numbers_section = self._io.read_bytes(self.num_numbers_section * 2)
        _io__raw_numbers_section = KaitaiStream(BytesIO(self._raw_numbers_section))
        self.numbers_section = Terminfo.NumbersSection(_io__raw_numbers_section, self, self._root)
        self._debug['numbers_section']['end'] = self._io.pos()
        self._debug['strings_section']['start'] = self._io.pos()
        self._raw_strings_section = self._io.read_bytes(self.num_strings_offsets * 2)
        _io__raw_strings_section = KaitaiStream(BytesIO(self._raw_strings_section))
        self.strings_section = Terminfo.StringsSection(_io__raw_strings_section, self, self._root)
        self._debug['strings_section']['end'] = self._io.pos()
        self._debug['string_table']['start'] = self._io.pos()
        self._raw_string_table = self._io.read_bytes(self.len_string_table)
        _io__raw_string_table = KaitaiStream(BytesIO(self._raw_string_table))
        self.string_table = Terminfo.StringTable(_io__raw_string_table, self, self._root)
        self._debug['string_table']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.names_section._fetch_instances()
        self.boolean_section._fetch_instances()
        if (self.len_names_section + self.len_boolean_section) % 2 == 1:
            pass

        self.numbers_section._fetch_instances()
        self.strings_section._fetch_instances()
        self.string_table._fetch_instances()

    class BooleanSection(KaitaiStruct):
        SEQ_FIELDS = ["flags"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Terminfo.BooleanSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self._debug['flags']['arr'] = []
            self.flags = []
            i = 0
            while not self._io.is_eof():
                self._debug['flags']['arr'].append({'start': self._io.pos()})
                self.flags.append(Terminfo.Flag(self._io, self, self._root))
                self._debug['flags']['arr'][len(self.flags) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['flags']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.flags)):
                pass
                self.flags[i]._fetch_instances()



    class Flag(KaitaiStruct):
        SEQ_FIELDS = ["flag"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Terminfo.Flag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flag']['start'] = self._io.pos()
            self.flag = self._io.read_u1()
            self._debug['flag']['end'] = self._io.pos()
            if not  ((self.flag == 0) or (self.flag == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.flag, self._io, u"/types/flag/seq/0")


        def _fetch_instances(self):
            pass


    class NamesSection(KaitaiStruct):
        SEQ_FIELDS = ["names"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Terminfo.NamesSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['names']['start'] = self._io.pos()
            self.names = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['names']['end'] = self._io.pos()
            _ = self.names
            if not len(self.names) > 0:
                raise kaitaistruct.ValidationExprError(self.names, self._io, u"/types/names_section/seq/0")


        def _fetch_instances(self):
            pass


    class NumbersSection(KaitaiStruct):
        SEQ_FIELDS = ["number"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Terminfo.NumbersSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['number']['start'] = self._io.pos()
            self._debug['number']['arr'] = []
            self.number = []
            i = 0
            while not self._io.is_eof():
                self._debug['number']['arr'].append({'start': self._io.pos()})
                self.number.append(self._io.read_u2le())
                self._debug['number']['arr'][len(self.number) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['number']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.number)):
                pass



    class StringTable(KaitaiStruct):
        SEQ_FIELDS = ["strings"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Terminfo.StringTable, self).__init__(_io)
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
                self.strings.append(self._io.read_bytes_term(0, False, True, True))
                self._debug['strings']['arr'][len(self.strings) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['strings']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.strings)):
                pass



    class StringsSection(KaitaiStruct):
        SEQ_FIELDS = ["string_offset"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Terminfo.StringsSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['string_offset']['start'] = self._io.pos()
            self._debug['string_offset']['arr'] = []
            self.string_offset = []
            i = 0
            while not self._io.is_eof():
                self._debug['string_offset']['arr'].append({'start': self._io.pos()})
                self.string_offset.append(self._io.read_u2le())
                self._debug['string_offset']['arr'][len(self.string_offset) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['string_offset']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.string_offset)):
                pass




