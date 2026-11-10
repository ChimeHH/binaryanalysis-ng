# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Minix1l(KaitaiStruct):
    SEQ_FIELDS = ["bootblock", "superblock", "inodes_bitmap", "zones_bitmap", "inodes", "padding"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Minix1l, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['bootblock']['start'] = self._io.pos()
        self.bootblock = self._io.read_bytes(self.block_size)
        self._debug['bootblock']['end'] = self._io.pos()
        self._debug['superblock']['start'] = self._io.pos()
        self._raw_superblock = self._io.read_bytes(self.block_size)
        _io__raw_superblock = KaitaiStream(BytesIO(self._raw_superblock))
        self.superblock = Minix1l.Superblock(_io__raw_superblock, self, self._root)
        self._debug['superblock']['end'] = self._io.pos()
        self._debug['inodes_bitmap']['start'] = self._io.pos()
        self.inodes_bitmap = self._io.read_bytes(self.superblock.num_inode_bitmap_blocks * self.block_size)
        self._debug['inodes_bitmap']['end'] = self._io.pos()
        self._debug['zones_bitmap']['start'] = self._io.pos()
        self.zones_bitmap = self._io.read_bytes(self.superblock.num_zone_bitmap_blocks * self.block_size)
        self._debug['zones_bitmap']['end'] = self._io.pos()
        self._debug['inodes']['start'] = self._io.pos()
        self._debug['inodes']['arr'] = []
        self.inodes = []
        for i in range(self.superblock.num_inodes):
            self._debug['inodes']['arr'].append({'start': self._io.pos()})
            self.inodes.append(Minix1l.Inode(self._io, self, self._root))
            self._debug['inodes']['arr'][i]['end'] = self._io.pos()

        self._debug['inodes']['end'] = self._io.pos()
        self._debug['padding']['start'] = self._io.pos()
        self.padding = self._io.read_bytes(-(self._io.pos()) % self.block_size)
        self._debug['padding']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.superblock._fetch_instances()
        for i in range(len(self.inodes)):
            pass
            self.inodes[i]._fetch_instances()

        _ = self.zones
        if hasattr(self, '_m_zones'):
            pass
            for i in range(len(self._m_zones)):
                pass
                self._m_zones[i]._fetch_instances()



    class DoubleIndirectZoneNumber(KaitaiStruct):
        SEQ_FIELDS = ["number"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Minix1l.DoubleIndirectZoneNumber, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['number']['start'] = self._io.pos()
            self.number = self._io.read_u2le()
            self._debug['number']['end'] = self._io.pos()
            if not self.number <= self._root.superblock.num_zones:
                raise kaitaistruct.ValidationGreaterThanError(self._root.superblock.num_zones, self.number, self._io, u"/types/double_indirect_zone_number/seq/0")


        def _fetch_instances(self):
            pass
            _ = self.zone_data
            if hasattr(self, '_m_zone_data'):
                pass
                for i in range(len(self._m_zone_data)):
                    pass
                    self._m_zone_data[i]._fetch_instances()



        @property
        def zone_data(self):
            if hasattr(self, '_m_zone_data'):
                return self._m_zone_data

            if self.number != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.number * self._root.block_size)
                self._debug['_m_zone_data']['start'] = io.pos()
                self._debug['_m_zone_data']['arr'] = []
                self._m_zone_data = []
                for i in range(self._root.block_size // 2):
                    self._debug['_m_zone_data']['arr'].append({'start': io.pos()})
                    self._m_zone_data.append(Minix1l.IndirectZoneNumber(io, self, self._root))
                    self._debug['_m_zone_data']['arr'][i]['end'] = io.pos()

                self._debug['_m_zone_data']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_zone_data', None)


    class IndirectZoneNumber(KaitaiStruct):
        SEQ_FIELDS = ["number"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Minix1l.IndirectZoneNumber, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['number']['start'] = self._io.pos()
            self.number = self._io.read_u2le()
            self._debug['number']['end'] = self._io.pos()
            if not self.number <= self._root.superblock.num_zones:
                raise kaitaistruct.ValidationGreaterThanError(self._root.superblock.num_zones, self.number, self._io, u"/types/indirect_zone_number/seq/0")


        def _fetch_instances(self):
            pass
            _ = self.zone_data
            if hasattr(self, '_m_zone_data'):
                pass
                for i in range(len(self._m_zone_data)):
                    pass
                    self._m_zone_data[i]._fetch_instances()



        @property
        def zone_data(self):
            if hasattr(self, '_m_zone_data'):
                return self._m_zone_data

            if self.number != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.number * self._root.block_size)
                self._debug['_m_zone_data']['start'] = io.pos()
                self._debug['_m_zone_data']['arr'] = []
                self._m_zone_data = []
                for i in range(self._root.block_size // 2):
                    self._debug['_m_zone_data']['arr'].append({'start': io.pos()})
                    self._m_zone_data.append(Minix1l.ZoneNumber(io, self, self._root))
                    self._debug['_m_zone_data']['arr'][i]['end'] = io.pos()

                self._debug['_m_zone_data']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_zone_data', None)


    class Inode(KaitaiStruct):
        SEQ_FIELDS = ["mode", "uid", "size", "time", "gid", "links", "direct_zone_numbers", "indirect_zone_number", "double_indirect_zone_number"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Minix1l.Inode, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['mode']['start'] = self._io.pos()
            self.mode = self._io.read_u2le()
            self._debug['mode']['end'] = self._io.pos()
            self._debug['uid']['start'] = self._io.pos()
            self.uid = self._io.read_u2le()
            self._debug['uid']['end'] = self._io.pos()
            self._debug['size']['start'] = self._io.pos()
            self.size = self._io.read_u4le()
            self._debug['size']['end'] = self._io.pos()
            self._debug['time']['start'] = self._io.pos()
            self.time = self._io.read_u4le()
            self._debug['time']['end'] = self._io.pos()
            self._debug['gid']['start'] = self._io.pos()
            self.gid = self._io.read_u1()
            self._debug['gid']['end'] = self._io.pos()
            self._debug['links']['start'] = self._io.pos()
            self.links = self._io.read_u1()
            self._debug['links']['end'] = self._io.pos()
            self._debug['direct_zone_numbers']['start'] = self._io.pos()
            self._debug['direct_zone_numbers']['arr'] = []
            self.direct_zone_numbers = []
            for i in range(7):
                self._debug['direct_zone_numbers']['arr'].append({'start': self._io.pos()})
                self.direct_zone_numbers.append(Minix1l.ZoneNumber(self._io, self, self._root))
                self._debug['direct_zone_numbers']['arr'][i]['end'] = self._io.pos()

            self._debug['direct_zone_numbers']['end'] = self._io.pos()
            self._debug['indirect_zone_number']['start'] = self._io.pos()
            self.indirect_zone_number = Minix1l.IndirectZoneNumber(self._io, self, self._root)
            self._debug['indirect_zone_number']['end'] = self._io.pos()
            self._debug['double_indirect_zone_number']['start'] = self._io.pos()
            self.double_indirect_zone_number = Minix1l.DoubleIndirectZoneNumber(self._io, self, self._root)
            self._debug['double_indirect_zone_number']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.direct_zone_numbers)):
                pass
                self.direct_zone_numbers[i]._fetch_instances()

            self.indirect_zone_number._fetch_instances()
            self.double_indirect_zone_number._fetch_instances()


    class Superblock(KaitaiStruct):
        SEQ_FIELDS = ["num_inodes", "num_zones", "num_inode_bitmap_blocks", "num_zone_bitmap_blocks", "first_data_zone", "size_log_zone", "max_size", "magic", "state"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Minix1l.Superblock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['num_inodes']['start'] = self._io.pos()
            self.num_inodes = self._io.read_u2le()
            self._debug['num_inodes']['end'] = self._io.pos()
            if not self.num_inodes >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.num_inodes, self._io, u"/types/superblock/seq/0")
            self._debug['num_zones']['start'] = self._io.pos()
            self.num_zones = self._io.read_u2le()
            self._debug['num_zones']['end'] = self._io.pos()
            if not self.num_zones >= 1:
                raise kaitaistruct.ValidationLessThanError(1, self.num_zones, self._io, u"/types/superblock/seq/1")
            self._debug['num_inode_bitmap_blocks']['start'] = self._io.pos()
            self.num_inode_bitmap_blocks = self._io.read_u2le()
            self._debug['num_inode_bitmap_blocks']['end'] = self._io.pos()
            if not self.num_inode_bitmap_blocks <= self._root._io.size() // self._root.block_size:
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size() // self._root.block_size, self.num_inode_bitmap_blocks, self._io, u"/types/superblock/seq/2")
            self._debug['num_zone_bitmap_blocks']['start'] = self._io.pos()
            self.num_zone_bitmap_blocks = self._io.read_u2le()
            self._debug['num_zone_bitmap_blocks']['end'] = self._io.pos()
            if not self.num_zone_bitmap_blocks <= self._root._io.size() // self._root.block_size:
                raise kaitaistruct.ValidationGreaterThanError(self._root._io.size() // self._root.block_size, self.num_zone_bitmap_blocks, self._io, u"/types/superblock/seq/3")
            self._debug['first_data_zone']['start'] = self._io.pos()
            self.first_data_zone = self._io.read_u2le()
            self._debug['first_data_zone']['end'] = self._io.pos()
            if not self.first_data_zone >= ((2 + self.num_inode_bitmap_blocks) + self.num_zone_bitmap_blocks) + (self.num_inodes // self._root.inode_size) % self._root.block_size:
                raise kaitaistruct.ValidationLessThanError(((2 + self.num_inode_bitmap_blocks) + self.num_zone_bitmap_blocks) + (self.num_inodes // self._root.inode_size) % self._root.block_size, self.first_data_zone, self._io, u"/types/superblock/seq/4")
            if not self.first_data_zone <= self.num_zones:
                raise kaitaistruct.ValidationGreaterThanError(self.num_zones, self.first_data_zone, self._io, u"/types/superblock/seq/4")
            self._debug['size_log_zone']['start'] = self._io.pos()
            self.size_log_zone = self._io.read_u2le()
            self._debug['size_log_zone']['end'] = self._io.pos()
            self._debug['max_size']['start'] = self._io.pos()
            self.max_size = self._io.read_u4le()
            self._debug['max_size']['end'] = self._io.pos()
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(2)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x8F\x13":
                raise kaitaistruct.ValidationNotEqualError(b"\x8F\x13", self.magic, self._io, u"/types/superblock/seq/7")
            self._debug['state']['start'] = self._io.pos()
            self.state = self._io.read_u2le()
            self._debug['state']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Zone(KaitaiStruct):
        SEQ_FIELDS = ["data"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Minix1l.Zone, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['data']['start'] = self._io.pos()
            self.data = self._io.read_bytes(self._root.block_size)
            self._debug['data']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class ZoneNumber(KaitaiStruct):
        SEQ_FIELDS = ["number"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Minix1l.ZoneNumber, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['number']['start'] = self._io.pos()
            self.number = self._io.read_u2le()
            self._debug['number']['end'] = self._io.pos()
            if not self.number <= self._root.superblock.num_zones:
                raise kaitaistruct.ValidationGreaterThanError(self._root.superblock.num_zones, self.number, self._io, u"/types/zone_number/seq/0")


        def _fetch_instances(self):
            pass
            _ = self.zone_data
            if hasattr(self, '_m_zone_data'):
                pass
                self._m_zone_data._fetch_instances()


        @property
        def zone_data(self):
            if hasattr(self, '_m_zone_data'):
                return self._m_zone_data

            if self.number != 0:
                pass
                io = self._root._io
                _pos = io.pos()
                io.seek(self.number * self._root.block_size)
                self._debug['_m_zone_data']['start'] = io.pos()
                self._m_zone_data = Minix1l.Zone(io, self, self._root)
                self._debug['_m_zone_data']['end'] = io.pos()
                io.seek(_pos)

            return getattr(self, '_m_zone_data', None)


    @property
    def block_size(self):
        if hasattr(self, '_m_block_size'):
            return self._m_block_size

        self._m_block_size = 1024
        return getattr(self, '_m_block_size', None)

    @property
    def inode_size(self):
        if hasattr(self, '_m_inode_size'):
            return self._m_inode_size

        self._m_inode_size = 32
        return getattr(self, '_m_inode_size', None)

    @property
    def zones(self):
        if hasattr(self, '_m_zones'):
            return self._m_zones

        _pos = self._io.pos()
        self._io.seek(self.superblock.first_data_zone * self.block_size)
        self._debug['_m_zones']['start'] = self._io.pos()
        self._debug['_m_zones']['arr'] = []
        self._m_zones = []
        for i in range(self.superblock.num_zones - self.superblock.first_data_zone):
            self._debug['_m_zones']['arr'].append({'start': self._io.pos()})
            self._m_zones.append(Minix1l.Zone(self._io, self, self._root))
            self._debug['_m_zones']['arr'][i]['end'] = self._io.pos()

        self._debug['_m_zones']['end'] = self._io.pos()
        self._io.seek(_pos)
        return getattr(self, '_m_zones', None)


