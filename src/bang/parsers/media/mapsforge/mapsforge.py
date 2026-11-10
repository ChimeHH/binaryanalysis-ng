# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import vlq_base128_le
from .vlq_base128_le import *
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Mapsforge(KaitaiStruct):
    """Incomplete and probably incorrect grammar for mapsforge files. The
    incorrectness is related to the use of leb128 (vlq_base128) which
    according to the mapsforge docs isn't true for signed values.
    
    .. seealso::
       Source - https://raw.githubusercontent.com/mapsforge/mapsforge/master/docs/Specification-Binary-Map-File.md
    """
    SEQ_FIELDS = ["preheader", "header", "maps_data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Mapsforge, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['preheader']['start'] = self._io.pos()
        self.preheader = Mapsforge.Preheader(self._io, self, self._root)
        self._debug['preheader']['end'] = self._io.pos()
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(self.preheader.len_header)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Mapsforge.MapsHeader(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['maps_data']['start'] = self._io.pos()
        self.maps_data = self._io.read_bytes((self.header.len_file - self.preheader.len_header) - 24)
        self._debug['maps_data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.preheader._fetch_instances()
        self.header._fetch_instances()

    class BoundingBox(KaitaiStruct):
        SEQ_FIELDS = ["min_lat", "min_lon", "max_lat", "max_lon"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Mapsforge.BoundingBox, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['min_lat']['start'] = self._io.pos()
            self.min_lat = self._io.read_u4be()
            self._debug['min_lat']['end'] = self._io.pos()
            self._debug['min_lon']['start'] = self._io.pos()
            self.min_lon = self._io.read_u4be()
            self._debug['min_lon']['end'] = self._io.pos()
            self._debug['max_lat']['start'] = self._io.pos()
            self.max_lat = self._io.read_u4be()
            self._debug['max_lat']['end'] = self._io.pos()
            self._debug['max_lon']['start'] = self._io.pos()
            self.max_lon = self._io.read_u4be()
            self._debug['max_lon']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class GeoCoordinate(KaitaiStruct):
        SEQ_FIELDS = ["lat", "lon"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Mapsforge.GeoCoordinate, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['lat']['start'] = self._io.pos()
            self.lat = self._io.read_u4be()
            self._debug['lat']['end'] = self._io.pos()
            self._debug['lon']['start'] = self._io.pos()
            self.lon = self._io.read_u4be()
            self._debug['lon']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class MapsHeader(KaitaiStruct):
        SEQ_FIELDS = ["version", "len_file", "creation_data", "bounding_box", "tile_size", "projection", "flags", "map_start_position", "start_zoom_level", "language_preference", "comment", "created_by", "poi_tags", "way_tags", "num_zoom_intervals", "zoom_intervals"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Mapsforge.MapsHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u4be()
            self._debug['version']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u8be()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['creation_data']['start'] = self._io.pos()
            self.creation_data = self._io.read_u8be()
            self._debug['creation_data']['end'] = self._io.pos()
            self._debug['bounding_box']['start'] = self._io.pos()
            self.bounding_box = Mapsforge.BoundingBox(self._io, self, self._root)
            self._debug['bounding_box']['end'] = self._io.pos()
            self._debug['tile_size']['start'] = self._io.pos()
            self.tile_size = self._io.read_u2be()
            self._debug['tile_size']['end'] = self._io.pos()
            self._debug['projection']['start'] = self._io.pos()
            self.projection = Mapsforge.MapsforgeString(self._io, self, self._root)
            self._debug['projection']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            if self.has_map_start_position_field:
                pass
                self._debug['map_start_position']['start'] = self._io.pos()
                self.map_start_position = Mapsforge.GeoCoordinate(self._io, self, self._root)
                self._debug['map_start_position']['end'] = self._io.pos()

            if self.has_start_zoom_level_field:
                pass
                self._debug['start_zoom_level']['start'] = self._io.pos()
                self.start_zoom_level = self._io.read_u1()
                self._debug['start_zoom_level']['end'] = self._io.pos()

            if self.has_language_preference_field:
                pass
                self._debug['language_preference']['start'] = self._io.pos()
                self.language_preference = Mapsforge.MapsforgeString(self._io, self, self._root)
                self._debug['language_preference']['end'] = self._io.pos()

            if self.has_comment_field:
                pass
                self._debug['comment']['start'] = self._io.pos()
                self.comment = Mapsforge.MapsforgeString(self._io, self, self._root)
                self._debug['comment']['end'] = self._io.pos()

            if self.has_created_by_field:
                pass
                self._debug['created_by']['start'] = self._io.pos()
                self.created_by = Mapsforge.MapsforgeString(self._io, self, self._root)
                self._debug['created_by']['end'] = self._io.pos()

            self._debug['poi_tags']['start'] = self._io.pos()
            self.poi_tags = Mapsforge.Tags(self._io, self, self._root)
            self._debug['poi_tags']['end'] = self._io.pos()
            self._debug['way_tags']['start'] = self._io.pos()
            self.way_tags = Mapsforge.Tags(self._io, self, self._root)
            self._debug['way_tags']['end'] = self._io.pos()
            self._debug['num_zoom_intervals']['start'] = self._io.pos()
            self.num_zoom_intervals = self._io.read_u1()
            self._debug['num_zoom_intervals']['end'] = self._io.pos()
            self._debug['zoom_intervals']['start'] = self._io.pos()
            self._debug['zoom_intervals']['arr'] = []
            self.zoom_intervals = []
            for i in range(self.num_zoom_intervals):
                self._debug['zoom_intervals']['arr'].append({'start': self._io.pos()})
                self.zoom_intervals.append(Mapsforge.ZoomInterval(self.len_file, self._io, self, self._root))
                self._debug['zoom_intervals']['arr'][i]['end'] = self._io.pos()

            self._debug['zoom_intervals']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.bounding_box._fetch_instances()
            self.projection._fetch_instances()
            if self.has_map_start_position_field:
                pass
                self.map_start_position._fetch_instances()

            if self.has_start_zoom_level_field:
                pass

            if self.has_language_preference_field:
                pass
                self.language_preference._fetch_instances()

            if self.has_comment_field:
                pass
                self.comment._fetch_instances()

            if self.has_created_by_field:
                pass
                self.created_by._fetch_instances()

            self.poi_tags._fetch_instances()
            self.way_tags._fetch_instances()
            for i in range(len(self.zoom_intervals)):
                pass
                self.zoom_intervals[i]._fetch_instances()


        @property
        def has_comment_field(self):
            if hasattr(self, '_m_has_comment_field'):
                return self._m_has_comment_field

            self._m_has_comment_field = self.flags & 8 == 8
            return getattr(self, '_m_has_comment_field', None)

        @property
        def has_created_by_field(self):
            if hasattr(self, '_m_has_created_by_field'):
                return self._m_has_created_by_field

            self._m_has_created_by_field = self.flags & 4 == 4
            return getattr(self, '_m_has_created_by_field', None)

        @property
        def has_debug_information(self):
            if hasattr(self, '_m_has_debug_information'):
                return self._m_has_debug_information

            self._m_has_debug_information = self.flags & 128 == 128
            return getattr(self, '_m_has_debug_information', None)

        @property
        def has_language_preference_field(self):
            if hasattr(self, '_m_has_language_preference_field'):
                return self._m_has_language_preference_field

            self._m_has_language_preference_field = self.flags & 16 == 16
            return getattr(self, '_m_has_language_preference_field', None)

        @property
        def has_map_start_position_field(self):
            if hasattr(self, '_m_has_map_start_position_field'):
                return self._m_has_map_start_position_field

            self._m_has_map_start_position_field = self.flags & 64 == 64
            return getattr(self, '_m_has_map_start_position_field', None)

        @property
        def has_start_zoom_level_field(self):
            if hasattr(self, '_m_has_start_zoom_level_field'):
                return self._m_has_start_zoom_level_field

            self._m_has_start_zoom_level_field = self.flags & 32 == 32
            return getattr(self, '_m_has_start_zoom_level_field', None)


    class MapsforgeString(KaitaiStruct):
        SEQ_FIELDS = ["len_string", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Mapsforge.MapsforgeString, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_string']['start'] = self._io.pos()
            self.len_string = vlq_base128_le.VlqBase128Le(self._io)
            self._debug['len_string']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = (self._io.read_bytes(self.len_string.value)).decode(u"UTF-8")
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.len_string._fetch_instances()


    class Preheader(KaitaiStruct):
        SEQ_FIELDS = ["magic", "len_header"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Mapsforge.Preheader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(20)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x6D\x61\x70\x73\x66\x6F\x72\x67\x65\x20\x62\x69\x6E\x61\x72\x79\x20\x4F\x53\x4D":
                raise kaitaistruct.ValidationNotEqualError(b"\x6D\x61\x70\x73\x66\x6F\x72\x67\x65\x20\x62\x69\x6E\x61\x72\x79\x20\x4F\x53\x4D", self.magic, self._io, u"/types/preheader/seq/0")
            self._debug['len_header']['start'] = self._io.pos()
            self.len_header = self._io.read_u4be()
            self._debug['len_header']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Tags(KaitaiStruct):
        SEQ_FIELDS = ["num_tags", "tags"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Mapsforge.Tags, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_tags']['start'] = self._io.pos()
            self.num_tags = self._io.read_u2be()
            self._debug['num_tags']['end'] = self._io.pos()
            self._debug['tags']['start'] = self._io.pos()
            self._debug['tags']['arr'] = []
            self.tags = []
            for i in range(self.num_tags):
                self._debug['tags']['arr'].append({'start': self._io.pos()})
                self.tags.append(Mapsforge.MapsforgeString(self._io, self, self._root))
                self._debug['tags']['arr'][i]['end'] = self._io.pos()

            self._debug['tags']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.tags)):
                pass
                self.tags[i]._fetch_instances()



    class ZoomInterval(KaitaiStruct):
        SEQ_FIELDS = ["base_zoom_level", "minimal_zoom_level", "maximal_zoom_level", "ofs_sub_file", "len_sub_file"]
        def __init__(self, max_offset, _io, _parent=None, _root=None):
            super(Mapsforge.ZoomInterval, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.max_offset = max_offset
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['base_zoom_level']['start'] = self._io.pos()
            self.base_zoom_level = self._io.read_u1()
            self._debug['base_zoom_level']['end'] = self._io.pos()
            self._debug['minimal_zoom_level']['start'] = self._io.pos()
            self.minimal_zoom_level = self._io.read_u1()
            self._debug['minimal_zoom_level']['end'] = self._io.pos()
            self._debug['maximal_zoom_level']['start'] = self._io.pos()
            self.maximal_zoom_level = self._io.read_u1()
            self._debug['maximal_zoom_level']['end'] = self._io.pos()
            self._debug['ofs_sub_file']['start'] = self._io.pos()
            self.ofs_sub_file = self._io.read_u8be()
            self._debug['ofs_sub_file']['end'] = self._io.pos()
            if not self.ofs_sub_file >= self._root.preheader.len_header:
                raise kaitaistruct.ValidationLessThanError(self._root.preheader.len_header, self.ofs_sub_file, self._io, u"/types/zoom_interval/seq/3")
            if not self.ofs_sub_file <= self.max_offset:
                raise kaitaistruct.ValidationGreaterThanError(self.max_offset, self.ofs_sub_file, self._io, u"/types/zoom_interval/seq/3")
            self._debug['len_sub_file']['start'] = self._io.pos()
            self.len_sub_file = self._io.read_u8be()
            self._debug['len_sub_file']['end'] = self._io.pos()
            if not self.len_sub_file <= self.max_offset - self.ofs_sub_file:
                raise kaitaistruct.ValidationGreaterThanError(self.max_offset - self.ofs_sub_file, self.len_sub_file, self._io, u"/types/zoom_interval/seq/4")


        def _fetch_instances(self):
            pass



