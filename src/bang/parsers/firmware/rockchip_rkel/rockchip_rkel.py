# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class RockchipRkel(KaitaiStruct):
    """Image format found in devices with the Rockchip RK3566, such as the PineNote
    <https://wiki.pine64.org/wiki/PineNote>
    
    Example files:
    
    <https://github.com/BPI-SINOVOIP/BPI-Rockchip-Android11/tree/master/device/rockchip/rk356x/rk3566_eink/ota>
    """
    SEQ_FIELDS = ["header", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(RockchipRkel, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(64)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = RockchipRkel.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self._raw_data = self._io.read_bytes(self.header.len_data - 64)
        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
        self.data = RockchipRkel.Images(self.header.num_images, _io__raw_data, self, self._root)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.data._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_data", "height", "width", "num_images", "version"]
        def __init__(self, _io, _parent=None, _root=None):
            super(RockchipRkel.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x52\x4B\x45\x4C":
                raise kaitaistruct.ValidationNotEqualError(b"\x52\x4B\x45\x4C", self.magic, self._io, u"/types/header/seq/0")
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u4le()
            self._debug['height']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u4le()
            self._debug['width']['end'] = self._io.pos()
            self._debug['num_images']['start'] = self._io.pos()
            self.num_images = self._io.read_u4le()
            self._debug['num_images']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = (KaitaiStream.bytes_terminate(self._io.read_bytes_full(), 0, False)).decode(u"UTF-8")
            self._debug['version']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class ImageEntry(KaitaiStruct):
        SEQ_FIELDS = ["signature", "unknown_1", "height", "width", "unknown_2", "ofs_image_data", "len_image_data", "unknown_3"]
        def __init__(self, _io, _parent=None, _root=None):
            super(RockchipRkel.ImageEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(4)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x47\x52\x30\x34":
                raise kaitaistruct.ValidationNotEqualError(b"\x47\x52\x30\x34", self.signature, self._io, u"/types/image_entry/seq/0")
            self._debug['unknown_1']['start'] = self._io.pos()
            self.unknown_1 = self._io.read_u4le()
            self._debug['unknown_1']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u2le()
            self._debug['height']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u2le()
            self._debug['width']['end'] = self._io.pos()
            self._debug['unknown_2']['start'] = self._io.pos()
            self.unknown_2 = self._io.read_u4le()
            self._debug['unknown_2']['end'] = self._io.pos()
            self._debug['ofs_image_data']['start'] = self._io.pos()
            self.ofs_image_data = self._io.read_u4le()
            self._debug['ofs_image_data']['end'] = self._io.pos()
            self._debug['len_image_data']['start'] = self._io.pos()
            self.len_image_data = self._io.read_u4le()
            self._debug['len_image_data']['end'] = self._io.pos()
            self._debug['unknown_3']['start'] = self._io.pos()
            self.unknown_3 = self._io.read_bytes(8)
            self._debug['unknown_3']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.image_data
            if hasattr(self, '_m_image_data'):
                pass


        @property
        def image_data(self):
            if hasattr(self, '_m_image_data'):
                return self._m_image_data

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_image_data)
            self._debug['_m_image_data']['start'] = io.pos()
            self._m_image_data = io.read_bytes(self.len_image_data)
            self._debug['_m_image_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_image_data', None)


    class Images(KaitaiStruct):
        SEQ_FIELDS = ["image_entries"]
        def __init__(self, num_images, _io, _parent=None, _root=None):
            super(RockchipRkel.Images, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_images = num_images
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['image_entries']['start'] = self._io.pos()
            self._debug['image_entries']['arr'] = []
            self._raw_image_entries = []
            self.image_entries = []
            for i in range(self.num_images):
                self._debug['image_entries']['arr'].append({'start': self._io.pos()})
                self._raw_image_entries.append(self._io.read_bytes(32))
                _io__raw_image_entries = KaitaiStream(BytesIO(self._raw_image_entries[i]))
                self.image_entries.append(RockchipRkel.ImageEntry(_io__raw_image_entries, self, self._root))
                self._debug['image_entries']['arr'][i]['end'] = self._io.pos()

            self._debug['image_entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.image_entries)):
                pass
                self.image_entries[i]._fetch_instances()




