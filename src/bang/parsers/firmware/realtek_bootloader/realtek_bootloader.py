# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class RealtekBootloader(KaitaiStruct):
    """Realtek RTL8198 and RTL8196C related. The docs do not always fully correspond
    to devices seen in the wild.
    
    .. seealso::
       Source - https://github.com/krzys-h/8level-WRT-1200AC-firmware-tools
    
    
    .. seealso::
       Source - https://github.com/jameshilliard/WECB-VZ-GPL/blob/master/rtl819x/bootcode/boot/init/rtk.h
    """

    class Signatures(IntEnum):
        cr6c = 1668429411
        r6cr = 1916167026
    SEQ_FIELDS = ["header", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(RealtekBootloader, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = RealtekBootloader.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self.data = self._io.read_bytes(self.header.len_data)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["signature", "load_address", "flash_memory_address", "len_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(RealtekBootloader.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = KaitaiStream.resolve_enum(RealtekBootloader.Signatures, self._io.read_u4be())
            self._debug['signature']['end'] = self._io.pos()
            if not  ((self.signature == RealtekBootloader.Signatures.cr6c) or (self.signature == RealtekBootloader.Signatures.r6cr)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.signature, self._io, u"/types/header/seq/0")
            self._debug['load_address']['start'] = self._io.pos()
            self.load_address = self._io.read_u4be()
            self._debug['load_address']['end'] = self._io.pos()
            self._debug['flash_memory_address']['start'] = self._io.pos()
            self.flash_memory_address = self._io.read_u4be()
            self._debug['flash_memory_address']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4be()
            self._debug['len_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



