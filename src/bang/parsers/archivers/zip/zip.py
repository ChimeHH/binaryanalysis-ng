# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Zip(KaitaiStruct):
    """ZIP is a popular archive file format, introduced in 1989 by Phil Katz
    and originally implemented in PKZIP utility by PKWARE.
    
    Thanks to solid support of it in most desktop environments and
    operating systems, and algorithms / specs availability in public
    domain, it quickly became tool of choice for implementing file
    containers.
    
    For example, Java .jar files, OpenDocument, Office Open XML, EPUB files
    are actually ZIP archives.
    
    .. seealso::
       Source - https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
    
    
    .. seealso::
       Source - https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html
    """

    class Compression(IntEnum):
        none = 0
        shrunk = 1
        reduced_1 = 2
        reduced_2 = 3
        reduced_3 = 4
        reduced_4 = 5
        imploded = 6
        deflated = 8
        enhanced_deflated = 9
        pkware_dcl_imploded = 10
        bzip2 = 12
        lzma = 14
        ibm_terse = 18
        ibm_lz77_z = 19
        zstandard = 93
        mp3 = 94
        xz = 95
        jpeg = 96
        wavpack = 97
        ppmd = 98
        aex_encryption_marker = 99

    class ExtraCodes(IntEnum):
        zip64 = 1
        av_info = 7
        os2 = 9
        ntfs = 10
        openvms = 12
        pkware_unix = 13
        file_stream_and_fork_descriptors = 14
        patch_descriptor = 15
        pkcs7 = 20
        x509_cert_id_and_signature_for_file = 21
        x509_cert_id_for_central_dir = 22
        strong_encryption_header = 23
        record_management_controls = 24
        pkcs7_enc_recip_cert_list = 25
        reserved_for_timestamp = 32
        policy_decryption_key = 33
        smartcrypt_key_provider = 34
        smartcrypt_policy_key_data = 35
        ibm_s390_uncomp = 101
        ibm_s390_comp = 102
        minizip_ng_sign = 4293
        usd = 6534
        minizip_ng_hash = 6737
        poszip_4690 = 18064
        extended_timestamp = 21589
        xceed_unicode = 21838
        keyvaluepairs = 22091
        infozip_unix_old = 22613
        ziparchive_unicode = 23116
        ziparchive_seekable = 23117
        beos = 25922
        infozip_unicode_path = 28789
        asi_unix = 30062
        infozip_unix = 30805
        infozip_unix_var_size = 30837
        aex_encryption = 39169
        apache_commons_compress = 41246
        microsoft_open_packaging_growth_hint = 41504
        java_jar = 51966
        minizip_ng_central_directory = 52685
        zip_align = 55605
        alzip_code_page = 58746
        sms_qdos = 64842

    class SectionTypes(IntEnum):
        central_dir_entry = 33639248
        dahua_local_file = 67323972
        local_file = 67324752
        digital_signature = 84233040
        end_of_central_dir = 101010256
        zip64_end_of_central_dir = 101075792
        instar_local_file = 117656400
        zip64_end_of_central_dir_locator = 117853008
        instar_central_dir_entry = 134302544
        archive_extra_data = 134630224
        data_descriptor = 134695760
        instar_end_of_central_dir = 151341904

    class VersionMapping(IntEnum):
        msdos = 0
        amiga = 1
        openvms = 2
        unix = 3
        vm_cms = 4
        atari_st = 5
        os2_hpfs = 6
        macintosh = 7
        z_system = 8
        cp_m = 9
        windows_ntfs = 10
        mvs = 11
        vse = 12
        acorn_risc = 13
        vfat = 14
        alternate_mvs = 15
        beos = 16
        tandem = 17
        os_400 = 18
        os_x = 19
    SEQ_FIELDS = ["sections"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Zip, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['sections']['start'] = self._io.pos()
        self._debug['sections']['arr'] = []
        self.sections = []
        i = 0
        while True:
            self._debug['sections']['arr'].append({'start': self._io.pos()})
            _ = Zip.PkSection(self._io, self, self._root)
            self.sections.append(_)
            self._debug['sections']['arr'][len(self.sections) - 1]['end'] = self._io.pos()
            if  ((_.section_type == Zip.SectionTypes.end_of_central_dir) or (_.section_type == Zip.SectionTypes.instar_end_of_central_dir)) :
                break
            i += 1
        self._debug['sections']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.sections)):
            pass
            self.sections[i]._fetch_instances()


    class ArchiveExtraData(KaitaiStruct):
        SEQ_FIELDS = ["len_extra_field", "data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.ArchiveExtraData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_extra_field']['start'] = self._io.pos()
            self.len_extra_field = self._io.read_u4le()
            self._debug['len_extra_field']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_extra_field)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class CentralDirEntry(KaitaiStruct):
        """
        .. seealso::
           - 4.3.12 - https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
        """
        SEQ_FIELDS = ["version_made_by", "version_needed_to_extract", "flags", "compression_method", "file_mod_time", "crc32", "len_body_compressed", "len_body_uncompressed", "len_file_name", "len_extra", "len_comment", "disk_number_start", "int_file_attr", "ext_file_attr", "ofs_local_header", "file_name", "extra", "comment"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.CentralDirEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version_made_by']['start'] = self._io.pos()
            self.version_made_by = Zip.Version(self._io, self, self._root)
            self._debug['version_made_by']['end'] = self._io.pos()
            self._debug['version_needed_to_extract']['start'] = self._io.pos()
            self.version_needed_to_extract = Zip.Version(self._io, self, self._root)
            self._debug['version_needed_to_extract']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u2le()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['compression_method']['start'] = self._io.pos()
            self.compression_method = KaitaiStream.resolve_enum(Zip.Compression, self._io.read_u2le())
            self._debug['compression_method']['end'] = self._io.pos()
            self._debug['file_mod_time']['start'] = self._io.pos()
            self.file_mod_time = self._io.read_bytes(4)
            self._debug['file_mod_time']['end'] = self._io.pos()
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['len_body_compressed']['start'] = self._io.pos()
            self.len_body_compressed = self._io.read_u4le()
            self._debug['len_body_compressed']['end'] = self._io.pos()
            self._debug['len_body_uncompressed']['start'] = self._io.pos()
            self.len_body_uncompressed = self._io.read_u4le()
            self._debug['len_body_uncompressed']['end'] = self._io.pos()
            self._debug['len_file_name']['start'] = self._io.pos()
            self.len_file_name = self._io.read_u2le()
            self._debug['len_file_name']['end'] = self._io.pos()
            self._debug['len_extra']['start'] = self._io.pos()
            self.len_extra = self._io.read_u2le()
            self._debug['len_extra']['end'] = self._io.pos()
            self._debug['len_comment']['start'] = self._io.pos()
            self.len_comment = self._io.read_u2le()
            self._debug['len_comment']['end'] = self._io.pos()
            self._debug['disk_number_start']['start'] = self._io.pos()
            self.disk_number_start = self._io.read_u2le()
            self._debug['disk_number_start']['end'] = self._io.pos()
            self._debug['int_file_attr']['start'] = self._io.pos()
            self.int_file_attr = self._io.read_u2le()
            self._debug['int_file_attr']['end'] = self._io.pos()
            self._debug['ext_file_attr']['start'] = self._io.pos()
            self.ext_file_attr = self._io.read_u4le()
            self._debug['ext_file_attr']['end'] = self._io.pos()
            self._debug['ofs_local_header']['start'] = self._io.pos()
            self.ofs_local_header = self._io.read_s4le()
            self._debug['ofs_local_header']['end'] = self._io.pos()
            self._debug['file_name']['start'] = self._io.pos()
            self.file_name = (self._io.read_bytes(self.len_file_name)).decode(u"UTF-8")
            self._debug['file_name']['end'] = self._io.pos()
            self._debug['extra']['start'] = self._io.pos()
            _on = self.has_padding
            if _on == False:
                pass
                self._raw_extra = self._io.read_bytes(self.len_extra)
                _io__raw_extra = KaitaiStream(BytesIO(self._raw_extra))
                self.extra = Zip.Extras(Zip.SectionTypes.central_dir_entry, _io__raw_extra, self, self._root)
            elif _on == True:
                pass
                self._raw_extra = self._io.read_bytes(self.len_extra)
                _io__raw_extra = KaitaiStream(BytesIO(self._raw_extra))
                self.extra = Zip.Empty(_io__raw_extra, self, self._root)
            else:
                pass
                self.extra = self._io.read_bytes(self.len_extra)
            self._debug['extra']['end'] = self._io.pos()
            self._debug['comment']['start'] = self._io.pos()
            self.comment = self._io.read_bytes(self.len_comment)
            self._debug['comment']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.version_made_by._fetch_instances()
            self.version_needed_to_extract._fetch_instances()
            _on = self.has_padding
            if _on == False:
                pass
                self.extra._fetch_instances()
            elif _on == True:
                pass
                self.extra._fetch_instances()
            else:
                pass
            _ = self.local_header
            if hasattr(self, '_m_local_header'):
                pass
                self._m_local_header._fetch_instances()


        @property
        def has_padding(self):
            if hasattr(self, '_m_has_padding'):
                return self._m_has_padding

            self._m_has_padding = self.len_extra < 4
            return getattr(self, '_m_has_padding', None)

        @property
        def local_header(self):
            if hasattr(self, '_m_local_header'):
                return self._m_local_header

            _pos = self._io.pos()
            self._io.seek(self.ofs_local_header)
            self._debug['_m_local_header']['start'] = self._io.pos()
            self._m_local_header = Zip.PkSection(self._io, self, self._root)
            self._debug['_m_local_header']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_local_header', None)


    class DataDescriptor(KaitaiStruct):
        SEQ_FIELDS = ["crc32", "len_body_compressed", "len_body_uncompressed"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.DataDescriptor, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['len_body_compressed']['start'] = self._io.pos()
            self.len_body_compressed = self._io.read_u4le()
            self._debug['len_body_compressed']['end'] = self._io.pos()
            self._debug['len_body_uncompressed']['start'] = self._io.pos()
            self.len_body_uncompressed = self._io.read_u4le()
            self._debug['len_body_uncompressed']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class DataDescriptor64(KaitaiStruct):
        SEQ_FIELDS = ["crc32", "len_body_compressed", "len_body_uncompressed"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.DataDescriptor64, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['len_body_compressed']['start'] = self._io.pos()
            self.len_body_compressed = self._io.read_u8le()
            self._debug['len_body_compressed']['end'] = self._io.pos()
            self._debug['len_body_uncompressed']['start'] = self._io.pos()
            self.len_body_uncompressed = self._io.read_u8le()
            self._debug['len_body_uncompressed']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class DigitalSignature(KaitaiStruct):
        SEQ_FIELDS = ["len_signature", "signature"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.DigitalSignature, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_signature']['start'] = self._io.pos()
            self.len_signature = self._io.read_u2le()
            self._debug['len_signature']['end'] = self._io.pos()
            self._debug['signature']['start'] = self._io.pos()
            self.signature = self._io.read_bytes(self.len_signature)
            self._debug['signature']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Empty(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.Empty, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass


    class EndOfCentralDir(KaitaiStruct):
        SEQ_FIELDS = ["disk_of_end_of_central_dir", "disk_of_central_dir", "num_central_dir_entries_on_disk", "num_central_dir_entries_total", "len_central_dir", "ofs_central_dir", "len_comment", "comment"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.EndOfCentralDir, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['disk_of_end_of_central_dir']['start'] = self._io.pos()
            self.disk_of_end_of_central_dir = self._io.read_u2le()
            self._debug['disk_of_end_of_central_dir']['end'] = self._io.pos()
            self._debug['disk_of_central_dir']['start'] = self._io.pos()
            self.disk_of_central_dir = self._io.read_u2le()
            self._debug['disk_of_central_dir']['end'] = self._io.pos()
            self._debug['num_central_dir_entries_on_disk']['start'] = self._io.pos()
            self.num_central_dir_entries_on_disk = self._io.read_u2le()
            self._debug['num_central_dir_entries_on_disk']['end'] = self._io.pos()
            self._debug['num_central_dir_entries_total']['start'] = self._io.pos()
            self.num_central_dir_entries_total = self._io.read_u2le()
            self._debug['num_central_dir_entries_total']['end'] = self._io.pos()
            self._debug['len_central_dir']['start'] = self._io.pos()
            self.len_central_dir = self._io.read_u4le()
            self._debug['len_central_dir']['end'] = self._io.pos()
            self._debug['ofs_central_dir']['start'] = self._io.pos()
            self.ofs_central_dir = self._io.read_u4le()
            self._debug['ofs_central_dir']['end'] = self._io.pos()
            self._debug['len_comment']['start'] = self._io.pos()
            self.len_comment = self._io.read_u2le()
            self._debug['len_comment']['end'] = self._io.pos()
            self._debug['comment']['start'] = self._io.pos()
            self.comment = self._io.read_bytes(self.len_comment)
            self._debug['comment']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class ExtraField(KaitaiStruct):
        SEQ_FIELDS = ["code", "len_body", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.ExtraField, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['code']['start'] = self._io.pos()
            self.code = KaitaiStream.resolve_enum(Zip.ExtraCodes, self._io.read_u2le())
            self._debug['code']['end'] = self._io.pos()
            self._debug['len_body']['start'] = self._io.pos()
            self.len_body = self._io.read_u2le()
            self._debug['len_body']['end'] = self._io.pos()
            self._debug['body']['start'] = self._io.pos()
            _on = self.code
            if _on == Zip.ExtraCodes.aex_encryption:
                pass
                self._raw_body = self._io.read_bytes(self.len_body)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Zip.ExtraField.AexEncryption(_io__raw_body, self, self._root)
            elif _on == Zip.ExtraCodes.alzip_code_page:
                pass
                self._raw_body = self._io.read_bytes(self.len_body)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Zip.ExtraField.AlzipCodePage(_io__raw_body, self, self._root)
            elif _on == Zip.ExtraCodes.extended_timestamp:
                pass
                self._raw_body = self._io.read_bytes(self.len_body)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Zip.ExtraField.ExtendedTimestamp(_io__raw_body, self, self._root)
            elif _on == Zip.ExtraCodes.infozip_unicode_path:
                pass
                self._raw_body = self._io.read_bytes(self.len_body)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Zip.ExtraField.InfozipUnicodePath(_io__raw_body, self, self._root)
            elif _on == Zip.ExtraCodes.infozip_unix_var_size:
                pass
                self._raw_body = self._io.read_bytes(self.len_body)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Zip.ExtraField.InfozipUnixVarSize(_io__raw_body, self, self._root)
            elif _on == Zip.ExtraCodes.minizip_ng_hash:
                pass
                self._raw_body = self._io.read_bytes(self.len_body)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Zip.ExtraField.MinizipNgHash(_io__raw_body, self, self._root)
            elif _on == Zip.ExtraCodes.ntfs:
                pass
                self._raw_body = self._io.read_bytes(self.len_body)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Zip.ExtraField.Ntfs(_io__raw_body, self, self._root)
            elif _on == Zip.ExtraCodes.xceed_unicode:
                pass
                self._raw_body = self._io.read_bytes(self.len_body)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Zip.ExtraField.XceedUnicode(_io__raw_body, self, self._root)
            else:
                pass
                self.body = self._io.read_bytes(self.len_body)
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.code
            if _on == Zip.ExtraCodes.aex_encryption:
                pass
                self.body._fetch_instances()
            elif _on == Zip.ExtraCodes.alzip_code_page:
                pass
                self.body._fetch_instances()
            elif _on == Zip.ExtraCodes.extended_timestamp:
                pass
                self.body._fetch_instances()
            elif _on == Zip.ExtraCodes.infozip_unicode_path:
                pass
                self.body._fetch_instances()
            elif _on == Zip.ExtraCodes.infozip_unix_var_size:
                pass
                self.body._fetch_instances()
            elif _on == Zip.ExtraCodes.minizip_ng_hash:
                pass
                self.body._fetch_instances()
            elif _on == Zip.ExtraCodes.ntfs:
                pass
                self.body._fetch_instances()
            elif _on == Zip.ExtraCodes.xceed_unicode:
                pass
                self.body._fetch_instances()
            else:
                pass

        class AexEncryption(KaitaiStruct):
            """
            .. seealso::
               Source - http://www.winzip.com/aes_info.htm
            """

            class Encryption(IntEnum):
                bit_128 = 1
                bit_192 = 2
                bit_256 = 3
            SEQ_FIELDS = ["version_number", "vendor_id", "encryption_strength", "compression_method"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.ExtraField.AexEncryption, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['version_number']['start'] = self._io.pos()
                self.version_number = self._io.read_u2le()
                self._debug['version_number']['end'] = self._io.pos()
                self._debug['vendor_id']['start'] = self._io.pos()
                self.vendor_id = self._io.read_bytes(2)
                self._debug['vendor_id']['end'] = self._io.pos()
                self._debug['encryption_strength']['start'] = self._io.pos()
                self.encryption_strength = KaitaiStream.resolve_enum(Zip.ExtraField.AexEncryption.Encryption, self._io.read_u1())
                self._debug['encryption_strength']['end'] = self._io.pos()
                self._debug['compression_method']['start'] = self._io.pos()
                self.compression_method = KaitaiStream.resolve_enum(Zip.Compression, self._io.read_u2le())
                self._debug['compression_method']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class AlzipCodePage(KaitaiStruct):
            """
            .. seealso::
               Source - https://github.com/icsharpcode/SharpZipLib/issues/657
            """
            SEQ_FIELDS = ["code_page"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.ExtraField.AlzipCodePage, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['code_page']['start'] = self._io.pos()
                self.code_page = self._io.read_u4le()
                self._debug['code_page']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class ExtendedTimestamp(KaitaiStruct):
            """
            .. seealso::
               Source - https://github.com/LuaDist/zip/blob/b710806/proginfo/extrafld.txt#L817
            """
            SEQ_FIELDS = ["flags"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.ExtraField.ExtendedTimestamp, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['flags']['start'] = self._io.pos()
                self._raw_flags = self._io.read_bytes(1)
                _io__raw_flags = KaitaiStream(BytesIO(self._raw_flags))
                self.flags = Zip.ExtraField.ExtendedTimestamp.InfoFlags(_io__raw_flags, self, self._root)
                self._debug['flags']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.flags._fetch_instances()

            class InfoFlags(KaitaiStruct):
                SEQ_FIELDS = ["has_mod_time", "has_access_time", "has_create_time", "reserved"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Zip.ExtraField.ExtendedTimestamp.InfoFlags, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['has_mod_time']['start'] = self._io.pos()
                    self.has_mod_time = self._io.read_bits_int_le(1) != 0
                    self._debug['has_mod_time']['end'] = self._io.pos()
                    self._debug['has_access_time']['start'] = self._io.pos()
                    self.has_access_time = self._io.read_bits_int_le(1) != 0
                    self._debug['has_access_time']['end'] = self._io.pos()
                    self._debug['has_create_time']['start'] = self._io.pos()
                    self.has_create_time = self._io.read_bits_int_le(1) != 0
                    self._debug['has_create_time']['end'] = self._io.pos()
                    self._debug['reserved']['start'] = self._io.pos()
                    self.reserved = self._io.read_bits_int_le(5)
                    self._debug['reserved']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass



        class InfozipUnicodePath(KaitaiStruct):
            SEQ_FIELDS = ["version", "crc32", "name"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.ExtraField.InfozipUnicodePath, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['version']['start'] = self._io.pos()
                self.version = self._io.read_u1()
                self._debug['version']['end'] = self._io.pos()
                self._debug['crc32']['start'] = self._io.pos()
                self.crc32 = self._io.read_u4le()
                self._debug['crc32']['end'] = self._io.pos()
                self._debug['name']['start'] = self._io.pos()
                self.name = (self._io.read_bytes_full()).decode(u"UTF-8")
                self._debug['name']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class InfozipUnixVarSize(KaitaiStruct):
            """
            .. seealso::
               Source - https://github.com/LuaDist/zip/blob/b710806/proginfo/extrafld.txt#L1339
            """
            SEQ_FIELDS = ["version", "len_uid", "uid", "len_gid", "gid"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.ExtraField.InfozipUnixVarSize, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['version']['start'] = self._io.pos()
                self.version = self._io.read_u1()
                self._debug['version']['end'] = self._io.pos()
                self._debug['len_uid']['start'] = self._io.pos()
                self.len_uid = self._io.read_u1()
                self._debug['len_uid']['end'] = self._io.pos()
                self._debug['uid']['start'] = self._io.pos()
                self.uid = self._io.read_bytes(self.len_uid)
                self._debug['uid']['end'] = self._io.pos()
                self._debug['len_gid']['start'] = self._io.pos()
                self.len_gid = self._io.read_u1()
                self._debug['len_gid']['end'] = self._io.pos()
                self._debug['gid']['start'] = self._io.pos()
                self.gid = self._io.read_bytes(self.len_gid)
                self._debug['gid']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class Keyvaluepairs(KaitaiStruct):
            SEQ_FIELDS = ["len_payload", "payload"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.ExtraField.Keyvaluepairs, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['len_payload']['start'] = self._io.pos()
                self.len_payload = self._io.read_u2le()
                self._debug['len_payload']['end'] = self._io.pos()
                self._debug['payload']['start'] = self._io.pos()
                self._raw_payload = self._io.read_bytes(self.len_payload)
                _io__raw_payload = KaitaiStream(BytesIO(self._raw_payload))
                self.payload = Zip.ExtraField.Keyvaluepairs.Payload(_io__raw_payload, self, self._root)
                self._debug['payload']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.payload._fetch_instances()

            class Keyvaluepair(KaitaiStruct):
                SEQ_FIELDS = ["len_key", "key", "len_value", "value"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Zip.ExtraField.Keyvaluepairs.Keyvaluepair, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['len_key']['start'] = self._io.pos()
                    self.len_key = self._io.read_u2le()
                    self._debug['len_key']['end'] = self._io.pos()
                    self._debug['key']['start'] = self._io.pos()
                    self.key = (self._io.read_bytes(self.len_key)).decode(u"UTF-8")
                    self._debug['key']['end'] = self._io.pos()
                    self._debug['len_value']['start'] = self._io.pos()
                    self.len_value = self._io.read_u2le()
                    self._debug['len_value']['end'] = self._io.pos()
                    self._debug['value']['start'] = self._io.pos()
                    self.value = (self._io.read_bytes(self.len_value)).decode(u"UTF-8")
                    self._debug['value']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass


            class Payload(KaitaiStruct):
                SEQ_FIELDS = ["signature", "num_keyvaluepairs", "keyvaluepairs"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Zip.ExtraField.Keyvaluepairs.Payload, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['signature']['start'] = self._io.pos()
                    self.signature = self._io.read_bytes(13)
                    self._debug['signature']['end'] = self._io.pos()
                    if not self.signature == b"\x4B\x65\x79\x56\x61\x6C\x75\x65\x50\x61\x69\x72\x73":
                        raise kaitaistruct.ValidationNotEqualError(b"\x4B\x65\x79\x56\x61\x6C\x75\x65\x50\x61\x69\x72\x73", self.signature, self._io, u"/types/extra_field/types/keyvaluepairs/types/payload/seq/0")
                    self._debug['num_keyvaluepairs']['start'] = self._io.pos()
                    self.num_keyvaluepairs = self._io.read_u1()
                    self._debug['num_keyvaluepairs']['end'] = self._io.pos()
                    self._debug['keyvaluepairs']['start'] = self._io.pos()
                    self._debug['keyvaluepairs']['arr'] = []
                    self.keyvaluepairs = []
                    for i in range(self.num_keyvaluepairs):
                        self._debug['keyvaluepairs']['arr'].append({'start': self._io.pos()})
                        self.keyvaluepairs.append(Zip.ExtraField.Keyvaluepairs.Keyvaluepair(self._io, self, self._root))
                        self._debug['keyvaluepairs']['arr'][i]['end'] = self._io.pos()

                    self._debug['keyvaluepairs']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    for i in range(len(self.keyvaluepairs)):
                        pass
                        self.keyvaluepairs[i]._fetch_instances()




        class MinizipNgHash(KaitaiStruct):
            """
            .. seealso::
               Source - https://github.com/zlib-ng/minizip-ng/blob/3da04514/doc/mz_extrafield.md
            
            
            .. seealso::
               Source - https://github.com/zlib-ng/minizip-ng/blob/3da04514cd51b75a325565393ba31ff719d7f5f2/mz.h#L124
            """

            class MinizipNgHashAlgorithms(IntEnum):
                md5 = 10
                sha1 = 20
                sha224 = 22
                sha256 = 23
                sha384 = 24
                sha512 = 25
            SEQ_FIELDS = ["algorithm", "len_digest", "digest"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.ExtraField.MinizipNgHash, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['algorithm']['start'] = self._io.pos()
                self.algorithm = KaitaiStream.resolve_enum(Zip.ExtraField.MinizipNgHash.MinizipNgHashAlgorithms, self._io.read_u2le())
                self._debug['algorithm']['end'] = self._io.pos()
                self._debug['len_digest']['start'] = self._io.pos()
                self.len_digest = self._io.read_u2le()
                self._debug['len_digest']['end'] = self._io.pos()
                self._debug['digest']['start'] = self._io.pos()
                self.digest = self._io.read_bytes(self.len_digest)
                self._debug['digest']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class Ntfs(KaitaiStruct):
            """
            .. seealso::
               Source - https://github.com/LuaDist/zip/blob/b710806/proginfo/extrafld.txt#L191
            """
            SEQ_FIELDS = ["reserved", "attributes"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.ExtraField.Ntfs, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['reserved']['start'] = self._io.pos()
                self.reserved = self._io.read_u4le()
                self._debug['reserved']['end'] = self._io.pos()
                self._debug['attributes']['start'] = self._io.pos()
                self._debug['attributes']['arr'] = []
                self.attributes = []
                i = 0
                while not self._io.is_eof():
                    self._debug['attributes']['arr'].append({'start': self._io.pos()})
                    self.attributes.append(Zip.ExtraField.Ntfs.Attribute(self._io, self, self._root))
                    self._debug['attributes']['arr'][len(self.attributes) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['attributes']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.attributes)):
                    pass
                    self.attributes[i]._fetch_instances()


            class Attribute(KaitaiStruct):
                SEQ_FIELDS = ["tag", "len_body", "body"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Zip.ExtraField.Ntfs.Attribute, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['tag']['start'] = self._io.pos()
                    self.tag = self._io.read_u2le()
                    self._debug['tag']['end'] = self._io.pos()
                    self._debug['len_body']['start'] = self._io.pos()
                    self.len_body = self._io.read_u2le()
                    self._debug['len_body']['end'] = self._io.pos()
                    self._debug['body']['start'] = self._io.pos()
                    _on = self.tag
                    if _on == 1:
                        pass
                        self._raw_body = self._io.read_bytes(self.len_body)
                        _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                        self.body = Zip.ExtraField.Ntfs.Attribute1(_io__raw_body, self, self._root)
                    else:
                        pass
                        self.body = self._io.read_bytes(self.len_body)
                    self._debug['body']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    _on = self.tag
                    if _on == 1:
                        pass
                        self.body._fetch_instances()
                    else:
                        pass


            class Attribute1(KaitaiStruct):
                SEQ_FIELDS = ["last_mod_time", "last_access_time", "creation_time"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Zip.ExtraField.Ntfs.Attribute1, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['last_mod_time']['start'] = self._io.pos()
                    self.last_mod_time = self._io.read_u8le()
                    self._debug['last_mod_time']['end'] = self._io.pos()
                    self._debug['last_access_time']['start'] = self._io.pos()
                    self.last_access_time = self._io.read_u8le()
                    self._debug['last_access_time']['end'] = self._io.pos()
                    self._debug['creation_time']['start'] = self._io.pos()
                    self.creation_time = self._io.read_u8le()
                    self._debug['creation_time']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass



        class XceedUnicode(KaitaiStruct):
            SEQ_FIELDS = ["magic", "num_characters", "data"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.ExtraField.XceedUnicode, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['magic']['start'] = self._io.pos()
                self.magic = self._io.read_bytes(4)
                self._debug['magic']['end'] = self._io.pos()
                if not self.magic == b"\x4E\x55\x43\x58":
                    raise kaitaistruct.ValidationNotEqualError(b"\x4E\x55\x43\x58", self.magic, self._io, u"/types/extra_field/types/xceed_unicode/seq/0")
                self._debug['num_characters']['start'] = self._io.pos()
                self.num_characters = self._io.read_u2le()
                self._debug['num_characters']['end'] = self._io.pos()
                self._debug['data']['start'] = self._io.pos()
                self.data = (self._io.read_bytes_full()).decode(u"UTF-16LE")
                self._debug['data']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class Zip64(KaitaiStruct):
            SEQ_FIELDS = ["len_original", "len_compressed", "ofs_relative_header", "disk_start_number"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.ExtraField.Zip64, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['len_original']['start'] = self._io.pos()
                self.len_original = self._io.read_u8le()
                self._debug['len_original']['end'] = self._io.pos()
                self._debug['len_compressed']['start'] = self._io.pos()
                self.len_compressed = self._io.read_u8le()
                self._debug['len_compressed']['end'] = self._io.pos()
                self._debug['ofs_relative_header']['start'] = self._io.pos()
                self.ofs_relative_header = self._io.read_u8le()
                self._debug['ofs_relative_header']['end'] = self._io.pos()
                self._debug['disk_start_number']['start'] = self._io.pos()
                self.disk_start_number = self._io.read_u4le()
                self._debug['disk_start_number']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass



    class Extras(KaitaiStruct):
        SEQ_FIELDS = ["entries"]
        def __init__(self, type, _io, _parent=None, _root=None):
            super(Zip.Extras, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.type = type
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['entries']['start'] = self._io.pos()
            self._debug['entries']['arr'] = []
            self.entries = []
            i = 0
            while True:
                self._debug['entries']['arr'].append({'start': self._io.pos()})
                _ = Zip.ExtraField(self._io, self, self._root)
                self.entries.append(_)
                self._debug['entries']['arr'][len(self.entries) - 1]['end'] = self._io.pos()
                if  ((self._io.is_eof()) or (self._io.size() - self._io.pos() < 4)) :
                    break
                i += 1
            self._debug['entries']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.entries)):
                pass
                self.entries[i]._fetch_instances()



    class LocalFile(KaitaiStruct):
        SEQ_FIELDS = ["header", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.LocalFile, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header']['start'] = self._io.pos()
            self.header = Zip.LocalFileHeader(self._io, self, self._root)
            self._debug['header']['end'] = self._io.pos()
            if self.header.len_body_compressed != 4294967295:
                pass
                self._debug['body']['start'] = self._io.pos()
                self.body = self._io.read_bytes(self.header.len_body_compressed)
                self._debug['body']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.header._fetch_instances()
            if self.header.len_body_compressed != 4294967295:
                pass



    class LocalFileHeader(KaitaiStruct):
        SEQ_FIELDS = ["version", "flags", "compression_method", "file_mod_time", "crc32", "len_body_compressed", "len_body_uncompressed", "len_file_name", "len_extra", "file_name", "extra"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.LocalFileHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = Zip.Version(self._io, self, self._root)
            self._debug['version']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self._raw_flags = self._io.read_bytes(2)
            _io__raw_flags = KaitaiStream(BytesIO(self._raw_flags))
            self.flags = Zip.LocalFileHeader.GpFlags(_io__raw_flags, self, self._root)
            self._debug['flags']['end'] = self._io.pos()
            self._debug['compression_method']['start'] = self._io.pos()
            self.compression_method = KaitaiStream.resolve_enum(Zip.Compression, self._io.read_u2le())
            self._debug['compression_method']['end'] = self._io.pos()
            self._debug['file_mod_time']['start'] = self._io.pos()
            self.file_mod_time = self._io.read_bytes(4)
            self._debug['file_mod_time']['end'] = self._io.pos()
            self._debug['crc32']['start'] = self._io.pos()
            self.crc32 = self._io.read_u4le()
            self._debug['crc32']['end'] = self._io.pos()
            self._debug['len_body_compressed']['start'] = self._io.pos()
            self.len_body_compressed = self._io.read_u4le()
            self._debug['len_body_compressed']['end'] = self._io.pos()
            self._debug['len_body_uncompressed']['start'] = self._io.pos()
            self.len_body_uncompressed = self._io.read_u4le()
            self._debug['len_body_uncompressed']['end'] = self._io.pos()
            self._debug['len_file_name']['start'] = self._io.pos()
            self.len_file_name = self._io.read_u2le()
            self._debug['len_file_name']['end'] = self._io.pos()
            self._debug['len_extra']['start'] = self._io.pos()
            self.len_extra = self._io.read_u2le()
            self._debug['len_extra']['end'] = self._io.pos()
            self._debug['file_name']['start'] = self._io.pos()
            self.file_name = (self._io.read_bytes(self.len_file_name)).decode(u"UTF-8")
            self._debug['file_name']['end'] = self._io.pos()
            self._debug['extra']['start'] = self._io.pos()
            _on = self.has_padding
            if _on == False:
                pass
                self._raw_extra = self._io.read_bytes(self.len_extra)
                _io__raw_extra = KaitaiStream(BytesIO(self._raw_extra))
                self.extra = Zip.Extras(Zip.SectionTypes.local_file, _io__raw_extra, self, self._root)
            elif _on == True:
                pass
                self._raw_extra = self._io.read_bytes(self.len_extra)
                _io__raw_extra = KaitaiStream(BytesIO(self._raw_extra))
                self.extra = Zip.Empty(_io__raw_extra, self, self._root)
            else:
                pass
                self.extra = self._io.read_bytes(self.len_extra)
            self._debug['extra']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.version._fetch_instances()
            self.flags._fetch_instances()
            _on = self.has_padding
            if _on == False:
                pass
                self.extra._fetch_instances()
            elif _on == True:
                pass
                self.extra._fetch_instances()
            else:
                pass

        class GpFlags(KaitaiStruct):
            """
            .. seealso::
               - 4.4.4 - https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
            
            
            .. seealso::
               Local file headers - https://users.cs.jmu.edu/buchhofp/forensics/formats/pkzip.html
            """

            class DeflateMode(IntEnum):
                normal = 0
                maximum = 1
                fast = 2
                super_fast = 3
            SEQ_FIELDS = ["file_encrypted", "comp_options_raw", "has_data_descriptor", "reserved_1", "comp_patched_data", "strong_encrypt", "reserved_2", "lang_encoding", "reserved_3", "mask_header_values", "reserved_4"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.LocalFileHeader.GpFlags, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['file_encrypted']['start'] = self._io.pos()
                self.file_encrypted = self._io.read_bits_int_le(1) != 0
                self._debug['file_encrypted']['end'] = self._io.pos()
                self._debug['comp_options_raw']['start'] = self._io.pos()
                self.comp_options_raw = self._io.read_bits_int_le(2)
                self._debug['comp_options_raw']['end'] = self._io.pos()
                self._debug['has_data_descriptor']['start'] = self._io.pos()
                self.has_data_descriptor = self._io.read_bits_int_le(1) != 0
                self._debug['has_data_descriptor']['end'] = self._io.pos()
                self._debug['reserved_1']['start'] = self._io.pos()
                self.reserved_1 = self._io.read_bits_int_le(1) != 0
                self._debug['reserved_1']['end'] = self._io.pos()
                self._debug['comp_patched_data']['start'] = self._io.pos()
                self.comp_patched_data = self._io.read_bits_int_le(1) != 0
                self._debug['comp_patched_data']['end'] = self._io.pos()
                self._debug['strong_encrypt']['start'] = self._io.pos()
                self.strong_encrypt = self._io.read_bits_int_le(1) != 0
                self._debug['strong_encrypt']['end'] = self._io.pos()
                self._debug['reserved_2']['start'] = self._io.pos()
                self.reserved_2 = self._io.read_bits_int_le(4)
                self._debug['reserved_2']['end'] = self._io.pos()
                self._debug['lang_encoding']['start'] = self._io.pos()
                self.lang_encoding = self._io.read_bits_int_le(1) != 0
                self._debug['lang_encoding']['end'] = self._io.pos()
                self._debug['reserved_3']['start'] = self._io.pos()
                self.reserved_3 = self._io.read_bits_int_le(1) != 0
                self._debug['reserved_3']['end'] = self._io.pos()
                self._debug['mask_header_values']['start'] = self._io.pos()
                self.mask_header_values = self._io.read_bits_int_le(1) != 0
                self._debug['mask_header_values']['end'] = self._io.pos()
                self._debug['reserved_4']['start'] = self._io.pos()
                self.reserved_4 = self._io.read_bits_int_le(2)
                self._debug['reserved_4']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass

            @property
            def deflated_mode(self):
                if hasattr(self, '_m_deflated_mode'):
                    return self._m_deflated_mode

                if  ((self._parent.compression_method == Zip.Compression.deflated) or (self._parent.compression_method == Zip.Compression.enhanced_deflated)) :
                    pass
                    self._m_deflated_mode = KaitaiStream.resolve_enum(Zip.LocalFileHeader.GpFlags.DeflateMode, self.comp_options_raw)

                return getattr(self, '_m_deflated_mode', None)

            @property
            def imploded_dict_byte_size(self):
                """8KiB or 4KiB in bytes."""
                if hasattr(self, '_m_imploded_dict_byte_size'):
                    return self._m_imploded_dict_byte_size

                if self._parent.compression_method == Zip.Compression.imploded:
                    pass
                    self._m_imploded_dict_byte_size = (8 if self.comp_options_raw & 1 != 0 else 4) * 1024

                return getattr(self, '_m_imploded_dict_byte_size', None)

            @property
            def imploded_num_sf_trees(self):
                if hasattr(self, '_m_imploded_num_sf_trees'):
                    return self._m_imploded_num_sf_trees

                if self._parent.compression_method == Zip.Compression.imploded:
                    pass
                    self._m_imploded_num_sf_trees = (3 if self.comp_options_raw & 2 != 0 else 2)

                return getattr(self, '_m_imploded_num_sf_trees', None)

            @property
            def lzma_has_eos_marker(self):
                if hasattr(self, '_m_lzma_has_eos_marker'):
                    return self._m_lzma_has_eos_marker

                if self._parent.compression_method == Zip.Compression.lzma:
                    pass
                    self._m_lzma_has_eos_marker = self.comp_options_raw & 1 != 0

                return getattr(self, '_m_lzma_has_eos_marker', None)


        @property
        def has_padding(self):
            if hasattr(self, '_m_has_padding'):
                return self._m_has_padding

            self._m_has_padding = self.len_extra < 4
            return getattr(self, '_m_has_padding', None)


    class PkSection(KaitaiStruct):
        SEQ_FIELDS = ["section_type", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.PkSection, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['section_type']['start'] = self._io.pos()
            self.section_type = KaitaiStream.resolve_enum(Zip.SectionTypes, self._io.read_u4le())
            self._debug['section_type']['end'] = self._io.pos()
            if not  ((self.section_type == Zip.SectionTypes.central_dir_entry) or (self.section_type == Zip.SectionTypes.instar_central_dir_entry) or (self.section_type == Zip.SectionTypes.local_file) or (self.section_type == Zip.SectionTypes.dahua_local_file) or (self.section_type == Zip.SectionTypes.instar_local_file) or (self.section_type == Zip.SectionTypes.digital_signature) or (self.section_type == Zip.SectionTypes.end_of_central_dir) or (self.section_type == Zip.SectionTypes.instar_end_of_central_dir) or (self.section_type == Zip.SectionTypes.zip64_end_of_central_dir) or (self.section_type == Zip.SectionTypes.zip64_end_of_central_dir_locator) or (self.section_type == Zip.SectionTypes.archive_extra_data) or (self.section_type == Zip.SectionTypes.data_descriptor)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.section_type, self._io, u"/types/pk_section/seq/0")
            self._debug['body']['start'] = self._io.pos()
            _on = self.section_type
            if _on == Zip.SectionTypes.archive_extra_data:
                pass
                self.body = Zip.ArchiveExtraData(self._io, self, self._root)
            elif _on == Zip.SectionTypes.central_dir_entry:
                pass
                self.body = Zip.CentralDirEntry(self._io, self, self._root)
            elif _on == Zip.SectionTypes.dahua_local_file:
                pass
                self.body = Zip.LocalFile(self._io, self, self._root)
            elif _on == Zip.SectionTypes.data_descriptor:
                pass
                self.body = Zip.DataDescriptor(self._io, self, self._root)
            elif _on == Zip.SectionTypes.digital_signature:
                pass
                self.body = Zip.DigitalSignature(self._io, self, self._root)
            elif _on == Zip.SectionTypes.end_of_central_dir:
                pass
                self.body = Zip.EndOfCentralDir(self._io, self, self._root)
            elif _on == Zip.SectionTypes.instar_central_dir_entry:
                pass
                self.body = Zip.CentralDirEntry(self._io, self, self._root)
            elif _on == Zip.SectionTypes.instar_end_of_central_dir:
                pass
                self.body = Zip.EndOfCentralDir(self._io, self, self._root)
            elif _on == Zip.SectionTypes.instar_local_file:
                pass
                self.body = Zip.LocalFile(self._io, self, self._root)
            elif _on == Zip.SectionTypes.local_file:
                pass
                self.body = Zip.LocalFile(self._io, self, self._root)
            elif _on == Zip.SectionTypes.zip64_end_of_central_dir:
                pass
                self.body = Zip.Zip64EndOfCentralDir(self._io, self, self._root)
            elif _on == Zip.SectionTypes.zip64_end_of_central_dir_locator:
                pass
                self.body = Zip.Zip64EndOfCentralDirLocator(self._io, self, self._root)
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.section_type
            if _on == Zip.SectionTypes.archive_extra_data:
                pass
                self.body._fetch_instances()
            elif _on == Zip.SectionTypes.central_dir_entry:
                pass
                self.body._fetch_instances()
            elif _on == Zip.SectionTypes.dahua_local_file:
                pass
                self.body._fetch_instances()
            elif _on == Zip.SectionTypes.data_descriptor:
                pass
                self.body._fetch_instances()
            elif _on == Zip.SectionTypes.digital_signature:
                pass
                self.body._fetch_instances()
            elif _on == Zip.SectionTypes.end_of_central_dir:
                pass
                self.body._fetch_instances()
            elif _on == Zip.SectionTypes.instar_central_dir_entry:
                pass
                self.body._fetch_instances()
            elif _on == Zip.SectionTypes.instar_end_of_central_dir:
                pass
                self.body._fetch_instances()
            elif _on == Zip.SectionTypes.instar_local_file:
                pass
                self.body._fetch_instances()
            elif _on == Zip.SectionTypes.local_file:
                pass
                self.body._fetch_instances()
            elif _on == Zip.SectionTypes.zip64_end_of_central_dir:
                pass
                self.body._fetch_instances()
            elif _on == Zip.SectionTypes.zip64_end_of_central_dir_locator:
                pass
                self.body._fetch_instances()


    class PkSection64(KaitaiStruct):
        SEQ_FIELDS = ["section_type", "body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.PkSection64, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['section_type']['start'] = self._io.pos()
            self.section_type = KaitaiStream.resolve_enum(Zip.SectionTypes, self._io.read_u4le())
            self._debug['section_type']['end'] = self._io.pos()
            if not  ((self.section_type == Zip.SectionTypes.data_descriptor)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.section_type, self._io, u"/types/pk_section64/seq/0")
            self._debug['body']['start'] = self._io.pos()
            _on = self.section_type
            if _on == Zip.SectionTypes.data_descriptor:
                pass
                self.body = Zip.DataDescriptor64(self._io, self, self._root)
            self._debug['body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.section_type
            if _on == Zip.SectionTypes.data_descriptor:
                pass
                self.body._fetch_instances()


    class Version(KaitaiStruct):
        SEQ_FIELDS = ["version", "host_system"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['version']['start'] = self._io.pos()
            self.version = self._io.read_u1()
            self._debug['version']['end'] = self._io.pos()
            self._debug['host_system']['start'] = self._io.pos()
            self.host_system = KaitaiStream.resolve_enum(Zip.VersionMapping, self._io.read_u1())
            self._debug['host_system']['end'] = self._io.pos()
            if not  ((self.host_system == Zip.VersionMapping.msdos) or (self.host_system == Zip.VersionMapping.amiga) or (self.host_system == Zip.VersionMapping.openvms) or (self.host_system == Zip.VersionMapping.unix) or (self.host_system == Zip.VersionMapping.vm_cms) or (self.host_system == Zip.VersionMapping.atari_st) or (self.host_system == Zip.VersionMapping.os2_hpfs) or (self.host_system == Zip.VersionMapping.macintosh) or (self.host_system == Zip.VersionMapping.z_system) or (self.host_system == Zip.VersionMapping.cp_m) or (self.host_system == Zip.VersionMapping.windows_ntfs) or (self.host_system == Zip.VersionMapping.mvs) or (self.host_system == Zip.VersionMapping.vse) or (self.host_system == Zip.VersionMapping.acorn_risc) or (self.host_system == Zip.VersionMapping.vfat) or (self.host_system == Zip.VersionMapping.alternate_mvs) or (self.host_system == Zip.VersionMapping.beos) or (self.host_system == Zip.VersionMapping.tandem) or (self.host_system == Zip.VersionMapping.os_400) or (self.host_system == Zip.VersionMapping.os_x)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.host_system, self._io, u"/types/version/seq/1")


        def _fetch_instances(self):
            pass


    class Zip64EndOfCentralDir(KaitaiStruct):
        SEQ_FIELDS = ["len_record", "zip64_end_of_central_dir_body"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.Zip64EndOfCentralDir, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_record']['start'] = self._io.pos()
            self.len_record = self._io.read_u8le()
            self._debug['len_record']['end'] = self._io.pos()
            self._debug['zip64_end_of_central_dir_body']['start'] = self._io.pos()
            self._raw_zip64_end_of_central_dir_body = self._io.read_bytes(self.len_record)
            _io__raw_zip64_end_of_central_dir_body = KaitaiStream(BytesIO(self._raw_zip64_end_of_central_dir_body))
            self.zip64_end_of_central_dir_body = Zip.Zip64EndOfCentralDir.Zip64EndOfCentralDirBody(_io__raw_zip64_end_of_central_dir_body, self, self._root)
            self._debug['zip64_end_of_central_dir_body']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.zip64_end_of_central_dir_body._fetch_instances()

        class Zip64EndOfCentralDirBody(KaitaiStruct):
            SEQ_FIELDS = ["version_made_by", "version_needed_to_extract", "this_disk", "disk_of_start_of_central_dir", "num_central_dir_entries_on_disk", "num_central_dir_entries_total", "len_central_dir", "ofs_central_dir", "extensible_data"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Zip.Zip64EndOfCentralDir.Zip64EndOfCentralDirBody, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['version_made_by']['start'] = self._io.pos()
                self.version_made_by = Zip.Version(self._io, self, self._root)
                self._debug['version_made_by']['end'] = self._io.pos()
                self._debug['version_needed_to_extract']['start'] = self._io.pos()
                self.version_needed_to_extract = Zip.Version(self._io, self, self._root)
                self._debug['version_needed_to_extract']['end'] = self._io.pos()
                self._debug['this_disk']['start'] = self._io.pos()
                self.this_disk = self._io.read_u4le()
                self._debug['this_disk']['end'] = self._io.pos()
                self._debug['disk_of_start_of_central_dir']['start'] = self._io.pos()
                self.disk_of_start_of_central_dir = self._io.read_u4le()
                self._debug['disk_of_start_of_central_dir']['end'] = self._io.pos()
                self._debug['num_central_dir_entries_on_disk']['start'] = self._io.pos()
                self.num_central_dir_entries_on_disk = self._io.read_u8le()
                self._debug['num_central_dir_entries_on_disk']['end'] = self._io.pos()
                self._debug['num_central_dir_entries_total']['start'] = self._io.pos()
                self.num_central_dir_entries_total = self._io.read_u8le()
                self._debug['num_central_dir_entries_total']['end'] = self._io.pos()
                self._debug['len_central_dir']['start'] = self._io.pos()
                self.len_central_dir = self._io.read_u8le()
                self._debug['len_central_dir']['end'] = self._io.pos()
                self._debug['ofs_central_dir']['start'] = self._io.pos()
                self.ofs_central_dir = self._io.read_u8le()
                self._debug['ofs_central_dir']['end'] = self._io.pos()
                self._debug['extensible_data']['start'] = self._io.pos()
                self.extensible_data = self._io.read_bytes_full()
                self._debug['extensible_data']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.version_made_by._fetch_instances()
                self.version_needed_to_extract._fetch_instances()



    class Zip64EndOfCentralDirLocator(KaitaiStruct):
        SEQ_FIELDS = ["disk_of_start_of_central_dir", "ofs_zip64_end_of_central_dir", "total_number_of_disks"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Zip.Zip64EndOfCentralDirLocator, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['disk_of_start_of_central_dir']['start'] = self._io.pos()
            self.disk_of_start_of_central_dir = self._io.read_u4le()
            self._debug['disk_of_start_of_central_dir']['end'] = self._io.pos()
            self._debug['ofs_zip64_end_of_central_dir']['start'] = self._io.pos()
            self.ofs_zip64_end_of_central_dir = self._io.read_u8le()
            self._debug['ofs_zip64_end_of_central_dir']['end'] = self._io.pos()
            self._debug['total_number_of_disks']['start'] = self._io.pos()
            self.total_number_of_disks = self._io.read_u4le()
            self._debug['total_number_of_disks']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass



