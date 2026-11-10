# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class RomfsAmbarella(KaitaiStruct):
    """Test files: <http://dc.p-mc.eu/0803/firmware>
    
    .. seealso::
       (section 4.1) - http://web.archive.org/web/20190402224117/https://courses.cs.ut.ee/MTAT.07.022/2015_spring/uploads/Main/karl-report-s15.pdf
    """
    SEQ_FIELDS = ["num_files", "magic", "padding", "file_headers"]
    def __init__(self, _io, _parent=None, _root=None):
        super(RomfsAmbarella, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['num_files']['start'] = self._io.pos()
        self.num_files = self._io.read_u4le()
        self._debug['num_files']['end'] = self._io.pos()
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x8A\x32\xFC\x66":
            raise kaitaistruct.ValidationNotEqualError(b"\x8A\x32\xFC\x66", self.magic, self._io, u"/seq/1")
        self._debug['padding']['start'] = self._io.pos()
        self._debug['padding']['arr'] = []
        self.padding = []
        for i in range(2040):
            self._debug['padding']['arr'].append({'start': self._io.pos()})
            self.padding.append(RomfsAmbarella.PaddingByte(self._io, self, self._root))
            self._debug['padding']['arr'][i]['end'] = self._io.pos()

        self._debug['padding']['end'] = self._io.pos()
        self._debug['file_headers']['start'] = self._io.pos()
        self._debug['file_headers']['arr'] = []
        self.file_headers = []
        for i in range(self.num_files):
            self._debug['file_headers']['arr'].append({'start': self._io.pos()})
            self.file_headers.append(RomfsAmbarella.FileHeader(self._io, self, self._root))
            self._debug['file_headers']['arr'][i]['end'] = self._io.pos()

        self._debug['file_headers']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.padding)):
            pass
            self.padding[i]._fetch_instances()

        for i in range(len(self.file_headers)):
            pass
            self.file_headers[i]._fetch_instances()


    class FileHeader(KaitaiStruct):
        SEQ_FIELDS = ["name", "ofs_data", "len_data", "magic"]
        def __init__(self, _io, _parent=None, _root=None):
            super(RomfsAmbarella.FileHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(116), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['ofs_data']['start'] = self._io.pos()
            self.ofs_data = self._io.read_u4le()
            self._debug['ofs_data']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x76\xAB\x87\x23":
                raise kaitaistruct.ValidationNotEqualError(b"\x76\xAB\x87\x23", self.magic, self._io, u"/types/file_header/seq/3")


        def _fetch_instances(self):
            pass
            _ = self.data
            if hasattr(self, '_m_data'):
                pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            _pos = self._io.pos()
            self._io.seek(self.ofs_data)
            self._debug['_m_data']['start'] = self._io.pos()
            self._m_data = self._io.read_bytes(self.len_data)
            self._debug['_m_data']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_data', None)


    class PaddingByte(KaitaiStruct):
        SEQ_FIELDS = ["padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(RomfsAmbarella.PaddingByte, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(1)
            self._debug['padding']['end'] = self._io.pos()
            if not self.padding == b"\xFF":
                raise kaitaistruct.ValidationNotEqualError(b"\xFF", self.padding, self._io, u"/types/padding_byte/seq/0")


        def _fetch_instances(self):
            pass



