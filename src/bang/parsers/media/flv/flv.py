# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Flv(KaitaiStruct):
    """
    .. seealso::
       Source - https://wwwimages2.adobe.com/content/dam/acom/en/devnet/flv/video_file_format_spec_v10_1.pdf
    """

    class DataType(IntEnum):
        audio = 8
        video = 9
        script = 18
    SEQ_FIELDS = ["preheader", "rest_of_header", "previous_tag_size0", "tags"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Flv, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['preheader']['start'] = self._io.pos()
        self.preheader = Flv.Preheader(self._io, self, self._root)
        self._debug['preheader']['end'] = self._io.pos()
        self._debug['rest_of_header']['start'] = self._io.pos()
        self.rest_of_header = self._io.read_bytes(self.preheader.len_header - 9)
        self._debug['rest_of_header']['end'] = self._io.pos()
        self._debug['previous_tag_size0']['start'] = self._io.pos()
        self.previous_tag_size0 = self._io.read_u4be()
        self._debug['previous_tag_size0']['end'] = self._io.pos()
        if not self.previous_tag_size0 == 0:
            raise kaitaistruct.ValidationNotEqualError(0, self.previous_tag_size0, self._io, u"/seq/2")
        self._debug['tags']['start'] = self._io.pos()
        self._debug['tags']['arr'] = []
        self.tags = []
        i = 0
        while not self._io.is_eof():
            self._debug['tags']['arr'].append({'start': self._io.pos()})
            self.tags.append(Flv.TagAndSize(self._io, self, self._root))
            self._debug['tags']['arr'][len(self.tags) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['tags']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.preheader._fetch_instances()
        for i in range(len(self.tags)):
            pass
            self.tags[i]._fetch_instances()


    class Flags(KaitaiStruct):
        SEQ_FIELDS = ["reserved", "audio", "reserved2", "video"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Flv.Flags, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bits_int_be(5)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['audio']['start'] = self._io.pos()
            self.audio = self._io.read_bits_int_be(1) != 0
            self._debug['audio']['end'] = self._io.pos()
            self._debug['reserved2']['start'] = self._io.pos()
            self.reserved2 = self._io.read_bits_int_be(1) != 0
            self._debug['reserved2']['end'] = self._io.pos()
            self._debug['video']['start'] = self._io.pos()
            self.video = self._io.read_bits_int_be(1) != 0
            self._debug['video']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Preheader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "flags", "len_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Flv.Preheader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(3)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x46\x4C\x56":
                raise kaitaistruct.ValidationNotEqualError(b"\x46\x4C\x56", self.magic, self._io, u"/types/preheader/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u1()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.version, self._io, u"/types/preheader/seq/1")
            self._debug['flags']['start'] = self._io.pos()
            self.flags = Flv.Flags(self._io, self, self._root)
            self._debug['flags']['end'] = self._io.pos()
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4be()
            self._debug['len_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.flags._fetch_instances()


    class Tag(KaitaiStruct):
        SEQ_FIELDS = ["reserved", "filter", "type", "len_data", "timestamp", "timestamp_extended", "stream_id", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Flv.Tag, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bits_int_be(2)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['filter']['start'] = self._io.pos()
            self.filter = self._io.read_bits_int_be(1) != 0
            self._debug['filter']['end'] = self._io.pos()
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Flv.DataType, self._io.read_bits_int_be(5))
            self._debug['type']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_bits_int_be(24)
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['timestamp']['start'] = self._io.pos()
            self.timestamp = self._io.read_bits_int_be(24)
            self._debug['timestamp']['end'] = self._io.pos()
            self._debug['timestamp_extended']['start'] = self._io.pos()
            self.timestamp_extended = self._io.read_u1()
            self._debug['timestamp_extended']['end'] = self._io.pos()
            self._debug['stream_id']['start'] = self._io.pos()
            self.stream_id = self._io.read_bits_int_be(24)
            self._debug['stream_id']['end'] = self._io.pos()
            if not self.stream_id == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.stream_id, self._io, u"/types/tag/seq/6")
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class TagAndSize(KaitaiStruct):
        SEQ_FIELDS = ["tag", "previous_tag_size"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Flv.TagAndSize, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tag']['start'] = self._io.pos()
            self.tag = Flv.Tag(self._io, self, self._root)
            self._debug['tag']['end'] = self._io.pos()
            self._debug['previous_tag_size']['start'] = self._io.pos()
            self.previous_tag_size = self._io.read_u4be()
            self._debug['previous_tag_size']['end'] = self._io.pos()
            if not self.previous_tag_size == self.tag.len_data + 11:
                raise kaitaistruct.ValidationNotEqualError(self.tag.len_data + 11, self.previous_tag_size, self._io, u"/types/tag_and_size/seq/1")


        def _fetch_instances(self):
            pass
            self.tag._fetch_instances()



