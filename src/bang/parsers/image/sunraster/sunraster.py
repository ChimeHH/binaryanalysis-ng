# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Sunraster(KaitaiStruct):
    """
    .. seealso::
       Source - https://www.fileformat.info/format/sunraster/egff.htm
    
    
    .. seealso::
       Source - https://www.fileformat.info/format/sunraster/spec/6191a773bc0046f18d42e77ca16c3a8c/view.htm
    
    
    .. seealso::
       Source - https://www.fileformat.info/format/sunraster/spec/598a59c4fac64c52897585d390d86360/view.htm
    """

    class BitmapTypes(IntEnum):
        old = 0
        standard = 1
        byte_encoded = 2
        rgb = 3
        tiff = 4
        iff = 5
        experimental = 65535
    SEQ_FIELDS = ["magic", "width", "height", "depth", "len_image_data", "bitmap_type", "color_map_type", "len_color_map"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Sunraster, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x59\xA6\x6A\x95":
            raise kaitaistruct.ValidationNotEqualError(b"\x59\xA6\x6A\x95", self.magic, self._io, u"/seq/0")
        self._debug['width']['start'] = self._io.pos()
        self.width = self._io.read_u4be()
        self._debug['width']['end'] = self._io.pos()
        self._debug['height']['start'] = self._io.pos()
        self.height = self._io.read_u4be()
        self._debug['height']['end'] = self._io.pos()
        self._debug['depth']['start'] = self._io.pos()
        self.depth = self._io.read_u4be()
        self._debug['depth']['end'] = self._io.pos()
        self._debug['len_image_data']['start'] = self._io.pos()
        self.len_image_data = self._io.read_u4be()
        self._debug['len_image_data']['end'] = self._io.pos()
        self._debug['bitmap_type']['start'] = self._io.pos()
        self.bitmap_type = KaitaiStream.resolve_enum(Sunraster.BitmapTypes, self._io.read_u4be())
        self._debug['bitmap_type']['end'] = self._io.pos()
        if not  ((self.bitmap_type == Sunraster.BitmapTypes.old) or (self.bitmap_type == Sunraster.BitmapTypes.standard) or (self.bitmap_type == Sunraster.BitmapTypes.byte_encoded) or (self.bitmap_type == Sunraster.BitmapTypes.rgb) or (self.bitmap_type == Sunraster.BitmapTypes.tiff) or (self.bitmap_type == Sunraster.BitmapTypes.iff) or (self.bitmap_type == Sunraster.BitmapTypes.experimental)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.bitmap_type, self._io, u"/seq/5")
        self._debug['color_map_type']['start'] = self._io.pos()
        self.color_map_type = self._io.read_u4be()
        self._debug['color_map_type']['end'] = self._io.pos()
        if not  ((self.color_map_type == 0) or (self.color_map_type == 1) or (self.color_map_type == 2)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.color_map_type, self._io, u"/seq/6")
        self._debug['len_color_map']['start'] = self._io.pos()
        self.len_color_map = self._io.read_u4be()
        self._debug['len_color_map']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass


