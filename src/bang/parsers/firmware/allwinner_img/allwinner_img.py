# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class AllwinnerImg(KaitaiStruct):
    """Format of boot files found on certain Android devices based on Allwinner chipsets.
    
    .. seealso::
       Source - https://github.com/Ithamar/awutils/blob/5d6284e/imagewty.h
    """
    SEQ_FIELDS = ["img_header", "file_headers"]
    def __init__(self, _io, _parent=None, _root=None):
        super(AllwinnerImg, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['img_header']['start'] = self._io.pos()
        self._raw_img_header = self._io.read_bytes(1024)
        _io__raw_img_header = KaitaiStream(BytesIO(self._raw_img_header))
        self.img_header = AllwinnerImg.Header(_io__raw_img_header, self, self._root)
        self._debug['img_header']['end'] = self._io.pos()
        self._debug['file_headers']['start'] = self._io.pos()
        self._debug['file_headers']['arr'] = []
        self.file_headers = []
        for i in range(self.img_header.num_files):
            self._debug['file_headers']['arr'].append({'start': self._io.pos()})
            self.file_headers.append(AllwinnerImg.FileHeader(self._io, self, self._root))
            self._debug['file_headers']['arr'][i]['end'] = self._io.pos()

        self._debug['file_headers']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.img_header._fetch_instances()
        for i in range(len(self.file_headers)):
            pass
            self.file_headers[i]._fetch_instances()


    class FileHeader(KaitaiStruct):
        SEQ_FIELDS = ["common", "file_header_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AllwinnerImg.FileHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['common']['start'] = self._io.pos()
            self.common = AllwinnerImg.FileHeaderCommon(self._io, self, self._root)
            self._debug['common']['end'] = self._io.pos()
            self._debug['file_header_data']['start'] = self._io.pos()
            _on = self._root.img_header.header_version
            if _on == 256:
                pass
                self._raw_file_header_data = self._io.read_bytes(self.common.len_header_total - 32)
                _io__raw_file_header_data = KaitaiStream(BytesIO(self._raw_file_header_data))
                self.file_header_data = AllwinnerImg.FileHeaderV1(_io__raw_file_header_data, self, self._root)
            elif _on == 768:
                pass
                self._raw_file_header_data = self._io.read_bytes(self.common.len_header_total - 32)
                _io__raw_file_header_data = KaitaiStream(BytesIO(self._raw_file_header_data))
                self.file_header_data = AllwinnerImg.FileHeaderV3(_io__raw_file_header_data, self, self._root)
            else:
                pass
                self.file_header_data = self._io.read_bytes(self.common.len_header_total - 32)
            self._debug['file_header_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.common._fetch_instances()
            _on = self._root.img_header.header_version
            if _on == 256:
                pass
                self.file_header_data._fetch_instances()
            elif _on == 768:
                pass
                self.file_header_data._fetch_instances()
            else:
                pass


    class FileHeaderCommon(KaitaiStruct):
        SEQ_FIELDS = ["len_filename", "len_header_total", "maintype", "subtype"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AllwinnerImg.FileHeaderCommon, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_filename']['start'] = self._io.pos()
            self.len_filename = self._io.read_u4le()
            self._debug['len_filename']['end'] = self._io.pos()
            self._debug['len_header_total']['start'] = self._io.pos()
            self.len_header_total = self._io.read_u4le()
            self._debug['len_header_total']['end'] = self._io.pos()
            self._debug['maintype']['start'] = self._io.pos()
            self.maintype = (self._io.read_bytes(8)).decode(u"ASCII")
            self._debug['maintype']['end'] = self._io.pos()
            self._debug['subtype']['start'] = self._io.pos()
            self.subtype = (self._io.read_bytes(16)).decode(u"ASCII")
            self._debug['subtype']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class FileHeaderV1(KaitaiStruct):
        SEQ_FIELDS = ["unknown_1", "stored_length", "original_length", "offset", "unknown_2", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AllwinnerImg.FileHeaderV1, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['unknown_1']['start'] = self._io.pos()
            self.unknown_1 = self._io.read_u4le()
            self._debug['unknown_1']['end'] = self._io.pos()
            self._debug['stored_length']['start'] = self._io.pos()
            self.stored_length = self._io.read_u4le()
            self._debug['stored_length']['end'] = self._io.pos()
            self._debug['original_length']['start'] = self._io.pos()
            self.original_length = self._io.read_u4le()
            self._debug['original_length']['end'] = self._io.pos()
            self._debug['offset']['start'] = self._io.pos()
            self.offset = self._io.read_u4le()
            self._debug['offset']['end'] = self._io.pos()
            self._debug['unknown_2']['start'] = self._io.pos()
            self.unknown_2 = self._io.read_u4le()
            self._debug['unknown_2']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class FileHeaderV3(KaitaiStruct):
        SEQ_FIELDS = ["unknown_0", "name", "stored_length", "pad1", "original_length", "pad2", "offset"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AllwinnerImg.FileHeaderV3, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['unknown_0']['start'] = self._io.pos()
            self.unknown_0 = self._io.read_u4le()
            self._debug['unknown_0']['end'] = self._io.pos()
            if not self.unknown_0 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.unknown_0, self._io, u"/types/file_header_v3/seq/0")
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"ASCII")
            self._debug['name']['end'] = self._io.pos()
            self._debug['stored_length']['start'] = self._io.pos()
            self.stored_length = self._io.read_u4le()
            self._debug['stored_length']['end'] = self._io.pos()
            self._debug['pad1']['start'] = self._io.pos()
            self.pad1 = self._io.read_bytes(4)
            self._debug['pad1']['end'] = self._io.pos()
            self._debug['original_length']['start'] = self._io.pos()
            self.original_length = self._io.read_u4le()
            self._debug['original_length']['end'] = self._io.pos()
            self._debug['pad2']['start'] = self._io.pos()
            self.pad2 = self._io.read_bytes(4)
            self._debug['pad2']['end'] = self._io.pos()
            self._debug['offset']['start'] = self._io.pos()
            self.offset = self._io.read_u4le()
            self._debug['offset']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "header_version", "len_header", "ram_base", "format_version", "len_image", "len_image_header", "unknown", "usb_pid", "usb_vid", "hardware_id", "firmware_id", "val1", "val1024_1", "num_files", "val1024_2", "val0_1", "val0_2", "val0_3", "val0_4"]
        def __init__(self, _io, _parent=None, _root=None):
            super(AllwinnerImg.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(8)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x49\x4D\x41\x47\x45\x57\x54\x59":
                raise kaitaistruct.ValidationNotEqualError(b"\x49\x4D\x41\x47\x45\x57\x54\x59", self.magic, self._io, u"/types/header/seq/0")
            self._debug['header_version']['start'] = self._io.pos()
            self.header_version = self._io.read_u4le()
            self._debug['header_version']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['ram_base']['start'] = self._io.pos()
            self.ram_base = self._io.read_u4le()
            self._debug['ram_base']['end'] = self._io.pos()
            self._debug['format_version']['start'] = self._io.pos()
            self.format_version = self._io.read_u4le()
            self._debug['format_version']['end'] = self._io.pos()
            if not self.format_version == 1049140:
                raise kaitaistruct.ValidationNotEqualError(1049140, self.format_version, self._io, u"/types/header/seq/4")
            self._debug['len_image']['start'] = self._io.pos()
            self.len_image = self._io.read_u4le()
            self._debug['len_image']['end'] = self._io.pos()
            self._debug['len_image_header']['start'] = self._io.pos()
            self.len_image_header = self._io.read_u4le()
            self._debug['len_image_header']['end'] = self._io.pos()
            if self.header_version == 768:
                pass
                self._debug['unknown']['start'] = self._io.pos()
                self.unknown = self._io.read_u4le()
                self._debug['unknown']['end'] = self._io.pos()

            self._debug['usb_pid']['start'] = self._io.pos()
            self.usb_pid = self._io.read_u4le()
            self._debug['usb_pid']['end'] = self._io.pos()
            self._debug['usb_vid']['start'] = self._io.pos()
            self.usb_vid = self._io.read_u4le()
            self._debug['usb_vid']['end'] = self._io.pos()
            self._debug['hardware_id']['start'] = self._io.pos()
            self.hardware_id = self._io.read_u4le()
            self._debug['hardware_id']['end'] = self._io.pos()
            self._debug['firmware_id']['start'] = self._io.pos()
            self.firmware_id = self._io.read_u4le()
            self._debug['firmware_id']['end'] = self._io.pos()
            self._debug['val1']['start'] = self._io.pos()
            self.val1 = self._io.read_u4le()
            self._debug['val1']['end'] = self._io.pos()
            if not self.val1 == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.val1, self._io, u"/types/header/seq/12")
            self._debug['val1024_1']['start'] = self._io.pos()
            self.val1024_1 = self._io.read_u4le()
            self._debug['val1024_1']['end'] = self._io.pos()
            if not self.val1024_1 == 1024:
                raise kaitaistruct.ValidationNotEqualError(1024, self.val1024_1, self._io, u"/types/header/seq/13")
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u4le()
            self._debug['num_files']['end'] = self._io.pos()
            self._debug['val1024_2']['start'] = self._io.pos()
            self.val1024_2 = self._io.read_u4le()
            self._debug['val1024_2']['end'] = self._io.pos()
            if not self.val1024_2 == 1024:
                raise kaitaistruct.ValidationNotEqualError(1024, self.val1024_2, self._io, u"/types/header/seq/15")
            self._debug['val0_1']['start'] = self._io.pos()
            self.val0_1 = self._io.read_u4le()
            self._debug['val0_1']['end'] = self._io.pos()
            if not self.val0_1 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.val0_1, self._io, u"/types/header/seq/16")
            self._debug['val0_2']['start'] = self._io.pos()
            self.val0_2 = self._io.read_u4le()
            self._debug['val0_2']['end'] = self._io.pos()
            if not self.val0_2 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.val0_2, self._io, u"/types/header/seq/17")
            self._debug['val0_3']['start'] = self._io.pos()
            self.val0_3 = self._io.read_u4le()
            self._debug['val0_3']['end'] = self._io.pos()
            if not self.val0_3 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.val0_3, self._io, u"/types/header/seq/18")
            self._debug['val0_4']['start'] = self._io.pos()
            self.val0_4 = self._io.read_u4le()
            self._debug['val0_4']['end'] = self._io.pos()
            if not self.val0_4 == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.val0_4, self._io, u"/types/header/seq/19")


        def _fetch_instances(self):
            pass
            if self.header_version == 768:
                pass




