# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class LinuxX86(KaitaiStruct):
    """
    .. seealso::
       Source - https://www.kernel.org/doc/Documentation/x86/boot.txt
    """

    class HardwareSubarchs(IntEnum):
        default = 0
        lguest = 1
        xen = 2
        moorestown = 3
        ce4100 = 4
    SEQ_FIELDS = ["header"]
    def __init__(self, _io, _parent=None, _root=None):
        super(LinuxX86, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self.header = LinuxX86.Header(self._io, self, self._root)
        self._debug['header']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()

    class CommonHeader(KaitaiStruct):
        SEQ_FIELDS = ["reserved", "setup_sects", "root_flags", "syssize", "ram_size", "vid_mode", "root_dev", "boot_flag"]
        def __init__(self, _io, _parent=None, _root=None):
            super(LinuxX86.CommonHeader, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(497)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['setup_sects']['start'] = self._io.pos()
            self.setup_sects = self._io.read_u1()
            self._debug['setup_sects']['end'] = self._io.pos()
            self._debug['root_flags']['start'] = self._io.pos()
            self.root_flags = self._io.read_u2le()
            self._debug['root_flags']['end'] = self._io.pos()
            self._debug['syssize']['start'] = self._io.pos()
            self.syssize = self._io.read_u4le()
            self._debug['syssize']['end'] = self._io.pos()
            self._debug['ram_size']['start'] = self._io.pos()
            self.ram_size = self._io.read_u2le()
            self._debug['ram_size']['end'] = self._io.pos()
            self._debug['vid_mode']['start'] = self._io.pos()
            self.vid_mode = self._io.read_u2le()
            self._debug['vid_mode']['end'] = self._io.pos()
            self._debug['root_dev']['start'] = self._io.pos()
            self.root_dev = self._io.read_u2le()
            self._debug['root_dev']['end'] = self._io.pos()
            self._debug['boot_flag']['start'] = self._io.pos()
            self.boot_flag = self._io.read_bytes(2)
            self._debug['boot_flag']['end'] = self._io.pos()
            if not self.boot_flag == b"\x55\xAA":
                raise kaitaistruct.ValidationNotEqualError(b"\x55\xAA", self.boot_flag, self._io, u"/types/common_header/seq/7")


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["common_header", "jump", "magic", "version", "realmode_switch", "start_sys_seg", "kernel_version", "type_of_loader", "loadflags", "setup_move_size", "code32_start", "ramdisk_image", "ramdisk_size", "bootsect_kludge", "heap_end_ptr", "ext_loader_ver", "ext_loader_type", "cmd_line_ptr", "initrd_addr_max", "kernel_alignment", "relocatable_kernel", "min_alignment", "xloadflags", "cmdline_size", "hardware_subarch", "hardware_subarch_data", "ofs_payload", "len_payload", "setup_data", "pref_address", "init_size", "handover_offset"]
        def __init__(self, _io, _parent=None, _root=None):
            super(LinuxX86.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['common_header']['start'] = self._io.pos()
            self.common_header = LinuxX86.CommonHeader(self._io, self, self._root)
            self._debug['common_header']['end'] = self._io.pos()
            self._debug['jump']['start'] = self._io.pos()
            self.jump = LinuxX86.Jump(self._io, self, self._root)
            self._debug['jump']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x48\x64\x72\x53":
                raise kaitaistruct.ValidationNotEqualError(b"\x48\x64\x72\x53", self.magic, self._io, u"/types/header/seq/2")
            self._debug['version']['start'] = self._io.pos()
            self.version = LinuxX86.Version(self._io, self, self._root)
            self._debug['version']['end'] = self._io.pos()
            self._debug['realmode_switch']['start'] = self._io.pos()
            self.realmode_switch = self._io.read_u4le()
            self._debug['realmode_switch']['end'] = self._io.pos()
            self._debug['start_sys_seg']['start'] = self._io.pos()
            self.start_sys_seg = self._io.read_u2le()
            self._debug['start_sys_seg']['end'] = self._io.pos()
            self._debug['kernel_version']['start'] = self._io.pos()
            self.kernel_version = self._io.read_u2le()
            self._debug['kernel_version']['end'] = self._io.pos()
            self._debug['type_of_loader']['start'] = self._io.pos()
            self.type_of_loader = self._io.read_u1()
            self._debug['type_of_loader']['end'] = self._io.pos()
            self._debug['loadflags']['start'] = self._io.pos()
            self.loadflags = self._io.read_u1()
            self._debug['loadflags']['end'] = self._io.pos()
            self._debug['setup_move_size']['start'] = self._io.pos()
            self.setup_move_size = self._io.read_u2le()
            self._debug['setup_move_size']['end'] = self._io.pos()
            self._debug['code32_start']['start'] = self._io.pos()
            self.code32_start = self._io.read_u4le()
            self._debug['code32_start']['end'] = self._io.pos()
            self._debug['ramdisk_image']['start'] = self._io.pos()
            self.ramdisk_image = self._io.read_u4le()
            self._debug['ramdisk_image']['end'] = self._io.pos()
            self._debug['ramdisk_size']['start'] = self._io.pos()
            self.ramdisk_size = self._io.read_u4le()
            self._debug['ramdisk_size']['end'] = self._io.pos()
            self._debug['bootsect_kludge']['start'] = self._io.pos()
            self.bootsect_kludge = self._io.read_u4le()
            self._debug['bootsect_kludge']['end'] = self._io.pos()
            self._debug['heap_end_ptr']['start'] = self._io.pos()
            self.heap_end_ptr = self._io.read_u2le()
            self._debug['heap_end_ptr']['end'] = self._io.pos()
            self._debug['ext_loader_ver']['start'] = self._io.pos()
            self.ext_loader_ver = self._io.read_u1()
            self._debug['ext_loader_ver']['end'] = self._io.pos()
            self._debug['ext_loader_type']['start'] = self._io.pos()
            self.ext_loader_type = self._io.read_u1()
            self._debug['ext_loader_type']['end'] = self._io.pos()
            self._debug['cmd_line_ptr']['start'] = self._io.pos()
            self.cmd_line_ptr = self._io.read_u4le()
            self._debug['cmd_line_ptr']['end'] = self._io.pos()
            self._debug['initrd_addr_max']['start'] = self._io.pos()
            self.initrd_addr_max = self._io.read_u4le()
            self._debug['initrd_addr_max']['end'] = self._io.pos()
            self._debug['kernel_alignment']['start'] = self._io.pos()
            self.kernel_alignment = self._io.read_u4le()
            self._debug['kernel_alignment']['end'] = self._io.pos()
            self._debug['relocatable_kernel']['start'] = self._io.pos()
            self.relocatable_kernel = self._io.read_u1()
            self._debug['relocatable_kernel']['end'] = self._io.pos()
            self._debug['min_alignment']['start'] = self._io.pos()
            self.min_alignment = self._io.read_u1()
            self._debug['min_alignment']['end'] = self._io.pos()
            self._debug['xloadflags']['start'] = self._io.pos()
            self.xloadflags = self._io.read_u2le()
            self._debug['xloadflags']['end'] = self._io.pos()
            if self.version.minor >= 6:
                pass
                self._debug['cmdline_size']['start'] = self._io.pos()
                self.cmdline_size = self._io.read_u4le()
                self._debug['cmdline_size']['end'] = self._io.pos()

            if self.version.minor >= 7:
                pass
                self._debug['hardware_subarch']['start'] = self._io.pos()
                self.hardware_subarch = KaitaiStream.resolve_enum(LinuxX86.HardwareSubarchs, self._io.read_u4le())
                self._debug['hardware_subarch']['end'] = self._io.pos()

            if self.version.minor >= 7:
                pass
                self._debug['hardware_subarch_data']['start'] = self._io.pos()
                self.hardware_subarch_data = self._io.read_bytes(8)
                self._debug['hardware_subarch_data']['end'] = self._io.pos()

            if self.version.minor >= 8:
                pass
                self._debug['ofs_payload']['start'] = self._io.pos()
                self.ofs_payload = self._io.read_u4le()
                self._debug['ofs_payload']['end'] = self._io.pos()

            if self.version.minor >= 8:
                pass
                self._debug['len_payload']['start'] = self._io.pos()
                self.len_payload = self._io.read_u4le()
                self._debug['len_payload']['end'] = self._io.pos()

            if self.version.minor >= 9:
                pass
                self._debug['setup_data']['start'] = self._io.pos()
                self.setup_data = self._io.read_u8le()
                self._debug['setup_data']['end'] = self._io.pos()

            if self.version.minor >= 10:
                pass
                self._debug['pref_address']['start'] = self._io.pos()
                self.pref_address = self._io.read_u8le()
                self._debug['pref_address']['end'] = self._io.pos()

            if self.version.minor >= 10:
                pass
                self._debug['init_size']['start'] = self._io.pos()
                self.init_size = self._io.read_u4le()
                self._debug['init_size']['end'] = self._io.pos()

            if self.version.minor >= 11:
                pass
                self._debug['handover_offset']['start'] = self._io.pos()
                self.handover_offset = self._io.read_u4le()
                self._debug['handover_offset']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            self.common_header._fetch_instances()
            self.jump._fetch_instances()
            self.version._fetch_instances()
            if self.version.minor >= 6:
                pass

            if self.version.minor >= 7:
                pass

            if self.version.minor >= 7:
                pass

            if self.version.minor >= 8:
                pass

            if self.version.minor >= 8:
                pass

            if self.version.minor >= 9:
                pass

            if self.version.minor >= 10:
                pass

            if self.version.minor >= 10:
                pass

            if self.version.minor >= 11:
                pass

            _ = self.kernel_version_string
            if hasattr(self, '_m_kernel_version_string'):
                pass

            _ = self.payload
            if hasattr(self, '_m_payload'):
                pass


        @property
        def kernel_version_string(self):
            if hasattr(self, '_m_kernel_version_string'):
                return self._m_kernel_version_string

            _pos = self._io.pos()
            self._io.seek(self.kernel_version + 512)
            self._debug['_m_kernel_version_string']['start'] = self._io.pos()
            self._m_kernel_version_string = (self._io.read_bytes_term(0, False, True, True)).decode(u"ASCII")
            self._debug['_m_kernel_version_string']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_kernel_version_string', None)

        @property
        def payload(self):
            if hasattr(self, '_m_payload'):
                return self._m_payload

            if self.ofs_payload != 0:
                pass
                _pos = self._io.pos()
                self._io.seek(self.real_mode_code_size + self.ofs_payload)
                self._debug['_m_payload']['start'] = self._io.pos()
                self._m_payload = self._io.read_bytes(self.len_payload)
                self._debug['_m_payload']['end'] = self._io.pos()
                self._io.seek(_pos)

            return getattr(self, '_m_payload', None)

        @property
        def protected_mode_code_size(self):
            if hasattr(self, '_m_protected_mode_code_size'):
                return self._m_protected_mode_code_size

            self._m_protected_mode_code_size = self.common_header.syssize * 2
            return getattr(self, '_m_protected_mode_code_size', None)

        @property
        def real_mode_code_size(self):
            if hasattr(self, '_m_real_mode_code_size'):
                return self._m_real_mode_code_size

            self._m_real_mode_code_size = self.setup_code_size + 512
            return getattr(self, '_m_real_mode_code_size', None)

        @property
        def setup_code_size(self):
            if hasattr(self, '_m_setup_code_size'):
                return self._m_setup_code_size

            self._m_setup_code_size = (4 * 512 if self.common_header.setup_sects == 0 else self.common_header.setup_sects * 512)
            return getattr(self, '_m_setup_code_size', None)


    class Jump(KaitaiStruct):
        SEQ_FIELDS = ["jump_instruction", "signed_offset"]
        def __init__(self, _io, _parent=None, _root=None):
            super(LinuxX86.Jump, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['jump_instruction']['start'] = self._io.pos()
            self.jump_instruction = self._io.read_u1()
            self._debug['jump_instruction']['end'] = self._io.pos()
            if not self.jump_instruction == 235:
                raise kaitaistruct.ValidationNotEqualError(235, self.jump_instruction, self._io, u"/types/jump/seq/0")
            self._debug['signed_offset']['start'] = self._io.pos()
            self.signed_offset = self._io.read_s1()
            self._debug['signed_offset']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def header_length(self):
            if hasattr(self, '_m_header_length'):
                return self._m_header_length

            self._m_header_length = self.signed_offset + 514
            return getattr(self, '_m_header_length', None)


    class Version(KaitaiStruct):
        SEQ_FIELDS = ["minor", "major"]
        def __init__(self, _io, _parent=None, _root=None):
            super(LinuxX86.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u1()
            self._debug['minor']['end'] = self._io.pos()
            if not self.minor >= 2:
                raise kaitaistruct.ValidationLessThanError(2, self.minor, self._io, u"/types/version/seq/0")
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u1()
            self._debug['major']['end'] = self._io.pos()
            if not self.major == 2:
                raise kaitaistruct.ValidationNotEqualError(2, self.major, self._io, u"/types/version/seq/1")


        def _fetch_instances(self):
            pass



