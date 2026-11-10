# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Aboot(KaitaiStruct):
    """A not so well documented format for aboot files, which can be found
    on some Android devices. This grammar only supports version 3 but not
    the `unified boot` version.
    
    Test file: hammerhead-krt16m-factory-fb4041cc.zip
    
    Version 2:
    
    * qsd8250_ffa
    * qsd8250_surf
    * qsd8650a_st1x
    
    Version 3:
    
    * apq8084
    * fsm9010
    * fsm9900
    * mdm9615
    * mdm9625
    * mdm9635
    * msm7627a
    * msm7627_surf
    * msm7630_surf
    * msm8226
    * msm8610
    * msm8660_surf
    * msm8960
    * msm8974
    
    .. seealso::
       Source - https://source.codeaurora.org/quic/la/kernel/lk/tree/target/msm8974/tools/mkheader.c?h=master&id=82117399ba17ea60b7f771c641ff5b1c9283bdc9#n161
    """
    SEQ_FIELDS = ["appsbl", "version", "image_source_pointer", "image_destination_pointer", "len_image", "len_code", "magic6", "len_signature", "magic8", "len_certificate_chain", "image"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Aboot, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['appsbl']['start'] = self._io.pos()
        self.appsbl = self._io.read_u4le()
        self._debug['appsbl']['end'] = self._io.pos()
        if not self.appsbl == 5:
            raise kaitaistruct.ValidationNotEqualError(5, self.appsbl, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        if not self.version == 3:
            raise kaitaistruct.ValidationNotEqualError(3, self.version, self._io, u"/seq/1")
        self._debug['image_source_pointer']['start'] = self._io.pos()
        self.image_source_pointer = self._io.read_u4le()
        self._debug['image_source_pointer']['end'] = self._io.pos()
        if not self.image_source_pointer == 0:
            raise kaitaistruct.ValidationNotEqualError(0, self.image_source_pointer, self._io, u"/seq/2")
        self._debug['image_destination_pointer']['start'] = self._io.pos()
        self.image_destination_pointer = self._io.read_u4le()
        self._debug['image_destination_pointer']['end'] = self._io.pos()
        self._debug['len_image']['start'] = self._io.pos()
        self.len_image = self._io.read_u4le()
        self._debug['len_image']['end'] = self._io.pos()
        self._debug['len_code']['start'] = self._io.pos()
        self.len_code = self._io.read_u4le()
        self._debug['len_code']['end'] = self._io.pos()
        self._debug['magic6']['start'] = self._io.pos()
        self.magic6 = self._io.read_u4le()
        self._debug['magic6']['end'] = self._io.pos()
        self._debug['len_signature']['start'] = self._io.pos()
        self.len_signature = self._io.read_u4le()
        self._debug['len_signature']['end'] = self._io.pos()
        self._debug['magic8']['start'] = self._io.pos()
        self.magic8 = self._io.read_u4le()
        self._debug['magic8']['end'] = self._io.pos()
        self._debug['len_certificate_chain']['start'] = self._io.pos()
        self.len_certificate_chain = self._io.read_u4le()
        self._debug['len_certificate_chain']['end'] = self._io.pos()
        self._debug['image']['start'] = self._io.pos()
        self._raw_image = self._io.read_bytes(self.len_image)
        _io__raw_image = KaitaiStream(BytesIO(self._raw_image))
        self.image = Aboot.Image(_io__raw_image, self, self._root)
        self._debug['image']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.image._fetch_instances()

    class Image(KaitaiStruct):
        SEQ_FIELDS = ["raw_appsbl", "signature", "certificate_chain"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aboot.Image, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['raw_appsbl']['start'] = self._io.pos()
            self.raw_appsbl = self._io.read_bytes(self._root.len_code)
            self._debug['raw_appsbl']['end'] = self._io.pos()
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(self._root.len_signature)
            self._debug['signature']['end'] = self._io.pos()
            self._debug['certificate_chain']['start'] = self._io.pos()
            self.certificate_chain = self._io.read_bytes(self._root.len_certificate_chain)
            self._debug['certificate_chain']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



