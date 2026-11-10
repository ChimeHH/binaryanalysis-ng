# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Nb0(KaitaiStruct):
    """A barely documented older Android firmware format used on FreeScale/NXP
    devices.
    
    Test file (if you can find it): "ViewPad 7 Firmware v3_42_uk.zip". The
    firmware update for the Acer BeTouch E130 also contains it, although it is
    hidden deep inside the firmware.
    
    Note: the extension "nb0' is also often used for Windows CE files.
    
    .. seealso::
       Source - https://github.com/yohanes/Acer-BeTouch-E130-RUT/blob/master/nb0.h
    
    
    .. seealso::
       Source - https://github.com/yohanes/Acer-BeTouch-E130-RUT/blob/master/nb0.c
    """
    SEQ_FIELDS = ["num_entries", "entries"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Nb0, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['num_entries']['start'] = self._io.pos()
        self.num_entries = self._io.read_u4le()
        self._debug['num_entries']['end'] = self._io.pos()
        if not self.num_entries >= 1:
            raise kaitaistruct.ValidationLessThanError(1, self.num_entries, self._io, u"/seq/0")
        if not self.num_entries <= self._root._io.size() // 64:
            raise kaitaistruct.ValidationGreaterThanError(self._root._io.size() // 64, self.num_entries, self._io, u"/seq/0")
        self._debug['entries']['start'] = self._io.pos()
        self._debug['entries']['arr'] = []
        self._raw_entries = []
        self.entries = []
        i = 0
        while True:
            self._debug['entries']['arr'].append({'start': self._io.pos()})
            _buf = self._io.read_bytes(64)
            self._raw_entries.append(_buf)
            _io__raw_entries = KaitaiStream(BytesIO(self._raw_entries[-1]))
            _ = Nb0.Entry(_io__raw_entries, self, self._root)
            self.entries.append(_)
            self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
            if i == self.num_entries - 1:
                break
            i += 1
        self._debug['entries']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.entries)):
            pass
            self.entries[i]._fetch_instances()

        _ = self.partitions
        if hasattr(self, '_m_partitions'):
            pass
            for i in range(len(self._m_partitions)):
                pass
                self._m_partitions[i]._fetch_instances()



    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["ofs_partition", "len_partition", "unknown1", "unknown2", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Nb0.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_partition']['start'] = self._io.pos()
            self.ofs_partition = self._io.read_u4le()
            self._debug['ofs_partition']['end'] = self._io.pos()
            self._debug['len_partition']['start'] = self._io.pos()
            self.len_partition = self._io.read_u4le()
            self._debug['len_partition']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_u4le()
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_u4le()
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(48), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PartitionType(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, i, _io, _parent=None, _root=None):
            super(Nb0.PartitionType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.i = i
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.body
            if hasattr(self, '_m_body'):
                pass


        @property
        def body(self):
            if hasattr(self, '_m_body'):
                return self._m_body

            _pos = self._io.pos()
            self._io.seek((self._root.entries[self.i].ofs_partition + self._root.num_entries * 64) + 4)
            self._debug['_m_body']['start'] = self._io.pos()
            self._m_body = self._io.read_bytes(self._root.entries[self.i].len_partition)
            self._debug['_m_body']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_body', None)


    @property
    def partitions(self):
        if hasattr(self, '_m_partitions'):
            return self._m_partitions

        self._debug['_m_partitions']['start'] = self._io.pos()
        self._debug['_m_partitions']['arr'] = []
        self._m_partitions = []
        for i in range(self.num_entries):
            self._debug['_m_partitions']['arr'].append({'start': self._io.pos()})
            self._m_partitions.append(Nb0.PartitionType(i, self._io, self, self._root))
            self._debug['_m_partitions']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_partitions']['end'] = self._io.pos()
        return getattr(self, '_m_partitions', None)


