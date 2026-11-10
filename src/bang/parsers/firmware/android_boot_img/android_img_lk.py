# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class AndroidImgLk(KaitaiStruct):
    """A variant from (probably) Qualcomm with a slightly different file format.
    
    Test file: lineage-14.1-20180620-nightly-FP2-signed.zip
    
    .. seealso::
       Source - https://github.com/M1cha/android_bootable_bootloader_lk/blob/condor/app/aboot/bootimg.h
    """
    SEQ_FIELDS = ["header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(AndroidImgLk, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = AndroidImgLk.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        _ = self.header_version
        if hasattr(self, '_m_header_version'):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "kernel", "ramdisk", "second", "tags_load", "page_size", "dt_size", "unused", "name", "cmdline"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidImgLk.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x41\x4E\x44\x52\x4F\x49\x44\x21":
                raise kaitaistruct.ValidationNotEqualError(b"\x41\x4E\x44\x52\x4F\x49\x44\x21", self.magic, self._io, u"/types/header/seq/0")
            self._debug['kernel']['start'] = self._io.pos()
            self.kernel = AndroidImgLk.Load(self._io, self, self._root)
            self._debug['kernel']['end'] = self._io.pos()
            self._debug['ramdisk']['start'] = self._io.pos()
            self.ramdisk = AndroidImgLk.Load(self._io, self, self._root)
            self._debug['ramdisk']['end'] = self._io.pos()
            self._debug['second']['start'] = self._io.pos()
            self.second = AndroidImgLk.Load(self._io, self, self._root)
            self._debug['second']['end'] = self._io.pos()
            self._debug['tags_load']['start'] = self._io.pos()
            self.tags_load = self._io.read_u4le()
            self._debug['tags_load']['end'] = self._io.pos()
            self._debug['page_size']['start'] = self._io.pos()
            self.page_size = self._io.read_u4le()
            self._debug['page_size']['end'] = self._io.pos()
            self._debug['dt_size']['start'] = self._io.pos()
            self.dt_size = self._io.read_u4le()
            self._debug['dt_size']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_u4le()
            self._debug['unused']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['cmdline']['start'] = self._io.pos()
            self.cmdline = (KaitaiStream.bytes_terminate(self._io.read_bytes(512), 0, False)).decode(u"ASCII")
            self._debug['cmdline']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.kernel._fetch_instances()
            self.ramdisk._fetch_instances()
            self.second._fetch_instances()
            _ = self.dtb
            if hasattr(self, '_m_dtb'):
                pass

            _ = self.kernel_img
            if hasattr(self, '_m_kernel_img'):
                pass

            _ = self.ramdisk_img
            if hasattr(self, '_m_ramdisk_img'):
                pass

            _ = self.second_img
            if hasattr(self, '_m_second_img'):
                pass


        @property
        def base(self):
            """base loading address."""
            if hasattr(self, '_m_base'):
                return self._m_base

            self._m_base = self.kernel.addr - 32768
            return getattr(self, '_m_base', None)

        @property
        def dtb(self):
            if hasattr(self, '_m_dtb'):
                return self._m_dtb

            _pos = self._io.pos()
            self._io.seek(self.dtb_pos)
            self._debug['_m_dtb']['start'] = self._io.pos()
            self._m_dtb = self._io.read_bytes(self.dt_size)
            self._debug['_m_dtb']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_dtb', None)

        @property
        def dtb_pos(self):
            if hasattr(self, '_m_dtb_pos'):
                return self._m_dtb_pos

            self._m_dtb_pos = ((((((self.page_size + self.kernel.size) + self.ramdisk.size) + self.second.size) + self.page_size) - 1) // self.page_size) * self.page_size
            return getattr(self, '_m_dtb_pos', None)

        @property
        def kernel_img(self):
            if hasattr(self, '_m_kernel_img'):
                return self._m_kernel_img

            _pos = self._io.pos()
            self._io.seek(self.page_size)
            self._debug['_m_kernel_img']['start'] = self._io.pos()
            self._m_kernel_img = self._io.read_bytes(self.kernel.size)
            self._debug['_m_kernel_img']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_kernel_img', None)

        @property
        def kernel_offset(self):
            """kernel offset from base."""
            if hasattr(self, '_m_kernel_offset'):
                return self._m_kernel_offset

            self._m_kernel_offset = self.kernel.addr - self.base
            return getattr(self, '_m_kernel_offset', None)

        @property
        def ramdisk_img(self):
            if hasattr(self, '_m_ramdisk_img'):
                return self._m_ramdisk_img

            if self.ramdisk.size > 0:
                pass
                _pos = self._io.pos()
                self._io.seek(((((self.page_size + self.kernel.size) + self.page_size) - 1) // self.page_size) * self.page_size)
                self._debug['_m_ramdisk_img']['start'] = self._io.pos()
                self._m_ramdisk_img = self._io.read_bytes(self.ramdisk.size)
                self._debug['_m_ramdisk_img']['end'] = self._io.pos()
                self._io.seek(_pos)

            return getattr(self, '_m_ramdisk_img', None)

        @property
        def ramdisk_offset(self):
            """ramdisk offset from base."""
            if hasattr(self, '_m_ramdisk_offset'):
                return self._m_ramdisk_offset

            self._m_ramdisk_offset = (self.ramdisk.addr - self.base if self.ramdisk.addr > 0 else 0)
            return getattr(self, '_m_ramdisk_offset', None)

        @property
        def second_img(self):
            if hasattr(self, '_m_second_img'):
                return self._m_second_img

            if self.second.size > 0:
                pass
                _pos = self._io.pos()
                self._io.seek((((((self.page_size + self.kernel.size) + self.ramdisk.size) + self.page_size) - 1) // self.page_size) * self.page_size)
                self._debug['_m_second_img']['start'] = self._io.pos()
                self._m_second_img = self._io.read_bytes(self.second.size)
                self._debug['_m_second_img']['end'] = self._io.pos()
                self._io.seek(_pos)

            return getattr(self, '_m_second_img', None)

        @property
        def second_offset(self):
            """2nd bootloader offset from base."""
            if hasattr(self, '_m_second_offset'):
                return self._m_second_offset

            self._m_second_offset = (self.second.addr - self.base if self.second.addr > 0 else 0)
            return getattr(self, '_m_second_offset', None)

        @property
        def tags_offset(self):
            """tags offset from base."""
            if hasattr(self, '_m_tags_offset'):
                return self._m_tags_offset

            self._m_tags_offset = self.tags_load - self.base
            return getattr(self, '_m_tags_offset', None)


    class Load(KaitaiStruct):
        SEQ_FIELDS = ["size", "addr"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AndroidImgLk.Load, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['addr']['start'] = self._io.pos()
            self.addr = self._io.read_u4le()
            self._debug['addr']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def header_version(self):
        if hasattr(self, '_m_header_version'):
            return self._m_header_version

        _pos = self._io.pos()
        self._io.seek(40)
        self._debug['_m_header_version']['start'] = self._io.pos()
        self._m_header_version = self._io.read_u4le()
        self._debug['_m_header_version']['end'] = self._io.pos()
        if not self._m_header_version >= 40:
            raise kaitaistruct.ValidationLessThanError(40, self._m_header_version, self._io, u"/instances/header_version")
        self._io.seek(_pos)
        return getattr(self, '_m_header_version', None)


