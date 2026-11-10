# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class AndroidImgdata(KaitaiStruct):
    """
    .. seealso::
       https://gist.github.com/shinyquagsire23/ba0f6209592d50fb8e4166620228aaa5 - https://github.com/NVISOsecurity/nexus_5_bootloader_unpacker/blob/master/imgdata_tool.c
    """
    SEQ_FIELDS = ["header", "images"]
    def __init__(self, _io, _parent=None, _root=None):
        super(AndroidImgdata, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = AndroidImgdata.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['images']['start'] = self._io.pos()
        self._debug['images']['arr'] = []
        self.images = []
        for i in range(self.header.num_files):
            self._debug['images']['arr'].append({'start': self._io.pos()})
            self.images.append(AndroidImgdata.Image(self._io, self, self._root))
            self._debug['images']['arr'][i]['end'] = self._io.pos()

        self._debug['images']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.images)):
            pass
            self.images[i]._fetch_instances()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "unknown", "num_files", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidImgdata.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x49\x4D\x47\x44\x41\x54\x41\x21":
                raise kaitaistruct.ValidationNotEqualError(b"\x49\x4D\x47\x44\x41\x54\x41\x21", self.magic, self._io, u"/types/header/seq/0")
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_u4le()
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u4le()
            self._debug['num_files']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(8)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Image(KaitaiStruct):
        SEQ_FIELDS = ["name", "image_width", "image_height", "screen_x_position", "screen_y_position", "ofs_image", "len_image"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidImgdata.Image, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['image_width']['start'] = self._io.pos()
            self.image_width = self._io.read_u4le()
            self._debug['image_width']['end'] = self._io.pos()
            self._debug['image_height']['start'] = self._io.pos()
            self.image_height = self._io.read_u4le()
            self._debug['image_height']['end'] = self._io.pos()
            self._debug['screen_x_position']['start'] = self._io.pos()
            self.screen_x_position = self._io.read_u4le()
            self._debug['screen_x_position']['end'] = self._io.pos()
            self._debug['screen_y_position']['start'] = self._io.pos()
            self.screen_y_position = self._io.read_u4le()
            self._debug['screen_y_position']['end'] = self._io.pos()
            self._debug['ofs_image']['start'] = self._io.pos()
            self.ofs_image = self._io.read_u4le()
            self._debug['ofs_image']['end'] = self._io.pos()
            self._debug['len_image']['start'] = self._io.pos()
            self.len_image = self._io.read_u4le()
            self._debug['len_image']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.image_body
            if hasattr(self, '_m_image_body'):
                pass


        @property
        def image_body(self):
            if hasattr(self, '_m_image_body'):
                return self._m_image_body

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_image)
            self._debug['_m_image_body']['start'] = io.pos()
            self._m_image_body = io.read_bytes(self.len_image)
            self._debug['_m_image_body']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_image_body', None)



