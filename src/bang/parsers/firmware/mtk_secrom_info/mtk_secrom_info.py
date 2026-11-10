# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MtkSecromInfo(KaitaiStruct):
    """
    .. seealso::
       Source - https://android.googlesource.com/kernel/mediatek/+/0164f13d76f1966b140ea06261ea6f63c073e080/drivers/misc/mediatek/masp/asf/asf_inc/sec_rom_info.h
    """
    SEQ_FIELDS = ["sec_rom"]
    def __init__(self, _io, _parent=None, _root=None):
        super(MtkSecromInfo, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['sec_rom']['start'] = self._io.pos()
        self._raw_sec_rom = self._io.read_bytes(960)
        _io__raw_sec_rom = KaitaiStream(BytesIO(self._raw_sec_rom))
        self.sec_rom = MtkSecromInfo.SecRom(_io__raw_sec_rom, self, self._root)
        self._debug['sec_rom']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.sec_rom._fetch_instances()

    class SecCtrl(KaitaiStruct):
        SEQ_FIELDS = ["name", "version", "usb_dl", "boot", "modem_auth", "sds_en", "ac_en", "aes_legacy", "secro_ac_en", "sml_aes_key_ac_en", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkSecromInfo.SecCtrl, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['usb_dl']['start'] = self._io.pos()
            self.usb_dl = self._io.read_u4le()
            self._debug['usb_dl']['end'] = self._io.pos()
            self._debug['boot']['start'] = self._io.pos()
            self.boot = self._io.read_u4le()
            self._debug['boot']['end'] = self._io.pos()
            self._debug['modem_auth']['start'] = self._io.pos()
            self.modem_auth = self._io.read_u4le()
            self._debug['modem_auth']['end'] = self._io.pos()
            self._debug['sds_en']['start'] = self._io.pos()
            self.sds_en = self._io.read_u4le()
            self._debug['sds_en']['end'] = self._io.pos()
            self._debug['ac_en']['start'] = self._io.pos()
            self.ac_en = self._io.read_bytes(1)
            self._debug['ac_en']['end'] = self._io.pos()
            self._debug['aes_legacy']['start'] = self._io.pos()
            self.aes_legacy = self._io.read_bytes(1)
            self._debug['aes_legacy']['end'] = self._io.pos()
            self._debug['secro_ac_en']['start'] = self._io.pos()
            self.secro_ac_en = self._io.read_bytes(1)
            self._debug['secro_ac_en']['end'] = self._io.pos()
            self._debug['sml_aes_key_ac_en']['start'] = self._io.pos()
            self.sml_aes_key_ac_en = self._io.read_bytes(1)
            self._debug['sml_aes_key_ac_en']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(12)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class SecKey(KaitaiStruct):
        SEQ_FIELDS = ["name", "version", "img_rsa_n", "img_rsa_e", "sml_aes_key", "crypto_seed", "sml_auth_rsa_n", "sml_auth_rsa_e"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkSecromInfo.SecKey, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['img_rsa_n']['start'] = self._io.pos()
            self.img_rsa_n = self._io.read_bytes(256)
            self._debug['img_rsa_n']['end'] = self._io.pos()
            self._debug['img_rsa_e']['start'] = self._io.pos()
            self.img_rsa_e = self._io.read_bytes(5)
            self._debug['img_rsa_e']['end'] = self._io.pos()
            self._debug['sml_aes_key']['start'] = self._io.pos()
            self.sml_aes_key = self._io.read_bytes(32)
            self._debug['sml_aes_key']['end'] = self._io.pos()
            self._debug['crypto_seed']['start'] = self._io.pos()
            self.crypto_seed = self._io.read_bytes(16)
            self._debug['crypto_seed']['end'] = self._io.pos()
            self._debug['sml_auth_rsa_n']['start'] = self._io.pos()
            self.sml_auth_rsa_n = self._io.read_bytes(256)
            self._debug['sml_auth_rsa_n']['end'] = self._io.pos()
            self._debug['sml_auth_rsa_e']['start'] = self._io.pos()
            self.sml_auth_rsa_e = self._io.read_bytes(5)
            self._debug['sml_auth_rsa_e']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class SecRom(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "platform_id", "project_id", "sec_ro_exists", "ofs_sec_ro", "len_sec_ro", "ofs_anti_clone", "len_anti_clone", "ofs_sec_cfg", "len_sec_cfg", "reserved", "sec_ctrl", "reserved_2", "secure_boot_partitions", "sec_key"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkSecromInfo.SecRom, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(16)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x41\x4E\x44\x5F\x52\x4F\x4D\x49\x4E\x46\x4F\x5F\x76\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x41\x4E\x44\x5F\x52\x4F\x4D\x49\x4E\x46\x4F\x5F\x76\x00\x00\x00", self.magic, self._io, u"/types/sec_rom/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 2:
                raise kaitaistruct.ValidationNotEqualError(2, self.version, self._io, u"/types/sec_rom/seq/1")
            self._debug['platform_id']['start'] = self._io.pos()
            self.platform_id = self._io.read_bytes(16)
            self._debug['platform_id']['end'] = self._io.pos()
            self._debug['project_id']['start'] = self._io.pos()
            self.project_id = self._io.read_bytes(16)
            self._debug['project_id']['end'] = self._io.pos()
            self._debug['sec_ro_exists']['start'] = self._io.pos()
            self.sec_ro_exists = self._io.read_u4le()
            self._debug['sec_ro_exists']['end'] = self._io.pos()
            self._debug['ofs_sec_ro']['start'] = self._io.pos()
            self.ofs_sec_ro = self._io.read_u4le()
            self._debug['ofs_sec_ro']['end'] = self._io.pos()
            self._debug['len_sec_ro']['start'] = self._io.pos()
            self.len_sec_ro = self._io.read_u4le()
            self._debug['len_sec_ro']['end'] = self._io.pos()
            self._debug['ofs_anti_clone']['start'] = self._io.pos()
            self.ofs_anti_clone = self._io.read_u4le()
            self._debug['ofs_anti_clone']['end'] = self._io.pos()
            if not self.ofs_anti_clone == 84:
                raise kaitaistruct.ValidationNotEqualError(84, self.ofs_anti_clone, self._io, u"/types/sec_rom/seq/7")
            self._debug['len_anti_clone']['start'] = self._io.pos()
            self.len_anti_clone = self._io.read_u4le()
            self._debug['len_anti_clone']['end'] = self._io.pos()
            if not self.len_anti_clone == 224:
                raise kaitaistruct.ValidationNotEqualError(224, self.len_anti_clone, self._io, u"/types/sec_rom/seq/8")
            self._debug['ofs_sec_cfg']['start'] = self._io.pos()
            self.ofs_sec_cfg = self._io.read_u4le()
            self._debug['ofs_sec_cfg']['end'] = self._io.pos()
            self._debug['len_sec_cfg']['start'] = self._io.pos()
            self.len_sec_cfg = self._io.read_u4le()
            self._debug['len_sec_cfg']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(128)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['sec_ctrl']['start'] = self._io.pos()
            self._raw_sec_ctrl = self._io.read_bytes(52)
            _io__raw_sec_ctrl = KaitaiStream(BytesIO(self._raw_sec_ctrl))
            self.sec_ctrl = MtkSecromInfo.SecCtrl(_io__raw_sec_ctrl, self, self._root)
            self._debug['sec_ctrl']['end'] = self._io.pos()
            self._debug['reserved_2']['start'] = self._io.pos()
            self.reserved_2 = self._io.read_bytes(18)
            self._debug['reserved_2']['end'] = self._io.pos()
            self._debug['secure_boot_partitions']['start'] = self._io.pos()
            self._raw_secure_boot_partitions = self._io.read_bytes(90)
            _io__raw_secure_boot_partitions = KaitaiStream(BytesIO(self._raw_secure_boot_partitions))
            self.secure_boot_partitions = MtkSecromInfo.SecureBootPartitions(_io__raw_secure_boot_partitions, self, self._root)
            self._debug['secure_boot_partitions']['end'] = self._io.pos()
            self._debug['sec_key']['start'] = self._io.pos()
            self._raw_sec_key = self._io.read_bytes(592)
            _io__raw_sec_key = KaitaiStream(BytesIO(self._raw_sec_key))
            self.sec_key = MtkSecromInfo.SecKey(_io__raw_sec_key, self, self._root)
            self._debug['sec_key']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.sec_ctrl._fetch_instances()
            self.secure_boot_partitions._fetch_instances()
            self.sec_key._fetch_instances()


    class SecureBootPartitions(KaitaiStruct):
        SEQ_FIELDS = ["name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkSecromInfo.SecureBootPartitions, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self._debug['name']['arr'] = []
            self.name = []
            for i in range(9):
                self._debug['name']['arr'].append({'start': self._io.pos()})
                self.name.append((KaitaiStream.bytes_terminate(self._io.read_bytes(10), 0, False)).decode(u"UTF-8"))
                self._debug['name']['arr'][i]['end'] = self._io.pos()

            self._debug['name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.name)):
                pass




