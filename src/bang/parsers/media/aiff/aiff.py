# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Aiff(KaitaiStruct):
    """
    .. seealso::
       Source - https://en.wikipedia.org/wiki/Audio_Interchange_File_Format
    
    
    .. seealso::
       Source - https://web.archive.org/web/20071219035740/http://www.cnpbagwell.com/aiff-c.txt
    
    
    .. seealso::
       Source - http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/AIFF/AIFF.html
    """

    class AiffType(IntEnum):
        aifc = 1095321155
        aiff = 1095321158

    class Compression(IntEnum):
        alaw_ccitt = 1095516503
        float32 = 1179398962
        g722 = 1194799666
        g726 = 1194799670
        g728 = 1194799672
        gsm = 1196641568
        not_compressed = 1313820229
        ulaw_ccitt = 1431060823
        alaw = 1634492791
        fl32 = 1718367026
        fl64 = 1718367796
        sowt = 1936684916
        ulaw = 1970037111

    class Fourcc(IntEnum):
        copyright = 677587232
        audio_recording = 1095062340
        annotation = 1095650895
        application = 1095782476
        author = 1096111176
        common = 1129270605
        comment = 1129270612
        fver = 1180058962
        id3 = 1229206304
        instrument = 1229869908
        marker = 1296126539
        midi = 1296647241
        name = 1312902469
        ssnd = 1397968452

    class PlayMode(IntEnum):
        no_loop = 0
        forward = 1
        forward_backward = 2
    SEQ_FIELDS = ["header", "aiff_type", "chunks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Aiff, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Aiff.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['aiff_type']['start'] = self._io.pos()
        self.aiff_type = KaitaiStream.resolve_enum(Aiff.AiffType, self._io.read_u4be())
        self._debug['aiff_type']['end'] = self._io.pos()
        if not  ((self.aiff_type == Aiff.AiffType.aifc) or (self.aiff_type == Aiff.AiffType.aiff)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.aiff_type, self._io, u"/seq/1")
        self._debug['chunks']['start'] = self._io.pos()
        self._raw_chunks = self._io.read_bytes(self.header.len_data - 4)
        _io__raw_chunks = KaitaiStream(BytesIO(self._raw_chunks))
        self.chunks = Aiff.Chunks(_io__raw_chunks, self, self._root)
        self._debug['chunks']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.chunks._fetch_instances()

    class Chunk(KaitaiStruct):
        SEQ_FIELDS = ["fourcc", "len_chunk", "data", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.Chunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['fourcc']['start'] = self._io.pos()
            self.fourcc = KaitaiStream.resolve_enum(Aiff.Fourcc, self._io.read_u4be())
            self._debug['fourcc']['end'] = self._io.pos()
            self._debug['len_chunk']['start'] = self._io.pos()
            self.len_chunk = self._io.read_u4be()
            self._debug['len_chunk']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            _on = self.fourcc
            if _on == Aiff.Fourcc.annotation:
                pass
                self._raw_data = self._io.read_bytes(self.len_chunk)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Aiff.TextChunk(_io__raw_data, self, self._root)
            elif _on == Aiff.Fourcc.author:
                pass
                self._raw_data = self._io.read_bytes(self.len_chunk)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Aiff.TextChunk(_io__raw_data, self, self._root)
            elif _on == Aiff.Fourcc.common:
                pass
                self._raw_data = self._io.read_bytes(self.len_chunk)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Aiff.CommonChunk(_io__raw_data, self, self._root)
            elif _on == Aiff.Fourcc.copyright:
                pass
                self._raw_data = self._io.read_bytes(self.len_chunk)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Aiff.TextChunk(_io__raw_data, self, self._root)
            elif _on == Aiff.Fourcc.fver:
                pass
                self._raw_data = self._io.read_bytes(self.len_chunk)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Aiff.FormatVersionChunk(_io__raw_data, self, self._root)
            elif _on == Aiff.Fourcc.instrument:
                pass
                self._raw_data = self._io.read_bytes(self.len_chunk)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Aiff.InstrumentChunk(_io__raw_data, self, self._root)
            elif _on == Aiff.Fourcc.marker:
                pass
                self._raw_data = self._io.read_bytes(self.len_chunk)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Aiff.MarkerChunk(_io__raw_data, self, self._root)
            elif _on == Aiff.Fourcc.name:
                pass
                self._raw_data = self._io.read_bytes(self.len_chunk)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Aiff.TextChunk(_io__raw_data, self, self._root)
            elif _on == Aiff.Fourcc.ssnd:
                pass
                self._raw_data = self._io.read_bytes(self.len_chunk)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Aiff.SsndChunk(_io__raw_data, self, self._root)
            else:
                pass
                self.data = self._io.read_bytes(self.len_chunk)
            self._debug['data']['end'] = self._io.pos()
            if self.len_chunk % 2 == 1:
                pass
                self._debug['padding']['start'] = self._io.pos()
                self.padding = self._io.read_bytes(1)
                self._debug['padding']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            _on = self.fourcc
            if _on == Aiff.Fourcc.annotation:
                pass
                self.data._fetch_instances()
            elif _on == Aiff.Fourcc.author:
                pass
                self.data._fetch_instances()
            elif _on == Aiff.Fourcc.common:
                pass
                self.data._fetch_instances()
            elif _on == Aiff.Fourcc.copyright:
                pass
                self.data._fetch_instances()
            elif _on == Aiff.Fourcc.fver:
                pass
                self.data._fetch_instances()
            elif _on == Aiff.Fourcc.instrument:
                pass
                self.data._fetch_instances()
            elif _on == Aiff.Fourcc.marker:
                pass
                self.data._fetch_instances()
            elif _on == Aiff.Fourcc.name:
                pass
                self.data._fetch_instances()
            elif _on == Aiff.Fourcc.ssnd:
                pass
                self.data._fetch_instances()
            else:
                pass
            if self.len_chunk % 2 == 1:
                pass



    class Chunks(KaitaiStruct):
        SEQ_FIELDS = ["chunks"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.Chunks, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['chunks']['start'] = self._io.pos()
            self._debug['chunks']['arr'] = []
            self.chunks = []
            i = 0
            while not self._io.is_eof():
                self._debug['chunks']['arr'].append({'start': self._io.pos()})
                self.chunks.append(Aiff.Chunk(self._io, self, self._root))
                self._debug['chunks']['arr'][len(self.chunks) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['chunks']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.chunks)):
                pass
                self.chunks[i]._fetch_instances()



    class CommonChunk(KaitaiStruct):
        SEQ_FIELDS = ["num_channels", "num_sample_frames", "sample_size", "sample_rate", "compression_type", "compression_name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.CommonChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_channels']['start'] = self._io.pos()
            self.num_channels = self._io.read_u2be()
            self._debug['num_channels']['end'] = self._io.pos()
            self._debug['num_sample_frames']['start'] = self._io.pos()
            self.num_sample_frames = self._io.read_u4be()
            self._debug['num_sample_frames']['end'] = self._io.pos()
            self._debug['sample_size']['start'] = self._io.pos()
            self.sample_size = self._io.read_u2be()
            self._debug['sample_size']['end'] = self._io.pos()
            self._debug['sample_rate']['start'] = self._io.pos()
            self.sample_rate = self._io.read_bytes(10)
            self._debug['sample_rate']['end'] = self._io.pos()
            if self._root.aiff_type == Aiff.AiffType.aifc:
                pass
                self._debug['compression_type']['start'] = self._io.pos()
                self.compression_type = KaitaiStream.resolve_enum(Aiff.Compression, self._io.read_u4be())
                self._debug['compression_type']['end'] = self._io.pos()

            if self._root.aiff_type == Aiff.AiffType.aifc:
                pass
                self._debug['compression_name']['start'] = self._io.pos()
                self.compression_name = Aiff.Pstring(self._io, self, self._root)
                self._debug['compression_name']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self._root.aiff_type == Aiff.AiffType.aifc:
                pass

            if self._root.aiff_type == Aiff.AiffType.aifc:
                pass
                self.compression_name._fetch_instances()



    class FormatVersionChunk(KaitaiStruct):
        SEQ_FIELDS = ["timestamp"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.FormatVersionChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['timestamp']['start'] = self._io.pos()
            self.timestamp = self._io.read_u4be()
            self._debug['timestamp']['end'] = self._io.pos()
            if not self.timestamp == 2726318400:
                raise kaitaistruct.ValidationNotEqualError(2726318400, self.timestamp, self._io, u"/types/format_version_chunk/seq/0")


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x46\x4F\x52\x4D":
                raise kaitaistruct.ValidationNotEqualError(b"\x46\x4F\x52\x4D", self.magic, self._io, u"/types/header/seq/0")
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4be()
            self._debug['len_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class InstrumentChunk(KaitaiStruct):
        SEQ_FIELDS = ["base_note", "detune", "low_note", "high_note", "low_velocity", "gain", "sustain_loop", "release_loop"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.InstrumentChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['base_note']['start'] = self._io.pos()
            self.base_note = self._io.read_u1()
            self._debug['base_note']['end'] = self._io.pos()
            self._debug['detune']['start'] = self._io.pos()
            self.detune = self._io.read_u1()
            self._debug['detune']['end'] = self._io.pos()
            self._debug['low_note']['start'] = self._io.pos()
            self.low_note = self._io.read_u1()
            self._debug['low_note']['end'] = self._io.pos()
            self._debug['high_note']['start'] = self._io.pos()
            self.high_note = self._io.read_u1()
            self._debug['high_note']['end'] = self._io.pos()
            self._debug['low_velocity']['start'] = self._io.pos()
            self.low_velocity = self._io.read_u1()
            self._debug['low_velocity']['end'] = self._io.pos()
            self._debug['gain']['start'] = self._io.pos()
            self.gain = self._io.read_u2be()
            self._debug['gain']['end'] = self._io.pos()
            self._debug['sustain_loop']['start'] = self._io.pos()
            self.sustain_loop = Aiff.Loop(self._io, self, self._root)
            self._debug['sustain_loop']['end'] = self._io.pos()
            self._debug['release_loop']['start'] = self._io.pos()
            self.release_loop = Aiff.Loop(self._io, self, self._root)
            self._debug['release_loop']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.sustain_loop._fetch_instances()
            self.release_loop._fetch_instances()


    class Loop(KaitaiStruct):
        SEQ_FIELDS = ["play_mode", "begin_loop", "end_loop"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.Loop, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['play_mode']['start'] = self._io.pos()
            self.play_mode = KaitaiStream.resolve_enum(Aiff.PlayMode, self._io.read_u2be())
            self._debug['play_mode']['end'] = self._io.pos()
            self._debug['begin_loop']['start'] = self._io.pos()
            self.begin_loop = self._io.read_u2be()
            self._debug['begin_loop']['end'] = self._io.pos()
            self._debug['end_loop']['start'] = self._io.pos()
            self.end_loop = self._io.read_u2be()
            self._debug['end_loop']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Marker(KaitaiStruct):
        SEQ_FIELDS = ["marker_id", "position", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.Marker, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['marker_id']['start'] = self._io.pos()
            self.marker_id = self._io.read_u2be()
            self._debug['marker_id']['end'] = self._io.pos()
            self._debug['position']['start'] = self._io.pos()
            self.position = self._io.read_u4be()
            self._debug['position']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = Aiff.Pstring(self._io, self, self._root)
            self._debug['name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.name._fetch_instances()


    class MarkerChunk(KaitaiStruct):
        SEQ_FIELDS = ["num_markers", "markers"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.MarkerChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_markers']['start'] = self._io.pos()
            self.num_markers = self._io.read_u2be()
            self._debug['num_markers']['end'] = self._io.pos()
            self._debug['markers']['start'] = self._io.pos()
            self._debug['markers']['arr'] = []
            self.markers = []
            for i in range(self.num_markers):
                self._debug['markers']['arr'].append({'start': self._io.pos()})
                self.markers.append(Aiff.Marker(self._io, self, self._root))
                self._debug['markers']['arr'][i]['end'] = self._io.pos()

            self._debug['markers']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.markers)):
                pass
                self.markers[i]._fetch_instances()



    class Pstring(KaitaiStruct):
        SEQ_FIELDS = ["len_string", "string", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.Pstring, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_string']['start'] = self._io.pos()
            self.len_string = self._io.read_u1()
            self._debug['len_string']['end'] = self._io.pos()
            self._debug['string']['start'] = self._io.pos()
            self.string = (self._io.read_bytes(self.len_string)).decode(u"ASCII")
            self._debug['string']['end'] = self._io.pos()
            if self.len_string % 2 == 0:
                pass
                self._debug['padding']['start'] = self._io.pos()
                self.padding = self._io.read_bytes(1)
                self._debug['padding']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.len_string % 2 == 0:
                pass



    class SsndChunk(KaitaiStruct):
        SEQ_FIELDS = ["offset", "block_size", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.SsndChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['offset']['start'] = self._io.pos()
            self.offset = self._io.read_u4be()
            self._debug['offset']['end'] = self._io.pos()
            self._debug['block_size']['start'] = self._io.pos()
            self.block_size = self._io.read_u4be()
            self._debug['block_size']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes_full()
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class TextChunk(KaitaiStruct):
        SEQ_FIELDS = ["text"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Aiff.TextChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['text']['start'] = self._io.pos()
            self.text = (self._io.read_bytes_full()).decode(u"ASCII")
            self._debug['text']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



