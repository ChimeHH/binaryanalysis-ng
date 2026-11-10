# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Aapt(KaitaiStruct):
    """
    .. seealso::
       Source - https://android.googlesource.com/platform/frameworks/base/+/0ba2a37eafd802d240e602bfdc74fc4cfe0c07cd/tools/aapt2/formats.md
    """

    class EntryTypes(IntEnum):
        table = 0
        file = 1
    SEQ_FIELDS = ["magic", "version", "num_entries", "entries"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Aapt, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x41\x41\x50\x54":
            raise kaitaistruct.ValidationNotEqualError(b"\x41\x41\x50\x54", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        if not self.version == 1:
            raise kaitaistruct.ValidationNotEqualError(1, self.version, self._io, u"/seq/1")
        self._debug['num_entries']['start'] = self._io.pos()
        self.num_entries = self._io.read_u4le()
        self._debug['num_entries']['end'] = self._io.pos()
        self._debug['entries']['start'] = self._io.pos()
        self._debug['entries']['arr'] = []
        self.entries = []
        for i in range(self.num_entries):
            self._debug['entries']['arr'].append({'start': self._io.pos()})
            self.entries.append(Aapt.Entry(self._io, self, self._root))
            self._debug['entries']['arr'][i]['end'] = self._io.pos()

        self._debug['entries']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.entries)):
            pass
            self.entries[i]._fetch_instances()


    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["entry_type", "len_data", "data", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aapt.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entry_type']['start'] = self._io.pos()
            self.entry_type = KaitaiStream.resolve_enum(Aapt.EntryTypes, self._io.read_u4le())
            self._debug['entry_type']['end'] = self._io.pos()
            if not  ((self.entry_type == Aapt.EntryTypes.table) or (self.entry_type == Aapt.EntryTypes.file)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.entry_type, self._io, u"/types/entry/seq/0")
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u8le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            _on = self.entry_type
            if _on == Aapt.EntryTypes.file:
                pass
                self.data = Aapt.File(self._io, self, self._root)
            elif _on == Aapt.EntryTypes.table:
                pass
                self.data = Aapt.Table(self.len_data, self._io, self, self._root)
            self._debug['data']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self._io.pos()) % 4)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.entry_type
            if _on == Aapt.EntryTypes.file:
                pass
                self.data._fetch_instances()
            elif _on == Aapt.EntryTypes.table:
                pass
                self.data._fetch_instances()


    class File(KaitaiStruct):
        SEQ_FIELDS = ["len_header", "len_data", "header", "padding1", "data", "padding2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aapt.File, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u8le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['header']['start'] = self._io.pos()
            self.header = self._io.read_bytes(self.len_header)
            self._debug['header']['end'] = self._io.pos()
            self._debug['padding1']['start'] = self._io.pos()
            self.padding1 = self._io.read_bytes(-(self.len_header) % 4)
            self._debug['padding1']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()
            self._debug['padding2']['start'] = self._io.pos()
            self.padding2 = self._io.read_bytes(-(self.len_data) % 4)
            self._debug['padding2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Table(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, len_data, _io, _parent=None, _root=None):
            super(Aapt.Table, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.len_data = len_data
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



