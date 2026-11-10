# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Cab(KaitaiStruct):
    """
    .. seealso::
       Source - https://download.microsoft.com/download/4/d/a/4da14f27-b4ef-4170-a6e6-5b1ef85b1baa/[ms-cab].pdf
    """
    SEQ_FIELDS = ["preheader", "cab_data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Cab, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['preheader']['start'] = self._io.pos()
        self.preheader = Cab.Preheader(self._io, self, self._root)
        self._debug['preheader']['end'] = self._io.pos()
        self._debug['cab_data']['start'] = self._io.pos()
        self._raw_cab_data = self._io.read_bytes(self.preheader.len_cabinet - 12)
        _io__raw_cab_data = KaitaiStream(BytesIO(self._raw_cab_data))
        self.cab_data = Cab.CabData(_io__raw_cab_data, self, self._root)
        self._debug['cab_data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.preheader._fetch_instances()
        self.cab_data._fetch_instances()

    class CabData(KaitaiStruct):
        SEQ_FIELDS = ["header", "first_folder", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Cab.CabData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Cab.Header(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['first_folder']['start'] = self._io.pos()
            self.first_folder = Cab.Folder(self._io, self, self._root)
            self._debug['first_folder']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes_full()
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.first_folder._fetch_instances()


    class Folder(KaitaiStruct):
        SEQ_FIELDS = ["ofs_cab_start", "num_cfdata_blocks", "type_compress", "per_folder_reserved_area"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Cab.Folder, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_cab_start']['start'] = self._io.pos()
            self.ofs_cab_start = self._io.read_u4le()
            self._debug['ofs_cab_start']['end'] = self._io.pos()
            self._debug['num_cfdata_blocks']['start'] = self._io.pos()
            self.num_cfdata_blocks = self._io.read_u2le()
            self._debug['num_cfdata_blocks']['end'] = self._io.pos()
            self._debug['type_compress']['start'] = self._io.pos()
            self.type_compress = self._io.read_u2le()
            self._debug['type_compress']['end'] = self._io.pos()
            if self._parent.header.reserve_present:
                pass
                self._debug['per_folder_reserved_area']['start'] = self._io.pos()
                self.per_folder_reserved_area = self._io.read_bytes(self._parent.header.len_per_folder_reserved)
                self._debug['per_folder_reserved_area']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self._parent.header.reserve_present:
                pass



    class Header(KaitaiStruct):
        SEQ_FIELDS = ["reserved2", "ofs_cffile", "reserved3", "version", "num_folders", "num_files", "flags", "set_id", "cabinet_number", "len_per_cabinet_reserved", "len_per_folder_reserved", "len_per_datablock_reserved", "per_cabinet_reserved_area", "previous_cabinet", "previous_disk", "next_cabinet", "next_disk"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Cab.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bytes(4)
            self._debug['reserved2']['end'] = self._io.pos()
            if not self.reserved2 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.reserved2, self._io, u"/types/header/seq/0")
            self._debug['ofs_cffile']['start'] = self._io.pos()
            self.ofs_cffile = self._io.read_u4le()
            self._debug['ofs_cffile']['end'] = self._io.pos()
            if not self.ofs_cffile <= self._root.preheader.len_cabinet:
                raise kaitaistruct.ValidationGreaterThanError(self._root.preheader.len_cabinet, self.ofs_cffile, self._io, u"/types/header/seq/1")
            self._debug['reserved3']['start'] = self._io.pos()
            self.reserved3 = self._io.read_bytes(4)
            self._debug['reserved3']['end'] = self._io.pos()
            if not self.reserved3 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.reserved3, self._io, u"/types/header/seq/2")
            self._debug['version']['start'] = self._io.pos()
            self.version = Cab.Version(self._io, self, self._root)
            self._debug['version']['end'] = self._io.pos()
            self._debug['num_folders']['start'] = self._io.pos()
            self.num_folders = self._io.read_u2le()
            self._debug['num_folders']['end'] = self._io.pos()
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u2le()
            self._debug['num_files']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['set_id']['start'] = self._io.pos()
            self.set_id = self._io.read_u2le()
            self._debug['set_id']['end'] = self._io.pos()
            self._debug['cabinet_number']['start'] = self._io.pos()
            self.cabinet_number = self._io.read_u2le()
            self._debug['cabinet_number']['end'] = self._io.pos()
            if self.reserve_present:
                pass
                self._debug['len_per_cabinet_reserved']['start'] = self._io.pos()
                self.len_per_cabinet_reserved = self._io.read_u2le()
                self._debug['len_per_cabinet_reserved']['end'] = self._io.pos()
                if not self.len_per_cabinet_reserved >= 0:
                    raise kaitaistruct.ValidationLessThanError(0, self.len_per_cabinet_reserved, self._io, u"/types/header/seq/9")
                if not self.len_per_cabinet_reserved <= 60000:
                    raise kaitaistruct.ValidationGreaterThanError(60000, self.len_per_cabinet_reserved, self._io, u"/types/header/seq/9")

            if self.reserve_present:
                pass
                self._debug['len_per_folder_reserved']['start'] = self._io.pos()
                self.len_per_folder_reserved = self._io.read_u1()
                self._debug['len_per_folder_reserved']['end'] = self._io.pos()
                if not self.len_per_folder_reserved >= 0:
                    raise kaitaistruct.ValidationLessThanError(0, self.len_per_folder_reserved, self._io, u"/types/header/seq/10")
                if not self.len_per_folder_reserved <= 255:
                    raise kaitaistruct.ValidationGreaterThanError(255, self.len_per_folder_reserved, self._io, u"/types/header/seq/10")

            if self.reserve_present:
                pass
                self._debug['len_per_datablock_reserved']['start'] = self._io.pos()
                self.len_per_datablock_reserved = self._io.read_u1()
                self._debug['len_per_datablock_reserved']['end'] = self._io.pos()
                if not self.len_per_datablock_reserved >= 0:
                    raise kaitaistruct.ValidationLessThanError(0, self.len_per_datablock_reserved, self._io, u"/types/header/seq/11")
                if not self.len_per_datablock_reserved <= 255:
                    raise kaitaistruct.ValidationGreaterThanError(255, self.len_per_datablock_reserved, self._io, u"/types/header/seq/11")

            if self.reserve_present:
                pass
                self._debug['per_cabinet_reserved_area']['start'] = self._io.pos()
                self.per_cabinet_reserved_area = self._io.read_bytes(self.len_per_cabinet_reserved)
                self._debug['per_cabinet_reserved_area']['end'] = self._io.pos()

            if self.has_previous_cabinet:
                pass
                self._debug['previous_cabinet']['start'] = self._io.pos()
                self.previous_cabinet = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                self._debug['previous_cabinet']['end'] = self._io.pos()

            if self.has_previous_cabinet:
                pass
                self._debug['previous_disk']['start'] = self._io.pos()
                self.previous_disk = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                self._debug['previous_disk']['end'] = self._io.pos()

            if self.has_next_cabinet:
                pass
                self._debug['next_cabinet']['start'] = self._io.pos()
                self.next_cabinet = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                self._debug['next_cabinet']['end'] = self._io.pos()

            if self.has_next_cabinet:
                pass
                self._debug['next_disk']['start'] = self._io.pos()
                self.next_disk = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
                self._debug['next_disk']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.version._fetch_instances()
            if self.reserve_present:
                pass

            if self.reserve_present:
                pass

            if self.reserve_present:
                pass

            if self.reserve_present:
                pass

            if self.has_previous_cabinet:
                pass

            if self.has_previous_cabinet:
                pass

            if self.has_next_cabinet:
                pass

            if self.has_next_cabinet:
                pass


        @property
        def has_next_cabinet(self):
            if hasattr(self, '_m_has_next_cabinet'):
                return self._m_has_next_cabinet

            self._m_has_next_cabinet = self.flags & 2 == 2
            return getattr(self, '_m_has_next_cabinet', None)

        @property
        def has_previous_cabinet(self):
            if hasattr(self, '_m_has_previous_cabinet'):
                return self._m_has_previous_cabinet

            self._m_has_previous_cabinet = self.flags & 1 == 1
            return getattr(self, '_m_has_previous_cabinet', None)

        @property
        def reserve_present(self):
            if hasattr(self, '_m_reserve_present'):
                return self._m_reserve_present

            self._m_reserve_present = self.flags & 4 == 4
            return getattr(self, '_m_reserve_present', None)


    class Preheader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "reserved1", "len_cabinet"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Cab.Preheader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x4D\x53\x43\x46":
                raise kaitaistruct.ValidationNotEqualError(b"\x4D\x53\x43\x46", self.magic, self._io, u"/types/preheader/seq/0")
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bytes(4)
            self._debug['reserved1']['end'] = self._io.pos()
            if not self.reserved1 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.reserved1, self._io, u"/types/preheader/seq/1")
            self._debug['len_cabinet']['start'] = self._io.pos()
            self.len_cabinet = self._io.read_u4le()
            self._debug['len_cabinet']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Version(KaitaiStruct):
        SEQ_FIELDS = ["minor", "major"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Cab.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u1()
            self._debug['minor']['end'] = self._io.pos()
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u1()
            self._debug['major']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



