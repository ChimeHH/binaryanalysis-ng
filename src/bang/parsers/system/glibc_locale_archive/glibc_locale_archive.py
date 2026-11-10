# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class GlibcLocaleArchive(KaitaiStruct):
    """
    .. seealso::
       Source - https://sourceware.org/git/?p=glibc.git;a=blob;f=locale/locarchive.h;h=012ffd03f30c5f7535e8d9053afbc5c1a35acc94;hb=HEAD
    """

    class Category(IntEnum):
        messages = 537071888
        monetary = 537071889
        paper = 537071890
        all = 537071891
        numeric = 537071892
        ctype_variant = 537071893
        collate_variant = 537071894
        time = 537071895
        identification = 537071897
        address = 537071900
        name = 537071901
        measurement = 537071902
        telephone = 537071903
        collate = 537202711
        ctype = 537462560
    SEQ_FIELDS = ["magic", "serial", "ofs_namehash", "namehash_used", "num_namehash", "ofs_string", "string_used", "num_string", "ofs_locrec_table", "locrectab_used", "num_locrectab", "ofs_sumhash", "sumhash_used", "num_sumhash"]
    def __init__(self, _io, _parent=None, _root=None):
        super(GlibcLocaleArchive, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_u4le()
        self._debug['magic']['end'] = self._io.pos()
        self._debug['serial']['start'] = self._io.pos()
        self.serial = self._io.read_u4le()
        self._debug['serial']['end'] = self._io.pos()
        self._debug['ofs_namehash']['start'] = self._io.pos()
        self.ofs_namehash = self._io.read_u4le()
        self._debug['ofs_namehash']['end'] = self._io.pos()
        self._debug['namehash_used']['start'] = self._io.pos()
        self.namehash_used = self._io.read_u4le()
        self._debug['namehash_used']['end'] = self._io.pos()
        self._debug['num_namehash']['start'] = self._io.pos()
        self.num_namehash = self._io.read_u4le()
        self._debug['num_namehash']['end'] = self._io.pos()
        self._debug['ofs_string']['start'] = self._io.pos()
        self.ofs_string = self._io.read_u4le()
        self._debug['ofs_string']['end'] = self._io.pos()
        self._debug['string_used']['start'] = self._io.pos()
        self.string_used = self._io.read_u4le()
        self._debug['string_used']['end'] = self._io.pos()
        self._debug['num_string']['start'] = self._io.pos()
        self.num_string = self._io.read_u4le()
        self._debug['num_string']['end'] = self._io.pos()
        self._debug['ofs_locrec_table']['start'] = self._io.pos()
        self.ofs_locrec_table = self._io.read_u4le()
        self._debug['ofs_locrec_table']['end'] = self._io.pos()
        self._debug['locrectab_used']['start'] = self._io.pos()
        self.locrectab_used = self._io.read_u4le()
        self._debug['locrectab_used']['end'] = self._io.pos()
        self._debug['num_locrectab']['start'] = self._io.pos()
        self.num_locrectab = self._io.read_u4le()
        self._debug['num_locrectab']['end'] = self._io.pos()
        self._debug['ofs_sumhash']['start'] = self._io.pos()
        self.ofs_sumhash = self._io.read_u4le()
        self._debug['ofs_sumhash']['end'] = self._io.pos()
        self._debug['sumhash_used']['start'] = self._io.pos()
        self.sumhash_used = self._io.read_u4le()
        self._debug['sumhash_used']['end'] = self._io.pos()
        self._debug['num_sumhash']['start'] = self._io.pos()
        self.num_sumhash = self._io.read_u4le()
        self._debug['num_sumhash']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _ = self.locrec_table
        if hasattr(self, '_m_locrec_table'):
            pass

        _ = self.md5_table
        if hasattr(self, '_m_md5_table'):
            pass
            self._m_md5_table._fetch_instances()

        _ = self.name_hash_table
        if hasattr(self, '_m_name_hash_table'):
            pass
            self._m_name_hash_table._fetch_instances()

        _ = self.string_table
        if hasattr(self, '_m_string_table'):
            pass
            self._m_string_table._fetch_instances()


    class LocRec(KaitaiStruct):
        SEQ_FIELDS = ["ofs_locrec", "len_locrec"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GlibcLocaleArchive.LocRec, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_locrec']['start'] = self._io.pos()
            self.ofs_locrec = self._io.read_u4le()
            self._debug['ofs_locrec']['end'] = self._io.pos()
            self._debug['len_locrec']['start'] = self._io.pos()
            self.len_locrec = self._io.read_u4le()
            self._debug['len_locrec']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.loc_rec
            if hasattr(self, '_m_loc_rec'):
                pass

            _ = self.loc_rec_type
            if hasattr(self, '_m_loc_rec_type'):
                pass


        @property
        def loc_rec(self):
            if hasattr(self, '_m_loc_rec'):
                return self._m_loc_rec

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_locrec)
            self._debug['_m_loc_rec']['start'] = io.pos()
            self._m_loc_rec = io.read_bytes(self.len_locrec)
            self._debug['_m_loc_rec']['end'] = io.pos()
            io.seek(_pos)
            return getattr(self, '_m_loc_rec', None)

        @property
        def loc_rec_type(self):
            if hasattr(self, '_m_loc_rec_type'):
                return self._m_loc_rec_type

            io = self._root._io
            _pos = io.pos()
            io.seek(self.ofs_locrec)
            self._debug['_m_loc_rec_type']['start'] = io.pos()
            self._m_loc_rec_type = KaitaiStream.resolve_enum(GlibcLocaleArchive.Category, io.read_u4le())
            self._debug['_m_loc_rec_type']['end'] = io.pos()
            if not  ((self._m_loc_rec_type == GlibcLocaleArchive.Category.ctype) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.ctype_variant) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.numeric) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.time) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.collate) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.collate_variant) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.monetary) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.messages) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.all) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.paper) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.name) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.address) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.telephone) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.measurement) or (self._m_loc_rec_type == GlibcLocaleArchive.Category.identification)) :
                raise kaitaistruct.ValidationNotAnyOfError(self._m_loc_rec_type, self._io, u"/types/loc_rec/instances/loc_rec_type")
            io.seek(_pos)
            return getattr(self, '_m_loc_rec_type', None)


    class LocRecEntry(KaitaiStruct):
        SEQ_FIELDS = ["references", "loc_recs"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GlibcLocaleArchive.LocRecEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['references']['start'] = self._io.pos()
            self.references = self._io.read_u4le()
            self._debug['references']['end'] = self._io.pos()
            self._debug['loc_recs']['start'] = self._io.pos()
            self._debug['loc_recs']['arr'] = []
            self.loc_recs = []
            for i in range(self._root.lc_last):
                self._debug['loc_recs']['arr'].append({'start': self._io.pos()})
                self.loc_recs.append(GlibcLocaleArchive.LocRec(self._io, self, self._root))
                self._debug['loc_recs']['arr'][i]['end'] = self._io.pos()

            self._debug['loc_recs']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.loc_recs)):
                pass
                self.loc_recs[i]._fetch_instances()



    class Md5Table(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, num_md5, _io, _parent=None, _root=None):
            super(GlibcLocaleArchive.Md5Table, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_md5 = num_md5
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_md5):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(GlibcLocaleArchive.SumHashEntry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class NameHashEntry(KaitaiStruct):
        SEQ_FIELDS = ["hash_value", "ofs_name", "ofs_locrec"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GlibcLocaleArchive.NameHashEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['hash_value']['start'] = self._io.pos()
            self.hash_value = self._io.read_u4le()
            self._debug['hash_value']['end'] = self._io.pos()
            self._debug['ofs_name']['start'] = self._io.pos()
            self.ofs_name = self._io.read_u4le()
            self._debug['ofs_name']['end'] = self._io.pos()
            self._debug['ofs_locrec']['start'] = self._io.pos()
            self.ofs_locrec = self._io.read_u4le()
            self._debug['ofs_locrec']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.locrec
            if hasattr(self, '_m_locrec'):
                pass
                self._m_locrec._fetch_instances()

            _ = self.name
            if hasattr(self, '_m_name'):
                pass


        @property
        def locrec(self):
            if hasattr(self, '_m_locrec'):
                return self._m_locrec

            if self.ofs_locrec != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_locrec)
                self._debug['_m_locrec']['start'] = io.pos()
                self._m_locrec = GlibcLocaleArchive.LocRecEntry(io, self, self._root)
                self._debug['_m_locrec']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_locrec', None)

        @property
        def name(self):
            if hasattr(self, '_m_name'):
                return self._m_name

            if self.ofs_name != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.ofs_name)
                self._debug['_m_name']['start'] = io.pos()
                self._m_name = (io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
                self._debug['_m_name']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_name', None)


    class NameHashTable(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, num_namehash, _io, _parent=None, _root=None):
            super(GlibcLocaleArchive.NameHashTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_namehash = num_namehash
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_namehash):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(GlibcLocaleArchive.NameHashEntry(self._io, self, self._root))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class StringTable(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, num_string, _io, _parent=None, _root=None):
            super(GlibcLocaleArchive.StringTable, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.num_string = num_string
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_string):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append((self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8"))
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass



    class SumHashEntry(KaitaiStruct):
        SEQ_FIELDS = ["md5", "ofs_entry"]
        def __init__(self, _io, _parent=None, _root=None):
            super(GlibcLocaleArchive.SumHashEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['md5']['start'] = self._io.pos()
            self.md5 = self._io.read_bytes(16)
            self._debug['md5']['end'] = self._io.pos()
            self._debug['ofs_entry']['start'] = self._io.pos()
            self.ofs_entry = self._io.read_u4le()
            self._debug['ofs_entry']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def lc_last(self):
        if hasattr(self, '_m_lc_last'):
            return self._m_lc_last

        self._m_lc_last = 13
        return getattr(self, '_m_lc_last', None)

    @property
    def len_locrec_table(self):
        if hasattr(self, '_m_len_locrec_table'):
            return self._m_len_locrec_table

        self._m_len_locrec_table = self.ofs_sumhash - self.ofs_locrec_table
        return getattr(self, '_m_len_locrec_table', None)

    @property
    def len_name_hash_table(self):
        if hasattr(self, '_m_len_name_hash_table'):
            return self._m_len_name_hash_table

        self._m_len_name_hash_table = self.ofs_string - self.ofs_namehash
        return getattr(self, '_m_len_name_hash_table', None)

    @property
    def len_string_table(self):
        if hasattr(self, '_m_len_string_table'):
            return self._m_len_string_table

        self._m_len_string_table = self.ofs_locrec_table - self.ofs_string
        return getattr(self, '_m_len_string_table', None)

    @property
    def locrec_table(self):
        if hasattr(self, '_m_locrec_table'):
            return self._m_locrec_table

        _pos = self._io.pos()
        self._io.seek(self.ofs_locrec_table)
        self._debug['_m_locrec_table']['start'] = self._io.pos()
        self._m_locrec_table = self._io.read_bytes(self.len_locrec_table)
        self._debug['_m_locrec_table']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_locrec_table', None)

    @property
    def md5_table(self):
        if hasattr(self, '_m_md5_table'):
            return self._m_md5_table

        _pos = self._io.pos()
        self._io.seek(self.ofs_sumhash)
        self._debug['_m_md5_table']['start'] = self._io.pos()
        self._m_md5_table = GlibcLocaleArchive.Md5Table(self.num_sumhash, self._io, self, self._root)
        self._debug['_m_md5_table']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_md5_table', None)

    @property
    def name_hash_table(self):
        if hasattr(self, '_m_name_hash_table'):
            return self._m_name_hash_table

        _pos = self._io.pos()
        self._io.seek(self.ofs_namehash)
        self._debug['_m_name_hash_table']['start'] = self._io.pos()
        self._raw__m_name_hash_table = self._io.read_bytes(self.len_name_hash_table)
        _io__raw__m_name_hash_table = KaitaiStream(BytesIO(self._raw__m_name_hash_table))
        self._m_name_hash_table = GlibcLocaleArchive.NameHashTable(self.num_namehash, _io__raw__m_name_hash_table, self, self._root)
        self._debug['_m_name_hash_table']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_name_hash_table', None)

    @property
    def string_table(self):
        if hasattr(self, '_m_string_table'):
            return self._m_string_table

        _pos = self._io.pos()
        self._io.seek(self.ofs_string)
        self._debug['_m_string_table']['start'] = self._io.pos()
        self._raw__m_string_table = self._io.read_bytes(self.len_string_table)
        _io__raw__m_string_table = KaitaiStream(BytesIO(self._raw__m_string_table))
        self._m_string_table = GlibcLocaleArchive.StringTable(self.namehash_used, _io__raw__m_string_table, self, self._root)
        self._debug['_m_string_table']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_string_table', None)


