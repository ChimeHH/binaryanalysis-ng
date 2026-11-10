# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class QtTranslation(KaitaiStruct):
    """
    .. seealso::
       Source - https://code.qt.io/cgit/qt/qtbase.git/tree/src/corelib/kernel/qtranslator.cpp?h=dev
    """

    class TagTypes(IntEnum):
        end = 1
        source_text_16 = 2
        translation = 3
        context_16 = 4
        obsolete_1 = 5
        source_text = 6
        context = 7
        comment = 8
        obsolete_2 = 9

    class TranslatorTags(IntEnum):
        contexts = 47
        hashes = 66
        messages = 105
        numerus_rules = 136
        dependencies = 150
        language = 167
    SEQ_FIELDS = ["header", "tags"]
    def __init__(self, _io, _parent=None, _root=None):
        super(QtTranslation, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = QtTranslation.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['tags']['start'] = self._io.pos()
        self._debug['tags']['arr'] = []
        self.tags = []
        i = 0
        while not self._io.is_eof():
            self._debug['tags']['arr'].append({'start': self._io.pos()})
            self.tags.append(QtTranslation.Tag(self._io, self, self._root))
            self._debug['tags']['arr'][len(self.tags) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['tags']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.tags)):
            pass
            self.tags[i]._fetch_instances()


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["signature"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtTranslation.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(16)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x3C\xB8\x64\x18\xCA\xEF\x9C\x95\xCD\x21\x1C\xBF\x60\xA1\xBD\xDD":
                raise kaitaistruct.ValidationNotEqualError(b"\x3C\xB8\x64\x18\xCA\xEF\x9C\x95\xCD\x21\x1C\xBF\x60\xA1\xBD\xDD", self.signature, self._io, u"/types/header/seq/0")


        def _fetch_instances(self):
            pass


    class Message(KaitaiStruct):
        SEQ_FIELDS = ["tag", "payload"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtTranslation.Message, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tag']['start'] = self._io.pos()
            self.tag = KaitaiStream.resolve_enum(QtTranslation.TagTypes, self._io.read_u1())
            self._debug['tag']['end'] = self._io.pos()
            self._debug['payload']['start'] = self._io.pos()
            _on = self.tag
            if _on == QtTranslation.TagTypes.comment:
                pass
                self.payload = QtTranslation.Message.TagText(self._io, self, self._root)
            elif _on == QtTranslation.TagTypes.context:
                pass
                self.payload = QtTranslation.Message.TagText(self._io, self, self._root)
            elif _on == QtTranslation.TagTypes.source_text:
                pass
                self.payload = QtTranslation.Message.TagText(self._io, self, self._root)
            elif _on == QtTranslation.TagTypes.translation:
                pass
                self.payload = QtTranslation.Message.Translation(self._io, self, self._root)
            self._debug['payload']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.tag
            if _on == QtTranslation.TagTypes.comment:
                pass
                self.payload._fetch_instances()
            elif _on == QtTranslation.TagTypes.context:
                pass
                self.payload._fetch_instances()
            elif _on == QtTranslation.TagTypes.source_text:
                pass
                self.payload._fetch_instances()
            elif _on == QtTranslation.TagTypes.translation:
                pass
                self.payload._fetch_instances()

        class TagText(KaitaiStruct):
            SEQ_FIELDS = ["len_data", "data"]
            def __init__(self, _io, _parent=None, _root=None):
                super(QtTranslation.Message.TagText, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['len_data']['start'] = self._io.pos()
                self.len_data = self._io.read_u4be()
                self._debug['len_data']['end'] = self._io.pos()
                self._debug['data']['start'] = self._io.pos()
                self.data = (self._io.read_bytes(self.len_data)).decode(u"UTF-8")
                self._debug['data']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class Translation(KaitaiStruct):
            SEQ_FIELDS = ["len_data", "data"]
            def __init__(self, _io, _parent=None, _root=None):
                super(QtTranslation.Message.Translation, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['len_data']['start'] = self._io.pos()
                self.len_data = self._io.read_u4be()
                self._debug['len_data']['end'] = self._io.pos()
                self._debug['data']['start'] = self._io.pos()
                self.data = self._io.read_bytes(self.len_data)
                self._debug['data']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass



    class Messages(KaitaiStruct):
        SEQ_FIELDS = ["messages"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtTranslation.Messages, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['messages']['start'] = self._io.pos()
            self._debug['messages']['arr'] = []
            self.messages = []
            i = 0
            while not self._io.is_eof():
                self._debug['messages']['arr'].append({'start': self._io.pos()})
                self.messages.append(QtTranslation.Message(self._io, self, self._root))
                self._debug['messages']['arr'][len(self.messages) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['messages']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.messages)):
                pass
                self.messages[i]._fetch_instances()



    class Tag(KaitaiStruct):
        SEQ_FIELDS = ["tag", "len_data", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(QtTranslation.Tag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tag']['start'] = self._io.pos()
            self.tag = KaitaiStream.resolve_enum(QtTranslation.TranslatorTags, self._io.read_u1())
            self._debug['tag']['end'] = self._io.pos()
            if not  ((self.tag == QtTranslation.TranslatorTags.contexts) or (self.tag == QtTranslation.TranslatorTags.hashes) or (self.tag == QtTranslation.TranslatorTags.messages) or (self.tag == QtTranslation.TranslatorTags.numerus_rules) or (self.tag == QtTranslation.TranslatorTags.dependencies) or (self.tag == QtTranslation.TranslatorTags.language)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.tag, self._io, u"/types/tag/seq/0")
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4be()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            _on = self.tag
            if _on == QtTranslation.TranslatorTags.language:
                pass
                self.data = (self._io.read_bytes(self.len_data)).decode(u"UTF-8")
            elif _on == QtTranslation.TranslatorTags.messages:
                pass
                self._raw_data = self._io.read_bytes(self.len_data)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = QtTranslation.Messages(_io__raw_data, self, self._root)
            else:
                pass
                self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.tag
            if _on == QtTranslation.TranslatorTags.language:
                pass
            elif _on == QtTranslation.TranslatorTags.messages:
                pass
                self.data._fetch_instances()
            else:
                pass



