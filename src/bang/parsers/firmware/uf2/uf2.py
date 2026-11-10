# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Uf2(KaitaiStruct):
    """UF2 is a file format, developed by Microsoft for PXT (also known as
    Microsoft MakeCode), that is particularly suitable for flashing
    microcontrollers over MSC (Mass Storage Class; aka removable flash drive).
    
    The list of family-ids is stored in a separate JSON file:
    
    <https://github.com/microsoft/uf2/blob/master/utils/uf2families.json>
    
    This file is regularly updated and the family_id enum should be kept in
    sync with this JSON file.
    
    Test files can be found on the MicroPython website:
    
    <https://micropython.org/download/rp2-pico/>
    
    .. seealso::
       Source - https://github.com/microsoft/uf2/blob/b05acf5/README.md
    """

    class FamilyId(IntEnum):
        stm32l4 = 16738585
        stm32l5 = 69471199
        stm32f411xc = 114362747
        m0sense = 299792458
        atmega32 = 374814231
        saml21 = 407992330
        nrf52 = 458716255
        esp32 = 475996592
        stm32l1 = 505365293
        stm32l0 = 539900561
        stm32wl = 558239728
        rtl8710b = 585160444
        lpc55 = 716994540
        esp32c2 = 730387100
        stm32f411xe = 767756741
        stm32g0 = 806311475
        esp32s31 = 822212545
        gd32f350 = 835856582
        esp32h2 = 858203894
        rtl8720d = 863621090
        esp32p4 = 1026592404
        maixplayu4 = 1265126769
        stm32g4 = 1282483210
        stm32h5 = 1318001757
        csk4 = 1332399698
        mimxrt10xx = 1337120189
        xr809 = 1374225320
        stm32f7 = 1404571392
        esp32c6 = 1410195298
        samd51 = 1427194976
        stm32f4 = 1467308631
        fx2 = 1511523995
        stm32f2 = 1561987630
        stm32f1 = 1591873650
        nrf52833 = 1646171002
        stm32f0 = 1685595318
        bk7231u = 1733968048
        samd21 = 1760373640
        ch32v = 1771791084
        bk7251 = 1786956866
        stm32f3 = 1803837832
        stm32f407 = 1829315322
        stm32h7 = 1840668802
        csk6 = 1853049000
        nrf52832xxab = 1869948536
        stm32wb = 1892771411
        nrf52832xxaa = 1920081230
        max32690 = 1947226634
        esp32c61 = 2010665156
        bk7231n = 2067722800
        ra4m1 = 2078840685
        py32f071_uvk5_v3 = 2105173743
        esp8266 = 2125160941
        kl32l2 = 2139350931
        nrf52820 = 2181929567
        stm32f407vg = 2410701054
        max78002 = 2446589208
        rza1lu = 2501329455
        gd32vf103 = 2599435827
        esp32h4 = 2651564682
        rtl8710a = 2684343619
        at32f415 = 2697558926
        nrf52840 = 2913282112
        esp32h21 = 3067936943
        esp32s2 = 3218951918
        esp32s3 = 3296614247
        esp32c3 = 3559628908
        max32650 = 3594487346
        bl602 = 3725750455
        rtl8720c = 3767498084
        rp2040 = 3834380118
        rp2xxx_absolute = 3834380119
        rp2xxx_data = 3834380120
        rp2350_arm_s = 3834380121
        rp2350_riscv = 3834380122
        rp2350_arm_ns = 3834380123
        max32666 = 4039314801
        esp32c5 = 4145808195
    SEQ_FIELDS = ["uf2_block_start", "uf2_blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Uf2, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['uf2_block_start']['start'] = self._io.pos()
        self.uf2_block_start = Uf2.Uf2Block(self._io, self, self._root)
        self._debug['uf2_block_start']['end'] = self._io.pos()
        self._debug['uf2_blocks']['start'] = self._io.pos()
        self._debug['uf2_blocks']['arr'] = []
        self.uf2_blocks = []
        for i in range(self.uf2_block_start.num_blocks - 1):
            self._debug['uf2_blocks']['arr'].append({'start': self._io.pos()})
            self.uf2_blocks.append(Uf2.Uf2Block(self._io, self, self._root))
            self._debug['uf2_blocks']['arr'][i]['end'] = self._io.pos()

        self._debug['uf2_blocks']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.uf2_block_start._fetch_instances()
        for i in range(len(self.uf2_blocks)):
            pass
            self.uf2_blocks[i]._fetch_instances()


    class Uf2Block(KaitaiStruct):
        SEQ_FIELDS = ["magic", "second_magic", "flags", "target_address", "len_payload", "block_number", "num_blocks", "file_size", "family_id", "data", "end_magic"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Uf2.Uf2Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x55\x46\x32\x0A":
                raise kaitaistruct.ValidationNotEqualError(b"\x55\x46\x32\x0A", self.magic, self._io, u"/types/uf2_block/seq/0")
            self._debug['second_magic']['start'] = self._io.pos()
            self.second_magic = self._io.read_bytes(4)
            self._debug['second_magic']['end'] = self._io.pos()
            if not self.second_magic == b"\x57\x51\x5D\x9E":
                raise kaitaistruct.ValidationNotEqualError(b"\x57\x51\x5D\x9E", self.second_magic, self._io, u"/types/uf2_block/seq/1")
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['target_address']['start'] = self._io.pos()
            self.target_address = self._io.read_u4le()
            self._debug['target_address']['end'] = self._io.pos()
            self._debug['len_payload']['start'] = self._io.pos()
            self.len_payload = self._io.read_u4le()
            self._debug['len_payload']['end'] = self._io.pos()
            self._debug['block_number']['start'] = self._io.pos()
            self.block_number = self._io.read_u4le()
            self._debug['block_number']['end'] = self._io.pos()
            self._debug['num_blocks']['start'] = self._io.pos()
            self.num_blocks = self._io.read_u4le()
            self._debug['num_blocks']['end'] = self._io.pos()
            if self.flags & 8192 == 0:
                pass
                self._debug['file_size']['start'] = self._io.pos()
                self.file_size = self._io.read_u4le()
                self._debug['file_size']['end'] = self._io.pos()

            if self.flags & 8192 != 0:
                pass
                self._debug['family_id']['start'] = self._io.pos()
                self.family_id = KaitaiStream.resolve_enum(Uf2.FamilyId, self._io.read_u4le())
                self._debug['family_id']['end'] = self._io.pos()

            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(476)
            self._debug['data']['end'] = self._io.pos()
            self._debug['end_magic']['start'] = self._io.pos()
            self.end_magic = self._io.read_bytes(4)
            self._debug['end_magic']['end'] = self._io.pos()
            if not self.end_magic == b"\x30\x6F\xB1\x0A":
                raise kaitaistruct.ValidationNotEqualError(b"\x30\x6F\xB1\x0A", self.end_magic, self._io, u"/types/uf2_block/seq/10")


        def _fetch_instances(self):
            pass
            if self.flags & 8192 == 0:
                pass

            if self.flags & 8192 != 0:
                pass




