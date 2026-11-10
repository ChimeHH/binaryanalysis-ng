# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Qcdt(KaitaiStruct):
    """Format of Qualcomm DTB files. Note: the device entries can all point to
    the same entry as DTB files can be shared between devices.
    
    .. seealso::
       (v1) - https://gitlab.com/Codeaurora/platform_system_core/-/raw/83b5d524c5/dtbtool/dtbtool.txt
    
    
    .. seealso::
       (v2) - https://raw.githubusercontent.com/omnirom/android_device_lge_g4-common/android-6.0/dtbtool/dtbtool.txt
    
    
    .. seealso::
       (v3) - https://raw.githubusercontent.com/CyanogenMod/android_device_qcom_common/cm-14.1/dtbtool/dtbtool.txt
    
    
    .. seealso::
       Source - https://source.codeaurora.org/quic/kernel/skales/plain/dtbTool?id=1.6.0
    
    
    .. seealso::
       web.archive.org/web/20160402060151if_/https://developer.qualcomm.com/qfile/28821/lm80-p0436-1_little_kernel_boot_loader_overview.pdf (section 2.4.1)
    
    
    .. seealso::
       Source - https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/soc/qcom/socinfo.c?id=b0bc160c311a0e7163c00a7e66116d28ce9771df
    
    
    .. seealso::
       Source - https://android.googlesource.com/kernel/msm/+/android-7.1.0_r0.2/drivers/soc/qcom/socinfo.c
    
    
    .. seealso::
       Source - https://github.com/brinlyau/P810D02_ZTE_T792_KitKat_3.4/blob/master/P810D02_ZTE_T792_KitKat_340_kernel/arch/arm/mach-msm/socinfo.c
    
    
    .. seealso::
       Source - https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/include/dt-bindings/arm/qcom,ids.h?id=f5bbbfec59b4e2fb7520a91de3df8a6174325d6a
    """

    class PlatformIds(IntEnum):
        cdp = 1
        ffa = 2
        fluid = 3
        fusion = 4
        oem = 5
        qt = 6
        mtp_mdm = 7
        mtp = 8
        liquid = 9
        dragonboard = 10
        qrd = 11
        evb = 12
        hrd = 13
        dtv = 14
        rumi = 15
        virtio = 16
        xpm = 20
        rcm = 21
        stp = 23
        sbc = 24
        adp = 25
        cls = 29
        ttp = 30
        hdk = 31
        iot = 32
        idp = 34

    class PmicIds(IntEnum):
        unknown = 0
        pm8941 = 1
        pm8841 = 2
        pm8019 = 3
        pm8026 = 4
        pm8110 = 5
        pma8084 = 6
        pmi8962 = 7
        pmd9635 = 8
        pm8994 = 9
        pmi8994 = 10
        pm8916 = 11
        pm8004 = 12
        pm8909 = 13
        pm2433 = 14
        pmd9655 = 15
        pm8950 = 16
        pmi8950 = 17
        pmk8001 = 18
        pmi8996 = 19
        pm8998 = 20
        pmi8998 = 21
        pm8953 = 22
        smb1380 = 23
        pm8005 = 24
        pm8937 = 25
        pm660l = 26
        pm660 = 27
        pm8150 = 30
        pm8150l = 31
        pm8150b = 32
        pmk8002 = 33
        pm8009 = 36
        pmi632 = 37
        pm8150c = 38
        pm6150 = 40
        smb2351 = 41
        pm8008 = 44
        pm6125 = 45
        pm7250b = 46
        pmk8350 = 47
        pm8350 = 48
        pm8350c = 49
        pm8350b = 50
        pmr735a = 51
        pmr735b = 52
        pm6350 = 54
        pm2250 = 55
        pm8450 = 58
        pm8010 = 65
        pm8550vs = 69
        pm8550ve = 70
        pm8550b = 71
        pmr735d = 72
        pm8550 = 73
        pmk8550 = 74
        pm7550ba = 76
        pmm8650au = 78
        pmm8650au_psail = 79
        pm7550 = 80
        pmc8380 = 82
        smb2360 = 83
        pm8750b = 86
        pmd8028 = 87
        pmc1020h = 88
        pmiv0104 = 89
        pmiv0102 = 90
        pmiv0108 = 91
        pmk8850 = 92
        pmh0101 = 93
        pmau0102 = 94
        smb2370 = 95
        pmh0104 = 96
        pmh0110 = 97
        pmcx0102 = 98

    class SocIds(IntEnum):
        msm7x01_1 = 1
        msm7x01_2 = 16
        msm7x01_3 = 17
        msm7x01_4 = 18
        msm7x01_5 = 19
        msm7x25_1 = 20
        msm7225 = 21
        msm7x01_6 = 23
        msm7525 = 24
        msm7x01_7 = 25
        msm7x01_8 = 26
        msm7625 = 27
        msm8x50_1 = 30
        msm7x01_9 = 32
        msm7x01_10 = 33
        msm7x01_11 = 34
        msm7x01_12 = 35
        msm8x50_2 = 36
        msm8x50_3 = 37
        msm8x50_4 = 38
        msm7x25_2 = 39
        msm7x25_3 = 40
        msm7x25_5 = 42
        msm7x27_1 = 43
        msm7x27_2 = 44
        msm7x30_1 = 59
        msm7x30_2 = 60
        msm7x27_3 = 61
        msm7625_1 = 62
        msm7225_1 = 63
        msm7225_2 = 66
        msm7227_1 = 67
        msm7627_1 = 68
        msm7627_2 = 69
        msm8260 = 70
        msm8660 = 71
        msm8x55_1 = 74
        msm8x55_2 = 75
        msm8x55_3 = 85
        apq8060 = 86
        msm8960 = 87
        msm7x25a_1 = 88
        msm7x25a_2 = 89
        msm7x27a_1 = 90
        msm7x27a_2 = 91
        msm7x27a_3 = 92
        fsm_9xxx_1 = 94
        fsm_9xxx_2 = 95
        msm7x25a_3 = 96
        msm7x27a_4 = 97
        msm7x25aa_1 = 98
        msm7x25aa_2 = 99
        msm7x25aa_3 = 100
        msm7x27aa_1 = 101
        msm7x27aa_2 = 102
        msm7x27aa_3 = 103
        msm9615_1 = 104
        msm9615_2 = 105
        msm9615_3 = 106
        msm9615_4 = 107
        apq8064 = 109
        msm8930 = 116
        msm8630 = 117
        msm8230 = 118
        apq8030 = 119
        msm8627 = 120
        msm8227 = 121
        msm8660a = 122
        msm8260a = 123
        apq8060a = 124
        msm8974 = 126
        msm8225 = 127
        msm8625_2 = 128
        msm8625 = 129
        mpq8064 = 130
        msm7x25ab_1 = 131
        msm7x25ab_2 = 132
        msm7x25ab_3 = 133
        msm9625_1 = 134
        msm7x25ab_4 = 135
        msm8960ab = 138
        apq8060ab = 139
        msm8260ab = 140
        msm8660ab = 141
        msm8930aa = 142
        msm8630aa = 143
        msm8230aa = 144
        msm8626 = 145
        msm8610 = 147
        msm9625_2 = 148
        msm9625_3 = 149
        msm9625_4 = 150
        msm9625_5 = 151
        msm9625_6 = 152
        apq8064ab = 153
        msm8930ab = 154
        msm8630ab = 155
        msm8230ab = 156
        apq8030ab = 157
        msm8226 = 158
        msm8526 = 159
        apq8030aa = 160
        msm8110 = 161
        msm8210 = 162
        msm8810 = 163
        msm8212 = 164
        msm8612 = 165
        msm8112 = 166
        msm8125 = 167
        msm8225q = 168
        msm8625q = 169
        msm8125q = 170
        apq8064aa = 172
        msm9625_7 = 173
        msm9625_8 = 174
        msm9625_9 = 175
        apq8084 = 178
        msm8130 = 179
        msm8130aa = 180
        msm8130ab = 181
        msm8627aa = 182
        msm8227aa = 183
        apq8074 = 184
        msm8274 = 185
        msm8674 = 186
        mdm9635 = 187
        msm8974_pro_ac = 194
        msm8126 = 198
        apq8026 = 199
        msm8926 = 200
        ipq8062 = 201
        ipq8064 = 202
        ipq8066 = 203
        ipq8068 = 204
        msm8326 = 205
        msm8916 = 206
        msm8994 = 207
        apq8074pro_aa = 208
        apq8074pro_ab = 209
        apq8074pro_ac = 210
        msm8274pro_aa = 211
        msm8274pro_ab = 212
        msm8274pro_ac = 213
        msm8674pro_aa = 214
        msm8674pro_ab = 215
        msm8674pro_ac = 216
        msm8974pro_aa = 217
        msm8974pro_ab = 218
        apq8028 = 219
        msm8128 = 220
        msm8228 = 221
        msm8528 = 222
        msm8628 = 223
        msm8928 = 224
        msm8510 = 225
        msm8512 = 226
        msm8936 = 233
        mdm9640 = 234
        msm8939 = 239
        apq8036 = 240
        apq8039 = 241
        msm8236 = 242
        msm8636 = 243
        apq8064_au = 244
        msm8909 = 245
        msm8996 = 246
        apq8016 = 247
        msm8216 = 248
        msm8116 = 249
        msm8616 = 250
        msm8992 = 251
        apq8092 = 252
        apq8094 = 253
        msm8209 = 258
        msm8208 = 259
        mdm9209 = 260
        mdm9309 = 261
        mdm9609 = 262
        msm8239 = 263
        msm8952 = 264
        apq8009 = 265
        msm8956 = 266
        msm8929 = 268
        msm8629 = 269
        msm8229 = 270
        apq8029 = 271
        ipq4019 = 273
        apq8056 = 274
        msm8609 = 275
        apq8076 = 277
        msm8976 = 278
        mdm9650 = 279
        ipq8065 = 280
        ipq8069 = 281
        mdm9655 = 283
        mdm9250 = 284
        mdm9255 = 285
        mdm9350 = 286
        apq8052 = 289
        mdm9607 = 290
        apq8096 = 291
        msm8998 = 292
        msm8953 = 293
        msm8937 = 294
        apq8037 = 295
        mdm8207 = 296
        mdm9207 = 297
        mdm9307 = 298
        mdm9628 = 299
        msm8909w = 300
        apq8009w = 301
        msm8996l = 302
        msm8917 = 303
        apq8053 = 304
        msm8996sg = 305
        apq8017 = 307
        msm8217 = 308
        msm8617 = 309
        msm8996au = 310
        apq8096au = 311
        apq8096sg = 312
        msm8940 = 313
        sdx201 = 314
        sdm660 = 317
        sdm630 = 318
        apq8098 = 319
        msm8920 = 320
        sdm845 = 321
        mdm9206 = 322
        sda660 = 324
        sdm658 = 325
        sda658 = 326
        sda630 = 327
        msm8905 = 331
        sdx202 = 333
        sdm670 = 336
        sdm450 = 338
        sm8150 = 339
        sda845 = 341
        sdm636 = 345
        sda636 = 346
        sdm632 = 349
        sda632 = 350
        sda450 = 351
        sdm439 = 353
        sdm429 = 354
        sm8250 = 356
        sa8155 = 362
        sda439 = 363
        sda429 = 364
        sm7150 = 365
        sm7150p = 366
        ipq8070 = 375
        ipq8071 = 376
        qm215 = 386
        ipq8072a = 389
        ipq8074a = 390
        ipq8076a = 391
        sm6125 = 394
        ipq8070a = 395
        ipq8071a = 396
        ipq8172 = 397
        ipq8173 = 398
        ipq8174 = 399
        ipq6018 = 402
        ipq6028 = 403
        sdm429w = 416
        sm4250 = 417
        ipq6000 = 421
        ipq6010 = 422
        sc7180 = 425
        sm6350 = 434
        qcm2150 = 436
        sda429w = 437
        sm8350 = 439
        qcm2290 = 441
        sm7125 = 443
        sm6115 = 444
        ipq5010 = 446
        ipq5018 = 447
        ipq5028 = 448
        sc8280xp = 449
        ipq6005 = 453
        qrb5165 = 455
        sm8450 = 457
        sm7225 = 459
        sa8295p = 460
        sa8540p = 461
        qcm4290 = 469
        qcs4290 = 470
        sm7325 = 475
        sm8450_1 = 480
        sm8450_2 = 482
        sc7280 = 487
        sc7180p = 495
        qcm6490 = 497
        qcs6490 = 498
        sm7325p = 499
        ipq5000 = 503
        ipq0509 = 504
        ipq0518 = 505
        sm7450 = 506
        sm6375 = 507
        ipq9514 = 510
        ipq9550 = 511
        ipq9554 = 512
        ipq9570 = 513
        ipq9574 = 514
        sm8550 = 519
        ipq5016 = 520
        ipq9510 = 521
        qrb4210 = 523
        qrb2210 = 524
        sar2130p = 525
        sm8475 = 530
        sm8475p = 531
        sa8255p = 532
        sa8650p = 533
        sa8775p = 534
        qru1000 = 539
        sm8475_2 = 540
        qdu1000 = 545
        sm7450p = 547
        x1e80100 = 555
        sm8650 = 557
        sm4450 = 568
        ipq5019 = 569
        sar1130p = 579
        qdu1010 = 587
        qru1032 = 588
        qru1052 = 589
        qru1062 = 590
        ipq5332 = 592
        ipq5322 = 593
        ipq5312 = 594
        ipq5302 = 595
        qcs8550 = 603
        qcm8550 = 604
        sm8750 = 618
        ipq5300 = 624
        sm7635 = 636
        sm6650 = 640
        sm6650p = 641
        ipq5321 = 650
        ipq5424 = 651
        qcm6690 = 657
        qcs6690 = 658
        sm7750 = 659
        sm8850 = 660
        qcs9100 = 667
        ipq5404 = 671
        qcs8300 = 674
        qcs8275 = 675
        qcs9075 = 676
        qcs615 = 680
        sa8797p = 690
        cq7790m = 731
        cq7790s = 732
        cq2390m = 756
        cq2390s = 758
        iq2390s = 759
        ipq5200 = 765
        ipq5210 = 766
        qcf2200 = 767
        qcf3200 = 768
        qcf3210 = 769
        ipq9620 = 770
        ipq9650 = 771
        ipq9610 = 778
        ipq9630 = 779
        ipq9640 = 780
        ipq9670 = 781
    SEQ_FIELDS = ["magic", "version", "num_dtbs", "device_entries"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Qcdt, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\x51\x43\x44\x54":
            raise kaitaistruct.ValidationNotEqualError(b"\x51\x43\x44\x54", self.magic, self._io, u"/seq/0")
        self._debug['version']['start'] = self._io.pos()
        self.version = self._io.read_u4le()
        self._debug['version']['end'] = self._io.pos()
        if not  ((self.version == 1) or (self.version == 2) or (self.version == 3)) :
            raise kaitaistruct.ValidationNotAnyOfError(self.version, self._io, u"/seq/1")
        self._debug['num_dtbs']['start'] = self._io.pos()
        self.num_dtbs = self._io.read_u4le()
        self._debug['num_dtbs']['end'] = self._io.pos()
        self._debug['device_entries']['start'] = self._io.pos()
        self._debug['device_entries']['arr'] = []
        self.device_entries = []
        for i in range(self.num_dtbs):
            self._debug['device_entries']['arr'].append({'start': self._io.pos()})
            self.device_entries.append(Qcdt.DeviceEntry(self._io, self, self._root))
            self._debug['device_entries']['arr'][i]['end'] = self._io.pos()

        self._debug['device_entries']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.device_entries)):
            pass
            self.device_entries[i]._fetch_instances()


    class DeviceEntry(KaitaiStruct):
        SEQ_FIELDS = ["platform_id", "variant_id", "subtype_id", "soc_revision", "pmic0", "pmic1", "pmic2", "pmic3", "ofs_dtb", "len_dtb"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Qcdt.DeviceEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['platform_id']['start'] = self._io.pos()
            self.platform_id = KaitaiStream.resolve_enum(Qcdt.SocIds, self._io.read_u4le())
            self._debug['platform_id']['end'] = self._io.pos()
            self._debug['variant_id']['start'] = self._io.pos()
            self.variant_id = self._io.read_u4le()
            self._debug['variant_id']['end'] = self._io.pos()
            if self._root.version > 1:
                pass
                self._debug['subtype_id']['start'] = self._io.pos()
                self.subtype_id = self._io.read_u4le()
                self._debug['subtype_id']['end'] = self._io.pos()

            self._debug['soc_revision']['start'] = self._io.pos()
            self.soc_revision = self._io.read_u4le()
            self._debug['soc_revision']['end'] = self._io.pos()
            if self._root.version > 2:
                pass
                self._debug['pmic0']['start'] = self._io.pos()
                self.pmic0 = self._io.read_u4le()
                self._debug['pmic0']['end'] = self._io.pos()

            if self._root.version > 2:
                pass
                self._debug['pmic1']['start'] = self._io.pos()
                self.pmic1 = self._io.read_u4le()
                self._debug['pmic1']['end'] = self._io.pos()

            if self._root.version > 2:
                pass
                self._debug['pmic2']['start'] = self._io.pos()
                self.pmic2 = self._io.read_u4le()
                self._debug['pmic2']['end'] = self._io.pos()

            if self._root.version > 2:
                pass
                self._debug['pmic3']['start'] = self._io.pos()
                self.pmic3 = self._io.read_u4le()
                self._debug['pmic3']['end'] = self._io.pos()

            self._debug['ofs_dtb']['start'] = self._io.pos()
            self.ofs_dtb = self._io.read_u4le()
            self._debug['ofs_dtb']['end'] = self._io.pos()
            self._debug['len_dtb']['start'] = self._io.pos()
            self.len_dtb = self._io.read_u4le()
            self._debug['len_dtb']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            if self._root.version > 1:
                pass

            if self._root.version > 2:
                pass

            if self._root.version > 2:
                pass

            if self._root.version > 2:
                pass

            if self._root.version > 2:
                pass

            _ = self.data
            if hasattr(self, '_m_data'):
                pass


        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data

            _pos = self._io.pos()
            self._io.seek(self.ofs_dtb)
            self._debug['_m_data']['start'] = self._io.pos()
            self._m_data = self._io.read_bytes(self.len_dtb)
            self._debug['_m_data']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_data', None)



