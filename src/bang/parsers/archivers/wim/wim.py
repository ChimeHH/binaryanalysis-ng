# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Wim(KaitaiStruct):
    SEQ_FIELDS = ["preheader", "header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Wim, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['preheader']['start'] = self._io.pos()
        self.preheader = Wim.Preheader(self._io, self, self._root)
        self._debug['preheader']['end'] = self._io.pos()
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(self.preheader.len_header - 12)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Wim.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.preheader._fetch_instances()
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["version", "flags", "len_data", "guid", "part_number", "total_parts", "image_count", "ofs_table", "xml_metadata", "boot_metadata", "boot_index", "integrity", "unused"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Wim.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['guid']['start'] = self._io.pos()
            self.guid = self._io.read_bytes(16)
            self._debug['guid']['end'] = self._io.pos()
            self._debug['part_number']['start'] = self._io.pos()
            self.part_number = self._io.read_u2le()
            self._debug['part_number']['end'] = self._io.pos()
            self._debug['total_parts']['start'] = self._io.pos()
            self.total_parts = self._io.read_u2le()
            self._debug['total_parts']['end'] = self._io.pos()
            self._debug['image_count']['start'] = self._io.pos()
            self.image_count = self._io.read_u4le()
            self._debug['image_count']['end'] = self._io.pos()
            self._debug['ofs_table']['start'] = self._io.pos()
            self.ofs_table = Wim.ReshdrDiskShort(self._io, self, self._root)
            self._debug['ofs_table']['end'] = self._io.pos()
            self._debug['xml_metadata']['start'] = self._io.pos()
            self.xml_metadata = Wim.ReshdrDiskShort(self._io, self, self._root)
            self._debug['xml_metadata']['end'] = self._io.pos()
            self._debug['boot_metadata']['start'] = self._io.pos()
            self.boot_metadata = Wim.ReshdrDiskShort(self._io, self, self._root)
            self._debug['boot_metadata']['end'] = self._io.pos()
            self._debug['boot_index']['start'] = self._io.pos()
            self.boot_index = self._io.read_u4le()
            self._debug['boot_index']['end'] = self._io.pos()
            self._debug['integrity']['start'] = self._io.pos()
            self.integrity = Wim.ReshdrDiskShort(self._io, self, self._root)
            self._debug['integrity']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_bytes(60)
            self._debug['unused']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.ofs_table._fetch_instances()
            self.xml_metadata._fetch_instances()
            self.boot_metadata._fetch_instances()
            self.integrity._fetch_instances()
            _ = self.xml
            if hasattr(self, '_m_xml'):
                pass


        @property
        def xml(self):
            if hasattr(self, '_m_xml'):
                return self._m_xml

            io = self._root._io
            _pos = io.pos()
            io.seek(self.xml_metadata.offset)
            self._debug['_m_xml']['start'] = io.pos()
            self._m_xml = io.read_bytes(self.xml_metadata.size)
            self._debug['_m_xml']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_xml', None)


    class Preheader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Wim.Preheader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x4D\x53\x57\x49\x4D\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x4D\x53\x57\x49\x4D\x00\x00\x00", self.magic, self._io, u"/types/preheader/seq/0")
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            if not self.len_header >= 208:
                raise kaitaistruct.ValidationLessThanError(208, self.len_header, self._io, u"/types/preheader/seq/1")


        def _fetch_instances(self):
            pass


    class ReshdrDiskShort(KaitaiStruct):
        SEQ_FIELDS = ["size_and_flags", "offset", "uncompressed_size"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Wim.ReshdrDiskShort, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size_and_flags']['start'] = self._io.pos()
            self.size_and_flags = self._io.read_u8le()
            self._debug['size_and_flags']['end'] = self._io.pos()
            self._debug['offset']['start'] = self._io.pos()
            self.offset = self._io.read_u8le()
            self._debug['offset']['end'] = self._io.pos()
            self._debug['uncompressed_size']['start'] = self._io.pos()
            self.uncompressed_size = self._io.read_u8le()
            self._debug['uncompressed_size']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def flags(self):
            if hasattr(self, '_m_flags'):
                return self._m_flags

            self._m_flags = self.size_and_flags >> 56
            return getattr(self, '_m_flags', None)

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = self.size_and_flags & 72057594037927935
            return getattr(self, '_m_size', None)



