# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Oat(KaitaiStruct):
    """The OAT format is an optimized format for Dalvik DEX code. OAT files are
    typically distributed as ELF files, with the OAT and DEX code spanning
    various ELF sections.
    
    Google frequently updates the OAT format, but not every version is in use
    in real products.
    
    <https://github.com/JesusFreke/smali/blob/master/dexlib2/OatVersions.txt>
    
    .. seealso::
       Source - https://android.googlesource.com/platform/art/+/master/runtime/oat.h
    """
    SEQ_FIELDS = ["magic", "version", "oat_header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Oat, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x6F\x61\x74\x0A":
            raise kaitaistruct.ValidationNotEqualError(b"\x6F\x61\x74\x0A", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = (KaitaiStream.bytes_terminate(self._io.read_bytes(4), 0, False)).decode(u"UTF-8")
        self._debug['version']['end'] = self._io.pos()
        self._debug['oat_header']['start'] = self._io.pos()
        _on = self.version
        if _on == u"079":
            pass
            self.oat_header = Oat.Header079(self._io, self, self._root)
        elif _on == u"131":
            pass
            self.oat_header = Oat.Header131(self._io, self, self._root)
        elif _on == u"137":
            pass
            self.oat_header = Oat.Header131(self._io, self, self._root)
        elif _on == u"138":
            pass
            self.oat_header = Oat.Header131(self._io, self, self._root)
        elif _on == u"229":
            pass
            self.oat_header = Oat.Header229(self._io, self, self._root)
        self._debug['oat_header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _on = self.version
        if _on == u"079":
            pass
            self.oat_header._fetch_instances()
        elif _on == u"131":
            pass
            self.oat_header._fetch_instances()
        elif _on == u"137":
            pass
            self.oat_header._fetch_instances()
        elif _on == u"138":
            pass
            self.oat_header._fetch_instances()
        elif _on == u"229":
            pass
            self.oat_header._fetch_instances()

    class Header079(KaitaiStruct):
        SEQ_FIELDS = ["adler32_checksum", "instruction_set", "instruction_set_features_bitmap", "num_dex_file", "ofs_executable", "ofs_interpreter_to_interpreter_bridge", "ofs_interpreter_to_compiled_code_bridge", "ofs_jni_dlsym_lookup", "ofs_quick_generic_jni_trampoline", "ofs_quick_imt_conflict_trampoline", "ofs_quick_resolution_trampoline", "ofs_quick_to_interpreter_bridge", "image_patch_delta", "ofs_image_file_oat_checksum", "ofs_image_file_location_oat_data", "len_key_value_store", "key_value_store"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Oat.Header079, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['adler32_checksum']['start'] = self._io.pos()
            self.adler32_checksum = self._io.read_u4le()
            self._debug['adler32_checksum']['end'] = self._io.pos()
            self._debug['instruction_set']['start'] = self._io.pos()
            self.instruction_set = self._io.read_u4le()
            self._debug['instruction_set']['end'] = self._io.pos()
            self._debug['instruction_set_features_bitmap']['start'] = self._io.pos()
            self.instruction_set_features_bitmap = self._io.read_u4le()
            self._debug['instruction_set_features_bitmap']['end'] = self._io.pos()
            self._debug['num_dex_file']['start'] = self._io.pos()
            self.num_dex_file = self._io.read_u4le()
            self._debug['num_dex_file']['end'] = self._io.pos()
            self._debug['ofs_executable']['start'] = self._io.pos()
            self.ofs_executable = self._io.read_u4le()
            self._debug['ofs_executable']['end'] = self._io.pos()
            self._debug['ofs_interpreter_to_interpreter_bridge']['start'] = self._io.pos()
            self.ofs_interpreter_to_interpreter_bridge = self._io.read_u4le()
            self._debug['ofs_interpreter_to_interpreter_bridge']['end'] = self._io.pos()
            self._debug['ofs_interpreter_to_compiled_code_bridge']['start'] = self._io.pos()
            self.ofs_interpreter_to_compiled_code_bridge = self._io.read_u4le()
            self._debug['ofs_interpreter_to_compiled_code_bridge']['end'] = self._io.pos()
            self._debug['ofs_jni_dlsym_lookup']['start'] = self._io.pos()
            self.ofs_jni_dlsym_lookup = self._io.read_u4le()
            self._debug['ofs_jni_dlsym_lookup']['end'] = self._io.pos()
            self._debug['ofs_quick_generic_jni_trampoline']['start'] = self._io.pos()
            self.ofs_quick_generic_jni_trampoline = self._io.read_u4le()
            self._debug['ofs_quick_generic_jni_trampoline']['end'] = self._io.pos()
            self._debug['ofs_quick_imt_conflict_trampoline']['start'] = self._io.pos()
            self.ofs_quick_imt_conflict_trampoline = self._io.read_u4le()
            self._debug['ofs_quick_imt_conflict_trampoline']['end'] = self._io.pos()
            self._debug['ofs_quick_resolution_trampoline']['start'] = self._io.pos()
            self.ofs_quick_resolution_trampoline = self._io.read_u4le()
            self._debug['ofs_quick_resolution_trampoline']['end'] = self._io.pos()
            self._debug['ofs_quick_to_interpreter_bridge']['start'] = self._io.pos()
            self.ofs_quick_to_interpreter_bridge = self._io.read_u4le()
            self._debug['ofs_quick_to_interpreter_bridge']['end'] = self._io.pos()
            self._debug['image_patch_delta']['start'] = self._io.pos()
            self.image_patch_delta = self._io.read_u4le()
            self._debug['image_patch_delta']['end'] = self._io.pos()
            self._debug['ofs_image_file_oat_checksum']['start'] = self._io.pos()
            self.ofs_image_file_oat_checksum = self._io.read_u4le()
            self._debug['ofs_image_file_oat_checksum']['end'] = self._io.pos()
            self._debug['ofs_image_file_location_oat_data']['start'] = self._io.pos()
            self.ofs_image_file_location_oat_data = self._io.read_u4le()
            self._debug['ofs_image_file_location_oat_data']['end'] = self._io.pos()
            self._debug['len_key_value_store']['start'] = self._io.pos()
            self.len_key_value_store = self._io.read_u4le()
            self._debug['len_key_value_store']['end'] = self._io.pos()
            self._debug['key_value_store']['start'] = self._io.pos()
            self._raw_key_value_store = self._io.read_bytes(self.len_key_value_store)
            _io__raw_key_value_store = KaitaiStream(BytesIO(self._raw_key_value_store))
            self.key_value_store = Oat.KeyValueStore(_io__raw_key_value_store, self, self._root)
            self._debug['key_value_store']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.key_value_store._fetch_instances()


    class Header131(KaitaiStruct):
        SEQ_FIELDS = ["adler32_checksum", "instruction_set", "instruction_set_features_bitmap", "num_dex_file", "ofs_oat_dex_files", "ofs_executable", "ofs_interpreter_to_interpreter_bridge", "ofs_interpreter_to_compiled_code_bridge", "ofs_jni_dlsym_lookup", "ofs_quick_generic_jni_trampoline", "ofs_quick_imt_conflict_trampoline", "ofs_quick_resolution_trampoline", "ofs_quick_to_interpreter_bridge", "image_patch_delta", "ofs_image_file_oat_checksum", "ofs_image_file_location_oat_data", "len_key_value_store", "key_value_store"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Oat.Header131, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['adler32_checksum']['start'] = self._io.pos()
            self.adler32_checksum = self._io.read_u4le()
            self._debug['adler32_checksum']['end'] = self._io.pos()
            self._debug['instruction_set']['start'] = self._io.pos()
            self.instruction_set = self._io.read_u4le()
            self._debug['instruction_set']['end'] = self._io.pos()
            self._debug['instruction_set_features_bitmap']['start'] = self._io.pos()
            self.instruction_set_features_bitmap = self._io.read_u4le()
            self._debug['instruction_set_features_bitmap']['end'] = self._io.pos()
            self._debug['num_dex_file']['start'] = self._io.pos()
            self.num_dex_file = self._io.read_u4le()
            self._debug['num_dex_file']['end'] = self._io.pos()
            self._debug['ofs_oat_dex_files']['start'] = self._io.pos()
            self.ofs_oat_dex_files = self._io.read_u4le()
            self._debug['ofs_oat_dex_files']['end'] = self._io.pos()
            self._debug['ofs_executable']['start'] = self._io.pos()
            self.ofs_executable = self._io.read_u4le()
            self._debug['ofs_executable']['end'] = self._io.pos()
            self._debug['ofs_interpreter_to_interpreter_bridge']['start'] = self._io.pos()
            self.ofs_interpreter_to_interpreter_bridge = self._io.read_u4le()
            self._debug['ofs_interpreter_to_interpreter_bridge']['end'] = self._io.pos()
            self._debug['ofs_interpreter_to_compiled_code_bridge']['start'] = self._io.pos()
            self.ofs_interpreter_to_compiled_code_bridge = self._io.read_u4le()
            self._debug['ofs_interpreter_to_compiled_code_bridge']['end'] = self._io.pos()
            self._debug['ofs_jni_dlsym_lookup']['start'] = self._io.pos()
            self.ofs_jni_dlsym_lookup = self._io.read_u4le()
            self._debug['ofs_jni_dlsym_lookup']['end'] = self._io.pos()
            self._debug['ofs_quick_generic_jni_trampoline']['start'] = self._io.pos()
            self.ofs_quick_generic_jni_trampoline = self._io.read_u4le()
            self._debug['ofs_quick_generic_jni_trampoline']['end'] = self._io.pos()
            self._debug['ofs_quick_imt_conflict_trampoline']['start'] = self._io.pos()
            self.ofs_quick_imt_conflict_trampoline = self._io.read_u4le()
            self._debug['ofs_quick_imt_conflict_trampoline']['end'] = self._io.pos()
            self._debug['ofs_quick_resolution_trampoline']['start'] = self._io.pos()
            self.ofs_quick_resolution_trampoline = self._io.read_u4le()
            self._debug['ofs_quick_resolution_trampoline']['end'] = self._io.pos()
            self._debug['ofs_quick_to_interpreter_bridge']['start'] = self._io.pos()
            self.ofs_quick_to_interpreter_bridge = self._io.read_u4le()
            self._debug['ofs_quick_to_interpreter_bridge']['end'] = self._io.pos()
            self._debug['image_patch_delta']['start'] = self._io.pos()
            self.image_patch_delta = self._io.read_u4le()
            self._debug['image_patch_delta']['end'] = self._io.pos()
            self._debug['ofs_image_file_oat_checksum']['start'] = self._io.pos()
            self.ofs_image_file_oat_checksum = self._io.read_u4le()
            self._debug['ofs_image_file_oat_checksum']['end'] = self._io.pos()
            self._debug['ofs_image_file_location_oat_data']['start'] = self._io.pos()
            self.ofs_image_file_location_oat_data = self._io.read_u4le()
            self._debug['ofs_image_file_location_oat_data']['end'] = self._io.pos()
            self._debug['len_key_value_store']['start'] = self._io.pos()
            self.len_key_value_store = self._io.read_u4le()
            self._debug['len_key_value_store']['end'] = self._io.pos()
            self._debug['key_value_store']['start'] = self._io.pos()
            self._raw_key_value_store = self._io.read_bytes(self.len_key_value_store)
            _io__raw_key_value_store = KaitaiStream(BytesIO(self._raw_key_value_store))
            self.key_value_store = Oat.KeyValueStore(_io__raw_key_value_store, self, self._root)
            self._debug['key_value_store']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.key_value_store._fetch_instances()


    class Header229(KaitaiStruct):
        SEQ_FIELDS = ["adler32_checksum", "instruction_set", "instruction_set_features_bitmap", "num_dex_file", "ofs_oat_dex_files", "ofs_bcp_bss_info", "ofs_executable", "ofs_jni_dlsym_lookup_trampoline", "ofs_jni_dlsym_lookup_critical_trampoline", "ofs_quick_generic_jni_trampoline", "ofs_quick_imt_conflict_trampoline", "ofs_quick_resolution_trampoline", "ofs_quick_to_interpreter_bridge", "ofs_nterp_trampoline", "len_key_value_store", "key_value_store"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Oat.Header229, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['adler32_checksum']['start'] = self._io.pos()
            self.adler32_checksum = self._io.read_u4le()
            self._debug['adler32_checksum']['end'] = self._io.pos()
            self._debug['instruction_set']['start'] = self._io.pos()
            self.instruction_set = self._io.read_u4le()
            self._debug['instruction_set']['end'] = self._io.pos()
            self._debug['instruction_set_features_bitmap']['start'] = self._io.pos()
            self.instruction_set_features_bitmap = self._io.read_u4le()
            self._debug['instruction_set_features_bitmap']['end'] = self._io.pos()
            self._debug['num_dex_file']['start'] = self._io.pos()
            self.num_dex_file = self._io.read_u4le()
            self._debug['num_dex_file']['end'] = self._io.pos()
            self._debug['ofs_oat_dex_files']['start'] = self._io.pos()
            self.ofs_oat_dex_files = self._io.read_u4le()
            self._debug['ofs_oat_dex_files']['end'] = self._io.pos()
            self._debug['ofs_bcp_bss_info']['start'] = self._io.pos()
            self.ofs_bcp_bss_info = self._io.read_u4le()
            self._debug['ofs_bcp_bss_info']['end'] = self._io.pos()
            self._debug['ofs_executable']['start'] = self._io.pos()
            self.ofs_executable = self._io.read_u4le()
            self._debug['ofs_executable']['end'] = self._io.pos()
            self._debug['ofs_jni_dlsym_lookup_trampoline']['start'] = self._io.pos()
            self.ofs_jni_dlsym_lookup_trampoline = self._io.read_u4le()
            self._debug['ofs_jni_dlsym_lookup_trampoline']['end'] = self._io.pos()
            self._debug['ofs_jni_dlsym_lookup_critical_trampoline']['start'] = self._io.pos()
            self.ofs_jni_dlsym_lookup_critical_trampoline = self._io.read_u4le()
            self._debug['ofs_jni_dlsym_lookup_critical_trampoline']['end'] = self._io.pos()
            self._debug['ofs_quick_generic_jni_trampoline']['start'] = self._io.pos()
            self.ofs_quick_generic_jni_trampoline = self._io.read_u4le()
            self._debug['ofs_quick_generic_jni_trampoline']['end'] = self._io.pos()
            self._debug['ofs_quick_imt_conflict_trampoline']['start'] = self._io.pos()
            self.ofs_quick_imt_conflict_trampoline = self._io.read_u4le()
            self._debug['ofs_quick_imt_conflict_trampoline']['end'] = self._io.pos()
            self._debug['ofs_quick_resolution_trampoline']['start'] = self._io.pos()
            self.ofs_quick_resolution_trampoline = self._io.read_u4le()
            self._debug['ofs_quick_resolution_trampoline']['end'] = self._io.pos()
            self._debug['ofs_quick_to_interpreter_bridge']['start'] = self._io.pos()
            self.ofs_quick_to_interpreter_bridge = self._io.read_u4le()
            self._debug['ofs_quick_to_interpreter_bridge']['end'] = self._io.pos()
            self._debug['ofs_nterp_trampoline']['start'] = self._io.pos()
            self.ofs_nterp_trampoline = self._io.read_u4le()
            self._debug['ofs_nterp_trampoline']['end'] = self._io.pos()
            self._debug['len_key_value_store']['start'] = self._io.pos()
            self.len_key_value_store = self._io.read_u4le()
            self._debug['len_key_value_store']['end'] = self._io.pos()
            self._debug['key_value_store']['start'] = self._io.pos()
            self._raw_key_value_store = self._io.read_bytes(self.len_key_value_store)
            _io__raw_key_value_store = KaitaiStream(BytesIO(self._raw_key_value_store))
            self.key_value_store = Oat.KeyValueStore(_io__raw_key_value_store, self, self._root)
            self._debug['key_value_store']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.key_value_store._fetch_instances()


    class KeyValue(KaitaiStruct):
        SEQ_FIELDS = ["key", "value"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Oat.KeyValue, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['key']['start'] = self._io.pos()
            self.key = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['key']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = (self._io.read_bytes_term(0, False, True, True)).decode(u"UTF-8")
            self._debug['value']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class KeyValueStore(KaitaiStruct):
        SEQ_FIELDS = ["key_values"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Oat.KeyValueStore, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['key_values']['start'] = self._io.pos()
            self._debug['key_values']['arr'] = []
            self.key_values = []
            i = 0
            while not self._io.is_eof():
                self._debug['key_values']['arr'].append({'start': self._io.pos()})
                self.key_values.append(Oat.KeyValue(self._io, self, self._root))
                self._debug['key_values']['arr'][len(self.key_values) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['key_values']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.key_values)):
                pass
                self.key_values[i]._fetch_instances()




