# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections
import zlib


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MtkImage(KaitaiStruct):
    """Container format of various Mediatek files
    
    .. seealso::
       Source - https://github.com/omnirom/android_device_oppo_r819/blob/android-4.4/mkmtkbootimg/bootimg.h
    
    
    .. seealso::
       Source - http://web.archive.org/web/20200805105219/https://www.rigacci.org/wiki/doku.php/doc/appunti/android/logo_bootanimation
    
    
    .. seealso::
       Source - http://web.archive.org/web/20201123215346/https://www.rigacci.org/wiki/lib/exe/fetch.php/doc/appunti/android/mtk-android-logo.txt
    """
    SEQ_FIELDS = ["header", "payload"]
    def __init__(self, _io, _parent=None, _root=None):
        super(MtkImage, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(512)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = MtkImage.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['payload']['start'] = self._io.pos()
        _on = self.header.magic
        if _on == u"LOGO":
            pass
            self._raw_payload = self._io.read_bytes(self.header.len_payload)
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = MtkImage.Images(_io__raw_payload, self, self._root)
        elif _on == u"logo":
            pass
            self._raw_payload = self._io.read_bytes(self.header.len_payload)
            _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
            self.payload = MtkImage.Images(_io__raw_payload, self, self._root)
        else:
            pass
            self.payload = self._io.read_bytes(self.header.len_payload)
        self._debug['payload']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        _on = self.header.magic
        if _on == u"LOGO":
            pass
            self.payload._fetch_instances()
        elif _on == u"logo":
            pass
            self.payload._fetch_instances()
        else:
            pass

    class Header(KaitaiStruct):
        SEQ_FIELDS = ["mtk_magic", "len_payload", "magic"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkImage.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['mtk_magic']['start'] = self._io.pos()
            self.mtk_magic = self._io.read_bytes(4)
            self._debug['mtk_magic']['end'] = self._io.pos()
            if not self.mtk_magic == b"\x88\x16\x88\x58":
                raise kaitaistruct.ValidationNotEqualError(b"\x88\x16\x88\x58", self.mtk_magic, self._io, u"/types/header/seq/0")
            self._debug['len_payload']['start'] = self._io.pos()
            self.len_payload = self._io.read_u4le()
            self._debug['len_payload']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['magic']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Images(KaitaiStruct):
        SEQ_FIELDS = ["num_pictures", "total_block_size", "offsets"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MtkImage.Images, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_pictures']['start'] = self._io.pos()
            self.num_pictures = self._io.read_u4le()
            self._debug['num_pictures']['end'] = self._io.pos()
            self._debug['total_block_size']['start'] = self._io.pos()
            self.total_block_size = self._io.read_u4le()
            self._debug['total_block_size']['end'] = self._io.pos()
            if not self.total_block_size == self._root.header.len_payload:
                raise kaitaistruct.ValidationNotEqualError(self._root.header.len_payload, self.total_block_size, self._io, u"/types/images/seq/1")
            self._debug['offsets']['start'] = self._io.pos()
            self._debug['offsets']['arr'] = []
            self.offsets = []
            for i in range(self.num_pictures):
                self._debug['offsets']['arr'].append({'start': self._io.pos()})
                self.offsets.append(self._io.read_u4le())
                self._debug['offsets']['arr'][i]['end'] = self._io.pos()

            self._debug['offsets']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.offsets)):
                pass

            _ = self.data
            if hasattr(self, '_m_data'):
                pass
                for i in range(len(self._m_data)):
                    pass
                    self._m_data[i]._fetch_instances()



        class Body(KaitaiStruct):
            SEQ_FIELDS = []
            def __init__(self, i, _io, _parent=None, _root=None):
                super(MtkImage.Images.Body, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self.i = i
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                pass


            def _fetch_instances(self):
                pass
                _ = self.body
                if hasattr(self, '_m_body'):
                    pass


            @property
            def body(self):
                if hasattr(self, '_m_body'):
                    return self._m_body

                _pos = self._io.pos()
                self._io.seek(self._parent.offsets[self.i])
                self._debug['_m_body']['start'] = self._io.pos()
                self._raw__m_body = self._io.read_bytes((self._parent.total_block_size - self._parent.offsets[self.i] if self.i == len(self._parent.offsets) - 1 else self._parent.offsets[self.i + 1] - self._parent.offsets[self.i]))
                self._m_body = zlib.decompress(self._raw__m_body)
                self._debug['_m_body']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_body', None)


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            self._debug['_m_data']['start'] = self._io.pos()
            self._debug['_m_data']['arr'] = []
            self._m_data = []
            for i in range(self.num_pictures):
                self._debug['_m_data']['arr'].append({'start': self._io.pos()})
                self._m_data.append(MtkImage.Images.Body(i, self._io, self, self._root))
                self._debug['_m_data']['arr'][i]['end'] = self._io.pos()

            self._debug['_m_data']['end'] = self._io.pos()
            return getattr(self, '_m_data', None)



