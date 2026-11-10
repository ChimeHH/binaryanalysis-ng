# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Rkboot(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/rockchip-linux/rkdeveloptool/blob/master/RKBoot.h#L7
    
    
    .. seealso::
       Source - https://github.com/rockchip-linux/rkdeveloptool/blob/master/RKBoot.cpp#L212
    
    
    .. seealso::
       Source - https://github.com/rockchip-linux/rkdeveloptool/blob/master/boot_merger.h#L122
    """

    class Rkdevice(IntEnum):
        none = 0
        rksmart = 842412611
        rkcayman = 842478401
        rk281x = 842543448
        rkpanda = 842543682
        rk29 = 842608728
        rk292x = 842609240
        rk30 = 858796097
        rk30b = 858861633
        rk31 = 858861634
        rk32 = 858927169
        rkcrown = 1313821251
        rk27 = 1380659767
        rk28 = 1380659768
        rknano = 1851879023
    SEQ_FIELDS = ["magic", "size", "header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Rkboot, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x42\x4F\x4F\x54":
            raise kaitaistruct.ValidationNotEqualError(b"\x42\x4F\x4F\x54", self.magic, self._io, u"/seq/0")
        self._debug['size']['start'] = self._io.pos()
        self.size = self._io.read_u2le()
        self._debug['size']['end'] = self._io.pos()
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes((self.size - 4) - 2)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Rkboot.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        _ = self.crc
        if hasattr(self, '_m_crc'):
            pass

        _ = self.entries_471
        if hasattr(self, '_m_entries_471'):
            pass
            for i in range(len(self._m_entries_471)):
                pass
                self._m_entries_471[i]._fetch_instances()


        _ = self.entries_472
        if hasattr(self, '_m_entries_472'):
            pass
            for i in range(len(self._m_entries_472)):
                pass
                self._m_entries_472[i]._fetch_instances()


        _ = self.entries_loader
        if hasattr(self, '_m_entries_loader'):
            pass
            for i in range(len(self._m_entries_loader)):
                pass
                self._m_entries_loader[i]._fetch_instances()



    class Header(KaitaiStruct):
        SEQ_FIELDS = ["version", "merge_version", "release_time", "supported_chip", "num_entries_471", "ofs_entries_471", "len_entry_471", "num_entries_472", "ofs_entries_472", "len_entry_472", "num_entries_loader", "ofs_entries_loader", "len_entry_loader", "flags", "rc4_flags", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Rkboot.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['merge_version']['start'] = self._io.pos()
            self.merge_version = self._io.read_u4le()
            self._debug['merge_version']['end'] = self._io.pos()
            self._debug['release_time']['start'] = self._io.pos()
            self.release_time = Rkboot.Rktime(self._io, self, self._root)
            self._debug['release_time']['end'] = self._io.pos()
            self._debug['supported_chip']['start'] = self._io.pos()
            self.supported_chip = KaitaiStream.resolve_enum(Rkboot.Rkdevice, self._io.read_u4le())
            self._debug['supported_chip']['end'] = self._io.pos()
            self._debug['num_entries_471']['start'] = self._io.pos()
            self.num_entries_471 = self._io.read_u1()
            self._debug['num_entries_471']['end'] = self._io.pos()
            self._debug['ofs_entries_471']['start'] = self._io.pos()
            self.ofs_entries_471 = self._io.read_u4le()
            self._debug['ofs_entries_471']['end'] = self._io.pos()
            self._debug['len_entry_471']['start'] = self._io.pos()
            self.len_entry_471 = self._io.read_u1()
            self._debug['len_entry_471']['end'] = self._io.pos()
            self._debug['num_entries_472']['start'] = self._io.pos()
            self.num_entries_472 = self._io.read_u1()
            self._debug['num_entries_472']['end'] = self._io.pos()
            self._debug['ofs_entries_472']['start'] = self._io.pos()
            self.ofs_entries_472 = self._io.read_u4le()
            self._debug['ofs_entries_472']['end'] = self._io.pos()
            self._debug['len_entry_472']['start'] = self._io.pos()
            self.len_entry_472 = self._io.read_u1()
            self._debug['len_entry_472']['end'] = self._io.pos()
            self._debug['num_entries_loader']['start'] = self._io.pos()
            self.num_entries_loader = self._io.read_u1()
            self._debug['num_entries_loader']['end'] = self._io.pos()
            self._debug['ofs_entries_loader']['start'] = self._io.pos()
            self.ofs_entries_loader = self._io.read_u4le()
            self._debug['ofs_entries_loader']['end'] = self._io.pos()
            self._debug['len_entry_loader']['start'] = self._io.pos()
            self.len_entry_loader = self._io.read_u1()
            self._debug['len_entry_loader']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['rc4_flags']['start'] = self._io.pos()
            self.rc4_flags = self._io.read_u1()
            self._debug['rc4_flags']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(57)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.release_time._fetch_instances()


    class RkEntry(KaitaiStruct):
        SEQ_FIELDS = ["size", "entry_type", "name", "ofs_data", "len_data", "data_delay"]
        def __init__(self, valid_version, _io, _parent=None, _root=None):
            super(Rkboot.RkEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.valid_version = valid_version
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u1()
            self._debug['size']['end'] = self._io.pos()
            self._debug['entry_type']['start'] = self._io.pos()
            self.entry_type = self._io.read_u4le()
            self._debug['entry_type']['end'] = self._io.pos()
            if not self.entry_type == self.valid_version:
                raise kaitaistruct.ValidationNotEqualError(self.valid_version, self.entry_type, self._io, u"/types/rk_entry/seq/1")
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(40)).decode(u"UTF-16LE")
            self._debug['name']['end'] = self._io.pos()
            self._debug['ofs_data']['start'] = self._io.pos()
            self.ofs_data = self._io.read_u4le()
            self._debug['ofs_data']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['data_delay']['start'] = self._io.pos()
            self.data_delay = self._io.read_u4le()
            self._debug['data_delay']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.data
            if hasattr(self, '_m_data'):
                pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_data)
            self._debug['_m_data']['start'] = io.pos()
            self._m_data = io.read_bytes(self.len_data)
            self._debug['_m_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_data', None)


    class Rktime(KaitaiStruct):
        SEQ_FIELDS = ["year", "month", "day", "hour", "minute", "second"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Rkboot.Rktime, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['year']['start'] = self._io.pos()
            self.year = self._io.read_u2le()
            self._debug['year']['end'] = self._io.pos()
            self._debug['month']['start'] = self._io.pos()
            self.month = self._io.read_u1()
            self._debug['month']['end'] = self._io.pos()
            self._debug['day']['start'] = self._io.pos()
            self.day = self._io.read_u1()
            self._debug['day']['end'] = self._io.pos()
            self._debug['hour']['start'] = self._io.pos()
            self.hour = self._io.read_u1()
            self._debug['hour']['end'] = self._io.pos()
            self._debug['minute']['start'] = self._io.pos()
            self.minute = self._io.read_u1()
            self._debug['minute']['end'] = self._io.pos()
            self._debug['second']['start'] = self._io.pos()
            self.second = self._io.read_u1()
            self._debug['second']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def crc(self):
        if hasattr(self, '_m_crc'):
            return self._m_crc

        _pos = self._io.pos()
        self._io.seek(self.entries_loader[-1].ofs_data + self.entries_loader[-1].len_data)
        self._debug['_m_crc']['start'] = self._io.pos()
        self._m_crc = self._io.read_bytes(4)
        self._debug['_m_crc']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_crc', None)

    @property
    def entries_471(self):
        if hasattr(self, '_m_entries_471'):
            return self._m_entries_471

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_entries_471)
        self._debug['_m_entries_471']['start'] = self._io.pos()
        self._debug['_m_entries_471']['arr'] = []
        self._raw__m_entries_471 = []
        self._m_entries_471 = []
        for i in range(self.header.num_entries_471):
            self._debug['_m_entries_471']['arr'].append({'start': self._io.pos()})
            self._raw__m_entries_471.append(self._io.read_bytes(self.header.len_entry_471))
            _io__raw__m_entries_471 = KaitaiStream(BytesIO(self._raw__m_entries_471[i]))
            self._m_entries_471.append(Rkboot.RkEntry(1, _io__raw__m_entries_471, self, self._root))
            self._debug['_m_entries_471']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_entries_471']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_entries_471', None)

    @property
    def entries_472(self):
        if hasattr(self, '_m_entries_472'):
            return self._m_entries_472

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_entries_472)
        self._debug['_m_entries_472']['start'] = self._io.pos()
        self._debug['_m_entries_472']['arr'] = []
        self._raw__m_entries_472 = []
        self._m_entries_472 = []
        for i in range(self.header.num_entries_472):
            self._debug['_m_entries_472']['arr'].append({'start': self._io.pos()})
            self._raw__m_entries_472.append(self._io.read_bytes(self.header.len_entry_472))
            _io__raw__m_entries_472 = KaitaiStream(BytesIO(self._raw__m_entries_472[i]))
            self._m_entries_472.append(Rkboot.RkEntry(2, _io__raw__m_entries_472, self, self._root))
            self._debug['_m_entries_472']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_entries_472']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_entries_472', None)

    @property
    def entries_loader(self):
        if hasattr(self, '_m_entries_loader'):
            return self._m_entries_loader

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_entries_loader)
        self._debug['_m_entries_loader']['start'] = self._io.pos()
        self._debug['_m_entries_loader']['arr'] = []
        self._raw__m_entries_loader = []
        self._m_entries_loader = []
        for i in range(self.header.num_entries_loader):
            self._debug['_m_entries_loader']['arr'].append({'start': self._io.pos()})
            self._raw__m_entries_loader.append(self._io.read_bytes(self.header.len_entry_loader))
            _io__raw__m_entries_loader = KaitaiStream(BytesIO(self._raw__m_entries_loader[i]))
            self._m_entries_loader.append(Rkboot.RkEntry(4, _io__raw__m_entries_loader, self, self._root))
            self._debug['_m_entries_loader']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_entries_loader']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_entries_loader', None)


