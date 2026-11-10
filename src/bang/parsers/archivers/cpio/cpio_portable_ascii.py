# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class CpioPortableAscii(KaitaiStruct):
    SEQ_FIELDS = ["entries"]
    def __init__(self, _io, _parent=None, _root=None):
        super(CpioPortableAscii, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['entries']['start'] = self._io.pos()
        self._debug['entries']['arr'] = []
        self.entries = []
        i = 0
        while True:
            self._debug['entries']['arr'].append({'start': self._io.pos()})
            _ = CpioPortableAscii.CpioPortableAsciiHeaderAndFile(self._io, self, self._root)
            self.entries.append(_)
            self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
            if  ((_.filename == self.trailing_filename) and (_.header.fsize == 0)) :
                break
            i += 1
        self._debug['entries']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.entries)):
            pass
            self.entries[i]._fetch_instances()


    class CpioPortableAsciiHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "dev", "ino", "mode", "uid", "gid", "nlink", "rdev", "mtime", "namesize", "filesize"]
        def __init__(self, _io, _parent=None, _root=None):
            super(CpioPortableAscii.CpioPortableAsciiHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(6)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x30\x37\x30\x37\x30\x37":
                raise kaitaistruct.ValidationNotEqualError(b"\x30\x37\x30\x37\x30\x37", self.magic, self._io, u"/types/cpio_portable_ascii_header/seq/0")
            self._debug['dev']['start'] = self._io.pos()
            self.dev = (self._io.read_bytes(6)).decode(u"ASCII")
            self._debug['dev']['end'] = self._io.pos()
            self._debug['ino']['start'] = self._io.pos()
            self.ino = (self._io.read_bytes(6)).decode(u"ASCII")
            self._debug['ino']['end'] = self._io.pos()
            self._debug['mode']['start'] = self._io.pos()
            self.mode = (self._io.read_bytes(6)).decode(u"ASCII")
            self._debug['mode']['end'] = self._io.pos()
            self._debug['uid']['start'] = self._io.pos()
            self.uid = (self._io.read_bytes(6)).decode(u"ASCII")
            self._debug['uid']['end'] = self._io.pos()
            self._debug['gid']['start'] = self._io.pos()
            self.gid = (self._io.read_bytes(6)).decode(u"ASCII")
            self._debug['gid']['end'] = self._io.pos()
            self._debug['nlink']['start'] = self._io.pos()
            self.nlink = (self._io.read_bytes(6)).decode(u"ASCII")
            self._debug['nlink']['end'] = self._io.pos()
            self._debug['rdev']['start'] = self._io.pos()
            self.rdev = (self._io.read_bytes(6)).decode(u"ASCII")
            self._debug['rdev']['end'] = self._io.pos()
            self._debug['mtime']['start'] = self._io.pos()
            self.mtime = (self._io.read_bytes(11)).decode(u"ASCII")
            self._debug['mtime']['end'] = self._io.pos()
            self._debug['namesize']['start'] = self._io.pos()
            self.namesize = (self._io.read_bytes(6)).decode(u"ASCII")
            self._debug['namesize']['end'] = self._io.pos()
            self._debug['filesize']['start'] = self._io.pos()
            self.filesize = (self._io.read_bytes(11)).decode(u"ASCII")
            self._debug['filesize']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def bsize(self):
            if hasattr(self, '_m_bsize'):
                return self._m_bsize

            self._m_bsize = (((self.hsize + self.nsize) + self.npaddingsize) + self.fsize) + self.fpaddingsize
            return getattr(self, '_m_bsize', None)

        @property
        def cpio_mode(self):
            if hasattr(self, '_m_cpio_mode'):
                return self._m_cpio_mode

            self._m_cpio_mode = int(self.mode, 8)
            return getattr(self, '_m_cpio_mode', None)

        @property
        def fpaddingsize(self):
            if hasattr(self, '_m_fpaddingsize'):
                return self._m_fpaddingsize

            self._m_fpaddingsize = 0
            return getattr(self, '_m_fpaddingsize', None)

        @property
        def fsize(self):
            if hasattr(self, '_m_fsize'):
                return self._m_fsize

            self._m_fsize = int(self.filesize, 8)
            return getattr(self, '_m_fsize', None)

        @property
        def hsize(self):
            if hasattr(self, '_m_hsize'):
                return self._m_hsize

            self._m_hsize = 2 * 11 + 9 * 6
            return getattr(self, '_m_hsize', None)

        @property
        def npaddingsize(self):
            if hasattr(self, '_m_npaddingsize'):
                return self._m_npaddingsize

            self._m_npaddingsize = 0
            return getattr(self, '_m_npaddingsize', None)

        @property
        def nsize(self):
            if hasattr(self, '_m_nsize'):
                return self._m_nsize

            self._m_nsize = int(self.namesize, 8)
            return getattr(self, '_m_nsize', None)


    class CpioPortableAsciiHeaderAndFile(KaitaiStruct):
        SEQ_FIELDS = ["header", "filename", "filedata"]
        def __init__(self, _io, _parent=None, _root=None):
            super(CpioPortableAscii.CpioPortableAsciiHeaderAndFile, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = CpioPortableAscii.CpioPortableAsciiHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['filename']['start'] = self._io.pos()
            self.filename = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.header.nsize), 0, False)).decode(u"ASCII")
            self._debug['filename']['end'] = self._io.pos()
            self._debug['filedata']['start'] = self._io.pos()
            self.filedata = self._io.read_bytes(self.header.fsize)
            self._debug['filedata']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()


    @property
    def trailing_filename(self):
        if hasattr(self, '_m_trailing_filename'):
            return self._m_trailing_filename

        self._m_trailing_filename = u"TRAILER!!!"
        return getattr(self, '_m_trailing_filename', None)


