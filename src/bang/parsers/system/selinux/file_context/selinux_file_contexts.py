# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class SelinuxFileContexts(KaitaiStruct):
    """SELinux file_contexts.bin file is a file containing compiled regular
    expressions that are used by the SELinux labeling system.
    
    Note: the version has changed a few times but the description of the file
    format in the source code was not changed. For example, regex-arch was
    introduced in version 5, but is not documented. Similarly, the regex
    study data was removed/reworked, but also not documented.
    
    Test files:
      - version 4: inside omni-7.1.2-20171120-flounder-WEEKLY.zip from OmniROM
      - version 5: /etc/selinux/targeted/contexts/files/file_contexts.bin on Fedora 33
    
    .. seealso::
       Source - https://github.com/SELinuxProject/selinux/blob/b550c0e/libselinux/utils/sefcontext_compile.c#L68
    """
    SEQ_FIELDS = ["magic", "version", "len_pcre_version", "pcre_version", "len_regex_arch", "regex_arch", "num_stems", "stems", "num_regexes", "regexes"]
    def __init__(self, _io, _parent=None, _root=None):
        super(SelinuxFileContexts, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x8A\xFF\x7C\xF9":
            raise kaitaistruct.ValidationNotEqualError(b"\x8A\xFF\x7C\xF9", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        if not  ((self.version == 4) or (self.version == 5)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/seq/1")
        self._debug['len_pcre_version']['start'] = self._io.pos()
        self.len_pcre_version = self._io.read_u4le()
        self._debug['len_pcre_version']['end'] = self._io.pos()
        self._debug['pcre_version']['start'] = self._io.pos()
        self.pcre_version = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_pcre_version), 0, False)).decode(u"UTF-8")
        self._debug['pcre_version']['end'] = self._io.pos()
        if self.version > 4:
            pass
            self._debug['len_regex_arch']['start'] = self._io.pos()
            self.len_regex_arch = self._io.read_u4le()
            self._debug['len_regex_arch']['end'] = self._io.pos()

        if self.version > 4:
            pass
            self._debug['regex_arch']['start'] = self._io.pos()
            self.regex_arch = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_regex_arch), 0, False)).decode(u"UTF-8")
            self._debug['regex_arch']['end'] = self._io.pos()

        self._debug['num_stems']['start'] = self._io.pos()
        self.num_stems = self._io.read_u4le()
        self._debug['num_stems']['end'] = self._io.pos()
        self._debug['stems']['start'] = self._io.pos()
        self._debug['stems']['arr'] = []
        self.stems = []
        for i in range(self.num_stems):
            self._debug['stems']['arr'].append({'start': self._io.pos()})
            self.stems.append(SelinuxFileContexts.Stem(self._io, self, self._root))
            self._debug['stems']['arr'][i]['end'] = self._io.pos()

        self._debug['stems']['end'] = self._io.pos()
        self._debug['num_regexes']['start'] = self._io.pos()
        self.num_regexes = self._io.read_u4le()
        self._debug['num_regexes']['end'] = self._io.pos()
        self._debug['regexes']['start'] = self._io.pos()
        self._debug['regexes']['arr'] = []
        self.regexes = []
        for i in range(self.num_regexes):
            self._debug['regexes']['arr'].append({'start': self._io.pos()})
            self.regexes.append(SelinuxFileContexts.Regex(self._io, self, self._root))
            self._debug['regexes']['arr'][i]['end'] = self._io.pos()

        self._debug['regexes']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        if self.version > 4:
            pass

        if self.version > 4:
            pass

        for i in range(len(self.stems)):
            pass
            self.stems[i]._fetch_instances()

        for i in range(len(self.regexes)):
            pass
            self.regexes[i]._fetch_instances()


    class Regex(KaitaiStruct):
        SEQ_FIELDS = ["len_context", "raw_context", "len_regex_str", "regex_str", "mode_bits", "stem_id", "spec_meta_chars", "spec_prefix_len", "len_pcre_regex_data", "pcre_regex_data", "len_pcre_regex_study_data", "pcre_regex_study_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SelinuxFileContexts.Regex, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_context']['start'] = self._io.pos()
            self.len_context = self._io.read_u4le()
            self._debug['len_context']['end'] = self._io.pos()
            self._debug['raw_context']['start'] = self._io.pos()
            self.raw_context = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_context), 0, False)).decode(u"UTF-8")
            self._debug['raw_context']['end'] = self._io.pos()
            self._debug['len_regex_str']['start'] = self._io.pos()
            self.len_regex_str = self._io.read_u4le()
            self._debug['len_regex_str']['end'] = self._io.pos()
            self._debug['regex_str']['start'] = self._io.pos()
            self.regex_str = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_regex_str), 0, False)).decode(u"UTF-8")
            self._debug['regex_str']['end'] = self._io.pos()
            self._debug['mode_bits']['start'] = self._io.pos()
            self.mode_bits = self._io.read_u4le()
            self._debug['mode_bits']['end'] = self._io.pos()
            self._debug['stem_id']['start'] = self._io.pos()
            self.stem_id = self._io.read_s4le()
            self._debug['stem_id']['end'] = self._io.pos()
            self._debug['spec_meta_chars']['start'] = self._io.pos()
            self.spec_meta_chars = self._io.read_u4le()
            self._debug['spec_meta_chars']['end'] = self._io.pos()
            self._debug['spec_prefix_len']['start'] = self._io.pos()
            self.spec_prefix_len = self._io.read_u4le()
            self._debug['spec_prefix_len']['end'] = self._io.pos()
            self._debug['len_pcre_regex_data']['start'] = self._io.pos()
            self.len_pcre_regex_data = self._io.read_u4le()
            self._debug['len_pcre_regex_data']['end'] = self._io.pos()
            self._debug['pcre_regex_data']['start'] = self._io.pos()
            self.pcre_regex_data = self._io.read_bytes(self.len_pcre_regex_data)
            self._debug['pcre_regex_data']['end'] = self._io.pos()
            if self._root.version < 5:
                pass
                self._debug['len_pcre_regex_study_data']['start'] = self._io.pos()
                self.len_pcre_regex_study_data = self._io.read_u4le()
                self._debug['len_pcre_regex_study_data']['end'] = self._io.pos()

            if self._root.version < 5:
                pass
                self._debug['pcre_regex_study_data']['start'] = self._io.pos()
                self.pcre_regex_study_data = self._io.read_bytes(self.len_pcre_regex_study_data)
                self._debug['pcre_regex_study_data']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self._root.version < 5:
                pass

            if self._root.version < 5:
                pass



    class Stem(KaitaiStruct):
        SEQ_FIELDS = ["len_stem", "stem"]
        def __init__(self, _io, _parent=None, _root=None):
            super(SelinuxFileContexts.Stem, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_stem']['start'] = self._io.pos()
            self.len_stem = self._io.read_u4le()
            self._debug['len_stem']['end'] = self._io.pos()
            self._debug['stem']['start'] = self._io.pos()
            self.stem = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_stem + 1), 0, False)).decode(u"UTF-8")
            self._debug['stem']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



