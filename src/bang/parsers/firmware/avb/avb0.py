# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Avb0(KaitaiStruct):
    """
    .. seealso::
       Source - https://android.googlesource.com/platform/external/avb/+/de53827b226bccef7407e4c253b0152e8d9f8e04/libavb/avb_vbmeta_image.h
    
    
    .. seealso::
       Source - https://android.googlesource.com/platform/external/avb/+/de53827b226bccef7407e4c253b0152e8d9f8e04/libavb/avb_crypto.h
    """

    class DescriptorTags(IntEnum):
        property = 0
        hashtree = 1
        hash = 2
        kernel_cmdline = 3
        chain_partition = 4

    class Encryption(IntEnum):
        no_encryption = 0
        sha256_rsa2048 = 1
        sha256_rsa4096 = 2
        sha256_rsa8192 = 3
        sha512_rsa2048 = 4
        sha512_rsa4096 = 5
        sha512_rsa8192 = 6
    SEQ_FIELDS = ["header", "authentication_data", "auxiliary_data", "padding", "blocks"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Avb0, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['header']['start'] = self._io.pos()
        self._raw_header = self._io.read_bytes(256)
        _io__raw_header = KaitaiStream(BytesIO(self._raw_header))
        self.header = Avb0.Header(_io__raw_header, self, self._root)
        self._debug['header']['end'] = self._io.pos()
        self._debug['authentication_data']['start'] = self._io.pos()
        self._raw_authentication_data = self._io.read_bytes(self.header.len_authentication_block)
        _io__raw_authentication_data = KaitaiStream(BytesIO(self._raw_authentication_data))
        self.authentication_data = Avb0.AuthenticationData(_io__raw_authentication_data, self, self._root)
        self._debug['authentication_data']['end'] = self._io.pos()
        self._debug['auxiliary_data']['start'] = self._io.pos()
        self._raw_auxiliary_data = self._io.read_bytes(self.header.len_auxiliary_block)
        _io__raw_auxiliary_data = KaitaiStream(BytesIO(self._raw_auxiliary_data))
        self.auxiliary_data = Avb0.AuxiliaryData(_io__raw_auxiliary_data, self, self._root)
        self._debug['auxiliary_data']['end'] = self._io.pos()
        self._debug['padding']['start'] = self._io.pos()
        self._debug['padding']['arr'] = []
        self.padding = []
        for i in range(-(self._io.pos()) % self.block_size):
            self._debug['padding']['arr'].append({'start': self._io.pos()})
            self.padding.append(Avb0.PaddingByte(self._io, self, self._root))
            self._debug['padding']['arr'][i]['end'] = self._io.pos()

        self._debug['padding']['end'] = self._io.pos()
        self._debug['blocks']['start'] = self._io.pos()
        self._debug['blocks']['arr'] = []
        self._raw_blocks = []
        self.blocks = []
        i = 0
        while True:
            self._debug['blocks']['arr'].append({'start': self._io.pos()})
            _buf = self._io.read_bytes(self.block_size)
            self._raw_blocks.append(_buf)
            _io__raw_blocks = KaitaiStream(BytesIO(self._raw_blocks[-1]))
            _ = Avb0.Block(_io__raw_blocks, self, self._root)
            self.blocks.append(_)
            self._debug['blocks']['arr'][len(self.blocks) - 1]['end'] = self._io.pos()
            if  ((_.footer.is_footer) or (self._io.is_eof()) or ( (((not (_.footer.is_footer))) and ((not (_.footer.is_padding)))) )) :
                break
            i += 1
        self._debug['blocks']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        self.header._fetch_instances()
        self.authentication_data._fetch_instances()
        self.auxiliary_data._fetch_instances()
        for i in range(len(self.padding)):
            pass
            self.padding[i]._fetch_instances()

        for i in range(len(self.blocks)):
            pass
            self.blocks[i]._fetch_instances()


    class AuthenticationData(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.AuthenticationData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.hash
            if hasattr(self, '_m_hash'):
                pass

            _ = self.signature
            if hasattr(self, '_m_signature'):
                pass


        @property
        def hash(self):
            if hasattr(self, '_m_hash'):
                return self._m_hash

            _pos = self._io.pos()
            self._io.seek(self._root.header.ofs_hash)
            self._debug['_m_hash']['start'] = self._io.pos()
            self._m_hash = self._io.read_bytes(self._root.header.len_hash)
            self._debug['_m_hash']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_hash', None)

        @property
        def signature(self):
            if hasattr(self, '_m_signature'):
                return self._m_signature

            _pos = self._io.pos()
            self._io.seek(self._root.header.ofs_signature)
            self._debug['_m_signature']['start'] = self._io.pos()
            self._m_signature = self._io.read_bytes(self._root.header.len_signature)
            self._debug['_m_signature']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_signature', None)


    class AuxiliaryData(KaitaiStruct):
        SEQ_FIELDS = []
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.AuxiliaryData, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            pass


        def _fetch_instances(self):
            pass
            _ = self.descriptors
            if hasattr(self, '_m_descriptors'):
                pass
                self._m_descriptors._fetch_instances()

            _ = self.public_key
            if hasattr(self, '_m_public_key'):
                pass

            _ = self.public_key_metadata
            if hasattr(self, '_m_public_key_metadata'):
                pass


        @property
        def descriptors(self):
            if hasattr(self, '_m_descriptors'):
                return self._m_descriptors

            _pos = self._io.pos()
            self._io.seek(self._root.header.ofs_descriptors)
            self._debug['_m_descriptors']['start'] = self._io.pos()
            self._raw__m_descriptors = self._io.read_bytes(self._root.header.len_descriptors)
            _io__raw__m_descriptors = KaitaiStream(BytesIO(self._raw__m_descriptors))
            self._m_descriptors = Avb0.Descriptors(_io__raw__m_descriptors, self, self._root)
            self._debug['_m_descriptors']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_descriptors', None)

        @property
        def public_key(self):
            if hasattr(self, '_m_public_key'):
                return self._m_public_key

            _pos = self._io.pos()
            self._io.seek(self._root.header.ofs_public_key)
            self._debug['_m_public_key']['start'] = self._io.pos()
            self._m_public_key = self._io.read_bytes(self._root.header.len_public_key)
            self._debug['_m_public_key']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_public_key', None)

        @property
        def public_key_metadata(self):
            if hasattr(self, '_m_public_key_metadata'):
                return self._m_public_key_metadata

            _pos = self._io.pos()
            self._io.seek(self._root.header.ofs_public_key_metadata)
            self._debug['_m_public_key_metadata']['start'] = self._io.pos()
            self._m_public_key_metadata = self._io.read_bytes(self._root.header.len_public_key_metadata)
            self._debug['_m_public_key_metadata']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_public_key_metadata', None)


    class Block(KaitaiStruct):
        SEQ_FIELDS = ["padding", "footer"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.Block, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['padding']['start'] = self._io.pos()
            self._debug['padding']['arr'] = []
            self.padding = []
            for i in range((self._root.block_size - self._root.footer_size) // 64):
                self._debug['padding']['arr'].append({'start': self._io.pos()})
                self.padding.append(Avb0.PaddingBlock(self._io, self, self._root))
                self._debug['padding']['arr'][i]['end'] = self._io.pos()

            self._debug['padding']['end'] = self._io.pos()
            self._debug['footer']['start'] = self._io.pos()
            self._raw_footer = self._io.read_bytes_full()
            _io__raw_footer = KaitaiStream(BytesIO(self._raw_footer))
            self.footer = Avb0.FooterOrPadding(_io__raw_footer, self, self._root)
            self._debug['footer']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.padding)):
                pass
                self.padding[i]._fetch_instances()

            self.footer._fetch_instances()


    class ChainPartition(KaitaiStruct):
        SEQ_FIELDS = ["rollback_index_location", "len_partition_name", "len_public_key", "reserved", "partition_name", "public_key"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.ChainPartition, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['rollback_index_location']['start'] = self._io.pos()
            self.rollback_index_location = self._io.read_u4be()
            self._debug['rollback_index_location']['end'] = self._io.pos()
            self._debug['len_partition_name']['start'] = self._io.pos()
            self.len_partition_name = self._io.read_u4be()
            self._debug['len_partition_name']['end'] = self._io.pos()
            self._debug['len_public_key']['start'] = self._io.pos()
            self.len_public_key = self._io.read_u4be()
            self._debug['len_public_key']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(64)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['partition_name']['start'] = self._io.pos()
            self.partition_name = (self._io.read_bytes(self.len_partition_name)).decode(u"UTF-8")
            self._debug['partition_name']['end'] = self._io.pos()
            self._debug['public_key']['start'] = self._io.pos()
            self.public_key = self._io.read_bytes(self.len_public_key)
            self._debug['public_key']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Descriptor(KaitaiStruct):
        SEQ_FIELDS = ["tag", "len_descriptor_data", "descriptor_data", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.Descriptor, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['tag']['start'] = self._io.pos()
            self.tag = KaitaiStream.resolve_enum(Avb0.DescriptorTags, self._io.read_u8be())
            self._debug['tag']['end'] = self._io.pos()
            self._debug['len_descriptor_data']['start'] = self._io.pos()
            self.len_descriptor_data = self._io.read_u8be()
            self._debug['len_descriptor_data']['end'] = self._io.pos()
            self._debug['descriptor_data']['start'] = self._io.pos()
            _on = self.tag
            if _on == Avb0.DescriptorTags.chain_partition:
                pass
                self._raw_descriptor_data = self._io.read_bytes(self.len_descriptor_data)
                _io__raw_descriptor_data = KaitaiStream(BytesIO(self._raw_descriptor_data))
                self.descriptor_data = Avb0.ChainPartition(_io__raw_descriptor_data, self, self._root)
            elif _on == Avb0.DescriptorTags.hash:
                pass
                self._raw_descriptor_data = self._io.read_bytes(self.len_descriptor_data)
                _io__raw_descriptor_data = KaitaiStream(BytesIO(self._raw_descriptor_data))
                self.descriptor_data = Avb0.Hash(_io__raw_descriptor_data, self, self._root)
            elif _on == Avb0.DescriptorTags.hashtree:
                pass
                self._raw_descriptor_data = self._io.read_bytes(self.len_descriptor_data)
                _io__raw_descriptor_data = KaitaiStream(BytesIO(self._raw_descriptor_data))
                self.descriptor_data = Avb0.Hashtree(_io__raw_descriptor_data, self, self._root)
            elif _on == Avb0.DescriptorTags.kernel_cmdline:
                pass
                self._raw_descriptor_data = self._io.read_bytes(self.len_descriptor_data)
                _io__raw_descriptor_data = KaitaiStream(BytesIO(self._raw_descriptor_data))
                self.descriptor_data = Avb0.KernelCmdline(_io__raw_descriptor_data, self, self._root)
            elif _on == Avb0.DescriptorTags.property:
                pass
                self._raw_descriptor_data = self._io.read_bytes(self.len_descriptor_data)
                _io__raw_descriptor_data = KaitaiStream(BytesIO(self._raw_descriptor_data))
                self.descriptor_data = Avb0.PropertyDescriptor(_io__raw_descriptor_data, self, self._root)
            else:
                pass
                self.descriptor_data = self._io.read_bytes(self.len_descriptor_data)
            self._debug['descriptor_data']['end'] = self._io.pos()
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self._io.pos()) % 8)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.tag
            if _on == Avb0.DescriptorTags.chain_partition:
                pass
                self.descriptor_data._fetch_instances()
            elif _on == Avb0.DescriptorTags.hash:
                pass
                self.descriptor_data._fetch_instances()
            elif _on == Avb0.DescriptorTags.hashtree:
                pass
                self.descriptor_data._fetch_instances()
            elif _on == Avb0.DescriptorTags.kernel_cmdline:
                pass
                self.descriptor_data._fetch_instances()
            elif _on == Avb0.DescriptorTags.property:
                pass
                self.descriptor_data._fetch_instances()
            else:
                pass


    class Descriptors(KaitaiStruct):
        SEQ_FIELDS = ["descriptor"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.Descriptors, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['descriptor']['start'] = self._io.pos()
            self._debug['descriptor']['arr'] = []
            self.descriptor = []
            i = 0
            while not self._io.is_eof():
                self._debug['descriptor']['arr'].append({'start': self._io.pos()})
                self.descriptor.append(Avb0.Descriptor(self._io, self, self._root))
                self._debug['descriptor']['arr'][len(self.descriptor) - 1]['end'] = self._io.pos()
                i += 1

            self._debug['descriptor']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.descriptor)):
                pass
                self.descriptor[i]._fetch_instances()



    class Footer(KaitaiStruct):
        SEQ_FIELDS = ["magic", "major_version", "minor_version", "original_image_size", "vbmeta_offset", "vbmeta_size", "reserved"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.Footer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x41\x56\x42\x66":
                raise kaitaistruct.ValidationNotEqualError(b"\x41\x56\x42\x66", self.magic, self._io, u"/types/footer/seq/0")
            self._debug['major_version']['start'] = self._io.pos()
            self.major_version = self._io.read_u4be()
            self._debug['major_version']['end'] = self._io.pos()
            self._debug['minor_version']['start'] = self._io.pos()
            self.minor_version = self._io.read_u4be()
            self._debug['minor_version']['end'] = self._io.pos()
            self._debug['original_image_size']['start'] = self._io.pos()
            self.original_image_size = self._io.read_u8be()
            self._debug['original_image_size']['end'] = self._io.pos()
            self._debug['vbmeta_offset']['start'] = self._io.pos()
            self.vbmeta_offset = self._io.read_u8be()
            self._debug['vbmeta_offset']['end'] = self._io.pos()
            self._debug['vbmeta_size']['start'] = self._io.pos()
            self.vbmeta_size = self._io.read_u8be()
            self._debug['vbmeta_size']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(28)
            self._debug['reserved']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class FooterOrPadding(KaitaiStruct):
        SEQ_FIELDS = ["footer", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.FooterOrPadding, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            if self.is_footer:
                pass
                self._debug['footer']['start'] = self._io.pos()
                self.footer = Avb0.Footer(self._io, self, self._root)
                self._debug['footer']['end'] = self._io.pos()

            if self.is_padding:
                pass
                self._debug['padding']['start'] = self._io.pos()
                self._debug['padding']['arr'] = []
                self.padding = []
                i = 0
                while not self._io.is_eof():
                    self._debug['padding']['arr'].append({'start': self._io.pos()})
                    self.padding.append(Avb0.PaddingByte(self._io, self, self._root))
                    self._debug['padding']['arr'][len(self.padding) - 1]['end'] = self._io.pos()
                    i += 1

                self._debug['padding']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if self.is_footer:
                pass
                self.footer._fetch_instances()

            if self.is_padding:
                pass
                for i in range(len(self.padding)):
                    pass
                    self.padding[i]._fetch_instances()


            _ = self.magic
            if hasattr(self, '_m_magic'):
                pass


        @property
        def is_footer(self):
            if hasattr(self, '_m_is_footer'):
                return self._m_is_footer

            self._m_is_footer = self.magic == b"\x41\x56\x42\x66"
            return getattr(self, '_m_is_footer', None)

        @property
        def is_padding(self):
            if hasattr(self, '_m_is_padding'):
                return self._m_is_padding

            self._m_is_padding = self.magic == b"\x00\x00\x00\x00"
            return getattr(self, '_m_is_padding', None)

        @property
        def magic(self):
            if hasattr(self, '_m_magic'):
                return self._m_magic

            _pos = self._io.pos()
            self._io.seek(0)
            self._debug['_m_magic']['start'] = self._io.pos()
            self._m_magic = self._io.read_bytes(4)
            self._debug['_m_magic']['end'] = self._io.pos()
            self._io.seek(_pos)
            return getattr(self, '_m_magic', None)


    class Hash(KaitaiStruct):
        SEQ_FIELDS = ["image_size", "hash_algorithm", "len_partition_name", "len_salt", "len_digest", "flags", "reserved", "partition_name", "salt", "digest"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.Hash, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['image_size']['start'] = self._io.pos()
            self.image_size = self._io.read_u8be()
            self._debug['image_size']['end'] = self._io.pos()
            self._debug['hash_algorithm']['start'] = self._io.pos()
            self.hash_algorithm = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['hash_algorithm']['end'] = self._io.pos()
            self._debug['len_partition_name']['start'] = self._io.pos()
            self.len_partition_name = self._io.read_u4be()
            self._debug['len_partition_name']['end'] = self._io.pos()
            self._debug['len_salt']['start'] = self._io.pos()
            self.len_salt = self._io.read_u4be()
            self._debug['len_salt']['end'] = self._io.pos()
            self._debug['len_digest']['start'] = self._io.pos()
            self.len_digest = self._io.read_u4be()
            self._debug['len_digest']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(60)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['partition_name']['start'] = self._io.pos()
            self.partition_name = (self._io.read_bytes(self.len_partition_name)).decode(u"UTF-8")
            self._debug['partition_name']['end'] = self._io.pos()
            self._debug['salt']['start'] = self._io.pos()
            self.salt = self._io.read_bytes(self.len_salt)
            self._debug['salt']['end'] = self._io.pos()
            self._debug['digest']['start'] = self._io.pos()
            self.digest = self._io.read_bytes(self.len_digest)
            self._debug['digest']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Hashtree(KaitaiStruct):
        SEQ_FIELDS = ["dm_verity_version", "image_size", "tree_offset", "tree_size", "data_block_size", "hash_block_size", "fec_num_roots", "fec_offset", "fec_size", "hash_algorithm", "len_partition_name", "len_salt", "len_root_digest", "flags", "reserved", "partition_name", "salt", "root_digest"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.Hashtree, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['dm_verity_version']['start'] = self._io.pos()
            self.dm_verity_version = self._io.read_u4be()
            self._debug['dm_verity_version']['end'] = self._io.pos()
            self._debug['image_size']['start'] = self._io.pos()
            self.image_size = self._io.read_u8be()
            self._debug['image_size']['end'] = self._io.pos()
            self._debug['tree_offset']['start'] = self._io.pos()
            self.tree_offset = self._io.read_u8be()
            self._debug['tree_offset']['end'] = self._io.pos()
            self._debug['tree_size']['start'] = self._io.pos()
            self.tree_size = self._io.read_u8be()
            self._debug['tree_size']['end'] = self._io.pos()
            self._debug['data_block_size']['start'] = self._io.pos()
            self.data_block_size = self._io.read_u4be()
            self._debug['data_block_size']['end'] = self._io.pos()
            self._debug['hash_block_size']['start'] = self._io.pos()
            self.hash_block_size = self._io.read_u4be()
            self._debug['hash_block_size']['end'] = self._io.pos()
            self._debug['fec_num_roots']['start'] = self._io.pos()
            self.fec_num_roots = self._io.read_u4be()
            self._debug['fec_num_roots']['end'] = self._io.pos()
            self._debug['fec_offset']['start'] = self._io.pos()
            self.fec_offset = self._io.read_u8be()
            self._debug['fec_offset']['end'] = self._io.pos()
            self._debug['fec_size']['start'] = self._io.pos()
            self.fec_size = self._io.read_u8be()
            self._debug['fec_size']['end'] = self._io.pos()
            self._debug['hash_algorithm']['start'] = self._io.pos()
            self.hash_algorithm = (KaitaiStream.bytes_terminate(self._io.read_bytes(32), 0, False)).decode(u"UTF-8")
            self._debug['hash_algorithm']['end'] = self._io.pos()
            self._debug['len_partition_name']['start'] = self._io.pos()
            self.len_partition_name = self._io.read_u4be()
            self._debug['len_partition_name']['end'] = self._io.pos()
            self._debug['len_salt']['start'] = self._io.pos()
            self.len_salt = self._io.read_u4be()
            self._debug['len_salt']['end'] = self._io.pos()
            self._debug['len_root_digest']['start'] = self._io.pos()
            self.len_root_digest = self._io.read_u4be()
            self._debug['len_root_digest']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['reserved']['start'] = self._io.pos()
            self.reserved = self._io.read_bytes(60)
            self._debug['reserved']['end'] = self._io.pos()
            self._debug['partition_name']['start'] = self._io.pos()
            self.partition_name = (self._io.read_bytes(self.len_partition_name)).decode(u"UTF-8")
            self._debug['partition_name']['end'] = self._io.pos()
            self._debug['salt']['start'] = self._io.pos()
            self.salt = self._io.read_bytes(self.len_salt)
            self._debug['salt']['end'] = self._io.pos()
            self._debug['root_digest']['start'] = self._io.pos()
            self.root_digest = self._io.read_bytes(self.len_root_digest)
            self._debug['root_digest']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class Header(KaitaiStruct):
        SEQ_FIELDS = ["magic", "major_version", "minor_version", "len_authentication_block", "len_auxiliary_block", "algorithm", "ofs_hash", "len_hash", "ofs_signature", "len_signature", "ofs_public_key", "len_public_key", "ofs_public_key_metadata", "len_public_key_metadata", "ofs_descriptors", "len_descriptors", "rollback_index", "flags", "padding1", "release_string", "padding2"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.Header, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['magic']['start'] = self._io.pos()
            self.magic = self._io.read_bytes(4)
            self._debug['magic']['end'] = self._io.pos()
            if not self.magic == b"\x41\x56\x42\x30":
                raise kaitaistruct.ValidationNotEqualError(b"\x41\x56\x42\x30", self.magic, self._io, u"/types/header/seq/0")
            self._debug['major_version']['start'] = self._io.pos()
            self.major_version = self._io.read_u4be()
            self._debug['major_version']['end'] = self._io.pos()
            self._debug['minor_version']['start'] = self._io.pos()
            self.minor_version = self._io.read_u4be()
            self._debug['minor_version']['end'] = self._io.pos()
            self._debug['len_authentication_block']['start'] = self._io.pos()
            self.len_authentication_block = self._io.read_u8be()
            self._debug['len_authentication_block']['end'] = self._io.pos()
            self._debug['len_auxiliary_block']['start'] = self._io.pos()
            self.len_auxiliary_block = self._io.read_u8be()
            self._debug['len_auxiliary_block']['end'] = self._io.pos()
            self._debug['algorithm']['start'] = self._io.pos()
            self.algorithm = KaitaiStream.resolve_enum(Avb0.Encryption, self._io.read_u4be())
            self._debug['algorithm']['end'] = self._io.pos()
            if not  ((self.algorithm == Avb0.Encryption.no_encryption) or (self.algorithm == Avb0.Encryption.sha256_rsa2048) or (self.algorithm == Avb0.Encryption.sha256_rsa4096) or (self.algorithm == Avb0.Encryption.sha256_rsa8192) or (self.algorithm == Avb0.Encryption.sha512_rsa2048) or (self.algorithm == Avb0.Encryption.sha512_rsa4096) or (self.algorithm == Avb0.Encryption.sha512_rsa8192)) :
                raise kaitaistruct.ValidationNotAnyOfError(self.algorithm, self._io, u"/types/header/seq/5")
            self._debug['ofs_hash']['start'] = self._io.pos()
            self.ofs_hash = self._io.read_u8be()
            self._debug['ofs_hash']['end'] = self._io.pos()
            self._debug['len_hash']['start'] = self._io.pos()
            self.len_hash = self._io.read_u8be()
            self._debug['len_hash']['end'] = self._io.pos()
            self._debug['ofs_signature']['start'] = self._io.pos()
            self.ofs_signature = self._io.read_u8be()
            self._debug['ofs_signature']['end'] = self._io.pos()
            self._debug['len_signature']['start'] = self._io.pos()
            self.len_signature = self._io.read_u8be()
            self._debug['len_signature']['end'] = self._io.pos()
            self._debug['ofs_public_key']['start'] = self._io.pos()
            self.ofs_public_key = self._io.read_u8be()
            self._debug['ofs_public_key']['end'] = self._io.pos()
            self._debug['len_public_key']['start'] = self._io.pos()
            self.len_public_key = self._io.read_u8be()
            self._debug['len_public_key']['end'] = self._io.pos()
            self._debug['ofs_public_key_metadata']['start'] = self._io.pos()
            self.ofs_public_key_metadata = self._io.read_u8be()
            self._debug['ofs_public_key_metadata']['end'] = self._io.pos()
            self._debug['len_public_key_metadata']['start'] = self._io.pos()
            self.len_public_key_metadata = self._io.read_u8be()
            self._debug['len_public_key_metadata']['end'] = self._io.pos()
            self._debug['ofs_descriptors']['start'] = self._io.pos()
            self.ofs_descriptors = self._io.read_u8be()
            self._debug['ofs_descriptors']['end'] = self._io.pos()
            self._debug['len_descriptors']['start'] = self._io.pos()
            self.len_descriptors = self._io.read_u8be()
            self._debug['len_descriptors']['end'] = self._io.pos()
            self._debug['rollback_index']['start'] = self._io.pos()
            self.rollback_index = self._io.read_u8be()
            self._debug['rollback_index']['end'] = self._io.pos()
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['padding1']['start'] = self._io.pos()
            self.padding1 = self._io.read_bytes(4)
            self._debug['padding1']['end'] = self._io.pos()
            if not self.padding1 == b"\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00", self.padding1, self._io, u"/types/header/seq/18")
            self._debug['release_string']['start'] = self._io.pos()
            self.release_string = (KaitaiStream.bytes_terminate(self._io.read_bytes(48), 0, False)).decode(u"UTF-8")
            self._debug['release_string']['end'] = self._io.pos()
            self._debug['padding2']['start'] = self._io.pos()
            self._debug['padding2']['arr'] = []
            self.padding2 = []
            for i in range(80):
                self._debug['padding2']['arr'].append({'start': self._io.pos()})
                self.padding2.append(Avb0.PaddingByte(self._io, self, self._root))
                self._debug['padding2']['arr'][i]['end'] = self._io.pos()

            self._debug['padding2']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.padding2)):
                pass
                self.padding2[i]._fetch_instances()



    class KernelCmdline(KaitaiStruct):
        SEQ_FIELDS = ["flags", "len_kernel_cmdline", "kernel_cmdline"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.KernelCmdline, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['flags']['start'] = self._io.pos()
            self.flags = self._io.read_u4be()
            self._debug['flags']['end'] = self._io.pos()
            self._debug['len_kernel_cmdline']['start'] = self._io.pos()
            self.len_kernel_cmdline = self._io.read_u4be()
            self._debug['len_kernel_cmdline']['end'] = self._io.pos()
            self._debug['kernel_cmdline']['start'] = self._io.pos()
            self.kernel_cmdline = (self._io.read_bytes(self.len_kernel_cmdline)).decode(u"UTF-8")
            self._debug['kernel_cmdline']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class PaddingBlock(KaitaiStruct):
        SEQ_FIELDS = ["padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.PaddingBlock, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(64)
            self._debug['padding']['end'] = self._io.pos()
            if not self.padding == b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", self.padding, self._io, u"/types/padding_block/seq/0")


        def _fetch_instances(self):
            pass


    class PaddingByte(KaitaiStruct):
        SEQ_FIELDS = ["padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.PaddingByte, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(1)
            self._debug['padding']['end'] = self._io.pos()
            if not self.padding == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.padding, self._io, u"/types/padding_byte/seq/0")


        def _fetch_instances(self):
            pass


    class PropertyDescriptor(KaitaiStruct):
        SEQ_FIELDS = ["len_key_data", "len_value_data", "key", "null_byte1", "value", "null_byte2", "padding"]
        def __init__(self, _io, _parent=None, _root=None):
            super(Avb0.PropertyDescriptor, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['len_key_data']['start'] = self._io.pos()
            self.len_key_data = self._io.read_u8be()
            self._debug['len_key_data']['end'] = self._io.pos()
            self._debug['len_value_data']['start'] = self._io.pos()
            self.len_value_data = self._io.read_u8be()
            self._debug['len_value_data']['end'] = self._io.pos()
            self._debug['key']['start'] = self._io.pos()
            self.key = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_key_data), 0, False)).decode(u"UTF-8")
            self._debug['key']['end'] = self._io.pos()
            self._debug['null_byte1']['start'] = self._io.pos()
            self.null_byte1 = self._io.read_bytes(1)
            self._debug['null_byte1']['end'] = self._io.pos()
            if not self.null_byte1 == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.null_byte1, self._io, u"/types/property_descriptor/seq/3")
            self._debug['value']['start'] = self._io.pos()
            self.value = (KaitaiStream.bytes_terminate(self._io.read_bytes(self.len_value_data), 0, False)).decode(u"UTF-8")
            self._debug['value']['end'] = self._io.pos()
            self._debug['null_byte2']['start'] = self._io.pos()
            self.null_byte2 = self._io.read_bytes(1)
            self._debug['null_byte2']['end'] = self._io.pos()
            if not self.null_byte2 == b"\x00":
                raise kaitaistruct.ValidationNotEqualError(b"\x00", self.null_byte2, self._io, u"/types/property_descriptor/seq/5")
            self._debug['padding']['start'] = self._io.pos()
            self.padding = self._io.read_bytes(-(self._io.pos()) % 8)
            self._debug['padding']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    @property
    def block_size(self):
        if hasattr(self, '_m_block_size'):
            return self._m_block_size

        self._m_block_size = 4096
        return getattr(self, '_m_block_size', None)

    @property
    def footer_size(self):
        if hasattr(self, '_m_footer_size'):
            return self._m_footer_size

        self._m_footer_size = 64
        return getattr(self, '_m_footer_size', None)


