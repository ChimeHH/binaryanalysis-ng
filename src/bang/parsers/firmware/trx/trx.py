# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Trx(KaitaiStruct):
    """
    .. seealso::
       Source - https://web.archive.org/web/20190127154419/https://openwrt.org/docs/techref/header
    """
    SEQ_FIELDS = ["preheader", "header_and_data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Trx, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['preheader']['start'] = self._io.pos()
        self.preheader = Trx.Preheader(self._io, self, self._root)
        self._debug['preheader']['end'] = self._io.pos()
        self._debug['header_and_data']['start'] = self._io.pos()
        self._raw_header_and_data = self._io.read_bytes(self.preheader.len_trx - 12)
        _io__raw_header_and_data = KaitaiStream(BytesIO(self._raw_header_and_data))
        self.header_and_data = Trx.HeaderAndData(_io__raw_header_and_data, self, self._root)
        self._debug['header_and_data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.preheader._fetch_instances()
        self.header_and_data._fetch_instances()
        _ = self.raw_data
        if hasattr(self, '_m_raw_data'):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["flags", "version", "ofs_partition0", "ofs_partition1", "ofs_partition2", "offset_partition3"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Trx.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u2le()
            self._debug['version']['end'] = self._io.pos()
            if not  ((self.version == 1) or (self.version == 2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/types/header/seq/1")
            self._debug['ofs_partition0']['start'] = self._io.pos()
            self.ofs_partition0 = self._io.read_u4le()
            self._debug['ofs_partition0']['end'] = self._io.pos()
            _ = self.ofs_partition0
            if not  ((_ == 0) or (_ >= self.len_header)) :
                raise kaitaistruct.ValidationExprError(self.ofs_partition0, self._io, u"/types/header/seq/2")
            self._debug['ofs_partition1']['start'] = self._io.pos()
            self.ofs_partition1 = self._io.read_u4le()
            self._debug['ofs_partition1']['end'] = self._io.pos()
            _ = self.ofs_partition1
            if not  ((_ == 0) or ( ((_ >= self.len_header) and (_ >= self.ofs_partition0)) )) :
                raise kaitaistruct.ValidationExprError(self.ofs_partition1, self._io, u"/types/header/seq/3")
            self._debug['ofs_partition2']['start'] = self._io.pos()
            self.ofs_partition2 = self._io.read_u4le()
            self._debug['ofs_partition2']['end'] = self._io.pos()
            _ = self.ofs_partition2
            if not  ((_ == 0) or ( ((_ >= self.len_header) and (_ >= self.ofs_partition1)) )) :
                raise kaitaistruct.ValidationExprError(self.ofs_partition2, self._io, u"/types/header/seq/4")
            if self.version > 1:
                pass
                self._debug['offset_partition3']['start'] = self._io.pos()
                self.offset_partition3 = self._io.read_u4le()
                self._debug['offset_partition3']['end'] = self._io.pos()
                _ = self.offset_partition3
                if not  ((_ == 0) or ( ((_ >= self.len_header) and (_ >= self.ofs_partition2)) )) :
                    raise kaitaistruct.ValidationExprError(self.offset_partition3, self._io, u"/types/header/seq/5")



        def _fetch_instances(self):
            pass
            if self.version > 1:
                pass

            _ = self.partition0
            if hasattr(self, '_m_partition0'):
                pass

            _ = self.partition1
            if hasattr(self, '_m_partition1'):
                pass

            _ = self.partition2
            if hasattr(self, '_m_partition2'):
                pass

            _ = self.partition3
            if hasattr(self, '_m_partition3'):
                pass


        @property
        def len_header(self):
            if hasattr(self, '_m_len_header'):
                return self._m_len_header

            self._m_len_header = (28 if self.version == 1 else 32)
            return getattr(self, '_m_len_header', None)

        @property
        def ofs_partition3(self):
            if hasattr(self, '_m_ofs_partition3'):
                return self._m_ofs_partition3

            self._m_ofs_partition3 = (self.offset_partition3 if self.version > 1 else 0)
            return getattr(self, '_m_ofs_partition3', None)

        @property
        def partition0(self):
            if hasattr(self, '_m_partition0'):
                return self._m_partition0

            if self.ofs_partition0 != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_partition0)
                self._debug['_m_partition0']['start'] = io.pos()
                self._m_partition0 = io.read_bytes((self._root.preheader.len_trx - self.ofs_partition0 if self.ofs_partition1 == 0 else self.ofs_partition1 - self.ofs_partition0))
                self._debug['_m_partition0']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_partition0', None)

        @property
        def partition1(self):
            if hasattr(self, '_m_partition1'):
                return self._m_partition1

            if self.ofs_partition1 != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_partition1)
                self._debug['_m_partition1']['start'] = io.pos()
                self._m_partition1 = io.read_bytes((self._root.preheader.len_trx - self.ofs_partition1 if self.ofs_partition2 == 0 else self.ofs_partition2 - self.ofs_partition1))
                self._debug['_m_partition1']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_partition1', None)

        @property
        def partition2(self):
            if hasattr(self, '_m_partition2'):
                return self._m_partition2

            if self.ofs_partition2 != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_partition2)
                self._debug['_m_partition2']['start'] = io.pos()
                self._m_partition2 = io.read_bytes((self._root.preheader.len_trx - self.ofs_partition2 if self.ofs_partition3 == 0 else self.ofs_partition3 - self.ofs_partition2))
                self._debug['_m_partition2']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_partition2', None)

        @property
        def partition3(self):
            if hasattr(self, '_m_partition3'):
                return self._m_partition3

            if  ((self.version > 1) and (self.ofs_partition3 != 0)) :
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_partition3)
                self._debug['_m_partition3']['start'] = io.pos()
                self._m_partition3 = io.read_bytes(self._root.preheader.len_trx - self.ofs_partition3)
                self._debug['_m_partition3']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_partition3', None)


    class HeaderAndData(KaitaiStruct):
        SEQ_FIELDS = ["header", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Trx.HeaderAndData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Trx.Header(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes_full()
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()


    class Preheader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_trx", "crc32"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Trx.Preheader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x48\x44\x52\x30":
                raise kaitaistruct.ValidationNotEqualError(b"\x48\x44\x52\x30", self.magic, self._io, u"/types/preheader/seq/0")
            self._debug['len_trx']['start'] = self._io.pos()
            self.len_trx = self._io.read_u4le()
            self._debug['len_trx']['end'] = self._io.pos()
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def raw_data(self):
        if hasattr(self, '_m_raw_data'):
            return self._m_raw_data

        _pos = self._io.pos()
        self._io.seek(12)
        self._debug['_m_raw_data']['start'] = self._io.pos()
        self._m_raw_data = self._io.read_bytes(self.preheader.len_trx - 12)
        self._debug['_m_raw_data']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_raw_data', None)


