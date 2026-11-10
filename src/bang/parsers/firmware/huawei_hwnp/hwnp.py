# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Hwnp(KaitaiStruct):
    """Test files: https://www.zhiwanyuzhou.com/download/Firmware/Router/Huawei/HG/HG8245V100R006C00SPC205%20Software/
    
    .. seealso::
       Source - https://github.com/0xuserpag3/HuaweiFirmwareTool
    """
    SEQ_FIELDS = ["header", "products_and_items"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Hwnp, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Hwnp.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['products_and_items']['start'] = self._io.pos()
        self._raw_products_and_items = self._io.read_bytes(self.header.len_header)
        _io__raw_products_and_items = KaitaiStream(BytesIO(self._raw_products_and_items))
        self.products_and_items = Hwnp.ProductsAndItems(_io__raw_products_and_items, self, self._root)
        self._debug['products_and_items']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.products_and_items._fetch_instances()

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_data", "crc32", "len_header", "header_crc32", "num_items", "unknown", "len_product_list", "len_item", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Hwnp.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x48\x57\x4E\x50":
                raise kaitaistruct.ValidationNotEqualError(b"\x48\x57\x4E\x50", self.magic, self._io, u"/types/header/seq/0")
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4le()
            self._debug['len_header']['end'] = self._io.pos()
            self._debug['header_crc32']['start'] = self._io.pos()
            self.header_crc32 = self._io.read_u4le()
            self._debug['header_crc32']['end'] = self._io.pos()
            self._debug['num_items']['start'] = self._io.pos()
            self.num_items = self._io.read_u4le()
            self._debug['num_items']['end'] = self._io.pos()
            self._debug['unknown']['start'] = self._io.pos()
            self.unknown = self._io.read_bytes(2)
            self._debug['unknown']['end'] = self._io.pos()
            self._debug['len_product_list']['start'] = self._io.pos()
            self.len_product_list = self._io.read_u2le()
            self._debug['len_product_list']['end'] = self._io.pos()
            self._debug['len_item']['start'] = self._io.pos()
            self.len_item = self._io.read_u4le()
            self._debug['len_item']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(4)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Item(KaitaiStruct):
        SEQ_FIELDS = ["iter", "crc32", "ofs_data", "len_data", "name", "section", "version", "policy", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Hwnp.Item, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['iter']['start'] = self._io.pos()
            self.iter = self._io.read_u4le()
            self._debug['iter']['end'] = self._io.pos()
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['ofs_data']['start'] = self._io.pos()
            self.ofs_data = self._io.read_u4le()
            self._debug['ofs_data']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (KaitaiStream.bytes_terminate(self._io.read_bytes(256), 0, False)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()
            self._debug['section']['start'] = self._io.pos()
            self.section = (KaitaiStream.bytes_terminate(self._io.read_bytes(16), 0, False)).decode(u"UTF-8")
            self._debug['section']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"UTF-8")
            self._debug['version']['end'] = self._io.pos()
            self._debug['policy']['start'] = self._io.pos()
            self.policy = self._io.read_u4le()
            self._debug['policy']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(4)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.data
            if hasattr(self, '_m_data'):
                pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_data)
            self._debug['_m_data']['start'] = io.pos()
            self._m_data = io.read_bytes(self.len_data)
            self._debug['_m_data']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_data', None)


    class ProductsAndItems(KaitaiStruct):
        SEQ_FIELDS = ["product_list", "items"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Hwnp.ProductsAndItems, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['product_list']['start'] = self._io.pos()
            self.product_list = self._io.read_bytes(self._root.header.len_product_list)
            self._debug['product_list']['end'] = self._io.pos()
            self._debug['items']['start'] = self._io.pos()
            self._debug['items']['arr'] = []
            self._raw_items = []
            self.items = []
            for i in range(self._root.header.num_items):
                self._debug['items']['arr'].append({'start': self._io.pos()})
                self._raw_items.append(self._io.read_bytes(self._root.header.len_item))
                _io__raw_items = KaitaiStream(BytesIO(self._raw_items[i]))
                self.items.append(Hwnp.Item(_io__raw_items, self, self._root))
                self._debug['items']['arr'][i]['end'] = self._io.pos()

            self._debug['items']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.items)):
                pass
                self.items[i]._fetch_instances()




