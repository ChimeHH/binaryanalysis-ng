# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild
# type: ignore

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
import collections
from enum import IntEnum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 11):
    raise Exception("Incompatible Kaitai Struct Python API: 0.11 or later is required, but you have %s" % (kaitaistruct.__version__))

class JavaClass(KaitaiStruct):
    """
    .. seealso::
       Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.1
    """
    SEQ_FIELDS = ["magic", "version_minor", "version_major", "constant_pool_count", "constant_pool", "access_flags", "this_class", "super_class", "interfaces_count", "interfaces", "fields_count", "fields", "methods_count", "methods", "attributes_count", "attributes"]
    def __init__(self, _io, _parent=None, _root=None):
        super(JavaClass, self).__init__(_io)
        self._parent = _parent
        self._root = _root or self
        self._debug = collections.defaultdict(dict)
        self._read()

    def _read(self):
        self._debug['magic']['start'] = self._io.pos()
        self.magic = self._io.read_bytes(4)
        self._debug['magic']['end'] = self._io.pos()
        if not self.magic == b"\xCA\xFE\xBA\xBE":
            raise kaitaistruct.ValidationNotEqualError(b"\xCA\xFE\xBA\xBE", self.magic, self._io, u"/seq/0")
        self._debug['version_minor']['start'] = self._io.pos()
        self.version_minor = self._io.read_u2be()
        self._debug['version_minor']['end'] = self._io.pos()
        self._debug['version_major']['start'] = self._io.pos()
        self.version_major = self._io.read_u2be()
        self._debug['version_major']['end'] = self._io.pos()
        if not self.version_major >= 43:
            raise kaitaistruct.ValidationLessThanError(43, self.version_major, self._io, u"/seq/2")
        self._debug['constant_pool_count']['start'] = self._io.pos()
        self.constant_pool_count = self._io.read_u2be()
        self._debug['constant_pool_count']['end'] = self._io.pos()
        self._debug['constant_pool']['start'] = self._io.pos()
        self._debug['constant_pool']['arr'] = []
        self.constant_pool = []
        for i in range(self.constant_pool_count - 1):
            self._debug['constant_pool']['arr'].append({'start': self._io.pos()})
            self.constant_pool.append(JavaClass.ConstantPoolEntry((self.constant_pool[i - 1].is_two_entries if i != 0 else False), self._io, self, self._root))
            self._debug['constant_pool']['arr'][i]['end'] = self._io.pos()

        self._debug['constant_pool']['end'] = self._io.pos()
        self._debug['access_flags']['start'] = self._io.pos()
        self.access_flags = self._io.read_u2be()
        self._debug['access_flags']['end'] = self._io.pos()
        self._debug['this_class']['start'] = self._io.pos()
        self.this_class = self._io.read_u2be()
        self._debug['this_class']['end'] = self._io.pos()
        self._debug['super_class']['start'] = self._io.pos()
        self.super_class = self._io.read_u2be()
        self._debug['super_class']['end'] = self._io.pos()
        self._debug['interfaces_count']['start'] = self._io.pos()
        self.interfaces_count = self._io.read_u2be()
        self._debug['interfaces_count']['end'] = self._io.pos()
        self._debug['interfaces']['start'] = self._io.pos()
        self._debug['interfaces']['arr'] = []
        self.interfaces = []
        for i in range(self.interfaces_count):
            self._debug['interfaces']['arr'].append({'start': self._io.pos()})
            self.interfaces.append(self._io.read_u2be())
            self._debug['interfaces']['arr'][i]['end'] = self._io.pos()

        self._debug['interfaces']['end'] = self._io.pos()
        self._debug['fields_count']['start'] = self._io.pos()
        self.fields_count = self._io.read_u2be()
        self._debug['fields_count']['end'] = self._io.pos()
        self._debug['fields']['start'] = self._io.pos()
        self._debug['fields']['arr'] = []
        self.fields = []
        for i in range(self.fields_count):
            self._debug['fields']['arr'].append({'start': self._io.pos()})
            self.fields.append(JavaClass.FieldInfo(self._io, self, self._root))
            self._debug['fields']['arr'][i]['end'] = self._io.pos()

        self._debug['fields']['end'] = self._io.pos()
        self._debug['methods_count']['start'] = self._io.pos()
        self.methods_count = self._io.read_u2be()
        self._debug['methods_count']['end'] = self._io.pos()
        self._debug['methods']['start'] = self._io.pos()
        self._debug['methods']['arr'] = []
        self.methods = []
        for i in range(self.methods_count):
            self._debug['methods']['arr'].append({'start': self._io.pos()})
            self.methods.append(JavaClass.MethodInfo(self._io, self, self._root))
            self._debug['methods']['arr'][i]['end'] = self._io.pos()

        self._debug['methods']['end'] = self._io.pos()
        self._debug['attributes_count']['start'] = self._io.pos()
        self.attributes_count = self._io.read_u2be()
        self._debug['attributes_count']['end'] = self._io.pos()
        self._debug['attributes']['start'] = self._io.pos()
        self._debug['attributes']['arr'] = []
        self.attributes = []
        for i in range(self.attributes_count):
            self._debug['attributes']['arr'].append({'start': self._io.pos()})
            self.attributes.append(JavaClass.AttributeInfo(self._io, self, self._root))
            self._debug['attributes']['arr'][i]['end'] = self._io.pos()

        self._debug['attributes']['end'] = self._io.pos()


    def _fetch_instances(self):
        pass
        for i in range(len(self.constant_pool)):
            pass
            self.constant_pool[i]._fetch_instances()

        for i in range(len(self.interfaces)):
            pass

        for i in range(len(self.fields)):
            pass
            self.fields[i]._fetch_instances()

        for i in range(len(self.methods)):
            pass
            self.methods[i]._fetch_instances()

        for i in range(len(self.attributes)):
            pass
            self.attributes[i]._fetch_instances()


    class AttributeInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7
        """
        SEQ_FIELDS = ["name_index", "attribute_length", "info"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.AttributeInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name_index']['start'] = self._io.pos()
            self.name_index = self._io.read_u2be()
            self._debug['name_index']['end'] = self._io.pos()
            self._debug['attribute_length']['start'] = self._io.pos()
            self.attribute_length = self._io.read_u4be()
            self._debug['attribute_length']['end'] = self._io.pos()
            self._debug['info']['start'] = self._io.pos()
            _on = (self.name_as_str).decode(u"ascii")
            if _on == u"Code":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyCode(_io__raw_info, self, self._root)
            elif _on == u"ConstantValue":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyConstantValue(_io__raw_info, self, self._root)
            elif _on == u"EnclosingMethod":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyEnclosingMethod(_io__raw_info, self, self._root)
            elif _on == u"Exceptions":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyExceptions(_io__raw_info, self, self._root)
            elif _on == u"InnerClasses":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyInnerClasses(_io__raw_info, self, self._root)
            elif _on == u"LineNumberTable":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyLineNumberTable(_io__raw_info, self, self._root)
            elif _on == u"LocalVariableTable":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyLocalVariableTable(_io__raw_info, self, self._root)
            elif _on == u"LocalVariableTypeTable":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyLocalVariableTypeTable(_io__raw_info, self, self._root)
            elif _on == u"ModuleMainClass":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyModuleMainClass(_io__raw_info, self, self._root)
            elif _on == u"ModulePackages":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyModulePackages(_io__raw_info, self, self._root)
            elif _on == u"NestHost":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyNestHost(_io__raw_info, self, self._root)
            elif _on == u"NestMembers":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyNestMembers(_io__raw_info, self, self._root)
            elif _on == u"PermittedSubclasses":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyPermittedSubclasses(_io__raw_info, self, self._root)
            elif _on == u"Record":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyRecord(_io__raw_info, self, self._root)
            elif _on == u"RuntimeVisibleAnnotations":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations(_io__raw_info, self, self._root)
            elif _on == u"Signature":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodySignature(_io__raw_info, self, self._root)
            elif _on == u"SourceDebugExtension":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodySourceDebugExtension(_io__raw_info, self, self._root)
            elif _on == u"SourceFile":
                pass
                self._raw_info = self._io.read_bytes(self.attribute_length)
                _io__raw_info = KaitaiStream(BytesIO(self._raw_info))
                self.info = JavaClass.AttributeInfo.AttrBodySourceFile(_io__raw_info, self, self._root)
            else:
                pass
                self.info = self._io.read_bytes(self.attribute_length)
            self._debug['info']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            _on = (self.name_as_str).decode(u"ascii")
            if _on == u"Code":
                pass
                self.info._fetch_instances()
            elif _on == u"ConstantValue":
                pass
                self.info._fetch_instances()
            elif _on == u"EnclosingMethod":
                pass
                self.info._fetch_instances()
            elif _on == u"Exceptions":
                pass
                self.info._fetch_instances()
            elif _on == u"InnerClasses":
                pass
                self.info._fetch_instances()
            elif _on == u"LineNumberTable":
                pass
                self.info._fetch_instances()
            elif _on == u"LocalVariableTable":
                pass
                self.info._fetch_instances()
            elif _on == u"LocalVariableTypeTable":
                pass
                self.info._fetch_instances()
            elif _on == u"ModuleMainClass":
                pass
                self.info._fetch_instances()
            elif _on == u"ModulePackages":
                pass
                self.info._fetch_instances()
            elif _on == u"NestHost":
                pass
                self.info._fetch_instances()
            elif _on == u"NestMembers":
                pass
                self.info._fetch_instances()
            elif _on == u"PermittedSubclasses":
                pass
                self.info._fetch_instances()
            elif _on == u"Record":
                pass
                self.info._fetch_instances()
            elif _on == u"RuntimeVisibleAnnotations":
                pass
                self.info._fetch_instances()
            elif _on == u"Signature":
                pass
                self.info._fetch_instances()
            elif _on == u"SourceDebugExtension":
                pass
                self.info._fetch_instances()
            elif _on == u"SourceFile":
                pass
                self.info._fetch_instances()
            else:
                pass

        class AttrBodyCode(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.3
            """
            SEQ_FIELDS = ["max_stack", "max_locals", "code_length", "code", "exception_table_length", "exception_table", "attributes_count", "attributes"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyCode, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['max_stack']['start'] = self._io.pos()
                self.max_stack = self._io.read_u2be()
                self._debug['max_stack']['end'] = self._io.pos()
                self._debug['max_locals']['start'] = self._io.pos()
                self.max_locals = self._io.read_u2be()
                self._debug['max_locals']['end'] = self._io.pos()
                self._debug['code_length']['start'] = self._io.pos()
                self.code_length = self._io.read_u4be()
                self._debug['code_length']['end'] = self._io.pos()
                self._debug['code']['start'] = self._io.pos()
                self.code = self._io.read_bytes(self.code_length)
                self._debug['code']['end'] = self._io.pos()
                self._debug['exception_table_length']['start'] = self._io.pos()
                self.exception_table_length = self._io.read_u2be()
                self._debug['exception_table_length']['end'] = self._io.pos()
                self._debug['exception_table']['start'] = self._io.pos()
                self._debug['exception_table']['arr'] = []
                self.exception_table = []
                for i in range(self.exception_table_length):
                    self._debug['exception_table']['arr'].append({'start': self._io.pos()})
                    self.exception_table.append(JavaClass.AttributeInfo.AttrBodyCode.ExceptionEntry(self._io, self, self._root))
                    self._debug['exception_table']['arr'][i]['end'] = self._io.pos()

                self._debug['exception_table']['end'] = self._io.pos()
                self._debug['attributes_count']['start'] = self._io.pos()
                self.attributes_count = self._io.read_u2be()
                self._debug['attributes_count']['end'] = self._io.pos()
                self._debug['attributes']['start'] = self._io.pos()
                self._debug['attributes']['arr'] = []
                self.attributes = []
                for i in range(self.attributes_count):
                    self._debug['attributes']['arr'].append({'start': self._io.pos()})
                    self.attributes.append(JavaClass.AttributeInfo(self._io, self, self._root))
                    self._debug['attributes']['arr'][i]['end'] = self._io.pos()

                self._debug['attributes']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.exception_table)):
                    pass
                    self.exception_table[i]._fetch_instances()

                for i in range(len(self.attributes)):
                    pass
                    self.attributes[i]._fetch_instances()


            class ExceptionEntry(KaitaiStruct):
                """
                .. seealso::
                   Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.3
                """
                SEQ_FIELDS = ["start_pc", "end_pc", "handler_pc", "catch_type"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(JavaClass.AttributeInfo.AttrBodyCode.ExceptionEntry, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['start_pc']['start'] = self._io.pos()
                    self.start_pc = self._io.read_u2be()
                    self._debug['start_pc']['end'] = self._io.pos()
                    self._debug['end_pc']['start'] = self._io.pos()
                    self.end_pc = self._io.read_u2be()
                    self._debug['end_pc']['end'] = self._io.pos()
                    self._debug['handler_pc']['start'] = self._io.pos()
                    self.handler_pc = self._io.read_u2be()
                    self._debug['handler_pc']['end'] = self._io.pos()
                    self._debug['catch_type']['start'] = self._io.pos()
                    self.catch_type = self._io.read_u2be()
                    self._debug['catch_type']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def catch_exception(self):
                    if hasattr(self, '_m_catch_exception'):
                        return self._m_catch_exception

                    if self.catch_type != 0:
                        pass
                        self._m_catch_exception = self._root.constant_pool[self.catch_type - 1]

                    return getattr(self, '_m_catch_exception', None)



        class AttrBodyConstantValue(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.2
            """
            SEQ_FIELDS = ["constant_value_index"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyConstantValue, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['constant_value_index']['start'] = self._io.pos()
                self.constant_value_index = self._io.read_u2be()
                self._debug['constant_value_index']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass

            @property
            def constant_value(self):
                if hasattr(self, '_m_constant_value'):
                    return self._m_constant_value

                self._m_constant_value = self._root.constant_pool[self.constant_value_index - 1].cp_info.value
                return getattr(self, '_m_constant_value', None)


        class AttrBodyEnclosingMethod(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.7
            """
            SEQ_FIELDS = ["class_index", "method_index"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyEnclosingMethod, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['class_index']['start'] = self._io.pos()
                self.class_index = self._io.read_u2be()
                self._debug['class_index']['end'] = self._io.pos()
                self._debug['method_index']['start'] = self._io.pos()
                self.method_index = self._io.read_u2be()
                self._debug['method_index']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass

            @property
            def class_file(self):
                if hasattr(self, '_m_class_file'):
                    return self._m_class_file

                self._m_class_file = self._root.constant_pool[self.class_index - 1].cp_info
                return getattr(self, '_m_class_file', None)

            @property
            def method_name_type(self):
                if hasattr(self, '_m_method_name_type'):
                    return self._m_method_name_type

                if self.method_index != 0:
                    pass
                    self._m_method_name_type = self._root.constant_pool[self.method_index - 1].cp_info

                return getattr(self, '_m_method_name_type', None)


        class AttrBodyExceptions(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.5
            """
            SEQ_FIELDS = ["number_of_exceptions", "exceptions"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyExceptions, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['number_of_exceptions']['start'] = self._io.pos()
                self.number_of_exceptions = self._io.read_u2be()
                self._debug['number_of_exceptions']['end'] = self._io.pos()
                self._debug['exceptions']['start'] = self._io.pos()
                self._debug['exceptions']['arr'] = []
                self.exceptions = []
                for i in range(self.number_of_exceptions):
                    self._debug['exceptions']['arr'].append({'start': self._io.pos()})
                    self.exceptions.append(JavaClass.AttributeInfo.AttrBodyExceptions.ExceptionTableEntry(self._io, self, self._root))
                    self._debug['exceptions']['arr'][i]['end'] = self._io.pos()

                self._debug['exceptions']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.exceptions)):
                    pass
                    self.exceptions[i]._fetch_instances()


            class ExceptionTableEntry(KaitaiStruct):
                SEQ_FIELDS = ["index"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(JavaClass.AttributeInfo.AttrBodyExceptions.ExceptionTableEntry, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['index']['start'] = self._io.pos()
                    self.index = self._io.read_u2be()
                    self._debug['index']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def as_info(self):
                    if hasattr(self, '_m_as_info'):
                        return self._m_as_info

                    self._m_as_info = self._root.constant_pool[self.index - 1].cp_info
                    return getattr(self, '_m_as_info', None)

                @property
                def name_as_str(self):
                    if hasattr(self, '_m_name_as_str'):
                        return self._m_name_as_str

                    self._m_name_as_str = self.as_info.name_as_str
                    return getattr(self, '_m_name_as_str', None)



        class AttrBodyInnerClasses(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.6
            """
            SEQ_FIELDS = ["num_inner_classes", "inner_classes"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyInnerClasses, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['num_inner_classes']['start'] = self._io.pos()
                self.num_inner_classes = self._io.read_u2be()
                self._debug['num_inner_classes']['end'] = self._io.pos()
                self._debug['inner_classes']['start'] = self._io.pos()
                self._debug['inner_classes']['arr'] = []
                self.inner_classes = []
                for i in range(self.num_inner_classes):
                    self._debug['inner_classes']['arr'].append({'start': self._io.pos()})
                    self.inner_classes.append(JavaClass.AttributeInfo.AttrBodyInnerClasses.InnerClass(self._io, self, self._root))
                    self._debug['inner_classes']['arr'][i]['end'] = self._io.pos()

                self._debug['inner_classes']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.inner_classes)):
                    pass
                    self.inner_classes[i]._fetch_instances()


            class InnerClass(KaitaiStruct):
                SEQ_FIELDS = ["inner_class_info_index", "outer_class_info_index", "inner_name_index", "access_flags"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(JavaClass.AttributeInfo.AttrBodyInnerClasses.InnerClass, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['inner_class_info_index']['start'] = self._io.pos()
                    self.inner_class_info_index = self._io.read_u2be()
                    self._debug['inner_class_info_index']['end'] = self._io.pos()
                    self._debug['outer_class_info_index']['start'] = self._io.pos()
                    self.outer_class_info_index = self._io.read_u2be()
                    self._debug['outer_class_info_index']['end'] = self._io.pos()
                    self._debug['inner_name_index']['start'] = self._io.pos()
                    self.inner_name_index = self._io.read_u2be()
                    self._debug['inner_name_index']['end'] = self._io.pos()
                    self._debug['access_flags']['start'] = self._io.pos()
                    self.access_flags = self._io.read_u2be()
                    self._debug['access_flags']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def inner_class(self):
                    if hasattr(self, '_m_inner_class'):
                        return self._m_inner_class

                    self._m_inner_class = self._root.constant_pool[self.inner_class_info_index - 1].cp_info
                    return getattr(self, '_m_inner_class', None)

                @property
                def inner_class_name(self):
                    if hasattr(self, '_m_inner_class_name'):
                        return self._m_inner_class_name

                    if self.inner_name_index != 0:
                        pass
                        self._m_inner_class_name = self._root.constant_pool[self.inner_name_index - 1].cp_info.value

                    return getattr(self, '_m_inner_class_name', None)

                @property
                def is_abstract(self):
                    if hasattr(self, '_m_is_abstract'):
                        return self._m_is_abstract

                    self._m_is_abstract = self.access_flags & 1024 == 1024
                    return getattr(self, '_m_is_abstract', None)

                @property
                def is_annotation(self):
                    if hasattr(self, '_m_is_annotation'):
                        return self._m_is_annotation

                    self._m_is_annotation = self.access_flags & 8192 == 8192
                    return getattr(self, '_m_is_annotation', None)

                @property
                def is_enum(self):
                    if hasattr(self, '_m_is_enum'):
                        return self._m_is_enum

                    self._m_is_enum = self.access_flags & 16384 == 16384
                    return getattr(self, '_m_is_enum', None)

                @property
                def is_final(self):
                    if hasattr(self, '_m_is_final'):
                        return self._m_is_final

                    self._m_is_final = self.access_flags & 16 == 16
                    return getattr(self, '_m_is_final', None)

                @property
                def is_interface(self):
                    if hasattr(self, '_m_is_interface'):
                        return self._m_is_interface

                    self._m_is_interface = self.access_flags & 512 == 512
                    return getattr(self, '_m_is_interface', None)

                @property
                def is_private(self):
                    if hasattr(self, '_m_is_private'):
                        return self._m_is_private

                    self._m_is_private = self.access_flags & 2 == 2
                    return getattr(self, '_m_is_private', None)

                @property
                def is_protected(self):
                    if hasattr(self, '_m_is_protected'):
                        return self._m_is_protected

                    self._m_is_protected = self.access_flags & 4 == 4
                    return getattr(self, '_m_is_protected', None)

                @property
                def is_public(self):
                    if hasattr(self, '_m_is_public'):
                        return self._m_is_public

                    self._m_is_public = self.access_flags & 1 == 1
                    return getattr(self, '_m_is_public', None)

                @property
                def is_static(self):
                    if hasattr(self, '_m_is_static'):
                        return self._m_is_static

                    self._m_is_static = self.access_flags & 8 == 8
                    return getattr(self, '_m_is_static', None)

                @property
                def is_synthetic(self):
                    if hasattr(self, '_m_is_synthetic'):
                        return self._m_is_synthetic

                    self._m_is_synthetic = self.access_flags & 4096 == 4096
                    return getattr(self, '_m_is_synthetic', None)

                @property
                def outer_class(self):
                    if hasattr(self, '_m_outer_class'):
                        return self._m_outer_class

                    if self.outer_class_info_index != 0:
                        pass
                        self._m_outer_class = self._root.constant_pool[self.outer_class_info_index - 1].cp_info

                    return getattr(self, '_m_outer_class', None)



        class AttrBodyLineNumberTable(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.12
            """
            SEQ_FIELDS = ["line_number_table_length", "line_number_table"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyLineNumberTable, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['line_number_table_length']['start'] = self._io.pos()
                self.line_number_table_length = self._io.read_u2be()
                self._debug['line_number_table_length']['end'] = self._io.pos()
                self._debug['line_number_table']['start'] = self._io.pos()
                self._debug['line_number_table']['arr'] = []
                self.line_number_table = []
                for i in range(self.line_number_table_length):
                    self._debug['line_number_table']['arr'].append({'start': self._io.pos()})
                    self.line_number_table.append(JavaClass.AttributeInfo.AttrBodyLineNumberTable.LineNumberTableEntry(self._io, self, self._root))
                    self._debug['line_number_table']['arr'][i]['end'] = self._io.pos()

                self._debug['line_number_table']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.line_number_table)):
                    pass
                    self.line_number_table[i]._fetch_instances()


            class LineNumberTableEntry(KaitaiStruct):
                SEQ_FIELDS = ["start_pc", "line_number"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(JavaClass.AttributeInfo.AttrBodyLineNumberTable.LineNumberTableEntry, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['start_pc']['start'] = self._io.pos()
                    self.start_pc = self._io.read_u2be()
                    self._debug['start_pc']['end'] = self._io.pos()
                    self._debug['line_number']['start'] = self._io.pos()
                    self.line_number = self._io.read_u2be()
                    self._debug['line_number']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass



        class AttrBodyLocalVariableTable(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.13
            """
            SEQ_FIELDS = ["local_variable_table_length", "local_variable_table"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyLocalVariableTable, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['local_variable_table_length']['start'] = self._io.pos()
                self.local_variable_table_length = self._io.read_u2be()
                self._debug['local_variable_table_length']['end'] = self._io.pos()
                self._debug['local_variable_table']['start'] = self._io.pos()
                self._debug['local_variable_table']['arr'] = []
                self.local_variable_table = []
                for i in range(self.local_variable_table_length):
                    self._debug['local_variable_table']['arr'].append({'start': self._io.pos()})
                    self.local_variable_table.append(JavaClass.AttributeInfo.AttrBodyLocalVariableTable.LocalVariableTableEntry(self._io, self, self._root))
                    self._debug['local_variable_table']['arr'][i]['end'] = self._io.pos()

                self._debug['local_variable_table']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.local_variable_table)):
                    pass
                    self.local_variable_table[i]._fetch_instances()


            class LocalVariableTableEntry(KaitaiStruct):
                SEQ_FIELDS = ["start_pc", "length", "name_index", "descriptor_index", "index"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(JavaClass.AttributeInfo.AttrBodyLocalVariableTable.LocalVariableTableEntry, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['start_pc']['start'] = self._io.pos()
                    self.start_pc = self._io.read_u2be()
                    self._debug['start_pc']['end'] = self._io.pos()
                    self._debug['length']['start'] = self._io.pos()
                    self.length = self._io.read_u2be()
                    self._debug['length']['end'] = self._io.pos()
                    self._debug['name_index']['start'] = self._io.pos()
                    self.name_index = self._io.read_u2be()
                    self._debug['name_index']['end'] = self._io.pos()
                    self._debug['descriptor_index']['start'] = self._io.pos()
                    self.descriptor_index = self._io.read_u2be()
                    self._debug['descriptor_index']['end'] = self._io.pos()
                    self._debug['index']['start'] = self._io.pos()
                    self.index = self._io.read_u2be()
                    self._debug['index']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def descriptor_as_str(self):
                    if hasattr(self, '_m_descriptor_as_str'):
                        return self._m_descriptor_as_str

                    self._m_descriptor_as_str = self._root.constant_pool[self.descriptor_index - 1].cp_info.raw_value
                    return getattr(self, '_m_descriptor_as_str', None)

                @property
                def name_as_str(self):
                    if hasattr(self, '_m_name_as_str'):
                        return self._m_name_as_str

                    self._m_name_as_str = self._root.constant_pool[self.name_index - 1].cp_info.raw_value
                    return getattr(self, '_m_name_as_str', None)



        class AttrBodyLocalVariableTypeTable(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.14
            """
            SEQ_FIELDS = ["local_variable_type_table_length", "local_variable_type_table"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyLocalVariableTypeTable, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['local_variable_type_table_length']['start'] = self._io.pos()
                self.local_variable_type_table_length = self._io.read_u2be()
                self._debug['local_variable_type_table_length']['end'] = self._io.pos()
                self._debug['local_variable_type_table']['start'] = self._io.pos()
                self._debug['local_variable_type_table']['arr'] = []
                self.local_variable_type_table = []
                for i in range(self.local_variable_type_table_length):
                    self._debug['local_variable_type_table']['arr'].append({'start': self._io.pos()})
                    self.local_variable_type_table.append(JavaClass.AttributeInfo.AttrBodyLocalVariableTypeTable.LocalVariableTypeTableEntry(self._io, self, self._root))
                    self._debug['local_variable_type_table']['arr'][i]['end'] = self._io.pos()

                self._debug['local_variable_type_table']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.local_variable_type_table)):
                    pass
                    self.local_variable_type_table[i]._fetch_instances()


            class LocalVariableTypeTableEntry(KaitaiStruct):
                SEQ_FIELDS = ["start_pc", "length", "name_index", "signature_index", "index"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(JavaClass.AttributeInfo.AttrBodyLocalVariableTypeTable.LocalVariableTypeTableEntry, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['start_pc']['start'] = self._io.pos()
                    self.start_pc = self._io.read_u2be()
                    self._debug['start_pc']['end'] = self._io.pos()
                    self._debug['length']['start'] = self._io.pos()
                    self.length = self._io.read_u2be()
                    self._debug['length']['end'] = self._io.pos()
                    self._debug['name_index']['start'] = self._io.pos()
                    self.name_index = self._io.read_u2be()
                    self._debug['name_index']['end'] = self._io.pos()
                    self._debug['signature_index']['start'] = self._io.pos()
                    self.signature_index = self._io.read_u2be()
                    self._debug['signature_index']['end'] = self._io.pos()
                    self._debug['index']['start'] = self._io.pos()
                    self.index = self._io.read_u2be()
                    self._debug['index']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def name_as_str(self):
                    if hasattr(self, '_m_name_as_str'):
                        return self._m_name_as_str

                    self._m_name_as_str = self._root.constant_pool[self.name_index - 1].cp_info.raw_value
                    return getattr(self, '_m_name_as_str', None)

                @property
                def signature_as_str(self):
                    if hasattr(self, '_m_signature_as_str'):
                        return self._m_signature_as_str

                    self._m_signature_as_str = self._root.constant_pool[self.signature_index - 1].cp_info.raw_value
                    return getattr(self, '_m_signature_as_str', None)



        class AttrBodyModuleMainClass(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.27
            """
            SEQ_FIELDS = ["main_class_index"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyModuleMainClass, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['main_class_index']['start'] = self._io.pos()
                self.main_class_index = self._io.read_u2be()
                self._debug['main_class_index']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass

            @property
            def main_class(self):
                if hasattr(self, '_m_main_class'):
                    return self._m_main_class

                self._m_main_class = self._root.constant_pool[self.main_class_index - 1].cp_info
                return getattr(self, '_m_main_class', None)


        class AttrBodyModulePackages(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.26
            """
            SEQ_FIELDS = ["num_packages", "packages"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyModulePackages, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['num_packages']['start'] = self._io.pos()
                self.num_packages = self._io.read_u2be()
                self._debug['num_packages']['end'] = self._io.pos()
                self._debug['packages']['start'] = self._io.pos()
                self._debug['packages']['arr'] = []
                self.packages = []
                for i in range(self.num_packages):
                    self._debug['packages']['arr'].append({'start': self._io.pos()})
                    self.packages.append(JavaClass.AttributeInfo.AttrBodyModulePackages.ModulePackage(self._io, self, self._root))
                    self._debug['packages']['arr'][i]['end'] = self._io.pos()

                self._debug['packages']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.packages)):
                    pass
                    self.packages[i]._fetch_instances()


            class ModulePackage(KaitaiStruct):
                SEQ_FIELDS = ["package_index"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(JavaClass.AttributeInfo.AttrBodyModulePackages.ModulePackage, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['package_index']['start'] = self._io.pos()
                    self.package_index = self._io.read_u2be()
                    self._debug['package_index']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def module_package(self):
                    if hasattr(self, '_m_module_package'):
                        return self._m_module_package

                    self._m_module_package = self._root.constant_pool[self.package_index - 1].cp_info
                    return getattr(self, '_m_module_package', None)



        class AttrBodyNestHost(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.28
            """
            SEQ_FIELDS = ["host_class_index"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyNestHost, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['host_class_index']['start'] = self._io.pos()
                self.host_class_index = self._io.read_u2be()
                self._debug['host_class_index']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass

            @property
            def host_class(self):
                if hasattr(self, '_m_host_class'):
                    return self._m_host_class

                self._m_host_class = self._root.constant_pool[self.host_class_index - 1].cp_info
                return getattr(self, '_m_host_class', None)


        class AttrBodyNestMembers(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.29
            """
            SEQ_FIELDS = ["num_classes", "classes"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyNestMembers, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['num_classes']['start'] = self._io.pos()
                self.num_classes = self._io.read_u2be()
                self._debug['num_classes']['end'] = self._io.pos()
                self._debug['classes']['start'] = self._io.pos()
                self.classes = JavaClass.AttributeInfo.AttrBodyNestMembers.NestedClass(self._io, self, self._root)
                self._debug['classes']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.classes._fetch_instances()

            class NestedClass(KaitaiStruct):
                SEQ_FIELDS = ["class_index"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(JavaClass.AttributeInfo.AttrBodyNestMembers.NestedClass, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['class_index']['start'] = self._io.pos()
                    self.class_index = self._io.read_u2be()
                    self._debug['class_index']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def nested_class(self):
                    if hasattr(self, '_m_nested_class'):
                        return self._m_nested_class

                    self._m_nested_class = self._root.constant_pool[self.class_index - 1].cp_info
                    return getattr(self, '_m_nested_class', None)



        class AttrBodyPermittedSubclasses(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.31
            """
            SEQ_FIELDS = ["num_classes", "classes"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyPermittedSubclasses, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['num_classes']['start'] = self._io.pos()
                self.num_classes = self._io.read_u2be()
                self._debug['num_classes']['end'] = self._io.pos()
                self._debug['classes']['start'] = self._io.pos()
                self.classes = JavaClass.AttributeInfo.AttrBodyPermittedSubclasses.Subclass(self._io, self, self._root)
                self._debug['classes']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.classes._fetch_instances()

            class Subclass(KaitaiStruct):
                SEQ_FIELDS = ["class_index"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(JavaClass.AttributeInfo.AttrBodyPermittedSubclasses.Subclass, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['class_index']['start'] = self._io.pos()
                    self.class_index = self._io.read_u2be()
                    self._debug['class_index']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass

                @property
                def subclass(self):
                    if hasattr(self, '_m_subclass'):
                        return self._m_subclass

                    self._m_subclass = self._root.constant_pool[self.class_index - 1].cp_info
                    return getattr(self, '_m_subclass', None)



        class AttrBodyRecord(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.30
            """
            SEQ_FIELDS = ["num_components", "components"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyRecord, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['num_components']['start'] = self._io.pos()
                self.num_components = self._io.read_u2be()
                self._debug['num_components']['end'] = self._io.pos()
                self._debug['components']['start'] = self._io.pos()
                self.components = JavaClass.AttributeInfo.AttrBodyRecord.RecordComponentInfo(self._io, self, self._root)
                self._debug['components']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                self.components._fetch_instances()

            class RecordComponentInfo(KaitaiStruct):
                SEQ_FIELDS = ["name_index", "descriptor_index", "num_attributes", "attributes"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(JavaClass.AttributeInfo.AttrBodyRecord.RecordComponentInfo, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['name_index']['start'] = self._io.pos()
                    self.name_index = self._io.read_u2be()
                    self._debug['name_index']['end'] = self._io.pos()
                    self._debug['descriptor_index']['start'] = self._io.pos()
                    self.descriptor_index = self._io.read_u2be()
                    self._debug['descriptor_index']['end'] = self._io.pos()
                    self._debug['num_attributes']['start'] = self._io.pos()
                    self.num_attributes = self._io.read_u2be()
                    self._debug['num_attributes']['end'] = self._io.pos()
                    self._debug['attributes']['start'] = self._io.pos()
                    self._debug['attributes']['arr'] = []
                    self.attributes = []
                    for i in range(self.num_attributes):
                        self._debug['attributes']['arr'].append({'start': self._io.pos()})
                        self.attributes.append(JavaClass.AttributeInfo(self._io, self, self._root))
                        self._debug['attributes']['arr'][i]['end'] = self._io.pos()

                    self._debug['attributes']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    for i in range(len(self.attributes)):
                        pass
                        self.attributes[i]._fetch_instances()


                @property
                def descriptor(self):
                    if hasattr(self, '_m_descriptor'):
                        return self._m_descriptor

                    self._m_descriptor = self._root.constant_pool[self.descriptor_index - 1].cp_info.raw_value
                    return getattr(self, '_m_descriptor', None)

                @property
                def name(self):
                    if hasattr(self, '_m_name'):
                        return self._m_name

                    self._m_name = self._root.constant_pool[self.name_index - 1].cp_info.raw_value
                    return getattr(self, '_m_name', None)



        class AttrBodyRuntimeVisibleAnnotations(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.16
            """
            SEQ_FIELDS = ["num_annotations", "annotations"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['num_annotations']['start'] = self._io.pos()
                self.num_annotations = self._io.read_u2be()
                self._debug['num_annotations']['end'] = self._io.pos()
                self._debug['annotations']['start'] = self._io.pos()
                self._debug['annotations']['arr'] = []
                self.annotations = []
                for i in range(self.num_annotations):
                    self._debug['annotations']['arr'].append({'start': self._io.pos()})
                    self.annotations.append(JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation(self._io, self, self._root))
                    self._debug['annotations']['arr'][i]['end'] = self._io.pos()

                self._debug['annotations']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass
                for i in range(len(self.annotations)):
                    pass
                    self.annotations[i]._fetch_instances()


            class Annotation(KaitaiStruct):
                SEQ_FIELDS = ["type_index", "num_element_value_pairs", "element_value_pairs"]
                def __init__(self, _io, _parent=None, _root=None):
                    super(JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation, self).__init__(_io)
                    self._parent = _parent
                    self._root = _root
                    self._debug = collections.defaultdict(dict)
                    self._read()

                def _read(self):
                    self._debug['type_index']['start'] = self._io.pos()
                    self.type_index = self._io.read_u2be()
                    self._debug['type_index']['end'] = self._io.pos()
                    self._debug['num_element_value_pairs']['start'] = self._io.pos()
                    self.num_element_value_pairs = self._io.read_u2be()
                    self._debug['num_element_value_pairs']['end'] = self._io.pos()
                    self._debug['element_value_pairs']['start'] = self._io.pos()
                    self._debug['element_value_pairs']['arr'] = []
                    self.element_value_pairs = []
                    for i in range(self.num_element_value_pairs):
                        self._debug['element_value_pairs']['arr'].append({'start': self._io.pos()})
                        self.element_value_pairs.append(JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair(self._io, self, self._root))
                        self._debug['element_value_pairs']['arr'][i]['end'] = self._io.pos()

                    self._debug['element_value_pairs']['end'] = self._io.pos()


                def _fetch_instances(self):
                    pass
                    for i in range(len(self.element_value_pairs)):
                        pass
                        self.element_value_pairs[i]._fetch_instances()


                class ElementValuePair(KaitaiStruct):
                    SEQ_FIELDS = ["element_name_index", "element_value"]
                    def __init__(self, _io, _parent=None, _root=None):
                        super(JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair, self).__init__(_io)
                        self._parent = _parent
                        self._root = _root
                        self._debug = collections.defaultdict(dict)
                        self._read()

                    def _read(self):
                        self._debug['element_name_index']['start'] = self._io.pos()
                        self.element_name_index = self._io.read_u2be()
                        self._debug['element_name_index']['end'] = self._io.pos()
                        self._debug['element_value']['start'] = self._io.pos()
                        self.element_value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue(self._io, self, self._root)
                        self._debug['element_value']['end'] = self._io.pos()


                    def _fetch_instances(self):
                        pass
                        self.element_value._fetch_instances()

                    class ElementValue(KaitaiStruct):
                        SEQ_FIELDS = ["tag", "value"]
                        def __init__(self, _io, _parent=None, _root=None):
                            super(JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue, self).__init__(_io)
                            self._parent = _parent
                            self._root = _root
                            self._debug = collections.defaultdict(dict)
                            self._read()

                        def _read(self):
                            self._debug['tag']['start'] = self._io.pos()
                            self.tag = (self._io.read_bytes(1)).decode(u"ASCII")
                            self._debug['tag']['end'] = self._io.pos()
                            self._debug['value']['start'] = self._io.pos()
                            _on = self.tag
                            if _on == u"@":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation(self._io, self, self._root)
                            elif _on == u"B":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ConstValueIndex(self._io, self, self._root)
                            elif _on == u"C":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ConstValueIndex(self._io, self, self._root)
                            elif _on == u"D":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ConstValueIndex(self._io, self, self._root)
                            elif _on == u"F":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ConstValueIndex(self._io, self, self._root)
                            elif _on == u"I":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ConstValueIndex(self._io, self, self._root)
                            elif _on == u"J":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ConstValueIndex(self._io, self, self._root)
                            elif _on == u"S":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ConstValueIndex(self._io, self, self._root)
                            elif _on == u"Z":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ConstValueIndex(self._io, self, self._root)
                            elif _on == u"[":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ArrayType(self._io, self, self._root)
                            elif _on == u"c":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ClassInfoIndex(self._io, self, self._root)
                            elif _on == u"e":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.EnumConstValue(self._io, self, self._root)
                            elif _on == u"s":
                                pass
                                self.value = JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ConstValueIndex(self._io, self, self._root)
                            self._debug['value']['end'] = self._io.pos()


                        def _fetch_instances(self):
                            pass
                            _on = self.tag
                            if _on == u"@":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"B":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"C":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"D":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"F":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"I":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"J":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"S":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"Z":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"[":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"c":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"e":
                                pass
                                self.value._fetch_instances()
                            elif _on == u"s":
                                pass
                                self.value._fetch_instances()

                        class ArrayType(KaitaiStruct):
                            SEQ_FIELDS = ["num_values", "element_values"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ArrayType, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['num_values']['start'] = self._io.pos()
                                self.num_values = self._io.read_u2be()
                                self._debug['num_values']['end'] = self._io.pos()
                                self._debug['element_values']['start'] = self._io.pos()
                                self._debug['element_values']['arr'] = []
                                self.element_values = []
                                for i in range(self.num_values):
                                    self._debug['element_values']['arr'].append({'start': self._io.pos()})
                                    self.element_values.append(JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue(self._io, self, self._root))
                                    self._debug['element_values']['arr'][i]['end'] = self._io.pos()

                                self._debug['element_values']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass
                                for i in range(len(self.element_values)):
                                    pass
                                    self.element_values[i]._fetch_instances()



                        class ClassInfoIndex(KaitaiStruct):
                            SEQ_FIELDS = ["value_index"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ClassInfoIndex, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['value_index']['start'] = self._io.pos()
                                self.value_index = self._io.read_u2be()
                                self._debug['value_index']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass

                            @property
                            def const_value(self):
                                if hasattr(self, '_m_const_value'):
                                    return self._m_const_value

                                self._m_const_value = self._root.constant_pool[self.value_index - 1].cp_info.raw_value
                                return getattr(self, '_m_const_value', None)


                        class ConstValueIndex(KaitaiStruct):
                            SEQ_FIELDS = ["value_index"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.ConstValueIndex, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['value_index']['start'] = self._io.pos()
                                self.value_index = self._io.read_u2be()
                                self._debug['value_index']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass

                            @property
                            def const_value(self):
                                if hasattr(self, '_m_const_value'):
                                    return self._m_const_value

                                self._m_const_value = self._root.constant_pool[self.value_index - 1]
                                return getattr(self, '_m_const_value', None)


                        class EnumConstValue(KaitaiStruct):
                            SEQ_FIELDS = ["type_name_index", "const_name_index"]
                            def __init__(self, _io, _parent=None, _root=None):
                                super(JavaClass.AttributeInfo.AttrBodyRuntimeVisibleAnnotations.Annotation.ElementValuePair.ElementValue.EnumConstValue, self).__init__(_io)
                                self._parent = _parent
                                self._root = _root
                                self._debug = collections.defaultdict(dict)
                                self._read()

                            def _read(self):
                                self._debug['type_name_index']['start'] = self._io.pos()
                                self.type_name_index = self._io.read_u2be()
                                self._debug['type_name_index']['end'] = self._io.pos()
                                self._debug['const_name_index']['start'] = self._io.pos()
                                self.const_name_index = self._io.read_u2be()
                                self._debug['const_name_index']['end'] = self._io.pos()


                            def _fetch_instances(self):
                                pass

                            @property
                            def const_name(self):
                                if hasattr(self, '_m_const_name'):
                                    return self._m_const_name

                                self._m_const_name = self._root.constant_pool[self.const_name_index - 1].cp_info.raw_value
                                return getattr(self, '_m_const_name', None)

                            @property
                            def type_name(self):
                                if hasattr(self, '_m_type_name'):
                                    return self._m_type_name

                                self._m_type_name = self._root.constant_pool[self.type_name_index - 1].cp_info.raw_value
                                return getattr(self, '_m_type_name', None)



                    @property
                    def element_name_as_str(self):
                        if hasattr(self, '_m_element_name_as_str'):
                            return self._m_element_name_as_str

                        self._m_element_name_as_str = self._root.constant_pool[self.element_name_index - 1].cp_info.raw_value
                        return getattr(self, '_m_element_name_as_str', None)


                @property
                def type_as_str(self):
                    if hasattr(self, '_m_type_as_str'):
                        return self._m_type_as_str

                    self._m_type_as_str = self._root.constant_pool[self.type_index - 1].cp_info.raw_value
                    return getattr(self, '_m_type_as_str', None)



        class AttrBodySignature(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.9
            """
            SEQ_FIELDS = ["signature_index"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodySignature, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['signature_index']['start'] = self._io.pos()
                self.signature_index = self._io.read_u2be()
                self._debug['signature_index']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass

            @property
            def signature_as_str(self):
                if hasattr(self, '_m_signature_as_str'):
                    return self._m_signature_as_str

                self._m_signature_as_str = self._root.constant_pool[self.signature_index - 1].cp_info.value
                return getattr(self, '_m_signature_as_str', None)


        class AttrBodySourceDebugExtension(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.11
            """
            SEQ_FIELDS = ["debug_extension"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodySourceDebugExtension, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['debug_extension']['start'] = self._io.pos()
                self.debug_extension = self._io.read_bytes_full()
                self._debug['debug_extension']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass


        class AttrBodySourceFile(KaitaiStruct):
            """
            .. seealso::
               Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.7.10
            """
            SEQ_FIELDS = ["sourcefile_index"]
            def __init__(self, _io, _parent=None, _root=None):
                super(JavaClass.AttributeInfo.AttrBodySourceFile, self).__init__(_io)
                self._parent = _parent
                self._root = _root
                self._debug = collections.defaultdict(dict)
                self._read()

            def _read(self):
                self._debug['sourcefile_index']['start'] = self._io.pos()
                self.sourcefile_index = self._io.read_u2be()
                self._debug['sourcefile_index']['end'] = self._io.pos()


            def _fetch_instances(self):
                pass

            @property
            def sourcefile_as_str(self):
                if hasattr(self, '_m_sourcefile_as_str'):
                    return self._m_sourcefile_as_str

                self._m_sourcefile_as_str = self._root.constant_pool[self.sourcefile_index - 1].cp_info.value
                return getattr(self, '_m_sourcefile_as_str', None)


        @property
        def name_as_str(self):
            if hasattr(self, '_m_name_as_str'):
                return self._m_name_as_str

            self._m_name_as_str = self._root.constant_pool[self.name_index - 1].cp_info.raw_value
            return getattr(self, '_m_name_as_str', None)

        @property
        def name_as_str_str(self):
            if hasattr(self, '_m_name_as_str_str'):
                return self._m_name_as_str_str

            self._m_name_as_str_str = (self._root.constant_pool[self.name_index - 1].cp_info.raw_value).decode(u"ascii")
            return getattr(self, '_m_name_as_str_str', None)


    class ClassCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.1
        """
        SEQ_FIELDS = ["name_index"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.ClassCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name_index']['start'] = self._io.pos()
            self.name_index = self._io.read_u2be()
            self._debug['name_index']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def name_as_info(self):
            if hasattr(self, '_m_name_as_info'):
                return self._m_name_as_info

            self._m_name_as_info = self._root.constant_pool[self.name_index - 1].cp_info
            return getattr(self, '_m_name_as_info', None)

        @property
        def name_as_str(self):
            if hasattr(self, '_m_name_as_str'):
                return self._m_name_as_str

            self._m_name_as_str = self.name_as_info.value
            return getattr(self, '_m_name_as_str', None)


    class ConstantPoolEntry(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4
        """

        class TagEnum(IntEnum):
            utf8 = 1
            integer = 3
            float = 4
            long = 5
            double = 6
            class_type = 7
            string = 8
            field_ref = 9
            method_ref = 10
            interface_method_ref = 11
            name_and_type = 12
            method_handle = 15
            method_type = 16
            dynamic = 17
            invoke_dynamic = 18
            module = 19
            package = 20
        SEQ_FIELDS = ["tag", "cp_info"]
        def __init__(self, is_prev_two_entries, _io, _parent=None, _root=None):
            super(JavaClass.ConstantPoolEntry, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self.is_prev_two_entries = is_prev_two_entries
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            if (not (self.is_prev_two_entries)):
                pass
                self._debug['tag']['start'] = self._io.pos()
                self.tag = KaitaiStream.resolve_enum(JavaClass.ConstantPoolEntry.TagEnum, self._io.read_u1())
                self._debug['tag']['end'] = self._io.pos()

            if (not (self.is_prev_two_entries)):
                pass
                self._debug['cp_info']['start'] = self._io.pos()
                _on = self.tag
                if _on == JavaClass.ConstantPoolEntry.TagEnum.class_type:
                    pass
                    self.cp_info = JavaClass.ClassCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.double:
                    pass
                    self.cp_info = JavaClass.DoubleCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.dynamic:
                    pass
                    self.cp_info = JavaClass.InvokeDynamicCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.field_ref:
                    pass
                    self.cp_info = JavaClass.FieldRefCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.float:
                    pass
                    self.cp_info = JavaClass.FloatCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.integer:
                    pass
                    self.cp_info = JavaClass.IntegerCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.interface_method_ref:
                    pass
                    self.cp_info = JavaClass.InterfaceMethodRefCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.invoke_dynamic:
                    pass
                    self.cp_info = JavaClass.InvokeDynamicCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.long:
                    pass
                    self.cp_info = JavaClass.LongCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.method_handle:
                    pass
                    self.cp_info = JavaClass.MethodHandleCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.method_ref:
                    pass
                    self.cp_info = JavaClass.MethodRefCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.method_type:
                    pass
                    self.cp_info = JavaClass.MethodTypeCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.module:
                    pass
                    self.cp_info = JavaClass.ClassCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.name_and_type:
                    pass
                    self.cp_info = JavaClass.NameAndTypeCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.package:
                    pass
                    self.cp_info = JavaClass.ClassCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.string:
                    pass
                    self.cp_info = JavaClass.StringCpInfo(self._io, self, self._root)
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.utf8:
                    pass
                    self.cp_info = JavaClass.Utf8CpInfo(self._io, self, self._root)
                self._debug['cp_info']['end'] = self._io.pos()



        def _fetch_instances(self):
            pass
            if (not (self.is_prev_two_entries)):
                pass

            if (not (self.is_prev_two_entries)):
                pass
                _on = self.tag
                if _on == JavaClass.ConstantPoolEntry.TagEnum.class_type:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.double:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.dynamic:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.field_ref:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.float:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.integer:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.interface_method_ref:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.invoke_dynamic:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.long:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.method_handle:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.method_ref:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.method_type:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.module:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.name_and_type:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.package:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.string:
                    pass
                    self.cp_info._fetch_instances()
                elif _on == JavaClass.ConstantPoolEntry.TagEnum.utf8:
                    pass
                    self.cp_info._fetch_instances()


        @property
        def is_two_entries(self):
            if hasattr(self, '_m_is_two_entries'):
                return self._m_is_two_entries

            self._m_is_two_entries = (False if self.is_prev_two_entries else  ((self.tag == JavaClass.ConstantPoolEntry.TagEnum.long) or (self.tag == JavaClass.ConstantPoolEntry.TagEnum.double)) )
            return getattr(self, '_m_is_two_entries', None)


    class DoubleCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.6
        """
        SEQ_FIELDS = ["value"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.DoubleCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_f8be()
            self._debug['value']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class FieldInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.5
        """
        SEQ_FIELDS = ["access_flags", "name_index", "descriptor_index", "attributes_count", "attributes"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.FieldInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['access_flags']['start'] = self._io.pos()
            self.access_flags = self._io.read_u2be()
            self._debug['access_flags']['end'] = self._io.pos()
            self._debug['name_index']['start'] = self._io.pos()
            self.name_index = self._io.read_u2be()
            self._debug['name_index']['end'] = self._io.pos()
            self._debug['descriptor_index']['start'] = self._io.pos()
            self.descriptor_index = self._io.read_u2be()
            self._debug['descriptor_index']['end'] = self._io.pos()
            self._debug['attributes_count']['start'] = self._io.pos()
            self.attributes_count = self._io.read_u2be()
            self._debug['attributes_count']['end'] = self._io.pos()
            self._debug['attributes']['start'] = self._io.pos()
            self._debug['attributes']['arr'] = []
            self.attributes = []
            for i in range(self.attributes_count):
                self._debug['attributes']['arr'].append({'start': self._io.pos()})
                self.attributes.append(JavaClass.AttributeInfo(self._io, self, self._root))
                self._debug['attributes']['arr'][i]['end'] = self._io.pos()

            self._debug['attributes']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.attributes)):
                pass
                self.attributes[i]._fetch_instances()


        @property
        def is_enum(self):
            if hasattr(self, '_m_is_enum'):
                return self._m_is_enum

            self._m_is_enum = self.access_flags & 16384 == 16384
            return getattr(self, '_m_is_enum', None)

        @property
        def is_final(self):
            if hasattr(self, '_m_is_final'):
                return self._m_is_final

            self._m_is_final = self.access_flags & 16 == 16
            return getattr(self, '_m_is_final', None)

        @property
        def is_private(self):
            if hasattr(self, '_m_is_private'):
                return self._m_is_private

            self._m_is_private = self.access_flags & 2 == 2
            return getattr(self, '_m_is_private', None)

        @property
        def is_protected(self):
            if hasattr(self, '_m_is_protected'):
                return self._m_is_protected

            self._m_is_protected = self.access_flags & 4 == 4
            return getattr(self, '_m_is_protected', None)

        @property
        def is_public(self):
            if hasattr(self, '_m_is_public'):
                return self._m_is_public

            self._m_is_public = self.access_flags & 1 == 1
            return getattr(self, '_m_is_public', None)

        @property
        def is_static(self):
            if hasattr(self, '_m_is_static'):
                return self._m_is_static

            self._m_is_static = self.access_flags & 8 == 8
            return getattr(self, '_m_is_static', None)

        @property
        def is_synthetic(self):
            if hasattr(self, '_m_is_synthetic'):
                return self._m_is_synthetic

            self._m_is_synthetic = self.access_flags & 4096 == 4096
            return getattr(self, '_m_is_synthetic', None)

        @property
        def is_transient(self):
            if hasattr(self, '_m_is_transient'):
                return self._m_is_transient

            self._m_is_transient = self.access_flags & 128 == 128
            return getattr(self, '_m_is_transient', None)

        @property
        def is_volatile(self):
            if hasattr(self, '_m_is_volatile'):
                return self._m_is_volatile

            self._m_is_volatile = self.access_flags & 64 == 64
            return getattr(self, '_m_is_volatile', None)

        @property
        def name_as_str(self):
            if hasattr(self, '_m_name_as_str'):
                return self._m_name_as_str

            self._m_name_as_str = self._root.constant_pool[self.name_index - 1].cp_info.value
            return getattr(self, '_m_name_as_str', None)


    class FieldRefCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.2
        """
        SEQ_FIELDS = ["class_index", "name_and_type_index"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.FieldRefCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['class_index']['start'] = self._io.pos()
            self.class_index = self._io.read_u2be()
            self._debug['class_index']['end'] = self._io.pos()
            self._debug['name_and_type_index']['start'] = self._io.pos()
            self.name_and_type_index = self._io.read_u2be()
            self._debug['name_and_type_index']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def class_as_info(self):
            if hasattr(self, '_m_class_as_info'):
                return self._m_class_as_info

            self._m_class_as_info = self._root.constant_pool[self.class_index - 1].cp_info
            return getattr(self, '_m_class_as_info', None)

        @property
        def name_and_type_as_info(self):
            if hasattr(self, '_m_name_and_type_as_info'):
                return self._m_name_and_type_as_info

            self._m_name_and_type_as_info = self._root.constant_pool[self.name_and_type_index - 1].cp_info
            return getattr(self, '_m_name_and_type_as_info', None)


    class FloatCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.5
        """
        SEQ_FIELDS = ["value"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.FloatCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_f4be()
            self._debug['value']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class IntegerCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.4
        """
        SEQ_FIELDS = ["value"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.IntegerCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_u4be()
            self._debug['value']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class InterfaceMethodRefCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.2
        """
        SEQ_FIELDS = ["class_index", "name_and_type_index"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.InterfaceMethodRefCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['class_index']['start'] = self._io.pos()
            self.class_index = self._io.read_u2be()
            self._debug['class_index']['end'] = self._io.pos()
            self._debug['name_and_type_index']['start'] = self._io.pos()
            self.name_and_type_index = self._io.read_u2be()
            self._debug['name_and_type_index']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def class_as_info(self):
            if hasattr(self, '_m_class_as_info'):
                return self._m_class_as_info

            self._m_class_as_info = self._root.constant_pool[self.class_index - 1].cp_info
            return getattr(self, '_m_class_as_info', None)

        @property
        def name_and_type_as_info(self):
            if hasattr(self, '_m_name_and_type_as_info'):
                return self._m_name_and_type_as_info

            self._m_name_and_type_as_info = self._root.constant_pool[self.name_and_type_index - 1].cp_info
            return getattr(self, '_m_name_and_type_as_info', None)


    class InvokeDynamicCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.10
        """
        SEQ_FIELDS = ["bootstrap_method_attr_index", "name_and_type_index"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.InvokeDynamicCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['bootstrap_method_attr_index']['start'] = self._io.pos()
            self.bootstrap_method_attr_index = self._io.read_u2be()
            self._debug['bootstrap_method_attr_index']['end'] = self._io.pos()
            self._debug['name_and_type_index']['start'] = self._io.pos()
            self.name_and_type_index = self._io.read_u2be()
            self._debug['name_and_type_index']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class LongCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.5
        """
        SEQ_FIELDS = ["value"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.LongCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['value']['start'] = self._io.pos()
            self.value = self._io.read_u8be()
            self._debug['value']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class MethodHandleCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.8
        """

        class ReferenceKindEnum(IntEnum):
            get_field = 1
            get_static = 2
            put_field = 3
            put_static = 4
            invoke_virtual = 5
            invoke_static = 6
            invoke_special = 7
            new_invoke_special = 8
            invoke_interface = 9
        SEQ_FIELDS = ["reference_kind", "reference_index"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.MethodHandleCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['reference_kind']['start'] = self._io.pos()
            self.reference_kind = KaitaiStream.resolve_enum(JavaClass.MethodHandleCpInfo.ReferenceKindEnum, self._io.read_u1())
            self._debug['reference_kind']['end'] = self._io.pos()
            self._debug['reference_index']['start'] = self._io.pos()
            self.reference_index = self._io.read_u2be()
            self._debug['reference_index']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class MethodInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.6
        """
        SEQ_FIELDS = ["access_flags", "name_index", "descriptor_index", "attributes_count", "attributes"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.MethodInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['access_flags']['start'] = self._io.pos()
            self.access_flags = self._io.read_u2be()
            self._debug['access_flags']['end'] = self._io.pos()
            self._debug['name_index']['start'] = self._io.pos()
            self.name_index = self._io.read_u2be()
            self._debug['name_index']['end'] = self._io.pos()
            self._debug['descriptor_index']['start'] = self._io.pos()
            self.descriptor_index = self._io.read_u2be()
            self._debug['descriptor_index']['end'] = self._io.pos()
            self._debug['attributes_count']['start'] = self._io.pos()
            self.attributes_count = self._io.read_u2be()
            self._debug['attributes_count']['end'] = self._io.pos()
            self._debug['attributes']['start'] = self._io.pos()
            self._debug['attributes']['arr'] = []
            self.attributes = []
            for i in range(self.attributes_count):
                self._debug['attributes']['arr'].append({'start': self._io.pos()})
                self.attributes.append(JavaClass.AttributeInfo(self._io, self, self._root))
                self._debug['attributes']['arr'][i]['end'] = self._io.pos()

            self._debug['attributes']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass
            for i in range(len(self.attributes)):
                pass
                self.attributes[i]._fetch_instances()


        @property
        def is_abstract(self):
            if hasattr(self, '_m_is_abstract'):
                return self._m_is_abstract

            self._m_is_abstract = self.access_flags & 1024 == 1024
            return getattr(self, '_m_is_abstract', None)

        @property
        def is_bridge(self):
            if hasattr(self, '_m_is_bridge'):
                return self._m_is_bridge

            self._m_is_bridge = self.access_flags & 64 == 64
            return getattr(self, '_m_is_bridge', None)

        @property
        def is_final(self):
            if hasattr(self, '_m_is_final'):
                return self._m_is_final

            self._m_is_final = self.access_flags & 16 == 16
            return getattr(self, '_m_is_final', None)

        @property
        def is_native(self):
            if hasattr(self, '_m_is_native'):
                return self._m_is_native

            self._m_is_native = self.access_flags & 256 == 256
            return getattr(self, '_m_is_native', None)

        @property
        def is_private(self):
            if hasattr(self, '_m_is_private'):
                return self._m_is_private

            self._m_is_private = self.access_flags & 2 == 2
            return getattr(self, '_m_is_private', None)

        @property
        def is_protected(self):
            if hasattr(self, '_m_is_protected'):
                return self._m_is_protected

            self._m_is_protected = self.access_flags & 4 == 4
            return getattr(self, '_m_is_protected', None)

        @property
        def is_public(self):
            if hasattr(self, '_m_is_public'):
                return self._m_is_public

            self._m_is_public = self.access_flags & 1 == 1
            return getattr(self, '_m_is_public', None)

        @property
        def is_static(self):
            if hasattr(self, '_m_is_static'):
                return self._m_is_static

            self._m_is_static = self.access_flags & 8 == 8
            return getattr(self, '_m_is_static', None)

        @property
        def is_strict(self):
            if hasattr(self, '_m_is_strict'):
                return self._m_is_strict

            self._m_is_strict = self.access_flags & 2048 == 2048
            return getattr(self, '_m_is_strict', None)

        @property
        def is_synchronized(self):
            if hasattr(self, '_m_is_synchronized'):
                return self._m_is_synchronized

            self._m_is_synchronized = self.access_flags & 32 == 32
            return getattr(self, '_m_is_synchronized', None)

        @property
        def is_synthetic(self):
            if hasattr(self, '_m_is_synthetic'):
                return self._m_is_synthetic

            self._m_is_synthetic = self.access_flags & 4096 == 4096
            return getattr(self, '_m_is_synthetic', None)

        @property
        def is_varargs(self):
            if hasattr(self, '_m_is_varargs'):
                return self._m_is_varargs

            self._m_is_varargs = self.access_flags & 128 == 128
            return getattr(self, '_m_is_varargs', None)

        @property
        def name_as_str(self):
            if hasattr(self, '_m_name_as_str'):
                return self._m_name_as_str

            self._m_name_as_str = self._root.constant_pool[self.name_index - 1].cp_info.value
            return getattr(self, '_m_name_as_str', None)


    class MethodRefCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.2
        """
        SEQ_FIELDS = ["class_index", "name_and_type_index"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.MethodRefCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['class_index']['start'] = self._io.pos()
            self.class_index = self._io.read_u2be()
            self._debug['class_index']['end'] = self._io.pos()
            self._debug['name_and_type_index']['start'] = self._io.pos()
            self.name_and_type_index = self._io.read_u2be()
            self._debug['name_and_type_index']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def class_as_info(self):
            if hasattr(self, '_m_class_as_info'):
                return self._m_class_as_info

            self._m_class_as_info = self._root.constant_pool[self.class_index - 1].cp_info
            return getattr(self, '_m_class_as_info', None)

        @property
        def name_and_type_as_info(self):
            if hasattr(self, '_m_name_and_type_as_info'):
                return self._m_name_and_type_as_info

            self._m_name_and_type_as_info = self._root.constant_pool[self.name_and_type_index - 1].cp_info
            return getattr(self, '_m_name_and_type_as_info', None)


    class MethodTypeCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.9
        """
        SEQ_FIELDS = ["descriptor_index"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.MethodTypeCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['descriptor_index']['start'] = self._io.pos()
            self.descriptor_index = self._io.read_u2be()
            self._debug['descriptor_index']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass


    class NameAndTypeCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.6
        """
        SEQ_FIELDS = ["name_index", "descriptor_index"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.NameAndTypeCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['name_index']['start'] = self._io.pos()
            self.name_index = self._io.read_u2be()
            self._debug['name_index']['end'] = self._io.pos()
            self._debug['descriptor_index']['start'] = self._io.pos()
            self.descriptor_index = self._io.read_u2be()
            self._debug['descriptor_index']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def descriptor_as_info(self):
            if hasattr(self, '_m_descriptor_as_info'):
                return self._m_descriptor_as_info

            self._m_descriptor_as_info = self._root.constant_pool[self.descriptor_index - 1].cp_info
            return getattr(self, '_m_descriptor_as_info', None)

        @property
        def descriptor_as_str(self):
            if hasattr(self, '_m_descriptor_as_str'):
                return self._m_descriptor_as_str

            self._m_descriptor_as_str = self.descriptor_as_info.value
            return getattr(self, '_m_descriptor_as_str', None)

        @property
        def name_as_info(self):
            if hasattr(self, '_m_name_as_info'):
                return self._m_name_as_info

            self._m_name_as_info = self._root.constant_pool[self.name_index - 1].cp_info
            return getattr(self, '_m_name_as_info', None)

        @property
        def name_as_str(self):
            if hasattr(self, '_m_name_as_str'):
                return self._m_name_as_str

            self._m_name_as_str = self.name_as_info.value
            return getattr(self, '_m_name_as_str', None)


    class StringCpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.3
        """
        SEQ_FIELDS = ["string_index"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.StringCpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['string_index']['start'] = self._io.pos()
            self.string_index = self._io.read_u2be()
            self._debug['string_index']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def name_as_str(self):
            if hasattr(self, '_m_name_as_str'):
                return self._m_name_as_str

            self._m_name_as_str = self.string_as_info.value
            return getattr(self, '_m_name_as_str', None)

        @property
        def string_as_info(self):
            if hasattr(self, '_m_string_as_info'):
                return self._m_string_as_info

            self._m_string_as_info = self._root.constant_pool[self.string_index - 1].cp_info
            return getattr(self, '_m_string_as_info', None)


    class Utf8CpInfo(KaitaiStruct):
        """
        .. seealso::
           Source - https://docs.oracle.com/javase/specs/jvms/se21/html/jvms-4.html#jvms-4.4.7
        """
        SEQ_FIELDS = ["str_len", "raw_value"]
        def __init__(self, _io, _parent=None, _root=None):
            super(JavaClass.Utf8CpInfo, self).__init__(_io)
            self._parent = _parent
            self._root = _root
            self._debug = collections.defaultdict(dict)
            self._read()

        def _read(self):
            self._debug['str_len']['start'] = self._io.pos()
            self.str_len = self._io.read_u2be()
            self._debug['str_len']['end'] = self._io.pos()
            self._debug['raw_value']['start'] = self._io.pos()
            self.raw_value = self._io.read_bytes(self.str_len)
            self._debug['raw_value']['end'] = self._io.pos()


        def _fetch_instances(self):
            pass

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value

            self._m_value = self.raw_value
            return getattr(self, '_m_value', None)


    @property
    def is_abstract(self):
        if hasattr(self, '_m_is_abstract'):
            return self._m_is_abstract

        self._m_is_abstract = self.access_flags & 1024 == 1024
        return getattr(self, '_m_is_abstract', None)

    @property
    def is_annotation(self):
        if hasattr(self, '_m_is_annotation'):
            return self._m_is_annotation

        self._m_is_annotation = self.access_flags & 8192 == 8192
        return getattr(self, '_m_is_annotation', None)

    @property
    def is_enum(self):
        if hasattr(self, '_m_is_enum'):
            return self._m_is_enum

        self._m_is_enum = self.access_flags & 16384 == 16384
        return getattr(self, '_m_is_enum', None)

    @property
    def is_final(self):
        if hasattr(self, '_m_is_final'):
            return self._m_is_final

        self._m_is_final = self.access_flags & 16 == 16
        return getattr(self, '_m_is_final', None)

    @property
    def is_interface(self):
        if hasattr(self, '_m_is_interface'):
            return self._m_is_interface

        self._m_is_interface = self.access_flags & 512 == 512
        return getattr(self, '_m_is_interface', None)

    @property
    def is_module(self):
        if hasattr(self, '_m_is_module'):
            return self._m_is_module

        self._m_is_module = self.access_flags & 32768 == 32768
        return getattr(self, '_m_is_module', None)

    @property
    def is_public(self):
        if hasattr(self, '_m_is_public'):
            return self._m_is_public

        self._m_is_public = self.access_flags & 1 == 1
        return getattr(self, '_m_is_public', None)

    @property
    def is_super(self):
        if hasattr(self, '_m_is_super'):
            return self._m_is_super

        self._m_is_super = self.access_flags & 32 == 32
        return getattr(self, '_m_is_super', None)

    @property
    def is_synthetic(self):
        if hasattr(self, '_m_is_synthetic'):
            return self._m_is_synthetic

        self._m_is_synthetic = self.access_flags & 4096 == 4096
        return getattr(self, '_m_is_synthetic', None)


