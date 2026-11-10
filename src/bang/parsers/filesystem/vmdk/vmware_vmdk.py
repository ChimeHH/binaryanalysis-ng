# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class VmwareVmdk(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/libyal/libvmdk/blob/master/documentation/VMWare%20Virtual%20Disk%20Format%20(VMDK).asciidoc#41-file-header
    
    
    .. seealso::
       Source - https://web.archive.org/web/20210308200012/https://www.vmware.com/support/developer/vddk/vmdk_50_technote.pdf
    
    
    .. seealso::
       Source - https://www.vmware.com/app/vmdk/?src=vmdk
    """

    class CompressionMethods(IntEnum):
        none = 0
        deflate = 1
    SEQ_FIELDS = ["header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(VmwareVmdk, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(self.len_sector)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = VmwareVmdk.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "flags", "size_max", "size_grain", "start_descriptor", "size_descriptor", "num_grain_table_entries", "start_secondary_grain", "start_primary_grain", "size_metadata", "is_dirty", "error_detection", "compression_method"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VmwareVmdk.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x4B\x44\x4D\x56":
                raise kaitaistruct.ValidationNotEqualError(b"\x4B\x44\x4D\x56", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            if not  ((self.version == 1) or (self.version == 2) or (self.version == 3)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/types/header/seq/1")
            self._debug['flags']['start'] = self._io.pos()
            self.flags = VmwareVmdk.HeaderFlags(self._io, self, self._root)
            self._debug['flags']['end'] = self._io.pos()
            self._debug['size_max']['start'] = self._io.pos()
            self.size_max = self._io.read_u8le()
            self._debug['size_max']['end'] = self._io.pos()
            self._debug['size_grain']['start'] = self._io.pos()
            self.size_grain = self._io.read_u8le()
            self._debug['size_grain']['end'] = self._io.pos()
            if not self.size_grain >= 8:
                raise kaitaistruct.ValidationLessThanError(8, self.size_grain, self._io, u"/types/header/seq/4")
            self._debug['start_descriptor']['start'] = self._io.pos()
            self.start_descriptor = self._io.read_u8le()
            self._debug['start_descriptor']['end'] = self._io.pos()
            self._debug['size_descriptor']['start'] = self._io.pos()
            self.size_descriptor = self._io.read_u8le()
            self._debug['size_descriptor']['end'] = self._io.pos()
            self._debug['num_grain_table_entries']['start'] = self._io.pos()
            self.num_grain_table_entries = self._io.read_u4le()
            self._debug['num_grain_table_entries']['end'] = self._io.pos()
            self._debug['start_secondary_grain']['start'] = self._io.pos()
            self.start_secondary_grain = self._io.read_u8le()
            self._debug['start_secondary_grain']['end'] = self._io.pos()
            self._debug['start_primary_grain']['start'] = self._io.pos()
            self.start_primary_grain = self._io.read_u8le()
            self._debug['start_primary_grain']['end'] = self._io.pos()
            self._debug['size_metadata']['start'] = self._io.pos()
            self.size_metadata = self._io.read_u8le()
            self._debug['size_metadata']['end'] = self._io.pos()
            self._debug['is_dirty']['start'] = self._io.pos()
            self.is_dirty = self._io.read_u1()
            self._debug['is_dirty']['end'] = self._io.pos()
            self._debug['error_detection']['start'] = self._io.pos()
            self.error_detection = VmwareVmdk.Header.ErrorDetection(self._io, self, self._root)
            self._debug['error_detection']['end'] = self._io.pos()
            self._debug['compression_method']['start'] = self._io.pos()
            self.compression_method = KaitaiStream.resolve_enum(VmwareVmdk.CompressionMethods, self._io.read_u2le())
            self._debug['compression_method']['end'] = self._io.pos()
            if not  ((self.compression_method == VmwareVmdk.CompressionMethods.none) or (self.compression_method == VmwareVmdk.CompressionMethods.deflate)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.compression_method, self._io, u"/types/header/seq/13")


        def _fetch_instances(self):
            pass
            self.flags._fetch_instances()
            self.error_detection._fetch_instances()
            _ = self.descriptor
            if hasattr(self, '_m_descriptor'):
                pass

            _ = self.grain_primary
            if hasattr(self, '_m_grain_primary'):
                pass

            _ = self.grain_secondary
            if hasattr(self, '_m_grain_secondary'):
                pass


        class ErrorDetection(KaitaiStruct):
            """Four entries are used to detect when an extent file has been
            corrupted by transferring it using FTP in text mode.
            """
            SEQ_FIELDS = ["single_end_line_char", "non_end_line_char", "double_end_line_char1", "double_end_line_char2"]
            def __init__(self, _io, _parent=None, _root=None):
                super(VmwareVmdk.Header.ErrorDetection, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['single_end_line_char']['start'] = self._io.pos()
                self.single_end_line_char = self._io.read_bytes(1)
                self._debug['single_end_line_char']['end'] = self._io.pos()
                if not self.single_end_line_char == b"\x0A":
                    raise kaitaistruct.ValidationNotEqualError(b"\x0A", self.single_end_line_char, self._io, u"/types/header/types/error_detection/seq/0")
                self._debug['non_end_line_char']['start'] = self._io.pos()
                self.non_end_line_char = self._io.read_bytes(1)
                self._debug['non_end_line_char']['end'] = self._io.pos()
                if not self.non_end_line_char == b"\x20":
                    raise kaitaistruct.ValidationNotEqualError(b"\x20", self.non_end_line_char, self._io, u"/types/header/types/error_detection/seq/1")
                self._debug['double_end_line_char1']['start'] = self._io.pos()
                self.double_end_line_char1 = self._io.read_bytes(1)
                self._debug['double_end_line_char1']['end'] = self._io.pos()
                if not self.double_end_line_char1 == b"\x0D":
                    raise kaitaistruct.ValidationNotEqualError(b"\x0D", self.double_end_line_char1, self._io, u"/types/header/types/error_detection/seq/2")
                self._debug['double_end_line_char2']['start'] = self._io.pos()
                self.double_end_line_char2 = self._io.read_bytes(1)
                self._debug['double_end_line_char2']['end'] = self._io.pos()
                if not self.double_end_line_char2 == b"\x0A":
                    raise kaitaistruct.ValidationNotEqualError(b"\x0A", self.double_end_line_char2, self._io, u"/types/header/types/error_detection/seq/3")


            def _fetch_instances(self):
                pass


        @property
        def descriptor(self):
            if hasattr(self, '_m_descriptor'):
                return self._m_descriptor

            if (not (self.start_descriptor == 0)):
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.start_descriptor * self._root.len_sector)
                self._debug['_m_descriptor']['start'] = io.pos()
                self._m_descriptor = (io.read_bytes(self.size_descriptor * self._root.len_sector)).decode(u"UTF-8")
                self._debug['_m_descriptor']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_descriptor', None)

        @property
        def gd_at_end(self):
            if hasattr(self, '_m_gd_at_end'):
                return self._m_gd_at_end

            self._m_gd_at_end = self.start_primary_grain == 18446744073709551615
            return getattr(self, '_m_gd_at_end', None)

        @property
        def grain_primary(self):
            if hasattr(self, '_m_grain_primary'):
                return self._m_grain_primary

            if  (((not (self.flags.use_secondary_grain_dir))) and ((not (self.gd_at_end)))) :
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.start_primary_grain * self._root.len_sector)
                self._debug['_m_grain_primary']['start'] = io.pos()
                self._m_grain_primary = io.read_bytes(self.size_grain * self._root.len_sector)
                self._debug['_m_grain_primary']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_grain_primary', None)

        @property
        def grain_secondary(self):
            if hasattr(self, '_m_grain_secondary'):
                return self._m_grain_secondary

            if (not (self.start_secondary_grain == 0)):
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.start_secondary_grain * self._root.len_sector)
                self._debug['_m_grain_secondary']['start'] = io.pos()
                self._m_grain_secondary = io.read_bytes(self.size_grain * self._root.len_sector)
                self._debug['_m_grain_secondary']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_grain_secondary', None)


    class HeaderFlags(KaitaiStruct):
        """
        .. seealso::
           Source - https://github.com/libyal/libvmdk/blob/master/documentation/VMWare%20Virtual%20Disk%20Format%20(VMDK).asciidoc#411-flags
        """
        SEQ_FIELDS = ["reserved1", "zeroed_grain_table_entry", "use_secondary_grain_dir", "valid_new_line_detection_test", "reserved2", "reserved3", "has_metadata", "has_compressed_grain", "reserved4"]
        def __init__(self, _io, _parent=None, _root=None):
            super(VmwareVmdk.HeaderFlags, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bits_int_be(5)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['zeroed_grain_table_entry']['start'] = self._io.pos()
            self.zeroed_grain_table_entry = self._io.read_bits_int_be(1) != 0
            self._debug['zeroed_grain_table_entry']['end'] = self._io.pos()
            self._debug['use_secondary_grain_dir']['start'] = self._io.pos()
            self.use_secondary_grain_dir = self._io.read_bits_int_be(1) != 0
            self._debug['use_secondary_grain_dir']['end'] = self._io.pos()
            self._debug['valid_new_line_detection_test']['start'] = self._io.pos()
            self.valid_new_line_detection_test = self._io.read_bits_int_be(1) != 0
            self._debug['valid_new_line_detection_test']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_u1()
            self._debug['reserved2']['end'] = self._io.pos()
            self._debug['reserved3']['start'] = self._io.pos()
            self.reserved3 = self._io.read_bits_int_be(6)
            self._debug['reserved3']['end'] = self._io.pos()
            self._debug['has_metadata']['start'] = self._io.pos()
            self.has_metadata = self._io.read_bits_int_be(1) != 0
            self._debug['has_metadata']['end'] = self._io.pos()
            self._debug['has_compressed_grain']['start'] = self._io.pos()
            self.has_compressed_grain = self._io.read_bits_int_be(1) != 0
            self._debug['has_compressed_grain']['end'] = self._io.pos()
            self._debug['reserved4']['start'] = self._io.pos()
            self.reserved4 = self._io.read_u1()
            self._debug['reserved4']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def len_sector(self):
        if hasattr(self, '_m_len_sector'):
            return self._m_len_sector

        self._m_len_sector = 512
        return getattr(self, '_m_len_sector', None)


