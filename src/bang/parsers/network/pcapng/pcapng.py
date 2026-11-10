# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Pcapng(KaitaiStruct):
    """Test files: <https://github.com/hadrielk/pcapng-test-generator>
    
    .. seealso::
       Source - https://github.com/pcapng/pcapng
    """

    class HeaderTypes(IntEnum):
        interface_description = 1
        packet_block = 2
        simple_packet = 3
        name_resolution = 4
        interface_statistics = 5
        enhanced_packet = 6
        irig_timestamp = 7
        arinc_429 = 8
        systemd_journal_expert = 9
        decryption_secrets = 10
        process_event = 257
        connection_event = 258
        sysdig_machine_info = 513
        sysdig_machine_info_version_1 = 514
        sysdig_fd_list = 515
        sysdig_event = 516
        sysdig_interface_list = 517
        sysdig_user_list = 518
        sysdig_process_info_version_2 = 519
        sysdig_event_with_flags = 520
        sysdig_process_info_version_3 = 521
        sysdig_process_info_version_4 = 528
        sysdig_process_info_version_5 = 529
        sysdig_process_info_version_6 = 530
        sysdig_process_info_version_7 = 531
        custom = 2989
        section_header = 168627466
        custom2 = 1073744813

    class Linktype(IntEnum):
        null_linktype = 0
        ethernet = 1
        exp_ethernet = 2
        ax25 = 3
        pronet = 4
        chaos = 5
        ieee802_5 = 6
        arcnet_bsd = 7
        slip = 8
        ppp = 9
        fddi = 10
        redback_smartedge = 32
        ppp_hdlc = 50
        ppp_ether = 51
        symantec_firewall = 99
        atm_rfc1483 = 100
        raw = 101
        c_hdlc = 104
        ieee802_11 = 105
        atm_clip = 106
        frelay = 107
        loop = 108
        enc = 109
        netbsd_hdlc = 112
        linux_sll = 113
        ltalk = 114
        econet = 115
        ipfilter = 116
        pflog = 117
        cisco_ios = 118
        ieee802_11_prism = 119
        aironet_header = 120
        ip_over_fc = 122
        sunatm = 123
        rio = 124
        pci_exp = 125
        aurora = 126
        ieee802_11_radiotap = 127
        tzsp = 128
        arcnet_linux = 129
        juniper_mlppp = 130
        juniper_mlfr = 131
        juniper_es = 132
        juniper_ggsn = 133
        juniper_mfr = 134
        juniper_atm2 = 135
        juniper_services = 136
        juniper_atm1 = 137
        apple_ip_over_ieee1394 = 138
        mtp2_with_phdr = 139
        mtp2 = 140
        mtp3 = 141
        sccp = 142
        docsis = 143
        linux_irda = 144
        ibm_sp = 145
        ibm_sn = 146
        user0 = 147
        user1 = 148
        user2 = 149
        user3 = 150
        user4 = 151
        user5 = 152
        user6 = 153
        user7 = 154
        user8 = 155
        user9 = 156
        user10 = 157
        user11 = 158
        user12 = 159
        user13 = 160
        user14 = 161
        user15 = 162
        ieee802_11_avs = 163
        juniper_monitor = 164
        bacnet_ms_tp = 165
        ppp_pppd = 166
        juniper_pppoe = 167
        juniper_pppoe_atm = 168
        gprs_llc = 169
        gpf_t = 170
        gpf_f = 171
        gcom_t1e1 = 172
        gcom_serial = 173
        juniper_pic_peer = 174
        erf_eth = 175
        erf_pos = 176
        linux_lapd = 177
        juniper_ether = 178
        juniper_ppp = 179
        juniper_frelay = 180
        juniper_chdlc = 181
        mfr = 182
        juniper_vp = 183
        a429 = 184
        a653_icm = 185
        usb_freebsd = 186
        bluetooth_hci_h4 = 187
        ieee802_16_mac_cps = 188
        usb_linux = 189
        can20b = 190
        ieee802_15_4_linux = 191
        ppi = 192
        ieee802_16_mac_cps_radio = 193
        juniper_ism = 194
        ieee802_15_4_withfcs = 195
        sita = 196
        erf = 197
        raif1 = 198
        ipmb_kontron = 199
        juniper_st = 200
        bluetooth_hci_h4_with_phdr = 201
        ax25_kiss = 202
        lapd = 203
        ppp_with_dir = 204
        c_hdlc_with_dir = 205
        frelay_with_dir = 206
        lapb_with_dir = 207
        ipmb_linux = 209
        flexray = 210
        most = 211
        lin = 212
        x2e_serial = 213
        x2e_xoraya = 214
        ieee802_15_4_nonask_phy = 215
        linux_evdev = 216
        gsmtap_um = 217
        gsmtap_abis = 218
        mpls = 219
        usb_linux_mmapped = 220
        dect = 221
        aos = 222
        wihart = 223
        fc_2 = 224
        fc_2_with_frame_delims = 225
        ipnet = 226
        can_socketcan = 227
        ipv4 = 228
        ipv6 = 229
        ieee802_15_4_nofcs = 230
        dbus = 231
        juniper_vs = 232
        juniper_srx_e2e = 233
        juniper_fibrechannel = 234
        dvb_ci = 235
        mux27010 = 236
        stanag_5066_d_pdu = 237
        juniper_atm_cemic = 238
        nflog = 239
        netanalyzer = 240
        netanalyzer_transparent = 241
        ipoib = 242
        mpeg_2_ts = 243
        ng40 = 244
        nfc_llcp = 245
        pfsync = 246
        infiniband = 247
        sctp = 248
        usbpcap = 249
        rtac_serial = 250
        bluetooth_le_ll = 251
        wireshark_upper_pdu = 252
        netlink = 253
        bluetooth_linux_monitor = 254
        bluetooth_bredr_bb = 255
        bluetooth_le_ll_with_phdr = 256
        profibus_dl = 257
        pktap = 258
        epon = 259
        ipmi_hpm_2 = 260
        zwave_r1_r2 = 261
        zwave_r3 = 262
        wattstopper_dlm = 263
        iso_14443 = 264
        rds = 265
        usb_darwin = 266
        openflow = 267
        sdlc = 268
        ti_lln_sniffer = 269
        loratap = 270
        vsock = 271
        nordic_ble = 272
        docsis31_xra31 = 273
        ethernet_mpacket = 274
        displayport_aux = 275
        linux_sll2 = 276
        sercos_monitor = 277
        openvizsla = 278
        ebhscr = 279
        vpp_dispatch = 280
        dsa_tag_brcm = 281
        dsa_tag_brcm_prepend = 282
        ieee802_15_4_tap = 283
        dsa_tag_dsa = 284
        dsa_tag_edsa = 285
        elee = 286
        zwave_serial = 287
        usb_2_0 = 288
        atsc_alp = 289
        etw = 290
        netanalyzer_ng = 291
        zboss_ncp = 292
        usb_2_0_low_speed = 293
        usb_2_0_full_speed = 294
        usb_2_0_high_speed = 295
        auerswald_log = 296
        zwave_tap = 297
        silabs_debug_channel = 298
        fira_uci = 299
    SEQ_FIELDS = ["blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Pcapng, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['blocks']['start'] = self._io.pos()
        self._debug['blocks']['arr'] = []
        self.blocks = []
        i = 0
        while not self._io.is_eof():
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            self.blocks.append(Pcapng.Block(self._io, self, self._root))
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            i += 1

        self._debug['blocks']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.blocks)):
            pass
            self.blocks[i]._fetch_instances()


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["header_type", "len_block", "rest_of_block", "len_block2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcapng.Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['header_type']['start'] = self._io.pos()
            self.header_type = KaitaiStream.resolve_enum(Pcapng.HeaderTypes, self._io.read_u4le())
            self._debug['header_type']['end'] = self._io.pos()
            if not  ((self.header_type == Pcapng.HeaderTypes.interface_description) or (self.header_type == Pcapng.HeaderTypes.packet_block) or (self.header_type == Pcapng.HeaderTypes.simple_packet) or (self.header_type == Pcapng.HeaderTypes.name_resolution) or (self.header_type == Pcapng.HeaderTypes.interface_statistics) or (self.header_type == Pcapng.HeaderTypes.enhanced_packet) or (self.header_type == Pcapng.HeaderTypes.decryption_secrets) or (self.header_type == Pcapng.HeaderTypes.custom) or (self.header_type == Pcapng.HeaderTypes.section_header) or (self.header_type == Pcapng.HeaderTypes.custom2) or (self.header_type == Pcapng.HeaderTypes.irig_timestamp) or (self.header_type == Pcapng.HeaderTypes.arinc_429) or (self.header_type == Pcapng.HeaderTypes.systemd_journal_expert) or (self.header_type == Pcapng.HeaderTypes.process_event) or (self.header_type == Pcapng.HeaderTypes.connection_event) or (self.header_type == Pcapng.HeaderTypes.sysdig_machine_info) or (self.header_type == Pcapng.HeaderTypes.sysdig_machine_info_version_1) or (self.header_type == Pcapng.HeaderTypes.sysdig_fd_list) or (self.header_type == Pcapng.HeaderTypes.sysdig_event) or (self.header_type == Pcapng.HeaderTypes.sysdig_interface_list) or (self.header_type == Pcapng.HeaderTypes.sysdig_user_list) or (self.header_type == Pcapng.HeaderTypes.sysdig_process_info_version_2) or (self.header_type == Pcapng.HeaderTypes.sysdig_event_with_flags) or (self.header_type == Pcapng.HeaderTypes.sysdig_process_info_version_3) or (self.header_type == Pcapng.HeaderTypes.sysdig_process_info_version_4) or (self.header_type == Pcapng.HeaderTypes.sysdig_process_info_version_5) or (self.header_type == Pcapng.HeaderTypes.sysdig_process_info_version_6) or (self.header_type == Pcapng.HeaderTypes.sysdig_process_info_version_7)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.header_type, self._io, u"/types/block/seq/0")
            self._debug['len_block']['start'] = self._io.pos()
            self.len_block = self._io.read_u4le()
            self._debug['len_block']['end'] = self._io.pos()
            self._debug['rest_of_block']['start'] = self._io.pos()
            _on = self.header_type
            if _on == Pcapng.HeaderTypes.decryption_secrets:
                pass
                self._raw_rest_of_block = self._io.read_bytes((self.len_block - 4 * 2) - 4)
                _io__raw_rest_of_block = KaitaiStream(BytesIO(self._raw_rest_of_block))
                self.rest_of_block = Pcapng.DecryptionSecretsBlock(_io__raw_rest_of_block, self, self._root)
            elif _on == Pcapng.HeaderTypes.enhanced_packet:
                pass
                self._raw_rest_of_block = self._io.read_bytes((self.len_block - 4 * 2) - 4)
                _io__raw_rest_of_block = KaitaiStream(BytesIO(self._raw_rest_of_block))
                self.rest_of_block = Pcapng.EnhancedPacketBlock(_io__raw_rest_of_block, self, self._root)
            elif _on == Pcapng.HeaderTypes.interface_description:
                pass
                self._raw_rest_of_block = self._io.read_bytes((self.len_block - 4 * 2) - 4)
                _io__raw_rest_of_block = KaitaiStream(BytesIO(self._raw_rest_of_block))
                self.rest_of_block = Pcapng.InterfaceDescriptionBlock(_io__raw_rest_of_block, self, self._root)
            elif _on == Pcapng.HeaderTypes.interface_statistics:
                pass
                self._raw_rest_of_block = self._io.read_bytes((self.len_block - 4 * 2) - 4)
                _io__raw_rest_of_block = KaitaiStream(BytesIO(self._raw_rest_of_block))
                self.rest_of_block = Pcapng.InterfaceStatisticsBlock(_io__raw_rest_of_block, self, self._root)
            elif _on == Pcapng.HeaderTypes.name_resolution:
                pass
                self._raw_rest_of_block = self._io.read_bytes((self.len_block - 4 * 2) - 4)
                _io__raw_rest_of_block = KaitaiStream(BytesIO(self._raw_rest_of_block))
                self.rest_of_block = Pcapng.NameResolutionBlock(_io__raw_rest_of_block, self, self._root)
            elif _on == Pcapng.HeaderTypes.section_header:
                pass
                self._raw_rest_of_block = self._io.read_bytes((self.len_block - 4 * 2) - 4)
                _io__raw_rest_of_block = KaitaiStream(BytesIO(self._raw_rest_of_block))
                self.rest_of_block = Pcapng.SectionHeaderBlock(_io__raw_rest_of_block, self, self._root)
            else:
                pass
                self.rest_of_block = self._io.read_bytes((self.len_block - 4 * 2) - 4)
            self._debug['rest_of_block']['end'] = self._io.pos()
            self._debug['len_block2']['start'] = self._io.pos()
            self.len_block2 = self._io.read_u4le()
            self._debug['len_block2']['end'] = self._io.pos()
            if not self.len_block2 == self.len_block:
                raise kaitaistruct.ValidationNotEqualError(self.len_block, self.len_block2, self._io, u"/types/block/seq/3")


        def _fetch_instances(self):
            pass
            _on = self.header_type
            if _on == Pcapng.HeaderTypes.decryption_secrets:
                pass
                self.rest_of_block._fetch_instances()
            elif _on == Pcapng.HeaderTypes.enhanced_packet:
                pass
                self.rest_of_block._fetch_instances()
            elif _on == Pcapng.HeaderTypes.interface_description:
                pass
                self.rest_of_block._fetch_instances()
            elif _on == Pcapng.HeaderTypes.interface_statistics:
                pass
                self.rest_of_block._fetch_instances()
            elif _on == Pcapng.HeaderTypes.name_resolution:
                pass
                self.rest_of_block._fetch_instances()
            elif _on == Pcapng.HeaderTypes.section_header:
                pass
                self.rest_of_block._fetch_instances()
            else:
                pass


    class DecryptionSecretsBlock(KaitaiStruct):
        SEQ_FIELDS = ["len_original_packet"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcapng.DecryptionSecretsBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_original_packet']['start'] = self._io.pos()
            self.len_original_packet = self._io.read_u4le()
            self._debug['len_original_packet']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class EnhancedPacketBlock(KaitaiStruct):
        SEQ_FIELDS = ["interface_id", "timestamp", "len_captured_packet", "len_original_packet", "data", "padding", "options"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcapng.EnhancedPacketBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['interface_id']['start'] = self._io.pos()
            self.interface_id = self._io.read_u4le()
            self._debug['interface_id']['end'] = self._io.pos()
            self._debug['timestamp']['start'] = self._io.pos()
            self.timestamp = Pcapng.Timestamp(self._io, self, self._root)
            self._debug['timestamp']['end'] = self._io.pos()
            self._debug['len_captured_packet']['start'] = self._io.pos()
            self.len_captured_packet = self._io.read_u4le()
            self._debug['len_captured_packet']['end'] = self._io.pos()
            self._debug['len_original_packet']['start'] = self._io.pos()
            self.len_original_packet = self._io.read_u4le()
            self._debug['len_original_packet']['end'] = self._io.pos()
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self.len_captured_packet)
            self._debug['data']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self.len_captured_packet) % 4)
            self._debug['padding']['end'] = self._io.pos()
            self._debug['options']['start'] = self._io.pos()
            self._debug['options']['arr'] = []
            self.options = []
            i = 0
            while not self._io.is_eof():
                self._debug['options']['arr'].append({'start': self._io.pos()})
                self.options.append(Pcapng.Option(self._io, self, self._root))
                self._debug['options']['arr'][len(self.options) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['options']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.timestamp._fetch_instances()
            for i in range(len(self.options)):
                pass
                self.options[i]._fetch_instances()



    class InterfaceDescriptionBlock(KaitaiStruct):
        SEQ_FIELDS = ["linktype", "reserved", "snaplen", "options"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcapng.InterfaceDescriptionBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['linktype']['start'] = self._io.pos()
            self.linktype = KaitaiStream.resolve_enum(Pcapng.Linktype, self._io.read_u2le())
            self._debug['linktype']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(2)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['snaplen']['start'] = self._io.pos()
            self.snaplen = self._io.read_u4le()
            self._debug['snaplen']['end'] = self._io.pos()
            self._debug['options']['start'] = self._io.pos()
            self._debug['options']['arr'] = []
            self.options = []
            i = 0
            while not self._io.is_eof():
                self._debug['options']['arr'].append({'start': self._io.pos()})
                self.options.append(Pcapng.Option(self._io, self, self._root))
                self._debug['options']['arr'][len(self.options) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['options']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.options)):
                pass
                self.options[i]._fetch_instances()



    class InterfaceStatisticsBlock(KaitaiStruct):
        SEQ_FIELDS = ["interface_id", "timestamp", "options"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcapng.InterfaceStatisticsBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['interface_id']['start'] = self._io.pos()
            self.interface_id = self._io.read_u4le()
            self._debug['interface_id']['end'] = self._io.pos()
            self._debug['timestamp']['start'] = self._io.pos()
            self.timestamp = Pcapng.Timestamp(self._io, self, self._root)
            self._debug['timestamp']['end'] = self._io.pos()
            self._debug['options']['start'] = self._io.pos()
            self._debug['options']['arr'] = []
            self.options = []
            i = 0
            while not self._io.is_eof():
                self._debug['options']['arr'].append({'start': self._io.pos()})
                self.options.append(Pcapng.Option(self._io, self, self._root))
                self._debug['options']['arr'][len(self.options) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['options']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.timestamp._fetch_instances()
            for i in range(len(self.options)):
                pass
                self.options[i]._fetch_instances()



    class NameResolutionBlock(KaitaiStruct):
        SEQ_FIELDS = ["records", "options"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcapng.NameResolutionBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['records']['start'] = self._io.pos()
            self._debug['records']['arr'] = []
            self.records = []
            i = 0
            while not self._io.is_eof():
                self._debug['records']['arr'].append({'start': self._io.pos()})
                self.records.append(Pcapng.Record(self._io, self, self._root))
                self._debug['records']['arr'][len(self.records) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['records']['end'] = self._io.pos()
            self._debug['options']['start'] = self._io.pos()
            self._debug['options']['arr'] = []
            self.options = []
            i = 0
            while not self._io.is_eof():
                self._debug['options']['arr'].append({'start': self._io.pos()})
                self.options.append(Pcapng.Option(self._io, self, self._root))
                self._debug['options']['arr'][len(self.options) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['options']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.records)):
                pass
                self.records[i]._fetch_instances()

            for i in range(len(self.options)):
                pass
                self.options[i]._fetch_instances()



    class Option(KaitaiStruct):

        class Options(IntEnum):
            end = 0
            custom1 = 2988
            custom2 = 2989
            custom3 = 19372
            custom4 = 19373
        SEQ_FIELDS = ["type", "len_value", "value", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcapng.Option, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Pcapng.Option.Options, self._io.read_u2le())
            self._debug['type']['end'] = self._io.pos()
            self._debug['len_value']['start'] = self._io.pos()
            self.len_value = self._io.read_u2le()
            self._debug['len_value']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_bytes(self.len_value)
            self._debug['value']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self.len_value) % 4)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Record(KaitaiStruct):

        class NameRecords(IntEnum):
            end = 0
            ipv4 = 1
            ipv6 = 2
        SEQ_FIELDS = ["type", "len_value", "value", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcapng.Record, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['type']['start'] = self._io.pos()
            self.type = KaitaiStream.resolve_enum(Pcapng.Record.NameRecords, self._io.read_u2le())
            self._debug['type']['end'] = self._io.pos()
            if not  ((self.type == Pcapng.Record.NameRecords.end) or (self.type == Pcapng.Record.NameRecords.ipv4) or (self.type == Pcapng.Record.NameRecords.ipv6)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.type, self._io, u"/types/record/seq/0")
            self._debug['len_value']['start'] = self._io.pos()
            self.len_value = self._io.read_u2le()
            self._debug['len_value']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_bytes(self.len_value)
            self._debug['value']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self.len_value) % 4)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class SectionHeaderBlock(KaitaiStruct):
        SEQ_FIELDS = ["byteorder_magic", "version", "len_section", "options"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcapng.SectionHeaderBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['byteorder_magic']['start'] = self._io.pos()
            self.byteorder_magic = self._io.read_bytes(4)
            self._debug['byteorder_magic']['end'] = self._io.pos()
            self._debug['version']['start'] = self._io.pos()
            self.version = Pcapng.Version(self._io, self, self._root)
            self._debug['version']['end'] = self._io.pos()
            self._debug['len_section']['start'] = self._io.pos()
            self.len_section = self._io.read_s8le()
            self._debug['len_section']['end'] = self._io.pos()
            self._debug['options']['start'] = self._io.pos()
            self._debug['options']['arr'] = []
            self.options = []
            i = 0
            while not self._io.is_eof():
                self._debug['options']['arr'].append({'start': self._io.pos()})
                self.options.append(Pcapng.Option(self._io, self, self._root))
                self._debug['options']['arr'][len(self.options) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['options']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            self.version._fetch_instances()
            for i in range(len(self.options)):
                pass
                self.options[i]._fetch_instances()



    class Timestamp(KaitaiStruct):
        SEQ_FIELDS = ["high", "low"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcapng.Timestamp, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['high']['start'] = self._io.pos()
            self.high = self._io.read_u4le()
            self._debug['high']['end'] = self._io.pos()
            self._debug['low']['start'] = self._io.pos()
            self.low = self._io.read_u4le()
            self._debug['low']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Version(KaitaiStruct):
        SEQ_FIELDS = ["major", "minor"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Pcapng.Version, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['major']['start'] = self._io.pos()
            self.major = self._io.read_u2le()
            self._debug['major']['end'] = self._io.pos()
            if not self.major == 1:
                raise kaitaistruct.ValidationNotEqualError(1, self.major, self._io, u"/types/version/seq/0")
            self._debug['minor']['start'] = self._io.pos()
            self.minor = self._io.read_u2le()
            self._debug['minor']['end'] = self._io.pos()
            if not self.minor == 0:
                raise kaitaistruct.ValidationNotEqualError(0, self.minor, self._io, u"/types/version/seq/1")


        def _fetch_instances(self):
            pass



