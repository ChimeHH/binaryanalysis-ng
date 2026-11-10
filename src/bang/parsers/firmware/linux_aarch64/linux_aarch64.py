# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class LinuxAarch64(KaitaiStruct):
    """
    .. seealso::
       Source - https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/Documentation/arch/arm64/booting.rst?h=v6.5
    """
    SEQ_FIELDS = ["code0", "code1", "ofs_text", "effective_image_size", "flags", "reserved_2", "reserved_3", "reserved_4", "magic", "reserved_5"]
    def __init__(self, _io, _parent=None, _root=None):
        super(LinuxAarch64, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['code0']['start'] = self._io.pos()
        self.code0 = self._io.read_u4le()
        self._debug['code0']['end'] = self._io.pos()
        self._debug['code1']['start'] = self._io.pos()
        self.code1 = self._io.read_u4le()
        self._debug['code1']['end'] = self._io.pos()
        self._debug['ofs_text']['start'] = self._io.pos()
        self.ofs_text = self._io.read_u8le()
        self._debug['ofs_text']['end'] = self._io.pos()
        self._debug['effective_image_size']['start'] = self._io.pos()
        self.effective_image_size = self._io.read_u8le()
        self._debug['effective_image_size']['end'] = self._io.pos()
        self._debug['flags']['start'] = self._io.pos()
        self._raw_flags = self._io.read_bytes(8)
        _io__raw_flags = KaitaiStream(BytesIO(self._raw_flags))
        self.flags = LinuxAarch64.Flags(_io__raw_flags, self, self._root)
        self._debug['flags']['end'] = self._io.pos()
        self._debug['reserved_2']['start'] = self._io.pos()
        self.reserved_2 = self._io.read_u8le()
        self._debug['reserved_2']['end'] = self._io.pos()
        self._debug['reserved_3']['start'] = self._io.pos()
        self.reserved_3 = self._io.read_u8le()
        self._debug['reserved_3']['end'] = self._io.pos()
        self._debug['reserved_4']['start'] = self._io.pos()
        self.reserved_4 = self._io.read_u8le()
        self._debug['reserved_4']['end'] = self._io.pos()
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x41\x52\x4D\x64":
            raise kaitaistruct.ValidationNotEqualError(b"\x41\x52\x4D\x64", self.magic, self._io, u"/seq/8")
        self._debug['reserved_5']['start'] = self._io.pos()
        self.reserved_5 = self._io.read_u4le()
        self._debug['reserved_5']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.flags._fetch_instances()

    class Flags(KaitaiStruct):
        SEQ_FIELDS = ["endianness", "page_size", "physical_placement"]
        def __init__(self, _io, _parent=None, _root=None):
            super(LinuxAarch64.Flags, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['endianness']['start'] = self._io.pos()
            self.endianness = self._io.read_bits_int_le(1) != 0
            self._debug['endianness']['end'] = self._io.pos()
            self._debug['page_size']['start'] = self._io.pos()
            self.page_size = self._io.read_bits_int_le(2)
            self._debug['page_size']['end'] = self._io.pos()
            self._debug['physical_placement']['start'] = self._io.pos()
            self.physical_placement = self._io.read_bits_int_le(1) != 0
            self._debug['physical_placement']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



