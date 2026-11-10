# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Xara(KaitaiStruct):
    """
    .. seealso::
       Source - https://en.wikipedia.org/wiki/Xar_(graphics)
    
    
    .. seealso::
       Source - http://site.xara.com/support/docs/webformat/spec/XARFormatDocument.pdf
    """

    class Compression(IntEnum):
        zlib = 0

    class Tags(IntEnum):
        up = 0
        down = 1
        file_header = 2
        end_of_file = 3
        atomic_tags = 10
        essential_tags = 11
        tag_description = 12
        start_compression = 30
        end_compression = 31
        document = 40
        chapter = 41
        spread = 42
        layer = 43
        page = 44
        spread_information = 45
        grid_ruler_settings = 46
        grid_ruler_origin = 47
        layer_details = 48
        guide_layer_details = 49
        define_rgb_colour = 50
        define_complex_colour = 51
        spread_scaling_active = 52
        spread_scaling_inactive = 53
        reserved60 = 60
        preview_bitmap_gif = 61
        preview_bitmap_jpeg = 62
        preview_bitmap_png = 63
        reserved64 = 64
        reserved65 = 65
        reserved66 = 66
        define_bitmap_jpeg = 67
        define_bitmap_png = 68
        reserved69 = 69
        reserved70 = 70
        define_bitmap_jpeg8bpp = 71
        viewport = 80
        view_quality = 81
        document_view = 82
        define_prefix_user_unit = 85
        define_suffix_user_unit = 86
        define_default_units = 87
        document_comment = 90
        document_dates = 91
        document_undo_size = 92
        document_flags = 93
        path = 100
        path_filled = 101
        path_stroked = 102
        path_filled_stroked = 103
        group = 104
        blend = 105
        blender = 106
        mould_envelope = 107
        mould_perspective = 108
        mould_group = 109
        mould_path = 110
        path_flags = 111
        guideline = 112
        path_relative = 113
        path_relative_filled = 114
        path_relative_stroked = 115
        path_relative_filled_striked = 116
        reserved117 = 117
        pathref_transform = 118
        flat_fill = 150
        line_colour = 151
        line_width = 152
        linear_fill = 153
        circular_fill = 154
        elliptical_fill = 155
        conical_fill = 156
        bitmap_fill = 157
        contone_bitmap_fill = 158
        fractal_fill = 159
        fill_effect_fade = 160
        fill_effect_rainbow = 161
        fill_effect_alt_rainbow = 162
        fill_repeating = 163
        fill_non_repeating = 164
        fill_repeating_inverted = 165
        flat_transparent_fill = 166
        linear_transparent_fill = 167
        circular_transparent_fill = 168
        ellipitcal_transparent_fill = 169
        conical_transparent_fill = 170
        bitmap_transparent_fill = 171
        fractal_transparent_fill = 172
        line_transparency = 173
        start_cap = 174
        end_cap = 175
        join_style = 176
        mitre_limit = 177
        winding_rule = 178
        quality = 179
        transparent_fill_repeating = 180
        transparent_fill_non_repeating = 181
        transparent_fill_repeating_inverted = 182
        dash_style = 183
        define_dash = 184
        arrow_head = 185
        arrow_tail = 186
        define_arrow = 187
        define_dash_scaled = 188
        user_value = 189
        flat_fill_none = 190
        flat_fill_black = 191
        flat_fill_white = 192
        line_colour_none = 193
        line_colour_black = 194
        line_colour_white = 195
        node_bitmap = 198
        node_contoned_bitmap = 199
        diamond_fill = 200
        diamond_transparent_fill = 201
        three_col_fill = 202
        three_col_transparent_fill = 203
        four_col_fill = 204
        four_col_transparent_fill = 205
        fill_repeating_extra = 206
        transparent_fill_repeating_extra = 207
        ellipse_simple = 1000
        ellipse_complex = 1001
        rectangle_simple = 1100
        rectangle_simple_reformed = 1101
        rectangle_simple_stellated = 1102
        rectangle_simple_stellated_reformed = 1103
        rectangle_simple_rounded = 1104
        rectangle_simple_rounded_reformed = 1105
        rectangle_simple_rounded_stellated = 1106
        rectangle_simple_rounded_stellated_reformed = 1107
        rectangle_complex = 1108
        rectangle_complex_reformed = 1109
        rectangle_complex_stellated = 1110
        rectangle_complex_stellated_reformed = 1111
        rectangle_complex_rounded = 1112
        rectangle_complex_rounded_reformed = 1113
        rectangle_complex_rounded_stellated = 1114
        rectangle_complex_rounded_stellated_reformed = 1115
        polygon_complex = 1200
        polygon_complex_reformed = 1201
        polygon_complex_stellated = 1212
        polygon_complex_stellated_reformed = 1213
        polygon_complex_rounded = 1214
        polygon_complex_rounded_reformed = 1215
        polygon_complex_rounded_stellated = 1216
        polygon_complex_rounded_stellated_reformed = 1217
        regular_shape_phase_1 = 1900
        regular_shape_phase_2 = 1901
        font_def_truetype = 2000
        font_def_atm = 2001
        text_story_simple = 2100
        text_story_complex = 2101
        text_story_simple_start_left = 2110
        text_story_simple_start_right = 2111
        text_story_simple_end_left = 2112
        text_story_simple_end_right = 2113
        text_story_complex_start_left = 2114
        text_story_complex_start_right = 2115
        text_story_complex_end_left = 2116
        text_story_complex_end_right = 2117
        text_story_word_wrap_info = 2150
        text_story_indent_info = 2151
        text_line = 2200
        text_string = 2201
        text_char = 2202
        text_eol = 2203
        text_kern = 2204
        text_caret = 2205
        text_line_info = 2206
        text_linespace_ratio = 2900
        text_linespace_absolute = 2901
        text_justification_left = 2902
        text_justification_centre = 2903
        text_justification_right = 2904
        text_justification_full = 2905
        text_font_size = 2906
        text_font_typeface = 2907
        text_bold_on = 2908
        text_bold_off = 2909
        text_italic_on = 2910
        text_italic_off = 2911
        text_underline_on = 2912
        text_underline_off = 2913
        text_script_on = 2914
        text_script_off = 2915
        text_superscript_on = 2916
        text_superscript_off = 2917
        text_tracking = 2918
        text_aspect_ratio = 2919
        text_baseline = 2920
        overprint_line_on = 3500
        overprint_line_off = 3501
        overprint_fill_on = 3502
        overprint_fill_off = 3503
        print_on_all_plates_on = 3504
        print_on_all_plates_off = 3505
        printer_settings = 3506
        image_setting = 3507
        colour_plate = 3508
        print_mark_default = 3509
        reserved3510 = 3510
        variable_width_func = 4000
        variable_width_table = 4001
        stroke_type = 4002
        stroke_definition = 4003
        stroke_airbrush = 4004
        noise_fill = 4010
        noise_transparent_fill = 4011
        mould_bounds = 4012
        export_hint = 4015
        web_address = 4020
        web_address_bounding_box = 4021
        layer_frame_props = 4030
        spread_anim_props = 4031
        wizop = 4040
        wizop_style = 4041
        wizop_style_ref = 4042
        shadow_controller = 4050
        shadow = 4051
        bevel = 4052
        bev_attr_indent = 4053
        bev_attr_light_angle = 4054
        bev_attr_light_contrast = 4055
        bev_attr_type = 4056
        bevel_link = 4057
        blender_curve_prop = 4060
        blend_path = 4061
        blender_curve_angles = 4062
        contour_controller = 4066
        contour = 4067
        set_sentinel = 4070
        set_property = 4071
        blend_profiles = 4072
        blender_additional = 4073
        node_blend_path_filled = 4074
        linear_fill_multi_stage = 4075
        circular_fill_multistage = 4076
        elliptical_fill_multistage = 4077
        conical_fill_multistage = 4078
        brush_attr = 4079
        brush_definition = 4080
        brush_data = 4081
        more_brush_data = 4082
        more_brush_attr = 4083
        clip_view_controller = 4084
        clip_view = 4085
        feather = 4086
        bar_property = 4087
        square_fill_multi_stage = 4088
        even_more_brush_data = 4102
        even_more_brush_attr = 4103
        time_stamp_brush_data = 4104
        brush_pressure_info = 4105
        brush_pressure_data = 4106
        brush_attr_pressure_info = 4107
        brush_colour_data = 4108
        brush_pressure_sample_data = 4109
        brush_time_sample_data = 4110
        brush_attr_fill_flags = 4111
        brush_transp_info = 4112
        brush_attr_transp_info = 4113
        document_nudge = 4114
        bitmap_properties = 4115
        document_bitmap_smoothing = 4116
        xpe_bitmap_properties = 4117
        define_bitmap_xpe = 4118
        current_attributes = 4119
        current_attribute_bounds = 4120
        linear_fill_3point = 4121
        linear_fill_multistage_3point = 4122
        linear_transparent_fill_3point = 4123
        duplication_offset = 4124
        live_effect = 4125
        locked_effect = 4126
        feather_effect = 4127
        compound_render = 4128
        object_bounds = 4129
        spread_phase2 = 4131
        current_attributes_phase2 = 4132
        spread_flash_props = 4134
        printer_settings_phase2 = 4135
        document_information = 4136
        clipview_path = 4137
        define_bitmap_png_real = 4138
        text_string_pos = 4139
        spread_flash_props2 = 4140
        text_linespace_leading = 4141
        text_tab = 4200
        text_left_indent = 4201
        text_first_indent = 4202
        text_right_indent = 4203
        text_ruler = 4204
        text_story_height_info = 4205
        text_story_link_info = 4206
        text_story_translation_info = 4207
        text_space_before = 4208
        text_space_after = 4209
        text_special_hyphen = 4210
        text_soft_return = 4211
        text_extra_font_info = 4212
        text_extra_tt_font_def = 4213
        text_extra_atm_font_def = 4214
    SEQ_FIELDS = ["header", "records"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Xara, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Xara.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['records']['start'] = self._io.pos()
        self._debug['records']['arr'] = []
        self.records = []
        i = 0
        while True:
            self._debug['records']['arr'].append({'start': self._io.pos()})
            _ = Xara.Record(self._io, self, self._root)
            self.records.append(_)
            self._debug['records']['arr'][len(self.records) - 1]['end'] = self._io.pos()
            if  ((_.tag == Xara.Tags.end_of_file) or (_.tag == Xara.Tags.start_compression)) :
                break
            i += 1
        self._debug['records']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.records)):
            pass
            self.records[i]._fetch_instances()


    class DocumentBitmapSmoothing(KaitaiStruct):
        SEQ_FIELDS = ["flags", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Xara.DocumentBitmapSmoothing, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(4)
            self._debug['reserved']['end'] = self._io.pos()
            if not self.reserved == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.reserved, self._io, u"/types/document_bitmap_smoothing/seq/1")


        def _fetch_instances(self):
            pass

        @property
        def enable_bitmap_smoothing(self):
            if hasattr(self, '_m_enable_bitmap_smoothing'):
                return self._m_enable_bitmap_smoothing

            self._m_enable_bitmap_smoothing = self.flags & 1
            return getattr(self, '_m_enable_bitmap_smoothing', None)


    class DocumentNudge(KaitaiStruct):
        SEQ_FIELDS = ["millipoint"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Xara.DocumentNudge, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['millipoint']['start'] = self._io.pos()
            self.millipoint = self._io.read_u4le()
            self._debug['millipoint']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class DuplicationOffset(KaitaiStruct):
        SEQ_FIELDS = ["coords"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Xara.DuplicationOffset, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['coords']['start'] = self._io.pos()
            self.coords = self._io.read_bytes(8)
            self._debug['coords']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class FileHeader(KaitaiStruct):
        SEQ_FIELDS = ["filetype", "len_file", "weblink", "refinement_flags", "producer", "producer_version", "producer_build"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Xara.FileHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['filetype']['start'] = self._io.pos()
            self.filetype = self._io.read_bytes(3)
            self._debug['filetype']['end'] = self._io.pos()
            self._debug['len_file']['start'] = self._io.pos()
            self.len_file = self._io.read_u4le()
            self._debug['len_file']['end'] = self._io.pos()
            self._debug['weblink']['start'] = self._io.pos()
            self.weblink = self._io.read_u4le()
            self._debug['weblink']['end'] = self._io.pos()
            self._debug['refinement_flags']['start'] = self._io.pos()
            self.refinement_flags = self._io.read_u4le()
            self._debug['refinement_flags']['end'] = self._io.pos()
            self._debug['producer']['start'] = self._io.pos()
            self.producer = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['producer']['end'] = self._io.pos()
            self._debug['producer_version']['start'] = self._io.pos()
            self.producer_version = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['producer_version']['end'] = self._io.pos()
            self._debug['producer_build']['start'] = self._io.pos()
            self.producer_build = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['producer_build']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "magic2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Xara.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x58\x41\x52\x41":
                raise kaitaistruct.ValidationNotEqualError(b"\x58\x41\x52\x41", self.magic, self._io, u"/types/header/seq/0")
            self._debug['magic2']['start'] = self._io.pos()
            self.magic2 = self._io.read_bytes(4)
            self._debug['magic2']['end'] = self._io.pos()
            if not self.magic2 == b"\xA3\xA3\x0D\x0A":
                raise kaitaistruct.ValidationNotEqualError(b"\xA3\xA3\x0D\x0A", self.magic2, self._io, u"/types/header/seq/1")


        def _fetch_instances(self):
            pass


    class Record(KaitaiStruct):
        SEQ_FIELDS = ["tag", "len_data", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Xara.Record, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tag']['start'] = self._io.pos()
            self.tag = KaitaiStream.resolve_enum(Xara.Tags, self._io.read_u4le())
            self._debug['tag']['end'] = self._io.pos()
            self._debug['len_data']['start'] = self._io.pos()
            self.len_data = self._io.read_u4le()
            self._debug['len_data']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            _on = self.tag
            if _on == Xara.Tags.document_bitmap_smoothing:
                pass
                self._raw_data = self._io.read_bytes(self.len_data)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Xara.DocumentBitmapSmoothing(_io__raw_data, self, self._root)
            elif _on == Xara.Tags.document_nudge:
                pass
                self._raw_data = self._io.read_bytes(self.len_data)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Xara.DocumentNudge(_io__raw_data, self, self._root)
            elif _on == Xara.Tags.duplication_offset:
                pass
                self._raw_data = self._io.read_bytes(self.len_data)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Xara.DuplicationOffset(_io__raw_data, self, self._root)
            elif _on == Xara.Tags.file_header:
                pass
                self._raw_data = self._io.read_bytes(self.len_data)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Xara.FileHeader(_io__raw_data, self, self._root)
            elif _on == Xara.Tags.start_compression:
                pass
                self._raw_data = self._io.read_bytes(self.len_data)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Xara.StartCompression(_io__raw_data, self, self._root)
            else:
                pass
                self.data = self._io.read_bytes(self.len_data)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.tag
            if _on == Xara.Tags.document_bitmap_smoothing:
                pass
                self.data._fetch_instances()
            elif _on == Xara.Tags.document_nudge:
                pass
                self.data._fetch_instances()
            elif _on == Xara.Tags.duplication_offset:
                pass
                self.data._fetch_instances()
            elif _on == Xara.Tags.file_header:
                pass
                self.data._fetch_instances()
            elif _on == Xara.Tags.start_compression:
                pass
                self.data._fetch_instances()
            else:
                pass


    class StartCompression(KaitaiStruct):
        SEQ_FIELDS = ["version", "format"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Xara.StartCompression, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_bytes(3)
            self._debug['version']['end'] = self._io.pos()
            self._debug['format']['start'] = self._io.pos()
            self.format = KaitaiStream.resolve_enum(Xara.Compression, self._io.read_u1())
            self._debug['format']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



