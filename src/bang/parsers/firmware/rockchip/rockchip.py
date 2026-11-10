# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Rockchip(KaitaiStruct):
    """
    .. seealso::
       Source - https://raw.githubusercontent.com/linux-rockchip/rkflashtool/0a5ad3a81/rkunpack.c
    """

    class ChipIdentifiers(IntEnum):
        rk3368 = 65
        rk29xx = 80
        rk30xx = 96
        rk31xx = 112
        rk32xx = 128
    SEQ_FIELDS = ["rockchip"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Rockchip, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['rockchip']['start'] = self._io.pos()
        _on = self.magic
        if _on == u"RKAF":
            pass
            self.rockchip = Rockchip.Rkaf(self._io, self, self._root)
        elif _on == u"RKFW":
            pass
            self.rockchip = Rockchip.Rkfw(self._io, self, self._root)
        self._debug['rockchip']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _on = self.magic
        if _on == u"RKAF":
            pass
            self.rockchip._fetch_instances()
        elif _on == u"RKFW":
            pass
            self.rockchip._fetch_instances()
        _ = self.magic
        if hasattr(self, '_m_magic'):
            pass


    class Rkaf(KaitaiStruct):
        SEQ_FIELDS = ["magic", "file_size", "unknown", "manufacturer", "num_files", "rockchip_files"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Rockchip.Rkaf, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x52\x4B\x41\x46":
                raise kaitaistruct.ValidationNotEqualError(b"\x52\x4B\x41\x46", self.magic, self._io, u"/types/rkaf/seq/0")
            self._debug['file_size']['start'] = self._io.pos()
            self.file_size = self._io.read_u4le()
            self._debug['file_size']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(64)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['manufacturer']['start'] = self._io.pos()
            self.manufacturer = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"UTF-8")
            self._debug['manufacturer']['end'] = self._io.pos()
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u4le()
            self._debug['num_files']['end'] = self._io.pos()
            _ = self.num_files
            if not self.num_files * 112 < self.file_size:
                raise kaitaistruct.ValidationExprError(self.num_files, self._io, u"/types/rkaf/seq/4")
            self._debug['rockchip_files']['start'] = self._io.pos()
            self._debug['rockchip_files']['arr'] = []
            self._raw_rockchip_files = []
            self.rockchip_files = []
            for i in range(self.num_files):
                self._debug['rockchip_files']['arr'].append({'start': self._io.pos()})
                self._raw_rockchip_files.append(self._io.read_bytes(112))
                _io__raw_rockchip_files = KaitaiStream(BytesIO(self._raw_rockchip_files[i]))
                self.rockchip_files.append(Rockchip.RockchipFile(_io__raw_rockchip_files, self, self._root))
                self._debug['rockchip_files']['arr'][i]['end'] = self._io.pos()

            self._debug['rockchip_files']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.rockchip_files)):
                pass
                self.rockchip_files[i]._fetch_instances()



    class Rkfw(KaitaiStruct):
        SEQ_FIELDS = ["magic", "unknown", "version", "unknown1", "date_information", "chip_id", "unknown2", "ofs_boot_image", "len_boot_image", "ofs_image", "len_image"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Rockchip.Rkfw, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x52\x4B\x46\x57":
                raise kaitaistruct.ValidationNotEqualError(b"\x52\x4B\x46\x57", self.magic, self._io, u"/types/rkfw/seq/0")
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(2)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_bytes(4)
            self._debug['version']['end'] = self._io.pos()
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_bytes(4)
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['date_information']['start'] = self._io.pos()
            self.date_information = self._io.read_bytes(7)
            self._debug['date_information']['end'] = self._io.pos()
            self._debug['chip_id']['start'] = self._io.pos()
            self.chip_id = KaitaiStream.resolve_enum(Rockchip.ChipIdentifiers, self._io.read_u1())
            self._debug['chip_id']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_bytes(3)
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['ofs_boot_image']['start'] = self._io.pos()
            self.ofs_boot_image = self._io.read_u4le()
            self._debug['ofs_boot_image']['end'] = self._io.pos()
            self._debug['len_boot_image']['start'] = self._io.pos()
            self.len_boot_image = self._io.read_u4le()
            self._debug['len_boot_image']['end'] = self._io.pos()
            self._debug['ofs_image']['start'] = self._io.pos()
            self.ofs_image = self._io.read_u4le()
            self._debug['ofs_image']['end'] = self._io.pos()
            self._debug['len_image']['start'] = self._io.pos()
            self.len_image = self._io.read_u4le()
            self._debug['len_image']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.boot_image
            if hasattr(self, '_m_boot_image'):
                pass

            _ = self.rkaf
            if hasattr(self, '_m_rkaf'):
                pass
                self._m_rkaf._fetch_instances()


        @property
        def boot_image(self):
            if hasattr(self, '_m_boot_image'):
                return self._m_boot_image

            _pos = self._io.pos()
            self._io.seek(self.ofs_boot_image)
            self._debug['_m_boot_image']['start'] = self._io.pos()
            self._m_boot_image = self._io.read_bytes(self.len_boot_image)
            self._debug['_m_boot_image']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_boot_image', None)

        @property
        def rkaf(self):
            if hasattr(self, '_m_rkaf'):
                return self._m_rkaf

            _pos = self._io.pos()
            self._io.seek(self.ofs_image)
            self._debug['_m_rkaf']['start'] = self._io.pos()
            self._raw__m_rkaf = self._io.read_bytes(self.len_image)
            _io__raw__m_rkaf = KaitaiStream(BytesIO(self._raw__m_rkaf))
            self._m_rkaf = Rockchip.Rkaf(_io__raw__m_rkaf, self, self._root)
            self._debug['_m_rkaf']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_rkaf', None)


    class RockchipFile(KaitaiStruct):
        SEQ_FIELDS = ["name", "path", "unknown", "ofs_image", "noff", "len_image", "len_file"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Rockchip.RockchipFile, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['path']['start'] = self._io.pos()
            self.path = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['path']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(32)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['ofs_image']['start'] = self._io.pos()
            self.ofs_image = self._io.read_u4le()
            self._debug['ofs_image']['end'] = self._io.pos()
            self._debug['noff']['start'] = self._io.pos()
            self.noff = self._io.read_u4le()
            self._debug['noff']['end'] = self._io.pos()
            self._debug['len_image']['start'] = self._io.pos()
            self.len_image = self._io.read_u4le()
            self._debug['len_image']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.data
            if hasattr(self, '_m_data'):
                pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            if self.ofs_image != 0:
                pass
                io = self._parent._io
                _pos = io.pos()
                io.seek(self.ofs_image)
                self._debug['_m_data']['start'] = io.pos()
                self._m_data = io.read_bytes(self.len_file)
                self._debug['_m_data']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_data', None)


    @property
    def magic(self):
        if hasattr(self, '_m_magic'):
            return self._m_magic

        _pos = self._io.pos()
        self._io.seek(0)
        self._debug['_m_magic']['start'] = self._io.pos()
        self._m_magic = (self._io.read_bytes(4)).decode(u"UTF-8")
        self._debug['_m_magic']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_magic', None)


