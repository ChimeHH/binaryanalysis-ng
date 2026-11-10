# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Tplink(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/rampageX/firmware-mod-kit/blob/104c8213f66d3aa9f9a2449f5d80638ad13c30dc/src/tpl-tool/src/tpl-tool.c
    """

    class DeviceInfo(IntEnum):
        tl_wa801nd_v1 = 134283265
        tl_wa901nd_v1 = 151060481
        tl_wa901nd_v2 = 151060482
        tl_wr941nd_v2 = 155254786
        tl_wr941nd_v4 = 155254788
        tl_wr1042nd_v1 = 272760833
        tl_wr1043nd_v1 = 272826369
        tl_wr2543n_v1 = 625147905
        tl_wdr4300_v1 = 1124073473
        tl_wdr4900_v1 = 1224736769
    SEQ_FIELDS = ["header", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Tplink, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(self.len_header)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Tplink.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self._raw_data = self._io.read_bytes(self.header.len_image - self.len_header)
        _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
        self.data = Tplink.Dummy(_io__raw_data, self, self._root)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.data._fetch_instances()
        _ = self.bootloader
        if hasattr(self, '_m_bootloader'):
            pass

        _ = self.image2
        if hasattr(self, '_m_image2'):
            pass

        _ = self.kernel
        if hasattr(self, '_m_kernel'):
            pass

        _ = self.rootfs
        if hasattr(self, '_m_rootfs'):
            pass


    class Dummy(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(Tplink.Dummy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["header_version", "vendor", "image_version", "product_id", "product_version", "padding_1", "image_checksum", "padding_2", "kernel_checksum", "padding_3", "kernel_load_address", "kernel_entry_point", "len_image", "ofs_kernel", "len_kernel", "ofs_rootfs", "len_rootfs", "ofs_bootloader", "len_bootloader", "firmware_version_major", "firmware_version_minor", "firmware_version_point", "padding_4"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Tplink.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header_version']['start'] = self._io.pos()
            self.header_version = self._io.read_u4be()
            self._debug['header_version']['end'] = self._io.pos()
            if not self.header_version == 16777216:
                raise kaitaistruct.ValidationNotEqualError(16777216, self.header_version, self._io, u"/types/header/seq/0")
            self._debug['vendor']['start'] = self._io.pos()
            self.vendor = (KaitaiStream.bytes_terminate(self._io.read_bytes(24), 0, False)).decode(u"UTF-8")
            self._debug['vendor']['end'] = self._io.pos()
            self._debug['image_version']['start'] = self._io.pos()
            self.image_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(36), 0, False)).decode(u"UTF-8")
            self._debug['image_version']['end'] = self._io.pos()
            self._debug['product_id']['start'] = self._io.pos()
            self.product_id = KaitaiStream.resolve_enum(Tplink.DeviceInfo, self._io.read_u4be())
            self._debug['product_id']['end'] = self._io.pos()
            self._debug['product_version']['start'] = self._io.pos()
            self.product_version = self._io.read_u4be()
            self._debug['product_version']['end'] = self._io.pos()
            self._debug['padding_1']['start'] = self._io.pos()
            self.padding_1 = self._io.read_bytes(4)
            self._debug['padding_1']['end'] = self._io.pos()
            if not self.padding_1 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.padding_1, self._io, u"/types/header/seq/5")
            self._debug['image_checksum']['start'] = self._io.pos()
            self.image_checksum = self._io.read_bytes(16)
            self._debug['image_checksum']['end'] = self._io.pos()
            self._debug['padding_2']['start'] = self._io.pos()
            self.padding_2 = self._io.read_bytes(4)
            self._debug['padding_2']['end'] = self._io.pos()
            if not self.padding_2 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.padding_2, self._io, u"/types/header/seq/7")
            self._debug['kernel_checksum']['start'] = self._io.pos()
            self.kernel_checksum = self._io.read_bytes(16)
            self._debug['kernel_checksum']['end'] = self._io.pos()
            self._debug['padding_3']['start'] = self._io.pos()
            self.padding_3 = self._io.read_bytes(4)
            self._debug['padding_3']['end'] = self._io.pos()
            if not self.padding_3 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.padding_3, self._io, u"/types/header/seq/9")
            self._debug['kernel_load_address']['start'] = self._io.pos()
            self.kernel_load_address = self._io.read_u4be()
            self._debug['kernel_load_address']['end'] = self._io.pos()
            self._debug['kernel_entry_point']['start'] = self._io.pos()
            self.kernel_entry_point = self._io.read_u4be()
            self._debug['kernel_entry_point']['end'] = self._io.pos()
            self._debug['len_image']['start'] = self._io.pos()
            self.len_image = self._io.read_u4be()
            self._debug['len_image']['end'] = self._io.pos()
            self._debug['ofs_kernel']['start'] = self._io.pos()
            self.ofs_kernel = self._io.read_u4be()
            self._debug['ofs_kernel']['end'] = self._io.pos()
            if not self.ofs_kernel <= self.len_image:
                raise kaitaistruct.ValidationGreaterThanError(self.len_image, self.ofs_kernel, self._io, u"/types/header/seq/13")
            self._debug['len_kernel']['start'] = self._io.pos()
            self.len_kernel = self._io.read_u4be()
            self._debug['len_kernel']['end'] = self._io.pos()
            if not self.len_kernel <= self.len_image:
                raise kaitaistruct.ValidationGreaterThanError(self.len_image, self.len_kernel, self._io, u"/types/header/seq/14")
            self._debug['ofs_rootfs']['start'] = self._io.pos()
            self.ofs_rootfs = self._io.read_u4be()
            self._debug['ofs_rootfs']['end'] = self._io.pos()
            if not self.ofs_rootfs <= self.len_image:
                raise kaitaistruct.ValidationGreaterThanError(self.len_image, self.ofs_rootfs, self._io, u"/types/header/seq/15")
            self._debug['len_rootfs']['start'] = self._io.pos()
            self.len_rootfs = self._io.read_u4be()
            self._debug['len_rootfs']['end'] = self._io.pos()
            if not self.len_rootfs <= self.len_image:
                raise kaitaistruct.ValidationGreaterThanError(self.len_image, self.len_rootfs, self._io, u"/types/header/seq/16")
            self._debug['ofs_bootloader']['start'] = self._io.pos()
            self.ofs_bootloader = self._io.read_u4be()
            self._debug['ofs_bootloader']['end'] = self._io.pos()
            if not self.ofs_bootloader <= self.len_image:
                raise kaitaistruct.ValidationGreaterThanError(self.len_image, self.ofs_bootloader, self._io, u"/types/header/seq/17")
            self._debug['len_bootloader']['start'] = self._io.pos()
            self.len_bootloader = self._io.read_u4be()
            self._debug['len_bootloader']['end'] = self._io.pos()
            if not self.len_bootloader <= self.len_image:
                raise kaitaistruct.ValidationGreaterThanError(self.len_image, self.len_bootloader, self._io, u"/types/header/seq/18")
            self._debug['firmware_version_major']['start'] = self._io.pos()
            self.firmware_version_major = self._io.read_u2be()
            self._debug['firmware_version_major']['end'] = self._io.pos()
            self._debug['firmware_version_minor']['start'] = self._io.pos()
            self.firmware_version_minor = self._io.read_u2be()
            self._debug['firmware_version_minor']['end'] = self._io.pos()
            self._debug['firmware_version_point']['start'] = self._io.pos()
            self.firmware_version_point = self._io.read_u2be()
            self._debug['firmware_version_point']['end'] = self._io.pos()
            self._debug['padding_4']['start'] = self._io.pos()
            self.padding_4 = self._io.read_bytes(354)
            self._debug['padding_4']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def bootloader(self):
        if hasattr(self, '_m_bootloader'):
            return self._m_bootloader

        if self.has_bootloader:
            pass
            io = self._root.data._io
            _pos = io.pos()
            io.seek(self.header.ofs_bootloader)
            self._debug['_m_bootloader']['start'] = io.pos()
            self._m_bootloader = io.read_bytes(self.header.len_bootloader)
            self._debug['_m_bootloader']['end'] = io.pos()
            io.seek(_pos)

        return getattr(self, '_m_bootloader', None)

    @property
    def has_bootloader(self):
        if hasattr(self, '_m_has_bootloader'):
            return self._m_has_bootloader

        self._m_has_bootloader = self.header.len_bootloader != 0
        return getattr(self, '_m_has_bootloader', None)

    @property
    def image2(self):
        if hasattr(self, '_m_image2'):
            return self._m_image2

        if self.has_bootloader:
            pass
            _pos = self._io.pos()
            self._io.seek(self.pos_image2)
            self._debug['_m_image2']['start'] = self._io.pos()
            self._m_image2 = self._io.read_bytes(self.header.len_image - self.pos_image2)
            self._debug['_m_image2']['end'] = self._io.pos()
            self._io.seek(_pos)

        return getattr(self, '_m_image2', None)

    @property
    def kernel(self):
        if hasattr(self, '_m_kernel'):
            return self._m_kernel

        if (not (self.has_bootloader)):
            pass
            io = self._root.data._io
            _pos = io.pos()
            io.seek(self.header.ofs_kernel - self._root.len_header)
            self._debug['_m_kernel']['start'] = io.pos()
            self._m_kernel = io.read_bytes(self.header.len_kernel)
            self._debug['_m_kernel']['end'] = io.pos()
            io.seek(_pos)

        return getattr(self, '_m_kernel', None)

    @property
    def len_header(self):
        if hasattr(self, '_m_len_header'):
            return self._m_len_header

        self._m_len_header = 512
        return getattr(self, '_m_len_header', None)

    @property
    def pos_image2(self):
        if hasattr(self, '_m_pos_image2'):
            return self._m_pos_image2

        self._m_pos_image2 = 131584
        return getattr(self, '_m_pos_image2', None)

    @property
    def rootfs(self):
        if hasattr(self, '_m_rootfs'):
            return self._m_rootfs

        if (not (self.has_bootloader)):
            pass
            io = self._root.data._io
            _pos = io.pos()
            io.seek(self.header.ofs_rootfs - self._root.len_header)
            self._debug['_m_rootfs']['start'] = io.pos()
            self._m_rootfs = io.read_bytes(self.header.len_rootfs)
            self._debug['_m_rootfs']['end'] = io.pos()
            io.seek(_pos)

        return getattr(self, '_m_rootfs', None)


