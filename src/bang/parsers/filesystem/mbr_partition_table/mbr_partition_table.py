# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class MbrPartitionTable(KaitaiStruct):
    """MBR (Master Boot Record) partition table is a traditional way of
    MS-DOS to partition larger hard disc drives into distinct
    partitions.
    
    This table is stored in the end of the boot sector (first sector) of
    the drive, after the bootstrap code. Original DOS 2.0 specification
    allowed only 4 partitions per disc, but DOS 3.2 introduced concept
    of "extended partitions", which work as nested extra "boot records"
    which are pointed to by original ("primary") partitions in MBR.
    """

    class PartitionType(IntEnum):
        empty = 0
        fat12 = 1
        xenix_root = 2
        xenix_usr = 3
        fat16_below_32m = 4
        extended = 5
        fat16 = 6
        hpfs_ntfs_exfat = 7
        aix = 8
        aix_bootable = 9
        os2_boot_manager = 10
        w95_fat32 = 11
        w95_fat32_lba = 12
        w95_fat16_lba = 14
        w95_extended_lba = 15
        opus = 16
        hidden_fat12 = 17
        compaq_diagnostics = 18
        hidden_fat16_below_32m = 20
        hidden_fat16 = 22
        hidden_hpfs_ntfs = 23
        ast_smartsleep = 24
        hidden_w95_fat32 = 27
        hidden_w95_fat32_lba = 28
        hidden_w95_fat16_lba = 30
        nec_dos = 36
        hidden_ntfs_winre = 39
        plan9 = 57
        partitionmagic_recovery = 60
        venix_80286 = 64
        ppc_prep_boot = 65
        sfs = 66
        qnx4 = 77
        qnx4_second_part = 78
        qnx4_third_part = 79
        ontrack_dm = 80
        ontrack_dm6_aux1 = 81
        cpm = 82
        ontrack_dm6_aux3 = 83
        ontrack_dm6 = 84
        ez_drive = 85
        golden_bow = 86
        priam_edisk = 92
        speedstor = 97
        gnu_hurd_or_sysv = 99
        novell_netware_286 = 100
        novell_netware_386 = 101
        disksecure_multi_boot = 112
        pc_ix = 117
        old_minix = 128
        minix_old_linux = 129
        linux_swap_solaris = 130
        linux = 131
        os2_hidden_or_intel_hibenation = 132
        linux_extended = 133
        ntfs_volume_set_1 = 134
        ntfs_volume_set_2 = 135
        linux_plaintext = 136
        linux_lvm = 142
        amoeba = 147
        amoeba_bbt = 148
        bsd_os = 159
        ibm_thinkpad_hibernation = 160
        freebsd = 165
        openbsd = 166
        nextstep = 167
        darwin_ufs = 168
        netbsd = 169
        darwin_boot = 171
        hfs_hfsplus = 175
        bsdi_fs = 183
        bsdi_swap = 184
        boot_wizard_hidden = 187
        acronis_fat32_lba = 188
        solaris_boot = 190
        solaris = 191
        drdos_sec_fat12 = 193
        drdos_sec_fat16_below_32m = 196
        drdos_sec_fat16 = 198
        syrinx = 199
        non_fs_data = 218
        cpm_ctos = 219
        dell_utility = 222
        bootit = 223
        dos_access = 225
        dos_ro = 227
        speedstore_extended = 228
        rufus_alignment = 234
        beos_fs = 235
        gpt = 238
        efi = 239
        linux_parisc_boot = 240
        speedstor_1 = 241
        dos_secondary = 242
        speedstore_large_partition = 244
        vmware_vmfs = 251
        vmware_vmkcore = 252
        linux_raid_autodetect = 253
        lanstep = 254
        xenix_bbt = 255
    SEQ_FIELDS = ["bootstrap_code", "partitions", "boot_signature"]
    def __init__(self, _io, _parent=None, _root=None):
        super(MbrPartitionTable, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['bootstrap_code']['start'] = self._io.pos()
        self.bootstrap_code = self._io.read_bytes(446)
        self._debug['bootstrap_code']['end'] = self._io.pos()
        self._debug['partitions']['start'] = self._io.pos()
        self._debug['partitions']['arr'] = []
        self.partitions = []
        for i in range(4):
            self._debug['partitions']['arr'].append({'start': self._io.pos()})
            self.partitions.append(MbrPartitionTable.PartitionEntry(self._io, self, self._root))
            self._debug['partitions']['arr'][i]['end'] = self._io.pos()

        self._debug['partitions']['end'] = self._io.pos()
        self._debug['boot_signature']['start'] = self._io.pos()
        self.boot_signature = self._io.read_bytes(2)
        self._debug['boot_signature']['end'] = self._io.pos()
        if not self.boot_signature == b"\x55\xAA":
            raise kaitaistruct.ValidationNotEqualError(b"\x55\xAA", self.boot_signature, self._io, u"/seq/2")


    def _fetch_instances(self):
        pass
        for i in range(len(self.partitions)):
            pass
            self.partitions[i]._fetch_instances()


    class Chs(KaitaiStruct):
        SEQ_FIELDS = ["head", "b2", "b3"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MbrPartitionTable.Chs, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['head']['start'] = self._io.pos()
            self.head = self._io.read_u1()
            self._debug['head']['end'] = self._io.pos()
            self._debug['b2']['start'] = self._io.pos()
            self.b2 = self._io.read_u1()
            self._debug['b2']['end'] = self._io.pos()
            self._debug['b3']['start'] = self._io.pos()
            self.b3 = self._io.read_u1()
            self._debug['b3']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def cylinder(self):
            if hasattr(self, '_m_cylinder'):
                return self._m_cylinder

            self._m_cylinder = self.b3 + ((self.b2 & 192) << 2)
            return getattr(self, '_m_cylinder', None)

        @property
        def sector(self):
            if hasattr(self, '_m_sector'):
                return self._m_sector

            self._m_sector = self.b2 & 63
            return getattr(self, '_m_sector', None)


    class PartitionEntry(KaitaiStruct):
        SEQ_FIELDS = ["status", "chs_start", "partition_type", "chs_end", "lba_start", "num_sectors"]
        def __init__(self, _io, _parent=None, _root=None):
            super(MbrPartitionTable.PartitionEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['status']['start'] = self._io.pos()
            self.status = self._io.read_u1()
            self._debug['status']['end'] = self._io.pos()
            self._debug['chs_start']['start'] = self._io.pos()
            self.chs_start = MbrPartitionTable.Chs(self._io, self, self._root)
            self._debug['chs_start']['end'] = self._io.pos()
            self._debug['partition_type']['start'] = self._io.pos()
            self.partition_type = KaitaiStream.resolve_enum(MbrPartitionTable.PartitionType, self._io.read_u1())
            self._debug['partition_type']['end'] = self._io.pos()
            if not  ((self.partition_type == MbrPartitionTable.PartitionType.empty) or (self.partition_type == MbrPartitionTable.PartitionType.fat12) or (self.partition_type == MbrPartitionTable.PartitionType.xenix_root) or (self.partition_type == MbrPartitionTable.PartitionType.xenix_usr) or (self.partition_type == MbrPartitionTable.PartitionType.fat16_below_32m) or (self.partition_type == MbrPartitionTable.PartitionType.extended) or (self.partition_type == MbrPartitionTable.PartitionType.fat16) or (self.partition_type == MbrPartitionTable.PartitionType.hpfs_ntfs_exfat) or (self.partition_type == MbrPartitionTable.PartitionType.aix) or (self.partition_type == MbrPartitionTable.PartitionType.aix_bootable) or (self.partition_type == MbrPartitionTable.PartitionType.os2_boot_manager) or (self.partition_type == MbrPartitionTable.PartitionType.w95_fat32) or (self.partition_type == MbrPartitionTable.PartitionType.w95_fat32_lba) or (self.partition_type == MbrPartitionTable.PartitionType.w95_fat16_lba) or (self.partition_type == MbrPartitionTable.PartitionType.w95_extended_lba) or (self.partition_type == MbrPartitionTable.PartitionType.opus) or (self.partition_type == MbrPartitionTable.PartitionType.hidden_fat12) or (self.partition_type == MbrPartitionTable.PartitionType.compaq_diagnostics) or (self.partition_type == MbrPartitionTable.PartitionType.hidden_fat16_below_32m) or (self.partition_type == MbrPartitionTable.PartitionType.hidden_fat16) or (self.partition_type == MbrPartitionTable.PartitionType.hidden_hpfs_ntfs) or (self.partition_type == MbrPartitionTable.PartitionType.ast_smartsleep) or (self.partition_type == MbrPartitionTable.PartitionType.hidden_w95_fat32) or (self.partition_type == MbrPartitionTable.PartitionType.hidden_w95_fat32_lba) or (self.partition_type == MbrPartitionTable.PartitionType.hidden_w95_fat16_lba) or (self.partition_type == MbrPartitionTable.PartitionType.nec_dos) or (self.partition_type == MbrPartitionTable.PartitionType.hidden_ntfs_winre) or (self.partition_type == MbrPartitionTable.PartitionType.plan9) or (self.partition_type == MbrPartitionTable.PartitionType.partitionmagic_recovery) or (self.partition_type == MbrPartitionTable.PartitionType.venix_80286) or (self.partition_type == MbrPartitionTable.PartitionType.ppc_prep_boot) or (self.partition_type == MbrPartitionTable.PartitionType.sfs) or (self.partition_type == MbrPartitionTable.PartitionType.qnx4) or (self.partition_type == MbrPartitionTable.PartitionType.qnx4_second_part) or (self.partition_type == MbrPartitionTable.PartitionType.qnx4_third_part) or (self.partition_type == MbrPartitionTable.PartitionType.ontrack_dm) or (self.partition_type == MbrPartitionTable.PartitionType.ontrack_dm6_aux1) or (self.partition_type == MbrPartitionTable.PartitionType.cpm) or (self.partition_type == MbrPartitionTable.PartitionType.ontrack_dm6_aux3) or (self.partition_type == MbrPartitionTable.PartitionType.ontrack_dm6) or (self.partition_type == MbrPartitionTable.PartitionType.ez_drive) or (self.partition_type == MbrPartitionTable.PartitionType.golden_bow) or (self.partition_type == MbrPartitionTable.PartitionType.priam_edisk) or (self.partition_type == MbrPartitionTable.PartitionType.speedstor) or (self.partition_type == MbrPartitionTable.PartitionType.gnu_hurd_or_sysv) or (self.partition_type == MbrPartitionTable.PartitionType.novell_netware_286) or (self.partition_type == MbrPartitionTable.PartitionType.novell_netware_386) or (self.partition_type == MbrPartitionTable.PartitionType.disksecure_multi_boot) or (self.partition_type == MbrPartitionTable.PartitionType.pc_ix) or (self.partition_type == MbrPartitionTable.PartitionType.old_minix) or (self.partition_type == MbrPartitionTable.PartitionType.minix_old_linux) or (self.partition_type == MbrPartitionTable.PartitionType.linux_swap_solaris) or (self.partition_type == MbrPartitionTable.PartitionType.linux) or (self.partition_type == MbrPartitionTable.PartitionType.os2_hidden_or_intel_hibenation) or (self.partition_type == MbrPartitionTable.PartitionType.linux_extended) or (self.partition_type == MbrPartitionTable.PartitionType.ntfs_volume_set_1) or (self.partition_type == MbrPartitionTable.PartitionType.ntfs_volume_set_2) or (self.partition_type == MbrPartitionTable.PartitionType.linux_plaintext) or (self.partition_type == MbrPartitionTable.PartitionType.linux_lvm) or (self.partition_type == MbrPartitionTable.PartitionType.amoeba) or (self.partition_type == MbrPartitionTable.PartitionType.amoeba_bbt) or (self.partition_type == MbrPartitionTable.PartitionType.bsd_os) or (self.partition_type == MbrPartitionTable.PartitionType.ibm_thinkpad_hibernation) or (self.partition_type == MbrPartitionTable.PartitionType.freebsd) or (self.partition_type == MbrPartitionTable.PartitionType.openbsd) or (self.partition_type == MbrPartitionTable.PartitionType.nextstep) or (self.partition_type == MbrPartitionTable.PartitionType.darwin_ufs) or (self.partition_type == MbrPartitionTable.PartitionType.netbsd) or (self.partition_type == MbrPartitionTable.PartitionType.darwin_boot) or (self.partition_type == MbrPartitionTable.PartitionType.hfs_hfsplus) or (self.partition_type == MbrPartitionTable.PartitionType.bsdi_fs) or (self.partition_type == MbrPartitionTable.PartitionType.bsdi_swap) or (self.partition_type == MbrPartitionTable.PartitionType.boot_wizard_hidden) or (self.partition_type == MbrPartitionTable.PartitionType.acronis_fat32_lba) or (self.partition_type == MbrPartitionTable.PartitionType.solaris_boot) or (self.partition_type == MbrPartitionTable.PartitionType.solaris) or (self.partition_type == MbrPartitionTable.PartitionType.drdos_sec_fat12) or (self.partition_type == MbrPartitionTable.PartitionType.drdos_sec_fat16_below_32m) or (self.partition_type == MbrPartitionTable.PartitionType.drdos_sec_fat16) or (self.partition_type == MbrPartitionTable.PartitionType.syrinx) or (self.partition_type == MbrPartitionTable.PartitionType.non_fs_data) or (self.partition_type == MbrPartitionTable.PartitionType.cpm_ctos) or (self.partition_type == MbrPartitionTable.PartitionType.dell_utility) or (self.partition_type == MbrPartitionTable.PartitionType.bootit) or (self.partition_type == MbrPartitionTable.PartitionType.dos_access) or (self.partition_type == MbrPartitionTable.PartitionType.dos_ro) or (self.partition_type == MbrPartitionTable.PartitionType.speedstore_extended) or (self.partition_type == MbrPartitionTable.PartitionType.rufus_alignment) or (self.partition_type == MbrPartitionTable.PartitionType.beos_fs) or (self.partition_type == MbrPartitionTable.PartitionType.gpt) or (self.partition_type == MbrPartitionTable.PartitionType.efi) or (self.partition_type == MbrPartitionTable.PartitionType.linux_parisc_boot) or (self.partition_type == MbrPartitionTable.PartitionType.speedstor_1) or (self.partition_type == MbrPartitionTable.PartitionType.dos_secondary) or (self.partition_type == MbrPartitionTable.PartitionType.speedstore_large_partition) or (self.partition_type == MbrPartitionTable.PartitionType.vmware_vmfs) or (self.partition_type == MbrPartitionTable.PartitionType.vmware_vmkcore) or (self.partition_type == MbrPartitionTable.PartitionType.linux_raid_autodetect) or (self.partition_type == MbrPartitionTable.PartitionType.lanstep) or (self.partition_type == MbrPartitionTable.PartitionType.xenix_bbt)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.partition_type, self._io, u"/types/partition_entry/seq/2")
            self._debug['chs_end']['start'] = self._io.pos()
            self.chs_end = MbrPartitionTable.Chs(self._io, self, self._root)
            self._debug['chs_end']['end'] = self._io.pos()
            self._debug['lba_start']['start'] = self._io.pos()
            self.lba_start = self._io.read_u4le()
            self._debug['lba_start']['end'] = self._io.pos()
            self._debug['num_sectors']['start'] = self._io.pos()
            self.num_sectors = self._io.read_u4le()
            self._debug['num_sectors']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.chs_start._fetch_instances()
            self.chs_end._fetch_instances()



