# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import IntEnum
import collections


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class Bencode(KaitaiStruct):
    """Binary serialization for a kind of subset of JSON, but that can be human-readable and editable in text editors indicating byte positions.
    Used in BitTorrent protocol.
    
    Sample: d6:kaitail2:isi146e9:% awesomeee
    
    .. seealso::
       Source - https://www.bittorrent.org/beps/bep_0003.html#bencoding
    """

    class Type(IntEnum):
        dict = 100
        end = 101
        int = 105
        list = 108
    SEQ_FIELDS = ["type_byte", "value"]
    def __init__(self, _io, _parent=None, _root=None):
        super(Bencode, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['type_byte']['start'] = self._io.pos()
        self.type_byte = self._io.read_u1()
        self._debug['type_byte']['end'] = self._io.pos()
        self._debug['value']['start'] = self._io.pos()
        _on = self.is_buffer
        if _on == False:
            pass
            self.value = Bencode.NonBuffer(self.type_byte, self._io, self, self._root)
        elif _on == True:
            pass
            self.value = Bencode.Buffer(self.type_byte, self._io, self, self._root)
        self._debug['value']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        _on = self.is_buffer
        if _on == False:
            pass
            self.value._fetch_instances()
        elif _on == True:
            pass
            self.value._fetch_instances()

    class Buffer(KaitaiStruct):
        SEQ_FIELDS = ["rest_size_str", "value"]
        def __init__(self, first_digit_byte, _io, _parent=None, _root=None):
            super(Bencode.Buffer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.first_digit_byte = first_digit_byte
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['rest_size_str']['start'] = self._io.pos()
            self.rest_size_str = (self._io.read_bytes_term(58, False, True, True)).decode(u"ASCII")
            self._debug['rest_size_str']['end'] = self._io.pos()
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_bytes(((((((((5 if len(self.rest_size_str) & 1 != 0 else 1) * (25 if len(self.rest_size_str) & 2 != 0 else 1)) * (625 if len(self.rest_size_str) & 4 != 0 else 1)) * (390625 if len(self.rest_size_str) & 8 != 0 else 1)) * (152587890625 if len(self.rest_size_str) & 16 != 0 else 1)) * (23283064365386962890625 if len(self.rest_size_str) & 32 != 0 else 1)) * (542101086242752217003726400434970855712890625 if len(self.rest_size_str) & 64 != 0 else 1)) * (293873587705571876992184134305561419454666389193021880377187926569604314863681793212890625 if len(self.rest_size_str) & 128 != 0 else 1) << len(self.rest_size_str)) * (self.first_digit_byte - 48) + (int(self.rest_size_str) if len(self.rest_size_str) > 0 else 0))
            self._debug['value']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class NonBuffer(KaitaiStruct):
        SEQ_FIELDS = ["value"]
        def __init__(self, type_byte, _io, _parent=None, _root=None):
            super(Bencode.NonBuffer, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.type_byte = type_byte
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            _on = self.type
            if _on == Bencode.Type.dict:
                pass
                self.value = Bencode.NonBuffer.Bdict(self._io, self, self._root)
            elif _on == Bencode.Type.int:
                pass
                self.value = Bencode.NonBuffer.Bint(self._io, self, self._root)
            elif _on == Bencode.Type.list:
                pass
                self.value = Bencode.NonBuffer.Blist(self._io, self, self._root)
            self._debug['value']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = self.type
            if _on == Bencode.Type.dict:
                pass
                self.value._fetch_instances()
            elif _on == Bencode.Type.int:
                pass
                self.value._fetch_instances()
            elif _on == Bencode.Type.list:
                pass
                self.value._fetch_instances()

        class Bdict(KaitaiStruct):
            SEQ_FIELDS = ["items"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Bencode.NonBuffer.Bdict, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['items']['start'] = self._io.pos()
                self._debug['items']['arr'] = []
                self.items = []
                i = 0
                while True:
                    self._debug['items']['arr'].append({'start': self._io.pos()})
                    _ = Bencode.NonBuffer.Bdict.Kwpair(self._io, self, self._root)
                    self.items.append(_)
                    self._debug['items']['arr'][len(self.items) - 1]['end'] = self._io.pos()
                    if _.key.type_byte == int(Bencode.Type.end):
                        break
                    i += 1
                self._debug['items']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.items)):
                    pass
                    self.items[i]._fetch_instances()


            class Kwpair(KaitaiStruct):
                SEQ_FIELDS = ["key", "value"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(Bencode.NonBuffer.Bdict.Kwpair, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['key']['start'] = self._io.pos()
                    self.key = Bencode(self._io, self, self._root)
                    self._debug['key']['end'] = self._io.pos()
                    _ = self.key
                    if not  ((self.key.is_buffer) or (self.is_end)) :
                        raise kaitaistruct.ValidationExprError(self.key, self._io, u"/types/non_buffer/types/bdict/types/kwpair/seq/0")
                    if (not (self.is_end)):
                        pass
                        self._debug['value']['start'] = self._io.pos()
                        self.value = Bencode(self._io, self, self._root)
                        self._debug['value']['end'] = self._io.pos()



                def _fetch_instances(self):
                    pass
                    self.key._fetch_instances()
                    if (not (self.is_end)):
                        pass
                        self.value._fetch_instances()


                @property
                def is_end(self):
                    if hasattr(self, '_m_is_end'):
                        return self._m_is_end

                    self._m_is_end = self.key.type_byte == int(Bencode.Type.end)
                    return getattr(self, '_m_is_end', None)



        class Bint(KaitaiStruct):
            SEQ_FIELDS = ["int_str"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Bencode.NonBuffer.Bint, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['int_str']['start'] = self._io.pos()
                self.int_str = (self._io.read_bytes_term(101, False, True, True)).decode(u"ASCII")
                self._debug['int_str']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass

            @property
            def value(self):
                if hasattr(self, '_m_value'):
                    return self._m_value

                self._m_value = int(self.int_str)
                return getattr(self, '_m_value', None)


        class Blist(KaitaiStruct):
            SEQ_FIELDS = ["values"]
            def __init__(self, _io, _parent=None, _root=None):
                super(Bencode.NonBuffer.Blist, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['values']['start'] = self._io.pos()
                self._debug['values']['arr'] = []
                self.values = []
                i = 0
                while True:
                    self._debug['values']['arr'].append({'start': self._io.pos()})
                    _ = Bencode(self._io, self, self._root)
                    self.values.append(_)
                    self._debug['values']['arr'][len(self.values) - 1]['end'] = self._io.pos()
                    if _.type_byte == int(Bencode.Type.end):
                        break
                    i += 1
                self._debug['values']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.values)):
                    pass
                    self.values[i]._fetch_instances()



        @property
        def type(self):
            if hasattr(self, '_m_type'):
                return self._m_type

            self._m_type = KaitaiStream.resolve_enum(Bencode.Type, self.type_byte)
            return getattr(self, '_m_type', None)


    @property
    def is_buffer(self):
        if hasattr(self, '_m_is_buffer'):
            return self._m_is_buffer

        self._m_is_buffer =  ((48 <= self.type_byte) and (self.type_byte <= 58)) 
        return getattr(self, '_m_is_buffer', None)


