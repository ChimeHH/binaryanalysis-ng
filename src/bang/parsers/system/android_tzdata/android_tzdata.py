# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import tzif
from .tzif import *
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class AndroidTzdata(KaitaiStruct):
    """
    .. seealso::
       Source - https://android.googlesource.com/platform/bionic/+/lollipop-mr1-dev/libc/tools/zoneinfo/ZoneCompactor.java
    """
    SEQ_FIELDS = ["signature", "year", "release", "ofs_index", "ofs_data", "ofs_zonetab"]
    def __init__(self, _io, _parent=None, _root=None):
        super(AndroidTzdata, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['signature']['start'] = self._io.pos()
        self.signature = self._io.read_bytes(6)
        self._debug['signature']['end'] = self._io.pos()
        if not self.signature == b"\x74\x7A\x64\x61\x74\x61":
            raise kaitaistruct.ValidationNotEqualError(b"\x74\x7A\x64\x61\x74\x61", self.signature, self._io, u"/seq/0")
        self._debug['year']['start'] = self._io.pos()
        self.year = (self._io.read_bytes(4)).decode(u"UTF-8")
        self._debug['year']['end'] = self._io.pos()
        self._debug['release']['start'] = self._io.pos()
        self.release = (KaitaiStream.bytes_terminate(self._io.read_bytes(2), 0, False)).decode(u"UTF-8")
        self._debug['release']['end'] = self._io.pos()
        self._debug['ofs_index']['start'] = self._io.pos()
        self.ofs_index = self._io.read_u4be()
        self._debug['ofs_index']['end'] = self._io.pos()
        self._debug['ofs_data']['start'] = self._io.pos()
        self.ofs_data = self._io.read_u4be()
        self._debug['ofs_data']['end'] = self._io.pos()
        self._debug['ofs_zonetab']['start'] = self._io.pos()
        self.ofs_zonetab = self._io.read_u4be()
        self._debug['ofs_zonetab']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _ = self.index
        if hasattr(self, '_m_index'):
            pass
            self._m_index._fetch_instances()

        _ = self.zonetab
        if hasattr(self, '_m_zonetab'):
            pass
            self._m_zonetab._fetch_instances()


    class Entries(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidTzdata.Entries, self).__init__(_io)
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
                self.entries.append(AndroidTzdata.Entry(self._io, self, self._root))
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["zonename", "ofs_timezone", "len_timezone", "raw_gmt_offset"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidTzdata.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['zonename']['start'] = self._io.pos()
            self.zonename = (KaitaiStream.bytes_terminate(self._io.read_bytes(40), 0, False)).decode(u"UTF-8")
            self._debug['zonename']['end'] = self._io.pos()
            self._debug['ofs_timezone']['start'] = self._io.pos()
            self.ofs_timezone = self._io.read_u4be()
            self._debug['ofs_timezone']['end'] = self._io.pos()
            self._debug['len_timezone']['start'] = self._io.pos()
            self.len_timezone = self._io.read_u4be()
            self._debug['len_timezone']['end'] = self._io.pos()
            self._debug['raw_gmt_offset']['start'] = self._io.pos()
            self.raw_gmt_offset = self._io.read_u4be()
            self._debug['raw_gmt_offset']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.raw_tzif
            if hasattr(self, '_m_raw_tzif'):
                pass

            _ = self.tzif
            if hasattr(self, '_m_tzif'):
                pass
                self._m_tzif._fetch_instances()


        @property
        def raw_tzif(self):
            if hasattr(self, '_m_raw_tzif'):
                return self._m_raw_tzif

            io = self._root._io
            _pos = io.pos()
            io.seek(self._root.ofs_data + self.ofs_timezone)
            self._debug['_m_raw_tzif']['start'] = io.pos()
            self._m_raw_tzif = io.read_bytes(self.len_timezone)
            self._debug['_m_raw_tzif']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_raw_tzif', None)

        @property
        def tzif(self):
            if hasattr(self, '_m_tzif'):
                return self._m_tzif

            io = self._root._io
            _pos = io.pos()
            io.seek(self._root.ofs_data + self.ofs_timezone)
            self._debug['_m_tzif']['start'] = io.pos()
            self._raw__m_tzif = io.read_bytes(self.len_timezone)
            _io__raw__m_tzif = KaitaiStream(BytesIO(self._raw__m_tzif))
            self._m_tzif = tzif.Tzif(_io__raw__m_tzif)
            self._debug['_m_tzif']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_tzif', None)


    class Zonetab(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidTzdata.Zonetab, self).__init__(_io)
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
                self.entries.append((self._io.read_bytes_term(10, False, True, True)).decode(u"UTF-8"))
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass



    @property
    def index(self):
        if hasattr(self, '_m_index'):
            return self._m_index

        _pos = self._io.pos()
        self._io.seek(self.ofs_index)
        self._debug['_m_index']['start'] = self._io.pos()
        self._raw__m_index = self._io.read_bytes(self.len_index)
        _io__raw__m_index = KaitaiStream(BytesIO(self._raw__m_index))
        self._m_index = AndroidTzdata.Entries(_io__raw__m_index, self, self._root)
        self._debug['_m_index']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_index', None)

    @property
    def len_index(self):
        if hasattr(self, '_m_len_index'):
            return self._m_len_index

        self._m_len_index = (self.ofs_data - self.ofs_index if self.ofs_data < self.ofs_zonetab else self.ofs_zonetab - self.ofs_index)
        return getattr(self, '_m_len_index', None)

    @property
    def zonetab(self):
        if hasattr(self, '_m_zonetab'):
            return self._m_zonetab

        _pos = self._io.pos()
        self._io.seek(self.ofs_zonetab)
        self._debug['_m_zonetab']['start'] = self._io.pos()
        self._raw__m_zonetab = self._io.read_bytes_full()
        _io__raw__m_zonetab = KaitaiStream(BytesIO(self._raw__m_zonetab))
        self._m_zonetab = AndroidTzdata.Zonetab(_io__raw__m_zonetab, self, self._root)
        self._debug['_m_zonetab']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_zonetab', None)


