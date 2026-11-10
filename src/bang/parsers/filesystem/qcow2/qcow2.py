# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Qcow2(KaitaiStruct):
    """
    .. seealso::
       Source - https://gitlab.com/qemu-project/qemu/-/blob/5135fe71101db08cf65090963247f9b1b8138b73/docs/interop/qcow2.txt
    """

    class CryptMethods(IntEnum):
        no_encryption = 0
        aes = 1
        luks = 2

    class HeaderExtensionTypes(IntEnum):
        end = 0
        full_disk_encryption_header_pointer = 87539319
        bitmaps_extension = 595929205
        external_data_file_name_string = 1145132097
        feature_name_table = 1745090647
        backing_file_format_name_string = 3799591626
    SEQ_FIELDS = ["header_cluster"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Qcow2, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header_cluster']['start'] = self._io.pos()
        self._raw_header_cluster = self._io.read_bytes(self.cluster_size)
        _io__raw_header_cluster = KaitaiStream(BytesIO(self._raw_header_cluster))
        self.header_cluster = Qcow2.Header(_io__raw_header_cluster, self, self._root)
        self._debug['header_cluster']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header_cluster._fetch_instances()
        _ = self.cluster_size_bits
        if hasattr(self, '_m_cluster_size_bits'):
            pass


    class FeatureName(KaitaiStruct):

        class FeatureTypes(IntEnum):
            incompatible = 0
            compatible = 1
            autoclear = 2
        SEQ_FIELDS = ["type", "bit_numner", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Qcow2.FeatureName, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Qcow2.FeatureName.FeatureTypes, self._io.read_u1())
            self._debug['type']['end'] = self._io.pos()
            self._debug['bit_numner']['start'] = self._io.pos()
            self.bit_numner = self._io.read_u1()
            self._debug['bit_numner']['end'] = self._io.pos()
            if not self.bit_numner <= 63:
                raise kaitaistruct.ValidationGreaterThanError(63, self.bit_numner, self._io, u"/types/feature_name/seq/1")
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(46), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class FeatureNameTable(KaitaiStruct):
        SEQ_FIELDS = ["feature_names"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Qcow2.FeatureNameTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['feature_names']['start'] = self._io.pos()
            self._debug['feature_names']['arr'] = []
            self.feature_names = []
            i = 0
            while not self._io.is_eof():
                self._debug['feature_names']['arr'].append({'start': self._io.pos()})
                self.feature_names.append(Qcow2.FeatureName(self._io, self, self._root))
                self._debug['feature_names']['arr'][len(self.feature_names) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['feature_names']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.feature_names)):
                pass
                self.feature_names[i]._fetch_instances()



    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "ofs_backing_file", "len_backing_file", "cluster_bits", "size", "crypt_method", "num_l1_entries", "ofs_l1_table", "ofs_refcount_table", "refcount_table_clusters", "nb_snapshots", "ofs_snapshots", "v3header", "header_extensions"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Qcow2.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x51\x46\x49\xFB":
                raise kaitaistruct.ValidationNotEqualError(b"\x51\x46\x49\xFB", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4be()
            self._debug['version']['end'] = self._io.pos()
            if not  ((self.version == 2) or (self.version == 3)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/types/header/seq/1")
            self._debug['ofs_backing_file']['start'] = self._io.pos()
            self.ofs_backing_file = self._io.read_u8be()
            self._debug['ofs_backing_file']['end'] = self._io.pos()
            self._debug['len_backing_file']['start'] = self._io.pos()
            self.len_backing_file = self._io.read_u4be()
            self._debug['len_backing_file']['end'] = self._io.pos()
            self._debug['cluster_bits']['start'] = self._io.pos()
            self.cluster_bits = self._io.read_u4be()
            self._debug['cluster_bits']['end'] = self._io.pos()
            if not self.cluster_bits >= 9:
                raise kaitaistruct.ValidationLessThanError(9, self.cluster_bits, self._io, u"/types/header/seq/4")
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u8be()
            self._debug['size']['end'] = self._io.pos()
            self._debug['crypt_method']['start'] = self._io.pos()
            self.crypt_method = KaitaiStream.resolve_enum(Qcow2.CryptMethods, self._io.read_u4be())
            self._debug['crypt_method']['end'] = self._io.pos()
            if not  ((self.crypt_method == Qcow2.CryptMethods.no_encryption) or (self.crypt_method == Qcow2.CryptMethods.aes) or (self.crypt_method == Qcow2.CryptMethods.luks)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.crypt_method, self._io, u"/types/header/seq/6")
            self._debug['num_l1_entries']['start'] = self._io.pos()
            self.num_l1_entries = self._io.read_u4be()
            self._debug['num_l1_entries']['end'] = self._io.pos()
            self._debug['ofs_l1_table']['start'] = self._io.pos()
            self.ofs_l1_table = self._io.read_u8be()
            self._debug['ofs_l1_table']['end'] = self._io.pos()
            _ = self.ofs_l1_table
            if not self.ofs_l1_table % self._root.cluster_size == 0:
                raise kaitaistruct.ValidationExprError(self.ofs_l1_table, self._io, u"/types/header/seq/8")
            self._debug['ofs_refcount_table']['start'] = self._io.pos()
            self.ofs_refcount_table = self._io.read_u8be()
            self._debug['ofs_refcount_table']['end'] = self._io.pos()
            _ = self.ofs_refcount_table
            if not self.ofs_refcount_table % self._root.cluster_size == 0:
                raise kaitaistruct.ValidationExprError(self.ofs_refcount_table, self._io, u"/types/header/seq/9")
            self._debug['refcount_table_clusters']['start'] = self._io.pos()
            self.refcount_table_clusters = self._io.read_u4be()
            self._debug['refcount_table_clusters']['end'] = self._io.pos()
            self._debug['nb_snapshots']['start'] = self._io.pos()
            self.nb_snapshots = self._io.read_u4be()
            self._debug['nb_snapshots']['end'] = self._io.pos()
            self._debug['ofs_snapshots']['start'] = self._io.pos()
            self.ofs_snapshots = self._io.read_u8be()
            self._debug['ofs_snapshots']['end'] = self._io.pos()
            _ = self.ofs_snapshots
            if not self.ofs_snapshots % self._root.cluster_size == 0:
                raise kaitaistruct.ValidationExprError(self.ofs_snapshots, self._io, u"/types/header/seq/12")
            if self.version > 2:
                pass
                self._debug['v3header']['start'] = self._io.pos()
                self.v3header = Qcow2.V3header(self._io, self, self._root)
                self._debug['v3header']['end'] = self._io.pos()

            self._debug['header_extensions']['start'] = self._io.pos()
            self._debug['header_extensions']['arr'] = []
            self.header_extensions = []
            i = 0
            while True:
                self._debug['header_extensions']['arr'].append({'start': self._io.pos()})
                _ = Qcow2.HeaderExtension(self._io, self, self._root)
                self.header_extensions.append(_)
                self._debug['header_extensions']['arr'][len(self.header_extensions) - 1]['end'] = self._io.pos()
                if  ((_.is_end) or (self._io.is_eof())) :
                    break
                i += 1
            self._debug['header_extensions']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            if self.version > 2:
                pass
                self.v3header._fetch_instances()

            for i in range(len(self.header_extensions)):
                pass
                self.header_extensions[i]._fetch_instances()

            _ = self.backing_file
            if hasattr(self, '_m_backing_file'):
                pass

            _ = self.l1table
            if hasattr(self, '_m_l1table'):
                pass
                self._m_l1table._fetch_instances()

            _ = self.refcount_table
            if hasattr(self, '_m_refcount_table'):
                pass
                self._m_refcount_table._fetch_instances()

            _ = self.snapshot_table
            if hasattr(self, '_m_snapshot_table'):
                pass
                self._m_snapshot_table._fetch_instances()


        @property
        def backing_file(self):
            if hasattr(self, '_m_backing_file'):
                return self._m_backing_file

            if self.len_backing_file != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_backing_file)
                self._debug['_m_backing_file']['start'] = io.pos()
                self._m_backing_file = (io.read_bytes(self.len_backing_file)).decode(u"UTF-8")
                self._debug['_m_backing_file']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_backing_file', None)

        @property
        def l1table(self):
            if hasattr(self, '_m_l1table'):
                return self._m_l1table

            if self.ofs_l1_table != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_l1_table)
                self._debug['_m_l1table']['start'] = io.pos()
                self._m_l1table = Qcow2.L1Table(self.num_l1_entries, io, self, self._root)
                self._debug['_m_l1table']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_l1table', None)

        @property
        def refcount_table(self):
            if hasattr(self, '_m_refcount_table'):
                return self._m_refcount_table

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_refcount_table)
            self._debug['_m_refcount_table']['start'] = io.pos()
            self._raw__m_refcount_table = io.read_bytes(self.refcount_table_clusters * self._root.cluster_size)
            _io__raw__m_refcount_table = KaitaiStream(BytesIO(self._raw__m_refcount_table))
            self._m_refcount_table = Qcow2.RefcountTable(_io__raw__m_refcount_table, self, self._root)
            self._debug['_m_refcount_table']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_refcount_table', None)

        @property
        def snapshot_table(self):
            if hasattr(self, '_m_snapshot_table'):
                return self._m_snapshot_table

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_snapshots)
            self._debug['_m_snapshot_table']['start'] = io.pos()
            self._m_snapshot_table = Qcow2.SnapshotTable(self.nb_snapshots, io, self, self._root)
            self._debug['_m_snapshot_table']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_snapshot_table', None)


    class HeaderExtension(KaitaiStruct):
        SEQ_FIELDS = ["type", "len_extension", "data", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Qcow2.HeaderExtension, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Qcow2.HeaderExtensionTypes, self._io.read_u4be())
            self._debug['type']['end'] = self._io.pos()
            if not  ((self.type == Qcow2.HeaderExtensionTypes.end) or (self.type == Qcow2.HeaderExtensionTypes.backing_file_format_name_string) or (self.type == Qcow2.HeaderExtensionTypes.feature_name_table) or (self.type == Qcow2.HeaderExtensionTypes.bitmaps_extension) or (self.type == Qcow2.HeaderExtensionTypes.full_disk_encryption_header_pointer) or (self.type == Qcow2.HeaderExtensionTypes.external_data_file_name_string)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.type, self._io, u"/types/header_extension/seq/0")
            self._debug['len_extension']['start'] = self._io.pos()
            self.len_extension = self._io.read_u4be()
            self._debug['len_extension']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            _on = self.type
            if _on == Qcow2.HeaderExtensionTypes.backing_file_format_name_string:
                pass
                self.data = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_extension), 0, False)).decode(u"UTF-8")
            elif _on == Qcow2.HeaderExtensionTypes.feature_name_table:
                pass
                self._raw_data = self._io.read_bytes(self.len_extension)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Qcow2.FeatureNameTable(_io__raw_data, self, self._root)
            else:
                pass
                self.data = self._io.read_bytes(self.len_extension)
            self._debug['data']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self.len_extension) % 8)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.type
            if _on == Qcow2.HeaderExtensionTypes.backing_file_format_name_string:
                pass
            elif _on == Qcow2.HeaderExtensionTypes.feature_name_table:
                pass
                self.data._fetch_instances()
            else:
                pass

        @property
        def is_end(self):
            if hasattr(self, '_m_is_end'):
                return self._m_is_end

            self._m_is_end = self.type == Qcow2.HeaderExtensionTypes.end
            return getattr(self, '_m_is_end', None)


    class L1Entry(KaitaiStruct):
        SEQ_FIELDS = ["requires_cow", "reserved", "ofs_l2_table", "reserved2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Qcow2.L1Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['requires_cow']['start'] = self._io.pos()
            self.requires_cow = self._io.read_bits_int_be(1) != 0
            self._debug['requires_cow']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bits_int_be(7)
            self._debug['reserved']['end'] = self._io.pos()
            if not self.reserved == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.reserved, self._io, u"/types/l1_entry/seq/1")
            self._debug['ofs_l2_table']['start'] = self._io.pos()
            self.ofs_l2_table = self._io.read_bits_int_be(47)
            self._debug['ofs_l2_table']['end'] = self._io.pos()
            _ = self.ofs_l2_table
            if not self.ofs_l2_table % self._root.cluster_size == 0:
                raise kaitaistruct.ValidationExprError(self.ofs_l2_table, self._io, u"/types/l1_entry/seq/2")
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bits_int_be(9)
            self._debug['reserved2']['end'] = self._io.pos()
            if not self.reserved2 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.reserved2, self._io, u"/types/l1_entry/seq/3")


        def _fetch_instances(self):
            pass


    class L1Table(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, num_l1_entries, _io, _parent=None, _root=None):
            super(Qcow2.L1Table, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_l1_entries = num_l1_entries
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_l1_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(self._io.read_bytes(2))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass



    class RefcountTable(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Qcow2.RefcountTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(self._io.read_bytes(2))
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass



    class SnapshotEntry(KaitaiStruct):
        SEQ_FIELDS = ["ofs_l1_table", "num_l1_entries", "len_unique_id", "len_name", "snapshot_time", "snapshot_time_nanoseconds", "snapshot_runtime_nanoseconds", "len_vm_state", "len_extra_data", "len_vm_state2", "len_virtual_disk_size", "icount_value", "unique_id", "snapshot_name", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Qcow2.SnapshotEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_l1_table']['start'] = self._io.pos()
            self.ofs_l1_table = self._io.read_u8be()
            self._debug['ofs_l1_table']['end'] = self._io.pos()
            _ = self.ofs_l1_table
            if not self.ofs_l1_table % self._root.cluster_size == 0:
                raise kaitaistruct.ValidationExprError(self.ofs_l1_table, self._io, u"/types/snapshot_entry/seq/0")
            self._debug['num_l1_entries']['start'] = self._io.pos()
            self.num_l1_entries = self._io.read_u4be()
            self._debug['num_l1_entries']['end'] = self._io.pos()
            self._debug['len_unique_id']['start'] = self._io.pos()
            self.len_unique_id = self._io.read_u2be()
            self._debug['len_unique_id']['end'] = self._io.pos()
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_u2be()
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['snapshot_time']['start'] = self._io.pos()
            self.snapshot_time = self._io.read_u4be()
            self._debug['snapshot_time']['end'] = self._io.pos()
            self._debug['snapshot_time_nanoseconds']['start'] = self._io.pos()
            self.snapshot_time_nanoseconds = self._io.read_u4be()
            self._debug['snapshot_time_nanoseconds']['end'] = self._io.pos()
            self._debug['snapshot_runtime_nanoseconds']['start'] = self._io.pos()
            self.snapshot_runtime_nanoseconds = self._io.read_u8be()
            self._debug['snapshot_runtime_nanoseconds']['end'] = self._io.pos()
            self._debug['len_vm_state']['start'] = self._io.pos()
            self.len_vm_state = self._io.read_u4be()
            self._debug['len_vm_state']['end'] = self._io.pos()
            self._debug['len_extra_data']['start'] = self._io.pos()
            self.len_extra_data = self._io.read_u4be()
            self._debug['len_extra_data']['end'] = self._io.pos()
            if self.len_extra_data >= 8:
                pass
                self._debug['len_vm_state2']['start'] = self._io.pos()
                self.len_vm_state2 = self._io.read_u8be()
                self._debug['len_vm_state2']['end'] = self._io.pos()

            if self.len_extra_data >= 16:
                pass
                self._debug['len_virtual_disk_size']['start'] = self._io.pos()
                self.len_virtual_disk_size = self._io.read_u8be()
                self._debug['len_virtual_disk_size']['end'] = self._io.pos()

            if self.len_extra_data >= 24:
                pass
                self._debug['icount_value']['start'] = self._io.pos()
                self.icount_value = self._io.read_u8be()
                self._debug['icount_value']['end'] = self._io.pos()

            self._debug['unique_id']['start'] = self._io.pos()
            self.unique_id = (self._io.read_bytes(self.len_unique_id)).decode(u"UTF-8")
            self._debug['unique_id']['end'] = self._io.pos()
            self._debug['snapshot_name']['start'] = self._io.pos()
            self.snapshot_name = (self._io.read_bytes(self.len_name)).decode(u"UTF-8")
            self._debug['snapshot_name']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self._io.pos()) % 8)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            if self.len_extra_data >= 8:
                pass

            if self.len_extra_data >= 16:
                pass

            if self.len_extra_data >= 24:
                pass

            _ = self.l1table
            if hasattr(self, '_m_l1table'):
                pass
                self._m_l1table._fetch_instances()


        @property
        def l1table(self):
            if hasattr(self, '_m_l1table'):
                return self._m_l1table

            if self.ofs_l1_table != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_l1_table)
                self._debug['_m_l1table']['start'] = io.pos()
                self._m_l1table = Qcow2.L1Table(self.num_l1_entries, io, self, self._root)
                self._debug['_m_l1table']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_l1table', None)


    class SnapshotTable(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, num_snapshots, _io, _parent=None, _root=None):
            super(Qcow2.SnapshotTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_snapshots = num_snapshots
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_snapshots):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(Qcow2.SnapshotEntry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class V3header(KaitaiStruct):
        SEQ_FIELDS = ["incompatible_features", "compatible_features", "autoclear_features", "refcount_order", "len_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Qcow2.V3header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['incompatible_features']['start'] = self._io.pos()
            self.incompatible_features = self._io.read_u8be()
            self._debug['incompatible_features']['end'] = self._io.pos()
            self._debug['compatible_features']['start'] = self._io.pos()
            self.compatible_features = self._io.read_u8be()
            self._debug['compatible_features']['end'] = self._io.pos()
            self._debug['autoclear_features']['start'] = self._io.pos()
            self.autoclear_features = self._io.read_u8be()
            self._debug['autoclear_features']['end'] = self._io.pos()
            self._debug['refcount_order']['start'] = self._io.pos()
            self.refcount_order = self._io.read_u4be()
            self._debug['refcount_order']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4be()
            self._debug['len_header']['end'] = self._io.pos()
            _ = self.len_header
            if not  ((self.len_header >= 104) and (self.len_header % 8 == 0)) :
                raise kaitaistruct.ValidationExprError(self.len_header, self._io, u"/types/v3header/seq/4")


        def _fetch_instances(self):
            pass


    @property
    def cluster_size(self):
        if hasattr(self, '_m_cluster_size'):
            return self._m_cluster_size

        self._m_cluster_size = 1 << self.cluster_size_bits
        return getattr(self, '_m_cluster_size', None)

    @property
    def cluster_size_bits(self):
        if hasattr(self, '_m_cluster_size_bits'):
            return self._m_cluster_size_bits

        _pos = self._io.pos()
        self._io.seek(20)
        self._debug['_m_cluster_size_bits']['start'] = self._io.pos()
        self._m_cluster_size_bits = self._io.read_u4be()
        self._debug['_m_cluster_size_bits']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_cluster_size_bits', None)


