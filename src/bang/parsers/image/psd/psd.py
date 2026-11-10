# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Psd(KaitaiStruct):
    """
    .. seealso::
       Source - https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/
    """

    class ColorMode(IntEnum):
        bitmap = 0
        grayscale = 1
        indexed = 2
        rgb = 3
        cmyk = 4
        multichannel = 7
        duotone = 8
        lab = 9

    class Compression(IntEnum):
        raw = 0
        rle = 1
        zip_without_prediction = 2
        zip_with_prediction = 3

    class ResourceIds(IntEnum):
        photoshop_20_information = 1000
        macintosh_print_manager_print_info = 1001
        macintosh_page_format_information = 1002
        indexed_color_table = 1003
        resolution_info = 1005
        alpha_channel_names = 1006
        display_info_structure = 1007
        caption = 1008
        border_information = 1009
        background_color = 1010
        print_flags = 1011
        grayscale_multichannel_halftoning = 1012
        color_halftoning = 1013
        duotone_halftoning = 1014
        grayscale_multichannel_transfer_function = 1015
        color_transfer_function = 1016
        duotone_transfer_function = 1017
        duotone_image_information = 1018
        effective_black_white = 1019
        obsolete_1020 = 1020
        eps_options = 1021
        quick_mask_information = 1022
        obsolete_1023 = 1023
        layer_state_information = 1024
        working_path = 1025
        layers_group_information = 1026
        obsolete_1027 = 1027
        iptc_naa_record = 1028
        image_mode_raw = 1029
        jpeg_quality = 1030
        grid_and_guides = 1032
        thumbnail_resource_photoshop_40 = 1033
        copyright_flag = 1034
        url = 1035
        thumbnail_resource = 1036
        global_angle = 1037
        color_samplers_resource_photoshop_50 = 1038
        icc_profile = 1039
        watermark = 1040
        icc_untagged_profile = 1041
        effects_visible = 1042
        spot_halftone = 1043
        document_specific_ids_seed_number = 1044
        unicode_alpha_names = 1045
        indexed_color_table_count = 1046
        transparancy_index = 1047
        global_altitude = 1049
        slices = 1050
        workflow_url = 1051
        jump_to_xpep = 1052
        alpha_identifiers = 1053
        url_list = 1054
        version_info = 1057
        exif_data_1 = 1058
        exif_data_3 = 1059
        xmp_metadata = 1060
        caption_digest = 1061
        print_scale = 1062
        pixel_aspect_ratio = 1064
        layer_comps = 1065
        alternate_duotone_colors = 1066
        alternate_spot_colors = 1067
        layer_selection_ids = 1069
        hdr_toning_information = 1070
        print_info = 1071
        layer_groups_enabled_id = 1072
        color_samplers_resource = 1073
        measurement_scale = 1074
        timeline_information = 1075
        sheet_disclosure = 1076
        displayinfo_structure = 1077
        onion_skins = 1078
        count_information = 1080
        print_information = 1082
        print_style = 1083
        macintosh_nsprintinfo = 1084
        windows_devmode = 1085
        auto_save_file_path = 1086
        auto_save_format = 1087
        path_selection_state = 1088
        name_clipping_path = 2999
        origin_path_info = 3000
        image_ready_variables = 7000
        image_ready_data_sets = 7001
        image_ready_default_selected_state = 7002
        image_ready_7_rollover_expanded_state = 7003
        image_ready_rollover_expanded_state = 7004
        image_ready_save_layer_settings = 7005
        image_ready_version = 7006
        lightroom_workflow = 8000
        print_flags_information = 10000
    SEQ_FIELDS = ["header", "color_mode_data", "image_resources", "layer_and_mask_information", "image_data"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Psd, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = Psd.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['color_mode_data']['start'] = self._io.pos()
        self.color_mode_data = Psd.ColorModeData(self._io, self, self._root)
        self._debug['color_mode_data']['end'] = self._io.pos()
        self._debug['image_resources']['start'] = self._io.pos()
        self.image_resources = Psd.ImageResourcesData(self._io, self, self._root)
        self._debug['image_resources']['end'] = self._io.pos()
        self._debug['layer_and_mask_information']['start'] = self._io.pos()
        self.layer_and_mask_information = Psd.LayerAndMaskInformation(self._io, self, self._root)
        self._debug['layer_and_mask_information']['end'] = self._io.pos()
        self._debug['image_data']['start'] = self._io.pos()
        self.image_data = Psd.ImageData(self._io, self, self._root)
        self._debug['image_data']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.color_mode_data._fetch_instances()
        self.image_resources._fetch_instances()
        self.layer_and_mask_information._fetch_instances()
        self.image_data._fetch_instances()

    class ColorModeData(KaitaiStruct):
        SEQ_FIELDS = ["len_color_mode", "color_mode"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Psd.ColorModeData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_color_mode']['start'] = self._io.pos()
            self.len_color_mode = self._io.read_u4be()
            self._debug['len_color_mode']['end'] = self._io.pos()
            self._debug['color_mode']['start'] = self._io.pos()
            self.color_mode = self._io.read_bytes(self.len_color_mode)
            self._debug['color_mode']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "reserved", "num_channels", "height", "width", "depth", "color_mode"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Psd.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x38\x42\x50\x53":
                raise kaitaistruct.ValidationNotEqualError(b"\x38\x42\x50\x53", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u2be()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.version, self._io, u"/types/header/seq/1")
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(6)
            self._debug['reserved']['end'] = self._io.pos()
            if not self.reserved == b"\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00", self.reserved, self._io, u"/types/header/seq/2")
            self._debug['num_channels']['start'] = self._io.pos()
            self.num_channels = self._io.read_u2be()
            self._debug['num_channels']['end'] = self._io.pos()
            if not self.num_channels >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.num_channels, self._io, u"/types/header/seq/3")
            if not self.num_channels <= 56:
                raise kaitaistruct.ValidationGreaterThanError(56, self.num_channels, self._io, u"/types/header/seq/3")
            self._debug['height']['start'] = self._io.pos()
            self.height = self._io.read_u4be()
            self._debug['height']['end'] = self._io.pos()
            if not self.height >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.height, self._io, u"/types/header/seq/4")
            if not self.height <= 30000:
                raise kaitaistruct.ValidationGreaterThanError(30000, self.height, self._io, u"/types/header/seq/4")
            self._debug['width']['start'] = self._io.pos()
            self.width = self._io.read_u4be()
            self._debug['width']['end'] = self._io.pos()
            if not self.width >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.width, self._io, u"/types/header/seq/5")
            if not self.width <= 30000:
                raise kaitaistruct.ValidationGreaterThanError(30000, self.width, self._io, u"/types/header/seq/5")
            self._debug['depth']['start'] = self._io.pos()
            self.depth = self._io.read_u2be()
            self._debug['depth']['end'] = self._io.pos()
            if not  ((self.depth == 1) or (self.depth == 8) or (self.depth == 16) or (self.depth == 32)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.depth, self._io, u"/types/header/seq/6")
            self._debug['color_mode']['start'] = self._io.pos()
            self.color_mode = KaitaiStream.resolve_enum(Psd.ColorMode, self._io.read_u2be())
            self._debug['color_mode']['end'] = self._io.pos()
            if not  ((self.color_mode == Psd.ColorMode.bitmap) or (self.color_mode == Psd.ColorMode.grayscale) or (self.color_mode == Psd.ColorMode.indexed) or (self.color_mode == Psd.ColorMode.rgb) or (self.color_mode == Psd.ColorMode.cmyk) or (self.color_mode == Psd.ColorMode.multichannel) or (self.color_mode == Psd.ColorMode.duotone) or (self.color_mode == Psd.ColorMode.lab)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.color_mode, self._io, u"/types/header/seq/7")


        def _fetch_instances(self):
            pass


    class ImageData(KaitaiStruct):
        SEQ_FIELDS = ["compression", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Psd.ImageData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['compression']['start'] = self._io.pos()
            self.compression = KaitaiStream.resolve_enum(Psd.Compression, self._io.read_u2be())
            self._debug['compression']['end'] = self._io.pos()
            if not  ((self.compression == Psd.Compression.raw) or (self.compression == Psd.Compression.rle)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.compression, self._io, u"/types/image_data/seq/0")
            self._debug['data']['start'] = self._io.pos()
            _on = self.compression
            if _on == Psd.Compression.raw:
                pass
                self.data = Psd.RawData(self._io, self, self._root)
            elif _on == Psd.Compression.rle:
                pass
                self.data = Psd.RleData(self._io, self, self._root)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.compression
            if _on == Psd.Compression.raw:
                pass
                self.data._fetch_instances()
            elif _on == Psd.Compression.rle:
                pass
                self.data._fetch_instances()


    class ImageResource(KaitaiStruct):
        SEQ_FIELDS = ["magic", "resource_id", "name", "padding1", "len_resource", "data", "padding2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Psd.ImageResource, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x38\x42\x49\x4D":
                raise kaitaistruct.ValidationNotEqualError(b"\x38\x42\x49\x4D", self.magic, self._io, u"/types/image_resource/seq/0")
            self._debug['resource_id']['start'] = self._io.pos()
            self.resource_id = KaitaiStream.resolve_enum(Psd.ResourceIds, self._io.read_u2be())
            self._debug['resource_id']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = Psd.PascalString(self._io, self, self._root)
            self._debug['name']['end'] = self._io.pos()
            if self.name.len_string % 2 == 0:
                pass
                self._debug['padding1']['start'] = self._io.pos()
                self.padding1 = self._io.read_bytes(1)
                self._debug['padding1']['end'] = self._io.pos()

            self._debug['len_resource']['start'] = self._io.pos()
            self.len_resource = self._io.read_u4be()
            self._debug['len_resource']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            _on = self.resource_id
            if _on == Psd.ResourceIds.xmp_metadata:
                pass
                self._raw_data = self._io.read_bytes(self.len_resource)
                _io__raw_data = KaitaiStream(BytesIO(self._raw_data))
                self.data = Psd.Xmp(_io__raw_data, self, self._root)
            else:
                pass
                self.data = self._io.read_bytes(self.len_resource)
            self._debug['data']['end'] = self._io.pos()
            if self.len_resource % 2 == 1:
                pass
                self._debug['padding2']['start'] = self._io.pos()
                self.padding2 = self._io.read_bytes(1)
                self._debug['padding2']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.name._fetch_instances()
            if self.name.len_string % 2 == 0:
                pass

            _on = self.resource_id
            if _on == Psd.ResourceIds.xmp_metadata:
                pass
                self.data._fetch_instances()
            else:
                pass
            if self.len_resource % 2 == 1:
                pass



    class ImageResources(KaitaiStruct):
        SEQ_FIELDS = ["image_resources"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Psd.ImageResources, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['image_resources']['start'] = self._io.pos()
            self._debug['image_resources']['arr'] = []
            self.image_resources = []
            i = 0
            while not self._io.is_eof():
                self._debug['image_resources']['arr'].append({'start': self._io.pos()})
                self.image_resources.append(Psd.ImageResource(self._io, self, self._root))
                self._debug['image_resources']['arr'][len(self.image_resources) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['image_resources']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.image_resources)):
                pass
                self.image_resources[i]._fetch_instances()



    class ImageResourcesData(KaitaiStruct):
        SEQ_FIELDS = ["len_resources", "resources"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Psd.ImageResourcesData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_resources']['start'] = self._io.pos()
            self.len_resources = self._io.read_u4be()
            self._debug['len_resources']['end'] = self._io.pos()
            self._debug['resources']['start'] = self._io.pos()
            self._raw_resources = self._io.read_bytes(self.len_resources)
            _io__raw_resources = KaitaiStream(BytesIO(self._raw_resources))
            self.resources = Psd.ImageResources(_io__raw_resources, self, self._root)
            self._debug['resources']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.resources._fetch_instances()


    class LayerAndMaskInformation(KaitaiStruct):
        SEQ_FIELDS = ["len_layer_and_mask_information", "layer_and_mask_information"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Psd.LayerAndMaskInformation, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_layer_and_mask_information']['start'] = self._io.pos()
            self.len_layer_and_mask_information = self._io.read_u4be()
            self._debug['len_layer_and_mask_information']['end'] = self._io.pos()
            self._debug['layer_and_mask_information']['start'] = self._io.pos()
            self.layer_and_mask_information = self._io.read_bytes(self.len_layer_and_mask_information)
            self._debug['layer_and_mask_information']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PascalString(KaitaiStruct):
        SEQ_FIELDS = ["len_string", "string"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Psd.PascalString, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_string']['start'] = self._io.pos()
            self.len_string = self._io.read_u1()
            self._debug['len_string']['end'] = self._io.pos()
            self._debug['string']['start'] = self._io.pos()
            self.string = self._io.read_bytes(self.len_string)
            self._debug['string']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class RawData(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Psd.RawData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes((self._root.header.height * self._root.header.width) * self._root.header.num_channels)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class RleData(KaitaiStruct):
        SEQ_FIELDS = ["byte_counts", "rle"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Psd.RleData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['byte_counts']['start'] = self._io.pos()
            self._debug['byte_counts']['arr'] = []
            self.byte_counts = []
            for i in range(self._root.header.height * self._root.header.num_channels):
                self._debug['byte_counts']['arr'].append({'start': self._io.pos()})
                self.byte_counts.append(self._io.read_u2be())
                self._debug['byte_counts']['arr'][i]['end'] = self._io.pos()

            self._debug['byte_counts']['end'] = self._io.pos()
            self._debug['rle']['start'] = self._io.pos()
            self._debug['rle']['arr'] = []
            self.rle = []
            for i in range(self._root.header.height * self._root.header.num_channels):
                self._debug['rle']['arr'].append({'start': self._io.pos()})
                self.rle.append(self._io.read_bytes(self.byte_counts[i]))
                self._debug['rle']['arr'][i]['end'] = self._io.pos()

            self._debug['rle']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.byte_counts)):
                pass

            for i in range(len(self.rle)):
                pass



    class Xmp(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Psd.Xmp, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = (self._io.read_bytes_full()).decode(u"UTF-8")
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



