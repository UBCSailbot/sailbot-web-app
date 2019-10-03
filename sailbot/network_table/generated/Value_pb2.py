# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Value.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Value.proto',
  package='NetworkTable',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bValue.proto\x12\x0cNetworkTable\"\xd0\x01\n\x05Value\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.NetworkTable.Value.Type\x12\x13\n\x0b\x64ouble_data\x18\x02 \x01(\x01\x12\x11\n\tbool_data\x18\x03 \x01(\x08\x12\x10\n\x08int_data\x18\x04 \x01(\x05\x12\x13\n\x0bstring_data\x18\x05 \x01(\t\x12\x12\n\nbytes_data\x18\x06 \x01(\x0c\"<\n\x04Type\x12\n\n\x06\x44OUBLE\x10\x00\x12\x08\n\x04\x42OOL\x10\x01\x12\x07\n\x03INT\x10\x02\x12\n\n\x06STRING\x10\x03\x12\t\n\x05\x42YTES\x10\x04\x62\x06proto3')
)



_VALUE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='NetworkTable.Value.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BYTES', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=178,
  serialized_end=238,
)
_sym_db.RegisterEnumDescriptor(_VALUE_TYPE)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='NetworkTable.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='NetworkTable.Value.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_data', full_name='NetworkTable.Value.double_data', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bool_data', full_name='NetworkTable.Value.bool_data', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='int_data', full_name='NetworkTable.Value.int_data', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_data', full_name='NetworkTable.Value.string_data', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_data', full_name='NetworkTable.Value.bytes_data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _VALUE_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=238,
)

_VALUE.fields_by_name['type'].enum_type = _VALUE_TYPE
_VALUE_TYPE.containing_type = _VALUE
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), {
  'DESCRIPTOR' : _VALUE,
  '__module__' : 'Value_pb2'
  # @@protoc_insertion_point(class_scope:NetworkTable.Value)
  })
_sym_db.RegisterMessage(Value)


# @@protoc_insertion_point(module_scope)
