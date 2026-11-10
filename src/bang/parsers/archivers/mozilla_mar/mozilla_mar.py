# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MozillaMar(KaitaiStruct):
    """Mozilla ARchive file is Mozilla's own archive format to distribute software updates.
    Test files can be found on Mozilla's FTP site, for example:
    
    <https://ftp.mozilla.org/pub/firefox/nightly/partials/>
    
    .. seealso::
       Source - https://wiki.mozilla.org/Software_Update:MAR
    """

    class BlockIdentifiers(IntEnum):
        product_information = 1

    class SignatureAlgorithms(IntEnum):
        rsa_pkcs1_sha1 = 1
        rsa_pkcs1_sha384 = 2
    SEQ_FIELDS = ["magic", "ofs_index", "file_size", "num_signatures", "signatures", "num_additional_sections", "additional_sections"]
    def __init__(self, _io, _parent=None, _root=None):
        super(MozillaMar, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x4D\x41\x52\x31":
            raise kaitaistruct.ValidationNotEqualError(b"\x4D\x41\x52\x31", self.magic, self._io, u"/seq/0")
        self._debug['ofs_index']['start'] = self._io.pos()
        self.ofs_index = self._io.read_u4be()
        self._debug['ofs_index']['end'] = self._io.pos()
        self._debug['file_size']['start'] = self._io.pos()
        self.file_size = self._io.read_u8be()
        self._debug['file_size']['end'] = self._io.pos()
        self._debug['num_signatures']['start'] = self._io.pos()
        self.num_signatures = self._io.read_u4be()
        self._debug['num_signatures']['end'] = self._io.pos()
        if not self.num_signatures <= 8:
            raise kaitaistruct.ValidationGreaterThanError(8, self.num_signatures, self._io, u"/seq/3")
        self._debug['signatures']['start'] = self._io.pos()
        self._debug['signatures']['arr'] = []
        self.signatures = []
        for i in range(self.num_signatures):
            self._debug['signatures']['arr'].append({'start': self._io.pos()})
            self.signatures.append(MozillaMar.Signature(self._io, self, self._root))
            self._debug['signatures']['arr'][i]['end'] = self._io.pos()

        self._debug['signatures']['end'] = self._io.pos()
        self._debug['num_additional_sections']['start'] = self._io.pos()
        self.num_additional_sections = self._io.read_u4be()
        self._debug['num_additional_sections']['end'] = self._io.pos()
        self._debug['additional_sections']['start'] = self._io.pos()
        self._debug['additional_sections']['arr'] = []
        self.additional_sections = []
        for i in range(self.num_additional_sections):
            self._debug['additional_sections']['arr'].append({'start': self._io.pos()})
            self.additional_sections.append(MozillaMar.AdditionalSection(self._io, self, self._root))
            self._debug['additional_sections']['arr'][i]['end'] = self._io.pos()

        self._debug['additional_sections']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.signatures)):
            pass
            self.signatures[i]._fetch_instances()

        for i in range(len(self.additional_sections)):
            pass
            self.additional_sections[i]._fetch_instances()

        _ = self.index
        if hasattr(self, '_m_index'):
            pass
            self._m_index._fetch_instances()


    class AdditionalSection(KaitaiStruct):
        SEQ_FIELDS = ["len_block", "block_identifier", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MozillaMar.AdditionalSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_block']['start'] = self._io.pos()
            self.len_block = self._io.read_u4be()
            self._debug['len_block']['end'] = self._io.pos()
            self._debug['block_identifier']['start'] = self._io.pos()
            self.block_identifier = KaitaiStream.resolve_enum(MozillaMar.BlockIdentifiers, self._io.read_u4be())
            self._debug['block_identifier']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.block_identifier
            if _on == MozillaMar.BlockIdentifiers.product_information:
                pass
                self._raw_body = self._io.read_bytes((self.len_block - 4) - 4)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = MozillaMar.ProductInformationBlock(_io__raw_body, self, self._root)
            else:
                pass
                self.body = self._io.read_bytes((self.len_block - 4) - 4)
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.block_identifier
            if _on == MozillaMar.BlockIdentifiers.product_information:
                pass
                self.body._fetch_instances()
            else:
                pass


    class IndexEntries(KaitaiStruct):
        SEQ_FIELDS = ["index_entry"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MozillaMar.IndexEntries, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['index_entry']['start'] = self._io.pos()
            self._debug['index_entry']['arr'] = []
            self.index_entry = []
            i = 0
            while not self._io.is_eof():
                self._debug['index_entry']['arr'].append({'start': self._io.pos()})
                self.index_entry.append(MozillaMar.IndexEntry(self._io, self, self._root))
                self._debug['index_entry']['arr'][len(self.index_entry) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['index_entry']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.index_entry)):
                pass
                self.index_entry[i]._fetch_instances()



    class IndexEntry(KaitaiStruct):
        SEQ_FIELDS = ["ofs_content", "len_content", "flags", "file_name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MozillaMar.IndexEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_content']['start'] = self._io.pos()
            self.ofs_content = self._io.read_u4be()
            self._debug['ofs_content']['end'] = self._io.pos()
            self._debug['len_content']['start'] = self._io.pos()
            self.len_content = self._io.read_u4be()
            self._debug['len_content']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['file_name']['start'] = self._io.pos()
            self.file_name = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['file_name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.content
            if hasattr(self, '_m_content'):
                pass


        @property
        def content(self):
            if hasattr(self, '_m_content'):
                return self._m_content

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_content)
            self._debug['_m_content']['start'] = io.pos()
            self._m_content = io.read_bytes(self.len_content)
            self._debug['_m_content']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_content', None)


    class MarIndex(KaitaiStruct):
        SEQ_FIELDS = ["len_index_entries", "index_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MozillaMar.MarIndex, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_index_entries']['start'] = self._io.pos()
            self.len_index_entries = self._io.read_u4be()
            self._debug['len_index_entries']['end'] = self._io.pos()
            self._debug['index_entries']['start'] = self._io.pos()
            self._raw_index_entries = self._io.read_bytes(self.len_index_entries)
            _io__raw_index_entries = KaitaiStream(BytesIO(self._raw_index_entries))
            self.index_entries = MozillaMar.IndexEntries(_io__raw_index_entries, self, self._root)
            self._debug['index_entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.index_entries._fetch_instances()


    class ProductInformationBlock(KaitaiStruct):
        SEQ_FIELDS = ["mar_channel_name", "product_version"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MozillaMar.ProductInformationBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['mar_channel_name']['start'] = self._io.pos()
            self.mar_channel_name = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"UTF-8")
            self._debug['mar_channel_name']['end'] = self._io.pos()
            self._debug['product_version']['start'] = self._io.pos()
            self.product_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['product_version']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Signature(KaitaiStruct):
        SEQ_FIELDS = ["algorithm", "len_signature", "signature"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MozillaMar.Signature, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['algorithm']['start'] = self._io.pos()
            self.algorithm = KaitaiStream.resolve_enum(MozillaMar.SignatureAlgorithms, self._io.read_u4be())
            self._debug['algorithm']['end'] = self._io.pos()
            self._debug['len_signature']['start'] = self._io.pos()
            self.len_signature = self._io.read_u4be()
            self._debug['len_signature']['end'] = self._io.pos()
            if not self.len_signature <= 2048:
                raise kaitaistruct.ValidationGreaterThanError(2048, self.len_signature, self._io, u"/types/signature/seq/1")
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(self.len_signature)
            self._debug['signature']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def index(self):
        if hasattr(self, '_m_index'):
            return self._m_index

        _pos = self._io.pos()
        self._io.seek(self.ofs_index)
        self._debug['_m_index']['start'] = self._io.pos()
        self._m_index = MozillaMar.MarIndex(self._io, self, self._root)
        self._debug['_m_index']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_index', None)


