# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Acdb(KaitaiStruct):
    """Label audio calibration database files from Qualcomm.
    This specification is based on a few samples found inside the
    firmware of several Android devices using a Qualcomm chipset and
    very incomplete as it is a proprietary format.
    """
    SEQ_FIELDS = ["header", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Acdb, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(32)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Acdb.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self._raw_data = self._io.read_bytes(self.header.filesize1)
        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
        self.data = Acdb.Data(_io__raw_data, self, self._root)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.data._fetch_instances()

    class Data(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Acdb.Data, self).__init__(_io)
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
                self.entries.append(Acdb.Entry(self._io, self, self._root))
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["name", "len_data", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Acdb.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(8)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "reserved1", "name", "reserved2", "filesize1", "filesize2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Acdb.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x51\x43\x4D\x53\x4E\x44\x44\x42":
                raise kaitaistruct.ValidationNotEqualError(b"\x51\x43\x4D\x53\x4E\x44\x44\x42", self.magic, self._io, u"/types/header/seq/0")
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bytes(8)
            self._debug['reserved1']['end'] = self._io.pos()
            if not self.reserved1 == b"\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00", self.reserved1, self._io, u"/types/header/seq/1")
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(4)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            if not  ((self.name == u"AMDB") or (self.name == u"AVDB") or (self.name == u"CCDB") or (self.name == u"GCDB")) :
                raise kaitaistruct.ValidationNotAnyOfError(self.name, self._io, u"/types/header/seq/2")
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bytes(4)
            self._debug['reserved2']['end'] = self._io.pos()
            if not self.reserved2 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.reserved2, self._io, u"/types/header/seq/3")
            self._debug['filesize1']['start'] = self._io.pos()
            self.filesize1 = self._io.read_u4le()
            self._debug['filesize1']['end'] = self._io.pos()
            self._debug['filesize2']['start'] = self._io.pos()
            self.filesize2 = self._io.read_u4le()
            self._debug['filesize2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



