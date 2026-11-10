# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Iso9660(KaitaiStruct):
    """ISO9660 is standard filesystem used on read-only optical discs
    (mostly CD-ROM). The standard was based on earlier High Sierra
    Format (HSF), proposed for CD-ROMs in 1985, and, after several
    revisions, it was accepted as ISO9660:1998.
    The format emphasizes portability (thus having pretty minimal
    features and very conservative file names standards) and sequential
    access (which favors disc devices with relatively slow rotation
    speed).
    
    SUSP: IEEE P1281
    RockRidge: IEEE P1282
    
    .. seealso::
       ecma-119 https://www.ecma-international.org/wp-content/uploads/ECMA-119_3rd_edition_december_2017.pdf
    
    
    .. seealso::
       susp https://web.archive.org/web/20170404132301/http://www.ymi.com/ymi/sites/default/files/pdf/Systems%20Use%20P1281.pdf
    
    
    .. seealso::
       rrip https://web.archive.org/web/20170404043745/http://www.ymi.com/ymi/sites/default/files/pdf/Rockridge.pdf
    
    
    .. seealso::
       rras http://www.estamos.de/makecd/Rock_Ridge_Amiga_Specific
    
    
    .. seealso::
       rrzf https://web.archive.org/web/20200612093441/https://dev.lovelyhq.com/libburnia/web/-/wikis/zisofs
    
    
    .. seealso::
       aaip http://fileformats.archiveteam.org/wiki/AAIP
    
    
    .. seealso::
       apple extensions http://fileformats.archiveteam.org/wiki/Apple_ISO_9660_extensions
    """

    class VolumeType(IntEnum):
        boot_record = 0
        primary = 1
        supplementary = 2
        volume_partition = 3
        set_terminator = 255
    SEQ_FIELDS = ["system_area", "data_area"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Iso9660, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['system_area']['start'] = self._io.pos()
        self.system_area = self._io.read_bytes(16 * self.sector_size)
        self._debug['system_area']['end'] = self._io.pos()
        self._debug['data_area']['start'] = self._io.pos()
        self._debug['data_area']['arr'] = []
        self._raw_data_area = []
        self.data_area = []
        i = 0
        while True:
            self._debug['data_area']['arr'].append({'start': self._io.pos()})
            _buf = self._io.read_bytes(self.sector_size)
            self._raw_data_area.append(_buf)
            _io__raw_data_area = KaitaiStream(BytesIO(self._raw_data_area[-1]))
            _ = Iso9660.VolumeDescriptor(_io__raw_data_area, self, self._root)
            self.data_area.append(_)
            self._debug['data_area']['arr'][len(self.data_area) - 1]['end'] = self._io.pos()
            if _.type == Iso9660.VolumeType.set_terminator:
                break
            i += 1
        self._debug['data_area']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.data_area)):
            pass
            self.data_area[i]._fetch_instances()


    class DatetimeLong(KaitaiStruct):
        """
        .. seealso::
           ecma-119 8.4.26.1
        """
        SEQ_FIELDS = ["year_string", "month_string", "day_string", "hour_string", "minute_string", "second_string", "hundredths_second_string", "timezone_offset"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Iso9660.DatetimeLong, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['year_string']['start'] = self._io.pos()
            self.year_string = (self._io.read_bytes(4)).decode(u"ASCII")
            self._debug['year_string']['end'] = self._io.pos()
            self._debug['month_string']['start'] = self._io.pos()
            self.month_string = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['month_string']['end'] = self._io.pos()
            self._debug['day_string']['start'] = self._io.pos()
            self.day_string = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['day_string']['end'] = self._io.pos()
            self._debug['hour_string']['start'] = self._io.pos()
            self.hour_string = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['hour_string']['end'] = self._io.pos()
            self._debug['minute_string']['start'] = self._io.pos()
            self.minute_string = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['minute_string']['end'] = self._io.pos()
            self._debug['second_string']['start'] = self._io.pos()
            self.second_string = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['second_string']['end'] = self._io.pos()
            self._debug['hundredths_second_string']['start'] = self._io.pos()
            self.hundredths_second_string = (self._io.read_bytes(2)).decode(u"ASCII")
            self._debug['hundredths_second_string']['end'] = self._io.pos()
            self._debug['timezone_offset']['start'] = self._io.pos()
            self.timezone_offset = self._io.read_s1()
            self._debug['timezone_offset']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def day(self):
            if hasattr(self, '_m_day'):
                return self._m_day

            self._m_day = int(self.day_string)
            return getattr(self, '_m_day', None)

        @property
        def hour(self):
            if hasattr(self, '_m_hour'):
                return self._m_hour

            self._m_hour = int(self.hour_string)
            return getattr(self, '_m_hour', None)

        @property
        def hundredths_second(self):
            if hasattr(self, '_m_hundredths_second'):
                return self._m_hundredths_second

            self._m_hundredths_second = int(self.hundredths_second_string)
            return getattr(self, '_m_hundredths_second', None)

        @property
        def minute(self):
            if hasattr(self, '_m_minute'):
                return self._m_minute

            self._m_minute = int(self.minute_string)
            return getattr(self, '_m_minute', None)

        @property
        def month(self):
            if hasattr(self, '_m_month'):
                return self._m_month

            self._m_month = int(self.month_string)
            return getattr(self, '_m_month', None)

        @property
        def second(self):
            if hasattr(self, '_m_second'):
                return self._m_second

            self._m_second = int(self.second_string)
            return getattr(self, '_m_second', None)

        @property
        def valid_date(self):
            if hasattr(self, '_m_valid_date'):
                return self._m_valid_date

            self._m_valid_date =  ((self.month <= 12) and (self.day <= 31) and (self.hour <= 23) and (self.minute <= 59) and (self.second <= 59)) 
            return getattr(self, '_m_valid_date', None)

        @property
        def year(self):
            if hasattr(self, '_m_year'):
                return self._m_year

            self._m_year = int(self.year_string)
            return getattr(self, '_m_year', None)


    class DatetimeLongOrEmpty(KaitaiStruct):
        """
        .. seealso::
           ecma-119 8.4.26.1
        """
        SEQ_FIELDS = ["datetime_str"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Iso9660.DatetimeLongOrEmpty, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['datetime_str']['start'] = self._io.pos()
            self.datetime_str = self._io.read_bytes(17)
            self._debug['datetime_str']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _ = self.datetime
            if hasattr(self, '_m_datetime'):
                pass
                self._m_datetime._fetch_instances()


        @property
        def datetime(self):
            if hasattr(self, '_m_datetime'):
                return self._m_datetime

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_datetime']['start'] = self._io.pos()
            self._m_datetime = Iso9660.DatetimeLong(self._io, self, self._root)
            self._debug['_m_datetime']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_datetime', None)

        @property
        def is_empty(self):
            if hasattr(self, '_m_is_empty'):
                return self._m_is_empty

            self._m_is_empty = self.datetime_str == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            return getattr(self, '_m_is_empty', None)


    class DatetimeShort(KaitaiStruct):
        """
        .. seealso::
           ecma-119 9.1.5
        """
        SEQ_FIELDS = ["year", "month", "day", "hour", "min", "sec", "offset"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Iso9660.DatetimeShort, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['year']['start'] = self._io.pos()
            self.year = self._io.read_u1()
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
            self._debug['min']['start'] = self._io.pos()
            self.min = self._io.read_u1()
            self._debug['min']['end'] = self._io.pos()
            self._debug['sec']['start'] = self._io.pos()
            self.sec = self._io.read_u1()
            self._debug['sec']['end'] = self._io.pos()
            self._debug['offset']['start'] = self._io.pos()
            self.offset = self._io.read_s1()
            self._debug['offset']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class U2bi(KaitaiStruct):
        """
        .. seealso::
           ecma-119 7.2.3
        """
        SEQ_FIELDS = ["le", "be"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Iso9660.U2bi, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['le']['start'] = self._io.pos()
            self.le = self._io.read_u2le()
            self._debug['le']['end'] = self._io.pos()
            self._debug['be']['start'] = self._io.pos()
            self.be = self._io.read_u2be()
            self._debug['be']['end'] = self._io.pos()
            if not self.be == self.le:
                raise kaitaistruct.ValidationNotEqualError(self.le, self.be, self._io, u"/types/u2bi/seq/1")


        def _fetch_instances(self):
            pass

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.le
            return getattr(self, '_m_value', None)


    class U4bi(KaitaiStruct):
        """
        .. seealso::
           ecma-119 7.3.3
        """
        SEQ_FIELDS = ["le", "be"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Iso9660.U4bi, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['le']['start'] = self._io.pos()
            self.le = self._io.read_u4le()
            self._debug['le']['end'] = self._io.pos()
            self._debug['be']['start'] = self._io.pos()
            self.be = self._io.read_u4be()
            self._debug['be']['end'] = self._io.pos()
            if not self.be == self.le:
                raise kaitaistruct.ValidationNotEqualError(self.le, self.be, self._io, u"/types/u4bi/seq/1")


        def _fetch_instances(self):
            pass

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.le
            return getattr(self, '_m_value', None)


    class VolumeDescriptor(KaitaiStruct):
        """
        .. seealso::
           ecma-119 8.1
        """
        SEQ_FIELDS = ["type", "magic", "version", "volume"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Iso9660.VolumeDescriptor, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Iso9660.VolumeType, self._io.read_u1())
            self._debug['type']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(5)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x43\x44\x30\x30\x31":
                raise kaitaistruct.ValidationNotEqualError(b"\x43\x44\x30\x30\x31", self.magic, self._io, u"/types/volume_descriptor/seq/1")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u1()
            self._debug['version']['end'] = self._io.pos()
            if not  ((self.version == 1) or (self.version == 2)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/types/volume_descriptor/seq/2")
            self._debug['volume']['start'] = self._io.pos()
            _on = self.type
            if _on == Iso9660.VolumeType.boot_record:
                pass
                self.volume = Iso9660.VolumeDescriptor.BootRecord(self._io, self, self._root)
            elif _on == Iso9660.VolumeType.primary:
                pass
                self.volume = Iso9660.VolumeDescriptor.Primary(self._io, self, self._root)
            elif _on == Iso9660.VolumeType.supplementary:
                pass
                self.volume = Iso9660.VolumeDescriptor.Supplementary(self._io, self, self._root)
            self._debug['volume']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.type
            if _on == Iso9660.VolumeType.boot_record:
                pass
                self.volume._fetch_instances()
            elif _on == Iso9660.VolumeType.primary:
                pass
                self.volume._fetch_instances()
            elif _on == Iso9660.VolumeType.supplementary:
                pass
                self.volume._fetch_instances()

        class BootRecord(KaitaiStruct):
            """
            .. seealso::
               ecma-119 8.2
            """
            SEQ_FIELDS = ["boot_system_identifier", "boot_identifier"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Iso9660.VolumeDescriptor.BootRecord, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['boot_system_identifier']['start'] = self._io.pos()
                self.boot_system_identifier = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ASCII")
                self._debug['boot_system_identifier']['end'] = self._io.pos()
                self._debug['boot_identifier']['start'] = self._io.pos()
                self.boot_identifier = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"ASCII")
                self._debug['boot_identifier']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class DirectoryRecord(KaitaiStruct):
            """
            .. seealso::
               ecma-119 9.1
            """
            SEQ_FIELDS = ["len_dr", "body"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Iso9660.VolumeDescriptor.DirectoryRecord, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['len_dr']['start'] = self._io.pos()
                self.len_dr = self._io.read_u1()
                self._debug['len_dr']['end'] = self._io.pos()
                if self.len_dr > 0:
                    pass
                    self._debug['body']['start'] = self._io.pos()
                    self._raw_body = self._io.read_bytes(self.len_dr - 1)
                    _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                    self.body = Iso9660.VolumeDescriptor.DirectoryRecord.Body(_io__raw_body, self, self._root)
                    self._debug['body']['end'] = self._io.pos()



            def _fetch_instances(self):
                pass
                if self.len_dr > 0:
                    pass
                    self.body._fetch_instances()


            class Body(KaitaiStruct):
                SEQ_FIELDS = ["ext_attr_rec_len", "extent", "data_len", "rec_date_time", "file_flags_multi_extent", "file_flags_reserved", "file_flags_protection", "file_flags_record", "file_flags_associated_file", "file_flags_directory", "file_flags_existence", "file_unit_size", "interleave_gap_size", "vol_seq_num", "len_fi", "file_id", "padding_field", "system_use"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Iso9660.VolumeDescriptor.DirectoryRecord.Body, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['ext_attr_rec_len']['start'] = self._io.pos()
                    self.ext_attr_rec_len = self._io.read_u1()
                    self._debug['ext_attr_rec_len']['end'] = self._io.pos()
                    self._debug['extent']['start'] = self._io.pos()
                    self.extent = Iso9660.U4bi(self._io, self, self._root)
                    self._debug['extent']['end'] = self._io.pos()
                    self._debug['data_len']['start'] = self._io.pos()
                    self.data_len = Iso9660.U4bi(self._io, self, self._root)
                    self._debug['data_len']['end'] = self._io.pos()
                    self._debug['rec_date_time']['start'] = self._io.pos()
                    self.rec_date_time = Iso9660.DatetimeShort(self._io, self, self._root)
                    self._debug['rec_date_time']['end'] = self._io.pos()
                    self._debug['file_flags_multi_extent']['start'] = self._io.pos()
                    self.file_flags_multi_extent = self._io.read_bits_int_be(1) != 0
                    self._debug['file_flags_multi_extent']['end'] = self._io.pos()
                    self._debug['file_flags_reserved']['start'] = self._io.pos()
                    self.file_flags_reserved = self._io.read_bits_int_be(2)
                    self._debug['file_flags_reserved']['end'] = self._io.pos()
                    self._debug['file_flags_protection']['start'] = self._io.pos()
                    self.file_flags_protection = self._io.read_bits_int_be(1) != 0
                    self._debug['file_flags_protection']['end'] = self._io.pos()
                    self._debug['file_flags_record']['start'] = self._io.pos()
                    self.file_flags_record = self._io.read_bits_int_be(1) != 0
                    self._debug['file_flags_record']['end'] = self._io.pos()
                    self._debug['file_flags_associated_file']['start'] = self._io.pos()
                    self.file_flags_associated_file = self._io.read_bits_int_be(1) != 0
                    self._debug['file_flags_associated_file']['end'] = self._io.pos()
                    self._debug['file_flags_directory']['start'] = self._io.pos()
                    self.file_flags_directory = self._io.read_bits_int_be(1) != 0
                    self._debug['file_flags_directory']['end'] = self._io.pos()
                    self._debug['file_flags_existence']['start'] = self._io.pos()
                    self.file_flags_existence = self._io.read_bits_int_be(1) != 0
                    self._debug['file_flags_existence']['end'] = self._io.pos()
                    self._debug['file_unit_size']['start'] = self._io.pos()
                    self.file_unit_size = self._io.read_u1()
                    self._debug['file_unit_size']['end'] = self._io.pos()
                    self._debug['interleave_gap_size']['start'] = self._io.pos()
                    self.interleave_gap_size = self._io.read_u1()
                    self._debug['interleave_gap_size']['end'] = self._io.pos()
                    self._debug['vol_seq_num']['start'] = self._io.pos()
                    self.vol_seq_num = Iso9660.U2bi(self._io, self, self._root)
                    self._debug['vol_seq_num']['end'] = self._io.pos()
                    self._debug['len_fi']['start'] = self._io.pos()
                    self.len_fi = self._io.read_u1()
                    self._debug['len_fi']['end'] = self._io.pos()
                    self._debug['file_id']['start'] = self._io.pos()
                    self.file_id = (self._io.read_bytes(self.len_fi)).decode(u"ASCII")
                    self._debug['file_id']['end'] = self._io.pos()
                    if self.len_fi % 2 == 0:
                        pass
                        self._debug['padding_field']['start'] = self._io.pos()
                        self.padding_field = self._io.read_bytes(1)
                        self._debug['padding_field']['end'] = self._io.pos()
                        if not self.padding_field == b"\x00":
                            raise kaitaistruct.ValidationNotEqualError(b"\x00", self.padding_field, self._io, u"/types/volume_descriptor/types/directory_record/types/body/seq/16")

                    self._debug['system_use']['start'] = self._io.pos()
                    self._raw_system_use = self._io.read_bytes_full()
                    _io__raw_system_use = KaitaiStream(BytesIO(self._raw_system_use))
                    self.system_use = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp(_io__raw_system_use, self, self._root)
                    self._debug['system_use']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    self.extent._fetch_instances()
                    self.data_len._fetch_instances()
                    self.rec_date_time._fetch_instances()
                    self.vol_seq_num._fetch_instances()
                    if self.len_fi % 2 == 0:
                        pass

                    self.system_use._fetch_instances()
                    _ = self.directory_records
                    if hasattr(self, '_m_directory_records'):
                        pass
                        self._m_directory_records._fetch_instances()

                    _ = self.file_content
                    if hasattr(self, '_m_file_content'):
                        pass


                class Susp(KaitaiStruct):
                    """We check if we have at least 4 bytes left.
                    The SUSP magic is 2 bytes. A complete SUSP entry
                    is at least 4 bytes long.
                    """
                    SEQ_FIELDS = ["entries"]
                    def __init__(self, _io, _parent=None, _root=None):
                        super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp, self).__init__(_io)
                        self._parent = _parent
                        self._root = _root
                        self._debug = collections.defaultdict(dict)
                        self._read()

                    def _read(self):
                        if self._io.size() - self._io.pos() >= 4:
                            pass
                            self._debug['entries']['start'] = self._io.pos()
                            self._debug['entries']['arr'] = []
                            self.entries = []
                            i = 0
                            while True:
                                self._debug['entries']['arr'].append({'start': self._io.pos()})
                                _ = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header(self._io, self, self._root)
                                self.entries.append(_)
                                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                                if self._io.size() - self._io.pos() < 4:
                                    break
                                i += 1
                            self._debug['entries']['end'] = self._io.pos()



                    def _fetch_instances(self):
                        pass
                        if self._io.size() - self._io.pos() >= 4:
                            pass
                            for i in range(len(self.entries)):
                                pass
                                self.entries[i]._fetch_instances()



                    class Header(KaitaiStruct):

                        class Signature(IntEnum):
                            apple_attribute_list = 16705
                            aaip_attribute_list = 16716
                            rras_amiga_specific = 16723
                            susp_continuation_area = 17221
                            rrip_child_link = 17228
                            susp_extensions_reference = 17746
                            susp_extension_selector = 17747
                            rrip_alternate_name = 20045
                            susp_padding_field = 20548
                            rrip_parent_link = 20556
                            rrip_posix_device_number = 20558
                            rrip_posix_file_attributes = 20568
                            rrip_relocated_directory = 21061
                            rrip_extensions_in_use_indicator = 21074
                            rrip_sparse_file = 21318
                            rrip_symbolic_link = 21324
                            susp_indicator = 21328
                            susp_terminator = 21332
                            rrip_time_file = 21574
                            rrzf_zisofs = 23110
                        SEQ_FIELDS = ["signature", "length", "version", "susp_data"]
                        def __init__(self, _io, _parent=None, _root=None):
                            super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header, self).__init__(_io)
                            self._parent = _parent
                            self._root = _root
                            self._debug = collections.defaultdict(dict)
                            self._read()

                        def _read(self):
                            self._debug['signature']['start'] = self._io.pos()
                            self.signature = KaitaiStream.resolve_enum(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature, self._io.read_u2be())
                            self._debug['signature']['end'] = self._io.pos()
                            self._debug['length']['start'] = self._io.pos()
                            self.length = self._io.read_u1()
                            self._debug['length']['end'] = self._io.pos()
                            self._debug['version']['start'] = self._io.pos()
                            self.version = self._io.read_u1()
                            self._debug['version']['end'] = self._io.pos()
                            self._debug['susp_data']['start'] = self._io.pos()
                            _on = self.signature
                            if _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.aaip_attribute_list:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspUnknown(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.apple_attribute_list:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspUnknown(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rras_amiga_specific:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RrasAs(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_alternate_name:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripNm(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_child_link:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripCl(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_extensions_in_use_indicator:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspUnknown(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_parent_link:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripPl(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_posix_device_number:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripPn(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_posix_file_attributes:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripPx(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_relocated_directory:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripRe(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_sparse_file:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripSf(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_symbolic_link:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspSl(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_time_file:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripTf(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrzf_zisofs:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RrzfZf(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_continuation_area:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspCe(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_extension_selector:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspEs(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_extensions_reference:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspEr(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_indicator:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspSp(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_padding_field:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspPd(_io__raw_susp_data, self, self._root)
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_terminator:
                                pass
                                self._raw_susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                                _io__raw_susp_data = KaitaiStream(BytesIO(self._raw_susp_data))
                                self.susp_data = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspSt(_io__raw_susp_data, self, self._root)
                            else:
                                pass
                                self.susp_data = self._io.read_bytes(self.length - ((2 + 1) + 1))
                            self._debug['susp_data']['end'] = self._io.pos()


                        def _fetch_instances(self):
                            pass
                            _on = self.signature
                            if _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.aaip_attribute_list:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.apple_attribute_list:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rras_amiga_specific:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_alternate_name:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_child_link:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_extensions_in_use_indicator:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_parent_link:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_posix_device_number:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_posix_file_attributes:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_relocated_directory:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_sparse_file:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_symbolic_link:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrip_time_file:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.rrzf_zisofs:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_continuation_area:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_extension_selector:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_extensions_reference:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_indicator:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_padding_field:
                                pass
                                self.susp_data._fetch_instances()
                            elif _on == Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.Signature.susp_terminator:
                                pass
                                self.susp_data._fetch_instances()
                            else:
                                pass

                        class RrasAs(KaitaiStruct):
                            """
                            .. seealso::
                               rras
                            """
                            SEQ_FIELDS = ["reserved", "flag_continue", "flag_comment", "flag_protection", "flags", "len_comment", "comment"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RrasAs, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['reserved']['start'] = self._io.pos()
                                self.reserved = self._io.read_bits_int_be(5)
                                self._debug['reserved']['end'] = self._io.pos()
                                self._debug['flag_continue']['start'] = self._io.pos()
                                self.flag_continue = self._io.read_bits_int_be(1) != 0
                                self._debug['flag_continue']['end'] = self._io.pos()
                                self._debug['flag_comment']['start'] = self._io.pos()
                                self.flag_comment = self._io.read_bits_int_be(1) != 0
                                self._debug['flag_comment']['end'] = self._io.pos()
                                self._debug['flag_protection']['start'] = self._io.pos()
                                self.flag_protection = self._io.read_bits_int_be(1) != 0
                                self._debug['flag_protection']['end'] = self._io.pos()
                                if self.flag_protection:
                                    pass
                                    self._debug['flags']['start'] = self._io.pos()
                                    self.flags = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RrasAs.Flags(self._io, self, self._root)
                                    self._debug['flags']['end'] = self._io.pos()

                                if  ((self.flag_comment) or (self.flag_continue)) :
                                    pass
                                    self._debug['len_comment']['start'] = self._io.pos()
                                    self.len_comment = self._io.read_u1()
                                    self._debug['len_comment']['end'] = self._io.pos()

                                if  ((self.flag_comment) or (self.flag_continue)) :
                                    pass
                                    self._debug['comment']['start'] = self._io.pos()
                                    self.comment = (self._io.read_bytes_full()).decode(u"ASCII")
                                    self._debug['comment']['end'] = self._io.pos()



                            def _fetch_instances(self):
                                pass
                                if self.flag_protection:
                                    pass
                                    self.flags._fetch_instances()

                                if  ((self.flag_comment) or (self.flag_continue)) :
                                    pass

                                if  ((self.flag_comment) or (self.flag_continue)) :
                                    pass


                            class Flags(KaitaiStruct):
                                """
                                .. seealso::
                                   rras 6
                                """
                                SEQ_FIELDS = ["user_bitfields", "reserved_bitfields", "other_read", "other_write", "other_exec", "other_del", "group_read", "group_write", "group_exec", "group_del", "reserved", "exec_script", "reent_exec", "archived", "owner_read", "owner_write", "owner_exec", "owner_del"]
                                def __init__(self, _io, _parent=None, _root=None):
                                    super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RrasAs.Flags, self).__init__(_io)
                                    self._parent = _parent
                                    self._root = _root
                                    self._debug = collections.defaultdict(dict)
                                    self._read()

                                def _read(self):
                                    self._debug['user_bitfields']['start'] = self._io.pos()
                                    self.user_bitfields = self._io.read_u1()
                                    self._debug['user_bitfields']['end'] = self._io.pos()
                                    self._debug['reserved_bitfields']['start'] = self._io.pos()
                                    self.reserved_bitfields = self._io.read_u1()
                                    self._debug['reserved_bitfields']['end'] = self._io.pos()
                                    self._debug['other_read']['start'] = self._io.pos()
                                    self.other_read = self._io.read_bits_int_be(1) != 0
                                    self._debug['other_read']['end'] = self._io.pos()
                                    self._debug['other_write']['start'] = self._io.pos()
                                    self.other_write = self._io.read_bits_int_be(1) != 0
                                    self._debug['other_write']['end'] = self._io.pos()
                                    self._debug['other_exec']['start'] = self._io.pos()
                                    self.other_exec = self._io.read_bits_int_be(1) != 0
                                    self._debug['other_exec']['end'] = self._io.pos()
                                    self._debug['other_del']['start'] = self._io.pos()
                                    self.other_del = self._io.read_bits_int_be(1) != 0
                                    self._debug['other_del']['end'] = self._io.pos()
                                    self._debug['group_read']['start'] = self._io.pos()
                                    self.group_read = self._io.read_bits_int_be(1) != 0
                                    self._debug['group_read']['end'] = self._io.pos()
                                    self._debug['group_write']['start'] = self._io.pos()
                                    self.group_write = self._io.read_bits_int_be(1) != 0
                                    self._debug['group_write']['end'] = self._io.pos()
                                    self._debug['group_exec']['start'] = self._io.pos()
                                    self.group_exec = self._io.read_bits_int_be(1) != 0
                                    self._debug['group_exec']['end'] = self._io.pos()
                                    self._debug['group_del']['start'] = self._io.pos()
                                    self.group_del = self._io.read_bits_int_be(1) != 0
                                    self._debug['group_del']['end'] = self._io.pos()
                                    self._debug['reserved']['start'] = self._io.pos()
                                    self.reserved = self._io.read_bits_int_be(1) != 0
                                    self._debug['reserved']['end'] = self._io.pos()
                                    self._debug['exec_script']['start'] = self._io.pos()
                                    self.exec_script = self._io.read_bits_int_be(1) != 0
                                    self._debug['exec_script']['end'] = self._io.pos()
                                    self._debug['reent_exec']['start'] = self._io.pos()
                                    self.reent_exec = self._io.read_bits_int_be(1) != 0
                                    self._debug['reent_exec']['end'] = self._io.pos()
                                    self._debug['archived']['start'] = self._io.pos()
                                    self.archived = self._io.read_bits_int_be(1) != 0
                                    self._debug['archived']['end'] = self._io.pos()
                                    self._debug['owner_read']['start'] = self._io.pos()
                                    self.owner_read = self._io.read_bits_int_be(1) != 0
                                    self._debug['owner_read']['end'] = self._io.pos()
                                    self._debug['owner_write']['start'] = self._io.pos()
                                    self.owner_write = self._io.read_bits_int_be(1) != 0
                                    self._debug['owner_write']['end'] = self._io.pos()
                                    self._debug['owner_exec']['start'] = self._io.pos()
                                    self.owner_exec = self._io.read_bits_int_be(1) != 0
                                    self._debug['owner_exec']['end'] = self._io.pos()
                                    self._debug['owner_del']['start'] = self._io.pos()
                                    self.owner_del = self._io.read_bits_int_be(1) != 0
                                    self._debug['owner_del']['end'] = self._io.pos()


                                def _fetch_instances(self):
                                    pass



                        class RripCl(KaitaiStruct):
                            """
                            .. seealso::
                               rrip 4.1.5.1
                            """
                            SEQ_FIELDS = ["lba_child"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripCl, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['lba_child']['start'] = self._io.pos()
                                self.lba_child = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['lba_child']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass
                                self.lba_child._fetch_instances()


                        class RripNm(KaitaiStruct):
                            """
                            .. seealso::
                               rrip 4.1.4
                            """
                            SEQ_FIELDS = ["reserved", "parent", "current", "continued", "name"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripNm, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['reserved']['start'] = self._io.pos()
                                self.reserved = self._io.read_bits_int_be(5)
                                self._debug['reserved']['end'] = self._io.pos()
                                self._debug['parent']['start'] = self._io.pos()
                                self.parent = self._io.read_bits_int_be(1) != 0
                                self._debug['parent']['end'] = self._io.pos()
                                self._debug['current']['start'] = self._io.pos()
                                self.current = self._io.read_bits_int_be(1) != 0
                                self._debug['current']['end'] = self._io.pos()
                                self._debug['continued']['start'] = self._io.pos()
                                self.continued = self._io.read_bits_int_be(1) != 0
                                self._debug['continued']['end'] = self._io.pos()
                                self._debug['name']['start'] = self._io.pos()
                                self.name = (self._io.read_bytes_full()).decode(u"ASCII")
                                self._debug['name']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass


                        class RripPl(KaitaiStruct):
                            """
                            .. seealso::
                               rrip 4.1.5.2
                            """
                            SEQ_FIELDS = ["lba_parent"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripPl, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['lba_parent']['start'] = self._io.pos()
                                self.lba_parent = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['lba_parent']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass
                                self.lba_parent._fetch_instances()


                        class RripPn(KaitaiStruct):
                            """
                            .. seealso::
                               rrip 4.1.2
                            """
                            SEQ_FIELDS = ["dev_t_high", "dev_t_low"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripPn, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['dev_t_high']['start'] = self._io.pos()
                                self.dev_t_high = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['dev_t_high']['end'] = self._io.pos()
                                self._debug['dev_t_low']['start'] = self._io.pos()
                                self.dev_t_low = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['dev_t_low']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass
                                self.dev_t_high._fetch_instances()
                                self.dev_t_low._fetch_instances()


                        class RripPx(KaitaiStruct):
                            """
                            .. seealso::
                               rrip 4.1.1
                            """
                            SEQ_FIELDS = ["file_mode", "links", "user", "group", "serial"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripPx, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['file_mode']['start'] = self._io.pos()
                                self.file_mode = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['file_mode']['end'] = self._io.pos()
                                self._debug['links']['start'] = self._io.pos()
                                self.links = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['links']['end'] = self._io.pos()
                                self._debug['user']['start'] = self._io.pos()
                                self.user = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['user']['end'] = self._io.pos()
                                self._debug['group']['start'] = self._io.pos()
                                self.group = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['group']['end'] = self._io.pos()
                                if self._parent.length >= 44:
                                    pass
                                    self._debug['serial']['start'] = self._io.pos()
                                    self.serial = Iso9660.U4bi(self._io, self, self._root)
                                    self._debug['serial']['end'] = self._io.pos()



                            def _fetch_instances(self):
                                pass
                                self.file_mode._fetch_instances()
                                self.links._fetch_instances()
                                self.user._fetch_instances()
                                self.group._fetch_instances()
                                if self._parent.length >= 44:
                                    pass
                                    self.serial._fetch_instances()



                        class RripRe(KaitaiStruct):
                            SEQ_FIELDS = []
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripRe, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                pass


                            def _fetch_instances(self):
                                pass


                        class RripSf(KaitaiStruct):
                            """
                            .. seealso::
                               rrip 4.1.7
                            """

                            class TableDepth(IntEnum):
                                max_64kb = 2
                                max_64mb = 4
                                max_4gb = 8
                                max_1tb = 16
                                max_256tb = 32
                                max_64pb = 64
                                max_16eb = 128
                            SEQ_FIELDS = ["virtual_file_size_high", "virtual_file_size_low", "table_depth"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripSf, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['virtual_file_size_high']['start'] = self._io.pos()
                                self.virtual_file_size_high = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['virtual_file_size_high']['end'] = self._io.pos()
                                self._debug['virtual_file_size_low']['start'] = self._io.pos()
                                self.virtual_file_size_low = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['virtual_file_size_low']['end'] = self._io.pos()
                                self._debug['table_depth']['start'] = self._io.pos()
                                self.table_depth = KaitaiStream.resolve_enum(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripSf.TableDepth, self._io.read_u1())
                                self._debug['table_depth']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass
                                self.virtual_file_size_high._fetch_instances()
                                self.virtual_file_size_low._fetch_instances()


                        class RripTf(KaitaiStruct):
                            """
                            .. seealso::
                               rrip 4.6.1
                            """
                            SEQ_FIELDS = ["long_form", "effective", "expiration", "backup", "attributes", "access", "modify", "creation", "datetime_short", "datetime_long"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripTf, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['long_form']['start'] = self._io.pos()
                                self.long_form = self._io.read_bits_int_be(1) != 0
                                self._debug['long_form']['end'] = self._io.pos()
                                self._debug['effective']['start'] = self._io.pos()
                                self.effective = self._io.read_bits_int_be(1) != 0
                                self._debug['effective']['end'] = self._io.pos()
                                self._debug['expiration']['start'] = self._io.pos()
                                self.expiration = self._io.read_bits_int_be(1) != 0
                                self._debug['expiration']['end'] = self._io.pos()
                                self._debug['backup']['start'] = self._io.pos()
                                self.backup = self._io.read_bits_int_be(1) != 0
                                self._debug['backup']['end'] = self._io.pos()
                                self._debug['attributes']['start'] = self._io.pos()
                                self.attributes = self._io.read_bits_int_be(1) != 0
                                self._debug['attributes']['end'] = self._io.pos()
                                self._debug['access']['start'] = self._io.pos()
                                self.access = self._io.read_bits_int_be(1) != 0
                                self._debug['access']['end'] = self._io.pos()
                                self._debug['modify']['start'] = self._io.pos()
                                self.modify = self._io.read_bits_int_be(1) != 0
                                self._debug['modify']['end'] = self._io.pos()
                                self._debug['creation']['start'] = self._io.pos()
                                self.creation = self._io.read_bits_int_be(1) != 0
                                self._debug['creation']['end'] = self._io.pos()
                                if (not (self.long_form)):
                                    pass
                                    self._debug['datetime_short']['start'] = self._io.pos()
                                    self.datetime_short = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripTf.Short(self._io, self, self._root)
                                    self._debug['datetime_short']['end'] = self._io.pos()

                                if self.long_form:
                                    pass
                                    self._debug['datetime_long']['start'] = self._io.pos()
                                    self.datetime_long = Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripTf.Long(self._io, self, self._root)
                                    self._debug['datetime_long']['end'] = self._io.pos()



                            def _fetch_instances(self):
                                pass
                                if (not (self.long_form)):
                                    pass
                                    self.datetime_short._fetch_instances()

                                if self.long_form:
                                    pass
                                    self.datetime_long._fetch_instances()


                            class Long(KaitaiStruct):
                                """The data is available in this specific order.
                                Multiple dates can be set.
                                
                                .. seealso::
                                   rrip 4.6.1
                                """
                                SEQ_FIELDS = ["creation", "modify", "access", "attributes", "backup", "expiration", "effective"]
                                def __init__(self, _io, _parent=None, _root=None):
                                    super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripTf.Long, self).__init__(_io)
                                    self._parent = _parent
                                    self._root = _root
                                    self._debug = collections.defaultdict(dict)
                                    self._read()

                                def _read(self):
                                    if self._parent.creation:
                                        pass
                                        self._debug['creation']['start'] = self._io.pos()
                                        self.creation = Iso9660.DatetimeLongOrEmpty(self._io, self, self._root)
                                        self._debug['creation']['end'] = self._io.pos()

                                    if self._parent.modify:
                                        pass
                                        self._debug['modify']['start'] = self._io.pos()
                                        self.modify = Iso9660.DatetimeLongOrEmpty(self._io, self, self._root)
                                        self._debug['modify']['end'] = self._io.pos()

                                    if self._parent.access:
                                        pass
                                        self._debug['access']['start'] = self._io.pos()
                                        self.access = Iso9660.DatetimeLongOrEmpty(self._io, self, self._root)
                                        self._debug['access']['end'] = self._io.pos()

                                    if self._parent.attributes:
                                        pass
                                        self._debug['attributes']['start'] = self._io.pos()
                                        self.attributes = Iso9660.DatetimeLongOrEmpty(self._io, self, self._root)
                                        self._debug['attributes']['end'] = self._io.pos()

                                    if self._parent.backup:
                                        pass
                                        self._debug['backup']['start'] = self._io.pos()
                                        self.backup = Iso9660.DatetimeLongOrEmpty(self._io, self, self._root)
                                        self._debug['backup']['end'] = self._io.pos()

                                    if self._parent.expiration:
                                        pass
                                        self._debug['expiration']['start'] = self._io.pos()
                                        self.expiration = Iso9660.DatetimeLongOrEmpty(self._io, self, self._root)
                                        self._debug['expiration']['end'] = self._io.pos()

                                    if self._parent.effective:
                                        pass
                                        self._debug['effective']['start'] = self._io.pos()
                                        self.effective = Iso9660.DatetimeLongOrEmpty(self._io, self, self._root)
                                        self._debug['effective']['end'] = self._io.pos()



                                def _fetch_instances(self):
                                    pass
                                    if self._parent.creation:
                                        pass
                                        self.creation._fetch_instances()

                                    if self._parent.modify:
                                        pass
                                        self.modify._fetch_instances()

                                    if self._parent.access:
                                        pass
                                        self.access._fetch_instances()

                                    if self._parent.attributes:
                                        pass
                                        self.attributes._fetch_instances()

                                    if self._parent.backup:
                                        pass
                                        self.backup._fetch_instances()

                                    if self._parent.expiration:
                                        pass
                                        self.expiration._fetch_instances()

                                    if self._parent.effective:
                                        pass
                                        self.effective._fetch_instances()



                            class Short(KaitaiStruct):
                                """The data is available in this specific order.
                                Multiple dates can be set.
                                
                                .. seealso::
                                   rrip 4.6.1
                                """
                                SEQ_FIELDS = ["creation", "modify", "access", "attributes", "backup", "expiration", "effective"]
                                def __init__(self, _io, _parent=None, _root=None):
                                    super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RripTf.Short, self).__init__(_io)
                                    self._parent = _parent
                                    self._root = _root
                                    self._debug = collections.defaultdict(dict)
                                    self._read()

                                def _read(self):
                                    if self._parent.creation:
                                        pass
                                        self._debug['creation']['start'] = self._io.pos()
                                        self.creation = Iso9660.DatetimeShort(self._io, self, self._root)
                                        self._debug['creation']['end'] = self._io.pos()

                                    if self._parent.modify:
                                        pass
                                        self._debug['modify']['start'] = self._io.pos()
                                        self.modify = Iso9660.DatetimeShort(self._io, self, self._root)
                                        self._debug['modify']['end'] = self._io.pos()

                                    if self._parent.access:
                                        pass
                                        self._debug['access']['start'] = self._io.pos()
                                        self.access = Iso9660.DatetimeShort(self._io, self, self._root)
                                        self._debug['access']['end'] = self._io.pos()

                                    if self._parent.attributes:
                                        pass
                                        self._debug['attributes']['start'] = self._io.pos()
                                        self.attributes = Iso9660.DatetimeShort(self._io, self, self._root)
                                        self._debug['attributes']['end'] = self._io.pos()

                                    if self._parent.backup:
                                        pass
                                        self._debug['backup']['start'] = self._io.pos()
                                        self.backup = Iso9660.DatetimeShort(self._io, self, self._root)
                                        self._debug['backup']['end'] = self._io.pos()

                                    if self._parent.expiration:
                                        pass
                                        self._debug['expiration']['start'] = self._io.pos()
                                        self.expiration = Iso9660.DatetimeShort(self._io, self, self._root)
                                        self._debug['expiration']['end'] = self._io.pos()

                                    if self._parent.effective:
                                        pass
                                        self._debug['effective']['start'] = self._io.pos()
                                        self.effective = Iso9660.DatetimeShort(self._io, self, self._root)
                                        self._debug['effective']['end'] = self._io.pos()



                                def _fetch_instances(self):
                                    pass
                                    if self._parent.creation:
                                        pass
                                        self.creation._fetch_instances()

                                    if self._parent.modify:
                                        pass
                                        self.modify._fetch_instances()

                                    if self._parent.access:
                                        pass
                                        self.access._fetch_instances()

                                    if self._parent.attributes:
                                        pass
                                        self.attributes._fetch_instances()

                                    if self._parent.backup:
                                        pass
                                        self.backup._fetch_instances()

                                    if self._parent.expiration:
                                        pass
                                        self.expiration._fetch_instances()

                                    if self._parent.effective:
                                        pass
                                        self.effective._fetch_instances()




                        class RrzfZf(KaitaiStruct):
                            """
                            .. seealso::
                               rrzf
                            """

                            class Algorithm(IntEnum):
                                paged_zlib = 28794

                            class BlockSize(IntEnum):
                                bs_32kib = 15
                                bs_64kib = 16
                                bs_128kib = 17
                            SEQ_FIELDS = ["algorithm", "header_size", "block_size", "uncompressed_size"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RrzfZf, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['algorithm']['start'] = self._io.pos()
                                self.algorithm = KaitaiStream.resolve_enum(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RrzfZf.Algorithm, self._io.read_u2be())
                                self._debug['algorithm']['end'] = self._io.pos()
                                self._debug['header_size']['start'] = self._io.pos()
                                self.header_size = self._io.read_u1()
                                self._debug['header_size']['end'] = self._io.pos()
                                self._debug['block_size']['start'] = self._io.pos()
                                self.block_size = KaitaiStream.resolve_enum(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.RrzfZf.BlockSize, self._io.read_u1())
                                self._debug['block_size']['end'] = self._io.pos()
                                self._debug['uncompressed_size']['start'] = self._io.pos()
                                self.uncompressed_size = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['uncompressed_size']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass
                                self.uncompressed_size._fetch_instances()


                        class SuspCe(KaitaiStruct):
                            """
                            .. seealso::
                               susp 5.1
                            """
                            SEQ_FIELDS = ["ca_location", "ca_offset", "ca_length"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspCe, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['ca_location']['start'] = self._io.pos()
                                self.ca_location = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['ca_location']['end'] = self._io.pos()
                                self._debug['ca_offset']['start'] = self._io.pos()
                                self.ca_offset = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['ca_offset']['end'] = self._io.pos()
                                self._debug['ca_length']['start'] = self._io.pos()
                                self.ca_length = Iso9660.U4bi(self._io, self, self._root)
                                self._debug['ca_length']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass
                                self.ca_location._fetch_instances()
                                self.ca_offset._fetch_instances()
                                self.ca_length._fetch_instances()


                        class SuspEr(KaitaiStruct):
                            """
                            .. seealso::
                               susp 5.5
                            """
                            SEQ_FIELDS = ["len_id", "len_des", "len_src", "ext_ver", "ext_id", "ext_des", "ext_src"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspEr, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['len_id']['start'] = self._io.pos()
                                self.len_id = self._io.read_u1()
                                self._debug['len_id']['end'] = self._io.pos()
                                self._debug['len_des']['start'] = self._io.pos()
                                self.len_des = self._io.read_u1()
                                self._debug['len_des']['end'] = self._io.pos()
                                self._debug['len_src']['start'] = self._io.pos()
                                self.len_src = self._io.read_u1()
                                self._debug['len_src']['end'] = self._io.pos()
                                self._debug['ext_ver']['start'] = self._io.pos()
                                self.ext_ver = self._io.read_u1()
                                self._debug['ext_ver']['end'] = self._io.pos()
                                self._debug['ext_id']['start'] = self._io.pos()
                                self.ext_id = self._io.read_bytes(self.len_id)
                                self._debug['ext_id']['end'] = self._io.pos()
                                self._debug['ext_des']['start'] = self._io.pos()
                                self.ext_des = self._io.read_bytes(self.len_des)
                                self._debug['ext_des']['end'] = self._io.pos()
                                self._debug['ext_src']['start'] = self._io.pos()
                                self.ext_src = self._io.read_bytes(self.len_src)
                                self._debug['ext_src']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass


                        class SuspEs(KaitaiStruct):
                            """
                            .. seealso::
                               susp 5.6
                            """
                            SEQ_FIELDS = ["ext_seq"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspEs, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['ext_seq']['start'] = self._io.pos()
                                self.ext_seq = self._io.read_u1()
                                self._debug['ext_seq']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass


                        class SuspPd(KaitaiStruct):
                            """
                            .. seealso::
                               susp 5.2
                            """
                            SEQ_FIELDS = ["padding_area"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspPd, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['padding_area']['start'] = self._io.pos()
                                self.padding_area = self._io.read_bytes_full()
                                self._debug['padding_area']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass


                        class SuspSl(KaitaiStruct):
                            """
                            .. seealso::
                               susp 4.1.3.1
                            """
                            SEQ_FIELDS = ["reserved", "continued", "component_records"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspSl, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['reserved']['start'] = self._io.pos()
                                self.reserved = self._io.read_bits_int_be(7)
                                self._debug['reserved']['end'] = self._io.pos()
                                self._debug['continued']['start'] = self._io.pos()
                                self.continued = self._io.read_bits_int_be(1) != 0
                                self._debug['continued']['end'] = self._io.pos()
                                self._debug['component_records']['start'] = self._io.pos()
                                self._debug['component_records']['arr'] = []
                                self.component_records = []
                                i = 0
                                while not self._io.is_eof():
                                    self._debug['component_records']['arr'].append({'start': self._io.pos()})
                                    self.component_records.append(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspSlComponentRecord(self._io, self, self._root))
                                    self._debug['component_records']['arr'][len(self.component_records) - 1]['end'] = self._io.pos()
                                    i += 1

                                self._debug['component_records']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass
                                for i in range(len(self.component_records)):
                                    pass
                                    self.component_records[i]._fetch_instances()



                        class SuspSlComponentRecord(KaitaiStruct):
                            """
                            .. seealso::
                               susp 4.1.3.1
                            """
                            SEQ_FIELDS = ["reserved", "root", "parent", "current", "continued", "len_component", "content"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspSlComponentRecord, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['reserved']['start'] = self._io.pos()
                                self.reserved = self._io.read_bits_int_be(4)
                                self._debug['reserved']['end'] = self._io.pos()
                                self._debug['root']['start'] = self._io.pos()
                                self.root = self._io.read_bits_int_be(1) != 0
                                self._debug['root']['end'] = self._io.pos()
                                self._debug['parent']['start'] = self._io.pos()
                                self.parent = self._io.read_bits_int_be(1) != 0
                                self._debug['parent']['end'] = self._io.pos()
                                self._debug['current']['start'] = self._io.pos()
                                self.current = self._io.read_bits_int_be(1) != 0
                                self._debug['current']['end'] = self._io.pos()
                                self._debug['continued']['start'] = self._io.pos()
                                self.continued = self._io.read_bits_int_be(1) != 0
                                self._debug['continued']['end'] = self._io.pos()
                                self._debug['len_component']['start'] = self._io.pos()
                                self.len_component = self._io.read_u1()
                                self._debug['len_component']['end'] = self._io.pos()
                                self._debug['content']['start'] = self._io.pos()
                                self.content = (self._io.read_bytes(self.len_component)).decode(u"ASCII")
                                self._debug['content']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass


                        class SuspSp(KaitaiStruct):
                            """
                            .. seealso::
                               susp 5.3
                            """
                            SEQ_FIELDS = ["check_bytes", "len_skp"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspSp, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['check_bytes']['start'] = self._io.pos()
                                self.check_bytes = self._io.read_bytes(2)
                                self._debug['check_bytes']['end'] = self._io.pos()
                                if not self.check_bytes == b"\xBE\xEF":
                                    raise kaitaistruct.ValidationNotEqualError(b"\xBE\xEF", self.check_bytes, self._io, u"/types/volume_descriptor/types/directory_record/types/body/types/susp/types/header/types/susp_sp/seq/0")
                                self._debug['len_skp']['start'] = self._io.pos()
                                self.len_skp = self._io.read_bytes_full()
                                self._debug['len_skp']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass


                        class SuspSt(KaitaiStruct):
                            SEQ_FIELDS = []
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspSt, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                pass


                            def _fetch_instances(self):
                                pass


                        class SuspUnknown(KaitaiStruct):
                            SEQ_FIELDS = ["data"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(Iso9660.VolumeDescriptor.DirectoryRecord.Body.Susp.Header.SuspUnknown, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['data']['start'] = self._io.pos()
                                self.data = self._io.read_bytes_full()
                                self._debug['data']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass




                @property
                def directory_records(self):
                    if hasattr(self, '_m_directory_records'):
                        return self._m_directory_records

                    if  ((self._parent.len_dr > 0) and (self.file_flags_directory)) :
                        pass
                        io = self._root._io
                        _pos = io.pos()
                        io.seek(self._root.sector_size * self.extent.value)
                        self._debug['_m_directory_records']['start'] = io.pos()
                        self._raw__m_directory_records = io.read_bytes(self.data_len.value)
                        _io__raw__m_directory_records = KaitaiStream(BytesIO(self._raw__m_directory_records))
                        self._m_directory_records = Iso9660.VolumeDescriptor.DirectoryRecords(_io__raw__m_directory_records, self, self._root)
                        self._debug['_m_directory_records']['end'] = io.pos()
                        io.seek(_pos)

                    return getattr(self, '_m_directory_records', None)

                @property
                def file_content(self):
                    if hasattr(self, '_m_file_content'):
                        return self._m_file_content

                    if  ((self._parent.len_dr > 0) and ((not (self.file_flags_directory)))) :
                        pass
                        io = self._root._io
                        _pos = io.pos()
                        io.seek(self._root.sector_size * self.extent.value)
                        self._debug['_m_file_content']['start'] = io.pos()
                        self._m_file_content = io.read_bytes(self.data_len.value)
                        self._debug['_m_file_content']['end'] = io.pos()
                        io.seek(_pos)

                    return getattr(self, '_m_file_content', None)



        class DirectoryRecords(KaitaiStruct):
            """First item "." points to it self
            Second item ".." points to the parent, or also to self if it is the root
            """
            SEQ_FIELDS = ["records"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Iso9660.VolumeDescriptor.DirectoryRecords, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['records']['start'] = self._io.pos()
                self._debug['records']['arr'] = []
                self.records = []
                i = 0
                while True:
                    self._debug['records']['arr'].append({'start': self._io.pos()})
                    _ = Iso9660.VolumeDescriptor.DirectoryRecord(self._io, self, self._root)
                    self.records.append(_)
                    self._debug['records']['arr'][len(self.records) - 1]['end'] = self._io.pos()
                    if  ((self._io.is_eof()) or (self._io.size() - self._io.pos() < 34)) :
                        break
                    i += 1
                self._debug['records']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.records)):
                    pass
                    self.records[i]._fetch_instances()



        class PathTableRecords(KaitaiStruct):
            """
            .. seealso::
               ecma-119 9.4
            """
            SEQ_FIELDS = ["path_table_record"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Iso9660.VolumeDescriptor.PathTableRecords, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['path_table_record']['start'] = self._io.pos()
                self._debug['path_table_record']['arr'] = []
                self.path_table_record = []
                i = 0
                while not self._io.is_eof():
                    self._debug['path_table_record']['arr'].append({'start': self._io.pos()})
                    self.path_table_record.append(Iso9660.VolumeDescriptor.PathTableRecords.PathTableRecord(self._io, self, self._root))
                    self._debug['path_table_record']['arr'][len(self.path_table_record) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['path_table_record']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.path_table_record)):
                    pass
                    self.path_table_record[i]._fetch_instances()


            class PathTableRecord(KaitaiStruct):
                """
                .. seealso::
                   ecma-119 9.4
                """
                SEQ_FIELDS = ["len_dir_name", "len_ext_rec", "loc_ext", "parent_dir_num", "dir_name", "padding_field"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Iso9660.VolumeDescriptor.PathTableRecords.PathTableRecord, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['len_dir_name']['start'] = self._io.pos()
                    self.len_dir_name = self._io.read_u1()
                    self._debug['len_dir_name']['end'] = self._io.pos()
                    self._debug['len_ext_rec']['start'] = self._io.pos()
                    self.len_ext_rec = self._io.read_u1()
                    self._debug['len_ext_rec']['end'] = self._io.pos()
                    self._debug['loc_ext']['start'] = self._io.pos()
                    self.loc_ext = self._io.read_u4le()
                    self._debug['loc_ext']['end'] = self._io.pos()
                    self._debug['parent_dir_num']['start'] = self._io.pos()
                    self.parent_dir_num = self._io.read_u2le()
                    self._debug['parent_dir_num']['end'] = self._io.pos()
                    self._debug['dir_name']['start'] = self._io.pos()
                    self.dir_name = (self._io.read_bytes(self.len_dir_name)).decode(u"ASCII")
                    self._debug['dir_name']['end'] = self._io.pos()
                    if self.len_dir_name % 2 == 1:
                        pass
                        self._debug['padding_field']['start'] = self._io.pos()
                        self.padding_field = self._io.read_bytes(1)
                        self._debug['padding_field']['end'] = self._io.pos()
                        if not self.padding_field == b"\x00":
                            raise kaitaistruct.ValidationNotEqualError(b"\x00", self.padding_field, self._io, u"/types/volume_descriptor/types/path_table_records/types/path_table_record/seq/5")



                def _fetch_instances(self):
                    pass
                    if self.len_dir_name % 2 == 1:
                        pass

                    _ = self.directory_records
                    if hasattr(self, '_m_directory_records'):
                        pass
                        self._m_directory_records._fetch_instances()


                @property
                def directory_records(self):
                    if hasattr(self, '_m_directory_records'):
                        return self._m_directory_records

                    io = self._root._io
                    _pos = io.pos()
                    io.seek(self._root.sector_size * self.loc_ext)
                    self._debug['_m_directory_records']['start'] = io.pos()
                    self._raw__m_directory_records = io.read_bytes(self._root.sector_size)
                    _io__raw__m_directory_records = KaitaiStream(BytesIO(self._raw__m_directory_records))
                    self._m_directory_records = Iso9660.VolumeDescriptor.DirectoryRecord(_io__raw__m_directory_records, self, self._root)
                    self._debug['_m_directory_records']['end'] = io.pos()
                    io.seek(_pos)
                    return getattr(self, '_m_directory_records', None)



        class Primary(KaitaiStruct):
            """
            .. seealso::
               ecma-119 8.4
            """
            SEQ_FIELDS = ["unused01", "system_identifier", "volume_identifier", "unused02", "volume_space_size", "unused03", "volume_set_size", "volume_sequence_number", "logical_block_size", "path_table_size", "loc_l_path_table", "loc_opt_l_path_table", "loc_m_path_table", "loc_opt_m_path_table", "root_directory", "volume_set_identifier", "publisher_identifier", "data_preparer_identifier", "application_identifier", "copyright_file_identifier", "abstract_file_identifier", "bibliographic_file_identifier", "volume_creation_date_and_time", "volume_modification_date_and_time", "volume_expiration_date_and_time", "volume_effective_date_and_time", "file_structure_version"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Iso9660.VolumeDescriptor.Primary, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['unused01']['start'] = self._io.pos()
                self.unused01 = self._io.read_bytes(1)
                self._debug['unused01']['end'] = self._io.pos()
                if not self.unused01 == b"\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x00", self.unused01, self._io, u"/types/volume_descriptor/types/primary/seq/0")
                self._debug['system_identifier']['start'] = self._io.pos()
                self.system_identifier = Iso9660.VolumeDescriptor.Text32(self._io, self, self._root)
                self._debug['system_identifier']['end'] = self._io.pos()
                self._debug['volume_identifier']['start'] = self._io.pos()
                self.volume_identifier = Iso9660.VolumeDescriptor.Text32(self._io, self, self._root)
                self._debug['volume_identifier']['end'] = self._io.pos()
                self._debug['unused02']['start'] = self._io.pos()
                self.unused02 = self._io.read_bytes(8)
                self._debug['unused02']['end'] = self._io.pos()
                if not self.unused02 == b"\x00\x00\x00\x00\x00\x00\x00\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00", self.unused02, self._io, u"/types/volume_descriptor/types/primary/seq/3")
                self._debug['volume_space_size']['start'] = self._io.pos()
                self.volume_space_size = Iso9660.U4bi(self._io, self, self._root)
                self._debug['volume_space_size']['end'] = self._io.pos()
                self._debug['unused03']['start'] = self._io.pos()
                self.unused03 = self._io.read_bytes(32)
                self._debug['unused03']['end'] = self._io.pos()
                if not self.unused03 == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.unused03, self._io, u"/types/volume_descriptor/types/primary/seq/5")
                self._debug['volume_set_size']['start'] = self._io.pos()
                self.volume_set_size = Iso9660.U2bi(self._io, self, self._root)
                self._debug['volume_set_size']['end'] = self._io.pos()
                self._debug['volume_sequence_number']['start'] = self._io.pos()
                self.volume_sequence_number = Iso9660.U2bi(self._io, self, self._root)
                self._debug['volume_sequence_number']['end'] = self._io.pos()
                self._debug['logical_block_size']['start'] = self._io.pos()
                self.logical_block_size = Iso9660.U2bi(self._io, self, self._root)
                self._debug['logical_block_size']['end'] = self._io.pos()
                self._debug['path_table_size']['start'] = self._io.pos()
                self.path_table_size = Iso9660.U4bi(self._io, self, self._root)
                self._debug['path_table_size']['end'] = self._io.pos()
                self._debug['loc_l_path_table']['start'] = self._io.pos()
                self.loc_l_path_table = self._io.read_u4le()
                self._debug['loc_l_path_table']['end'] = self._io.pos()
                self._debug['loc_opt_l_path_table']['start'] = self._io.pos()
                self.loc_opt_l_path_table = self._io.read_u4le()
                self._debug['loc_opt_l_path_table']['end'] = self._io.pos()
                self._debug['loc_m_path_table']['start'] = self._io.pos()
                self.loc_m_path_table = self._io.read_u4be()
                self._debug['loc_m_path_table']['end'] = self._io.pos()
                self._debug['loc_opt_m_path_table']['start'] = self._io.pos()
                self.loc_opt_m_path_table = self._io.read_u4be()
                self._debug['loc_opt_m_path_table']['end'] = self._io.pos()
                self._debug['root_directory']['start'] = self._io.pos()
                self._raw_root_directory = self._io.read_bytes(34)
                _io__raw_root_directory = KaitaiStream(BytesIO(self._raw_root_directory))
                self.root_directory = Iso9660.VolumeDescriptor.DirectoryRecord(_io__raw_root_directory, self, self._root)
                self._debug['root_directory']['end'] = self._io.pos()
                self._debug['volume_set_identifier']['start'] = self._io.pos()
                self.volume_set_identifier = Iso9660.VolumeDescriptor.Text128(self._io, self, self._root)
                self._debug['volume_set_identifier']['end'] = self._io.pos()
                self._debug['publisher_identifier']['start'] = self._io.pos()
                self.publisher_identifier = Iso9660.VolumeDescriptor.Text128(self._io, self, self._root)
                self._debug['publisher_identifier']['end'] = self._io.pos()
                self._debug['data_preparer_identifier']['start'] = self._io.pos()
                self.data_preparer_identifier = Iso9660.VolumeDescriptor.Text128(self._io, self, self._root)
                self._debug['data_preparer_identifier']['end'] = self._io.pos()
                self._debug['application_identifier']['start'] = self._io.pos()
                self.application_identifier = Iso9660.VolumeDescriptor.Text128(self._io, self, self._root)
                self._debug['application_identifier']['end'] = self._io.pos()
                self._debug['copyright_file_identifier']['start'] = self._io.pos()
                self.copyright_file_identifier = Iso9660.VolumeDescriptor.Text37(self._io, self, self._root)
                self._debug['copyright_file_identifier']['end'] = self._io.pos()
                self._debug['abstract_file_identifier']['start'] = self._io.pos()
                self.abstract_file_identifier = Iso9660.VolumeDescriptor.Text37(self._io, self, self._root)
                self._debug['abstract_file_identifier']['end'] = self._io.pos()
                self._debug['bibliographic_file_identifier']['start'] = self._io.pos()
                self.bibliographic_file_identifier = Iso9660.VolumeDescriptor.Text37(self._io, self, self._root)
                self._debug['bibliographic_file_identifier']['end'] = self._io.pos()
                self._debug['volume_creation_date_and_time']['start'] = self._io.pos()
                self._raw_volume_creation_date_and_time = self._io.read_bytes(17)
                _io__raw_volume_creation_date_and_time = KaitaiStream(BytesIO(self._raw_volume_creation_date_and_time))
                self.volume_creation_date_and_time = Iso9660.DatetimeLongOrEmpty(_io__raw_volume_creation_date_and_time, self, self._root)
                self._debug['volume_creation_date_and_time']['end'] = self._io.pos()
                self._debug['volume_modification_date_and_time']['start'] = self._io.pos()
                self._raw_volume_modification_date_and_time = self._io.read_bytes(17)
                _io__raw_volume_modification_date_and_time = KaitaiStream(BytesIO(self._raw_volume_modification_date_and_time))
                self.volume_modification_date_and_time = Iso9660.DatetimeLongOrEmpty(_io__raw_volume_modification_date_and_time, self, self._root)
                self._debug['volume_modification_date_and_time']['end'] = self._io.pos()
                self._debug['volume_expiration_date_and_time']['start'] = self._io.pos()
                self._raw_volume_expiration_date_and_time = self._io.read_bytes(17)
                _io__raw_volume_expiration_date_and_time = KaitaiStream(BytesIO(self._raw_volume_expiration_date_and_time))
                self.volume_expiration_date_and_time = Iso9660.DatetimeLongOrEmpty(_io__raw_volume_expiration_date_and_time, self, self._root)
                self._debug['volume_expiration_date_and_time']['end'] = self._io.pos()
                self._debug['volume_effective_date_and_time']['start'] = self._io.pos()
                self._raw_volume_effective_date_and_time = self._io.read_bytes(17)
                _io__raw_volume_effective_date_and_time = KaitaiStream(BytesIO(self._raw_volume_effective_date_and_time))
                self.volume_effective_date_and_time = Iso9660.DatetimeLongOrEmpty(_io__raw_volume_effective_date_and_time, self, self._root)
                self._debug['volume_effective_date_and_time']['end'] = self._io.pos()
                self._debug['file_structure_version']['start'] = self._io.pos()
                self.file_structure_version = self._io.read_s1()
                self._debug['file_structure_version']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.system_identifier._fetch_instances()
                self.volume_identifier._fetch_instances()
                self.volume_space_size._fetch_instances()
                self.volume_set_size._fetch_instances()
                self.volume_sequence_number._fetch_instances()
                self.logical_block_size._fetch_instances()
                self.path_table_size._fetch_instances()
                self.root_directory._fetch_instances()
                self.volume_set_identifier._fetch_instances()
                self.publisher_identifier._fetch_instances()
                self.data_preparer_identifier._fetch_instances()
                self.application_identifier._fetch_instances()
                self.copyright_file_identifier._fetch_instances()
                self.abstract_file_identifier._fetch_instances()
                self.bibliographic_file_identifier._fetch_instances()
                self.volume_creation_date_and_time._fetch_instances()
                self.volume_modification_date_and_time._fetch_instances()
                self.volume_expiration_date_and_time._fetch_instances()
                self.volume_effective_date_and_time._fetch_instances()
                _ = self.path_table
                if hasattr(self, '_m_path_table'):
                    pass
                    self._m_path_table._fetch_instances()


            @property
            def path_table(self):
                if hasattr(self, '_m_path_table'):
                    return self._m_path_table

                io = self._root._io
                _pos = io.pos()
                io.seek(self._root.sector_size * self.loc_l_path_table)
                self._debug['_m_path_table']['start'] = io.pos()
                self._raw__m_path_table = io.read_bytes(self.path_table_size.value)
                _io__raw__m_path_table = KaitaiStream(BytesIO(self._raw__m_path_table))
                self._m_path_table = Iso9660.VolumeDescriptor.PathTableRecords(_io__raw__m_path_table, self, self._root)
                self._debug['_m_path_table']['end'] = io.pos()
                io.seek(_pos)
                return getattr(self, '_m_path_table', None)


        class Supplementary(KaitaiStruct):
            """
            .. seealso::
               ecma-119 8.5
            """
            SEQ_FIELDS = ["volume_flags_reserved", "volume_flags_not_iso2375", "system_identifier", "volume_identifier", "unused01", "volume_space_size", "escape_sequences", "volume_set_size", "volume_sequence_number", "logical_block_size", "path_table_size", "loc_l_path_table", "loc_opt_l_path_table", "loc_m_path_table", "loc_opt_m_path_table", "root_directory", "volume_set_identifier", "publisher_identifier", "data_preparer_identifier", "application_identifier", "copyright_file_identifier", "abstract_file_identifier", "bibliographic_file_identifier", "volume_creation_date_and_time", "volume_modification_date_and_time", "volume_expiration_date_and_time", "volume_effective_date_and_time", "file_structure_version"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Iso9660.VolumeDescriptor.Supplementary, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['volume_flags_reserved']['start'] = self._io.pos()
                self.volume_flags_reserved = self._io.read_bits_int_be(7)
                self._debug['volume_flags_reserved']['end'] = self._io.pos()
                self._debug['volume_flags_not_iso2375']['start'] = self._io.pos()
                self.volume_flags_not_iso2375 = self._io.read_bits_int_be(1) != 0
                self._debug['volume_flags_not_iso2375']['end'] = self._io.pos()
                self._debug['system_identifier']['start'] = self._io.pos()
                self.system_identifier = Iso9660.VolumeDescriptor.Text32(self._io, self, self._root)
                self._debug['system_identifier']['end'] = self._io.pos()
                self._debug['volume_identifier']['start'] = self._io.pos()
                self.volume_identifier = Iso9660.VolumeDescriptor.Text32(self._io, self, self._root)
                self._debug['volume_identifier']['end'] = self._io.pos()
                self._debug['unused01']['start'] = self._io.pos()
                self.unused01 = self._io.read_bytes(8)
                self._debug['unused01']['end'] = self._io.pos()
                if not self.unused01 == b"\x00\x00\x00\x00\x00\x00\x00\x00":
                    raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00", self.unused01, self._io, u"/types/volume_descriptor/types/supplementary/seq/4")
                self._debug['volume_space_size']['start'] = self._io.pos()
                self.volume_space_size = Iso9660.U4bi(self._io, self, self._root)
                self._debug['volume_space_size']['end'] = self._io.pos()
                self._debug['escape_sequences']['start'] = self._io.pos()
                self.escape_sequences = self._io.read_bytes(32)
                self._debug['escape_sequences']['end'] = self._io.pos()
                self._debug['volume_set_size']['start'] = self._io.pos()
                self.volume_set_size = Iso9660.U2bi(self._io, self, self._root)
                self._debug['volume_set_size']['end'] = self._io.pos()
                self._debug['volume_sequence_number']['start'] = self._io.pos()
                self.volume_sequence_number = Iso9660.U2bi(self._io, self, self._root)
                self._debug['volume_sequence_number']['end'] = self._io.pos()
                self._debug['logical_block_size']['start'] = self._io.pos()
                self.logical_block_size = Iso9660.U2bi(self._io, self, self._root)
                self._debug['logical_block_size']['end'] = self._io.pos()
                self._debug['path_table_size']['start'] = self._io.pos()
                self.path_table_size = Iso9660.U4bi(self._io, self, self._root)
                self._debug['path_table_size']['end'] = self._io.pos()
                self._debug['loc_l_path_table']['start'] = self._io.pos()
                self.loc_l_path_table = self._io.read_u4le()
                self._debug['loc_l_path_table']['end'] = self._io.pos()
                self._debug['loc_opt_l_path_table']['start'] = self._io.pos()
                self.loc_opt_l_path_table = self._io.read_u4le()
                self._debug['loc_opt_l_path_table']['end'] = self._io.pos()
                self._debug['loc_m_path_table']['start'] = self._io.pos()
                self.loc_m_path_table = self._io.read_u4be()
                self._debug['loc_m_path_table']['end'] = self._io.pos()
                self._debug['loc_opt_m_path_table']['start'] = self._io.pos()
                self.loc_opt_m_path_table = self._io.read_u4be()
                self._debug['loc_opt_m_path_table']['end'] = self._io.pos()
                self._debug['root_directory']['start'] = self._io.pos()
                self._raw_root_directory = self._io.read_bytes(34)
                _io__raw_root_directory = KaitaiStream(BytesIO(self._raw_root_directory))
                self.root_directory = Iso9660.VolumeDescriptor.DirectoryRecord(_io__raw_root_directory, self, self._root)
                self._debug['root_directory']['end'] = self._io.pos()
                self._debug['volume_set_identifier']['start'] = self._io.pos()
                self.volume_set_identifier = Iso9660.VolumeDescriptor.Text128(self._io, self, self._root)
                self._debug['volume_set_identifier']['end'] = self._io.pos()
                self._debug['publisher_identifier']['start'] = self._io.pos()
                self.publisher_identifier = Iso9660.VolumeDescriptor.Text128(self._io, self, self._root)
                self._debug['publisher_identifier']['end'] = self._io.pos()
                self._debug['data_preparer_identifier']['start'] = self._io.pos()
                self.data_preparer_identifier = Iso9660.VolumeDescriptor.Text128(self._io, self, self._root)
                self._debug['data_preparer_identifier']['end'] = self._io.pos()
                self._debug['application_identifier']['start'] = self._io.pos()
                self.application_identifier = Iso9660.VolumeDescriptor.Text128(self._io, self, self._root)
                self._debug['application_identifier']['end'] = self._io.pos()
                self._debug['copyright_file_identifier']['start'] = self._io.pos()
                self.copyright_file_identifier = Iso9660.VolumeDescriptor.Text37(self._io, self, self._root)
                self._debug['copyright_file_identifier']['end'] = self._io.pos()
                self._debug['abstract_file_identifier']['start'] = self._io.pos()
                self.abstract_file_identifier = Iso9660.VolumeDescriptor.Text37(self._io, self, self._root)
                self._debug['abstract_file_identifier']['end'] = self._io.pos()
                self._debug['bibliographic_file_identifier']['start'] = self._io.pos()
                self.bibliographic_file_identifier = Iso9660.VolumeDescriptor.Text37(self._io, self, self._root)
                self._debug['bibliographic_file_identifier']['end'] = self._io.pos()
                self._debug['volume_creation_date_and_time']['start'] = self._io.pos()
                self._raw_volume_creation_date_and_time = self._io.read_bytes(17)
                _io__raw_volume_creation_date_and_time = KaitaiStream(BytesIO(self._raw_volume_creation_date_and_time))
                self.volume_creation_date_and_time = Iso9660.DatetimeLongOrEmpty(_io__raw_volume_creation_date_and_time, self, self._root)
                self._debug['volume_creation_date_and_time']['end'] = self._io.pos()
                self._debug['volume_modification_date_and_time']['start'] = self._io.pos()
                self._raw_volume_modification_date_and_time = self._io.read_bytes(17)
                _io__raw_volume_modification_date_and_time = KaitaiStream(BytesIO(self._raw_volume_modification_date_and_time))
                self.volume_modification_date_and_time = Iso9660.DatetimeLongOrEmpty(_io__raw_volume_modification_date_and_time, self, self._root)
                self._debug['volume_modification_date_and_time']['end'] = self._io.pos()
                self._debug['volume_expiration_date_and_time']['start'] = self._io.pos()
                self._raw_volume_expiration_date_and_time = self._io.read_bytes(17)
                _io__raw_volume_expiration_date_and_time = KaitaiStream(BytesIO(self._raw_volume_expiration_date_and_time))
                self.volume_expiration_date_and_time = Iso9660.DatetimeLongOrEmpty(_io__raw_volume_expiration_date_and_time, self, self._root)
                self._debug['volume_expiration_date_and_time']['end'] = self._io.pos()
                self._debug['volume_effective_date_and_time']['start'] = self._io.pos()
                self._raw_volume_effective_date_and_time = self._io.read_bytes(17)
                _io__raw_volume_effective_date_and_time = KaitaiStream(BytesIO(self._raw_volume_effective_date_and_time))
                self.volume_effective_date_and_time = Iso9660.DatetimeLongOrEmpty(_io__raw_volume_effective_date_and_time, self, self._root)
                self._debug['volume_effective_date_and_time']['end'] = self._io.pos()
                self._debug['file_structure_version']['start'] = self._io.pos()
                self.file_structure_version = self._io.read_s1()
                self._debug['file_structure_version']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.system_identifier._fetch_instances()
                self.volume_identifier._fetch_instances()
                self.volume_space_size._fetch_instances()
                self.volume_set_size._fetch_instances()
                self.volume_sequence_number._fetch_instances()
                self.logical_block_size._fetch_instances()
                self.path_table_size._fetch_instances()
                self.root_directory._fetch_instances()
                self.volume_set_identifier._fetch_instances()
                self.publisher_identifier._fetch_instances()
                self.data_preparer_identifier._fetch_instances()
                self.application_identifier._fetch_instances()
                self.copyright_file_identifier._fetch_instances()
                self.abstract_file_identifier._fetch_instances()
                self.bibliographic_file_identifier._fetch_instances()
                self.volume_creation_date_and_time._fetch_instances()
                self.volume_modification_date_and_time._fetch_instances()
                self.volume_expiration_date_and_time._fetch_instances()
                self.volume_effective_date_and_time._fetch_instances()
                _ = self.path_table
                if hasattr(self, '_m_path_table'):
                    pass
                    self._m_path_table._fetch_instances()


            @property
            def path_table(self):
                if hasattr(self, '_m_path_table'):
                    return self._m_path_table

                io = self._root._io
                _pos = io.pos()
                io.seek(self._root.sector_size * self.loc_l_path_table)
                self._debug['_m_path_table']['start'] = io.pos()
                self._raw__m_path_table = io.read_bytes(self.path_table_size.value)
                _io__raw__m_path_table = KaitaiStream(BytesIO(self._raw__m_path_table))
                self._m_path_table = Iso9660.VolumeDescriptor.PathTableRecords(_io__raw__m_path_table, self, self._root)
                self._debug['_m_path_table']['end'] = io.pos()
                io.seek(_pos)
                return getattr(self, '_m_path_table', None)


        class Text128(KaitaiStruct):
            SEQ_FIELDS = ["text"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Iso9660.VolumeDescriptor.Text128, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['text']['start'] = self._io.pos()
                self.text = (self._io.read_bytes(128)).decode(u"ASCII")
                self._debug['text']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class Text32(KaitaiStruct):
            SEQ_FIELDS = ["text"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Iso9660.VolumeDescriptor.Text32, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['text']['start'] = self._io.pos()
                self.text = (self._io.read_bytes(32)).decode(u"ASCII")
                self._debug['text']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class Text37(KaitaiStruct):
            SEQ_FIELDS = ["text"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Iso9660.VolumeDescriptor.Text37, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['text']['start'] = self._io.pos()
                self.text = (self._io.read_bytes(37)).decode(u"ASCII")
                self._debug['text']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass



    @property
    def sector_size(self):
        """
        .. seealso::
           ecma-119 6.1.2
        """
        if hasattr(self, '_m_sector_size'):
            return self._m_sector_size

        self._m_sector_size = 2048
        return getattr(self, '_m_sector_size', None)


