# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class VfatDirectoryRec(KaitaiStruct):
    SEQ_FIELDS = ["short_name", "short_ext", "attributes", "attributes_cpm", "create_time_ms", "create_time", "create_date", "access_date", "access_rights", "modified_time", "modified_date", "start_clus", "file_size"]
    def __init__(self, _io, _parent=None, _root=None):
        super(VfatDirectoryRec, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['short_name']['start'] = self._io.pos()
        self.short_name = self._io.read_bytes(8)
        self._debug['short_name']['end'] = self._io.pos()
        self._debug['short_ext']['start'] = self._io.pos()
        self.short_ext = self._io.read_bytes(3)
        self._debug['short_ext']['end'] = self._io.pos()
        self._debug['attributes']['start'] = self._io.pos()
        self.attributes = self._io.read_u1()
        self._debug['attributes']['end'] = self._io.pos()
        self._debug['attributes_cpm']['start'] = self._io.pos()
        self.attributes_cpm = self._io.read_u1()
        self._debug['attributes_cpm']['end'] = self._io.pos()
        self._debug['create_time_ms']['start'] = self._io.pos()
        self.create_time_ms = self._io.read_u1()
        self._debug['create_time_ms']['end'] = self._io.pos()
        self._debug['create_time']['start'] = self._io.pos()
        self.create_time = self._io.read_u2le()
        self._debug['create_time']['end'] = self._io.pos()
        self._debug['create_date']['start'] = self._io.pos()
        self.create_date = self._io.read_u2le()
        self._debug['create_date']['end'] = self._io.pos()
        self._debug['access_date']['start'] = self._io.pos()
        self.access_date = self._io.read_u2le()
        self._debug['access_date']['end'] = self._io.pos()
        self._debug['access_rights']['start'] = self._io.pos()
        self.access_rights = self._io.read_u2le()
        self._debug['access_rights']['end'] = self._io.pos()
        self._debug['modified_time']['start'] = self._io.pos()
        self.modified_time = self._io.read_u2le()
        self._debug['modified_time']['end'] = self._io.pos()
        self._debug['modified_date']['start'] = self._io.pos()
        self.modified_date = self._io.read_u2le()
        self._debug['modified_date']['end'] = self._io.pos()
        self._debug['start_clus']['start'] = self._io.pos()
        self.start_clus = self._io.read_u2le()
        self._debug['start_clus']['end'] = self._io.pos()
        self._debug['file_size']['start'] = self._io.pos()
        self.file_size = self._io.read_u4le()
        self._debug['file_size']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _ = self.lfn_part1
        if hasattr(self, '_m_lfn_part1'):
            pass

        _ = self.lfn_part2
        if hasattr(self, '_m_lfn_part2'):
            pass

        _ = self.lfn_part3
        if hasattr(self, '_m_lfn_part3'):
            pass

        _ = self.lfn_part_seq_nr
        if hasattr(self, '_m_lfn_part_seq_nr'):
            pass


    @property
    def attr_archive(self):
        if hasattr(self, '_m_attr_archive'):
            return self._m_attr_archive

        self._m_attr_archive = self.attributes & 32
        return getattr(self, '_m_attr_archive', None)

    @property
    def attr_device(self):
        if hasattr(self, '_m_attr_device'):
            return self._m_attr_device

        self._m_attr_device = self.attributes & 64
        return getattr(self, '_m_attr_device', None)

    @property
    def attr_hidden(self):
        if hasattr(self, '_m_attr_hidden'):
            return self._m_attr_hidden

        self._m_attr_hidden = self.attributes & 2
        return getattr(self, '_m_attr_hidden', None)

    @property
    def attr_read_only(self):
        if hasattr(self, '_m_attr_read_only'):
            return self._m_attr_read_only

        self._m_attr_read_only = self.attributes & 1
        return getattr(self, '_m_attr_read_only', None)

    @property
    def attr_reserved(self):
        if hasattr(self, '_m_attr_reserved'):
            return self._m_attr_reserved

        self._m_attr_reserved = self.attributes & 128
        return getattr(self, '_m_attr_reserved', None)

    @property
    def attr_subdirectory(self):
        if hasattr(self, '_m_attr_subdirectory'):
            return self._m_attr_subdirectory

        self._m_attr_subdirectory = self.attributes & 16
        return getattr(self, '_m_attr_subdirectory', None)

    @property
    def attr_system(self):
        if hasattr(self, '_m_attr_system'):
            return self._m_attr_system

        self._m_attr_system = self.attributes & 4
        return getattr(self, '_m_attr_system', None)

    @property
    def attr_volume_label(self):
        if hasattr(self, '_m_attr_volume_label'):
            return self._m_attr_volume_label

        self._m_attr_volume_label = self.attributes & 8
        return getattr(self, '_m_attr_volume_label', None)

    @property
    def is_lfn_entry(self):
        if hasattr(self, '_m_is_lfn_entry'):
            return self._m_is_lfn_entry

        self._m_is_lfn_entry = self.attributes == 15
        return getattr(self, '_m_is_lfn_entry', None)

    @property
    def lfn_part1(self):
        if hasattr(self, '_m_lfn_part1'):
            return self._m_lfn_part1

        _pos = self._io.pos()
        self._io.seek(1)
        self._debug['_m_lfn_part1']['start'] = self._io.pos()
        self._m_lfn_part1 = self._io.read_bytes(10)
        self._debug['_m_lfn_part1']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_lfn_part1', None)

    @property
    def lfn_part2(self):
        if hasattr(self, '_m_lfn_part2'):
            return self._m_lfn_part2

        _pos = self._io.pos()
        self._io.seek(14)
        self._debug['_m_lfn_part2']['start'] = self._io.pos()
        self._m_lfn_part2 = self._io.read_bytes(12)
        self._debug['_m_lfn_part2']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_lfn_part2', None)

    @property
    def lfn_part3(self):
        if hasattr(self, '_m_lfn_part3'):
            return self._m_lfn_part3

        _pos = self._io.pos()
        self._io.seek(28)
        self._debug['_m_lfn_part3']['start'] = self._io.pos()
        self._m_lfn_part3 = self._io.read_bytes(4)
        self._debug['_m_lfn_part3']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_lfn_part3', None)

    @property
    def lfn_part_seq_nr(self):
        if hasattr(self, '_m_lfn_part_seq_nr'):
            return self._m_lfn_part_seq_nr

        _pos = self._io.pos()
        self._io.seek(0)
        self._debug['_m_lfn_part_seq_nr']['start'] = self._io.pos()
        self._m_lfn_part_seq_nr = self._io.read_bytes(1)
        self._debug['_m_lfn_part_seq_nr']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_lfn_part_seq_nr', None)


