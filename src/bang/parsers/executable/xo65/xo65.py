# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Xo65(KaitaiStruct):
    """xo65 is an object format used by the cc65 compiler <https://cc65.github.io/>
    Test files can be found in the binary packages of the cc65 package, for example in Debian <https://packages.debian.org/sid/cc65>.
    
    .. seealso::
       Source - https://github.com/cc65/cc65/blob/4185caf85/src/common/objdefs.h
    """
    SEQ_FIELDS = ["object_header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Xo65, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['object_header']['start'] = self._io.pos()
        self.object_header = Xo65.ObjectHeader(self._io, self, self._root)
        self._debug['object_header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.object_header._fetch_instances()

    class ObjectHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "flags", "ofs_options", "len_options", "ofs_file_table", "len_file_table", "ofs_segment_table", "len_segment_table", "ofs_import_list", "len_import_list", "ofs_export_list", "len_export_list", "ofs_debug_symbols_list", "len_debug_symbols_list", "ofs_line_infos", "len_line_infos", "ofs_string_pool", "len_string_pool", "ofs_assertion_table", "len_assertion_table", "ofs_scope_table", "len_scope_table", "ofs_span_table", "len_span_table"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Xo65.ObjectHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x55\x7A\x6E\x61":
                raise kaitaistruct.ValidationNotEqualError(b"\x55\x7A\x6E\x61", self.magic, self._io, u"/types/object_header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u2le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['ofs_options']['start'] = self._io.pos()
            self.ofs_options = self._io.read_u4le()
            self._debug['ofs_options']['end'] = self._io.pos()
            self._debug['len_options']['start'] = self._io.pos()
            self.len_options = self._io.read_u4le()
            self._debug['len_options']['end'] = self._io.pos()
            self._debug['ofs_file_table']['start'] = self._io.pos()
            self.ofs_file_table = self._io.read_u4le()
            self._debug['ofs_file_table']['end'] = self._io.pos()
            self._debug['len_file_table']['start'] = self._io.pos()
            self.len_file_table = self._io.read_u4le()
            self._debug['len_file_table']['end'] = self._io.pos()
            self._debug['ofs_segment_table']['start'] = self._io.pos()
            self.ofs_segment_table = self._io.read_u4le()
            self._debug['ofs_segment_table']['end'] = self._io.pos()
            self._debug['len_segment_table']['start'] = self._io.pos()
            self.len_segment_table = self._io.read_u4le()
            self._debug['len_segment_table']['end'] = self._io.pos()
            self._debug['ofs_import_list']['start'] = self._io.pos()
            self.ofs_import_list = self._io.read_u4le()
            self._debug['ofs_import_list']['end'] = self._io.pos()
            self._debug['len_import_list']['start'] = self._io.pos()
            self.len_import_list = self._io.read_u4le()
            self._debug['len_import_list']['end'] = self._io.pos()
            self._debug['ofs_export_list']['start'] = self._io.pos()
            self.ofs_export_list = self._io.read_u4le()
            self._debug['ofs_export_list']['end'] = self._io.pos()
            self._debug['len_export_list']['start'] = self._io.pos()
            self.len_export_list = self._io.read_u4le()
            self._debug['len_export_list']['end'] = self._io.pos()
            self._debug['ofs_debug_symbols_list']['start'] = self._io.pos()
            self.ofs_debug_symbols_list = self._io.read_u4le()
            self._debug['ofs_debug_symbols_list']['end'] = self._io.pos()
            self._debug['len_debug_symbols_list']['start'] = self._io.pos()
            self.len_debug_symbols_list = self._io.read_u4le()
            self._debug['len_debug_symbols_list']['end'] = self._io.pos()
            self._debug['ofs_line_infos']['start'] = self._io.pos()
            self.ofs_line_infos = self._io.read_u4le()
            self._debug['ofs_line_infos']['end'] = self._io.pos()
            self._debug['len_line_infos']['start'] = self._io.pos()
            self.len_line_infos = self._io.read_u4le()
            self._debug['len_line_infos']['end'] = self._io.pos()
            self._debug['ofs_string_pool']['start'] = self._io.pos()
            self.ofs_string_pool = self._io.read_u4le()
            self._debug['ofs_string_pool']['end'] = self._io.pos()
            self._debug['len_string_pool']['start'] = self._io.pos()
            self.len_string_pool = self._io.read_u4le()
            self._debug['len_string_pool']['end'] = self._io.pos()
            self._debug['ofs_assertion_table']['start'] = self._io.pos()
            self.ofs_assertion_table = self._io.read_u4le()
            self._debug['ofs_assertion_table']['end'] = self._io.pos()
            self._debug['len_assertion_table']['start'] = self._io.pos()
            self.len_assertion_table = self._io.read_u4le()
            self._debug['len_assertion_table']['end'] = self._io.pos()
            self._debug['ofs_scope_table']['start'] = self._io.pos()
            self.ofs_scope_table = self._io.read_u4le()
            self._debug['ofs_scope_table']['end'] = self._io.pos()
            self._debug['len_scope_table']['start'] = self._io.pos()
            self.len_scope_table = self._io.read_u4le()
            self._debug['len_scope_table']['end'] = self._io.pos()
            self._debug['ofs_span_table']['start'] = self._io.pos()
            self.ofs_span_table = self._io.read_u4le()
            self._debug['ofs_span_table']['end'] = self._io.pos()
            self._debug['len_span_table']['start'] = self._io.pos()
            self.len_span_table = self._io.read_u4le()
            self._debug['len_span_table']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.assertion_table
            if hasattr(self, '_m_assertion_table'):
                pass

            _ = self.debug_symbols_list
            if hasattr(self, '_m_debug_symbols_list'):
                pass

            _ = self.export_list
            if hasattr(self, '_m_export_list'):
                pass

            _ = self.file_table
            if hasattr(self, '_m_file_table'):
                pass

            _ = self.import_list
            if hasattr(self, '_m_import_list'):
                pass

            _ = self.line_infos
            if hasattr(self, '_m_line_infos'):
                pass

            _ = self.options
            if hasattr(self, '_m_options'):
                pass

            _ = self.scope_table
            if hasattr(self, '_m_scope_table'):
                pass

            _ = self.segment_table
            if hasattr(self, '_m_segment_table'):
                pass

            _ = self.span_table
            if hasattr(self, '_m_span_table'):
                pass

            _ = self.string_pool
            if hasattr(self, '_m_string_pool'):
                pass
                self._m_string_pool._fetch_instances()


        @property
        def assertion_table(self):
            if hasattr(self, '_m_assertion_table'):
                return self._m_assertion_table

            _pos = self._io.pos()
            self._io.seek(self.ofs_assertion_table)
            self._debug['_m_assertion_table']['start'] = self._io.pos()
            self._m_assertion_table = self._io.read_bytes(self.len_assertion_table)
            self._debug['_m_assertion_table']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_assertion_table', None)

        @property
        def debug_symbols_list(self):
            if hasattr(self, '_m_debug_symbols_list'):
                return self._m_debug_symbols_list

            _pos = self._io.pos()
            self._io.seek(self.ofs_debug_symbols_list)
            self._debug['_m_debug_symbols_list']['start'] = self._io.pos()
            self._m_debug_symbols_list = self._io.read_bytes(self.len_debug_symbols_list)
            self._debug['_m_debug_symbols_list']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_debug_symbols_list', None)

        @property
        def export_list(self):
            if hasattr(self, '_m_export_list'):
                return self._m_export_list

            _pos = self._io.pos()
            self._io.seek(self.ofs_export_list)
            self._debug['_m_export_list']['start'] = self._io.pos()
            self._m_export_list = self._io.read_bytes(self.len_export_list)
            self._debug['_m_export_list']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_export_list', None)

        @property
        def file_table(self):
            if hasattr(self, '_m_file_table'):
                return self._m_file_table

            _pos = self._io.pos()
            self._io.seek(self.ofs_file_table)
            self._debug['_m_file_table']['start'] = self._io.pos()
            self._m_file_table = self._io.read_bytes(self.len_file_table)
            self._debug['_m_file_table']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_file_table', None)

        @property
        def import_list(self):
            if hasattr(self, '_m_import_list'):
                return self._m_import_list

            _pos = self._io.pos()
            self._io.seek(self.ofs_import_list)
            self._debug['_m_import_list']['start'] = self._io.pos()
            self._m_import_list = self._io.read_bytes(self.len_import_list)
            self._debug['_m_import_list']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_import_list', None)

        @property
        def line_infos(self):
            if hasattr(self, '_m_line_infos'):
                return self._m_line_infos

            _pos = self._io.pos()
            self._io.seek(self.ofs_line_infos)
            self._debug['_m_line_infos']['start'] = self._io.pos()
            self._m_line_infos = self._io.read_bytes(self.len_line_infos)
            self._debug['_m_line_infos']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_line_infos', None)

        @property
        def options(self):
            if hasattr(self, '_m_options'):
                return self._m_options

            _pos = self._io.pos()
            self._io.seek(self.ofs_options)
            self._debug['_m_options']['start'] = self._io.pos()
            self._m_options = self._io.read_bytes(self.len_options)
            self._debug['_m_options']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_options', None)

        @property
        def scope_table(self):
            if hasattr(self, '_m_scope_table'):
                return self._m_scope_table

            _pos = self._io.pos()
            self._io.seek(self.ofs_scope_table)
            self._debug['_m_scope_table']['start'] = self._io.pos()
            self._m_scope_table = self._io.read_bytes(self.len_scope_table)
            self._debug['_m_scope_table']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_scope_table', None)

        @property
        def segment_table(self):
            if hasattr(self, '_m_segment_table'):
                return self._m_segment_table

            _pos = self._io.pos()
            self._io.seek(self.ofs_segment_table)
            self._debug['_m_segment_table']['start'] = self._io.pos()
            self._m_segment_table = self._io.read_bytes(self.len_segment_table)
            self._debug['_m_segment_table']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_segment_table', None)

        @property
        def span_table(self):
            if hasattr(self, '_m_span_table'):
                return self._m_span_table

            _pos = self._io.pos()
            self._io.seek(self.ofs_span_table)
            self._debug['_m_span_table']['start'] = self._io.pos()
            self._m_span_table = self._io.read_bytes(self.len_span_table)
            self._debug['_m_span_table']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_span_table', None)

        @property
        def string_pool(self):
            if hasattr(self, '_m_string_pool'):
                return self._m_string_pool

            _pos = self._io.pos()
            self._io.seek(self.ofs_string_pool)
            self._debug['_m_string_pool']['start'] = self._io.pos()
            self._raw__m_string_pool = self._io.read_bytes(self.len_string_pool)
            _io__raw__m_string_pool = KaitaiStream(BytesIO(self._raw__m_string_pool))
            self._m_string_pool = Xo65.StringPool(_io__raw__m_string_pool, self, self._root)
            self._debug['_m_string_pool']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_string_pool', None)


    class StringPool(KaitaiStruct):
        SEQ_FIELDS = ["num_strings", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Xo65.StringPool, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_strings']['start'] = self._io.pos()
            self.num_strings = self._io.read_u2le()
            self._debug['num_strings']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_strings - 1):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Xo65.StringPoolEntry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class StringPoolEntry(KaitaiStruct):
        SEQ_FIELDS = ["len_string", "string"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Xo65.StringPoolEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_string']['start'] = self._io.pos()
            self.len_string = self._io.read_u1()
            self._debug['len_string']['end'] = self._io.pos()
            self._debug['string']['start'] = self._io.pos()
            self.string = (self._io.read_bytes(self.len_string)).decode(u"ASCII")
            self._debug['string']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



