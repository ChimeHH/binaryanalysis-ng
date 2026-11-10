# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class CpioOldBinary(KaitaiStruct):
    SEQ_FIELDS = ["entries"]
    def __init__(self, _io, _parent=None, _root=None):
        super(CpioOldBinary, self).__init__(_io)
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
            _ = CpioOldBinary.CpioOldBinaryHeaderAndFile(self._io, self, self._root)
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


    class CpioOldBinaryHeader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "dev", "ino", "mode", "uid", "gid", "nlink", "rdev", "mtime", "namesize", "filesize"]
        def __init__(self, _io, _parent=None, _root=None):
            super(CpioOldBinary.CpioOldBinaryHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\xC7\x71":
                raise kaitaistruct.ValidationNotEqualError(b"\xC7\x71", self.magic, self._io, u"/types/cpio_old_binary_header/seq/0")
            self._debug['dev']['start'] = self._io.pos()
            self.dev = self._io.read_u2le()
            self._debug['dev']['end'] = self._io.pos()
            self._debug['ino']['start'] = self._io.pos()
            self.ino = self._io.read_u2le()
            self._debug['ino']['end'] = self._io.pos()
            self._debug['mode']['start'] = self._io.pos()
            self.mode = self._io.read_u2le()
            self._debug['mode']['end'] = self._io.pos()
            self._debug['uid']['start'] = self._io.pos()
            self.uid = self._io.read_u2le()
            self._debug['uid']['end'] = self._io.pos()
            self._debug['gid']['start'] = self._io.pos()
            self.gid = self._io.read_u2le()
            self._debug['gid']['end'] = self._io.pos()
            self._debug['nlink']['start'] = self._io.pos()
            self.nlink = self._io.read_u2le()
            self._debug['nlink']['end'] = self._io.pos()
            self._debug['rdev']['start'] = self._io.pos()
            self.rdev = self._io.read_u2le()
            self._debug['rdev']['end'] = self._io.pos()
            self._debug['mtime']['start'] = self._io.pos()
            self.mtime = CpioOldBinary.FourByteUnsignedInteger(self._io, self, self._root)
            self._debug['mtime']['end'] = self._io.pos()
            self._debug['namesize']['start'] = self._io.pos()
            self.namesize = self._io.read_u2le()
            self._debug['namesize']['end'] = self._io.pos()
            self._debug['filesize']['start'] = self._io.pos()
            self.filesize = CpioOldBinary.FourByteUnsignedInteger(self._io, self, self._root)
            self._debug['filesize']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.mtime._fetch_instances()
            self.filesize._fetch_instances()

        @property
        def bsize(self):
            if hasattr(self, '_m_bsize'):
                return self._m_bsize

            self._m_bsize = (((self.hsize + self.nsize) + self.npaddingsize) + self.fsize) + self.fpaddingsize
            return getattr(self, '_m_bsize', None)

        @property
        def checked_filesize(self):
            if hasattr(self, '_m_checked_filesize'):
                return self._m_checked_filesize

            self._m_checked_filesize = (self.fsize if self.fsize < self._root._io.size() else -1)
            return getattr(self, '_m_checked_filesize', None)

        @property
        def cpio_mode(self):
            if hasattr(self, '_m_cpio_mode'):
                return self._m_cpio_mode

            self._m_cpio_mode = self.mode
            return getattr(self, '_m_cpio_mode', None)

        @property
        def fpaddingsize(self):
            if hasattr(self, '_m_fpaddingsize'):
                return self._m_fpaddingsize

            self._m_fpaddingsize = self.fsize % 2
            return getattr(self, '_m_fpaddingsize', None)

        @property
        def fsize(self):
            if hasattr(self, '_m_fsize'):
                return self._m_fsize

            self._m_fsize = self.filesize.value
            return getattr(self, '_m_fsize', None)

        @property
        def hsize(self):
            if hasattr(self, '_m_hsize'):
                return self._m_hsize

            self._m_hsize = 9 * 2 + 2 * 4
            return getattr(self, '_m_hsize', None)

        @property
        def npaddingsize(self):
            if hasattr(self, '_m_npaddingsize'):
                return self._m_npaddingsize

            self._m_npaddingsize = self.nsize % 2
            return getattr(self, '_m_npaddingsize', None)

        @property
        def nsize(self):
            if hasattr(self, '_m_nsize'):
                return self._m_nsize

            self._m_nsize = self.namesize
            return getattr(self, '_m_nsize', None)


    class CpioOldBinaryHeaderAndFile(KaitaiStruct):
        SEQ_FIELDS = ["header", "filename", "filename_padding", "filedata", "filedata_padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(CpioOldBinary.CpioOldBinaryHeaderAndFile, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = CpioOldBinary.CpioOldBinaryHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['filename']['start'] = self._io.pos()
            self.filename = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.header.nsize), 0, False)).decode(u"ASCII")
            self._debug['filename']['end'] = self._io.pos()
            self._debug['filename_padding']['start'] = self._io.pos()
            self.filename_padding = self._io.read_bytes(self.header.npaddingsize)
            self._debug['filename_padding']['end'] = self._io.pos()
            self._debug['filedata']['start'] = self._io.pos()
            self.filedata = self._io.read_bytes(self.header.checked_filesize)
            self._debug['filedata']['end'] = self._io.pos()
            self._debug['filedata_padding']['start'] = self._io.pos()
            self.filedata_padding = self._io.read_bytes(self.header.fpaddingsize)
            self._debug['filedata_padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()


    class FourByteUnsignedInteger(KaitaiStruct):
        SEQ_FIELDS = ["msb", "lsb"]
        def __init__(self, _io, _parent=None, _root=None):
            super(CpioOldBinary.FourByteUnsignedInteger, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['msb']['start'] = self._io.pos()
            self.msb = self._io.read_u2le()
            self._debug['msb']['end'] = self._io.pos()
            self._debug['lsb']['start'] = self._io.pos()
            self.lsb = self._io.read_u2le()
            self._debug['lsb']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.lsb + (self.msb << 16)
            return getattr(self, '_m_value', None)


    @property
    def trailing_filename(self):
        if hasattr(self, '_m_trailing_filename'):
            return self._m_trailing_filename

        self._m_trailing_filename = u"TRAILER!!!"
        return getattr(self, '_m_trailing_filename', None)


