# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class QtiChromatix(KaitaiStruct):
    """A proprietary format from Qualcomm."""
    SEQ_FIELDS = ["header", "data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(QtiChromatix, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = QtiChromatix.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['data']['start'] = self._io.pos()
        self.data = self._io.read_bytes(self.header.len_file - 76)
        self._debug['data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["signature", "unknown1", "len_file", "version", "unknown2", "parser_signature"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtiChromatix.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(20)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x51\x54\x49\x20\x43\x68\x72\x6F\x6D\x61\x74\x69\x78\x20\x48\x65\x61\x64\x65\x72":
                raise kaitaistruct.ValidationNotEqualError(b"\x51\x54\x49\x20\x43\x68\x72\x6F\x6D\x61\x74\x69\x78\x20\x48\x65\x61\x64\x65\x72", self.signature, self._io, u"/types/header/seq/0")
            self._debug['unknown1']['start'] = self._io.pos()
            self.unknown1 = self._io.read_bytes(8)
            self._debug['unknown1']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = QtiChromatix.Version(self._io, self, self._root)
            self._debug['version']['end'] = self._io.pos()
            self._debug['unknown2']['start'] = self._io.pos()
            self.unknown2 = self._io.read_bytes(2)
            self._debug['unknown2']['end'] = self._io.pos()
            self._debug['parser_signature']['start'] = self._io.pos()
            self.parser_signature = QtiChromatix.ParserSignature(self._io, self, self._root)
            self._debug['parser_signature']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.version._fetch_instances()
            self.parser_signature._fetch_instances()


    class ParserSignature(KaitaiStruct):
        SEQ_FIELDS = ["signature", "version", "space", "date"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtiChromatix.ParserSignature, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(18)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x50\x61\x72\x61\x6D\x65\x74\x65\x72\x20\x50\x61\x72\x73\x65\x72\x20\x56":
                raise kaitaistruct.ValidationNotEqualError(b"\x50\x61\x72\x61\x6D\x65\x74\x65\x72\x20\x50\x61\x72\x73\x65\x72\x20\x56", self.signature, self._io, u"/types/parser_signature/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self._raw_version = self._io.read_bytes(5)
            _io__raw_version = KaitaiStream(BytesIO(self._raw_version))
            self.version = QtiChromatix.ParserSignature.ParserVersion(_io__raw_version, self, self._root)
            self._debug['version']['end'] = self._io.pos()
            self._debug['space']['start'] = self._io.pos()
            self.space = self._io.read_bytes(1)
            self._debug['space']['end'] = self._io.pos()
            if not self.space == b"\x20":
                raise kaitaistruct.ValidationNotEqualError(b"\x20", self.space, self._io, u"/types/parser_signature/seq/2")
            self._debug['date']['start'] = self._io.pos()
            self._raw_date = self._io.read_bytes(12)
            _io__raw_date = KaitaiStream(BytesIO(self._raw_date))
            self.date = QtiChromatix.ParserSignature.Date(_io__raw_date, self, self._root)
            self._debug['date']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.version._fetch_instances()
            self.date._fetch_instances()

        class Date(KaitaiStruct):
            SEQ_FIELDS = ["parens_left", "date_string", "parens_right"]
            def __init__(self, _io, _parent=None, _root=None):
                super(QtiChromatix.ParserSignature.Date, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['parens_left']['start'] = self._io.pos()
                self.parens_left = self._io.read_bytes(1)
                self._debug['parens_left']['end'] = self._io.pos()
                if not self.parens_left == b"\x28":
                    raise kaitaistruct.ValidationNotEqualError(b"\x28", self.parens_left, self._io, u"/types/parser_signature/types/date/seq/0")
                self._debug['date_string']['start'] = self._io.pos()
                self.date_string = (self._io.read_bytes(10)).decode(u"UTF-8")
                self._debug['date_string']['end'] = self._io.pos()
                self._debug['parens_right']['start'] = self._io.pos()
                self.parens_right = self._io.read_bytes(1)
                self._debug['parens_right']['end'] = self._io.pos()
                if not self.parens_right == b"\x29":
                    raise kaitaistruct.ValidationNotEqualError(b"\x29", self.parens_right, self._io, u"/types/parser_signature/types/date/seq/2")


            def _fetch_instances(self):
                pass


        class ParserVersion(KaitaiStruct):
            SEQ_FIELDS = ["major_str", "minor_str", "sub_str"]
            def __init__(self, _io, _parent=None, _root=None):
                super(QtiChromatix.ParserSignature.ParserVersion, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['major_str']['start'] = self._io.pos()
                self.major_str = (self._io.read_bytes_term(46, False, True, True)).decode(u"UTF-8")
                self._debug['major_str']['end'] = self._io.pos()
                self._debug['minor_str']['start'] = self._io.pos()
                self.minor_str = (self._io.read_bytes_term(46, False, True, True)).decode(u"UTF-8")
                self._debug['minor_str']['end'] = self._io.pos()
                self._debug['sub_str']['start'] = self._io.pos()
                self.sub_str = (self._io.read_bytes_full()).decode(u"UTF-8")
                self._debug['sub_str']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass

            @property
            def major(self):
                if hasattr(self, '_m_major'):
                    return self._m_major

                self._m_major = int(self.major_str)
                return getattr(self, '_m_major', None)

            @property
            def minor(self):
                if hasattr(self, '_m_minor'):
                    return self._m_minor

                self._m_minor = int(self.minor_str)
                return getattr(self, '_m_minor', None)

            @property
            def sub(self):
                if hasattr(self, '_m_sub'):
                    return self._m_sub

                self._m_sub = int(self.sub_str)
                return getattr(self, '_m_sub', None)



    class Version(KaitaiStruct):
        SEQ_FIELDS = ["major", "minor", "sub"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtiChromatix.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u2le()
            self._debug['major']['end'] = self._io.pos()
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u2le()
            self._debug['minor']['end'] = self._io.pos()
            self._debug['sub']['start'] = self._io.pos()
            self.sub = self._io.read_u2le()
            self._debug['sub']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



