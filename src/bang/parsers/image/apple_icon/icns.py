# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from . import bytes_with_io
from .bytes_with_io import *
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Icns(KaitaiStruct):
    """Icon image format used by Mac OS 8.5 and later,
    including all versions of Mac OS X/macOS.
    This is the Mac equivalent of the Windows ICO format.
    
    An ICNS file stores an *icon family*:
    a collection of images with visually the same content,
    but at different resolutions and color depths.
    When the system renders an icon on screen,
    it chooses the most optimal format from the icon family to display to the user,
    depending on the icon's displayed size and the capabilities of the display hardware.
    
    An icon family in an ICNS file can also contain other nested icon families.
    This feature is sometimes used to represent different states or visual variants of the same icon,
    such as an opened, selected or dark mode version.
    
    Each icon in an icon family is identified by a four-byte type code,
    which also indicates the image data format and resolution.
    Supported formats include PNG and JPEG 2000 (for larger sizes and modern systems)
    and multiple raw bitmap formats with varying resolution, color depth, and transparency support
    (for smaller sizes and/or compatibility with older systems).
    
    ICNS data can be stored either as a standalone file,
    or as a resource with type code `'icns'` in a resource fork.
    The latter was especially common on Classic Mac OS and for Carbon applications,
    and is still used (as of macOS 10.14) by the Finder to store custom file and folder icons set by the user.
    
    .. seealso::
       <OSServices/IconStorage.h>
    
    
    .. seealso::
       <OSServices/IconStorage.r>
    
    
    .. seealso::
       <HIServices/Icons.r>
    
    
    .. seealso::
       libicns SourceForge project - https://sourceforge.net/p/icns/
    
    
    .. seealso::
       Python Pillow ICNS plugin code - https://github.com/python-pillow/Pillow/blob/master/src/PIL/IcnsImagePlugin.py
    
    
    .. seealso::
       Information about 'icns' resources in resource forks - https://www.macdisk.com/maciconen.php#icns
    """

    class ElementType(IntEnum):
        icon_32x32x1_with_mask = 1229147683
        table_of_contents = 1414480672
        drop_variant_family = 1685221232
        icon_48x48x8_mask = 1748528491
        icon_16x16_argb = 1768108084
        icon_32x32_argb = 1768108085
        icon_128x128_png_jp2 = 1768108087
        icon_256x256_png_jp2 = 1768108088
        icon_512x512_png_jp2 = 1768108089
        icon_512x512_at_2x_png_jp2 = 1768108336
        icon_16x16_at_2x_png_jp2 = 1768108337
        icon_32x32_at_2x_png_jp2 = 1768108338
        icon_128x128_at_2x_png_jp2 = 1768108339
        icon_256x256_at_2x_png_jp2 = 1768108340
        icon_48x48x1_with_mask = 1768122403
        icon_48x48x4 = 1768122420
        icon_48x48x8 = 1768122424
        icon_32x32x4 = 1768123444
        icon_32x32x8 = 1768123448
        icon_16x12x1_with_mask = 1768123683
        icon_16x12x4 = 1768123700
        icon_16x12x8 = 1768123704
        icon_composer_version = 1768123990
        main_family = 1768124019
        icon_16x16_png_jp2_rgb = 1768124468
        icon_32x32_png_jp2_rgb = 1768124469
        icon_64x64_png_jp2 = 1768124470
        icon_16x16x1_with_mask = 1768125219
        icon_16x16x4 = 1768125236
        icon_16x16x8 = 1768125240
        icon_18x18_at_2x_png_jp2 = 1768125250
        icon_18x18_argb = 1768125282
        icon_48x48_rgb = 1768436530
        icon_32x32_rgb = 1768698674
        info_dictionary = 1768842863
        icon_16x16_rgb = 1769157426
        icon_128x128_rgb = 1769222962
        icon_32x32x8_mask = 1815637355
        open_drop_variant_family = 1868853872
        open_variant_family = 1869636974
        rollover_variant_family = 1870030194
        icon_16x16x8_mask = 1933077867
        sbpp_variant_family = 1935831152
        sidebar_variant_family = 1935832176
        selected_variant_family = 1936483188
        icon_128x128x8_mask = 1949855083
        tile_variant_family = 1953066085
        dark_mode_variant_family = 4258869160
    SEQ_FIELDS = ["root_element"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Icns, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['root_element']['start'] = self._io.pos()
        self.root_element = Icns.IconFamilyElement(self._io, self, self._root)
        self._debug['root_element']['end'] = self._io.pos()
        _ = self.root_element
        if not _.header.type.as_enum == Icns.ElementType.main_family:
            raise kaitaistruct.ValidationExprError(self.root_element, self._io, u"/seq/0")


    def _fetch_instances(self):
        pass
        self.root_element._fetch_instances()

    class IcnsStylePackbits(KaitaiStruct):
        """A run-length encoding compression scheme similar to (but not the same as) PackBits.
        Used in the RGB and ARGB bitmap icon types.
        """
        SEQ_FIELDS = ["compressed_data_with_io"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Icns.IcnsStylePackbits, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['compressed_data_with_io']['start'] = self._io.pos()
            self.compressed_data_with_io = bytes_with_io.BytesWithIo(self._io)
            self._debug['compressed_data_with_io']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.compressed_data_with_io._fetch_instances()
            _ = self.chunks
            if hasattr(self, '_m_chunks'):
                pass
                for i in range(len(self._m_chunks)):
                    pass
                    self._m_chunks[i]._fetch_instances()



        class Chunk(KaitaiStruct):
            """A single chunk of compressed data.
            Each chunk stores either a sequence of literal bytes,
            or a single byte that is repeated a certain number of times.
            """
            SEQ_FIELDS = ["tag", "literal_data", "repeated_byte"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Icns.IcnsStylePackbits.Chunk, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['tag']['start'] = self._io.pos()
                self.tag = self._io.read_u1()
                self._debug['tag']['end'] = self._io.pos()
                if (not (self.is_repeat)):
                    pass
                    self._debug['literal_data']['start'] = self._io.pos()
                    self.literal_data = self._io.read_bytes(self.tag + 1)
                    self._debug['literal_data']['end'] = self._io.pos()

                if self.is_repeat:
                    pass
                    self._debug['repeated_byte']['start'] = self._io.pos()
                    self.repeated_byte = self._io.read_u1()
                    self._debug['repeated_byte']['end'] = self._io.pos()



            def _fetch_instances(self):
                pass
                if (not (self.is_repeat)):
                    pass

                if self.is_repeat:
                    pass


            @property
            def is_repeat(self):
                """If true, this is a repeat chunk.
                If false, this is a literal chunk.
                """
                if hasattr(self, '_m_is_repeat'):
                    return self._m_is_repeat

                self._m_is_repeat = self.tag >= 128
                return getattr(self, '_m_is_repeat', None)

            @property
            def len_literal_data(self):
                """If this is a literal chunk,
                the number of literal bytes stored in the chunk.
                """
                if hasattr(self, '_m_len_literal_data'):
                    return self._m_len_literal_data

                if (not (self.is_repeat)):
                    pass
                    self._m_len_literal_data = self.tag + 1

                return getattr(self, '_m_len_literal_data', None)

            @property
            def repeat_count(self):
                """If this is a repeat chunk,
                the number of times the stored byte should be repeated in the output.
                """
                if hasattr(self, '_m_repeat_count'):
                    return self._m_repeat_count

                if self.is_repeat:
                    pass
                    self._m_repeat_count = self.tag - 125

                return getattr(self, '_m_repeat_count', None)


        @property
        def chunks(self):
            """The compressed data parsed into chunks."""
            if hasattr(self, '_m_chunks'):
                return self._m_chunks

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_chunks']['start'] = self._io.pos()
            self._debug['_m_chunks']['arr'] = []
            self._m_chunks = []
            i = 0
            while not self._io.is_eof():
                self._debug['_m_chunks']['arr'].append({'start': self._io.pos()})
                self._m_chunks.append(Icns.IcnsStylePackbits.Chunk(self._io, self, self._root))
                self._debug['_m_chunks']['arr'][len(self._m_chunks) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['_m_chunks']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_chunks', None)

        @property
        def compressed_data(self):
            """The raw compressed data."""
            if hasattr(self, '_m_compressed_data'):
                return self._m_compressed_data

            self._m_compressed_data = self.compressed_data_with_io.data
            return getattr(self, '_m_compressed_data', None)


    class IconArgbData(KaitaiStruct):
        """The data for a 32-bit ARGB bitmap icon."""
        SEQ_FIELDS = ["signature", "compressed_data"]
        def __init__(self, width, height, _io, _parent=None, _root=None):
            super(Icns.IconArgbData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.width = width
            self.height = height
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(4)
            self._debug['signature']['end'] = self._io.pos()
            if not self.signature == b"\x41\x52\x47\x42":
                raise kaitaistruct.ValidationNotEqualError(b"\x41\x52\x47\x42", self.signature, self._io, u"/types/icon_argb_data/seq/0")
            self._debug['compressed_data']['start'] = self._io.pos()
            self.compressed_data = Icns.IcnsStylePackbits(self._io, self, self._root)
            self._debug['compressed_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.compressed_data._fetch_instances()


    class IconComposerVersionData(KaitaiStruct):
        """The element data for an Icon Composer version number."""
        SEQ_FIELDS = ["version"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Icns.IconComposerVersionData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_f4be()
            self._debug['version']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class IconFamilyData(KaitaiStruct):
        """The element data for an icon family."""
        SEQ_FIELDS = ["elements"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Icns.IconFamilyData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['elements']['start'] = self._io.pos()
            self._debug['elements']['arr'] = []
            self.elements = []
            i = 0
            while not self._io.is_eof():
                self._debug['elements']['arr'].append({'start': self._io.pos()})
                self.elements.append(Icns.IconFamilyElement(self._io, self, self._root))
                self._debug['elements']['arr'][len(self.elements) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['elements']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.elements)):
                pass
                self.elements[i]._fetch_instances()



    class IconFamilyElement(KaitaiStruct):
        """A single element in an icon family.
        
        It is normally safe to ignore elements with an unrecognized type code or unparseable data when reading -
        they are most likely new icon types/resolutions, icon family variants, or metadata introduced in a newer system version.
        However, when modifying and writing an icon family,
        such elements should be stripped out,
        to avoid leaving outdated information in the icon family that could be used by newer systems.
        """
        SEQ_FIELDS = ["header", "data_with_io"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Icns.IconFamilyElement, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Icns.IconFamilyElement.Header(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['data_with_io']['start'] = self._io.pos()
            self._raw_data_with_io = self._io.read_bytes(self.header.len_data)
            _io__raw_data_with_io = KaitaiStream(BytesIO(self._raw_data_with_io))
            self.data_with_io = bytes_with_io.BytesWithIo(_io__raw_data_with_io)
            self._debug['data_with_io']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.data_with_io._fetch_instances()
            _ = self.data_parsed
            if hasattr(self, '_m_data_parsed'):
                pass
                _on = self.header.type.as_enum
                if _on == Icns.ElementType.dark_mode_variant_family:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.drop_variant_family:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_128x128_at_2x_png_jp2:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_128x128_png_jp2:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_128x128_rgb:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_128x128x8_mask:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_16x12x1_with_mask:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_16x12x4:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_16x12x8:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_16x16_argb:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_16x16_at_2x_png_jp2:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_16x16_png_jp2_rgb:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_16x16_rgb:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_16x16x1_with_mask:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_16x16x4:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_16x16x8:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_16x16x8_mask:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_18x18_argb:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_18x18_at_2x_png_jp2:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_256x256_at_2x_png_jp2:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_256x256_png_jp2:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_32x32_argb:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_32x32_at_2x_png_jp2:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_32x32_png_jp2_rgb:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_32x32_rgb:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_32x32x1_with_mask:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_32x32x4:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_32x32x8:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_32x32x8_mask:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_48x48_rgb:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_48x48x1_with_mask:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_48x48x4:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_48x48x8:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_48x48x8_mask:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_512x512_at_2x_png_jp2:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_512x512_png_jp2:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_64x64_png_jp2:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.icon_composer_version:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.info_dictionary:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.main_family:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.open_drop_variant_family:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.open_variant_family:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.rollover_variant_family:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.sbpp_variant_family:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.selected_variant_family:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.sidebar_variant_family:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.table_of_contents:
                    pass
                    self._m_data_parsed._fetch_instances()
                elif _on == Icns.ElementType.tile_variant_family:
                    pass
                    self._m_data_parsed._fetch_instances()
                else:
                    pass
                    self._m_data_parsed._fetch_instances()


        class Header(KaitaiStruct):
            """An icon family element's header,
            storing the type code and length.
            """
            SEQ_FIELDS = ["type", "len_element"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Icns.IconFamilyElement.Header, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['type']['start'] = self._io.pos()
                self._raw_type = self._io.read_bytes(4)
                _io__raw_type = KaitaiStream(BytesIO(self._raw_type))
                self.type = Icns.IconFamilyElement.Header.TypeCode(_io__raw_type, self, self._root)
                self._debug['type']['end'] = self._io.pos()
                self._debug['len_element']['start'] = self._io.pos()
                self.len_element = self._io.read_u4be()
                self._debug['len_element']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.type._fetch_instances()

            class TypeCode(KaitaiStruct):
                """A four-character type code."""
                SEQ_FIELDS = ["as_bytes"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Icns.IconFamilyElement.Header.TypeCode, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['as_bytes']['start'] = self._io.pos()
                    self.as_bytes = self._io.read_bytes_full()
                    self._debug['as_bytes']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    _ = self.as_enum
                    if hasattr(self, '_m_as_enum'):
                        pass


                @property
                def as_enum(self):
                    """The type code as an integer-based enum."""
                    if hasattr(self, '_m_as_enum'):
                        return self._m_as_enum

                    _pos = self._io.pos()
                    self._io.seek(0)
                    self._debug['_m_as_enum']['start'] = self._io.pos()
                    self._m_as_enum = KaitaiStream.resolve_enum(Icns.ElementType, self._io.read_u4be())
                    self._debug['_m_as_enum']['end'] = self._io.pos()
                    self._io.seek(_pos)
                    return getattr(self, '_m_as_enum', None)


            @property
            def len_data(self):
                """The length of the data stored in the element.
                This is the length of the entire element minus the length of the header.
                """
                if hasattr(self, '_m_len_data'):
                    return self._m_len_data

                self._m_len_data = self.len_element - 8
                return getattr(self, '_m_len_data', None)


        @property
        def data(self):
            """The raw data stored in the element."""
            if hasattr(self, '_m_data'):
                return self._m_data

            self._m_data = self.data_with_io.data
            return getattr(self, '_m_data', None)

        @property
        def data_parsed(self):
            """The data stored in the element,
            parsed based on the type code in the header.
            """
            if hasattr(self, '_m_data_parsed'):
                return self._m_data_parsed

            io = self.data_with_io._io
            _pos = io.pos()
            io.seek(0)
            self._debug['_m_data_parsed']['start'] = io.pos()
            _on = self.header.type.as_enum
            if _on == Icns.ElementType.dark_mode_variant_family:
                pass
                self._m_data_parsed = Icns.IconFamilyData(io, self, self._root)
            elif _on == Icns.ElementType.drop_variant_family:
                pass
                self._m_data_parsed = Icns.IconFamilyData(io, self, self._root)
            elif _on == Icns.ElementType.icon_128x128_at_2x_png_jp2:
                pass
                self._m_data_parsed = Icns.IconPngJp2Data(128, 128, 2, io, self, self._root)
            elif _on == Icns.ElementType.icon_128x128_png_jp2:
                pass
                self._m_data_parsed = Icns.IconPngJp2Data(128, 128, 1, io, self, self._root)
            elif _on == Icns.ElementType.icon_128x128_rgb:
                pass
                self._m_data_parsed = Icns.IconRgbZeroPrefixedData(128, 128, io, self, self._root)
            elif _on == Icns.ElementType.icon_128x128x8_mask:
                pass
                self._m_data_parsed = Icns.IconX8MaskData(128, 128, io, self, self._root)
            elif _on == Icns.ElementType.icon_16x12x1_with_mask:
                pass
                self._m_data_parsed = Icns.IconX1AndMaskData(16, 12, io, self, self._root)
            elif _on == Icns.ElementType.icon_16x12x4:
                pass
                self._m_data_parsed = Icns.IconX4Data(16, 12, io, self, self._root)
            elif _on == Icns.ElementType.icon_16x12x8:
                pass
                self._m_data_parsed = Icns.IconX8Data(16, 12, io, self, self._root)
            elif _on == Icns.ElementType.icon_16x16_argb:
                pass
                self._m_data_parsed = Icns.IconArgbData(16, 16, io, self, self._root)
            elif _on == Icns.ElementType.icon_16x16_at_2x_png_jp2:
                pass
                self._m_data_parsed = Icns.IconPngJp2Data(16, 16, 2, io, self, self._root)
            elif _on == Icns.ElementType.icon_16x16_png_jp2_rgb:
                pass
                self._m_data_parsed = Icns.IconPngJp2RgbData(16, 16, io, self, self._root)
            elif _on == Icns.ElementType.icon_16x16_rgb:
                pass
                self._m_data_parsed = Icns.IconRgbData(16, 16, io, self, self._root)
            elif _on == Icns.ElementType.icon_16x16x1_with_mask:
                pass
                self._m_data_parsed = Icns.IconX1AndMaskData(16, 16, io, self, self._root)
            elif _on == Icns.ElementType.icon_16x16x4:
                pass
                self._m_data_parsed = Icns.IconX4Data(16, 16, io, self, self._root)
            elif _on == Icns.ElementType.icon_16x16x8:
                pass
                self._m_data_parsed = Icns.IconX8Data(16, 16, io, self, self._root)
            elif _on == Icns.ElementType.icon_16x16x8_mask:
                pass
                self._m_data_parsed = Icns.IconX8MaskData(16, 16, io, self, self._root)
            elif _on == Icns.ElementType.icon_18x18_argb:
                pass
                self._m_data_parsed = Icns.IconArgbData(18, 18, io, self, self._root)
            elif _on == Icns.ElementType.icon_18x18_at_2x_png_jp2:
                pass
                self._m_data_parsed = Icns.IconPngJp2Data(18, 18, 2, io, self, self._root)
            elif _on == Icns.ElementType.icon_256x256_at_2x_png_jp2:
                pass
                self._m_data_parsed = Icns.IconPngJp2Data(256, 256, 2, io, self, self._root)
            elif _on == Icns.ElementType.icon_256x256_png_jp2:
                pass
                self._m_data_parsed = Icns.IconPngJp2Data(256, 256, 1, io, self, self._root)
            elif _on == Icns.ElementType.icon_32x32_argb:
                pass
                self._m_data_parsed = Icns.IconArgbData(32, 32, io, self, self._root)
            elif _on == Icns.ElementType.icon_32x32_at_2x_png_jp2:
                pass
                self._m_data_parsed = Icns.IconPngJp2Data(32, 32, 2, io, self, self._root)
            elif _on == Icns.ElementType.icon_32x32_png_jp2_rgb:
                pass
                self._m_data_parsed = Icns.IconPngJp2RgbData(32, 32, io, self, self._root)
            elif _on == Icns.ElementType.icon_32x32_rgb:
                pass
                self._m_data_parsed = Icns.IconRgbData(32, 32, io, self, self._root)
            elif _on == Icns.ElementType.icon_32x32x1_with_mask:
                pass
                self._m_data_parsed = Icns.IconX1AndMaskData(32, 32, io, self, self._root)
            elif _on == Icns.ElementType.icon_32x32x4:
                pass
                self._m_data_parsed = Icns.IconX4Data(32, 32, io, self, self._root)
            elif _on == Icns.ElementType.icon_32x32x8:
                pass
                self._m_data_parsed = Icns.IconX8Data(32, 32, io, self, self._root)
            elif _on == Icns.ElementType.icon_32x32x8_mask:
                pass
                self._m_data_parsed = Icns.IconX8MaskData(32, 32, io, self, self._root)
            elif _on == Icns.ElementType.icon_48x48_rgb:
                pass
                self._m_data_parsed = Icns.IconRgbData(48, 48, io, self, self._root)
            elif _on == Icns.ElementType.icon_48x48x1_with_mask:
                pass
                self._m_data_parsed = Icns.IconX1AndMaskData(48, 48, io, self, self._root)
            elif _on == Icns.ElementType.icon_48x48x4:
                pass
                self._m_data_parsed = Icns.IconX4Data(48, 48, io, self, self._root)
            elif _on == Icns.ElementType.icon_48x48x8:
                pass
                self._m_data_parsed = Icns.IconX8Data(48, 48, io, self, self._root)
            elif _on == Icns.ElementType.icon_48x48x8_mask:
                pass
                self._m_data_parsed = Icns.IconX8MaskData(48, 48, io, self, self._root)
            elif _on == Icns.ElementType.icon_512x512_at_2x_png_jp2:
                pass
                self._m_data_parsed = Icns.IconPngJp2Data(512, 512, 2, io, self, self._root)
            elif _on == Icns.ElementType.icon_512x512_png_jp2:
                pass
                self._m_data_parsed = Icns.IconPngJp2Data(512, 512, 1, io, self, self._root)
            elif _on == Icns.ElementType.icon_64x64_png_jp2:
                pass
                self._m_data_parsed = Icns.IconPngJp2Data(64, 64, 1, io, self, self._root)
            elif _on == Icns.ElementType.icon_composer_version:
                pass
                self._m_data_parsed = Icns.IconComposerVersionData(io, self, self._root)
            elif _on == Icns.ElementType.info_dictionary:
                pass
                self._m_data_parsed = Icns.InfoDictionaryData(io, self, self._root)
            elif _on == Icns.ElementType.main_family:
                pass
                self._m_data_parsed = Icns.IconFamilyData(io, self, self._root)
            elif _on == Icns.ElementType.open_drop_variant_family:
                pass
                self._m_data_parsed = Icns.IconFamilyData(io, self, self._root)
            elif _on == Icns.ElementType.open_variant_family:
                pass
                self._m_data_parsed = Icns.IconFamilyData(io, self, self._root)
            elif _on == Icns.ElementType.rollover_variant_family:
                pass
                self._m_data_parsed = Icns.IconFamilyData(io, self, self._root)
            elif _on == Icns.ElementType.sbpp_variant_family:
                pass
                self._m_data_parsed = Icns.IconFamilyData(io, self, self._root)
            elif _on == Icns.ElementType.selected_variant_family:
                pass
                self._m_data_parsed = Icns.IconFamilyData(io, self, self._root)
            elif _on == Icns.ElementType.sidebar_variant_family:
                pass
                self._m_data_parsed = Icns.IconFamilyData(io, self, self._root)
            elif _on == Icns.ElementType.table_of_contents:
                pass
                self._m_data_parsed = Icns.TableOfContentsData(io, self, self._root)
            elif _on == Icns.ElementType.tile_variant_family:
                pass
                self._m_data_parsed = Icns.IconFamilyData(io, self, self._root)
            else:
                pass
                self._m_data_parsed = bytes_with_io.BytesWithIo(io)
            self._debug['_m_data_parsed']['end'] = io.pos()
            _ = self._m_data_parsed
            if not self._io.is_eof():
                raise kaitaistruct.ValidationExprError(self._m_data_parsed, self._io, u"/types/icon_family_element/instances/data_parsed")
            io.seek(_pos)
            return getattr(self, '_m_data_parsed', None)


    class IconPngJp2Data(KaitaiStruct):
        """The data for a PNG or JPEG 2000 icon.
        Mac OS X 10.5 only supports the JPEG 2000 format here;
        Mac OS X 10.6 and later support both PNG and JPEG 2000.
        
        As of Mac OS X 10.7,
        practically all system icons use PNG instead of JPEG 2000,
        and the developer tools (Icon Composer and `iconutil`) always output PNG data.
        The JPEG 2000 format is almost never used anymore here.
        """
        SEQ_FIELDS = ["png_or_jp2_data"]
        def __init__(self, point_width, point_height, scale, _io, _parent=None, _root=None):
            super(Icns.IconPngJp2Data, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.point_width = point_width
            self.point_height = point_height
            self.scale = scale
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['png_or_jp2_data']['start'] = self._io.pos()
            self.png_or_jp2_data = self._io.read_bytes_full()
            self._debug['png_or_jp2_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.format_check
            if hasattr(self, '_m_format_check'):
                pass
                self._m_format_check._fetch_instances()


        @property
        def format_check(self):
            """Internal helper instance, do not use.
            Use the is_png and is_jp2 instances instead.
            """
            if hasattr(self, '_m_format_check'):
                return self._m_format_check

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_format_check']['start'] = self._io.pos()
            self._m_format_check = Icns.PngJp2FormatCheck(self._io, self, self._root)
            self._debug['_m_format_check']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_format_check', None)

        @property
        def is_jp2(self):
            """Whether the data appears to be in JPEG 2000 format (based on its signature)."""
            if hasattr(self, '_m_is_jp2'):
                return self._m_is_jp2

            self._m_is_jp2 = self.format_check.is_jp2
            return getattr(self, '_m_is_jp2', None)

        @property
        def is_png(self):
            """Whether the data appears to be in PNG format (based on its signature)."""
            if hasattr(self, '_m_is_png'):
                return self._m_is_png

            self._m_is_png = self.format_check.is_png
            return getattr(self, '_m_is_png', None)

        @property
        def pixel_height(self):
            """The height of the icon in pixels,
            calculated based on the height in points and the scale.
            """
            if hasattr(self, '_m_pixel_height'):
                return self._m_pixel_height

            self._m_pixel_height = self.point_height * self.scale
            return getattr(self, '_m_pixel_height', None)

        @property
        def pixel_width(self):
            """The width of the icon in pixels,
            calculated based on the width in points and the scale.
            """
            if hasattr(self, '_m_pixel_width'):
                return self._m_pixel_width

            self._m_pixel_width = self.point_width * self.scale
            return getattr(self, '_m_pixel_width', None)


    class IconPngJp2RgbData(KaitaiStruct):
        """The data for an icon in PNG, JPEG 2000, or 24-bit RGB format.
        
        This format is only used by the 'icp4' (icon_16x16_png_jp2_rgb) and 'icp5' (icon_32x32_png_jp2_rgb) icon types.
        It is identical to the format used by all other PNG/JPEG 2000 icon types (icon_png_jp2_data),
        except that if the data is neither in PNG nor in JPEG 2000 format,
        it is treated as a 24-bit RGB bitmap instead (icon_rgb_data).
        
        The latter case is only rarely used in practice -
        RGB bitmaps already have their own dedicated icon types,
        'is32' (icon_16x16_rgb) and 'il32' (icon_32x32_rgb),
        so there is normally no need to repurpose PNG/JPEG 2000 icon types to also store RGB bitmaps.
        However, the icons in some of Apple's own apps (such as the Lion versions of the iWork '09 apps) use this feature.
        """
        SEQ_FIELDS = ["format_check"]
        def __init__(self, width, height, _io, _parent=None, _root=None):
            super(Icns.IconPngJp2RgbData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.width = width
            self.height = height
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['format_check']['start'] = self._io.pos()
            self.format_check = Icns.PngJp2FormatCheck(self._io, self, self._root)
            self._debug['format_check']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.format_check._fetch_instances()
            _ = self.png_or_jp2_data
            if hasattr(self, '_m_png_or_jp2_data'):
                pass

            _ = self.rgb_data
            if hasattr(self, '_m_rgb_data'):
                pass
                self._m_rgb_data._fetch_instances()


        @property
        def is_jp2(self):
            """Whether the data appears to be in JPEG 2000 format (based on its signature)."""
            if hasattr(self, '_m_is_jp2'):
                return self._m_is_jp2

            self._m_is_jp2 = self.format_check.is_jp2
            return getattr(self, '_m_is_jp2', None)

        @property
        def is_png(self):
            """Whether the data appears to be in PNG format (based on its signature)."""
            if hasattr(self, '_m_is_png'):
                return self._m_is_png

            self._m_is_png = self.format_check.is_png
            return getattr(self, '_m_is_png', None)

        @property
        def is_rgb(self):
            """Whether the data appears to be in RGB bitmap format.
            This is assumed to be the case if the data has neither a PNG nor a JPEG 2000 signature.
            """
            if hasattr(self, '_m_is_rgb'):
                return self._m_is_rgb

            self._m_is_rgb =  (((not (self.is_png))) and ((not (self.is_jp2)))) 
            return getattr(self, '_m_is_rgb', None)

        @property
        def png_or_jp2_data(self):
            """The icon data in PNG or JPEG 2000 format."""
            if hasattr(self, '_m_png_or_jp2_data'):
                return self._m_png_or_jp2_data

            if  ((self.is_png) or (self.is_jp2)) :
                pass
                _pos = self._io.pos()
                self._io.seek(0)
                self._debug['_m_png_or_jp2_data']['start'] = self._io.pos()
                self._m_png_or_jp2_data = self._io.read_bytes_full()
                self._debug['_m_png_or_jp2_data']['end'] = self._io.pos()
                self._io.seek(_pos)

            return getattr(self, '_m_png_or_jp2_data', None)

        @property
        def rgb_data(self):
            """The icon data in RGB bitmap format."""
            if hasattr(self, '_m_rgb_data'):
                return self._m_rgb_data

            if self.is_rgb:
                pass
                _pos = self._io.pos()
                self._io.seek(0)
                self._debug['_m_rgb_data']['start'] = self._io.pos()
                self._m_rgb_data = Icns.IconRgbData(self.width, self.height, self._io, self, self._root)
                self._debug['_m_rgb_data']['end'] = self._io.pos()
                self._io.seek(_pos)

            return getattr(self, '_m_rgb_data', None)


    class IconRgbData(KaitaiStruct):
        """The data for a 24-bit RGB bitmap icon.
        These icons do not contain a mask and instead use the mask from one of the other elements in the same family
        (the 8-bit mask element if possible,
        otherwise the 1-bit mask from the 1-bit icon).
        """
        SEQ_FIELDS = ["compressed_data"]
        def __init__(self, width, height, _io, _parent=None, _root=None):
            super(Icns.IconRgbData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.width = width
            self.height = height
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['compressed_data']['start'] = self._io.pos()
            self.compressed_data = Icns.IcnsStylePackbits(self._io, self, self._root)
            self._debug['compressed_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.compressed_data._fetch_instances()


    class IconRgbZeroPrefixedData(KaitaiStruct):
        """A variant of icon_rgb_data that has four extra zero bytes preceding the compressed RGB data.
        This variant is only used by the 'it32' (icon_128x128_rgb) icon type.
        """
        SEQ_FIELDS = ["zero_prefix", "icon"]
        def __init__(self, width, height, _io, _parent=None, _root=None):
            super(Icns.IconRgbZeroPrefixedData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.width = width
            self.height = height
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['zero_prefix']['start'] = self._io.pos()
            self.zero_prefix = self._io.read_bytes(4)
            self._debug['zero_prefix']['end'] = self._io.pos()
            if not self.zero_prefix == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.zero_prefix, self._io, u"/types/icon_rgb_zero_prefixed_data/seq/0")
            self._debug['icon']['start'] = self._io.pos()
            self.icon = Icns.IconRgbData(self.width, self.height, self._io, self, self._root)
            self._debug['icon']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.icon._fetch_instances()


    class IconX1AndMaskData(KaitaiStruct):
        """The data for a 1-bit monochrome bitmap icon with a 1-bit mask."""
        SEQ_FIELDS = ["icon", "mask"]
        def __init__(self, width, height, _io, _parent=None, _root=None):
            super(Icns.IconX1AndMaskData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.width = width
            self.height = height
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['icon']['start'] = self._io.pos()
            self.icon = self._io.read_bytes((self.width * self.height) // 8)
            self._debug['icon']['end'] = self._io.pos()
            self._debug['mask']['start'] = self._io.pos()
            self.mask = self._io.read_bytes((self.width * self.height) // 8)
            self._debug['mask']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class IconX4Data(KaitaiStruct):
        """The data for a 4-bit color bitmap icon.
        These icons do not contain a mask and instead use the mask from one of the other elements in the same family
        (the 8-bit mask element if possible,
        otherwise the 1-bit mask from the 1-bit icon).
        """
        SEQ_FIELDS = ["icon"]
        def __init__(self, width, height, _io, _parent=None, _root=None):
            super(Icns.IconX4Data, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.width = width
            self.height = height
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['icon']['start'] = self._io.pos()
            self.icon = self._io.read_bytes((self.width * self.height) // 2)
            self._debug['icon']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class IconX8Data(KaitaiStruct):
        """The data for an 8-bit color bitmap icon.
        These icons do not contain a mask and instead use the mask from one of the other elements in the same family
        (the 8-bit mask element if possible,
        otherwise the 1-bit mask from the 1-bit icon).
        """
        SEQ_FIELDS = ["icon"]
        def __init__(self, width, height, _io, _parent=None, _root=None):
            super(Icns.IconX8Data, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.width = width
            self.height = height
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['icon']['start'] = self._io.pos()
            self.icon = self._io.read_bytes(self.width * self.height)
            self._debug['icon']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class IconX8MaskData(KaitaiStruct):
        """The data for an 8-bit mask,
        to be used together with one of the maskless bitmap icons of the same size in the same family.
        """
        SEQ_FIELDS = ["mask"]
        def __init__(self, width, height, _io, _parent=None, _root=None):
            super(Icns.IconX8MaskData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.width = width
            self.height = height
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['mask']['start'] = self._io.pos()
            self.mask = self._io.read_bytes(self.width * self.height)
            self._debug['mask']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class InfoDictionaryData(KaitaiStruct):
        """The element data for an info dictionary."""
        SEQ_FIELDS = ["archived_data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Icns.InfoDictionaryData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['archived_data']['start'] = self._io.pos()
            self.archived_data = self._io.read_bytes_full()
            self._debug['archived_data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PngJp2FormatCheck(KaitaiStruct):
        """Internal helper type used to check if some data appears to be in PNG or JPEG 2000 format,
        or neither of the two.
        """
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(Icns.PngJp2FormatCheck, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.jp2_signature_check
            if hasattr(self, '_m_jp2_signature_check'):
                pass

            _ = self.png_signature_check
            if hasattr(self, '_m_png_signature_check'):
                pass


        @property
        def is_jp2(self):
            """Whether the data appears to be in JPEG 2000 format (based on its signature)."""
            if hasattr(self, '_m_is_jp2'):
                return self._m_is_jp2

            self._m_is_jp2 = self.jp2_signature_check == self.jp2_signature
            return getattr(self, '_m_is_jp2', None)

        @property
        def is_png(self):
            """Whether the data appears to be in PNG format (based on its signature)."""
            if hasattr(self, '_m_is_png'):
                return self._m_is_png

            self._m_is_png = self.png_signature_check == self.png_signature
            return getattr(self, '_m_is_png', None)

        @property
        def jp2_signature(self):
            """The JPEG 2000 format's signature."""
            if hasattr(self, '_m_jp2_signature'):
                return self._m_jp2_signature

            self._m_jp2_signature = b"\x00\x00\x00\x0C\x6A\x50\x20\x20\x0D\x0A\x87\x0A"
            return getattr(self, '_m_jp2_signature', None)

        @property
        def jp2_signature_check(self):
            """Internal helper instance used to check if the data starts with the JPEG 2000 signature."""
            if hasattr(self, '_m_jp2_signature_check'):
                return self._m_jp2_signature_check

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_jp2_signature_check']['start'] = self._io.pos()
            self._m_jp2_signature_check = self._io.read_bytes(len(self.jp2_signature))
            self._debug['_m_jp2_signature_check']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_jp2_signature_check', None)

        @property
        def png_signature(self):
            """The PNG format's signature."""
            if hasattr(self, '_m_png_signature'):
                return self._m_png_signature

            self._m_png_signature = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
            return getattr(self, '_m_png_signature', None)

        @property
        def png_signature_check(self):
            """Internal helper instance used to check if the data starts with the PNG signature."""
            if hasattr(self, '_m_png_signature_check'):
                return self._m_png_signature_check

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_png_signature_check']['start'] = self._io.pos()
            self._m_png_signature_check = self._io.read_bytes(len(self.png_signature))
            self._debug['_m_png_signature_check']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_png_signature_check', None)


    class TableOfContentsData(KaitaiStruct):
        """The element data for a table of contents."""
        SEQ_FIELDS = ["element_headers"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Icns.TableOfContentsData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['element_headers']['start'] = self._io.pos()
            self._debug['element_headers']['arr'] = []
            self.element_headers = []
            i = 0
            while not self._io.is_eof():
                self._debug['element_headers']['arr'].append({'start': self._io.pos()})
                self.element_headers.append(Icns.IconFamilyElement.Header(self._io, self, self._root))
                self._debug['element_headers']['arr'][len(self.element_headers) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['element_headers']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.element_headers)):
                pass
                self.element_headers[i]._fetch_instances()




