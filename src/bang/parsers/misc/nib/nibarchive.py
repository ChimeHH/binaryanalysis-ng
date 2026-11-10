# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Nibarchive(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/matsmattsson/nibsqueeze/blob/master/NibArchive.md
    """
    SEQ_FIELDS = ["header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Nibarchive, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Nibarchive.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        _ = self.class_names
        if hasattr(self, '_m_class_names'):
            pass
            for i in range(len(self._m_class_names)):
                pass
                self._m_class_names[i]._fetch_instances()


        _ = self.keys
        if hasattr(self, '_m_keys'):
            pass
            for i in range(len(self._m_keys)):
                pass
                self._m_keys[i]._fetch_instances()


        _ = self.objects
        if hasattr(self, '_m_objects'):
            pass
            for i in range(len(self._m_objects)):
                pass
                self._m_objects[i]._fetch_instances()


        _ = self.values
        if hasattr(self, '_m_values'):
            pass
            for i in range(len(self._m_values)):
                pass
                self._m_values[i]._fetch_instances()



    class ClassName(KaitaiStruct):
        SEQ_FIELDS = ["len_name", "num_other_ints", "other_ints", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Nibarchive.ClassName, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = Nibarchive.CompressedInteger(self._io, self, self._root)
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['num_other_ints']['start'] = self._io.pos()
            self.num_other_ints = Nibarchive.CompressedInteger(self._io, self, self._root)
            self._debug['num_other_ints']['end'] = self._io.pos()
            self._debug['other_ints']['start'] = self._io.pos()
            self._debug['other_ints']['arr'] = []
            self.other_ints = []
            for i in range(self.num_other_ints.value):
                self._debug['other_ints']['arr'].append({'start': self._io.pos()})
                self.other_ints.append(self._io.read_u4le())
                self._debug['other_ints']['arr'][i]['end'] = self._io.pos()

            self._debug['other_ints']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_name.value), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.len_name._fetch_instances()
            self.num_other_ints._fetch_instances()
            for i in range(len(self.other_ints)):
                pass



    class CompressedInteger(KaitaiStruct):
        SEQ_FIELDS = ["groups"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Nibarchive.CompressedInteger, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['groups']['start'] = self._io.pos()
            self._debug['groups']['arr'] = []
            self.groups = []
            i = 0
            while True:
                self._debug['groups']['arr'].append({'start': self._io.pos()})
                _ = Nibarchive.CompressedInteger.Group(self._io, self, self._root)
                self.groups.append(_)
                self._debug['groups']['arr'][len(self.groups) - 1]['end'] = self._io.pos()
                if (not (_.has_next)):
                    break
                i += 1
            self._debug['groups']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.groups)):
                pass
                self.groups[i]._fetch_instances()


        class Group(KaitaiStruct):
            """One byte group, clearly divided into 7-bit "value" chunk and 1-bit "continuation" flag.
            """
            SEQ_FIELDS = ["b"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Nibarchive.CompressedInteger.Group, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['b']['start'] = self._io.pos()
                self.b = self._io.read_u1()
                self._debug['b']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass

            @property
            def has_next(self):
                """If true, then we have more bytes to read."""
                if hasattr(self, '_m_has_next'):
                    return self._m_has_next

                self._m_has_next = self.b & 128 == 0
                return getattr(self, '_m_has_next', None)

            @property
            def value(self):
                """The 7-bit (base128) numeric value chunk of this group."""
                if hasattr(self, '_m_value'):
                    return self._m_value

                self._m_value = self.b & 127
                return getattr(self, '_m_value', None)


        @property
        def len(self):
            if hasattr(self, '_m_len'):
                return self._m_len

            self._m_len = len(self.groups)
            return getattr(self, '_m_len', None)

        @property
        def value(self):
            """Resulting value as normal integer."""
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = ((((((self.groups[0].value + (self.groups[1].value << 7 if self.len >= 2 else 0)) + (self.groups[2].value << 14 if self.len >= 3 else 0)) + (self.groups[3].value << 21 if self.len >= 4 else 0)) + (self.groups[4].value << 28 if self.len >= 5 else 0)) + (self.groups[5].value << 35 if self.len >= 6 else 0)) + (self.groups[6].value << 42 if self.len >= 7 else 0)) + (self.groups[7].value << 49 if self.len >= 8 else 0)
            return getattr(self, '_m_value', None)


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "constant_1", "constant_2", "num_objects", "ofs_objects", "num_keys", "ofs_keys", "num_values", "ofs_values", "num_class_names", "ofs_class_names"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Nibarchive.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(10)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x4E\x49\x42\x41\x72\x63\x68\x69\x76\x65":
                raise kaitaistruct.ValidationNotEqualError(b"\x4E\x49\x42\x41\x72\x63\x68\x69\x76\x65", self.magic, self._io, u"/types/header/seq/0")
            self._debug['constant_1']['start'] = self._io.pos()
            self.constant_1 = self._io.read_u4le()
            self._debug['constant_1']['end'] = self._io.pos()
            if not self.constant_1 == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.constant_1, self._io, u"/types/header/seq/1")
            self._debug['constant_2']['start'] = self._io.pos()
            self.constant_2 = self._io.read_u4le()
            self._debug['constant_2']['end'] = self._io.pos()
            self._debug['num_objects']['start'] = self._io.pos()
            self.num_objects = self._io.read_u4le()
            self._debug['num_objects']['end'] = self._io.pos()
            self._debug['ofs_objects']['start'] = self._io.pos()
            self.ofs_objects = self._io.read_u4le()
            self._debug['ofs_objects']['end'] = self._io.pos()
            self._debug['num_keys']['start'] = self._io.pos()
            self.num_keys = self._io.read_u4le()
            self._debug['num_keys']['end'] = self._io.pos()
            self._debug['ofs_keys']['start'] = self._io.pos()
            self.ofs_keys = self._io.read_u4le()
            self._debug['ofs_keys']['end'] = self._io.pos()
            self._debug['num_values']['start'] = self._io.pos()
            self.num_values = self._io.read_u4le()
            self._debug['num_values']['end'] = self._io.pos()
            self._debug['ofs_values']['start'] = self._io.pos()
            self.ofs_values = self._io.read_u4le()
            self._debug['ofs_values']['end'] = self._io.pos()
            self._debug['num_class_names']['start'] = self._io.pos()
            self.num_class_names = self._io.read_u4le()
            self._debug['num_class_names']['end'] = self._io.pos()
            self._debug['ofs_class_names']['start'] = self._io.pos()
            self.ofs_class_names = self._io.read_u4le()
            self._debug['ofs_class_names']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Key(KaitaiStruct):
        SEQ_FIELDS = ["len_name", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Nibarchive.Key, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = Nibarchive.CompressedInteger(self._io, self, self._root)
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(self.len_name.value)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.len_name._fetch_instances()


    class Obj(KaitaiStruct):
        SEQ_FIELDS = ["class_name_index_val", "values_index_val", "value_count_val"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Nibarchive.Obj, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['class_name_index_val']['start'] = self._io.pos()
            self.class_name_index_val = Nibarchive.CompressedInteger(self._io, self, self._root)
            self._debug['class_name_index_val']['end'] = self._io.pos()
            self._debug['values_index_val']['start'] = self._io.pos()
            self.values_index_val = Nibarchive.CompressedInteger(self._io, self, self._root)
            self._debug['values_index_val']['end'] = self._io.pos()
            self._debug['value_count_val']['start'] = self._io.pos()
            self.value_count_val = Nibarchive.CompressedInteger(self._io, self, self._root)
            self._debug['value_count_val']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.class_name_index_val._fetch_instances()
            self.values_index_val._fetch_instances()
            self.value_count_val._fetch_instances()

        @property
        def class_name_index(self):
            if hasattr(self, '_m_class_name_index'):
                return self._m_class_name_index

            self._m_class_name_index = self.class_name_index_val.value
            return getattr(self, '_m_class_name_index', None)

        @property
        def value_count(self):
            if hasattr(self, '_m_value_count'):
                return self._m_value_count

            self._m_value_count = self.value_count_val.value
            return getattr(self, '_m_value_count', None)

        @property
        def values_index(self):
            if hasattr(self, '_m_values_index'):
                return self._m_values_index

            self._m_values_index = self.values_index_val.value
            return getattr(self, '_m_values_index', None)


    class Value(KaitaiStruct):

        class ValueType(IntEnum):
            int8 = 0
            int16 = 1
            int32 = 2
            int64 = 3
            true = 4
            false = 5
            float = 6
            double = 7
            data = 8
            nil = 9
            object_reference = 10
        SEQ_FIELDS = ["key_index", "type", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Nibarchive.Value, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['key_index']['start'] = self._io.pos()
            self.key_index = Nibarchive.CompressedInteger(self._io, self, self._root)
            self._debug['key_index']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Nibarchive.Value.ValueType, self._io.read_u1())
            self._debug['type']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            _on = self.type
            if _on == Nibarchive.Value.ValueType.data:
                pass
                self.data = Nibarchive.Value.ValueData(self._io, self, self._root)
            elif _on == Nibarchive.Value.ValueType.double:
                pass
                self.data = self._io.read_f8le()
            elif _on == Nibarchive.Value.ValueType.float:
                pass
                self.data = self._io.read_f4le()
            elif _on == Nibarchive.Value.ValueType.int16:
                pass
                self.data = self._io.read_u2le()
            elif _on == Nibarchive.Value.ValueType.int32:
                pass
                self.data = self._io.read_u4le()
            elif _on == Nibarchive.Value.ValueType.int64:
                pass
                self.data = self._io.read_u8le()
            elif _on == Nibarchive.Value.ValueType.int8:
                pass
                self.data = self._io.read_u1()
            elif _on == Nibarchive.Value.ValueType.object_reference:
                pass
                self.data = self._io.read_u4le()
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.key_index._fetch_instances()
            _on = self.type
            if _on == Nibarchive.Value.ValueType.data:
                pass
                self.data._fetch_instances()
            elif _on == Nibarchive.Value.ValueType.double:
                pass
            elif _on == Nibarchive.Value.ValueType.float:
                pass
            elif _on == Nibarchive.Value.ValueType.int16:
                pass
            elif _on == Nibarchive.Value.ValueType.int32:
                pass
            elif _on == Nibarchive.Value.ValueType.int64:
                pass
            elif _on == Nibarchive.Value.ValueType.int8:
                pass
            elif _on == Nibarchive.Value.ValueType.object_reference:
                pass

        class ValueData(KaitaiStruct):
            SEQ_FIELDS = ["len_data", "data"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Nibarchive.Value.ValueData, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['len_data']['start'] = self._io.pos()
                self.len_data = Nibarchive.CompressedInteger(self._io, self, self._root)
                self._debug['len_data']['end'] = self._io.pos()
                self._debug['data']['start'] = self._io.pos()
                self.data = self._io.read_bytes(self.len_data.value)
                self._debug['data']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.len_data._fetch_instances()



    @property
    def class_names(self):
        if hasattr(self, '_m_class_names'):
            return self._m_class_names

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_class_names)
        self._debug['_m_class_names']['start'] = self._io.pos()
        self._debug['_m_class_names']['arr'] = []
        self._m_class_names = []
        for i in range(self.header.num_class_names):
            self._debug['_m_class_names']['arr'].append({'start': self._io.pos()})
            self._m_class_names.append(Nibarchive.ClassName(self._io, self, self._root))
            self._debug['_m_class_names']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_class_names']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_class_names', None)

    @property
    def keys(self):
        if hasattr(self, '_m_keys'):
            return self._m_keys

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_keys)
        self._debug['_m_keys']['start'] = self._io.pos()
        self._debug['_m_keys']['arr'] = []
        self._m_keys = []
        for i in range(self.header.num_keys):
            self._debug['_m_keys']['arr'].append({'start': self._io.pos()})
            self._m_keys.append(Nibarchive.Key(self._io, self, self._root))
            self._debug['_m_keys']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_keys']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_keys', None)

    @property
    def objects(self):
        if hasattr(self, '_m_objects'):
            return self._m_objects

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_objects)
        self._debug['_m_objects']['start'] = self._io.pos()
        self._debug['_m_objects']['arr'] = []
        self._m_objects = []
        for i in range(self.header.num_objects):
            self._debug['_m_objects']['arr'].append({'start': self._io.pos()})
            self._m_objects.append(Nibarchive.Obj(self._io, self, self._root))
            self._debug['_m_objects']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_objects']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_objects', None)

    @property
    def values(self):
        if hasattr(self, '_m_values'):
            return self._m_values

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_values)
        self._debug['_m_values']['start'] = self._io.pos()
        self._debug['_m_values']['arr'] = []
        self._m_values = []
        for i in range(self.header.num_values):
            self._debug['_m_values']['arr'].append({'start': self._io.pos()})
            self._m_values.append(Nibarchive.Value(self._io, self, self._root))
            self._debug['_m_values']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_values']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_values', None)


