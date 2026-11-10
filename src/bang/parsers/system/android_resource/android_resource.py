# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class AndroidResource(KaitaiStruct):
    """
    .. seealso::
       Source - https://android.googlesource.com/platform/frameworks/base.git/+/2fedba9a32d9e92344eaf6e9faf5b43e1bc2ae70/libs/androidfw/include/androidfw/ResourceTypes.h#202
    """

    class ResourceTypes(IntEnum):
        null_type = 0
        string_pool = 1
        table = 2
        xml = 3
        xml_start_namespace = 256
        xml_end_namespace = 257
        xml_start_element = 258
        xml_end_element = 259
        xml_cdata = 260
        xml_last_chunk = 383
        xml_resource_map = 384
        table_package = 512
        table_type = 513
        table_type_spec = 514
        table_library = 515
        table_overlayable = 516
        table_overlayable_policy = 517
        table_staged_alias = 518
    SEQ_FIELDS = ["resource"]
    def __init__(self, _io, _parent=None, _root=None):
        super(AndroidResource, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['resource']['start'] = self._io.pos()
        self.resource = AndroidResource.Chunk(self._io, self, self._root)
        self._debug['resource']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.resource._fetch_instances()

    class Chunk(KaitaiStruct):
        SEQ_FIELDS = ["header", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.Chunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = AndroidResource.Header(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.header.type
            if _on == AndroidResource.ResourceTypes.string_pool:
                pass
                self._raw_body = self._io.read_bytes(self.header.len_chunk - 8)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = AndroidResource.StringPool(_io__raw_body, self, self._root)
            elif _on == AndroidResource.ResourceTypes.table:
                pass
                self._raw_body = self._io.read_bytes(self.header.len_chunk - 8)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = AndroidResource.Table(_io__raw_body, self, self._root)
            elif _on == AndroidResource.ResourceTypes.table_package:
                pass
                self._raw_body = self._io.read_bytes(self.header.len_chunk - 8)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = AndroidResource.TablePackage(_io__raw_body, self, self._root)
            elif _on == AndroidResource.ResourceTypes.xml:
                pass
                self._raw_body = self._io.read_bytes(self.header.len_chunk - 8)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = AndroidResource.Xml(_io__raw_body, self, self._root)
            else:
                pass
                self.body = self._io.read_bytes(self.header.len_chunk - 8)
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            _on = self.header.type
            if _on == AndroidResource.ResourceTypes.string_pool:
                pass
                self.body._fetch_instances()
            elif _on == AndroidResource.ResourceTypes.table:
                pass
                self.body._fetch_instances()
            elif _on == AndroidResource.ResourceTypes.table_package:
                pass
                self.body._fetch_instances()
            elif _on == AndroidResource.ResourceTypes.xml:
                pass
                self.body._fetch_instances()
            else:
                pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["type", "len_header", "len_chunk"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(AndroidResource.ResourceTypes, self._io.read_u2le())
            self._debug['type']['end'] = self._io.pos()
            if not  ((self.type == AndroidResource.ResourceTypes.null_type) or (self.type == AndroidResource.ResourceTypes.string_pool) or (self.type == AndroidResource.ResourceTypes.table) or (self.type == AndroidResource.ResourceTypes.xml) or (self.type == AndroidResource.ResourceTypes.xml_start_namespace) or (self.type == AndroidResource.ResourceTypes.xml_end_namespace) or (self.type == AndroidResource.ResourceTypes.xml_start_element) or (self.type == AndroidResource.ResourceTypes.xml_end_element) or (self.type == AndroidResource.ResourceTypes.xml_cdata) or (self.type == AndroidResource.ResourceTypes.xml_last_chunk) or (self.type == AndroidResource.ResourceTypes.xml_resource_map) or (self.type == AndroidResource.ResourceTypes.table_package) or (self.type == AndroidResource.ResourceTypes.table_type) or (self.type == AndroidResource.ResourceTypes.table_type_spec) or (self.type == AndroidResource.ResourceTypes.table_library) or (self.type == AndroidResource.ResourceTypes.table_overlayable) or (self.type == AndroidResource.ResourceTypes.table_overlayable_policy) or (self.type == AndroidResource.ResourceTypes.table_staged_alias)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.type, self._io, u"/types/header/seq/0")
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u2le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['len_chunk']['start'] = self._io.pos()
            self.len_chunk = self._io.read_u4le()
            self._debug['len_chunk']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PoolString(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, i, ofs_strings, is_utf8, _io, _parent=None, _root=None):
            super(AndroidResource.PoolString, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.i = i
            self.ofs_strings = ofs_strings
            self.is_utf8 = is_utf8
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.string
            if hasattr(self, '_m_string'):
                pass


        @property
        def string(self):
            if hasattr(self, '_m_string'):
                return self._m_string

            if self.is_utf8:
                pass
                io = self._parent._io
                _pos = io.pos()
                io.seek(self.ofs_strings + self._parent.string_offsets[self.i])
                self._debug['_m_string']['start'] = io.pos()
                self._m_string = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self._debug['_m_string']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_string', None)


    class PoolStyle(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, i, ofs_styles, _io, _parent=None, _root=None):
            super(AndroidResource.PoolStyle, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.i = i
            self.ofs_styles = ofs_styles
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.style
            if hasattr(self, '_m_style'):
                pass
                self._m_style._fetch_instances()


        @property
        def style(self):
            if hasattr(self, '_m_style'):
                return self._m_style

            io = self._parent._io
            _pos = io.pos()
            io.seek(self.ofs_styles + self._parent.style_offsets[self.i])
            self._debug['_m_style']['start'] = io.pos()
            self._m_style = AndroidResource.StringPoolSpanArray(io, self, self._root)
            self._debug['_m_style']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_style', None)


    class StringPool(KaitaiStruct):
        SEQ_FIELDS = ["header", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.StringPool, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self._raw_header = self._io.read_bytes(self._parent.header.len_header - 8)
            _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
            self.header = AndroidResource.StringPoolHeader(_io__raw_header, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self._raw_body = self._io.read_bytes_full()
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = AndroidResource.StringPoolBody(_io__raw_body, self, self._root)
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.body._fetch_instances()

        @property
        def len_header(self):
            if hasattr(self, '_m_len_header'):
                return self._m_len_header

            self._m_len_header = self._parent.header.len_header
            return getattr(self, '_m_len_header', None)

        @property
        def strings(self):
            if hasattr(self, '_m_strings'):
                return self._m_strings

            self._m_strings = self.body.strings
            return getattr(self, '_m_strings', None)


    class StringPoolBody(KaitaiStruct):
        SEQ_FIELDS = ["string_offsets", "style_offsets"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.StringPoolBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['string_offsets']['start'] = self._io.pos()
            self._debug['string_offsets']['arr'] = []
            self.string_offsets = []
            for i in range(self._parent.header.num_strings):
                self._debug['string_offsets']['arr'].append({'start': self._io.pos()})
                self.string_offsets.append(self._io.read_u4le())
                self._debug['string_offsets']['arr'][i]['end'] = self._io.pos()

            self._debug['string_offsets']['end'] = self._io.pos()
            self._debug['style_offsets']['start'] = self._io.pos()
            self._debug['style_offsets']['arr'] = []
            self.style_offsets = []
            for i in range(self._parent.header.num_styles):
                self._debug['style_offsets']['arr'].append({'start': self._io.pos()})
                self.style_offsets.append(self._io.read_u4le())
                self._debug['style_offsets']['arr'][i]['end'] = self._io.pos()

            self._debug['style_offsets']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.string_offsets)):
                pass

            for i in range(len(self.style_offsets)):
                pass

            _ = self.strings
            if hasattr(self, '_m_strings'):
                pass
                for i in range(len(self._m_strings)):
                    pass
                    self._m_strings[i]._fetch_instances()


            _ = self.styles
            if hasattr(self, '_m_styles'):
                pass
                for i in range(len(self._m_styles)):
                    pass
                    self._m_styles[i]._fetch_instances()



        @property
        def ofs_strings(self):
            if hasattr(self, '_m_ofs_strings'):
                return self._m_ofs_strings

            self._m_ofs_strings = self._parent.header.ofs_strings - self._parent.len_header
            return getattr(self, '_m_ofs_strings', None)

        @property
        def ofs_styles(self):
            if hasattr(self, '_m_ofs_styles'):
                return self._m_ofs_styles

            self._m_ofs_styles = self._parent.header.ofs_styles - self._parent.len_header
            return getattr(self, '_m_ofs_styles', None)

        @property
        def strings(self):
            if hasattr(self, '_m_strings'):
                return self._m_strings

            self._debug['_m_strings']['start'] = self._io.pos()
            self._debug['_m_strings']['arr'] = []
            self._m_strings = []
            for i in range(self._parent.header.num_strings):
                self._debug['_m_strings']['arr'].append({'start': self._io.pos()})
                self._m_strings.append(AndroidResource.PoolString(i, self.ofs_strings, self._parent.header.is_utf8, self._io, self, self._root))
                self._debug['_m_strings']['arr'][i]['end'] = self._io.pos()

            self._debug['_m_strings']['end'] = self._io.pos()
            return getattr(self, '_m_strings', None)

        @property
        def styles(self):
            if hasattr(self, '_m_styles'):
                return self._m_styles

            self._debug['_m_styles']['start'] = self._io.pos()
            self._debug['_m_styles']['arr'] = []
            self._m_styles = []
            for i in range(self._parent.header.num_styles):
                self._debug['_m_styles']['arr'].append({'start': self._io.pos()})
                self._m_styles.append(AndroidResource.PoolStyle(i, self.ofs_styles, self._io, self, self._root))
                self._debug['_m_styles']['arr'][i]['end'] = self._io.pos()

            self._debug['_m_styles']['end'] = self._io.pos()
            return getattr(self, '_m_styles', None)


    class StringPoolHeader(KaitaiStruct):
        SEQ_FIELDS = ["num_strings", "num_styles", "flags", "ofs_strings", "ofs_styles"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.StringPoolHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_strings']['start'] = self._io.pos()
            self.num_strings = self._io.read_u4le()
            self._debug['num_strings']['end'] = self._io.pos()
            if not self.num_strings <= self._root._io.size() // 4:
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size() // 4, self.num_strings, self._io, u"/types/string_pool_header/seq/0")
            self._debug['num_styles']['start'] = self._io.pos()
            self.num_styles = self._io.read_u4le()
            self._debug['num_styles']['end'] = self._io.pos()
            if not self.num_styles <= self._root._io.size() // 4:
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size() // 4, self.num_styles, self._io, u"/types/string_pool_header/seq/1")
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['ofs_strings']['start'] = self._io.pos()
            self.ofs_strings = self._io.read_u4le()
            self._debug['ofs_strings']['end'] = self._io.pos()
            if not self.ofs_strings <= self._root._io.size():
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size(), self.ofs_strings, self._io, u"/types/string_pool_header/seq/3")
            self._debug['ofs_styles']['start'] = self._io.pos()
            self.ofs_styles = self._io.read_u4le()
            self._debug['ofs_styles']['end'] = self._io.pos()
            if not self.ofs_styles <= self._root._io.size():
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size(), self.ofs_styles, self._io, u"/types/string_pool_header/seq/4")


        def _fetch_instances(self):
            pass

        @property
        def is_sorted(self):
            if hasattr(self, '_m_is_sorted'):
                return self._m_is_sorted

            self._m_is_sorted = self.flags & 1 == 1
            return getattr(self, '_m_is_sorted', None)

        @property
        def is_utf8(self):
            if hasattr(self, '_m_is_utf8'):
                return self._m_is_utf8

            self._m_is_utf8 = self.flags & 256 == 256
            return getattr(self, '_m_is_utf8', None)


    class StringPoolSpan(KaitaiStruct):
        SEQ_FIELDS = ["reference", "first_char", "last_char"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.StringPoolSpan, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reference']['start'] = self._io.pos()
            self.reference = self._io.read_u4le()
            self._debug['reference']['end'] = self._io.pos()
            if self.reference != 4294967295:
                pass
                self._debug['first_char']['start'] = self._io.pos()
                self.first_char = self._io.read_u4le()
                self._debug['first_char']['end'] = self._io.pos()

            if self.reference != 4294967295:
                pass
                self._debug['last_char']['start'] = self._io.pos()
                self.last_char = self._io.read_u4le()
                self._debug['last_char']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.reference != 4294967295:
                pass

            if self.reference != 4294967295:
                pass



    class StringPoolSpanArray(KaitaiStruct):
        SEQ_FIELDS = ["string_pool_span"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.StringPoolSpanArray, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['string_pool_span']['start'] = self._io.pos()
            self._debug['string_pool_span']['arr'] = []
            self.string_pool_span = []
            i = 0
            while True:
                self._debug['string_pool_span']['arr'].append({'start': self._io.pos()})
                _ = AndroidResource.StringPoolSpan(self._io, self, self._root)
                self.string_pool_span.append(_)
                self._debug['string_pool_span']['arr'][len(self.string_pool_span) - 1]['end'] = self._io.pos()
                if _.reference == 4294967295:
                    break
                i += 1
            self._debug['string_pool_span']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.string_pool_span)):
                pass
                self.string_pool_span[i]._fetch_instances()



    class Table(KaitaiStruct):
        SEQ_FIELDS = ["header", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.Table, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self._raw_header = self._io.read_bytes(self._parent.header.len_header - 8)
            _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
            self.header = AndroidResource.TableHeader(_io__raw_header, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self._raw_body = self._io.read_bytes_full()
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = AndroidResource.TableBody(_io__raw_body, self, self._root)
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.body._fetch_instances()

        @property
        def len_header(self):
            if hasattr(self, '_m_len_header'):
                return self._m_len_header

            self._m_len_header = self._parent.header.len_header
            return getattr(self, '_m_len_header', None)


    class TableBody(KaitaiStruct):
        SEQ_FIELDS = ["string_pool", "res_tables"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.TableBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['string_pool']['start'] = self._io.pos()
            self.string_pool = AndroidResource.Chunk(self._io, self, self._root)
            self._debug['string_pool']['end'] = self._io.pos()
            self._debug['res_tables']['start'] = self._io.pos()
            self._debug['res_tables']['arr'] = []
            self.res_tables = []
            for i in range(self._parent.header.num_table_package):
                self._debug['res_tables']['arr'].append({'start': self._io.pos()})
                self.res_tables.append(AndroidResource.Chunk(self._io, self, self._root))
                self._debug['res_tables']['arr'][i]['end'] = self._io.pos()

            self._debug['res_tables']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.string_pool._fetch_instances()
            for i in range(len(self.res_tables)):
                pass
                self.res_tables[i]._fetch_instances()



    class TableHeader(KaitaiStruct):
        SEQ_FIELDS = ["num_table_package"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.TableHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_table_package']['start'] = self._io.pos()
            self.num_table_package = self._io.read_u4le()
            self._debug['num_table_package']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class TablePackage(KaitaiStruct):
        SEQ_FIELDS = ["header", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.TablePackage, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = AndroidResource.TablePackageHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self.body = self._io.read_bytes_full()
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()

        @property
        def len_header(self):
            if hasattr(self, '_m_len_header'):
                return self._m_len_header

            self._m_len_header = self._parent.header.len_header
            return getattr(self, '_m_len_header', None)


    class TablePackageHeader(KaitaiStruct):
        SEQ_FIELDS = ["package_id", "name", "type_strings", "last_public_type", "key_strings", "last_public_key", "type_id_offset"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.TablePackageHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['package_id']['start'] = self._io.pos()
            self.package_id = self._io.read_u4le()
            self._debug['package_id']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = self._io.read_bytes(256)
            self._debug['name']['end'] = self._io.pos()
            self._debug['type_strings']['start'] = self._io.pos()
            self.type_strings = self._io.read_u4le()
            self._debug['type_strings']['end'] = self._io.pos()
            self._debug['last_public_type']['start'] = self._io.pos()
            self.last_public_type = self._io.read_u4le()
            self._debug['last_public_type']['end'] = self._io.pos()
            self._debug['key_strings']['start'] = self._io.pos()
            self.key_strings = self._io.read_u4le()
            self._debug['key_strings']['end'] = self._io.pos()
            self._debug['last_public_key']['start'] = self._io.pos()
            self.last_public_key = self._io.read_u4le()
            self._debug['last_public_key']['end'] = self._io.pos()
            self._debug['type_id_offset']['start'] = self._io.pos()
            self.type_id_offset = self._io.read_u4le()
            self._debug['type_id_offset']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Xml(KaitaiStruct):
        SEQ_FIELDS = ["header", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.Xml, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = self._io.read_bytes(self._parent.header.len_header - 8)
            self._debug['header']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            self._raw_body = self._io.read_bytes_full()
            _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
            self.body = AndroidResource.XmlBody(_io__raw_body, self, self._root)
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.body._fetch_instances()


    class XmlBody(KaitaiStruct):
        SEQ_FIELDS = ["nodes"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidResource.XmlBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['nodes']['start'] = self._io.pos()
            self._debug['nodes']['arr'] = []
            self.nodes = []
            i = 0
            while not self._io.is_eof():
                self._debug['nodes']['arr'].append({'start': self._io.pos()})
                self.nodes.append(AndroidResource.Chunk(self._io, self, self._root))
                self._debug['nodes']['arr'][len(self.nodes) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['nodes']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.nodes)):
                pass
                self.nodes[i]._fetch_instances()




