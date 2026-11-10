# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class BtfExt(KaitaiStruct):
    """
    .. seealso::
       Source - https://docs.kernel.org/bpf/btf.html
    """
    SEQ_FIELDS = ["header", "func_info_section", "line_info_section"]
    def __init__(self, _io, _parent=None, _root=None):
        super(BtfExt, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = BtfExt.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['func_info_section']['start'] = self._io.pos()
        self._raw_func_info_section = self._io.read_bytes(self.header.rest_of_header.len_func_info_section)
        _io__raw_func_info_section = KaitaiStream(BytesIO(self._raw_func_info_section))
        self.func_info_section = BtfExt.FuncLineInfo(_io__raw_func_info_section, self, self._root)
        self._debug['func_info_section']['end'] = self._io.pos()
        self._debug['line_info_section']['start'] = self._io.pos()
        self._raw_line_info_section = self._io.read_bytes(self.header.rest_of_header.len_line_info_section)
        _io__raw_line_info_section = KaitaiStream(BytesIO(self._raw_line_info_section))
        self.line_info_section = BtfExt.FuncLineInfo(_io__raw_line_info_section, self, self._root)
        self._debug['line_info_section']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.func_info_section._fetch_instances()
        self.line_info_section._fetch_instances()

    class BtfExtInfoSec(KaitaiStruct):
        SEQ_FIELDS = ["ofs_section_name", "num_info", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(BtfExt.BtfExtInfoSec, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_section_name']['start'] = self._io.pos()
            self.ofs_section_name = self._io.read_u4le()
            self._debug['ofs_section_name']['end'] = self._io.pos()
            self._debug['num_info']['start'] = self._io.pos()
            self.num_info = self._io.read_u4le()
            self._debug['num_info']['end'] = self._io.pos()
            if not self.num_info >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.num_info, self._io, u"/types/btf_ext_info_sec/seq/1")
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.num_info * self._parent.len_info_rec)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class FuncLineInfo(KaitaiStruct):
        SEQ_FIELDS = ["len_info_rec", "btf_ext_info_secs"]
        def __init__(self, _io, _parent=None, _root=None):
            super(BtfExt.FuncLineInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_info_rec']['start'] = self._io.pos()
            self.len_info_rec = self._io.read_u4le()
            self._debug['len_info_rec']['end'] = self._io.pos()
            self._debug['btf_ext_info_secs']['start'] = self._io.pos()
            self._debug['btf_ext_info_secs']['arr'] = []
            self.btf_ext_info_secs = []
            i = 0
            while not self._io.is_eof():
                self._debug['btf_ext_info_secs']['arr'].append({'start': self._io.pos()})
                self.btf_ext_info_secs.append(BtfExt.BtfExtInfoSec(self._io, self, self._root))
                self._debug['btf_ext_info_secs']['arr'][len(self.btf_ext_info_secs) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['btf_ext_info_secs']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.btf_ext_info_secs)):
                pass
                self.btf_ext_info_secs[i]._fetch_instances()



    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "flags", "len_header", "rest_of_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(BtfExt.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x9F\xEB":
                raise kaitaistruct.ValidationNotEqualError(b"\x9F\xEB", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u1()
            self._debug['version']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['rest_of_header']['start'] = self._io.pos()
            self._raw_rest_of_header = self._io.read_bytes((((self.len_header - 2) - 1) - 1) - 4)
            _io__raw_rest_of_header = KaitaiStream(BytesIO(self._raw_rest_of_header))
            self.rest_of_header = BtfExt.Header.RestOfHeader(_io__raw_rest_of_header, self, self._root)
            self._debug['rest_of_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.rest_of_header._fetch_instances()

        class RestOfHeader(KaitaiStruct):
            SEQ_FIELDS = ["ofs_func_info_section", "len_func_info_section", "ofs_line_info_section", "len_line_info_section", "ofs_core_relo", "len_core_relo"]
            def __init__(self, _io, _parent=None, _root=None):
                super(BtfExt.Header.RestOfHeader, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['ofs_func_info_section']['start'] = self._io.pos()
                self.ofs_func_info_section = self._io.read_u4le()
                self._debug['ofs_func_info_section']['end'] = self._io.pos()
                self._debug['len_func_info_section']['start'] = self._io.pos()
                self.len_func_info_section = self._io.read_u4le()
                self._debug['len_func_info_section']['end'] = self._io.pos()
                self._debug['ofs_line_info_section']['start'] = self._io.pos()
                self.ofs_line_info_section = self._io.read_u4le()
                self._debug['ofs_line_info_section']['end'] = self._io.pos()
                self._debug['len_line_info_section']['start'] = self._io.pos()
                self.len_line_info_section = self._io.read_u4le()
                self._debug['len_line_info_section']['end'] = self._io.pos()
                if self._parent.len_header >= 32:
                    pass
                    self._debug['ofs_core_relo']['start'] = self._io.pos()
                    self.ofs_core_relo = self._io.read_u4le()
                    self._debug['ofs_core_relo']['end'] = self._io.pos()

                if self._parent.len_header >= 32:
                    pass
                    self._debug['len_core_relo']['start'] = self._io.pos()
                    self.len_core_relo = self._io.read_u4le()
                    self._debug['len_core_relo']['end'] = self._io.pos()



            def _fetch_instances(self):
                pass
                if self._parent.len_header >= 32:
                    pass

                if self._parent.len_header >= 32:
                    pass





