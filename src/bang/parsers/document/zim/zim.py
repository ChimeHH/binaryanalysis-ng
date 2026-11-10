# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Zim(KaitaiStruct):
    """Test files: https://wiki.kiwix.org/wiki/Content_in_all_languages
    
    .. seealso::
       Source - https://wiki.openzim.org/wiki/ZIM_file_format
    
    
    .. seealso::
       Source - https://wiki.openzim.org/wiki/ZIM_File_Example
    """

    class Compression(IntEnum):
        no_compression = 0
        no_compression2 = 1
        zlib = 2
        bzip2 = 3
        xz = 4
        zstd = 5

    class Namespace(IntEnum):
        layout = 45
        article = 65
        article_meta_data = 66
        user_content_entries = 67
        unknown = 72
        images_files = 73
        images_text = 74
        metadata = 77
        categories_text = 85
        categories_article_list = 86
        categories_per_article_or_well_known_entries = 87
        search_indexes = 88
        xapian_indexes = 90

    class NamespaceType(IntEnum):
        old_namespace = 0
        new_namespace = 1
    SEQ_FIELDS = ["header", "mimetypes"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Zim, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Zim.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['mimetypes']['start'] = self._io.pos()
        self.mimetypes = Zim.Mimetypes(self._io, self, self._root)
        self._debug['mimetypes']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.mimetypes._fetch_instances()
        _ = self.checksum
        if hasattr(self, '_m_checksum'):
            pass

        _ = self.clusters
        if hasattr(self, '_m_clusters'):
            pass
            self._m_clusters._fetch_instances()

        _ = self.titles
        if hasattr(self, '_m_titles'):
            pass
            self._m_titles._fetch_instances()

        _ = self.url_pointers
        if hasattr(self, '_m_url_pointers'):
            pass
            self._m_url_pointers._fetch_instances()


    class Cluster(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, i, _io, _parent=None, _root=None):
            super(Zim.Cluster, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.i = i
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.cluster
            if hasattr(self, '_m_cluster'):
                pass
                self._m_cluster._fetch_instances()


        @property
        def cluster(self):
            if hasattr(self, '_m_cluster'):
                return self._m_cluster

            io = self._root._io
            _pos = io.pos()
            io.seek(self._parent.cluster_offsets[self.i])
            self._debug['_m_cluster']['start'] = io.pos()
            self._raw__m_cluster = io.read_bytes(self.ofs_end - self.ofs_start)
            _io__raw__m_cluster = KaitaiStream(BytesIO(self._raw__m_cluster))
            self._m_cluster = Zim.ClusterBody(_io__raw__m_cluster, self, self._root)
            self._debug['_m_cluster']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_cluster', None)

        @property
        def ofs_end(self):
            if hasattr(self, '_m_ofs_end'):
                return self._m_ofs_end

            self._m_ofs_end = (self._parent.cluster_offsets[self.i + 1] if self.i < len(self._parent.cluster_offsets) - 1 else self._root.header.checksum)
            return getattr(self, '_m_ofs_end', None)

        @property
        def ofs_start(self):
            if hasattr(self, '_m_ofs_start'):
                return self._m_ofs_start

            self._m_ofs_start = self._parent.cluster_offsets[self.i]
            return getattr(self, '_m_ofs_start', None)


    class ClusterBody(KaitaiStruct):
        SEQ_FIELDS = ["flag", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.ClusterBody, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flag']['start'] = self._io.pos()
            self.flag = Zim.ClusterFlag(self._io, self, self._root)
            self._debug['flag']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.flag.compressed
            if _on == Zim.Compression.no_compression:
                pass
                self.body = Zim.ClusterPointers(self.flag.offset_size, self._io, self, self._root)
            elif _on == Zim.Compression.no_compression2:
                pass
                self.body = Zim.ClusterPointers(self.flag.offset_size, self._io, self, self._root)
            else:
                pass
                self.body = Zim.Raw(self._io, self, self._root)
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.flag._fetch_instances()
            _on = self.flag.compressed
            if _on == Zim.Compression.no_compression:
                pass
                self.body._fetch_instances()
            elif _on == Zim.Compression.no_compression2:
                pass
                self.body._fetch_instances()
            else:
                pass
                self.body._fetch_instances()


    class ClusterFlag(KaitaiStruct):
        SEQ_FIELDS = ["reserved1", "extended", "compressed"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.ClusterFlag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved1']['start'] = self._io.pos()
            self.reserved1 = self._io.read_bits_int_be(3)
            self._debug['reserved1']['end'] = self._io.pos()
            self._debug['extended']['start'] = self._io.pos()
            self.extended = self._io.read_bits_int_be(1) != 0
            self._debug['extended']['end'] = self._io.pos()
            self._debug['compressed']['start'] = self._io.pos()
            self.compressed = KaitaiStream.resolve_enum(Zim.Compression, self._io.read_bits_int_be(4))
            self._debug['compressed']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def offset_size(self):
            if hasattr(self, '_m_offset_size'):
                return self._m_offset_size

            self._m_offset_size = (8 if self.extended else 4)
            return getattr(self, '_m_offset_size', None)


    class ClusterPointers(KaitaiStruct):
        SEQ_FIELDS = ["offsets"]
        def __init__(self, offset_size, _io, _parent=None, _root=None):
            super(Zim.ClusterPointers, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.offset_size = offset_size
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['offsets']['start'] = self._io.pos()
            self._debug['offsets']['arr'] = []
            self.offsets = []
            for i in range(self.num_blobs):
                self._debug['offsets']['arr'].append({'start': self._io.pos()})
                _on = self.offset_size
                if _on == 4:
                    pass
                    self.offsets.append(self._io.read_u4le())
                elif _on == 8:
                    pass
                    self.offsets.append(self._io.read_u8le())
                self._debug['offsets']['arr'][i]['end'] = self._io.pos()

            self._debug['offsets']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.offsets)):
                pass
                _on = self.offset_size
                if _on == 4:
                    pass
                elif _on == 8:
                    pass

            _ = self.blobs
            if hasattr(self, '_m_blobs'):
                pass
                for i in range(len(self._m_blobs)):
                    pass
                    self._m_blobs[i]._fetch_instances()


            _ = self.first_offset
            if hasattr(self, '_m_first_offset'):
                pass
                _on = self.offset_size
                if _on == 4:
                    pass
                elif _on == 8:
                    pass


        class Blobs(KaitaiStruct):
            SEQ_FIELDS = []
            def __init__(self, index, _io, _parent=None, _root=None):
                super(Zim.ClusterPointers.Blobs, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self.index = index
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                pass


            def _fetch_instances(self):
                pass
                _ = self.blob
                if hasattr(self, '_m_blob'):
                    pass


            @property
            def blob(self):
                if hasattr(self, '_m_blob'):
                    return self._m_blob

                _pos = self._io.pos()
                self._io.seek(self._parent.offsets[self.index] + 1)
                self._debug['_m_blob']['start'] = self._io.pos()
                self._m_blob = self._io.read_bytes(self.end - self.start)
                self._debug['_m_blob']['end'] = self._io.pos()
                self._io.seek(_pos)
                return getattr(self, '_m_blob', None)

            @property
            def end(self):
                if hasattr(self, '_m_end'):
                    return self._m_end

                self._m_end = self._parent.offsets[self.index + 1]
                return getattr(self, '_m_end', None)

            @property
            def start(self):
                if hasattr(self, '_m_start'):
                    return self._m_start

                self._m_start = self._parent.offsets[self.index]
                return getattr(self, '_m_start', None)


        @property
        def blobs(self):
            """The last pointer points to the end of the data area.
            So there is always one more offset than blobs.
            """
            if hasattr(self, '_m_blobs'):
                return self._m_blobs

            self._debug['_m_blobs']['start'] = self._io.pos()
            self._debug['_m_blobs']['arr'] = []
            self._m_blobs = []
            for i in range(self.num_blobs - 1):
                self._debug['_m_blobs']['arr'].append({'start': self._io.pos()})
                self._m_blobs.append(Zim.ClusterPointers.Blobs(i, self._io, self, self._root))
                self._debug['_m_blobs']['arr'][i]['end'] = self._io.pos()

            self._debug['_m_blobs']['end'] = self._io.pos()
            return getattr(self, '_m_blobs', None)

        @property
        def first_offset(self):
            if hasattr(self, '_m_first_offset'):
                return self._m_first_offset

            _pos = self._io.pos()
            self._io.seek(1)
            self._debug['_m_first_offset']['start'] = self._io.pos()
            _on = self.offset_size
            if _on == 4:
                pass
                self._m_first_offset = self._io.read_u4le()
            elif _on == 8:
                pass
                self._m_first_offset = self._io.read_u8le()
            self._debug['_m_first_offset']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_first_offset', None)

        @property
        def num_blobs(self):
            """Since the first offset points to the start of the first data,
            the number of offsets can be determined by dividing this offset
            by OFFSET_SIZE.
            """
            if hasattr(self, '_m_num_blobs'):
                return self._m_num_blobs

            self._m_num_blobs = self.first_offset // self.offset_size
            return getattr(self, '_m_num_blobs', None)


    class Clusters(KaitaiStruct):
        SEQ_FIELDS = ["cluster_offsets"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.Clusters, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['cluster_offsets']['start'] = self._io.pos()
            self._debug['cluster_offsets']['arr'] = []
            self.cluster_offsets = []
            for i in range(self._root.header.num_clusters):
                self._debug['cluster_offsets']['arr'].append({'start': self._io.pos()})
                self.cluster_offsets.append(self._io.read_u8le())
                self._debug['cluster_offsets']['arr'][i]['end'] = self._io.pos()

            self._debug['cluster_offsets']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.cluster_offsets)):
                pass

            _ = self.clusters
            if hasattr(self, '_m_clusters'):
                pass
                for i in range(len(self._m_clusters)):
                    pass
                    self._m_clusters[i]._fetch_instances()



        @property
        def clusters(self):
            if hasattr(self, '_m_clusters'):
                return self._m_clusters

            self._debug['_m_clusters']['start'] = self._io.pos()
            self._debug['_m_clusters']['arr'] = []
            self._m_clusters = []
            for i in range(self._root.header.num_clusters):
                self._debug['_m_clusters']['arr'].append({'start': self._io.pos()})
                self._m_clusters.append(Zim.Cluster(i, self._io, self, self._root))
                self._debug['_m_clusters']['arr'][i]['end'] = self._io.pos()

            self._debug['_m_clusters']['end'] = self._io.pos()
            return getattr(self, '_m_clusters', None)


    class Content(KaitaiStruct):
        SEQ_FIELDS = ["len_parameter", "namespace", "revision", "cluster_number", "blob_number", "url", "title", "parameter"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.Content, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_parameter']['start'] = self._io.pos()
            self.len_parameter = self._io.read_u1()
            self._debug['len_parameter']['end'] = self._io.pos()
            if not self.len_parameter == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.len_parameter, self._io, u"/types/content/seq/0")
            self._debug['namespace']['start'] = self._io.pos()
            self.namespace = KaitaiStream.resolve_enum(Zim.Namespace, self._io.read_u1())
            self._debug['namespace']['end'] = self._io.pos()
            self._debug['revision']['start'] = self._io.pos()
            self.revision = self._io.read_u4le()
            self._debug['revision']['end'] = self._io.pos()
            self._debug['cluster_number']['start'] = self._io.pos()
            self.cluster_number = self._io.read_u4le()
            self._debug['cluster_number']['end'] = self._io.pos()
            self._debug['blob_number']['start'] = self._io.pos()
            self.blob_number = self._io.read_u4le()
            self._debug['blob_number']['end'] = self._io.pos()
            self._debug['url']['start'] = self._io.pos()
            self.url = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['url']['end'] = self._io.pos()
            self._debug['title']['start'] = self._io.pos()
            self.title = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['title']['end'] = self._io.pos()
            self._debug['parameter']['start'] = self._io.pos()
            self.parameter = self._io.read_bytes(self.len_parameter)
            self._debug['parameter']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Entry(KaitaiStruct):
        SEQ_FIELDS = ["mimetype", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.Entry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['mimetype']['start'] = self._io.pos()
            self.mimetype = self._io.read_u2le()
            self._debug['mimetype']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.mimetype
            if _on == 65535:
                pass
                self.body = Zim.Redirect(self._io, self, self._root)
            else:
                pass
                self.body = Zim.Content(self._io, self, self._root)
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.mimetype
            if _on == 65535:
                pass
                self.body._fetch_instances()
            else:
                pass
                self.body._fetch_instances()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "uuid", "num_articles", "num_clusters", "ofs_url_pointer", "ofs_title_pointer", "ofs_cluster_pointer", "ofs_mimelist_pointer", "main_page", "layout_page", "checksum"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x5A\x49\x4D\x04":
                raise kaitaistruct.ValidationNotEqualError(b"\x5A\x49\x4D\x04", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = Zim.Version(self._io, self, self._root)
            self._debug['version']['end'] = self._io.pos()
            self._debug['uuid']['start'] = self._io.pos()
            self.uuid = self._io.read_bytes(16)
            self._debug['uuid']['end'] = self._io.pos()
            self._debug['num_articles']['start'] = self._io.pos()
            self.num_articles = self._io.read_u4le()
            self._debug['num_articles']['end'] = self._io.pos()
            self._debug['num_clusters']['start'] = self._io.pos()
            self.num_clusters = self._io.read_u4le()
            self._debug['num_clusters']['end'] = self._io.pos()
            self._debug['ofs_url_pointer']['start'] = self._io.pos()
            self.ofs_url_pointer = self._io.read_u8le()
            self._debug['ofs_url_pointer']['end'] = self._io.pos()
            self._debug['ofs_title_pointer']['start'] = self._io.pos()
            self.ofs_title_pointer = self._io.read_u8le()
            self._debug['ofs_title_pointer']['end'] = self._io.pos()
            self._debug['ofs_cluster_pointer']['start'] = self._io.pos()
            self.ofs_cluster_pointer = self._io.read_u8le()
            self._debug['ofs_cluster_pointer']['end'] = self._io.pos()
            self._debug['ofs_mimelist_pointer']['start'] = self._io.pos()
            self.ofs_mimelist_pointer = self._io.read_u8le()
            self._debug['ofs_mimelist_pointer']['end'] = self._io.pos()
            self._debug['main_page']['start'] = self._io.pos()
            self.main_page = self._io.read_u4le()
            self._debug['main_page']['end'] = self._io.pos()
            self._debug['layout_page']['start'] = self._io.pos()
            self.layout_page = self._io.read_u4le()
            self._debug['layout_page']['end'] = self._io.pos()
            self._debug['checksum']['start'] = self._io.pos()
            self.checksum = self._io.read_u8le()
            self._debug['checksum']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.version._fetch_instances()


    class Mimetypes(KaitaiStruct):
        SEQ_FIELDS = ["mimetype"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.Mimetypes, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['mimetype']['start'] = self._io.pos()
            self._debug['mimetype']['arr'] = []
            self.mimetype = []
            i = 0
            while True:
                self._debug['mimetype']['arr'].append({'start': self._io.pos()})
                _ = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self.mimetype.append(_)
                self._debug['mimetype']['arr'][len(self.mimetype) - 1]['end'] = self._io.pos()
                if _ == u"":
                    break
                i += 1
            self._debug['mimetype']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.mimetype)):
                pass



    class Raw(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.Raw, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes_full()
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Redirect(KaitaiStruct):
        SEQ_FIELDS = ["len_parameter", "namespace", "revision", "redirect_index", "url", "title", "parameter"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.Redirect, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_parameter']['start'] = self._io.pos()
            self.len_parameter = self._io.read_u1()
            self._debug['len_parameter']['end'] = self._io.pos()
            if not self.len_parameter == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.len_parameter, self._io, u"/types/redirect/seq/0")
            self._debug['namespace']['start'] = self._io.pos()
            self.namespace = KaitaiStream.resolve_enum(Zim.Namespace, self._io.read_u1())
            self._debug['namespace']['end'] = self._io.pos()
            self._debug['revision']['start'] = self._io.pos()
            self.revision = self._io.read_u4le()
            self._debug['revision']['end'] = self._io.pos()
            self._debug['redirect_index']['start'] = self._io.pos()
            self.redirect_index = self._io.read_u4le()
            self._debug['redirect_index']['end'] = self._io.pos()
            self._debug['url']['start'] = self._io.pos()
            self.url = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['url']['end'] = self._io.pos()
            self._debug['title']['start'] = self._io.pos()
            self.title = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['title']['end'] = self._io.pos()
            self._debug['parameter']['start'] = self._io.pos()
            self.parameter = self._io.read_bytes(self.len_parameter)
            self._debug['parameter']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Titles(KaitaiStruct):
        SEQ_FIELDS = ["title"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.Titles, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['title']['start'] = self._io.pos()
            self._debug['title']['arr'] = []
            self.title = []
            for i in range(self._root.header.num_articles):
                self._debug['title']['arr'].append({'start': self._io.pos()})
                self.title.append(self._io.read_u4le())
                self._debug['title']['arr'][i]['end'] = self._io.pos()

            self._debug['title']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.title)):
                pass



    class UrlPointer(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, index, _io, _parent=None, _root=None):
            super(Zim.UrlPointer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.index = index
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.entry
            if hasattr(self, '_m_entry'):
                pass
                self._m_entry._fetch_instances()


        @property
        def entry(self):
            if hasattr(self, '_m_entry'):
                return self._m_entry

            io = self._root._io
            _pos = io.pos()
            io.seek(self._root.url_pointers.url_pointers[self.index])
            self._debug['_m_entry']['start'] = io.pos()
            self._m_entry = Zim.Entry(io, self, self._root)
            self._debug['_m_entry']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_entry', None)


    class UrlPointers(KaitaiStruct):
        SEQ_FIELDS = ["url_pointers"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.UrlPointers, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['url_pointers']['start'] = self._io.pos()
            self._debug['url_pointers']['arr'] = []
            self.url_pointers = []
            for i in range(self._root.header.num_articles):
                self._debug['url_pointers']['arr'].append({'start': self._io.pos()})
                self.url_pointers.append(self._io.read_u8le())
                self._debug['url_pointers']['arr'][i]['end'] = self._io.pos()

            self._debug['url_pointers']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.url_pointers)):
                pass

            _ = self.entries
            if hasattr(self, '_m_entries'):
                pass
                for i in range(len(self._m_entries)):
                    pass
                    self._m_entries[i]._fetch_instances()



        @property
        def entries(self):
            if hasattr(self, '_m_entries'):
                return self._m_entries

            self._debug['_m_entries']['start'] = self._io.pos()
            self._debug['_m_entries']['arr'] = []
            self._m_entries = []
            for i in range(self._root.header.num_articles):
                self._debug['_m_entries']['arr'].append({'start': self._io.pos()})
                self._m_entries.append(Zim.UrlPointer(i, self._io, self, self._root))
                self._debug['_m_entries']['arr'][i]['end'] = self._io.pos()

            self._debug['_m_entries']['end'] = self._io.pos()
            return getattr(self, '_m_entries', None)


    class Version(KaitaiStruct):
        SEQ_FIELDS = ["major", "minor"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zim.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u2le()
            self._debug['major']['end'] = self._io.pos()
            if not  ((self.major == 5) or (self.major == 6)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.major, self._io, u"/types/version/seq/0")
            self._debug['minor']['start'] = self._io.pos()
            self.minor = KaitaiStream.resolve_enum(Zim.NamespaceType, self._io.read_u2le())
            self._debug['minor']['end'] = self._io.pos()
            if not  ((self.minor == Zim.NamespaceType.old_namespace) or (self.minor == Zim.NamespaceType.new_namespace)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.minor, self._io, u"/types/version/seq/1")


        def _fetch_instances(self):
            pass


    @property
    def checksum(self):
        if hasattr(self, '_m_checksum'):
            return self._m_checksum

        _pos = self._io.pos()
        self._io.seek(self.header.checksum)
        self._debug['_m_checksum']['start'] = self._io.pos()
        self._m_checksum = self._io.read_bytes(16)
        self._debug['_m_checksum']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_checksum', None)

    @property
    def clusters(self):
        if hasattr(self, '_m_clusters'):
            return self._m_clusters

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_cluster_pointer)
        self._debug['_m_clusters']['start'] = self._io.pos()
        self._m_clusters = Zim.Clusters(self._io, self, self._root)
        self._debug['_m_clusters']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_clusters', None)

    @property
    def titles(self):
        if hasattr(self, '_m_titles'):
            return self._m_titles

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_title_pointer)
        self._debug['_m_titles']['start'] = self._io.pos()
        self._m_titles = Zim.Titles(self._io, self, self._root)
        self._debug['_m_titles']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_titles', None)

    @property
    def url_pointers(self):
        if hasattr(self, '_m_url_pointers'):
            return self._m_url_pointers

        _pos = self._io.pos()
        self._io.seek(self.header.ofs_url_pointer)
        self._debug['_m_url_pointers']['start'] = self._io.pos()
        self._m_url_pointers = Zim.UrlPointers(self._io, self, self._root)
        self._debug['_m_url_pointers']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_url_pointers', None)


