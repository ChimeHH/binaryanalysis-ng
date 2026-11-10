# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Ico(KaitaiStruct):
    """Microsoft Windows uses specific file format to store applications
    icons - ICO. This is a container that contains one or more image
    files (effectively, DIB parts of BMP files or full PNG files are
    contained inside).
    
    .. seealso::
       Source - https://msdn.microsoft.com/en-us/library/ms997538.aspx
    
    
    .. seealso::
       Source - https://en.wikipedia.org/wiki/ICO_(file_format)
    """
    SEQ_FIELDS = ["magic", "num_images", "images"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Ico, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x00\x00\x01\x00":
            raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x01\x00", self.magic, self._io, u"/seq/0")
        self._debug['num_images']['start'] = self._io.pos()
        self.num_images = self._io.read_u2le()
        self._debug['num_images']['end'] = self._io.pos()
        if not self.num_images >= 1:
            raise kaitaistruct.ValidationLessThanError(1, self.num_images, self._io, u"/seq/1")
        self._debug['images']['start'] = self._io.pos()
        self._debug['images']['arr'] = []
        self.images = []
        for i in range(self.num_images):
            self._debug['images']['arr'].append({'start': self._io.pos()})
            self.images.append(Ico.IconDirEntry(self._io, self, self._root))
            self._debug['images']['arr'][i]['end'] = self._io.pos()

        self._debug['images']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.images)):
            pass
            self.images[i]._fetch_instances()


    class Bitmapinfoheader(KaitaiStruct):
        """The icHeader member has the form of a DIB BITMAPINFOHEADER. Only the
        following members are used: biSize, biWidth, biHeight, biPlanes,
        biBitCount, biSizeImage. All other members must be 0.
        
        .. seealso::
           Source - https://web.archive.org/web/20160531004250/https://msdn.microsoft.com/en-us/library/ms997538.aspx
        """
        SEQ_FIELDS = ["len_header", "width", "height", "planes", "bit_count", "compression", "len_image", "x_resolution", "y_resolution", "num_colors_used", "num_colors_important"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ico.Bitmapinfoheader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            if not  ((self.len_header == 12) or (self.len_header == 64) or (self.len_header == 16) or (self.len_header == 40) or (self.len_header == 52) or (self.len_header == 56) or (self.len_header == 108) or (self.len_header == 124)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.len_header, self._io, u"/types/bitmapinfoheader/seq/0")
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u4le()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u4le()
            self._debug['height']['end'] = self._io.pos()
            self._debug['planes']['start'] = self._io.pos()
            self.planes = self._io.read_u2le()
            self._debug['planes']['end'] = self._io.pos()
            self._debug['bit_count']['start'] = self._io.pos()
            self.bit_count = self._io.read_u2le()
            self._debug['bit_count']['end'] = self._io.pos()
            if not  ((self.bit_count == 1) or (self.bit_count == 4) or (self.bit_count == 8) or (self.bit_count == 16) or (self.bit_count == 24) or (self.bit_count == 32)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.bit_count, self._io, u"/types/bitmapinfoheader/seq/4")
            self._debug['compression']['start'] = self._io.pos()
            self.compression = self._io.read_u4le()
            self._debug['compression']['end'] = self._io.pos()
            if not self.compression == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.compression, self._io, u"/types/bitmapinfoheader/seq/5")
            self._debug['len_image']['start'] = self._io.pos()
            self.len_image = self._io.read_u4le()
            self._debug['len_image']['end'] = self._io.pos()
            self._debug['x_resolution']['start'] = self._io.pos()
            self.x_resolution = self._io.read_u4le()
            self._debug['x_resolution']['end'] = self._io.pos()
            if not self.x_resolution == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.x_resolution, self._io, u"/types/bitmapinfoheader/seq/7")
            self._debug['y_resolution']['start'] = self._io.pos()
            self.y_resolution = self._io.read_u4le()
            self._debug['y_resolution']['end'] = self._io.pos()
            if not self.y_resolution == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.y_resolution, self._io, u"/types/bitmapinfoheader/seq/8")
            self._debug['num_colors_used']['start'] = self._io.pos()
            self.num_colors_used = self._io.read_u4le()
            self._debug['num_colors_used']['end'] = self._io.pos()
            self._debug['num_colors_important']['start'] = self._io.pos()
            self.num_colors_important = self._io.read_u4le()
            self._debug['num_colors_important']['end'] = self._io.pos()
            if not self.num_colors_important == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.num_colors_important, self._io, u"/types/bitmapinfoheader/seq/10")


        def _fetch_instances(self):
            pass


    class IconDirEntry(KaitaiStruct):
        SEQ_FIELDS = ["width", "height", "num_colors", "reserved", "num_planes", "bpp", "len_img", "ofs_img"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Ico.IconDirEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u1()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u1()
            self._debug['height']['end'] = self._io.pos()
            self._debug['num_colors']['start'] = self._io.pos()
            self.num_colors = self._io.read_u1()
            self._debug['num_colors']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_u1()
            self._debug['reserved']['end'] = self._io.pos()
            if not  ((self.reserved == 0) or (self.reserved == 255)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.reserved, self._io, u"/types/icon_dir_entry/seq/3")
            self._debug['num_planes']['start'] = self._io.pos()
            self.num_planes = self._io.read_u2le()
            self._debug['num_planes']['end'] = self._io.pos()
            self._debug['bpp']['start'] = self._io.pos()
            self.bpp = self._io.read_u2le()
            self._debug['bpp']['end'] = self._io.pos()
            self._debug['len_img']['start'] = self._io.pos()
            self.len_img = self._io.read_u4le()
            self._debug['len_img']['end'] = self._io.pos()
            if not self.len_img >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.len_img, self._io, u"/types/icon_dir_entry/seq/6")
            if not self.len_img <= self._root._io.size():
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size(), self.len_img, self._io, u"/types/icon_dir_entry/seq/6")
            self._debug['ofs_img']['start'] = self._io.pos()
            self.ofs_img = self._io.read_u4le()
            self._debug['ofs_img']['end'] = self._io.pos()
            if not self.ofs_img <= self._root._io.size():
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size(), self.ofs_img, self._io, u"/types/icon_dir_entry/seq/7")


        def _fetch_instances(self):
            pass
            _ = self.bmp
            if hasattr(self, '_m_bmp'):
                pass
                self._m_bmp._fetch_instances()

            _ = self.img
            if hasattr(self, '_m_img'):
                pass

            _ = self.png_header
            if hasattr(self, '_m_png_header'):
                pass


        @property
        def bmp(self):
            if hasattr(self, '_m_bmp'):
                return self._m_bmp

            if (not (self.is_png)):
                pass
                _pos = self._io.pos()
                self._io.seek(self.ofs_img)
                self._debug['_m_bmp']['start'] = self._io.pos()
                self._raw__m_bmp = self._io.read_bytes(40)
                _io__raw__m_bmp = KaitaiStream(BytesIO(self._raw__m_bmp))
                self._m_bmp = Ico.Bitmapinfoheader(_io__raw__m_bmp, self, self._root)
                self._debug['_m_bmp']['end'] = self._io.pos()
                self._io.seek(_pos)

            return getattr(self, '_m_bmp', None)

        @property
        def img(self):
            """Raw image data. Use `is_png` to determine whether this is an
            embedded PNG file (true) or a DIB bitmap (false) and call a
            relevant parser, if needed to parse image data further.
            """
            if hasattr(self, '_m_img'):
                return self._m_img

            _pos = self._io.pos()
            self._io.seek(self.ofs_img)
            self._debug['_m_img']['start'] = self._io.pos()
            self._m_img = self._io.read_bytes(self.len_img)
            self._debug['_m_img']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_img', None)

        @property
        def is_png(self):
            """True if this image is in PNG format."""
            if hasattr(self, '_m_is_png'):
                return self._m_is_png

            self._m_is_png = self.png_header == b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
            return getattr(self, '_m_is_png', None)

        @property
        def png_header(self):
            """Pre-reads first 8 bytes of the image to determine if it's an
            embedded PNG file.
            """
            if hasattr(self, '_m_png_header'):
                return self._m_png_header

            _pos = self._io.pos()
            self._io.seek(self.ofs_img)
            self._debug['_m_png_header']['start'] = self._io.pos()
            self._m_png_header = self._io.read_bytes(8)
            self._debug['_m_png_header']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_png_header', None)



