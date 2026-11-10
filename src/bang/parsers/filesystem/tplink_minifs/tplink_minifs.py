# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class TplinkMinifs(KaitaiStruct):
    """MINIFS is a file system found in certain TP-Link firmware files, such as
    RE450(V4)_210531.zip, for TP-Link's own TPOS RTOS.
    
    It consists of a header, followed by a list of file names, followed by
    meta information for each file, meta information about the LZMA compressed
    blobs including length, offset and uncompressed length, and then a number
    of LZMA compressed blobs.
    
    The LZMA blobs can contain the concatenated contents of multiple files.
    The meta information of a file contains an offset to the directory name,
    a file name, the LZMA blob (numbering starts at 0), the offset of the file
    in the uncompressed data and the size of the uncompressed file.
    """
    SEQ_FIELDS = ["header", "filenames", "inodes", "lzma_metas", "lzma_blobs_area"]
    def __init__(self, _io, _parent=None, _root=None):
        super(TplinkMinifs, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(32)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = TplinkMinifs.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['filenames']['start'] = self._io.pos()
        self._raw_filenames = self._io.read_bytes(self.header.len_filenames)
        _io__raw_filenames = KaitaiStream(BytesIO(self._raw_filenames))
        self.filenames = TplinkMinifs.Filenames(_io__raw_filenames, self, self._root)
        self._debug['filenames']['end'] = self._io.pos()
        self._debug['inodes']['start'] = self._io.pos()
        self._debug['inodes']['arr'] = []
        self.inodes = []
        for i in range(self.header.num_files):
            self._debug['inodes']['arr'].append({'start': self._io.pos()})
            self.inodes.append(TplinkMinifs.Inode((self.inodes[i - 1].cur_max_lzma_blob if i != 0 else 0), self._io, self, self._root))
            self._debug['inodes']['arr'][i]['end'] = self._io.pos()

        self._debug['inodes']['end'] = self._io.pos()
        self._debug['lzma_metas']['start'] = self._io.pos()
        self._debug['lzma_metas']['arr'] = []
        self.lzma_metas = []
        for i in range(self.inodes[-1].cur_max_lzma_blob + 1):
            self._debug['lzma_metas']['arr'].append({'start': self._io.pos()})
            self.lzma_metas.append(TplinkMinifs.LzmaMeta((self.lzma_metas[i - 1].ofs_end if i != 0 else 0), self._io, self, self._root))
            self._debug['lzma_metas']['arr'][i]['end'] = self._io.pos()

        self._debug['lzma_metas']['end'] = self._io.pos()
        self._debug['lzma_blobs_area']['start'] = self._io.pos()
        self._raw_lzma_blobs_area = self._io.read_bytes(self.lzma_metas[-1].ofs_end)
        _io__raw_lzma_blobs_area = KaitaiStream(BytesIO(self._raw_lzma_blobs_area))
        self.lzma_blobs_area = TplinkMinifs.Dummy(_io__raw_lzma_blobs_area, self, self._root)
        self._debug['lzma_blobs_area']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.filenames._fetch_instances()
        for i in range(len(self.inodes)):
            pass
            self.inodes[i]._fetch_instances()

        for i in range(len(self.lzma_metas)):
            pass
            self.lzma_metas[i]._fetch_instances()

        self.lzma_blobs_area._fetch_instances()
        _ = self.lzma_blobs
        if hasattr(self, '_m_lzma_blobs'):
            pass
            for i in range(len(self._m_lzma_blobs)):
                pass
                self._m_lzma_blobs[i]._fetch_instances()



    class Dummy(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(TplinkMinifs.Dummy, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class Filenames(KaitaiStruct):
        SEQ_FIELDS = ["filename"]
        def __init__(self, _io, _parent=None, _root=None):
            super(TplinkMinifs.Filenames, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['filename']['start'] = self._io.pos()
            self._debug['filename']['arr'] = []
            self.filename = []
            i = 0
            while not self._io.is_eof():
                self._debug['filename']['arr'].append({'start': self._io.pos()})
                self.filename.append((self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII"))
                self._debug['filename']['arr'][len(self.filename) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['filename']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.filename)):
                pass



    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "unknown_1", "num_files", "unknown_2", "len_filenames"]
        def __init__(self, _io, _parent=None, _root=None):
            super(TplinkMinifs.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(16)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x4D\x49\x4E\x49\x46\x53\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x4D\x49\x4E\x49\x46\x53\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.magic, self._io, u"/types/header/seq/0")
            self._debug['unknown_1']['start'] = self._io.pos()
            self.unknown_1 = self._io.read_u4be()
            self._debug['unknown_1']['end'] = self._io.pos()
            self._debug['num_files']['start'] = self._io.pos()
            self.num_files = self._io.read_u4be()
            self._debug['num_files']['end'] = self._io.pos()
            self._debug['unknown_2']['start'] = self._io.pos()
            self.unknown_2 = self._io.read_u4be()
            self._debug['unknown_2']['end'] = self._io.pos()
            self._debug['len_filenames']['start'] = self._io.pos()
            self.len_filenames = self._io.read_u4be()
            self._debug['len_filenames']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Inode(KaitaiStruct):
        SEQ_FIELDS = ["ofs_directory", "ofs_name", "lzma_blob", "ofs_file", "size"]
        def __init__(self, prev_max_lzma_blob, _io, _parent=None, _root=None):
            super(TplinkMinifs.Inode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.prev_max_lzma_blob = prev_max_lzma_blob
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_directory']['start'] = self._io.pos()
            self.ofs_directory = self._io.read_u4be()
            self._debug['ofs_directory']['end'] = self._io.pos()
            self._debug['ofs_name']['start'] = self._io.pos()
            self.ofs_name = self._io.read_u4be()
            self._debug['ofs_name']['end'] = self._io.pos()
            self._debug['lzma_blob']['start'] = self._io.pos()
            self.lzma_blob = self._io.read_u4be()
            self._debug['lzma_blob']['end'] = self._io.pos()
            self._debug['ofs_file']['start'] = self._io.pos()
            self.ofs_file = self._io.read_u4be()
            self._debug['ofs_file']['end'] = self._io.pos()
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4be()
            self._debug['size']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.directory_name
            if hasattr(self, '_m_directory_name'):
                pass

            _ = self.filename
            if hasattr(self, '_m_filename'):
                pass


        @property
        def cur_max_lzma_blob(self):
            if hasattr(self, '_m_cur_max_lzma_blob'):
                return self._m_cur_max_lzma_blob

            self._m_cur_max_lzma_blob = (self.lzma_blob if self.lzma_blob > self.prev_max_lzma_blob else self.prev_max_lzma_blob)
            return getattr(self, '_m_cur_max_lzma_blob', None)

        @property
        def directory_name(self):
            if hasattr(self, '_m_directory_name'):
                return self._m_directory_name

            io = self._root.filenames._io
            _pos = io.pos()
            io.seek(self.ofs_directory)
            self._debug['_m_directory_name']['start'] = io.pos()
            self._m_directory_name = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['_m_directory_name']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_directory_name', None)

        @property
        def filename(self):
            if hasattr(self, '_m_filename'):
                return self._m_filename

            io = self._root.filenames._io
            _pos = io.pos()
            io.seek(self.ofs_name)
            self._debug['_m_filename']['start'] = io.pos()
            self._m_filename = (io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['_m_filename']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_filename', None)


    class LzmaBlob(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, index, _io, _parent=None, _root=None):
            super(TplinkMinifs.LzmaBlob, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.index = index
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.data
            if hasattr(self, '_m_data'):
                pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            _pos = self._io.pos()
            self._io.seek(self._root.lzma_metas[self.index].ofs_blob)
            self._debug['_m_data']['start'] = self._io.pos()
            self._m_data = self._io.read_bytes(self._root.lzma_metas[self.index].len_blob)
            self._debug['_m_data']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_data', None)


    class LzmaMeta(KaitaiStruct):
        SEQ_FIELDS = ["ofs_blob", "len_blob", "len_blob_uncompressed"]
        def __init__(self, prev_ofs_end, _io, _parent=None, _root=None):
            super(TplinkMinifs.LzmaMeta, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.prev_ofs_end = prev_ofs_end
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_blob']['start'] = self._io.pos()
            self.ofs_blob = self._io.read_u4be()
            self._debug['ofs_blob']['end'] = self._io.pos()
            if not self.ofs_blob == self.prev_ofs_end:
                raise kaitaistruct.ValidationNotEqualError(self.prev_ofs_end, self.ofs_blob, self._io, u"/types/lzma_meta/seq/0")
            self._debug['len_blob']['start'] = self._io.pos()
            self.len_blob = self._io.read_u4be()
            self._debug['len_blob']['end'] = self._io.pos()
            self._debug['len_blob_uncompressed']['start'] = self._io.pos()
            self.len_blob_uncompressed = self._io.read_u4be()
            self._debug['len_blob_uncompressed']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def ofs_end(self):
            if hasattr(self, '_m_ofs_end'):
                return self._m_ofs_end

            self._m_ofs_end = self.ofs_blob + self.len_blob
            return getattr(self, '_m_ofs_end', None)


    @property
    def lzma_blobs(self):
        if hasattr(self, '_m_lzma_blobs'):
            return self._m_lzma_blobs

        io = self._root.lzma_blobs_area._io
        self._debug['_m_lzma_blobs']['start'] = io.pos()
        self._debug['_m_lzma_blobs']['arr'] = []
        self._m_lzma_blobs = []
        for i in range(self._root.inodes[-1].cur_max_lzma_blob + 1):
            self._debug['_m_lzma_blobs']['arr'].append({'start': io.pos()})
            self._m_lzma_blobs.append(TplinkMinifs.LzmaBlob(i, io, self, self._root))
            self._debug['_m_lzma_blobs']['arr'][i]['end'] = io.pos()

        self._debug['_m_lzma_blobs']['end'] = io.pos()
        return getattr(self, '_m_lzma_blobs', None)


