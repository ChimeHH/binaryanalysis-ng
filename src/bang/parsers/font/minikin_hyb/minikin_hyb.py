# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MinikinHyb(KaitaiStruct):
    """Text layout format as used on Android
    
    https://lwn.net/Articles/662569/
    
    .. seealso::
       Source - https://android.googlesource.com/platform/frameworks/minikin/+/6c8722e/doc/hyb_file_format.md
    """
    SEQ_FIELDS = ["magic", "version", "ofs_alphabet", "ofs_trie", "ofs_pattern", "file_size"]
    def __init__(self, _io, _parent=None, _root=None):
        super(MinikinHyb, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x68\x79\xAD\x62":
            raise kaitaistruct.ValidationNotEqualError(b"\x68\x79\xAD\x62", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        if not self.version == 0:
            raise kaitaistruct.ValidationNotEqualError(0, self.version, self._io, u"/seq/1")
        self._debug['ofs_alphabet']['start'] = self._io.pos()
        self.ofs_alphabet = self._io.read_u4le()
        self._debug['ofs_alphabet']['end'] = self._io.pos()
        self._debug['ofs_trie']['start'] = self._io.pos()
        self.ofs_trie = self._io.read_u4le()
        self._debug['ofs_trie']['end'] = self._io.pos()
        self._debug['ofs_pattern']['start'] = self._io.pos()
        self.ofs_pattern = self._io.read_u4le()
        self._debug['ofs_pattern']['end'] = self._io.pos()
        self._debug['file_size']['start'] = self._io.pos()
        self.file_size = self._io.read_u4le()
        self._debug['file_size']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _ = self.alphabet
        if hasattr(self, '_m_alphabet'):
            pass
            self._m_alphabet._fetch_instances()

        _ = self.pattern
        if hasattr(self, '_m_pattern'):
            pass
            self._m_pattern._fetch_instances()

        _ = self.trie
        if hasattr(self, '_m_trie'):
            pass
            self._m_trie._fetch_instances()


    class Alphabet(KaitaiStruct):
        SEQ_FIELDS = ["version", "alphabet_table"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MinikinHyb.Alphabet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            self._debug['alphabet_table']['start'] = self._io.pos()
            _on = self.version
            if _on == 0:
                pass
                self.alphabet_table = MinikinHyb.AlphabetDirect(self._io, self, self._root)
            elif _on == 1:
                pass
                self.alphabet_table = MinikinHyb.AlphabetGeneral(self._io, self, self._root)
            self._debug['alphabet_table']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.version
            if _on == 0:
                pass
                self.alphabet_table._fetch_instances()
            elif _on == 1:
                pass
                self.alphabet_table._fetch_instances()


    class AlphabetDirect(KaitaiStruct):
        SEQ_FIELDS = ["min_codepoint", "max_codepoint", "alphabet_data", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MinikinHyb.AlphabetDirect, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['min_codepoint']['start'] = self._io.pos()
            self.min_codepoint = self._io.read_u4le()
            self._debug['min_codepoint']['end'] = self._io.pos()
            self._debug['max_codepoint']['start'] = self._io.pos()
            self.max_codepoint = self._io.read_u4le()
            self._debug['max_codepoint']['end'] = self._io.pos()
            self._debug['alphabet_data']['start'] = self._io.pos()
            self.alphabet_data = self._io.read_bytes(self.max_codepoint - self.min_codepoint)
            self._debug['alphabet_data']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self.max_codepoint - self.min_codepoint) % 4)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 8 + (self.max_codepoint - self.min_codepoint)
            return getattr(self, '_m_size', None)


    class AlphabetGeneral(KaitaiStruct):
        SEQ_FIELDS = ["num_entries", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MinikinHyb.AlphabetGeneral, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u4le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(self._io.read_u4le())
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass


        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = 4 + self.num_entries * 4
            return getattr(self, '_m_size', None)


    class Pattern(KaitaiStruct):
        SEQ_FIELDS = ["version", "num_entries", "ofs_pattern", "len_pattern", "entries", "pattern_buf"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MinikinHyb.Pattern, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.version, self._io, u"/types/pattern/seq/0")
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u4le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['ofs_pattern']['start'] = self._io.pos()
            self.ofs_pattern = self._io.read_u4le()
            self._debug['ofs_pattern']['end'] = self._io.pos()
            self._debug['len_pattern']['start'] = self._io.pos()
            self.len_pattern = self._io.read_u4le()
            self._debug['len_pattern']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(self._io.read_u4le())
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()
            self._debug['pattern_buf']['start'] = self._io.pos()
            self.pattern_buf = self._io.read_bytes(self.len_pattern)
            self._debug['pattern_buf']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass


        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = (self.len_pattern + self.num_entries * 4) + 4 * 4
            return getattr(self, '_m_size', None)


    class Trie(KaitaiStruct):
        SEQ_FIELDS = ["version", "char_mask", "link_shift", "link_mask", "pattern_shift", "num_entries", "entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MinikinHyb.Trie, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4le()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.version, self._io, u"/types/trie/seq/0")
            self._debug['char_mask']['start'] = self._io.pos()
            self.char_mask = self._io.read_u4le()
            self._debug['char_mask']['end'] = self._io.pos()
            self._debug['link_shift']['start'] = self._io.pos()
            self.link_shift = self._io.read_u4le()
            self._debug['link_shift']['end'] = self._io.pos()
            self._debug['link_mask']['start'] = self._io.pos()
            self.link_mask = self._io.read_u4le()
            self._debug['link_mask']['end'] = self._io.pos()
            self._debug['pattern_shift']['start'] = self._io.pos()
            self.pattern_shift = self._io.read_u4le()
            self._debug['pattern_shift']['end'] = self._io.pos()
            self._debug['num_entries']['start'] = self._io.pos()
            self.num_entries = self._io.read_u4le()
            self._debug['num_entries']['end'] = self._io.pos()
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            for i in range(self.num_entries):
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(self._io.read_u4le())
                self._debug['entries']['arr'][i]['end'] = self._io.pos()

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass


        @property
        def size(self):
            if hasattr(self, '_m_size'):
                return self._m_size

            self._m_size = self.num_entries * 4 + 6 * 4
            return getattr(self, '_m_size', None)


    @property
    def alphabet(self):
        if hasattr(self, '_m_alphabet'):
            return self._m_alphabet

        _pos = self._io.pos()
        self._io.seek(self.ofs_alphabet)
        self._debug['_m_alphabet']['start'] = self._io.pos()
        self._m_alphabet = MinikinHyb.Alphabet(self._io, self, self._root)
        self._debug['_m_alphabet']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_alphabet', None)

    @property
    def pattern(self):
        if hasattr(self, '_m_pattern'):
            return self._m_pattern

        _pos = self._io.pos()
        self._io.seek(self.ofs_pattern)
        self._debug['_m_pattern']['start'] = self._io.pos()
        self._m_pattern = MinikinHyb.Pattern(self._io, self, self._root)
        self._debug['_m_pattern']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_pattern', None)

    @property
    def trie(self):
        if hasattr(self, '_m_trie'):
            return self._m_trie

        _pos = self._io.pos()
        self._io.seek(self.ofs_trie)
        self._debug['_m_trie']['start'] = self._io.pos()
        self._m_trie = MinikinHyb.Trie(self._io, self, self._root)
        self._debug['_m_trie']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_trie', None)


