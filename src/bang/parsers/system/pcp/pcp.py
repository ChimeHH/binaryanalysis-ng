# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Pcp(KaitaiStruct):
    """
    .. seealso::
       Source - https://github.com/performancecopilot/pcp/blob/main/man/man5/LOGARCHIVE.5
    
    
    .. seealso::
       Source - https://man7.org/linux/man-pages/man5/LOGARCHIVE.5.html
    """

    class LabelTypes(IntEnum):
        context = 1
        domain = 2
        indom = 4
        cluster = 8
        item = 16
        instances = 32

    class MetaRecords(IntEnum):
        description = 1
        instance_domain = 2
        label = 3
        text = 4
    SEQ_FIELDS = ["len_record1", "header", "len_record2", "records"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Pcp, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['len_record1']['start'] = self._io.pos()
        self.len_record1 = self._io.read_u4be()
        self._debug['len_record1']['end'] = self._io.pos()
        if not self.len_record1 == 132:
            raise kaitaistruct.ValidationNotEqualError(132, self.len_record1, self._io, u"/seq/0")
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(self.len_record1 - 4 * 2)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Pcp.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['len_record2']['start'] = self._io.pos()
        self.len_record2 = self._io.read_u4be()
        self._debug['len_record2']['end'] = self._io.pos()
        if not self.len_record2 == self.len_record1:
            raise kaitaistruct.ValidationNotEqualError(self.len_record1, self.len_record2, self._io, u"/seq/2")
        self._debug['records']['start'] = self._io.pos()
        self._debug['records']['arr'] = []
        self.records = []
        i = 0
        while not self._io.is_eof():
            self._debug['records']['arr'].append({'start': self._io.pos()})
            _on = self.header.log_volume_number
            if _on == -1:
                pass
                self.records.append(Pcp.Meta(self._io, self, self._root))
            elif _on == -2:
                pass
                self.records.append(Pcp.Index(self._io, self, self._root))
            else:
                pass
                self.records.append(Pcp.Archive(self._io, self, self._root))
            self._debug['records']['arr'][len(self.records) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['records']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        for i in range(len(self.records)):
            pass
            _on = self.header.log_volume_number
            if _on == -1:
                pass
                self.records[i]._fetch_instances()
            elif _on == -2:
                pass
                self.records[i]._fetch_instances()
            else:
                pass
                self.records[i]._fetch_instances()


    class Archive(KaitaiStruct):
        SEQ_FIELDS = ["len_record1", "pm_result", "len_record2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.Archive, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_record1']['start'] = self._io.pos()
            self.len_record1 = self._io.read_u4be()
            self._debug['len_record1']['end'] = self._io.pos()
            self._debug['pm_result']['start'] = self._io.pos()
            self.pm_result = self._io.read_bytes(self.len_record1 - 4 * 2)
            self._debug['pm_result']['end'] = self._io.pos()
            self._debug['len_record2']['start'] = self._io.pos()
            self.len_record2 = self._io.read_u4be()
            self._debug['len_record2']['end'] = self._io.pos()
            if not self.len_record2 == self.len_record1:
                raise kaitaistruct.ValidationNotEqualError(self.len_record1, self.len_record2, self._io, u"/types/archive/seq/2")


        def _fetch_instances(self):
            pass


    class Description(KaitaiStruct):
        SEQ_FIELDS = ["pmid", "pm_type", "instance_domain", "semantics", "units", "num_alternatives", "names"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.Description, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['pmid']['start'] = self._io.pos()
            self.pmid = self._io.read_u4be()
            self._debug['pmid']['end'] = self._io.pos()
            self._debug['pm_type']['start'] = self._io.pos()
            self.pm_type = self._io.read_u4be()
            self._debug['pm_type']['end'] = self._io.pos()
            self._debug['instance_domain']['start'] = self._io.pos()
            self.instance_domain = self._io.read_u4be()
            self._debug['instance_domain']['end'] = self._io.pos()
            self._debug['semantics']['start'] = self._io.pos()
            self.semantics = self._io.read_u4be()
            self._debug['semantics']['end'] = self._io.pos()
            self._debug['units']['start'] = self._io.pos()
            self.units = self._io.read_u4be()
            self._debug['units']['end'] = self._io.pos()
            self._debug['num_alternatives']['start'] = self._io.pos()
            self.num_alternatives = self._io.read_u4be()
            self._debug['num_alternatives']['end'] = self._io.pos()
            self._debug['names']['start'] = self._io.pos()
            self._debug['names']['arr'] = []
            self.names = []
            for i in range(self.num_alternatives):
                self._debug['names']['arr'].append({'start': self._io.pos()})
                self.names.append(Pcp.MetaName(self._io, self, self._root))
                self._debug['names']['arr'][i]['end'] = self._io.pos()

            self._debug['names']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.names)):
                pass
                self.names[i]._fetch_instances()



    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "version", "logger_pid", "seconds", "microseconds", "log_volume_number", "hostname", "timezone"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(3)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x50\x05\x26":
                raise kaitaistruct.ValidationNotEqualError(b"\x50\x05\x26", self.magic, self._io, u"/types/header/seq/0")
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u1()
            self._debug['version']['end'] = self._io.pos()
            if not self.version == 2:
                raise kaitaistruct.ValidationNotEqualError(2, self.version, self._io, u"/types/header/seq/1")
            self._debug['logger_pid']['start'] = self._io.pos()
            self.logger_pid = self._io.read_u4be()
            self._debug['logger_pid']['end'] = self._io.pos()
            self._debug['seconds']['start'] = self._io.pos()
            self.seconds = self._io.read_u4be()
            self._debug['seconds']['end'] = self._io.pos()
            self._debug['microseconds']['start'] = self._io.pos()
            self.microseconds = self._io.read_u4be()
            self._debug['microseconds']['end'] = self._io.pos()
            self._debug['log_volume_number']['start'] = self._io.pos()
            self.log_volume_number = self._io.read_s4be()
            self._debug['log_volume_number']['end'] = self._io.pos()
            self._debug['hostname']['start'] = self._io.pos()
            self.hostname = (KaitaiStream.bytes_terminate(self._io.read_bytes(64), 0, False)).decode(u"UTF-8")
            self._debug['hostname']['end'] = self._io.pos()
            self._debug['timezone']['start'] = self._io.pos()
            self.timezone = (KaitaiStream.bytes_terminate(self._io.read_bytes(40), 0, False)).decode(u"UTF-8")
            self._debug['timezone']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Index(KaitaiStruct):
        SEQ_FIELDS = ["index_entries"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.Index, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['index_entries']['start'] = self._io.pos()
            self._debug['index_entries']['arr'] = []
            self.index_entries = []
            i = 0
            while not self._io.is_eof():
                self._debug['index_entries']['arr'].append({'start': self._io.pos()})
                self.index_entries.append(Pcp.IndexEntry(self._io, self, self._root))
                self._debug['index_entries']['arr'][len(self.index_entries) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['index_entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.index_entries)):
                pass
                self.index_entries[i]._fetch_instances()



    class IndexEntry(KaitaiStruct):
        SEQ_FIELDS = ["event_time_seconds", "event_time_microseconds", "archive_volume", "ofs_meta", "ofs_archive"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.IndexEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['event_time_seconds']['start'] = self._io.pos()
            self.event_time_seconds = self._io.read_u4be()
            self._debug['event_time_seconds']['end'] = self._io.pos()
            self._debug['event_time_microseconds']['start'] = self._io.pos()
            self.event_time_microseconds = self._io.read_u4be()
            self._debug['event_time_microseconds']['end'] = self._io.pos()
            self._debug['archive_volume']['start'] = self._io.pos()
            self.archive_volume = self._io.read_u4be()
            self._debug['archive_volume']['end'] = self._io.pos()
            self._debug['ofs_meta']['start'] = self._io.pos()
            self.ofs_meta = self._io.read_u4be()
            self._debug['ofs_meta']['end'] = self._io.pos()
            self._debug['ofs_archive']['start'] = self._io.pos()
            self.ofs_archive = self._io.read_u4be()
            self._debug['ofs_archive']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class InstanceDomain(KaitaiStruct):
        SEQ_FIELDS = ["seconds", "microseconds", "instance_domain", "num_instances", "instance_numbers", "offsets", "names"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.InstanceDomain, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['seconds']['start'] = self._io.pos()
            self.seconds = self._io.read_u4be()
            self._debug['seconds']['end'] = self._io.pos()
            self._debug['microseconds']['start'] = self._io.pos()
            self.microseconds = self._io.read_u4be()
            self._debug['microseconds']['end'] = self._io.pos()
            self._debug['instance_domain']['start'] = self._io.pos()
            self.instance_domain = self._io.read_u4be()
            self._debug['instance_domain']['end'] = self._io.pos()
            self._debug['num_instances']['start'] = self._io.pos()
            self.num_instances = self._io.read_u4be()
            self._debug['num_instances']['end'] = self._io.pos()
            self._debug['instance_numbers']['start'] = self._io.pos()
            self._debug['instance_numbers']['arr'] = []
            self.instance_numbers = []
            for i in range(self.num_instances):
                self._debug['instance_numbers']['arr'].append({'start': self._io.pos()})
                self.instance_numbers.append(self._io.read_u4be())
                self._debug['instance_numbers']['arr'][i]['end'] = self._io.pos()

            self._debug['instance_numbers']['end'] = self._io.pos()
            self._debug['offsets']['start'] = self._io.pos()
            self._debug['offsets']['arr'] = []
            self.offsets = []
            for i in range(self.num_instances):
                self._debug['offsets']['arr'].append({'start': self._io.pos()})
                self.offsets.append(self._io.read_u4be())
                self._debug['offsets']['arr'][i]['end'] = self._io.pos()

            self._debug['offsets']['end'] = self._io.pos()
            self._debug['names']['start'] = self._io.pos()
            self._debug['names']['arr'] = []
            self.names = []
            for i in range(self.num_instances):
                self._debug['names']['arr'].append({'start': self._io.pos()})
                self.names.append((self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8"))
                self._debug['names']['arr'][i]['end'] = self._io.pos()

            self._debug['names']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.instance_numbers)):
                pass

            for i in range(len(self.offsets)):
                pass

            for i in range(len(self.names)):
                pass



    class Label(KaitaiStruct):
        SEQ_FIELDS = ["seconds", "microseconds", "label_type", "numeric_identifier", "num_instances", "ofs_jsonb"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.Label, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['seconds']['start'] = self._io.pos()
            self.seconds = self._io.read_u4be()
            self._debug['seconds']['end'] = self._io.pos()
            self._debug['microseconds']['start'] = self._io.pos()
            self.microseconds = self._io.read_u4be()
            self._debug['microseconds']['end'] = self._io.pos()
            self._debug['label_type']['start'] = self._io.pos()
            self.label_type = KaitaiStream.resolve_enum(Pcp.LabelTypes, self._io.read_u4be())
            self._debug['label_type']['end'] = self._io.pos()
            if not  ((self.label_type == Pcp.LabelTypes.context) or (self.label_type == Pcp.LabelTypes.domain) or (self.label_type == Pcp.LabelTypes.indom) or (self.label_type == Pcp.LabelTypes.cluster) or (self.label_type == Pcp.LabelTypes.item) or (self.label_type == Pcp.LabelTypes.instances)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.label_type, self._io, u"/types/label/seq/2")
            self._debug['numeric_identifier']['start'] = self._io.pos()
            self.numeric_identifier = self._io.read_s4be()
            self._debug['numeric_identifier']['end'] = self._io.pos()
            self._debug['num_instances']['start'] = self._io.pos()
            self.num_instances = self._io.read_u4be()
            self._debug['num_instances']['end'] = self._io.pos()
            self._debug['ofs_jsonb']['start'] = self._io.pos()
            self.ofs_jsonb = self._io.read_u4be()
            self._debug['ofs_jsonb']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class LabelEntry(KaitaiStruct):
        SEQ_FIELDS = ["ofs_name", "len_name", "flags", "ofs_value", "len_value"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.LabelEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['ofs_name']['start'] = self._io.pos()
            self.ofs_name = self._io.read_u2be()
            self._debug['ofs_name']['end'] = self._io.pos()
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_u1()
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u1()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['ofs_value']['start'] = self._io.pos()
            self.ofs_value = self._io.read_u2be()
            self._debug['ofs_value']['end'] = self._io.pos()
            self._debug['len_value']['start'] = self._io.pos()
            self.len_value = self._io.read_u2be()
            self._debug['len_value']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class LabelsetEntry(KaitaiStruct):
        SEQ_FIELDS = ["instance_identifier", "len_jsonb", "num_labels", "labels"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.LabelsetEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['instance_identifier']['start'] = self._io.pos()
            self.instance_identifier = self._io.read_s4be()
            self._debug['instance_identifier']['end'] = self._io.pos()
            self._debug['len_jsonb']['start'] = self._io.pos()
            self.len_jsonb = self._io.read_u4be()
            self._debug['len_jsonb']['end'] = self._io.pos()
            self._debug['num_labels']['start'] = self._io.pos()
            self.num_labels = self._io.read_u4be()
            self._debug['num_labels']['end'] = self._io.pos()
            self._debug['labels']['start'] = self._io.pos()
            self._debug['labels']['arr'] = []
            self.labels = []
            for i in range(self.num_labels):
                self._debug['labels']['arr'].append({'start': self._io.pos()})
                self.labels.append(Pcp.LabelEntry(self._io, self, self._root))
                self._debug['labels']['arr'][i]['end'] = self._io.pos()

            self._debug['labels']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.labels)):
                pass
                self.labels[i]._fetch_instances()



    class Meta(KaitaiStruct):
        SEQ_FIELDS = ["len_record1", "meta_record", "len_record2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.Meta, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_record1']['start'] = self._io.pos()
            self.len_record1 = self._io.read_u4be()
            self._debug['len_record1']['end'] = self._io.pos()
            self._debug['meta_record']['start'] = self._io.pos()
            self._raw_meta_record = self._io.read_bytes(self.len_record1 - 4 * 2)
            _io__raw_meta_record = KaitaiStream(BytesIO(self._raw_meta_record))
            self.meta_record = Pcp.MetaRecord(_io__raw_meta_record, self, self._root)
            self._debug['meta_record']['end'] = self._io.pos()
            self._debug['len_record2']['start'] = self._io.pos()
            self.len_record2 = self._io.read_u4be()
            self._debug['len_record2']['end'] = self._io.pos()
            if not self.len_record2 == self.len_record1:
                raise kaitaistruct.ValidationNotEqualError(self.len_record1, self.len_record2, self._io, u"/types/meta/seq/2")


        def _fetch_instances(self):
            pass
            self.meta_record._fetch_instances()


    class MetaName(KaitaiStruct):
        SEQ_FIELDS = ["len_name", "name"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.MetaName, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_name']['start'] = self._io.pos()
            self.len_name = self._io.read_u4be()
            self._debug['len_name']['end'] = self._io.pos()
            self._debug['name']['start'] = self._io.pos()
            self.name = (self._io.read_bytes(self.len_name)).decode(u"UTF-8")
            self._debug['name']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class MetaRecord(KaitaiStruct):
        SEQ_FIELDS = ["tag", "record"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.MetaRecord, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tag']['start'] = self._io.pos()
            self.tag = KaitaiStream.resolve_enum(Pcp.MetaRecords, self._io.read_u4be())
            self._debug['tag']['end'] = self._io.pos()
            if not  ((self.tag == Pcp.MetaRecords.description) or (self.tag == Pcp.MetaRecords.instance_domain) or (self.tag == Pcp.MetaRecords.label) or (self.tag == Pcp.MetaRecords.text)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.tag, self._io, u"/types/meta_record/seq/0")
            self._debug['record']['start'] = self._io.pos()
            _on = self.tag
            if _on == Pcp.MetaRecords.description:
                pass
                self.record = Pcp.Description(self._io, self, self._root)
            elif _on == Pcp.MetaRecords.instance_domain:
                pass
                self.record = Pcp.InstanceDomain(self._io, self, self._root)
            elif _on == Pcp.MetaRecords.label:
                pass
                self.record = Pcp.Label(self._io, self, self._root)
            elif _on == Pcp.MetaRecords.text:
                pass
                self.record = Pcp.Text(self._io, self, self._root)
            self._debug['record']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.tag
            if _on == Pcp.MetaRecords.description:
                pass
                self.record._fetch_instances()
            elif _on == Pcp.MetaRecords.instance_domain:
                pass
                self.record._fetch_instances()
            elif _on == Pcp.MetaRecords.label:
                pass
                self.record._fetch_instances()
            elif _on == Pcp.MetaRecords.text:
                pass
                self.record._fetch_instances()


    class PmResult(KaitaiStruct):
        SEQ_FIELDS = ["event_time_seconds", "event_time_microseconds", "num_pmids", "pm_value_sets", "pm_value_blocks"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.PmResult, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['event_time_seconds']['start'] = self._io.pos()
            self.event_time_seconds = self._io.read_u4be()
            self._debug['event_time_seconds']['end'] = self._io.pos()
            self._debug['event_time_microseconds']['start'] = self._io.pos()
            self.event_time_microseconds = self._io.read_u4be()
            self._debug['event_time_microseconds']['end'] = self._io.pos()
            self._debug['num_pmids']['start'] = self._io.pos()
            self.num_pmids = self._io.read_u4be()
            self._debug['num_pmids']['end'] = self._io.pos()
            self._debug['pm_value_sets']['start'] = self._io.pos()
            self._debug['pm_value_sets']['arr'] = []
            self.pm_value_sets = []
            for i in range(self.num_pmids):
                self._debug['pm_value_sets']['arr'].append({'start': self._io.pos()})
                self.pm_value_sets.append(Pcp.PmValueSet(self._io, self, self._root))
                self._debug['pm_value_sets']['arr'][i]['end'] = self._io.pos()

            self._debug['pm_value_sets']['end'] = self._io.pos()
            self._debug['pm_value_blocks']['start'] = self._io.pos()
            self._debug['pm_value_blocks']['arr'] = []
            self.pm_value_blocks = []
            for i in range(self.num_pmids):
                self._debug['pm_value_blocks']['arr'].append({'start': self._io.pos()})
                self.pm_value_blocks.append(Pcp.PmValueBlock(self._io, self, self._root))
                self._debug['pm_value_blocks']['arr'][i]['end'] = self._io.pos()

            self._debug['pm_value_blocks']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.pm_value_sets)):
                pass
                self.pm_value_sets[i]._fetch_instances()

            for i in range(len(self.pm_value_blocks)):
                pass
                self.pm_value_blocks[i]._fetch_instances()



    class PmValue(KaitaiStruct):
        SEQ_FIELDS = ["number_in_instance_domain", "value_or_offset"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.PmValue, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['number_in_instance_domain']['start'] = self._io.pos()
            self.number_in_instance_domain = self._io.read_u4be()
            self._debug['number_in_instance_domain']['end'] = self._io.pos()
            self._debug['value_or_offset']['start'] = self._io.pos()
            self.value_or_offset = self._io.read_u4be()
            self._debug['value_or_offset']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PmValueBlock(KaitaiStruct):
        SEQ_FIELDS = ["value_type", "len_subrecord", "data", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.PmValueBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value_type']['start'] = self._io.pos()
            self.value_type = self._io.read_u1()
            self._debug['value_type']['end'] = self._io.pos()
            self._debug['len_subrecord']['start'] = self._io.pos()
            self.len_subrecord = self._io.read_bits_int_be(24)
            self._debug['len_subrecord']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes((self.len_subrecord - 1) - 3)
            self._debug['data']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self.len_subrecord) % 4)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PmValueSet(KaitaiStruct):
        SEQ_FIELDS = ["pmid", "num_values", "storage_mode", "pm_values"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.PmValueSet, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['pmid']['start'] = self._io.pos()
            self.pmid = self._io.read_u4be()
            self._debug['pmid']['end'] = self._io.pos()
            self._debug['num_values']['start'] = self._io.pos()
            self.num_values = self._io.read_u4be()
            self._debug['num_values']['end'] = self._io.pos()
            self._debug['storage_mode']['start'] = self._io.pos()
            self.storage_mode = self._io.read_u4be()
            self._debug['storage_mode']['end'] = self._io.pos()
            self._debug['pm_values']['start'] = self._io.pos()
            self._debug['pm_values']['arr'] = []
            self.pm_values = []
            for i in range(self.num_values):
                self._debug['pm_values']['arr'].append({'start': self._io.pos()})
                self.pm_values.append(Pcp.PmValue(self._io, self, self._root))
                self._debug['pm_values']['arr'][i]['end'] = self._io.pos()

            self._debug['pm_values']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.pm_values)):
                pass
                self.pm_values[i]._fetch_instances()



    class Text(KaitaiStruct):
        SEQ_FIELDS = ["identifier_type", "numeric_identifier", "text"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcp.Text, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['identifier_type']['start'] = self._io.pos()
            self.identifier_type = self._io.read_u4be()
            self._debug['identifier_type']['end'] = self._io.pos()
            self._debug['numeric_identifier']['start'] = self._io.pos()
            self.numeric_identifier = self._io.read_u4be()
            self._debug['numeric_identifier']['end'] = self._io.pos()
            self._debug['text']['start'] = self._io.pos()
            self.text = (KaitaiStream.bytes_terminate(self._io.read_bytes_full(), 0, False)).decode(u"UTF-8")
            self._debug['text']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



