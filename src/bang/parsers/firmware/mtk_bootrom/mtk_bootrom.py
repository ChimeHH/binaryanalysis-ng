# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MtkBootrom(KaitaiStruct):
    """
    .. seealso::
       Source - https://source.denx.de/u-boot/u-boot/-/blob/a0953b34d9d8d9309c3eabbb75746fef66b15ffe/tools/mtk_image.h
    
    
    .. seealso::
       Source - https://source.denx.de/u-boot/u-boot/-/blob/a0953b34d9d8d9309c3eabbb75746fef66b15ffe/tools/mtk_image.c
    """

    class BootromType(IntEnum):
        file_info = 0
        bl_info = 1
        anti_clone = 2
        bl_security_key = 3
        brom_config = 7
        brom_security_config = 8

    class SignatureTypes(IntEnum):
        no_signature = 0
        sha256 = 1
    SEQ_FIELDS = ["file_info_header", "file_info_data", "bl_info_header", "bl_info_data", "brom_config_header", "brom_config_data", "bl_security_key_header", "bl_security_key_data", "anti_clone_header", "anti_clone_data", "brom_security_config_header", "brom_security_config_data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(MtkBootrom, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['file_info_header']['start'] = self._io.pos()
        self.file_info_header = MtkBootrom.CommonHeader(self._io, self, self._root)
        self._debug['file_info_header']['end'] = self._io.pos()
        self._debug['file_info_data']['start'] = self._io.pos()
        self._raw_file_info_data = self._io.read_bytes(self.file_info_header.len_data - 8)
        _io__raw_file_info_data = KaitaiStream(BytesIO(self._raw_file_info_data))
        self.file_info_data = MtkBootrom.FileInfo(_io__raw_file_info_data, self, self._root)
        self._debug['file_info_data']['end'] = self._io.pos()
        self._debug['bl_info_header']['start'] = self._io.pos()
        self.bl_info_header = MtkBootrom.CommonHeader(self._io, self, self._root)
        self._debug['bl_info_header']['end'] = self._io.pos()
        self._debug['bl_info_data']['start'] = self._io.pos()
        self._raw_bl_info_data = self._io.read_bytes(self.bl_info_header.len_data - 8)
        _io__raw_bl_info_data = KaitaiStream(BytesIO(self._raw_bl_info_data))
        self.bl_info_data = MtkBootrom.BlInfo(_io__raw_bl_info_data, self, self._root)
        self._debug['bl_info_data']['end'] = self._io.pos()
        self._debug['brom_config_header']['start'] = self._io.pos()
        self.brom_config_header = MtkBootrom.CommonHeader(self._io, self, self._root)
        self._debug['brom_config_header']['end'] = self._io.pos()
        self._debug['brom_config_data']['start'] = self._io.pos()
        self._raw_brom_config_data = self._io.read_bytes(self.brom_config_header.len_data - 8)
        _io__raw_brom_config_data = KaitaiStream(BytesIO(self._raw_brom_config_data))
        self.brom_config_data = MtkBootrom.BromConfig(_io__raw_brom_config_data, self, self._root)
        self._debug['brom_config_data']['end'] = self._io.pos()
        self._debug['bl_security_key_header']['start'] = self._io.pos()
        self.bl_security_key_header = MtkBootrom.CommonHeader(self._io, self, self._root)
        self._debug['bl_security_key_header']['end'] = self._io.pos()
        self._debug['bl_security_key_data']['start'] = self._io.pos()
        self._raw_bl_security_key_data = self._io.read_bytes(self.bl_security_key_header.len_data - 8)
        _io__raw_bl_security_key_data = KaitaiStream(BytesIO(self._raw_bl_security_key_data))
        self.bl_security_key_data = MtkBootrom.BlSecurityKey(_io__raw_bl_security_key_data, self, self._root)
        self._debug['bl_security_key_data']['end'] = self._io.pos()
        self._debug['anti_clone_header']['start'] = self._io.pos()
        self.anti_clone_header = MtkBootrom.CommonHeader(self._io, self, self._root)
        self._debug['anti_clone_header']['end'] = self._io.pos()
        self._debug['anti_clone_data']['start'] = self._io.pos()
        self._raw_anti_clone_data = self._io.read_bytes(self.anti_clone_header.len_data - 8)
        _io__raw_anti_clone_data = KaitaiStream(BytesIO(self._raw_anti_clone_data))
        self.anti_clone_data = MtkBootrom.AntiClone(_io__raw_anti_clone_data, self, self._root)
        self._debug['anti_clone_data']['end'] = self._io.pos()
        self._debug['brom_security_config_header']['start'] = self._io.pos()
        self.brom_security_config_header = MtkBootrom.CommonHeader(self._io, self, self._root)
        self._debug['brom_security_config_header']['end'] = self._io.pos()
        self._debug['brom_security_config_data']['start'] = self._io.pos()
        self._raw_brom_security_config_data = self._io.read_bytes(self.brom_security_config_header.len_data - 8)
        _io__raw_brom_security_config_data = KaitaiStream(BytesIO(self._raw_brom_security_config_data))
        self.brom_security_config_data = MtkBootrom.BromSecurityConfig(_io__raw_brom_security_config_data, self, self._root)
        self._debug['brom_security_config_data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.file_info_header._fetch_instances()
        self.file_info_data._fetch_instances()
        self.bl_info_header._fetch_instances()
        self.bl_info_data._fetch_instances()
        self.brom_config_header._fetch_instances()
        self.brom_config_data._fetch_instances()
        self.bl_security_key_header._fetch_instances()
        self.bl_security_key_data._fetch_instances()
        self.anti_clone_header._fetch_instances()
        self.anti_clone_data._fetch_instances()
        self.brom_security_config_header._fetch_instances()
        self.brom_security_config_data._fetch_instances()

    class AntiClone(KaitaiStruct):
        SEQ_FIELDS = ["ac_b2k", "ac_b2c", "padding", "ofs_anti_clone", "len_anti_clone"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkBootrom.AntiClone, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ac_b2k']['start'] = self._io.pos()
            self.ac_b2k = self._io.read_u1()
            self._debug['ac_b2k']['end'] = self._io.pos()
            self._debug['ac_b2c']['start'] = self._io.pos()
            self.ac_b2c = self._io.read_u1()
            self._debug['ac_b2c']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(2)
            self._debug['padding']['end'] = self._io.pos()
            self._debug['ofs_anti_clone']['start'] = self._io.pos()
            self.ofs_anti_clone = self._io.read_u1()
            self._debug['ofs_anti_clone']['end'] = self._io.pos()
            self._debug['len_anti_clone']['start'] = self._io.pos()
            self.len_anti_clone = self._io.read_u1()
            self._debug['len_anti_clone']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class BlInfo(KaitaiStruct):
        SEQ_FIELDS = ["attr"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkBootrom.BlInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['attr']['start'] = self._io.pos()
            self.attr = self._io.read_u4le()
            self._debug['attr']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class BlSecurityKey(KaitaiStruct):
        SEQ_FIELDS = ["key"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkBootrom.BlSecurityKey, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['key']['start'] = self._io.pos()
            self.key = self._io.read_bytes(524)
            self._debug['key']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class BromConfig(KaitaiStruct):
        SEQ_FIELDS = ["config_bits", "usbdl_by_auto_detect_timeout_ms", "unused1", "jump_bl_arm64", "unused2", "usbdl_by_kcol0_timeout_ms", "usbdl_by_flag_timeout_ms", "pad"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkBootrom.BromConfig, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['config_bits']['start'] = self._io.pos()
            self.config_bits = self._io.read_u4le()
            self._debug['config_bits']['end'] = self._io.pos()
            self._debug['usbdl_by_auto_detect_timeout_ms']['start'] = self._io.pos()
            self.usbdl_by_auto_detect_timeout_ms = self._io.read_u4le()
            self._debug['usbdl_by_auto_detect_timeout_ms']['end'] = self._io.pos()
            self._debug['unused1']['start'] = self._io.pos()
            self.unused1 = self._io.read_bytes(69)
            self._debug['unused1']['end'] = self._io.pos()
            self._debug['jump_bl_arm64']['start'] = self._io.pos()
            self.jump_bl_arm64 = self._io.read_u1()
            self._debug['jump_bl_arm64']['end'] = self._io.pos()
            self._debug['unused2']['start'] = self._io.pos()
            self.unused2 = self._io.read_bytes(2)
            self._debug['unused2']['end'] = self._io.pos()
            self._debug['usbdl_by_kcol0_timeout_ms']['start'] = self._io.pos()
            self.usbdl_by_kcol0_timeout_ms = self._io.read_u4le()
            self._debug['usbdl_by_kcol0_timeout_ms']['end'] = self._io.pos()
            self._debug['usbdl_by_flag_timeout_ms']['start'] = self._io.pos()
            self.usbdl_by_flag_timeout_ms = self._io.read_u4le()
            self._debug['usbdl_by_flag_timeout_ms']['end'] = self._io.pos()
            self._debug['pad']['start'] = self._io.pos()
            self.pad = self._io.read_bytes(4)
            self._debug['pad']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class BromSecurityConfig(KaitaiStruct):
        SEQ_FIELDS = ["configuration", "customer_name", "pad"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkBootrom.BromSecurityConfig, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['configuration']['start'] = self._io.pos()
            self.configuration = self._io.read_u4le()
            self._debug['configuration']['end'] = self._io.pos()
            self._debug['customer_name']['start'] = self._io.pos()
            self.customer_name = self._io.read_bytes(32)
            self._debug['customer_name']['end'] = self._io.pos()
            self._debug['pad']['start'] = self._io.pos()
            self.pad = self._io.read_bytes(4)
            self._debug['pad']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def jtag_enabled(self):
            if hasattr(self, '_m_jtag_enabled'):
                return self._m_jtag_enabled

            self._m_jtag_enabled = self.configuration & 1 == 1
            return getattr(self, '_m_jtag_enabled', None)

        @property
        def uart_enabled(self):
            if hasattr(self, '_m_uart_enabled'):
                return self._m_uart_enabled

            self._m_uart_enabled = self.configuration & 2 == 2
            return getattr(self, '_m_uart_enabled', None)


    class CommonHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "len_data", "bootrom_type"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkBootrom.CommonHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(3)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x4D\x4D\x4D":
                raise kaitaistruct.ValidationNotEqualError(b"\x4D\x4D\x4D", self.magic, self._io, u"/types/common_header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u1()
            self._debug['version']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u2le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['bootrom_type']['start'] = self._io.pos()
            self.bootrom_type = KaitaiStream.resolve_enum(MtkBootrom.BootromType, self._io.read_u2le())
            self._debug['bootrom_type']['end'] = self._io.pos()
            if not  ((self.bootrom_type == MtkBootrom.BootromType.anti_clone) or (self.bootrom_type == MtkBootrom.BootromType.bl_info) or (self.bootrom_type == MtkBootrom.BootromType.bl_security_key) or (self.bootrom_type == MtkBootrom.BootromType.brom_config) or (self.bootrom_type == MtkBootrom.BootromType.brom_security_config) or (self.bootrom_type == MtkBootrom.BootromType.file_info)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.bootrom_type, self._io, u"/types/common_header/seq/3")


        def _fetch_instances(self):
            pass


    class FileInfo(KaitaiStruct):
        SEQ_FIELDS = ["name", "unused", "file_type", "flash_type", "signature_type", "load_address", "total_size", "max_size", "header_size", "signature_size", "jump_offset", "processed"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkBootrom.FileInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(12), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['unused']['start'] = self._io.pos()
            self.unused = self._io.read_bytes(4)
            self._debug['unused']['end'] = self._io.pos()
            self._debug['file_type']['start'] = self._io.pos()
            self.file_type = self._io.read_u2le()
            self._debug['file_type']['end'] = self._io.pos()
            self._debug['flash_type']['start'] = self._io.pos()
            self.flash_type = self._io.read_u1()
            self._debug['flash_type']['end'] = self._io.pos()
            self._debug['signature_type']['start'] = self._io.pos()
            self.signature_type = self._io.read_u1()
            self._debug['signature_type']['end'] = self._io.pos()
            self._debug['load_address']['start'] = self._io.pos()
            self.load_address = self._io.read_u4le()
            self._debug['load_address']['end'] = self._io.pos()
            self._debug['total_size']['start'] = self._io.pos()
            self.total_size = self._io.read_u4le()
            self._debug['total_size']['end'] = self._io.pos()
            self._debug['max_size']['start'] = self._io.pos()
            self.max_size = self._io.read_u4le()
            self._debug['max_size']['end'] = self._io.pos()
            self._debug['header_size']['start'] = self._io.pos()
            self.header_size = self._io.read_u4le()
            self._debug['header_size']['end'] = self._io.pos()
            self._debug['signature_size']['start'] = self._io.pos()
            self.signature_size = self._io.read_u4le()
            self._debug['signature_size']['end'] = self._io.pos()
            self._debug['jump_offset']['start'] = self._io.pos()
            self.jump_offset = self._io.read_u4le()
            self._debug['jump_offset']['end'] = self._io.pos()
            self._debug['processed']['start'] = self._io.pos()
            self.processed = self._io.read_u4le()
            self._debug['processed']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



