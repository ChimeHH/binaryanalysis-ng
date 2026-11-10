# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Tzif(KaitaiStruct):
    """TZif is the binary file format used to represent data for a single time zone
    compiled by the _zic_ compiler from information in the IANA time zone
    database. It is used by most UNIX systems to calculate local time for a time
    zone, usually identified by a time zone identifier string referring to a
    relatively populous location within the geographic region covered by the time
    zone, for example: "America/New_York" or "Europe/Paris". This identifier is
    external to the TZif file itself.
    """
    SEQ_FIELDS = ["v1_struct", "v2_struct", "v2_footer"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Tzif, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['v1_struct']['start'] = self._io.pos()
        self.v1_struct = Tzif.TzStruct(False, self._io, self, self._root)
        self._debug['v1_struct']['end'] = self._io.pos()
        if self.version >= 2:
            pass
            self._debug['v2_struct']['start'] = self._io.pos()
            self.v2_struct = Tzif.TzStruct(True, self._io, self, self._root)
            self._debug['v2_struct']['end'] = self._io.pos()
            _ = self.v2_struct
            if not _.header.ver_byte == self._root.v1_struct.header.ver_byte:
                raise kaitaistruct.ValidationExprError(self.v2_struct, self._io, u"/seq/1")

        if self.version >= 2:
            pass
            self._debug['v2_footer']['start'] = self._io.pos()
            self.v2_footer = Tzif.TzFooter(self._io, self, self._root)
            self._debug['v2_footer']['end'] = self._io.pos()



    def _fetch_instances(self):
        pass
        self.v1_struct._fetch_instances()
        if self.version >= 2:
            pass
            self.v2_struct._fetch_instances()

        if self.version >= 2:
            pass
            self.v2_footer._fetch_instances()


    class TzData(KaitaiStruct):
        """
        .. seealso::
           Source - https://tools.ietf.org/html/rfc8536#section-3.2
        """
        SEQ_FIELDS = ["transition_times", "transition_types", "local_time_types", "tz_designations", "leap_second_records", "std_flags", "ut_flags"]
        def __init__(self, is_ts64, num_transition_times, num_local_time_types, len_tz_designations, num_leap_second_records, num_std_flags, num_ut_flags, _io, _parent=None, _root=None):
            super(Tzif.TzData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.is_ts64 = is_ts64
            self.num_transition_times = num_transition_times
            self.num_local_time_types = num_local_time_types
            self.len_tz_designations = len_tz_designations
            self.num_leap_second_records = num_leap_second_records
            self.num_std_flags = num_std_flags
            self.num_ut_flags = num_ut_flags
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['transition_times']['start'] = self._io.pos()
            self._debug['transition_times']['arr'] = []
            self.transition_times = []
            for i in range(self.num_transition_times):
                self._debug['transition_times']['arr'].append({'start': self._io.pos()})
                _on = self.is_ts64
                if _on == False:
                    pass
                    self.transition_times.append(self._io.read_s4be())
                elif _on == True:
                    pass
                    self.transition_times.append(self._io.read_s8be())
                self._debug['transition_times']['arr'][i]['end'] = self._io.pos()

            self._debug['transition_times']['end'] = self._io.pos()
            self._debug['transition_types']['start'] = self._io.pos()
            self._debug['transition_types']['arr'] = []
            self.transition_types = []
            for i in range(self.num_transition_times):
                self._debug['transition_types']['arr'].append({'start': self._io.pos()})
                self.transition_types.append(self._io.read_u1())
                self._debug['transition_types']['arr'][i]['end'] = self._io.pos()

            self._debug['transition_types']['end'] = self._io.pos()
            self._debug['local_time_types']['start'] = self._io.pos()
            self._debug['local_time_types']['arr'] = []
            self.local_time_types = []
            for i in range(self.num_local_time_types):
                self._debug['local_time_types']['arr'].append({'start': self._io.pos()})
                self.local_time_types.append(Tzif.TzLocalTimeType(self._io, self, self._root))
                self._debug['local_time_types']['arr'][i]['end'] = self._io.pos()

            self._debug['local_time_types']['end'] = self._io.pos()
            self._debug['tz_designations']['start'] = self._io.pos()
            self.tz_designations = self._io.read_bytes(self.len_tz_designations)
            self._debug['tz_designations']['end'] = self._io.pos()
            _ = self.tz_designations
            if not KaitaiStream.byte_array_index(_, -1) == 0:
                raise kaitaistruct.ValidationExprError(self.tz_designations, self._io, u"/types/tz_data/seq/3")
            self._debug['leap_second_records']['start'] = self._io.pos()
            self._debug['leap_second_records']['arr'] = []
            self.leap_second_records = []
            for i in range(self.num_leap_second_records):
                self._debug['leap_second_records']['arr'].append({'start': self._io.pos()})
                self.leap_second_records.append(Tzif.TzLeapSecondRecord(self.is_ts64, self._io, self, self._root))
                self._debug['leap_second_records']['arr'][i]['end'] = self._io.pos()

            self._debug['leap_second_records']['end'] = self._io.pos()
            self._debug['std_flags']['start'] = self._io.pos()
            self._debug['std_flags']['arr'] = []
            self.std_flags = []
            for i in range(self.num_std_flags):
                self._debug['std_flags']['arr'].append({'start': self._io.pos()})
                self.std_flags.append(self._io.read_u1())
                self._debug['std_flags']['arr'][i]['end'] = self._io.pos()

            self._debug['std_flags']['end'] = self._io.pos()
            self._debug['ut_flags']['start'] = self._io.pos()
            self._debug['ut_flags']['arr'] = []
            self.ut_flags = []
            for i in range(self.num_ut_flags):
                self._debug['ut_flags']['arr'].append({'start': self._io.pos()})
                self.ut_flags.append(self._io.read_u1())
                self._debug['ut_flags']['arr'][i]['end'] = self._io.pos()

            self._debug['ut_flags']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.transition_times)):
                pass
                _on = self.is_ts64
                if _on == False:
                    pass
                elif _on == True:
                    pass

            for i in range(len(self.transition_types)):
                pass

            for i in range(len(self.local_time_types)):
                pass
                self.local_time_types[i]._fetch_instances()

            for i in range(len(self.leap_second_records)):
                pass
                self.leap_second_records[i]._fetch_instances()

            for i in range(len(self.std_flags)):
                pass

            for i in range(len(self.ut_flags)):
                pass



    class TzFooter(KaitaiStruct):
        """
        .. seealso::
           Source - https://tools.ietf.org/html/rfc8536#section-3.3
        """
        SEQ_FIELDS = ["head_nl", "tz_string", "tail_nl"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Tzif.TzFooter, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['head_nl']['start'] = self._io.pos()
            self.head_nl = self._io.read_bytes(1)
            self._debug['head_nl']['end'] = self._io.pos()
            if not self.head_nl == b"\x0A":
                raise kaitaistruct.ValidationNotEqualError(b"\x0A", self.head_nl, self._io, u"/types/tz_footer/seq/0")
            self._debug['tz_string']['start'] = self._io.pos()
            self.tz_string = (self._io.read_bytes_term(10, False, False, True)).decode(u"ASCII")
            self._debug['tz_string']['end'] = self._io.pos()
            self._debug['tail_nl']['start'] = self._io.pos()
            self.tail_nl = self._io.read_bytes(1)
            self._debug['tail_nl']['end'] = self._io.pos()
            if not self.tail_nl == b"\x0A":
                raise kaitaistruct.ValidationNotEqualError(b"\x0A", self.tail_nl, self._io, u"/types/tz_footer/seq/2")


        def _fetch_instances(self):
            pass


    class TzHeader(KaitaiStruct):
        """
        .. seealso::
           Source - https://tools.ietf.org/html/rfc8536#section-3.1
        """
        SEQ_FIELDS = ["magic", "ver_byte", "reserved", "num_ut_flags", "num_std_flags", "num_leap_second_records", "num_transition_times", "num_local_time_types", "len_tz_designations"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Tzif.TzHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x54\x5A\x69\x66":
                raise kaitaistruct.ValidationNotEqualError(b"\x54\x5A\x69\x66", self.magic, self._io, u"/types/tz_header/seq/0")
            self._debug['ver_byte']['start'] = self._io.pos()
            self.ver_byte = self._io.read_u1()
            self._debug['ver_byte']['end'] = self._io.pos()
            _ = self.ver_byte
            if not  ((_ == 0) or ( ((_ >= 50) and (_ <= 57)) )) :
                raise kaitaistruct.ValidationExprError(self.ver_byte, self._io, u"/types/tz_header/seq/1")
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(15)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['num_ut_flags']['start'] = self._io.pos()
            self.num_ut_flags = self._io.read_u4be()
            self._debug['num_ut_flags']['end'] = self._io.pos()
            self._debug['num_std_flags']['start'] = self._io.pos()
            self.num_std_flags = self._io.read_u4be()
            self._debug['num_std_flags']['end'] = self._io.pos()
            self._debug['num_leap_second_records']['start'] = self._io.pos()
            self.num_leap_second_records = self._io.read_u4be()
            self._debug['num_leap_second_records']['end'] = self._io.pos()
            self._debug['num_transition_times']['start'] = self._io.pos()
            self.num_transition_times = self._io.read_u4be()
            self._debug['num_transition_times']['end'] = self._io.pos()
            if not self.num_transition_times <= self._root._io.size() // 5:
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size() // 5, self.num_transition_times, self._io, u"/types/tz_header/seq/6")
            self._debug['num_local_time_types']['start'] = self._io.pos()
            self.num_local_time_types = self._io.read_u4be()
            self._debug['num_local_time_types']['end'] = self._io.pos()
            _ = self.num_local_time_types
            if not  ((_ != 0) and ( ((self.num_ut_flags == 0) or (_ == self.num_ut_flags)) ) and ( ((self.num_std_flags == 0) or (_ == self.num_std_flags)) )) :
                raise kaitaistruct.ValidationExprError(self.num_local_time_types, self._io, u"/types/tz_header/seq/7")
            self._debug['len_tz_designations']['start'] = self._io.pos()
            self.len_tz_designations = self._io.read_u4be()
            self._debug['len_tz_designations']['end'] = self._io.pos()
            _ = self.len_tz_designations
            if not _ != 0:
                raise kaitaistruct.ValidationExprError(self.len_tz_designations, self._io, u"/types/tz_header/seq/8")


        def _fetch_instances(self):
            pass

        @property
        def version(self):
            """File format version number derived from `ver_byte`. The most recent
            version as of March 2021 is 3.
            """
            if hasattr(self, '_m_version'):
                return self._m_version

            self._m_version = (self.ver_byte - 48 if self.ver_byte >= 50 else 1)
            return getattr(self, '_m_version', None)


    class TzLeapSecondRecord(KaitaiStruct):
        """
        .. seealso::
           Source - https://tools.ietf.org/html/rfc8536#section-3.2
        """
        SEQ_FIELDS = ["occurrence", "correction"]
        def __init__(self, is_ts64, _io, _parent=None, _root=None):
            super(Tzif.TzLeapSecondRecord, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.is_ts64 = is_ts64
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['occurrence']['start'] = self._io.pos()
            _on = self.is_ts64
            if _on == False:
                pass
                self.occurrence = self._io.read_s4be()
            elif _on == True:
                pass
                self.occurrence = self._io.read_s8be()
            self._debug['occurrence']['end'] = self._io.pos()
            self._debug['correction']['start'] = self._io.pos()
            self.correction = self._io.read_s4be()
            self._debug['correction']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.is_ts64
            if _on == False:
                pass
            elif _on == True:
                pass


    class TzLocalTimeType(KaitaiStruct):
        """
        .. seealso::
           Source - https://tools.ietf.org/html/rfc8536#section-3.2
        """
        SEQ_FIELDS = ["ut_offset", "dst_flag", "desig_idx"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Tzif.TzLocalTimeType, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ut_offset']['start'] = self._io.pos()
            self.ut_offset = self._io.read_s4be()
            self._debug['ut_offset']['end'] = self._io.pos()
            self._debug['dst_flag']['start'] = self._io.pos()
            self.dst_flag = self._io.read_u1()
            self._debug['dst_flag']['end'] = self._io.pos()
            if not  ((self.dst_flag == 0) or (self.dst_flag == 1)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.dst_flag, self._io, u"/types/tz_local_time_type/seq/1")
            self._debug['desig_idx']['start'] = self._io.pos()
            self.desig_idx = self._io.read_u1()
            self._debug['desig_idx']['end'] = self._io.pos()
            _ = self.desig_idx
            if not _ < self._parent.len_tz_designations:
                raise kaitaistruct.ValidationExprError(self.desig_idx, self._io, u"/types/tz_local_time_type/seq/2")


        def _fetch_instances(self):
            pass


    class TzStruct(KaitaiStruct):
        SEQ_FIELDS = ["header", "data"]
        def __init__(self, is_ts64, _io, _parent=None, _root=None):
            super(Tzif.TzStruct, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.is_ts64 = is_ts64
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Tzif.TzHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = Tzif.TzData(self.is_ts64, self.header.num_transition_times, self.header.num_local_time_types, self.header.len_tz_designations, self.header.num_leap_second_records, self.header.num_std_flags, self.header.num_ut_flags, self._io, self, self._root)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            self.data._fetch_instances()


    @property
    def version(self):
        if hasattr(self, '_m_version'):
            return self._m_version

        self._m_version = self.v1_struct.header.version
        return getattr(self, '_m_version', None)


