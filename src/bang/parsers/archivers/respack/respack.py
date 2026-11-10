# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Respack(KaitaiStruct):
    """Resource file found in CPB firmware archives, mostly used on older CoolPad
    phones and/or tablets. The only observed files are called "ResPack.cfg".
    
    Also used as by Baidu Maps. Test files (file extension: .rs) can be found in:
    <https://www.asus.com/mobile-handhelds/wearable-healthcare/asus-vivowatch/asus-vivowatch-5-hc-b05/helpdesk_download/?model2Name=ASUS-VivoWatch-5-HC-B05>
    """
    SEQ_FIELDS = ["header", "json"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Respack, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Respack.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['json']['start'] = self._io.pos()
        self.json = (self._io.read_bytes(self.header.len_json)).decode(u"UTF-8")
        self._debug['json']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "unknown", "len_json", "md5_bytes"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Respack.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x52\x53":
                raise kaitaistruct.ValidationNotEqualError(b"\x52\x53", self.magic, self._io, u"/types/header/seq/0")
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(8)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['len_json']['start'] = self._io.pos()
            self.len_json = self._io.read_u4le()
            self._debug['len_json']['end'] = self._io.pos()
            self._debug['md5_bytes']['start'] = self._io.pos()
            self.md5_bytes = self._io.read_bytes(32)
            self._debug['md5_bytes']['end'] = self._io.pos()
            _ = self.md5_bytes
            if not  ((KaitaiStream.byte_array_min(_) >= 48) and (KaitaiStream.byte_array_max(_) <= 102)) :
                raise kaitaistruct.ValidationExprError(self.md5_bytes, self._io, u"/types/header/seq/3")


        def _fetch_instances(self):
            pass

        @property
        def md5(self):
            if hasattr(self, '_m_md5'):
                return self._m_md5

            self._m_md5 = (self.md5_bytes).decode(u"ascii")
            return getattr(self, '_m_md5', None)



