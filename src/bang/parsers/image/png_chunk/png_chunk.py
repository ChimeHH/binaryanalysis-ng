# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections
import zlib


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class PngChunk(KaitaiStruct):
    """Individual PNG chunks to enable partial carving of data.
    """

    class BlendOpValues(IntEnum):
        source = 0
        over = 1

    class ColorType(IntEnum):
        greyscale = 0
        truecolor = 2
        indexed = 3
        greyscale_alpha = 4
        truecolor_alpha = 6

    class CompressionMethods(IntEnum):
        zlib = 0

    class DisposeOpValues(IntEnum):
        none = 0
        background = 1
        previous = 2

    class PhysUnit(IntEnum):
        unknown = 0
        meter = 1
    SEQ_FIELDS = ["chunk"]
    def __init__(self, _io, _parent=None, _root=None):
        super(PngChunk, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['chunk']['start'] = self._io.pos()
        self.chunk = PngChunk.Chunk(self._io, self, self._root)
        self._debug['chunk']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.chunk._fetch_instances()

    class AdobeFireworksChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://stackoverflow.com/questions/4242402/the-fireworks-png-format-any-insight-any-libs/51683285#51683285
        """
        SEQ_FIELDS = ["preview_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.AdobeFireworksChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['preview_data']['start'] = self._io.pos()
            self._raw_preview_data = self._io.read_bytes_full()
            self.preview_data = zlib.decompress(self._raw_preview_data)
            self._debug['preview_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class AnimationControlChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.mozilla.org/APNG_Specification#.60acTL.60:_The_Animation_Control_Chunk
        """
        SEQ_FIELDS = ["num_frames", "num_plays"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.AnimationControlChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_frames']['start'] = self._io.pos()
            self.num_frames = self._io.read_u4be()
            self._debug['num_frames']['end'] = self._io.pos()
            self._debug['num_plays']['start'] = self._io.pos()
            self.num_plays = self._io.read_u4be()
            self._debug['num_plays']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class ChrmChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11cHRM
        """
        SEQ_FIELDS = ["white_point", "red", "green", "blue"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.ChrmChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['white_point']['start'] = self._io.pos()
            self.white_point = PngChunk.Point(self._io, self, self._root)
            self._debug['white_point']['end'] = self._io.pos()
            self._debug['red']['start'] = self._io.pos()
            self.red = PngChunk.Point(self._io, self, self._root)
            self._debug['red']['end'] = self._io.pos()
            self._debug['green']['start'] = self._io.pos()
            self.green = PngChunk.Point(self._io, self, self._root)
            self._debug['green']['end'] = self._io.pos()
            self._debug['blue']['start'] = self._io.pos()
            self.blue = PngChunk.Point(self._io, self, self._root)
            self._debug['blue']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.white_point._fetch_instances()
            self.red._fetch_instances()
            self.green._fetch_instances()
            self.blue._fetch_instances()


    class Chunk(KaitaiStruct):
        SEQ_FIELDS = ["len", "type", "body", "crc"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.Chunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len']['start'] = self._io.pos()
            self.len = self._io.read_u4be()
            self._debug['len']['end'] = self._io.pos()
            if not self.len <= 10485760:
                raise kaitaistruct.ValidationGreaterThanError(10485760, self.len, self._io, u"/types/chunk/seq/0")
            self._debug['type']['start'] = self._io.pos()
            self.type = (self._io.read_bytes(4)).decode(u"UTF-8")
            self._debug['type']['end'] = self._io.pos()
            _ = self.type
            if not self.type != u"\000\000\000\000":
                raise kaitaistruct.ValidationExprError(self.type, self._io, u"/types/chunk/seq/1")
            self._debug['body']['start'] = self._io.pos()
            _on = self.type
            if _on == u"IHDR":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.IhdrChunk(_io__raw_body, self, self._root)
            elif _on == u"acTL":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.AnimationControlChunk(_io__raw_body, self, self._root)
            elif _on == u"cHRM":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.ChrmChunk(_io__raw_body, self, self._root)
            elif _on == u"fcTL":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.FrameControlChunk(_io__raw_body, self, self._root)
            elif _on == u"fdAT":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.FrameDataChunk(_io__raw_body, self, self._root)
            elif _on == u"gAMA":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.GamaChunk(_io__raw_body, self, self._root)
            elif _on == u"iTXt":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.InternationalTextChunk(_io__raw_body, self, self._root)
            elif _on == u"mkBS":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.AdobeFireworksChunk(_io__raw_body, self, self._root)
            elif _on == u"mkTS":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.AdobeFireworksChunk(_io__raw_body, self, self._root)
            elif _on == u"pHYs":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.PhysChunk(_io__raw_body, self, self._root)
            elif _on == u"prVW":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.AdobeFireworksChunk(_io__raw_body, self, self._root)
            elif _on == u"sRGB":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.SrgbChunk(_io__raw_body, self, self._root)
            elif _on == u"skRf":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.EvernoteSkrfChunk(_io__raw_body, self, self._root)
            elif _on == u"tIME":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.TimeChunk(_io__raw_body, self, self._root)
            elif _on == u"zTXt":
                pass
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = PngChunk.CompressedTextChunk(_io__raw_body, self, self._root)
            else:
                pass
                self.body = self._io.read_bytes(self.len)
            self._debug['body']['end'] = self._io.pos()
            self._debug['crc']['start'] = self._io.pos()
            self.crc = self._io.read_bytes(4)
            self._debug['crc']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.type
            if _on == u"IHDR":
                pass
                self.body._fetch_instances()
            elif _on == u"acTL":
                pass
                self.body._fetch_instances()
            elif _on == u"cHRM":
                pass
                self.body._fetch_instances()
            elif _on == u"fcTL":
                pass
                self.body._fetch_instances()
            elif _on == u"fdAT":
                pass
                self.body._fetch_instances()
            elif _on == u"gAMA":
                pass
                self.body._fetch_instances()
            elif _on == u"iTXt":
                pass
                self.body._fetch_instances()
            elif _on == u"mkBS":
                pass
                self.body._fetch_instances()
            elif _on == u"mkTS":
                pass
                self.body._fetch_instances()
            elif _on == u"pHYs":
                pass
                self.body._fetch_instances()
            elif _on == u"prVW":
                pass
                self.body._fetch_instances()
            elif _on == u"sRGB":
                pass
                self.body._fetch_instances()
            elif _on == u"skRf":
                pass
                self.body._fetch_instances()
            elif _on == u"tIME":
                pass
                self.body._fetch_instances()
            elif _on == u"zTXt":
                pass
                self.body._fetch_instances()
            else:
                pass


    class CompressedTextChunk(KaitaiStruct):
        """Compressed text chunk effectively allows to store key-value
        string pairs in PNG container, compressing "value" part (which
        can be quite lengthy) with zlib compression.
        
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11zTXt
        """
        SEQ_FIELDS = ["keyword", "compression_method", "text_datastream"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.CompressedTextChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['keyword']['start'] = self._io.pos()
            self.keyword = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['keyword']['end'] = self._io.pos()
            self._debug['compression_method']['start'] = self._io.pos()
            self.compression_method = KaitaiStream.resolve_enum(PngChunk.CompressionMethods, self._io.read_u1())
            self._debug['compression_method']['end'] = self._io.pos()
            self._debug['text_datastream']['start'] = self._io.pos()
            self._raw_text_datastream = self._io.read_bytes_full()
            self.text_datastream = zlib.decompress(self._raw_text_datastream)
            self._debug['text_datastream']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class EvernoteSkrfChunk(KaitaiStruct):
        SEQ_FIELDS = ["uuid", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.EvernoteSkrfChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['uuid']['start'] = self._io.pos()
            self.uuid = self._io.read_bytes(16)
            self._debug['uuid']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes_full()
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class FrameControlChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.mozilla.org/APNG_Specification#.60fcTL.60:_The_Frame_Control_Chunk
        """
        SEQ_FIELDS = ["sequence_number", "width", "height", "x_offset", "y_offset", "delay_num", "delay_den", "dispose_op", "blend_op"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.FrameControlChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['sequence_number']['start'] = self._io.pos()
            self.sequence_number = self._io.read_u4be()
            self._debug['sequence_number']['end'] = self._io.pos()
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u4be()
            self._debug['width']['end'] = self._io.pos()
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u4be()
            self._debug['height']['end'] = self._io.pos()
            self._debug['x_offset']['start'] = self._io.pos()
            self.x_offset = self._io.read_u4be()
            self._debug['x_offset']['end'] = self._io.pos()
            self._debug['y_offset']['start'] = self._io.pos()
            self.y_offset = self._io.read_u4be()
            self._debug['y_offset']['end'] = self._io.pos()
            self._debug['delay_num']['start'] = self._io.pos()
            self.delay_num = self._io.read_u2be()
            self._debug['delay_num']['end'] = self._io.pos()
            self._debug['delay_den']['start'] = self._io.pos()
            self.delay_den = self._io.read_u2be()
            self._debug['delay_den']['end'] = self._io.pos()
            self._debug['dispose_op']['start'] = self._io.pos()
            self.dispose_op = KaitaiStream.resolve_enum(PngChunk.DisposeOpValues, self._io.read_u1())
            self._debug['dispose_op']['end'] = self._io.pos()
            self._debug['blend_op']['start'] = self._io.pos()
            self.blend_op = KaitaiStream.resolve_enum(PngChunk.BlendOpValues, self._io.read_u1())
            self._debug['blend_op']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def delay(self):
            """Time to display this frame, in seconds."""
            if hasattr(self, '_m_delay'):
                return self._m_delay

            self._m_delay = self.delay_num / (100.0 if self.delay_den == 0 else self.delay_den)
            return getattr(self, '_m_delay', None)


    class FrameDataChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://wiki.mozilla.org/APNG_Specification#.60fdAT.60:_The_Frame_Data_Chunk
        """
        SEQ_FIELDS = ["sequence_number", "frame_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.FrameDataChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['sequence_number']['start'] = self._io.pos()
            self.sequence_number = self._io.read_u4be()
            self._debug['sequence_number']['end'] = self._io.pos()
            self._debug['frame_data']['start'] = self._io.pos()
            self.frame_data = self._io.read_bytes_full()
            self._debug['frame_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class GamaChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11gAMA
        """
        SEQ_FIELDS = ["gamma_int"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.GamaChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['gamma_int']['start'] = self._io.pos()
            self.gamma_int = self._io.read_u4be()
            self._debug['gamma_int']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def gamma_ratio(self):
            if hasattr(self, '_m_gamma_ratio'):
                return self._m_gamma_ratio

            self._m_gamma_ratio = 100000.0 / self.gamma_int
            return getattr(self, '_m_gamma_ratio', None)


    class IhdrChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11IHDR
        """
        SEQ_FIELDS = ["width", "height", "bit_depth", "color_type", "compression_method", "filter_method", "interlace_method"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.IhdrChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u4be()
            self._debug['width']['end'] = self._io.pos()
            if not self.width >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.width, self._io, u"/types/ihdr_chunk/seq/0")
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u4be()
            self._debug['height']['end'] = self._io.pos()
            if not self.height >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.height, self._io, u"/types/ihdr_chunk/seq/1")
            self._debug['bit_depth']['start'] = self._io.pos()
            self.bit_depth = self._io.read_u1()
            self._debug['bit_depth']['end'] = self._io.pos()
            if not  ((self.bit_depth == 1) or (self.bit_depth == 2) or (self.bit_depth == 4) or (self.bit_depth == 8) or (self.bit_depth == 16)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.bit_depth, self._io, u"/types/ihdr_chunk/seq/2")
            self._debug['color_type']['start'] = self._io.pos()
            self.color_type = KaitaiStream.resolve_enum(PngChunk.ColorType, self._io.read_u1())
            self._debug['color_type']['end'] = self._io.pos()
            self._debug['compression_method']['start'] = self._io.pos()
            self.compression_method = self._io.read_u1()
            self._debug['compression_method']['end'] = self._io.pos()
            self._debug['filter_method']['start'] = self._io.pos()
            self.filter_method = self._io.read_u1()
            self._debug['filter_method']['end'] = self._io.pos()
            self._debug['interlace_method']['start'] = self._io.pos()
            self.interlace_method = self._io.read_u1()
            self._debug['interlace_method']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class InternationalText(KaitaiStruct):
        SEQ_FIELDS = ["text"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.InternationalText, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['text']['start'] = self._io.pos()
            self.text = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._debug['text']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class InternationalTextChunk(KaitaiStruct):
        """International text chunk effectively allows to store key-value string pairs in
        PNG container. Both "key" (keyword) and "value" (text) parts are
        given in pre-defined subset of iso8859-1 without control
        characters.
        
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11iTXt
        """
        SEQ_FIELDS = ["keyword", "compression_flag", "compression_method", "language_tag", "translated_keyword", "text"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.InternationalTextChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['keyword']['start'] = self._io.pos()
            self.keyword = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['keyword']['end'] = self._io.pos()
            self._debug['compression_flag']['start'] = self._io.pos()
            self.compression_flag = self._io.read_u1()
            self._debug['compression_flag']['end'] = self._io.pos()
            if not  ((self.compression_flag == 0) or (self.compression_flag == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.compression_flag, self._io, u"/types/international_text_chunk/seq/1")
            self._debug['compression_method']['start'] = self._io.pos()
            self.compression_method = KaitaiStream.resolve_enum(PngChunk.CompressionMethods, self._io.read_u1())
            self._debug['compression_method']['end'] = self._io.pos()
            self._debug['language_tag']['start'] = self._io.pos()
            self.language_tag = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['language_tag']['end'] = self._io.pos()
            self._debug['translated_keyword']['start'] = self._io.pos()
            self.translated_keyword = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['translated_keyword']['end'] = self._io.pos()
            self._debug['text']['start'] = self._io.pos()
            _on = self.compression_flag
            if _on == 0:
                pass
                self._raw_text = self._io.read_bytes_full()
                _io__raw_text = KaitaiStream(BytesIO(self._raw_text))
                self.text = PngChunk.InternationalText(_io__raw_text, self, self._root)
            elif _on == 1:
                pass
                self._raw_text = self._io.read_bytes_full()
                _io__raw_text = KaitaiStream(BytesIO(self._raw_text))
                self.text = PngChunk.InternationalTextCompressed(_io__raw_text, self, self._root)
            else:
                pass
                self.text = self._io.read_bytes_full()
            self._debug['text']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.compression_flag
            if _on == 0:
                pass
                self.text._fetch_instances()
            elif _on == 1:
                pass
                self.text._fetch_instances()
            else:
                pass


    class InternationalTextCompressed(KaitaiStruct):
        SEQ_FIELDS = ["text"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.InternationalTextCompressed, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['text']['start'] = self._io.pos()
            self._raw_text = self._io.read_bytes_full()
            self.text = zlib.decompress(self._raw_text)
            self._debug['text']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PhysChunk(KaitaiStruct):
        """"Physical size" chunk stores data that allows to translate
        logical pixels into physical units (meters, etc) and vice-versa.
        
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11pHYs
        """
        SEQ_FIELDS = ["pixels_per_unit_x", "pixels_per_unit_y", "unit"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.PhysChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['pixels_per_unit_x']['start'] = self._io.pos()
            self.pixels_per_unit_x = self._io.read_u4be()
            self._debug['pixels_per_unit_x']['end'] = self._io.pos()
            self._debug['pixels_per_unit_y']['start'] = self._io.pos()
            self.pixels_per_unit_y = self._io.read_u4be()
            self._debug['pixels_per_unit_y']['end'] = self._io.pos()
            self._debug['unit']['start'] = self._io.pos()
            self.unit = KaitaiStream.resolve_enum(PngChunk.PhysUnit, self._io.read_u1())
            self._debug['unit']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PlteChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11PLTE
        """
        SEQ_FIELDS = ["entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.PlteChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                self.entries.append(PngChunk.Rgb(self._io, self, self._root))
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class Point(KaitaiStruct):
        SEQ_FIELDS = ["x_int", "y_int"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.Point, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['x_int']['start'] = self._io.pos()
            self.x_int = self._io.read_u4be()
            self._debug['x_int']['end'] = self._io.pos()
            self._debug['y_int']['start'] = self._io.pos()
            self.y_int = self._io.read_u4be()
            self._debug['y_int']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def x(self):
            if hasattr(self, '_m_x'):
                return self._m_x

            self._m_x = self.x_int / 100000.0
            return getattr(self, '_m_x', None)

        @property
        def y(self):
            if hasattr(self, '_m_y'):
                return self._m_y

            self._m_y = self.y_int / 100000.0
            return getattr(self, '_m_y', None)


    class Rgb(KaitaiStruct):
        SEQ_FIELDS = ["r", "g", "b"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.Rgb, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['r']['start'] = self._io.pos()
            self.r = self._io.read_u1()
            self._debug['r']['end'] = self._io.pos()
            self._debug['g']['start'] = self._io.pos()
            self.g = self._io.read_u1()
            self._debug['g']['end'] = self._io.pos()
            self._debug['b']['start'] = self._io.pos()
            self.b = self._io.read_u1()
            self._debug['b']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class SrgbChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11sRGB
        """

        class Intent(IntEnum):
            perceptual = 0
            relative_colorimetric = 1
            saturation = 2
            absolute_colorimetric = 3
        SEQ_FIELDS = ["render_intent"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.SrgbChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['render_intent']['start'] = self._io.pos()
            self.render_intent = KaitaiStream.resolve_enum(PngChunk.SrgbChunk.Intent, self._io.read_u1())
            self._debug['render_intent']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class TextChunk(KaitaiStruct):
        """Text chunk effectively allows to store key-value string pairs in
        PNG container. Both "key" (keyword) and "value" (text) parts are
        given in pre-defined subset of iso8859-1 without control
        characters.
        
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11tEXt
        """
        SEQ_FIELDS = ["keyword", "text"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.TextChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['keyword']['start'] = self._io.pos()
            self.keyword = (self._io.read_bytes_term(0, False, True, True)).decode(u"ISO-8859-1")
            self._debug['keyword']['end'] = self._io.pos()
            self._debug['text']['start'] = self._io.pos()
            self.text = (self._io.read_bytes_full()).decode(u"ISO-8859-1")
            self._debug['text']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class TimeChunk(KaitaiStruct):
        """Time chunk stores time stamp of last modification of this image,
        up to 1 second precision in UTC timezone.
        
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11tIME
        """
        SEQ_FIELDS = ["year", "month", "day", "hour", "minute", "second"]
        def __init__(self, _io, _parent=None, _root=None):
            super(PngChunk.TimeChunk, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['year']['start'] = self._io.pos()
            self.year = self._io.read_u2be()
            self._debug['year']['end'] = self._io.pos()
            self._debug['month']['start'] = self._io.pos()
            self.month = self._io.read_u1()
            self._debug['month']['end'] = self._io.pos()
            self._debug['day']['start'] = self._io.pos()
            self.day = self._io.read_u1()
            self._debug['day']['end'] = self._io.pos()
            self._debug['hour']['start'] = self._io.pos()
            self.hour = self._io.read_u1()
            self._debug['hour']['end'] = self._io.pos()
            self._debug['minute']['start'] = self._io.pos()
            self.minute = self._io.read_u1()
            self._debug['minute']['end'] = self._io.pos()
            self._debug['second']['start'] = self._io.pos()
            self.second = self._io.read_u1()
            self._debug['second']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



