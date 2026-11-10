# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Gdkp(KaitaiStruct):
    """
    .. seealso::
       Source - https://gitlab.gnome.org/GNOME/gdk-pixbuf/-/blob/2.42.2/gdk-pixbuf/gdk-pixdata.h
    """
    SEQ_FIELDS = ["header", "pixel_data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Gdkp, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(24)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Gdkp.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['pixel_data']['start'] = self._io.pos()
        self.pixel_data = self._io.read_bytes(self.header.len_pixel_data - 24)
        self._debug['pixel_data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_pixel_data", "pixdata_type", "rowstride", "width", "height"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Gdkp.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x47\x64\x6B\x50":
                raise kaitaistruct.ValidationNotEqualError(b"\x47\x64\x6B\x50", self.magic, self._io, u"/types/header/seq/0")
            self._debug['len_pixel_data']['start'] = self._io.pos()
            self.len_pixel_data = self._io.read_u4be()
            self._debug['len_pixel_data']['end'] = self._io.pos()
            self._debug['pixdata_type']['start'] = self._io.pos()
            self.pixdata_type = self._io.read_u4be()
            self._debug['pixdata_type']['end'] = self._io.pos()
            self._debug['rowstride']['start'] = self._io.pos()
            self.rowstride = self._io.read_u4be()
            self._debug['rowstride']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u4be()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u4be()
            self._debug['height']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



