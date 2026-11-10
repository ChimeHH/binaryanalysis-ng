# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Sunplus(KaitaiStruct):
    """
    .. seealso::
       Source - https://web.archive.org/web/20210301164514/https://www.goprawn.com/forum/sunplus-cams/10333-icatch-sunplus-firmware-hacks
    
    
    .. seealso::
       Source - https://github.com/Linouth/iCatch-V50-Playground
    """
    SEQ_FIELDS = ["header", "isp_bootloader", "aimg", "bimg", "cimg", "bin", "bad_pixel", "dram"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Sunplus, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(1024)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Sunplus.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['isp_bootloader']['start'] = self._io.pos()
        self.isp_bootloader = self._io.read_bytes(self.header.ofs_aimg - 1024)
        self._debug['isp_bootloader']['end'] = self._io.pos()
        self._debug['aimg']['start'] = self._io.pos()
        self.aimg = self._io.read_bytes(self.len_aimg)
        self._debug['aimg']['end'] = self._io.pos()
        self._debug['bimg']['start'] = self._io.pos()
        self.bimg = self._io.read_bytes(self.len_bimg)
        self._debug['bimg']['end'] = self._io.pos()
        if self.header.ofs_cimg != 0:
            pass
            self._debug['cimg']['start'] = self._io.pos()
            self.cimg = self._io.read_bytes(self.len_cimg)
            self._debug['cimg']['end'] = self._io.pos()

        if self.header.ofs_bin != 0:
            pass
            self._debug['bin']['start'] = self._io.pos()
            self.bin = self._io.read_bytes(self.len_bin)
            self._debug['bin']['end'] = self._io.pos()

        self._debug['bad_pixel']['start'] = self._io.pos()
        self.bad_pixel = self._io.read_bytes(self.len_bad_pixel)
        self._debug['bad_pixel']['end'] = self._io.pos()
        self._debug['dram']['start'] = self._io.pos()
        self.dram = self._io.read_bytes(self.len_dram)
        self._debug['dram']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        if self.header.ofs_cimg != 0:
            pass

        if self.header.ofs_bin != 0:
            pass

        _ = self.raw_header
        if hasattr(self, '_m_raw_header'):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_firmware", "ofs_aimg", "ofs_bimg", "ofs_cimg", "ofs_bin", "ofs_bad_pixel", "ofs_dram"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Sunplus.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(16)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x53\x55\x4E\x50\x20\x42\x55\x52\x4E\x20\x46\x49\x4C\x45\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x53\x55\x4E\x50\x20\x42\x55\x52\x4E\x20\x46\x49\x4C\x45\x00\x00", self.magic, self._io, u"/types/header/seq/0")
            self._debug['len_firmware']['start'] = self._io.pos()
            self.len_firmware = self._io.read_u4le()
            self._debug['len_firmware']['end'] = self._io.pos()
            self._debug['ofs_aimg']['start'] = self._io.pos()
            self.ofs_aimg = self._io.read_u4le()
            self._debug['ofs_aimg']['end'] = self._io.pos()
            self._debug['ofs_bimg']['start'] = self._io.pos()
            self.ofs_bimg = self._io.read_u4le()
            self._debug['ofs_bimg']['end'] = self._io.pos()
            self._debug['ofs_cimg']['start'] = self._io.pos()
            self.ofs_cimg = self._io.read_u4le()
            self._debug['ofs_cimg']['end'] = self._io.pos()
            self._debug['ofs_bin']['start'] = self._io.pos()
            self.ofs_bin = self._io.read_u4le()
            self._debug['ofs_bin']['end'] = self._io.pos()
            self._debug['ofs_bad_pixel']['start'] = self._io.pos()
            self.ofs_bad_pixel = self._io.read_u4le()
            self._debug['ofs_bad_pixel']['end'] = self._io.pos()
            self._debug['ofs_dram']['start'] = self._io.pos()
            self.ofs_dram = self._io.read_u4le()
            self._debug['ofs_dram']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def len_aimg(self):
        if hasattr(self, '_m_len_aimg'):
            return self._m_len_aimg

        self._m_len_aimg = self.header.ofs_bimg - self.header.ofs_aimg
        return getattr(self, '_m_len_aimg', None)

    @property
    def len_bad_pixel(self):
        if hasattr(self, '_m_len_bad_pixel'):
            return self._m_len_bad_pixel

        self._m_len_bad_pixel = self.header.ofs_dram - self.header.ofs_bad_pixel
        return getattr(self, '_m_len_bad_pixel', None)

    @property
    def len_bimg(self):
        if hasattr(self, '_m_len_bimg'):
            return self._m_len_bimg

        self._m_len_bimg = (self.header.ofs_bin - self.header.ofs_bimg if self.header.ofs_cimg == 0 else self.header.ofs_cimg - self.header.ofs_bimg)
        return getattr(self, '_m_len_bimg', None)

    @property
    def len_bin(self):
        if hasattr(self, '_m_len_bin'):
            return self._m_len_bin

        self._m_len_bin = (0 if self.header.ofs_bin == 0 else self.header.ofs_bad_pixel - self.header.ofs_bin)
        return getattr(self, '_m_len_bin', None)

    @property
    def len_cimg(self):
        if hasattr(self, '_m_len_cimg'):
            return self._m_len_cimg

        self._m_len_cimg = (self.header.ofs_bad_pixel - self.header.ofs_cimg if self.header.ofs_bin == 0 else self.header.ofs_bin - self.header.ofs_cimg)
        return getattr(self, '_m_len_cimg', None)

    @property
    def len_dram(self):
        if hasattr(self, '_m_len_dram'):
            return self._m_len_dram

        self._m_len_dram = self.header.len_firmware - self.header.ofs_dram
        return getattr(self, '_m_len_dram', None)

    @property
    def raw_header(self):
        if hasattr(self, '_m_raw_header'):
            return self._m_raw_header

        _pos = self._io.pos()
        self._io.seek(0)
        self._debug['_m_raw_header']['start'] = self._io.pos()
        self._m_raw_header = self._io.read_bytes(1024)
        self._debug['_m_raw_header']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_raw_header', None)


